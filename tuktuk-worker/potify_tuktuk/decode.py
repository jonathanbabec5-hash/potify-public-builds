"""Decode top-level RunTaskV0 instructions and their committed payouts."""
import hashlib
import re

PROGRAM = "tuktukUrfhXT6ZT77QTU8RQtvgL967uRuVagWF57zVA"
COMPUTE_BUDGET = "ComputeBudget111111111111111111111111111111"
ED25519 = "Ed25519SigVerify111111111111111111111111111"
ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
RUN = hashlib.sha256(b"global:run_task_v0").digest()[:8]
INVOKE = re.compile(r"Program (\w+) invoke \[(\d+)\]")
END = re.compile(r"Program (\w+) (success|failed:.*)")
PAYOUT = re.compile(r"Program log: Paying out reward (\d+)")


def unbase58(value):
    number = 0
    for char in value:
        number = number * 58 + ALPHABET.index(char)
    zeros = len(value) - len(value.lstrip("1"))
    return bytes(zeros) + number.to_bytes((number.bit_length() + 7) // 8, "big")


def payment_logs(logs):
    """Get one record per outer TukTuk invocation. Ignore nested program output."""
    stack, frames = [], []
    for line in logs or []:
        start = INVOKE.fullmatch(line)
        if start:
            program, level = start.groups()
            if int(level) != len(stack) + 1:
                return []
            if not stack and program == PROGRAM:
                frames.append({"amounts": [], "closed": False, "run": False})
            stack.append(program)
            continue
        end = END.fullmatch(line)
        if end:
            if not stack or stack[-1] != end[1]:
                return []
            if stack == [PROGRAM]:
                frames[-1]["closed"] = end[2] == "success"
            stack.pop()
            continue
        if stack == [PROGRAM]:
            if line == "Program log: Instruction: RunTaskV0":
                frames[-1]["run"] = True
            amount = PAYOUT.fullmatch(line)
            if amount:
                frames[-1]["amounts"].append(int(amount[1]))
    return frames


def address(keys, index):
    if type(index) is not int or index < 0 or index >= len(keys):
        raise ValueError("account index outside message")
    return keys[index]


def decode(signature, tx):
    if not tx or tx.get("meta") is None:
        return {"signature": signature, "status": "unavailable"}
    if tx["transaction"]["signatures"][0] != signature:
        raise ValueError("RPC returned a different signature")
    meta = tx["meta"]
    msg = tx["transaction"]["message"]
    loaded = meta.get("loadedAddresses") or {}
    keys = msg["accountKeys"] + loaded.get("writable", []) + loaded.get("readonly", [])
    fee = meta["fee"]
    frames = payment_logs(meta.get("logMessages"))
    failed = meta["err"] is not None
    runs, outer_count, simple = [], 0, True
    for ix in msg["instructions"]:
        program = address(keys, ix["programIdIndex"])
        if program != PROGRAM:
            simple &= program in (COMPUTE_BUDGET, ED25519)
            continue
        frame_pos = outer_count
        outer_count += 1
        if not unbase58(ix["data"]).startswith(RUN):
            simple = False
            continue
        accounts = ix["accounts"]
        worker, queue, task = [address(keys, accounts[i]) for i in (0, 2, 3)]
        reward = 0 if failed else None
        if not failed and frame_pos < len(frames):
            frame = frames[frame_pos]
            if frame["closed"] and frame["run"] and len(frame["amounts"]) == 1:
                reward = frame["amounts"][0]
        runs.append(dict(worker=worker, queue=queue, task=task, reward_lamports=reward))
    if not failed and len(frames) != outer_count:
        for run in runs:
            run["reward_lamports"] = None
    status = ("failed" if failed else "completed") if runs else "other"
    # The payer can sponsor another worker, receive returned rent, or pay unrelated fees.
    # Admit a transaction to the break-even model only if the balance also reconciles.
    net = None
    if status == "completed" and simple and len(runs) == 1 and runs[0]["worker"] == keys[0]:
        reward = runs[0]["reward_lamports"]
        delta = meta["postBalances"][0] - meta["preBalances"][0]
        if reward is not None and reward - fee == delta:
            net = delta
    return dict(signature=signature, slot=tx["slot"], block_time=tx.get("blockTime"),
                status=status, payer=keys[0], fee_lamports=fee,
                reconciled_win_net_lamports=net, runs=runs)

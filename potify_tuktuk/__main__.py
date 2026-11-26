"""Sample settled TukTuk jobs, verify a sample or model an operator's costs."""
import argparse
import json
import math
import os
import sys
import tempfile
from pathlib import Path

from .decode import PROGRAM, unbase58
from .report import break_even, summarize
from .rpc import Client, MAINNET, ReadError, collect

from .window import select_window

PUBLIC_RPC = "https://api.mainnet-beta.solana.com"


def signature_arg(value):
    try:
        if not 64 <= len(value) <= 88 or len(unbase58(value)) != 64:
            raise ValueError()
    except ValueError:
        raise argparse.ArgumentTypeError("expected a Solana transaction signature") from None
    return value


def make_sample(rows):
    return dict(schema=1, cluster=MAINNET, program=PROGRAM,
                summary=summarize(rows), transactions=rows)


def read_sample(path):
    sample = json.loads(path.read_text())
    if (sample.get("schema"), sample.get("cluster"), sample.get("program")) != (1, MAINNET, PROGRAM):
        raise ValueError("Unexpected sample format, cluster or program")
    signatures = [signature_arg(row["signature"]) for row in sample["transactions"]]
    if len(set(signatures)) != len(signatures):
        raise ValueError("Sample has duplicate signatures")
    return sample


def write_result(data, path):
    text = json.dumps(data, indent=2) + "\n"
    if path is None:
        print(text, end="")
        return
    with tempfile.NamedTemporaryFile("w", dir=path.parent, delete=False) as output:
        try:
            output.write(text)
            output.flush()
            os.replace(output.name, path)
        finally:
            Path(output.name).unlink(missing_ok=True)


def run(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    scan = commands.add_parser("scan", help="Read a page of finalized program signatures")
    scan.add_argument("--limit", type=int, default=24)
    scan.add_argument("--hours", type=int, help="Draw the sample across this many hours (1 to 168)")
    scan.add_argument("--seed", type=int, default=42, help="Seed for a stratified window sample")
    scan.add_argument("--before", type=signature_arg, help="Exclusive signature for older pages")
    verify = commands.add_parser("verify", help="Refetch every signature and compare decoded fields")
    verify.add_argument("sample", type=Path)
    for cmd in [scan, verify]:
        cmd.add_argument("--pause", type=float, default=0.4, help="Seconds between transaction reads")
    scan.add_argument("--out", type=Path, help="Write the machine-readable sample to a file")
    model = commands.add_parser("model", help="Calculate break-even using a reconciled sample")
    model.add_argument("sample", type=Path)
    model.add_argument("--failed-fee-lamports", type=int, required=True)
    model.add_argument("--attempts-per-day", type=int, required=True)
    model.add_argument("--daily-cost-lamports", type=int, required=True)
    args = parser.parse_args(argv)
    if args.command == "model":
        sample = read_sample(args.sample)
        write_result(break_even(summarize(sample["transactions"]), args.failed_fee_lamports,
                                args.attempts_per_day, args.daily_cost_lamports), None)
        return 0
    if not math.isfinite(args.pause) or args.pause < 0:
        parser.error("--pause must be finite and nonnegative")
    if args.command == "scan" and not 1 <= args.limit <= 1000:
        parser.error("--limit must be between 1 and 1000")
    if args.command == "scan" and args.hours is not None:
        if not 1 <= args.hours <= 168 or args.before:
            parser.error("--hours requires 1 to 168 hours and cannot be combined with --before")
    client = Client(os.environ.get("SOLANA_RPC_URL") or PUBLIC_RPC)
    client.mainnet()
    if args.command == "scan":
        if args.hours:
            signatures, selection = select_window(client, args.hours, args.limit, args.seed)
        else:
            signatures = [row["signature"] for row in client.page(args.limit, args.before)]
            selection = None
        result = make_sample(collect(client, signatures, args.pause))
        if selection:
            result["selection"] = selection
        write_result(result, args.out)
        if args.out:
            write_result(result["summary"], None)
        return 2 if result["summary"]["statuses"].get("unavailable") else 0
    previous = read_sample(args.sample)
    signatures = [row["signature"] for row in previous["transactions"]]
    current = make_sample(collect(client, signatures, args.pause))
    if current["summary"]["statuses"].get("unavailable") or not signatures:
        print("Verification incomplete.", file=sys.stderr)
        return 2
    # Sampling metadata describes the original signature crawl. Verify only the
    # individual transactions and their recalculated totals here.
    if current != {k: v for k, v in previous.items() if k != "selection"}:
        print("The stored sample differs from the finalized RPC data.", file=sys.stderr)
        return 1
    print(f"Verified {len(signatures)} finalized transactions and their totals.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except (OSError, ReadError, ValueError, KeyError, TypeError, argparse.ArgumentTypeError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)

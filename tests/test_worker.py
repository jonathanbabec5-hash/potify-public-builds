import contextlib
import copy
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from potify_tuktuk.__main__ import make_sample, read_sample, run, write_result
from potify_tuktuk.decode import PROGRAM, decode, payment_logs
from potify_tuktuk.report import break_even, summarize
from potify_tuktuk.rpc import Client, ReadError, collect
from potify_tuktuk.window import select_window

DATA = json.loads((Path(__file__).parent / "fixtures" / "run.json").read_text())
SIG = DATA["transaction"]["signatures"][0]


class DecoderTests(unittest.TestCase):
    def setUp(self):
        self.tx = copy.deepcopy(DATA)
        self.meta = self.tx["meta"]
        self.msg = self.tx["transaction"]["message"]
        self.ix = self.msg["instructions"][-1]

    def row(self):
        return decode(SIG, self.tx)

    def test_real_versioned_transaction(self):
        row = self.row()
        self.assertEqual(row["slot"], 474307594)
        self.assertEqual(row["runs"][0]["worker"], "BcS9rqkjquBDyi1faYqWYaLfW2Pc9fAXuBxoDHKYdYRM")
        self.assertEqual(row["runs"][0]["reward_lamports"], 15000)
        self.assertEqual(row["reconciled_win_net_lamports"], 4828)

    def test_lookup_table_account_indices(self):
        self.ix["accounts"][2] = len(self.msg["accountKeys"])
        loaded = self.meta["loadedAddresses"]
        self.assertEqual(self.row()["runs"][0]["queue"], (loaded["writable"] + loaded["readonly"])[0])

    def test_failed_bundle_rolls_back_logged_payments(self):
        self.meta["err"] = {"InstructionError": [3, "Custom"]}
        row = self.row()
        self.assertEqual(row["status"], "failed")
        self.assertEqual(row["runs"][0]["reward_lamports"], 0)
        self.assertEqual(summarize([row])["fees_on_failed_run_transactions_lamports"], self.meta["fee"])

    def test_cpi_message_cannot_claim_payout(self):
        logs = [f"Program {PROGRAM} invoke [1]", "Program log: Instruction: RunTaskV0",
                "Program Dummy invoke [2]", "Program log: Paying out reward 9000",
                "Program Dummy success", "Program log: Paying out reward 17", f"Program {PROGRAM} success"]
        self.assertEqual(payment_logs(logs)[0]["amounts"], [17])
        self.meta["logMessages"] = logs[:-2]
        self.assertIsNone(self.row()["runs"][0]["reward_lamports"])

    def test_missing_logs_do_not_turn_into_zero_reward(self):
        self.meta["logMessages"] = None
        s = summarize([self.row()])
        self.assertEqual((s["completed_jobs"], s["jobs_with_verified_payout"]), (1, 0))

    def test_batched_jobs_count_once_per_job(self):
        self.msg["instructions"].append(copy.deepcopy(self.ix))
        self.meta["logMessages"] *= 2
        s = summarize([self.row()])
        self.assertEqual((s["completed_jobs"], s["verified_rewards_lamports"]), (2, 30000))
        self.assertEqual(s["reconciled_single_wins"], 0)

    def test_sponsored_and_mixed_balance_changes(self):
        self.meta["postBalances"][0] += 100
        self.assertIsNone(self.row()["reconciled_win_net_lamports"])
        self.ix["accounts"][0] = 1
        row = self.row()
        self.assertNotEqual(row["payer"], row["runs"][0]["worker"])
        self.assertIsNone(row["reconciled_win_net_lamports"])

    def test_non_run_and_bad_index(self):
        self.ix["data"] = "11"
        self.assertEqual(self.row()["status"], "other")
        self.ix["programIdIndex"] = -1
        with self.assertRaises(ValueError):
            self.row()

    def test_missing_and_wrong_signature(self):
        self.assertEqual(decode(SIG, None)["status"], "unavailable")
        with self.assertRaises(ValueError):
            decode("wrong", self.tx)


class WorkflowTests(unittest.TestCase):
    def test_replay_and_offline_model(self):
        sample = make_sample([decode(SIG, DATA)])
        with tempfile.TemporaryDirectory() as tmp:
            file = Path(tmp) / "sample.json"
            write_result(sample, file)
            self.assertEqual(read_sample(file), sample)
            with patch("potify_tuktuk.__main__.Client") as client, contextlib.redirect_stdout(io.StringIO()):
                client.return_value.transaction.return_value = DATA
                self.assertEqual(run(["verify", str(file), "--pause", "0"]), 0)
                self.assertEqual(run(["model", str(file), "--failed-fee-lamports", "5000",
                                      "--attempts-per-day", "1", "--daily-cost-lamports", "0"]), 0)
                sample["summary"]["completed_jobs"] += 1
                write_result(sample, file)
                with contextlib.redirect_stderr(io.StringIO()):
                    self.assertEqual(run(["verify", str(file)]), 1)

    def test_break_even_and_infeasible(self):
        s = {"reconciled_single_wins": 2, "reconciled_net_lamports": 12000}
        self.assertEqual(break_even(s, 6000, 10, 0)["required_win_percent"], 50)
        self.assertEqual(break_even(s, 6000, 10, 30000)["required_win_percent"], 75)
        self.assertFalse(break_even(s, 6000, 10, 70000)["can_break_even"])
        with self.assertRaises(ValueError):
            break_even(summarize([]), 0, 1, 0)

    def test_failed_reads_are_counted_and_duplicates_removed(self):
        rpc = Mock()
        rpc.transaction.side_effect = ReadError("busy")
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(collect(rpc, [SIG, SIG], 0), [{"signature": SIG, "status": "unavailable"}])
        rpc.transaction.assert_called_once()

    def test_requires_full_genesis_hash(self):
        rpc = Client("https://example.invalid")
        with patch.object(rpc, "call", return_value="5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp"):
            with self.assertRaises(ReadError):
                rpc.mainnet()

    def test_stratified_window_and_exclusive_start(self):
        page = [{"signature": str(t), "blockTime": t} for t in (7500, 7000, 6500, 6000, 5500, 3900, 3800)]
        client = Mock()
        client.page.return_value = page
        chosen, plan = select_window(client, 1, 2, 42)
        self.assertEqual(plan["program_signatures"], 5)
        self.assertEqual(plan["start_exclusive"], 3900)
        self.assertIn(chosen[0], ["7500", "7000"])
        self.assertIn(chosen[1], ["6500", "6000", "5500"])

    def test_window_history_gap(self):
        client = Mock()
        client.page.side_effect = [[{"signature": SIG, "blockTime": 8000}], []]
        with self.assertRaises(ReadError):
            select_window(client, 1, 2, 42)


if __name__ == "__main__":
    unittest.main()

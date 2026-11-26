"""Aggregate finalized observations. A win belongs to the signer of RunTaskV0."""
from collections import Counter
from fractions import Fraction


def summarize(rows):
    statuses = Counter(row["status"] for row in rows)
    winners, payouts, fees_lost, net = Counter(), [], 0, []
    for row in rows:
        if row["status"] == "failed":
            fees_lost += row["fee_lamports"]
        if row["status"] != "completed":
            continue
        for run in row["runs"]:
            winners[run["worker"]] += 1
            if run["reward_lamports"] is not None:
                payouts.append(run["reward_lamports"])
        if row["reconciled_win_net_lamports"] is not None:
            net.append(row["reconciled_win_net_lamports"])
    times = [row["block_time"] for row in rows if row.get("block_time") is not None]
    return dict(sample_transactions=len(rows), statuses=dict(statuses),
                first_block_time=min(times, default=None), last_block_time=max(times, default=None),
                completed_jobs=sum(winners.values()), jobs_with_verified_payout=len(payouts),
                verified_rewards_lamports=sum(payouts), completed_jobs_by_worker=dict(winners.most_common()),
                fees_on_failed_run_transactions_lamports=fees_lost,
                reconciled_single_wins=len(net), reconciled_net_lamports=sum(net),
                lowest_reconciled_net_lamports=min(net, default=None),
                highest_reconciled_net_lamports=max(net, default=None))


def break_even(summary, failed_fee, attempts, daily_cost):
    if failed_fee < 0 or daily_cost < 0 or attempts <= 0:
        raise ValueError("costs must be nonnegative and attempts must be positive")
    count = summary["reconciled_single_wins"]
    if not count:
        raise ValueError("No fully reconciled single-job wins to model")
    win_net = Fraction(summary["reconciled_net_lamports"], count)
    cost_per_attempt = Fraction(daily_cost, attempts)
    possible = win_net >= cost_per_attempt
    if not possible:
        percent = None
    elif cost_per_attempt + failed_fee == 0:
        percent = 0.0
    else:
        percent = float(100 * (cost_per_attempt + failed_fee) / (win_net + failed_fee))
    return dict(assumed_failed_fee_lamports=failed_fee, assumed_attempts_per_day=attempts,
                assumed_daily_cost_lamports=daily_cost, mean_win_net_lamports=float(win_net),
                can_break_even=possible, required_win_percent=percent)

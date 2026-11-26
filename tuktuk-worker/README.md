# POTIFY TukTuk worker

[Complete project directory](docs/DIRECTORY.md) · [Technical whitepaper](docs/WHITEPAPER.md) · [Marketing and sales plan](docs/MARKETING.md)

An application posts a scheduled job to a TukTuk queue and funds a reward. Independent workers compete to execute it on Solana. The successful worker receives SOL in the same transaction. This gives POTIFY a place to find paid work without signing up each application as a customer. The identity of the software that requested a job is generally unknown.

[Mainnet results](examples/RESULTS.md) · [Full-day sample](examples/day.json) · [Consecutive transactions](examples/mainnet.json) · [Upstream protocol](https://github.com/helium/tuktuk)

## Run the observer

From the repository root, enter the directory below. Python 3.10+ and access to a Solana JSON-RPC endpoint are the only requirements. Reading the examples and running the cost model work offline.

```sh
cd tuktuk-worker
python3 -m unittest discover -s tests -v
python3 -m potify_tuktuk scan --limit 24 --out sample.json
python3 -m potify_tuktuk scan --hours 24 --limit 32 --out day.json
python3 -m potify_tuktuk verify examples/day.json
python3 -m potify_tuktuk model examples/day.json --failed-fee-lamports 5000 --daily-cost-lamports 0 --attempts-per-day 100
```

Set `SOLANA_RPC_URL` to use a different endpoint. Reads require transaction history and verify the mainnet genesis hash. Network fees are zero for the observer. An RPC or hosting provider may charge for its services. On a rate limit or unavailable transaction, the observer retries, marks missing records and exits with a nonzero status. For older consecutive pages pass the final signature of the previous page to `scan --before`.

Once the workflow is on the default branch, a GitHub user can open **Actions → POTIFY TukTuk observer → Run workflow** from a phone. A manual run tests the code and makes a downloadable JSON sample. Pull requests run the offline tests. The workflow needs no wallet or secrets. Agents can read the committed JSON directly or consume the CLI's JSON output.

## What the numbers mean

- A recognized job is an outer `RunTaskV0` instruction for the TukTuk program. The signer account in that instruction is the worker. One transaction can contain several jobs. An instruction that calls TukTuk only through another program is outside this decoder's coverage.
- A verified reward comes from a completed transaction with an unambiguous payout logged inside that outer TukTuk invocation. Unavailable logs yield an unknown amount. Failed transactions roll back their job payouts. The fee payer may still incur a fee.
- A win enters the cost model if it contains one job, the signer pays the fee, the other outer instructions are budget or Ed25519 verification, and the signer's balance increases by exactly the payout minus the network fee (a negative change is possible). Sponsored executions, rent changes or bundled transfers can make other transactions unsuitable.
- In a time-window scan the tool first pages through program signatures, splits them into equal-count chronological groups, and samples one signature per group using a seed. The full signature count measures program activity. Only decoded transactions establish paid work. `verify` refetches the saved signatures and recalculates transaction fields and totals. The window metadata records the original crawl.
- Break-even uses the mean reconciled win, an assumed fee for a landed failure, daily hosting/RPC costs and attempts per day. At a win probability of `p`, expected net per attempt is `p × mean_win_net − (1 − p) × failed_fee − daily_cost / attempts`. Units are lamports, with one billion lamports per SOL. For a mix of fee-charging and uncharged losses, enter their average cost. The chain cannot reveal every competing attempt that never landed. Observed market share and a newcomer's win probability answer different questions.

## Operate the worker

The settlement implementation is Helium's pinned TukTuk crank turner 0.2.31. The optional [Docker Compose profile](operator/compose.yaml) runs that executable on a Linux/amd64 host. It watches existing queues and sends signed transactions. Jobs pay the crank-turner signer directly. Queue creation and its deposit are unnecessary for this role.

The operator supplies a **dedicated, limited-balance Solana keypair** from the host and an RPC endpoint with working WebSocket subscriptions. Keep any treasury key or recovery phrase out of this repository and out of GitHub Actions. The amount available to a continuously running signer can be consumed by failed attempts. The fee settings apply to individual work and do not enforce a daily budget.

```sh
# Set SOLANA_RPC_URL and POTIFY_WORKER_KEYPAIR_FILE in the operator's environment.
# Validate the configuration without starting a worker.
docker compose -f operator/compose.yaml --profile operator config --quiet

# Start a signing worker in the foreground. This can spend SOL.
docker compose -f operator/compose.yaml --profile operator up worker
```

Stop the foreground worker with Ctrl-C. Its service has no restart policy. The example requests a 15,000-lamport minimum reward, configures a 12,000-lamport fee ceiling and disables extra application retries and re-signs. Review [the configuration](operator/config.toml) against current fee conditions. A live trial would require its own record of attempts, paid wins, failed fees, RPC cost and hosting cost to establish POTIFY's net earnings.

## Files

```text
tuktuk-worker/
  README.md
  .gitignore
  requirements.txt
  potify_tuktuk/
    __init__.py
    __main__.py
    decode.py
    report.py
    rpc.py
    window.py
  operator/
    compose.yaml
    config.toml
  examples/
    RESULTS.md
    day.json
    mainnet.json
  tests/
    fixtures/run.json
    test_worker.py
```

The root workflow is at [potify-tuktuk.yml](../.github/workflows/potify-tuktuk.yml). The decoder follows the [on-chain account order and payout code](https://github.com/helium/tuktuk/blob/014ae27e567b472d3911bd3156340571d5d485a7/solana-programs/programs/tuktuk/src/instructions/run_task_v0.rs).

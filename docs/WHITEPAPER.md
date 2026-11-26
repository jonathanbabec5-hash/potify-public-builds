# Can a public job queue pay for the work of watching it?

A Solana application can fund a scheduled job. An independent worker can compete to execute it. POTIFY’s observer answers a narrower, measurable question. For a transaction in a public sample, can another developer reconstruct the job reward, identify the fee payer and reconcile the fee from the record?

## What a developer can reproduce

The observer reads finalized transactions, recognizes the supported outer run instruction and uses its invocation logs to identify a payout. Some transactions execute several jobs. Keep the transaction count, the job count and the count of individually reconciled wins separate. An ambiguous or missing payout should stay unknown. The CLI can replay the recorded samples and vary the assumed loss and operating costs in its model. [Decoder](../potify_tuktuk/decode.py) · [Offline tests](../tests/test_worker.py)

## What the sample shows

The published November 25–26 sample selected 32 transactions from a 24-hour window. It contains 32 paid jobs across 31 successful transactions and one failed transaction with a fee. The job winners were two observed worker addresses. POTIFY earned zero SOL from the observation. Supply in another window, a new operator’s win rate and its full operating cost remain open. [Sample and method](../examples/RESULTS.md)

## Acceptance

Run the offline tests from the worker directory. Pick one transaction from the saved examples. Explain which instruction, log and fee support the result. Record an unknown when the information cannot be reconciled. The read-only observer and the optional signing operator have separate entry points and acceptance criteria. The developer demo needs only the observer.

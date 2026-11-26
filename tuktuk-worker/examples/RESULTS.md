# What an existing TukTuk queue paid

Observed on Solana mainnet-beta, November 25–26, 2026. Each signature in the examples can be checked with the observer or opened in Solana Explorer.

## A 24-hour window

From November 25 at 5:03:32 p.m. through November 26 at 5:03:32 p.m. Eastern, the observer counted **9,723 finalized transactions mentioning the program**. It divided the signatures into 32 groups in time order and selected one per group using seed 42. The 32 selected transactions included 31 successes and one failure. One success ran two jobs.

| Observed metric | Result |
| --- | ---: |
| Completed jobs with a verified payout | 32 |
| Distinct queues among those jobs | 1 |
| Gross reward per job | 15,000 lamports |
| Total gross rewards in the sample | 480,000 lamports |
| Jobs won by the two observed worker addresses | 29 and 3 |
| Reconciled, single-job wins | 30 |
| Mean SOL retained per reconciled win after its network fee | 0.0000061976 SOL |
| Range across those wins | 4,260–9,730 lamports |
| Network fee paid on the one failed transaction | 5,934 lamports |

At that mean, **1,000 wins would retain about 0.0062 SOL** before failed attempts, hosting and RPC costs. Holding the win amount fixed and assuming each loss costs the observed 5,934 lamports, a worker would need to win **48.9% of its own attempts** to cover transaction fees with free hosting and RPC. The single failed observation does not establish an average loss. An unlanded attempt can have a different cost. Neither the number of available future jobs nor POTIFY's achievable win rate is measured here.

The verified result establishes real paid traffic and competition. POTIFY earned zero SOL in this test. The sample alone gives no reason to pay for a host or a private RPC plan.

[Sample and selection metadata](day.json) · [Example payout](https://explorer.solana.com/tx/5Rer1RgtnxrFZbCypTjqDZmgtRXBKXRxtaWioZkaNRadtnewdktnwbZaG4oT9WWGDSRCEG7HN6R7e8fKgWPsufup) · [Failed transaction](https://explorer.solana.com/tx/5wjki4YmGnAXVeXLfo1n3ZNgHSySCAPxSDUNhogebSFMBHMPpnfX2Fz623V3qUCdNQFZXzxVXas7vsxq4Xm21uEs) · [Two jobs in one transaction](https://explorer.solana.com/tx/5odVC1Rp5ZiyigTCRr1QKv2TckBMyEAKMoRD6d3F7EpCNAufUpjYskitEXyZhKR6vcuF5FxstUNAD3VU8hrpfGbz)

## Consecutive transactions

On November 26 from 4:51:44 p.m. to 4:59:43 p.m. Eastern, 24 consecutive transactions each executed one job. One wallet won all 24. It received 360,000 lamports in gross rewards, paid 190,370 lamports in network fees and retained 169,630 lamports. This short interval falls inside the 24-hour window, so the two samples should be interpreted separately. [Consecutive sample](mainnet.json)

## Repeat the calculation

From the `tuktuk-worker` directory, run the following commands.

```sh
python3 -m potify_tuktuk verify examples/day.json
python3 -m potify_tuktuk model examples/day.json --failed-fee-lamports 5934 --attempts-per-day 100 --daily-cost-lamports 0
```

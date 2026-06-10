# NFRA_COSTAWS incident cost-attribution — GLOBGRPH Item-2b 409 storm (2026-06-09/10)

**Author:** 0.7.0_AE_CloudOps (Andrew-direct via MSTR dispatch 20260610T193143Z; metrics figures = MSTR CloudWatch pull)
**Incident fix:** `2ce19eaee` (globgrph-v0.1.7) — NFRA_GLOBGRPH ITEM-2B, RAVC2-ACCEPTED 20260610T1832Z
**Cross-refs:** `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/NFRA_GLOBGRPH.ITEM-2B.ae-incremental-updater.md` (full root-cause record); scorecard `docs/architecture/NFRA_COSTRED_SCORECARD.md` (COO folds this line into the ledger)

## What burned

`opal-globgrph-incremental-updater` (Lambda, 512MB) thrashed for ~21h
(06-09T~21Z -> 06-10T~18Z): every batch hit Nessie 409 commit conflicts
(per-ARN delete loop = N+1 commits/batch x uncapped ESM concurrency), the
handler failed the whole batch, SQS redelivered, repeat to DLQ.

## Incident cost (CloudWatch-grounded, incident window 06-09 -> 06-10)

| Component | Figure | Cost |
|---|---|---|
| Lambda invocations | 11,365 | ~$0.002 (requests, negligible) |
| Lambda duration | 1,533,359,904 ms (~135s avg/invocation vs the 180s timeout) | — |
| Lambda GB-seconds | 766,680 (0.5 GB x 1,533,360 s) | **~$12.78** |
| SQS | ~1,019,238 main-queue NumberOfMessagesReceived + sends + DLQ | ~$1-2 |
| Nessie backend commit-retries (Fargate/DynamoDB) | not separately metered | low single $ |
| **TOTAL** | | **~$14-16, Lambda-dominated** |

## Framing (chronic-leak class)

- Burn rate ~**$0.61/hr** (Lambda alone). Ran **silently ~21h** (~$13).
- 7-day projection if unnoticed: **~$100+** — exactly the chronic-leak class
  NFRA_COSTAWS targets.
- Found at hour-21 ONLY via the LD-0177 TO-file discipline (the ITEM-2B pull
  tried to ship the updater and found it already live and failing) ->
  concrete same-day ROI on the structural TO-queue fix.

## Burn-stop evidence

- **Fix:** v0.1.7 = ESM `maximum_concurrency=2` + single-commit
  overwrite-with-filter upsert + reload-per-attempt retry. Deployed
  2026-06-10T18:11:51Z (0-diff, live sha verified).
- **Early (same-evening) metrics:** post-deploy 18:12->19:12Z = 40
  invocations, 77.1s total duration (~1.9s avg, includes one deliberate
  12.4s smoke) vs ~135s avg during the storm. Burn ~38.5 GB-s/hr
  (~$0.0006/hr) vs ~$0.61/hr — **~1000x reduction, burn stopped**.
- **Formal confirm (tomorrow, per dispatch action 2):** billing/CE Lambda
  GB-s for the function near-zero for the post-18:11Z window; RAVC2 to COO
  with the figure alongside the 02:00Z triple-fix artifact review.

## DLQ metric reconciliation (MSTR note resolved)

MSTR's `NumberOfMessagesSent` pull on the DLQ returned 0; the **298,351**
figure COO cited came from my `sqs get-queue-attributes
ApproximateNumberOfMessages` read on the DLQ at 18:0xZ — i.e. queue DEPTH
(visible-message count attribute), not the Sent metric. Both can be true:
EventBridge->SQS redrive deliveries do not emit `NumberOfMessagesSent` the
way producer SendMessage does (redrive moves are not client sends). Depth
was real; disposition = natural 24h expiry (COO-ratified 1832Z), gone by
~06-11T12Z. Cost driver is the 1.02M main-queue throughput regardless.

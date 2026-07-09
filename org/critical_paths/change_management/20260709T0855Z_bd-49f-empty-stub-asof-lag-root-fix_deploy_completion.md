# Deploy Completion Record
**Date opened:** 2026-07-09T08:55:22.049731+00:00
**Status:** OPEN
**Deploy:** ADVI_BDAPIMIG: 49F frozen-AUA ROOT fix -- snapshot as-of lag (BD_SNAPSHOT_ASOF_LAG_BDAYS=1) + content-grounded empty-stub guards in the shared bronze pull (CTO GO 083650Z)
**Authored by:** 0.6.0_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | commit + push CLOUD (bronze script + runner + TF + tests) | hash pushed |  | OPEN |
| L2 | s3-prefix | upload shared cot_bronze_ingest.py -> s3://opal-data-bd/code/bronze/ (runner pulls at runtime; bd plane ONLY, cot copy deliberately NOT touched) | ETag matches local md5; head-object confirms |  | OPEN |
| L3 | tf-lambda | safe-apply bd-49f-runner: new lambda_function.py + BD_SNAPSHOT_ASOF_LAG_BDAYS=1 | apply complete + 0-diff replan |  | OPEN |
| L4 | verify | LIVE non-mutating exercise: invoke runner date=2026-07-10 table=allocations -> as_of MUST resolve 2026-07-09 (lag live) and the empty snapshot MUST be REJECTED pre-write (no stub, no sidecar, no sentinel) | CW log shows REJECT + zero new S3 object |  | OPEN |
| L6 | verify | CTO-GATED un-freeze re-pull of the last complete business day + END-STATE proof the served AUA moved off the frozen figure | CTO GO + served-plane verification |  | OPEN |

## Log

- 20260709T085522Z OPENED by 0.6.0_AE_PartnerETL with 5 leg(s)

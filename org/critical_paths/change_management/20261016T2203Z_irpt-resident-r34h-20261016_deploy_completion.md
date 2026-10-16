# Deploy Completion Record
**Date opened:** 2026-10-16T22:03:50.696768+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R34H (AR-g-148): resident release 34h on the resident host: ONE new root /opt/irpt-resident/0485393f3a-r34h, three new S3 objects under ec2/investor-reporting-ycharts/resident/ (tar sha256 60cc8d1d, sums 5d5f39f1, host script 0daf0975), one restart; six members change and one is added (the lease counts calls per window in a row of its own, the resolve hop re-sends a window-budget refusal, the resident builds the ycharts price tier), bindings gain the ycharts tier and the budget (6 calls, 390 s); V2 in the service's own environment with TWO Yahoo calls and NO YCharts call (CTO condition 3); bound to the COO packet blob af80fbe4f3 (CTO half names it, msg 9902); rollback to r34g in the same session if V2 does not print V2S OK; r34g root and every earlier artifact KEPT, nothing deleted
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pre-read as root: running root r34g, the four changed code members at r34g values, price_transport_ycharts.py absent, r34h root absent, library unmoved, queue 0 0 | P1 STOP-READ-0 PASS and STOP-READ-2 PASS |  | OPEN |
| D1 | s3-prefix | three NEW keys under ec2/investor-reporting-ycharts/resident/ in opal-313476888478-lambda-artifacts (r34h tar, package sums, host install script), each read 404 first | each read back by VersionId with sha256 equal |  | OPEN |
| D2 | activation | install_r34.sh as root: installs the r34h root, keeps the r34g root, restarts the unit once, rolls itself back to r34g on a failed start | running root r34h active, restarts 0 |  | OPEN |
| V1 | verify | after-reads: members MATCH, package sums 313 of 313, census 6 changed 1 added 0 removed, imports, pool pin, pricing tiers estate yfinance ycharts, budget {6, 390}, producer list unchanged, queue 0 0, no sign-in | the V1 lines in the record |  | OPEN |
| V2 | verify | v2_service_env_r34h.sh as root in the service's own environment: V2S CONTROLS BACKOFF DOOR PRICING BUDGET TIER OK and V2S OK SPY KEPT and ZQXWVK NOT_KEPT; two Yahoo calls, no YCharts call | V2S OK, else step 8 rollback |  | OPEN |

## Log

- 20261016T220350Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)

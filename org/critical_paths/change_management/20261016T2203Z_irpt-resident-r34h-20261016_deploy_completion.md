# Deploy Completion Record
**Date opened:** 2026-10-16T22:03:50.696768+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T220945Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R34H (AR-g-148): resident release 34h on the resident host: ONE new root /opt/irpt-resident/0485393f3a-r34h, three new S3 objects under ec2/investor-reporting-ycharts/resident/ (tar sha256 60cc8d1d, sums 5d5f39f1, host script 0daf0975), one restart; six members change and one is added (the lease counts calls per window in a row of its own, the resolve hop re-sends a window-budget refusal, the resident builds the ycharts price tier), bindings gain the ycharts tier and the budget (6 calls, 390 s); V2 in the service's own environment with TWO Yahoo calls and NO YCharts call (CTO condition 3); bound to the COO packet blob af80fbe4f3 (CTO half names it, msg 9902); rollback to r34g in the same session if V2 does not print V2S OK; r34g root and every earlier artifact KEPT, nothing deleted
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pre-read as root: running root r34g, the four changed code members at r34g values, price_transport_ycharts.py absent, r34h root absent, library unmoved, queue 0 0 | P1 STOP-READ-0 PASS and STOP-READ-2 PASS | P1 STOP-READ-0 PASS root r34g, STOP-READ-2 PASS r34h absent, the four changed code members MATCH r34g values, price_transport_ycharts.py ABSENT, library and wrapper unmoved, queue 0 0, producer list unchanged, sign-in baseline 0 (ssm_p1_out.txt) | CLOSED 20261016T220549Z |
| D1 | s3-prefix | three NEW keys under ec2/investor-reporting-ycharts/resident/ in opal-313476888478-lambda-artifacts (r34h tar, package sums, host install script), each read 404 first | each read back by VersionId with sha256 equal | three keys read 404 first; uploaded from C:/dev/irpt-release-r34r and read back by VersionId with sha256 equal: tar tDpe4FKO0S3zH576hzysgQ4cJ0yO0xI9 (60cc8d1d), sums 0k.t3y5nMJii9t80OiatQ9PjONpBfDMt (5d5f39f1), host script d5gyvLRY_qx0dL4FiaUcCoKdEEF9gGjz (0daf0975) | CLOSED 20261016T220638Z |
| D2 | activation | install_r34.sh as root: installs the r34h root, keeps the r34g root, restarts the unit once, rolls itself back to r34g on a failed start | running root r34h active, restarts 0 | install_r34.sh as root rc 0 (Systems Manager 33b5dbce-c54b-402c-a9c1-2ad68fd93b07): guard root r34g, host script and sums sha256 verified on the host, package sums OK (314 members), one restart, running root /opt/irpt-resident/0485393f3a-r34h active restarts 0 MainPID 1123353; r34g root kept | CLOSED 20261016T220759Z |
| V1 | verify | after-reads: members MATCH, package sums 313 of 313, census 6 changed 1 added 0 removed, imports, pool pin, pricing tiers estate yfinance ycharts, budget {6, 390}, producer list unchanged, queue 0 0, no sign-in | the V1 lines in the record | after-reads: running root r34h active restarts 0; five release members MATCH; package sums 0 of 314 not OK; census package scope 6 changed 1 added 0 removed (full tree 64 changed incl bytecode); pool pin equal; opal_pricing tiers estate yfinance ycharts; ycharts_window_budget {6 calls, 390 s}; producer list unchanged; queue 0 0; no sign-in 0 (ssm_d2_out.txt, ssm_v1_census_out.txt); resident_worker import did not import in the census read (missing module extract, the read's path omission) and imported OK in the install's own P4 proof | CLOSED 20261016T220834Z |
| V2 | verify | v2_service_env_r34h.sh as root in the service's own environment: V2S CONTROLS BACKOFF DOOR PRICING BUDGET TIER OK and V2S OK SPY KEPT and ZQXWVK NOT_KEPT; two Yahoo calls, no YCharts call | V2S OK, else step 8 rollback | V2 as root in the service's own environment rc 0: V2S CONTROLS OK 4 of 4, BACKOFF OK, DOOR OK, PRICING OK, BUDGET OK, TIER OK, V2S OK SPY KEPT and ZQXWVK NOT_KEPT; two Yahoo calls and no YCharts call (ssm_v2s_out.txt) | CLOSED 20261016T220945Z |

## Log

- 20261016T220350Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261016T220549Z LEG P1 closed: P1 STOP-READ-0 PASS root r34g, STOP-READ-2 PASS r34h absent, the four changed code members MATCH r34g values, price_tran
- 20261016T220638Z LEG D1 closed: three keys read 404 first; uploaded from C:/dev/irpt-release-r34r and read back by VersionId with sha256 equal: tar tDpe
- 20261016T220759Z LEG D2 closed: install_r34.sh as root rc 0 (Systems Manager 33b5dbce-c54b-402c-a9c1-2ad68fd93b07): guard root r34g, host script and sum
- 20261016T220834Z LEG V1 closed: after-reads: running root r34h active restarts 0; five release members MATCH; package sums 0 of 314 not OK; census packa
- 20261016T220945Z LEG V2 closed: V2 as root in the service's own environment rc 0: V2S CONTROLS OK 4 of 4, BACKOFF OK, DOOR OK, PRICING OK, BUDGET OK, TI
- 20261016T220945Z CLOSED -- all 5 legs proven

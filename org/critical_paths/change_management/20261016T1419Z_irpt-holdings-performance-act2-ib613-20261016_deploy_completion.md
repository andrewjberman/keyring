# Deploy Completion Record
**Date opened:** 2026-10-16T14:19:12.500668+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-pr-613 (Act 2): restate the 47 split days of the 49 Financial holdings_performance_daily table (2024-07-09 to 2026-09-03) by one dated invoke each of irpt-holdings-performance-lambda, ascending, outside the fire window; prior version recorded per key before each write
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 30.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | gates: pair sha256, addenda blobs, three CTO halves, IB-pr-612 complete and its ledger CLOSED, no other open ledger or marker on the function or root, function CodeSha256 LiDXhN74, handler date line, producer --date, 47-day list equal to the signed record | the printed reads |  | OPEN |
| L2 | s3-prefix | the 47 served day keys of the 49 Financial holdings_performance_daily table (one per split day) written ONLY by the producer's dated invoke; prior IsLatest version id recorded before each write; Branch B per key = the prior version copied back over the same key | per-day prior and new version ids |  | OPEN |
| L3 | verify | per-day row-by-row comparison of the new version against the prior: only split-holding accounts changed, changed count equals the signed per-day count (985 on 2026-04-21), no stop | per-day counts |  | OPEN |
| L4 | verify | after the 47: totals (47 days, 1291 changed account-days, 47 invokes), ratio-absent names across the 47 manifests equal the signed 13, event keys date only, window 30+ minutes clear of a scheduled fire, siblings never invoked | the totals |  | OPEN |

## Log

- 20261016T141912Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)

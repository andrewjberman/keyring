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
| L1 | verify | gates: pair sha256, addenda blobs, three CTO halves, IB-pr-612 complete and its ledger CLOSED, no other open ledger or marker on the function or root, function CodeSha256 LiDXhN74, handler date line, producer --date, 47-day list equal to the signed record | the printed reads | pair sha256 8f645588ab10 equal; addenda blobs f0cec424f4, 47e819dd93, 82d849a97c equal; CTO halves SIGNED; IB-pr-612 complete and its ledger CLOSED; 2004 ledgers read, 0 OPEN naming the function or root; function CodeSha256 LiDXhN74; deployed handler.py line 109 holds the date path; producer --date present; 47 days equal the signed record (delta record sha256 d0492a3fba6b) | CLOSED 20261016T151007Z |
| L2 | s3-prefix | the 47 served day keys of the 49 Financial holdings_performance_daily table (one per split day) written ONLY by the producer's dated invoke; prior IsLatest version id recorded before each write; Branch B per key = the prior version copied back over the same key | per-day prior and new version ids | 47 served day keys of the 49F holdings_performance_daily table restated by one dated invoke each, ascending 2024-07-09 to 2026-09-03; prior IsLatest version recorded before every write (3 or more versions each); 1 refused invoke (date alone, nothing written) plus 47 writing invokes = 48; event {date, source} with source read from the schedule; siblings never invoked; no key deleted | CLOSED 20261016T151008Z |
| L3 | verify | per-day row-by-row comparison of the new version against the prior: only split-holding accounts changed, changed count equals the signed per-day count (985 on 2026-04-21), no stop | per-day counts | 47 of 47 days comparison_ok: changed rows equal the signed per-day counts (985 on 2026-04-21), sum 1291, other_rows_changed 0, changed accounts all split holders, compared over the prior version's 19 columns under the CTO's rule A (schema 1.1 to 1.2, span_trading_days added), account sets equal | CLOSED 20261016T151008Z |
| L4 | verify | after the 47: totals (47 days, 1291 changed account-days, 47 invokes), ratio-absent names across the 47 manifests equal the signed 13, event keys date only, window 30+ minutes clear of a scheduled fire, siblings never invoked | the totals | totals 47 days, 1291 changed account-days, 47 writing invokes; 47 manifests all declare split_adjust, named ratio-absent entries 13 = the signed sum 13, 0 mismatching days; window clear 169 minutes after the last fire and 4105 before the next (Monday 11:30Z); event keys date and source only; siblings invoked 0; rollback none | CLOSED 20261016T151008Z |

## Log

- 20261016T141912Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
- 20261016T151007Z LEG L1 closed: pair sha256 8f645588ab10 equal; addenda blobs f0cec424f4, 47e819dd93, 82d849a97c equal; CTO halves SIGNED; IB-pr-612 com
- 20261016T151008Z LEG L2 closed: 47 served day keys of the 49F holdings_performance_daily table restated by one dated invoke each, ascending 2024-07-09 t
- 20261016T151008Z LEG L3 closed: 47 of 47 days comparison_ok: changed rows equal the signed per-day counts (985 on 2026-04-21), sum 1291, other_rows_chan
- 20261016T151008Z LEG L4 closed: totals 47 days, 1291 changed account-days, 47 writing invokes; 47 manifests all declare split_adjust, named ratio-absent

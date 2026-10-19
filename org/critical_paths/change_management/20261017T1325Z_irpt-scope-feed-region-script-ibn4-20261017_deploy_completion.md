# Deploy Completion Record
**Date opened:** 2026-10-17T13:25:49.012136+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261019T130814Z
**Deploy:** IRPT_BCKEND TO-IB-pn-4 (ADDENDUM 4 + AMENDMENT 1): replace code/manual_api/pull_inflection_scope_account_returns.py (live ab5905d7, version FaHfnhIltMRNABo2GyALh7uzo4y7fOaZ) with the region-named script a92589d6, three-part smoke on the live prefixes, then add the feed row and chain entries to code/gold/orion-gold-dispatch.sh (live d6b00f6f, version L8GGxBIUqBl.XlBkXVcWuvhHb9YjrnaO; file at commit e7d5361cf9); saved copies first
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | gates 1(a) to 1(i) measured and both rollback copies saved outside the repository | the printed reads and saved sha256 values | gates 1(a)-1(i) measured: addendum blob 22172a052e, both halves bound, IB-pn-3 complete, no ledger open on the chain (98 worktrees read), live dispatch d6b00f6f equal to the pre-row copy, runner role simulations allowed, 294 households = bound, sidecar equals generated address, calendar present, filter does not match; saved copies script ab5905d7 (version FaHfnhIl..) and dispatch d6b00f6f (version L8GGxBII..) outside the repo | CLOSED 20261017T133039Z |
| L2 | s3-prefix | the repository script uploaded over code/manual_api/pull_inflection_scope_account_returns.py, read back sha256 equal to a92589d6 | uploaded sha256 and version id | script a92589d6 uploaded 2026-10-17T13:26:55Z as version tDiwpCZv.., read back sha256 equal; replaced object ab5905d7 saved first | CLOSED 20261017T133039Z |
| L3 | verify | the three-part smoke over the LIVE code prefixes (import, session_token under scrubbed region, plan-only run), no Orion request | the smoke output | three-part smoke clean on Python 3.9.25 over 209 flat files from the live prefixes: import and source_prefixes 0 socket attempts; session_token under scrubbed region OK; plan-only run OK; negative control NoRegionError on 4527c57f; orion_requests 0 | CLOSED 20261017T133039Z |
| L4 | s3-prefix | code/gold/orion-gold-dispatch.sh replaced by the file at commit e7d5361cf9 only after a clean smoke: exactly 1 row and its chain entries vs live | rows_added 1, chain entries equal chains carrying PERF, other_lines_changed 0 | dispatch from commit e7d5361cf9 (AMENDMENT 1) uploaded 2026-10-17T13:29:03Z as version JjTLNaZe.., read back sha256 e9aef66b equal; exactly 1 row, 2 chain entries (CHAIN_PULL, CHAIN_INCREMENTAL = chains carrying PERF), 0 other lines | CLOSED 20261017T133039Z |
| L5 | verify | the first scheduled chain run read from the STEP LOG: exit 0 not tolerated, no SKIPPED, coverage = denominator, daily_factor stored, requests within 294, calcGrossOfFees false, nothing outside orion/inflection | the first-run read | first scheduled chain (2026-10-18 11:33Z) read from the step log: exit 0, no TOLERATING, no SKIPPED, DAYS complete=1 skipped=0; CALLS 294 ok 0 failed (294 attempts, bound 294); coverage 863 = 795 RETURNED + 68 ABSENT, 0 zero, daily_factor stored; calc_gross_of_fees false, fee basis NET; 2 keys written, both under orion/inflection/, 1 version each; the 2026-10-19 chain skipped both as existing | CLOSED 20261019T125930Z |

## Log

- 20261017T132549Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261017T133039Z LEG L1 closed: gates 1(a)-1(i) measured: addendum blob 22172a052e, both halves bound, IB-pn-3 complete, no ledger open on the chain (98
- 20261017T133039Z LEG L2 closed: script a92589d6 uploaded 2026-10-17T13:26:55Z as version tDiwpCZv.., read back sha256 equal; replaced object ab5905d7 sa
- 20261017T133039Z LEG L3 closed: three-part smoke clean on Python 3.9.25 over 209 flat files from the live prefixes: import and source_prefixes 0 socket 
- 20261017T133039Z LEG L4 closed: dispatch from commit e7d5361cf9 (AMENDMENT 1) uploaded 2026-10-17T13:29:03Z as version JjTLNaZe.., read back sha256 e9ae
- 20261019T125930Z LEG L5 closed: first scheduled chain (2026-10-18 11:33Z) read from the step log: exit 0, no TOLERATING, no SKIPPED, DAYS complete=1 ski
- 20261019T130814Z CLOSED -- all 5 legs proven

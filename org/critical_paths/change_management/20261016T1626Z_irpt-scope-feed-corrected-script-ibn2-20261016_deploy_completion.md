# Deploy Completion Record
**Date opened:** 2026-10-16T16:26:47.784485+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-pn-2 (ADDENDUM 3): replace the Scope feed script code object code/manual_api/pull_inflection_scope_account_returns.py (live ab5905d7.., version CfFwbl1JeTo553ddKKssxBBx_23j1zTR) with the corrected script 4527c57f.., import smoke over the LIVE code prefixes on this host (Python 3.9; the runner stays stopped), then add the feed's one catalog row and its chain entries to code/gold/orion-gold-dispatch.sh (live d6b00f6f.., version 28oA7ykJ1O2TPVC2KFvm6hrhu8e1iD4H); saved copies in scratch; first scheduled chain is the proof
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 40.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | gates 1(a) to 1(g) measured now: addendum blob d4b8c52eee, IB-pn-1 complete, no other open ledger on the chain, live dispatch equals the repository copy before the row, runner role allowed, household count 294 = request bound, notification filter does not match | the printed reads |  | OPEN |
| L2 | s3-prefix | the corrected script uploaded over code/manual_api/pull_inflection_scope_account_returns.py, read back with sha256 equal to 4527c57f..; the replaced object saved first | uploaded sha256 and version ids |  | OPEN |
| L3 | verify | the import smoke: a flat directory built from the LIVE code/gold, code/manual_api, code/silver and code/bronze prefixes by basename (collisions detected), the uploaded script's top level executed with Python 3.9 and source_prefixes() called; no Orion request, no secret read, nothing written to S3 | the smoke output |  | OPEN |
| L4 | s3-prefix | code/gold/orion-gold-dispatch.sh replaced by the repository file ONLY after a clean smoke and ONLY if the difference to the live object is exactly one catalog row and its chain entries | rows_added 1, chain entries equal chains carrying PERF, other_lines_changed 0 |  | OPEN |
| L5 | verify | the first scheduled chain run read from the STEP LOG: exit 0 not tolerated, no SKIPPED, DAYS complete skipped=0, coverage = denominator, no zero, daily_factor stored, requests within 294, calcGrossOfFees false, nothing outside orion/inflection, no existing key changed | the first-run read |  | OPEN |

## Log

- 20261016T162647Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)

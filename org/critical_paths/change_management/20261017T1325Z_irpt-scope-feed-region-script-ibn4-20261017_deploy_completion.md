# Deploy Completion Record
**Date opened:** 2026-10-17T13:25:49.012136+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-pn-4 (ADDENDUM 4 + AMENDMENT 1): replace code/manual_api/pull_inflection_scope_account_returns.py (live ab5905d7, version FaHfnhIltMRNABo2GyALh7uzo4y7fOaZ) with the region-named script a92589d6, three-part smoke on the live prefixes, then add the feed row and chain entries to code/gold/orion-gold-dispatch.sh (live d6b00f6f, version L8GGxBIUqBl.XlBkXVcWuvhHb9YjrnaO; file at commit e7d5361cf9); saved copies first
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | gates 1(a) to 1(i) measured and both rollback copies saved outside the repository | the printed reads and saved sha256 values |  | OPEN |
| L2 | s3-prefix | the repository script uploaded over code/manual_api/pull_inflection_scope_account_returns.py, read back sha256 equal to a92589d6 | uploaded sha256 and version id |  | OPEN |
| L3 | verify | the three-part smoke over the LIVE code prefixes (import, session_token under scrubbed region, plan-only run), no Orion request | the smoke output |  | OPEN |
| L4 | s3-prefix | code/gold/orion-gold-dispatch.sh replaced by the file at commit e7d5361cf9 only after a clean smoke: exactly 1 row and its chain entries vs live | rows_added 1, chain entries equal chains carrying PERF, other_lines_changed 0 |  | OPEN |
| L5 | verify | the first scheduled chain run read from the STEP LOG: exit 0 not tolerated, no SKIPPED, coverage = denominator, daily_factor stored, requests within 294, calcGrossOfFees false, nothing outside orion/inflection | the first-run read |  | OPEN |

## Log

- 20261017T132549Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)

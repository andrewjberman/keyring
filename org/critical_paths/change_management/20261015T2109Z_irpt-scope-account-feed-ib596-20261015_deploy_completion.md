# Deploy Completion Record
**Date opened:** 2026-10-15T21:09:47.571745+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-pr-596: land the Orion Scope account feed on the inf gold chain: code/manual_api/pull_inflection_scope_account_returns.py, code/manual_api/trading_calendar.py, code/manual_api/scope_feed_addresses.json (generated from address()), and code/gold/orion-gold-dispatch.sh by exactly one catalog row and its chain entries; rollback copy saved (sha256 d6b00f6fdd75, version ZQZ21e2ArsbJUEw8iAzE_.i.f74PHX0r); request_bound 294 (the household count); first scheduled run read overnight
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 40.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | gates c to i measured now, request_bound stated before any upload | the printed reads |  | OPEN |
| L2 | s3-prefix | the script, trading_calendar.py and the sidecar uploaded to code/manual_api/ verbatim or generated from address(), each read back with sha256 equal | uploaded sha256 per object |  | OPEN |
| L3 | s3-prefix | code/gold/orion-gold-dispatch.sh replaced by the HEAD file ONLY if the diff to the saved copy is exactly one catalog row and its chain entries | rows_added 1, chain entries equal chains carrying PERF, other_lines_changed 0 |  | OPEN |
| L4 | verify | the first scheduled chain run: step exit 0 not tolerated, coverage = denominator, no zero, daily_factor stored, requests within 294, calcGrossOfFees false, nothing outside orion/inflection, no existing key changed | the first-run read |  | OPEN |

## Log

- 20261015T210947Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)

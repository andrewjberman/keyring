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
| L1 | verify | gates c to i measured now, request_bound stated before any upload | the printed reads | addendum blob 1e138cbeea equal, halves signed, 586 and 594 complete and VALID, script holds SCOPE-FEED-A/B; no other OPEN ledger or window names the chain (only this seat's ib600 IAM ledger, legs closed); live dispatch sha256 d6b00f6fdd75 = pre-feed repo copy (e7d5361cf9^); roster column account_start_date; runner role: secret read allowed, feed bronze and silver put allowed (after IB-pr-600), roster/positions get+list allowed, unrelated bucket implicitDeny; notification filters 12 configs printed, feed bronze key matches none; request_bound = household_count = 294 stated before any upload; every feed key begins orion/inflection/; the three basenames absent from all four code prefixes (no sync collision) | CLOSED 20261015T211023Z |
| L2 | s3-prefix | the script, trading_calendar.py and the sidecar uploaded to code/manual_api/ verbatim or generated from address(), each read back with sha256 equal | uploaded sha256 per object | uploaded to code/manual_api/ (each absent first, read back by version id): pull_inflection_scope_account_returns.py sha256 ab5905d71d39.. = repo (v CfFwbl1J..), trading_calendar.py 9bc467c6ce4d.. = repo lib (v w3crMN8l..), scope_feed_addresses.json 198af1c530ec.. generated from address() keys bucket, bronze_key_prefix, silver_key_prefix (v jwohEWNS..), consistency checked against the builder for a second date | CLOSED 20261015T211154Z |
| L3 | s3-prefix | code/gold/orion-gold-dispatch.sh replaced by the HEAD file ONLY if the diff to the saved copy is exactly one catalog row and its chain entries | rows_added 1, chain entries equal chains carrying PERF, other_lines_changed 0 | dispatch object code/gold/orion-gold-dispatch.sh: pre-edit live sha256 d6b00f6fdd75 (v ZQZ21e2A..) = pre-feed repo copy; diff to HEAD = rows_added 1 (INF_API_PULL_SCOPE_ACCTS), chain_entries_added 2 (CHAIN_PULL, CHAIN_INCREMENTAL) = chains_carrying_perf 2, other_lines_changed 0; uploaded HEAD file sha256 e9aef66bc8a4.. read back equal (new v s1MuRDO6..) at 21:11Z; saved copy scratch sha256 d6b00f6fdd75 | CLOSED 20261015T211155Z |
| L4 | verify | the first scheduled chain run: step exit 0 not tolerated, coverage = denominator, no zero, daily_factor stored, requests within 294, calcGrossOfFees false, nothing outside orion/inflection, no existing key changed | the first-run read | FIRST RUN FAILED, read 2026-10-16 13:00Z from chain_full_20261016_113302.log: step INF_API_PULL_SCOPE_ACCTS started 11:51:47Z, Traceback at pull_inflection_scope_account_returns.py line 34 (_HERE.parents[2], IndexError on /tmp/orion_gold_scripts), exit=1 wall 0.1s, TOLERATED by the chain; 0 requests, feed bronze and silver prefixes 0 keys, no existing key changed. Order step 7 Branch B performed 13:00Z: saved dispatch copy restored as new current version 28oA7ykJ1O2TPVC2KFvm6hrhu8e1iD4H, sha256 d6b00f6fdd75 equals saved_copy_sha256; script, calendar and sidecar left in place (inert). Row IRPT_BCKEND-D2-S221 | CLOSED 20261016T130147Z |

## Log

- 20261015T210947Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
- 20261015T211023Z LEG L1 closed: addendum blob 1e138cbeea equal, halves signed, 586 and 594 complete and VALID, script holds SCOPE-FEED-A/B; no other OPE
- 20261015T211154Z LEG L2 closed: uploaded to code/manual_api/ (each absent first, read back by version id): pull_inflection_scope_account_returns.py sha2
- 20261015T211155Z LEG L3 closed: dispatch object code/gold/orion-gold-dispatch.sh: pre-edit live sha256 d6b00f6fdd75 (v ZQZ21e2A..) = pre-feed repo copy;
- 20261016T130147Z LEG L4 closed: FIRST RUN FAILED, read 2026-10-16 13:00Z from chain_full_20261016_113302.log: step INF_API_PULL_SCOPE_ACCTS started 11:5

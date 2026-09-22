# Deploy Completion Record
**Date opened:** 2026-09-22T02:23:06.674519+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260922T035014Z
**Deploy:** AMGT-rk-91 move M2: filings/v1 source.json to filing_source silver + filing_attempt state
**Authored by:** 0.9.0_WK_AMGT_RESAPP~91
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | filing_source silver (14 rows) + filing_attempt state (180 keys) copies | per-object round-trip equal (AC4) | move_m2: silver_rows 14 (sec 13, issuer-site 1) round_trip_equal 14/14, state_puts 180 sha_equal 180/180, refused 0 (.scratch/r91/copy.json) | CLOSED 20260922T034848Z |
| L2 | activation | state grant added to opal-amgt-scoped-api-grants + opal-amgt-scoped-api redeployed | live re-read present + invoke equal (AC6) | IAM add: statements 4 has_state_fa True has_filings_v1 True (live re-read); redeploy: CodeSha256 vsWWFL9jRKHbQb9WP7x2Ob1Qv02nQpAOJkPcQk8/nkA= Active Successful; three thesis invokes 200 (CSL_AU_Equity, 6861_JP_Equity, CAT_US_Equity), management_status/roster_status match the pre-existing (as_of 2026-09-19, untouched) persisted documents | CLOSED 20260922T034903Z |
| L3 | activation | filings/v1 grant removed from opal-amgt-scoped-api-grants | live re-read absent, state present, invokes equal (AC6) | IAM remove: statements 4 has_state_fa True has_filings_v1 False (live re-read); three thesis invokes still 200 and equal to the pre-removal read; targeted plan on both resources reads No changes | CLOSED 20260922T034916Z |

## Log

- 20260922T022306Z OPENED by 0.9.0_WK_AMGT_RESAPP~91 with 3 leg(s)
- 20260922T034848Z LEG L1 closed: move_m2: silver_rows 14 (sec 13, issuer-site 1) round_trip_equal 14/14, state_puts 180 sha_equal 180/180, refused 0 (.sc
- 20260922T034903Z LEG L2 closed: IAM add: statements 4 has_state_fa True has_filings_v1 True (live re-read); redeploy: CodeSha256 vsWWFL9jRKHbQb9WP7x2Ob1
- 20260922T034916Z LEG L3 closed: IAM remove: statements 4 has_state_fa True has_filings_v1 False (live re-read); three thesis invokes still 200 and equal
- 20260922T035014Z CLOSED -- all 3 legs proven

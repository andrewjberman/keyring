# Deploy Completion Record
**Date opened:** 2026-10-16T19:07:59.297639+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-308: Cottonwood landing function irpt-cot-account-return-daily-lambda: ONE new bundle version (build-only hash +iYXakKx7..), ONE safe-apply plan 0/1/0 of account-return-daily (code attributes only), DRY RUN then FOUR rewrite events over the 66 landed gold days at the same keys (history_scope derived by the first-row rule; ten October days restated in external_flow and total_return_daily at the packet ceilings), whole-prefix after-read of the 3325 history days; bound to the signed packet sha256 962ef131ff27c49e (COO half and CTO half SIGNED); rollback: code version UnMNWDhcC3KpERDmGYdKAl83whx1oNFW, per-key prior versions; schedule ENABLED and untouched; nothing deleted
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | source-map entry artifact_sha256 for irpt-cot-account-return-daily-lambda plus this ledger sentinel, committed with explicit paths | commit ids recorded |  | OPEN |
| L2 | s3-prefix | artifact key investor-reporting/irpt-cot-account-return-daily-lambda.zip in opal-313476888478-lambda-artifacts: a NEW VERSION of the key (current unused version Amwu_BigtNXtPIwPXQIBPXmEFfKpg9RN; running version UnMNWDhcC3KpERDmGYdKAl83whx1oNFW is the rollback target) | new VersionId different from before, landed sha256 equals the built zip equals +iYXakKx7zhK33lv6W0jDAY1QsLYUNqNCuHHIA7owD0= |  | OPEN |
| L3 | tf-lambda | ONE safe-apply of infra/aws/terraform/investor-reporting/account-return-daily plan exactly 0 add 1 change 0 destroy on module.irpt_account_return_daily.aws_lambda_function.this by code attributes only | plan counts, naming gate 0 REFUSE, function CodeSha256 equals the built zip, policy five statements unchanged, schedule ENABLED untouched, post-apply plan No changes |  | OPEN |
| L4 | verify | DRY RUN event rewrite 2026-07-10 to 2026-08-13 dry_run true on the function (25 days, writes nothing) | ok true, held 0, 25 days, rows equal landed rows, Max Memory Used at most 819 MB, duration at most 720 s, versions unchanged |  | OPEN |
| L5 | s3-prefix | FOUR rewrite events over the 66 landed gold days of irpt/cottonwood/gold/account_return_daily in opal-data-cottonwood (two keys per day at the same keys; prior versions kept) | per event: rows equal, account_id and market_value_eod identical, allowance days only, claim inferred, PARTIAL and FULL counts, no FULL to PARTIAL flip, two versions per key |  | OPEN |
| L6 | verify | whole-prefix after-read of ALL 3325 history days (key list and version ids equal before, one version each), 66 landed days two versions, 3 held days absent, no new key outside, schedule ENABLED; the receipt | act5 values recorded, three criteria run |  | OPEN |

## Log

- 20261016T190759Z OPENED by 0.7.0_AE_CloudOps~IB2 with 6 leg(s)

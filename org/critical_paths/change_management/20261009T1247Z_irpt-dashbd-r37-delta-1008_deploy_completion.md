# Deploy Completion Record
**Date opened:** 2026-10-09T12:47:22.905946+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD DB-b-88: R37 DELTA -- realized key gains realized_gain; re-pin account_activity_lots.py (0a41f929a3) and 2026-10-08 lots backfill on irpt-49f-reporting-gold-lambda -- signed against R37 packet sha256 848dd8640688c28cb62ffab109c4d55ea4e5348bc5286400a824d8e1405fd40b; delta packet sha256 e4231140c59ecee6183cbab525193e612882a4d2c43150863a17f103d6e37ae6; targeted plan 0/1/0
**Authored by:** 0.9.0_WK_IRPT_DASHBD~63
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | source-map re-pin + artifact upload + targeted plan | Plan: 0 to add, 1 to change, 0 to destroy | source-map pin account_activity_lots.py -> 0a41f929a3 (DB-b-87 drain commit, blob db068fe88b = 9c980c6c15, not yet on origin/CLOUD) @d87079fd89; sha256 cfa366ec re-read = staged blob verified by the builder (18 of 18 members verified); artifact uploaded version a.YllA9SmwwfY34NlajqOaNsex2bBZAy (prior latest pPnoTZs86qlqo2waxfP4h2ogXwq3hoR5) sha256 yIAQjspL0nPX6tJOHxD+Dv0REVoZyBNRkhmHQxUVuEE= @7fbf4eb108; iam.tf locals.tf lambda.tf at efeb21df71 bytes 2c0ed377/5fe82384/9ae18719; anchor CodeSha256 ciTGx5UV re-read live before; targeted terraform plan -out: Plan: 0 to add, 1 to change, 0 to destroy | CLOSED 20261009T125351Z |
| D1 | activation | safe-apply of the saved plan, infra/aws/terraform/investor-reporting/reporting-gold | Apply complete, 1 changed | SAFE_APPLY_TERRAFORM=main terraform.exe .tools/safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/reporting-gold apply r41.tfplan, 2026-10-09 12:55Z, rc=0 (the Apply complete line was above the 15-line tail window and was not captured; effect verified: Lambda LastModified 2026-10-09T12:55:44Z, and a post-apply targeted plan reads No changes. Your infrastructure matches the configuration.); role policy untouched (7 sids unchanged) | CLOSED 20261009T125735Z |
| V1 | verify | readback CodeSha256 = source map deployed_code_sha256 | get-function-configuration CodeSha256 | get-function-configuration CodeSha256 yIAQjspL0nPX6tJOHxD+Dv0REVoZyBNRkhmHQxUVuEE= = artifact sha256 = source map deployed_code_sha256 (stamped by record-deploy-scope.py, ledger 61a60b9c7e); anchor ciTGx5UV before; State Active LastUpdateStatus Successful | CLOSED 20261009T125735Z |
| B1 | verify | ONE backfill 2026-10-08 (lots rows, no LOTS_SKIPPED, returns byte-equal) | request id + REPORT line + returns sha256 before/after |  | OPEN |

## Log

- 20261009T124722Z OPENED by 0.9.0_WK_IRPT_DASHBD~63 with 4 leg(s)
- 20261009T125351Z LEG P1 closed: source-map pin account_activity_lots.py -> 0a41f929a3 (DB-b-87 drain commit, blob db068fe88b = 9c980c6c15, not yet on or
- 20261009T125735Z LEG D1 closed: SAFE_APPLY_TERRAFORM=main terraform.exe .tools/safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/reporting-gol
- 20261009T125735Z LEG V1 closed: get-function-configuration CodeSha256 yIAQjspL0nPX6tJOHxD+Dv0REVoZyBNRkhmHQxUVuEE= = artifact sha256 = source map deploy

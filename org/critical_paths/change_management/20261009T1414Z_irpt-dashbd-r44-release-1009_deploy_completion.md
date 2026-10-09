# Deploy Completion Record
**Date opened:** 2026-10-09T14:14:09.320607+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T153201Z
**Deploy:** IRPT_DASHBD DB-b-95: R44 release -- DB-b-90 (account_activity_lots.py pin d18ddf000d) + DB-b-91 (handler.py blob 7c9bb9dcdc5b) as ONE gold Lambda release over live yIAQjspL on irpt-49f-reporting-gold-lambda -- signed against R44 packet sha256 28e224f030230bf2468e5bf5a78f29e5b55c9fcde5565e2c050275d16b06abc0 (COO half @723a5e7d62, CTO half @fa8d2c2961); targeted plan 0/1/0; built artifact sha256 and build commit are stated at leg P1
**Authored by:** 0.9.0_WK_IRPT_DASHBD~70
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 36.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | source-map re-pin + built-zip member census vs live zip + targeted plan | upload_member_diff exactly the two member paths, reporting_policies.json equal live, Plan: 0 to add, 1 to change, 0 to destroy | source-map re-pin 072d27a4a1; built oNgy4rnr...; member census vs live zip (S3 version a.YllA9SmwwfY34NlajqOaNsex2bBZAy): differ exactly account_activity_lots.py + handler.py, reporting_policies.json equal live, 19 of 19 members; upload version qh361rTWYO2VtgsirsJXq6kiqJEVBDpZ (f0d129281f); targeted plan 'Plan: 0 to add, 1 to change, 0 to destroy.' | CLOSED 20261009T143249Z |
| D1 | activation | one safe-apply of the saved plan, infra/aws/terraform/investor-reporting/reporting-gold | Apply complete, 1 changed | SAFE_APPLY_TERRAFORM=main terraform.exe .tools/safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/reporting-gold apply r44.tfplan: rc 0, 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' at 2026-10-09T14:34:30Z | CLOSED 20261009T143625Z |
| V1 | verify | readback CodeSha256 equals built, post-apply plan No changes | get-function-configuration CodeSha256 = built sha256; No changes | get-function-configuration CodeSha256 oNgy4rnrduvN9N2axhsHBfe9izZKd8dZGeFGXAIh+cM= = built = artifact metadata; LastUpdateStatus Successful, State Active; post-apply targeted plan 'No changes. Your infrastructure matches the configuration.'; source map stamped by record-deploy-scope.py (deployed_code_sha256, deploy_ledger d250d437a5) | CLOSED 20261009T143625Z |
| S1 | verify | first scheduled fire sizing read (85% of 900 s = 765 s, 85% of 2048 MB = 1740.8 MB); issuer reads REPORT line and closes this leg | REPORT line Duration and Max Memory Used against the 85% lines | TO-DB-b-103 ONE dry-run backfill 2026-10-08 on live oNgy4rnr (request bfac402b-2ddf-48c4-908a-8a298594e3a8, 7620 accounts, 585281 lots rows, 0 objects written): REPORT Duration 377366.04 ms vs 765000 ms line (49.3 pct of 900 s), Max Memory Used 1661 MB vs 1740.8 MB line (81.1 pct of 2048 MB) -> UNDER both | CLOSED 20261009T153201Z |

## Log

- 20261009T141409Z OPENED by 0.9.0_WK_IRPT_DASHBD~70 with 4 leg(s)
- 20261009T143249Z LEG P1 closed: source-map re-pin 072d27a4a1; built oNgy4rnr...; member census vs live zip (S3 version a.YllA9SmwwfY34NlajqOaNsex2bBZAy)
- 20261009T143625Z LEG D1 closed: SAFE_APPLY_TERRAFORM=main terraform.exe .tools/safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/reporting-gol
- 20261009T143625Z LEG V1 closed: get-function-configuration CodeSha256 oNgy4rnrduvN9N2axhsHBfe9izZKd8dZGeFGXAIh+cM= = built = artifact metadata; LastUpda
- 20261009T153201Z LEG S1 closed: TO-DB-b-103 ONE dry-run backfill 2026-10-08 on live oNgy4rnr (request bfac402b-2ddf-48c4-908a-8a298594e3a8, 7620 account
- 20261009T153201Z CLOSED -- all 4 legs proven

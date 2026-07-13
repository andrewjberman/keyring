# Deploy Completion Record
**Date opened:** 2026-07-13T05:35:41.568059+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260713T054209Z
**Deploy:** OPAL_ASSETS G4: per-(ETF,partner) ownership fold as additive rows (value_class=etf_ownership_held, 6th class) + ONE new IAM read grant opal-data-etfs/daily/*. Authored 0.8.0_AE_CloudComp @ 0105ef6e7; applied by 0.7.0_AE_CloudOps~A (single applier, no TF race).
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | G4 code+emitter.tf+source-map committed & pushed CLOUD | commit hashes | G4 code+emitter.tf 0105ef6e7 + header fix 127e7dc0f (applied ref), both pushed origin/CLOUD; source-map artifact_sha256->GfqMYehfKfQXFs6zeSvID2Rrb+jLdJPeX1+dau49Tf8= last_deployed_commit->127e7dc0f30e6786a93f240a63dab4970dede482 | CLOSED 20260713T054208Z |
| L2 | s3-prefix | opal-assets-daily-emitter.zip rebuilt+uploaded+VERIFIED (head-object sha match vs source-map) | sha256 head-object | head-object s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-daily-emitter.zip -> ContentLength=7942 content-sha256=GfqMYehfKfQXFs6zeSvID2Rrb+jLdJPeX1+dau49Tf8= == local build. NOTE: build-and-upload.sh PS upload SILENTLY NO-OP'D (upload-verify gate da5af3c8c FIRED and caught it -- first production catch); re-uploaded via bash aws + verified | CLOSED 20260713T054208Z |
| L3 | verify | safe-apply (Rule 18, NOT bare terraform apply) + 0-diff re-plan | plan 'No changes' | safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply: 0 added, 2 changed, 0 destroyed (aws_iam_role_policy.emitter + module.emitter.aws_lambda_function.this). Re-plan: 'no differences, no changes needed' = 0-diff | CLOSED 20260713T054208Z |
| L4 | verify | IAM APPLIED truth: get-role-policy shows the etfs grant + SINGLE-ARN simulates (etfs flips implicitDeny->allowed; mdpf pos-control allowed; opal-data-bd sovereign STAYS denied) | get-role-policy + 3 separate simulate calls | APPLIED (get-role-policy): ReadEtfsOwnershipDaily s3:GetObject arn:aws:s3:::opal-data-etfs/daily/* + ListEtfsOwnershipDaily present. SINGLE-ARN simulates (3 SEPARATE calls -- batching poisons verdicts, see finding): TARGET etfs/daily/49financial/2026-06-24.json implicitDeny->ALLOWED; POS CONTROL mdpf aggregate_aua/2026-07-10.json ALLOWED (instrument honest); SOVEREIGN opal-data-bd/schwab/silver/rps IMPLICITDENY (49F hold intact) | CLOSED 20260713T054209Z |
| L5 | verify | EXERCISE the deployed emitter (behavior, not config-read) + read rows back: every row carries value_class; ownership rows do not sum into base AUM classes; 49F carries partial:08242234-only | invoke + table read-back | invoke rc=200 -> {rows_written:26, base_rows:14, ownership_rows:12, run_date:2026-07-10}. Read-back run_date=2026-07-10: 26 rows, value_class MISSING=0 (model_value 7/custody_composite 1/platform_model_aua 1/etf_net_assets 4/model_value_sum 1 = 14 base + etf_ownership_held 12). 49F all 4 rows partial=08242234-only state=rolled_forward as_of=2026-06-24 (disclosed, not fabricated fresh); inflection+cottonwood fresh@2026-07-10; no zero-valued rows; ownership_pct present. 12 not 8 because cottonwood DOES have a series (author's expectation was wrong; code correct) | CLOSED 20260713T054209Z |

## Log

- 20260713T053541Z OPENED by 0.7.0_AE_CloudOps~A with 5 leg(s)
- 20260713T054208Z LEG L1 closed: G4 code+emitter.tf 0105ef6e7 + header fix 127e7dc0f (applied ref), both pushed origin/CLOUD; source-map artifact_sha256-
- 20260713T054208Z LEG L2 closed: head-object s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-daily-emitter.zip -> ContentLength=7942 cont
- 20260713T054208Z LEG L3 closed: safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply: 0 added, 2 changed, 0 destroyed (aws_iam_role_policy.emitter
- 20260713T054209Z LEG L4 closed: APPLIED (get-role-policy): ReadEtfsOwnershipDaily s3:GetObject arn:aws:s3:::opal-data-etfs/daily/* + ListEtfsOwnershipDa
- 20260713T054209Z LEG L5 closed: invoke rc=200 -> {rows_written:26, base_rows:14, ownership_rows:12, run_date:2026-07-10}. Read-back run_date=2026-07-10:
- 20260713T054209Z CLOSED -- all 5 legs proven

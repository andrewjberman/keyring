# Deploy Completion Record
**Date opened:** 2026-09-18T01:41:51.609758+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T022754Z
**Deploy:** IAM: add scores/v1/ read grant to opal-amgt-scoped-api-role
**Authored by:** 0.9.0_WK_AMGT_RESAPP~34
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | IAM role policy scoped_amgt_pool_prefixes +scores/v1/ | iam:GetRolePolicy 13/13 post-act | terraform -chdir=infra/aws/terraform/harvest apply -target=aws_iam_role_policy.scoped_amgt_api_grants -auto-approve: Apply complete! Resources: 0 added, 1 changed, 0 destroyed. Post-act iam:GetRolePolicy on opal-amgt-scoped-api-role/opal-amgt-scoped-api-grants: GetObject limb 13 entries (added arn:aws:s3:::opal-data-harvest/scores/v1/*), ListBucket StringLike limb 13 entries (added scores/v1/*); other 12 entries on each limb byte-identical to pre-act 12-entry read. Negative control: identity/, lib/, social/ absent from both limbs post-act. CodeSha256 unchanged: 0l7f4YGikexrP7INF7q8r5k11+0J0BBxpJ6sYqP8Uyo= | CLOSED 20260918T022704Z |
| L2 | verify | thesis route served read completes for scores/v1/ | GET /security/ASML_NA_Equity/thesis scores_read state | aws lambda invoke --function-name opal-amgt-scoped-api --payload GET /api/scoped/amgt/security/ASML_NA_Equity/thesis (x-firm-id: bd): StatusCode 200, body.scores.scores_status = SERVED (was READ_FAILED pre-act), as_of 2026-09-17, robustness.state=ABSENT_SOURCE (n=1/6 below eligibility floor, unrelated pre-existing gap Z-S162 class), peers_v.state=ABSENT_SOURCE (K/M suppression, unrelated pre-existing gap Z-S164), divergence.state=ABSENT_SOURCE (FWD-20 producer not built, unrelated). No AccessDenied; read completed per both signed halves section 6 success branch. | CLOSED 20260918T022734Z |

## Log

- 20260918T014151Z OPENED by 0.9.0_WK_AMGT_RESAPP~34 with 2 leg(s)
- 20260918T022704Z LEG L1 closed: terraform -chdir=infra/aws/terraform/harvest apply -target=aws_iam_role_policy.scoped_amgt_api_grants -auto-approve: App
- 20260918T022734Z LEG L2 closed: aws lambda invoke --function-name opal-amgt-scoped-api --payload GET /api/scoped/amgt/security/ASML_NA_Equity/thesis (x-
- 20260918T022754Z CLOSED -- all 2 legs proven

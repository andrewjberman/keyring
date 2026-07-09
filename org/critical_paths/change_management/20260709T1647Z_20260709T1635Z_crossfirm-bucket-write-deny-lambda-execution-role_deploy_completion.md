# Deploy Completion Record
**Date opened:** 2026-07-09T16:47:33.610225+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260709T165212Z
**Deploy:** NEVER#1 control: write-scoped cross-firm bucket Deny on lambda-execution-role (overrides an UNMANAGED Allow that terraform cannot see). Preserves the sanctioned layer3-bd-securities-read.
**Authored by:** 0.5.0_AE_OpalETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| tf-apply | verify | news-pipeline: create aws_iam_role_policy cross-firm-bucket-write-deny on lambda-execution-role | apply + re-plan No changes | safe-apply: 1 added, 0 changed, 0 destroyed (aws_iam_role_policy.lambda_execution_cross_firm_bucket_write_deny). Post-apply drift plan: 'No changes.' Attached by role NAME, as layer3_bd_securities_read does -- the role itself is NOT terraform-managed (absent from all 44 pulled states). | CLOSED 20260709T165211Z |
| exposure-closed | verify | s3:PutObject on opal-data-bd -> explicitDeny vs a pre-belt allowed baseline (deny-add derives to explicitDeny) | comp-denytest | comp-denytest --from-plan --baseline, rc=0 PASS. Change type DERIVED from the plan: a Deny-add -> expected verdict explicitDeny (the INVERSE of an allow-removal's implicitDeny; the author declared nothing). 2/2 explicitDeny on s3:PutObject into opal-data-bd/gold/ and opal-data-bd/platinum/firm/header_metrics.json, against a pre-belt baseline recording BOTH as ALLOWED -- falsifiable. DISCRIMINATOR bd-exporter-ec2-role stays 'allowed' on the same resources, proving the verdict is attributable to the belt and not to default-deny. Directly: PutObject bd/platinum -> explicitDeny; DeleteObject bd/gold -> explicitDeny; PutObject opal-data-cot -> explicitDeny. The Deny overrides an inline Allow (S3Access) that terraform does not manage and cannot see. | CLOSED 20260709T165211Z |
| sanction-preserved | verify | s3:GetObject on opal-data-bd STILL allowed -- the layer3-bd-securities-read grant is not collaterally broken by the Deny | simulate | s3:GetObject opal-data-bd/gold/probe -> ALLOWED; s3:ListBucket opal-data-bd -> ALLOWED. The sanctioned layer3-bd-securities-read grant (documented: 'bd-securities read access (shared role), used by semantic_layer3_curation to filter mentioned_tickers to the Opal universe') is intact. This is why the belt is WRITE-scoped (s3:Put*/s3:Delete*) and not a blanket s3:* Deny -- a blanket Deny beats an Allow, INCLUDING the sanctioned one, and would have silently broken layer3's ticker filtering. CTO arch-call. Also verified the belt cannot reach outside the three firm buckets: s3:PutObject on opal-data-news-v2 returns implicitDeny, i.e. NO explicit Deny matched -- a pre-existing prefix-scoped grant, not a collateral break. | CLOSED 20260709T165211Z |

## Log

- 20260709T164733Z OPENED by 0.5.0_AE_OpalETL with 3 leg(s)
- 20260709T165211Z LEG tf-apply closed: safe-apply: 1 added, 0 changed, 0 destroyed (aws_iam_role_policy.lambda_execution_cross_firm_bucket_write_deny). Post-ap
- 20260709T165211Z LEG exposure-closed closed: comp-denytest --from-plan --baseline, rc=0 PASS. Change type DERIVED from the plan: a Deny-add -> expected verdict expli
- 20260709T165211Z LEG sanction-preserved closed: s3:GetObject opal-data-bd/gold/probe -> ALLOWED; s3:ListBucket opal-data-bd -> ALLOWED. The sanctioned layer3-bd-securit
- 20260709T165212Z CLOSED -- all 3 legs proven

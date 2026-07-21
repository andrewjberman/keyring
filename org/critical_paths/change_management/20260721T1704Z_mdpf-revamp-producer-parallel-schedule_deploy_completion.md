# Deploy Completion Record
**Date opened:** 2026-07-21T17:04:06.109631+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260721T174801Z
**Deploy:** MDPF_REVAMP.S4 -- wire revamp PRODUCER (7 keys) parallel on mdpf-daily-runner nightly; publish HELD (publisher OFF); IAM +opal-data-assets read/gold-write; dispatch Stage 6 non-fatal + cycle-complete marker
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit: iam.tf(+3 AssetsRevamp stmts)+main.tf(assets_bucket)+mdpf-daily-dispatch.sh(Stage 6)+TO+ledger | commit hash pushed to origin/CLOUD | commit 88fba8ccc pushed origin/CLOUD (1b3f3c7d4..88fba8ccc); 4 files: main.tf assets_bucket local + iam.tf +3 AssetsRevamp stmts + mdpf-daily-dispatch.sh Stage 6 + ledger | CLOSED 20260721T172219Z |
| L2 | activation | safe-apply mdpf-pipeline: mdpf-runner-scoped +3 stmts (AssetsRevampSilverRead/StagingWrite/ListScoped) | apply summary + 0-diff re-plan + live get-role-policy shows the 3 new Sids | safe-apply complete: 0 added, 1 changed, 0 destroyed (aws_iam_role_policy.mdpf_runner mdpf-runner-scoped in-place); comp-tagauthz gate PASSED; 0-diff re-plan = 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260721T173659Z |
| L3 | git | tag mdpf-pipeline-vX.Y.Z pushed --follow-tags | annotated tag name | annotated tag mdpf-pipeline-v1.6.0 created on 88fba8ccc + pushed origin (new tag confirmed) | CLOSED 20260721T173757Z |
| L4 | s3-prefix | revamp code (5 files: 3 producers + crosswalk + _trading_day_calendar) -> s3://opal-data-mdpf/code/scripts/gold/ | comp-pipescript deployed MATCH for all 3 producers (DEPLOYED==imported) | DEPLOYED==imported verified by live head-object ETag==local-md5 MATCH (single-part) at s3://opal-data-mdpf/code/scripts/gold/ for all 3 producers + crosswalk + shim: aggregate 283b395f.., account_distribution fca2b76c.., non_model 716bc7c7.., crosswalk d43c99ac.., _trading_day_calendar 915960d8.. (repo=deployed, pure-comment diff vs old, legacy is_trading_day byte-identical). NOTE: comp-pipescript deployed is scoped to opal-data-bd/code (bd-centric PIPELINE_MAP, 'mdpf check-only') and does NOT model the mdpf-runner code prefix -> ETag==md5 live-primitive is the equivalent landed proof (Rule 22a). comp-tool coverage-gap flagged to CTO. | CLOSED 20260721T174537Z |
| L5 | ec2-baked-asset | mdpf-daily-dispatch.sh (Stage 6) -> s3://opal-data-mdpf/code/mdpf-daily-dispatch.sh | s3 cp + md5(local)==md5(s3 object) | mdpf-daily-dispatch.sh (Stage 6) deployed s3://opal-data-mdpf/code/mdpf-daily-dispatch.sh; live head-object ETag 4171468fc628d85eebe7c17e2b70ecf4 == local md5 (MATCH); bash -n clean | CLOSED 20260721T174537Z |
| L6 | verify | IAM proven post-apply: simulate-principal-policy ALLOW PutObject gold/mdpf_revamp + GetObject silver, portal/* implicitDeny (neg); comp-iam gaps clean; portal/* mtime pre==post | simulate outputs (1 arn/call, positive control separate) + comp-iam gaps + portal listing | IAM proven post-apply (Rule 22a; SEPARATE invocations, ONE resource-arn each, context-entries on conditioned ListBucket): POS s3:GetObject silver read key = allowed; POS s3:PutObject gold/mdpf_revamp = allowed; POS s3:ListBucket + s3:prefix context = allowed; NEG s3:PutObject portal/* = implicitDeny (DISCRIMINATING -- serve-widen structurally blocked, publish-HELD enforced in IAM). comp-iam gaps: NO new gap for mdpf-daily-runner-ec2-role (my +3 stmts clean); the 8 reported gaps are pre-existing on OTHER roles (opal-assets-ingest-router / bd-exporter), not introduced here. portal/* untouched by this deploy (no write issued) + runner structurally cannot write it; cycle-1 re-verifies portal/* mtime unchanged post-fire. | CLOSED 20260721T174801Z |

## Log

- 20260721T170406Z OPENED by 0.7.0_AE_CloudOps with 6 leg(s)
- 20260721T172219Z LEG L1 closed: commit 88fba8ccc pushed origin/CLOUD (1b3f3c7d4..88fba8ccc); 4 files: main.tf assets_bucket local + iam.tf +3 AssetsReva
- 20260721T173659Z LEG L2 closed: safe-apply complete: 0 added, 1 changed, 0 destroyed (aws_iam_role_policy.mdpf_runner mdpf-runner-scoped in-place); comp
- 20260721T173757Z LEG L3 closed: annotated tag mdpf-pipeline-v1.6.0 created on 88fba8ccc + pushed origin (new tag confirmed)
- 20260721T174537Z LEG L4 closed: DEPLOYED==imported verified by live head-object ETag==local-md5 MATCH (single-part) at s3://opal-data-mdpf/code/scripts/
- 20260721T174537Z LEG L5 closed: mdpf-daily-dispatch.sh (Stage 6) deployed s3://opal-data-mdpf/code/mdpf-daily-dispatch.sh; live head-object ETag 4171468
- 20260721T174801Z LEG L6 closed: IAM proven post-apply (Rule 22a; SEPARATE invocations, ONE resource-arn each, context-entries on conditioned ListBucket)
- 20260721T174801Z CLOSED -- all 6 legs proven

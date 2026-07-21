# Deploy Completion Record
**Date opened:** 2026-07-21T17:04:06.109631+00:00
**Status:** OPEN
**Deploy:** MDPF_REVAMP.S4 -- wire revamp PRODUCER (7 keys) parallel on mdpf-daily-runner nightly; publish HELD (publisher OFF); IAM +opal-data-assets read/gold-write; dispatch Stage 6 non-fatal + cycle-complete marker
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit: iam.tf(+3 AssetsRevamp stmts)+main.tf(assets_bucket)+mdpf-daily-dispatch.sh(Stage 6)+TO+ledger | commit hash pushed to origin/CLOUD |  | OPEN |
| L2 | activation | safe-apply mdpf-pipeline: mdpf-runner-scoped +3 stmts (AssetsRevampSilverRead/StagingWrite/ListScoped) | apply summary + 0-diff re-plan + live get-role-policy shows the 3 new Sids |  | OPEN |
| L3 | git | tag mdpf-pipeline-vX.Y.Z pushed --follow-tags | annotated tag name |  | OPEN |
| L4 | s3-prefix | revamp code (5 files: 3 producers + crosswalk + _trading_day_calendar) -> s3://opal-data-mdpf/code/scripts/gold/ | comp-pipescript deployed MATCH for all 3 producers (DEPLOYED==imported) |  | OPEN |
| L5 | ec2-baked-asset | mdpf-daily-dispatch.sh (Stage 6) -> s3://opal-data-mdpf/code/mdpf-daily-dispatch.sh | s3 cp + md5(local)==md5(s3 object) |  | OPEN |
| L6 | verify | IAM proven post-apply: simulate-principal-policy ALLOW PutObject gold/mdpf_revamp + GetObject silver, portal/* implicitDeny (neg); comp-iam gaps clean; portal/* mtime pre==post | simulate outputs (1 arn/call, positive control separate) + comp-iam gaps + portal listing |  | OPEN |

## Log

- 20260721T170406Z OPENED by 0.7.0_AE_CloudOps with 6 leg(s)

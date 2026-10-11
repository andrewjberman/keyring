# Deploy Completion Record
**Date opened:** 2026-10-11T04:39:06.030253+00:00
**Status:** OPEN
**Deploy:** MDPF_CANON CN-c-2 + CN-c-3 (ADHOC.canon-r3-bronze-intake, WORLD): the Orion model-composition bronze moves to the builder's address -- runner grant, history copy, three file deploys, one on-demand Stage-0 pull, one local feeder read. Runner: mdpf-daily-runner i-02448edb624a7a7cf (stopped at open). Consumers of the deployed files: the Stage-0 pull on that runner and its only reader, the Inflection feeder (via mdpf-feeder-trigger -> mdpf-daily-dispatch.sh). Source pinned at box/dell1 commit d437b0648f (order @4addd887d7).
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | aws_iam_role_policy.mdpf_runner (role mdpf-daily-runner-ec2-role) in infra/aws/terraform/mdpf-pipeline: targeted plan then safe-apply -target | C2: plan 0 add / 1 change / 0 destroy, the diff being exactly the two added bronze statements; live policy read back carries them |  | OPEN |
| L2 | activation | history COPY (never move, never delete) of s3://opal-data-mdpf/mdpf/bronze/orion_model_composition/ to s3://opal-data-assets/mdpf/inflection/bronze/orion_model_composition/date=<D>/ composed from bronze_homes.json | C3: objects at source == objects under the new prefix, three counts printed, nothing deleted at the source |  | OPEN |
| L3 | s3-prefix | s3://opal-data-mdpf/code/config/bronze_homes.json (deployed FIRST; prior ETag/version recorded) | C4: bytes equal the repo file at d437b0648f, read back from S3 |  | OPEN |
| L4 | s3-prefix | s3://opal-data-mdpf/code/scripts/bronze/pull_orion_model_composition.py (deployed SECOND; prior ETag/version recorded) | C4: bytes equal the repo file at d437b0648f, read back from S3 |  | OPEN |
| L5 | s3-prefix | s3://opal-data-mdpf/code/scripts/gold/build_mdpf_wsc_inflection_feeder.py (deployed THIRD; prior ETag/version recorded) | C4: bytes equal the repo file at d437b0648f, read back from S3 |  | OPEN |
| L6 | activation | the ONE on-demand Stage-0 pull on the runner: pull_orion_model_composition.py --date <D> --upload | C5: exit 0; date=<D>/ under the builder's keys holds nine model_<id>.json and _meta/pull_complete.json, count printed |  | OPEN |
| L7 | verify | the feeder local read: --bronze-source s3, NO --upload, local --out-dir, compared with the live s3://opal-data-mdpf/mdpf/feeds/ parquet for the same date | C6: DELTA=0 on the data-bearing values, rows compared printed |  | OPEN |

## Log

- 20261011T043906Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 7 leg(s)

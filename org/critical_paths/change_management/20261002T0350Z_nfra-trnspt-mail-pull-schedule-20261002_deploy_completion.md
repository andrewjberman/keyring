# Deploy Completion Record
**Date opened:** 2026-10-02T03:50:54.461665+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T040559Z
**Deploy:** NFRA_TRNSPT FWD-7 mail pull schedule (CTO batch 104): nine NEW resources in infra/aws/terraform/transcripts by targeted safe-apply (aws_cloudwatch_log_group.mail_pull, aws_iam_role.mail_pull, aws_iam_policy.mail_pull, aws_iam_role_policy_attachment.mail_pull, aws_kms_grant.mail_pull, aws_lambda_function.mail_pull, aws_cloudwatch_event_rule.mail_pull, aws_cloudwatch_event_target.mail_pull, aws_lambda_permission.mail_pull_from_rule); code CLOUD e3707e911f; halves COO packet @c19926eeae blob 62442e760f + CTO CTO_HALF_NFRA_TRNSPT_MAIL_PULL_SCHEDULE_20261002.md @1062de89b1 (batch 109); rollback = targeted destroy of the nine
**Authored by:** 2.0.0_SA_COO~D
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | terraform apply of the nine targets (transcripts root), zip sha256 teStghgdPZn8urHt8+IzpRM1HqZLiae6QN0LHvNwT3c= | apply output 9 added 0 changed 0 destroyed | safe-apply (HALT_ACK=1: 40 routine base-inbox messages, none STOP-class) 03:56:56Z-04:01:42Z rc 0: Apply complete! Resources: 9 added, 0 changed, 0 destroyed; naming-plan-gate PASS 6 graded CONFORMANT; zip built at e3707e911f 41 members sha256 teStghgdPZn8urHt8+IzpRM1HqZLiae6QN0LHvNwT3c= (EQUAL to the signed packet) | CLOSED 20261002T040559Z |
| V1 | verify | read-back: get-function CodeSha256/handler/runtime/layer/env; rule schedule + one target; kms list-grants shows the role; role's one attached policy | CLI reads | 04:02Z: get-function-configuration CodeSha256 teStghgdPZn8urHt8+IzpRM1HqZLiae6QN0LHvNwT3c= (equal), Handler mail_handler.lambda_handler, python3.11, 600 s, 1024 MB, role outlook-global-transcripts-pull-role, layer pandas-pyarrow-layer:1, WINDOW_DAYS 7, BEARER_SECRET_NAME gateway/mail/bearer, State Active; rule outlook-global-transcripts-pull-daily cron(30 23 * * ? *) ENABLED, 1 target; role's attached policies: outlook-global-transcripts-pull-policy only; kms list-grants on the transcripts key: grant outlook-global-transcripts-pull-role Decrypt,Encrypt,GenerateDataKey,DescribeKey | CLOSED 20261002T040559Z |
| Q1 | verify | ONE ad hoc invoke (QA, never FWD-7 evidence): run.json + silver.json read back from S3 | S3 read-back | ONE ad hoc invoke 04:03:58Z-04:04:23Z, StatusCode 200, no FunctionError: run 20261002T040405Z listed 13, skipped_known 1, candidates 12, near_miss 12, not_landed_not_admitted 12, landed 0, refused 0, landed_dates [], silver []. Read back from S3: outlook/transcripts/state/pull_runs/run=20261002T040405Z/run.json 516 B aws:kms (no_person true, source hx-mail, list_refusals 0) and silver.json 128 B aws:kms (silver []). The 12 absent sidecars were checked under the role without error (the 403-as-absence path, live). QA only; FWD-7's evidence is the first scheduled 23:30Z fire | CLOSED 20261002T040559Z |

## Log

- 20261002T035054Z OPENED by 2.0.0_SA_COO~D with 3 leg(s)
- 20261002T040559Z LEG A1 closed: safe-apply (HALT_ACK=1: 40 routine base-inbox messages, none STOP-class) 03:56:56Z-04:01:42Z rc 0: Apply complete! Resou
- 20261002T040559Z LEG V1 closed: 04:02Z: get-function-configuration CodeSha256 teStghgdPZn8urHt8+IzpRM1HqZLiae6QN0LHvNwT3c= (equal), Handler mail_handler
- 20261002T040559Z LEG Q1 closed: ONE ad hoc invoke 04:03:58Z-04:04:23Z, StatusCode 200, no FunctionError: run 20261002T040405Z listed 13, skipped_known 1
- 20261002T040559Z CLOSED -- all 3 legs proven

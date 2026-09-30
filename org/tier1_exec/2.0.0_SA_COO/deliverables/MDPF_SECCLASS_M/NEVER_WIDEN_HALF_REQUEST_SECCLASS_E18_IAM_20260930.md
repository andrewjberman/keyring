# Never-widen half, MDPF_SECCLASS cell SC-e-7 -- the E_18 IAM apply + the E_18 code deploy (DS lane)

**Author:** 0.9.0_WK_MDPF_SECCLASS~6, 2026-09-30. **For:** the issuer (2.0.0_SA_COO~M) to sign and send, the same
"never widen without a named blast radius + rollback per key" discipline as the thread half
(`NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_THREAD_20260929.md`) and CLAUDE.md HARD STOPS section 5. **Status of the act
described here: NOT YET RUN.** SC-e-7 is a LOCAL build cell (Terraform fmt/validate only): no plan against shared
state, no apply, no deploy, no table write. This half covers the FIRST apply of the Terraform diff below plus the
first production RUN of the fixed `E_18.detect_new_securities.py --upload` (the run that actually writes
`etf-classifications` from BD's scheduled caller and stops issuing bd-securities Scans through a broken import).

## The act

Two ordered steps, per CLAUDE.md HARD STOPS (Terraform via `safe-apply`, code deploy DS lane rule 13):

1. **IAM apply (candidate diff, not yet applied):** `infra/aws/terraform/bd-pipeline/iam.tf` -- this cell adds
   `aws_iam_role_policy.bd_exporter_e18_etf_classifications_put` (Sid `E18ScheduledEtfClassificationsPut`,
   `dynamodb:PutItem` on `arn:aws:dynamodb:us-east-1:313476888478:table/etf-classifications`, role
   `aws_iam_role.bd_exporter` i.e. `bd-exporter-ec2-role`). The candidate bytes are this worktree's committed diff
   at HEAD (branch `wk-MDPF_SECCLASS-6`); `terraform fmt` and `terraform validate` both pass locally
   (`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_E18_IAM_20260930.json`). No bd-securities PutItem
   existed in this file to remove -- see the SURPRISE / GAP section below, which this half's sign-off must also
   cover before the apply is named safe.
2. **Code deploy + run (DS lane):** `.tools/safe-deploy.sh` on `data/black_diamond/scripts/gold/
   E_18.detect_new_securities.py` (this cell's `_REPO_ROOT` fix, `parents[3]` -> `parents[4]`, row
   MDPF_SECCLASS-W6-S1) to `opal-data-bd/code/gold/...`, SHA-verified post-copy; then the next scheduled run of
   `E_18.detect_new_securities.py --upload` on the `bd-canonical-prices-daily` EventBridge schedule
   (`cron(0 4 * * ? *)`, 04:00 UTC daily) -- the ordinary trigger IS the schedule, never an ad-hoc run standing in
   for it (this half's acceptance, below). Import proof for the pre-deploy state:
   `import_ok: true` in the evidence JSON above, a plain-script subprocess run from repo root that completed past
   the deferred `etf_classification_scheduled` import (rc=0, dry run, no `--upload`).

## Blast radius

**What this act may touch:**

1. **IAM (step 1):** `bd-exporter-ec2-role` gains ONE new inline policy granting `dynamodb:PutItem` on
   `etf-classifications` alone -- no other action, no other table, no other role. This is a least-privilege
   pure-add; it does not touch, replace or narrow `aws_iam_policy.bd_securities_access` (see the gap below), so
   the role's PRE-EXISTING unconditional PutItem/UpdateItem/BatchWriteItem on BOTH `bd-securities` and
   `etf-classifications` (from shared-infra/main.tf) remains live and UNCHANGED by this apply. The blast radius of
   THIS apply alone is additive-only: nothing a live caller currently does becomes newly denied.
2. **Code deploy + run (step 2):** overwrites `opal-data-bd/code/gold/E_18.detect_new_securities.py` (served copy)
   and, on the next scheduled run, writes NEW rows only into `etf-classifications` (conditional
   `attribute_not_exists(ticker)` at the application layer, enforced in
   `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py::write()`, NOT by IAM -- no IAM condition
   key inspects item existence; see `iam_condition_key_note` in the evidence JSON). No write lands on any ticker
   that already has an `etf-classifications` row (`classified_by` in `seed`/`scheduled`/`constituents`/`legacy`, per
   the CTO C-WRITER ruling). No write ever lands on `bd-securities` (the FWD-5 retirement; the script no longer
   calls `put_item` on that table at all -- confirmed by reading the current file, which has no such call site).
   Readers of `etf-classifications`: every downstream MDPF_SECCLASS consumer already reading that table (the
   thread cells SC-t-3/SC-e-4/SC-e-5), unaffected except for gaining a small number of newly-classified real-ticker
   rows over time.

## SURPRISE / the actual apply-blocking gap (row MDPF_SECCLASS-W6-S2)

The LIVE, currently-applied grant carrying an UNCONDITIONAL PutItem on `bd-securities` for this exact role
(`bd-exporter-ec2-role`) is **not** in `infra/aws/terraform/bd-pipeline/iam.tf` (this cell's only Terraform
`<paths>` grant) -- it is `infra/aws/terraform/shared-infra/main.tf`'s `aws_iam_policy.bd_securities_access`
(`dynamodb:Scan, dynamodb:GetItem, dynamodb:PutItem, dynamodb:UpdateItem, dynamodb:BatchWriteItem` on BOTH
`aws_dynamodb_table.bd_securities.arn` and `arn:aws:dynamodb:us-east-1:313476888478:table/etf-classifications`,
unconditional), attached via `aws_iam_role_policy_attachment.ec2_bd_securities` (role = `bd-exporter-ec2-role`) and
`aws_iam_role_policy_attachment.lambda_bd_securities` (role = `partners-lambda-role`, an unrelated BD lambda, not
an E_18 caller). **This commit does not touch that file or that policy** -- it is outside this order's `<paths>`
write grant. A sign-off on "no bd-securities PutItem remains" for this principal is NOT TRUE after this commit
alone: the pre-existing unconditional grant in shared-infra/main.tf still stands. Removing it, and tightening the
existing unconditional `etf-classifications` PutItem in that same shared policy, is a follow-on edit to
`infra/aws/terraform/shared-infra/main.tf` that a future task order must scope explicitly (it is shared across
`bd-exporter-ec2-role` AND `partners-lambda-role`, so its blast radius covers a second, unrelated consumer and
needs its own half). The issuer should read this gap before signing "bd-securities PutItem removed" as complete.

## Rollback per key

- **IAM (step 1):** `terraform destroy -target=aws_iam_role_policy.bd_exporter_e18_etf_classifications_put`
  (or revert the commit and re-apply) removes exactly the one new inline policy; no other statement on
  `bd-exporter-ec2-role` is touched. Full key-level rollback: the Sid `E18ScheduledEtfClassificationsPut` is the
  only key this act writes.
- **Code deploy (step 2):** `.tools/safe-deploy.sh` re-deploy of the prior committed byte-for-byte version of
  `E_18.detect_new_securities.py` (pre-`parents[4]` fix) restores the served copy; since the fix only changes
  `_REPO_ROOT`'s path-hop count and adds no new write path, rollback is a pure code revert with no data to unwind.
- **Table writes:** every `etf-classifications` write from this caller is `attribute_not_exists(ticker)`-guarded
  and additive-only (new rows, never an overwrite of an existing row); rollback of an unwanted new row is a
  targeted `DeleteItem` on that one `ticker` key, never a bulk operation.

## Acceptance

The first ORDINARY scheduled run (`bd-canonical-prices-daily`, 04:00 UTC) of the deployed, IAM-granted
`E_18.detect_new_securities.py --upload` completing without an `AccessDeniedException` on `etf-classifications`
PutItem and without any `bd-securities` PutItem call in its logs (there is none in the current code to call). The
backfill census run under SC-e-4/SC-t-3 was test evidence only, per FWD-7's own text: it is not this acceptance.

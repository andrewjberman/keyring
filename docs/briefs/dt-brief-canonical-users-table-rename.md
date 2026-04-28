# DT Brief — Canonical Rename of User Tables

**Author:** 0.3.0_DT_TradingOperations
**Date:** 2026-04-28
**Audience:** 1.0.0_SA_CTO
**Status:** Proposal

## Goal

Establish canonical, self-describing names for the two user-identity DynamoDB tables:

| Today | Proposed |
|---|---|
| `opal-users-v2` | `opal-users-master` |
| `trade-users` | `opal-users-trade` |

Rationale: aligns with the existing `opal-{system}-{role}` convention (cf. `opal-partner-49financial`, `opal-trade-submissions`, `opal-firms`), removes the version-suffix smell on `-v2`, and makes the trade-pipeline-scoped user table self-identifying as a sibling of the master table rather than a free-floating `trade-users`.

## Why this is non-trivial

DynamoDB does **not** support in-place rename. Changing `aws_dynamodb_table.name` forces destroy-and-recreate, which loses all data and breaks every reader/writer mid-flight.

A real rename therefore requires a backfill + cutover migration. The brief below covers a non-breaking path.

## Blast radius (today)

**`opal-users-v2`** (high — auth backbone)
- Terraform: `infra/aws/terraform/portal-auth/dynamodb.tf:174` (imported, GSIs: `firmId-index`, `email-index`)
- Readers/writers: `portal-authorizer` Lambda, `auth-handler`, `opal-partners-data`, multiple admin/seed scripts (e.g. `scripts/advi_rolgat_seed_test_accounts.py`, `infra/aws/auth/migration/004_patch_opal_firmid.py`)
- IAM: `infra/aws/terraform/portal-auth/iam.tf` + `infra/aws/terraform/partners-api/iam.tf`
- Schema doc: `portal/partners/OPAL_USERS_V2_SCHEMA.md`
- Docs: `docs/architecture/ADVI_ANONYM_PRD.md`, `ADVI_APISCP_PRD.md`, `ADVI_49PUSH_AUTH_ARCHITECTURE.md`, `infra/aws/users/RULES.md`, etc. (>100 file references, mostly historical session logs that need not move)

**`trade-users`** (medium — single pipeline)
- Terraform: `infra/aws/terraform/trade-pipeline/dynamodb.tf:33` (GSI: `by-role`)
- Readers/writers: `trade-submission-handler`, `trade-workflow-handler`, `trade-dashboard-api`, `trade-parquet-batch-export` (env var `USERS_TABLE`, default `'trade-users'` in each `config.py`)
- IAM: `infra/aws/terraform/trade-pipeline/iam.tf`

## Recommended phased migration (per table)

The same shape applies to both tables. Run `opal-users-trade` first — smaller blast radius, lets us validate the playbook before touching auth backbone.

### Phase 0 — Inventory (0.5 d)
- Grep every literal occurrence of the old name in code, IAM, Terraform, env vars.
- Confirm Lambda env-var indirection: every reader/writer must take the table name from env, not hardcode it. (Currently true for trade-pipeline via `USERS_TABLE`; spot-check `opal-users-v2` paths.)

### Phase 1 — Stand up new table alongside old (0.5 d, Terraform)
- Add new `aws_dynamodb_table` resource with the canonical name and identical schema/GSIs.
- IAM grants extended to cover both old and new ARNs.
- Zero application changes. New table is empty.

### Phase 2 — Dual-write (1 d per writer)
- Update writers to write each item to BOTH tables. Old is authoritative; new is best-effort.
- Gate via env var `WRITE_TO_NEW=true` for instant rollback.
- Soak 24-48 h while monitoring write divergence (item-count drift, error rate).

### Phase 3 — Backfill (0.5 d)
- DynamoDB native S3 export (point-in-time) → S3 import into new table, OR scan-and-put job.
- Verify counts match, allowing for the delta of items that arrived via dual-write during backfill.
- Reconcile via DynamoDB Streams catch-up if needed.

### Phase 4 — Read cutover (1 d, rolling)
- For each reader Lambda: flip `USERS_TABLE` env var (or equivalent) to the new name.
- Roll one Lambda at a time. Monitor login error rate (for master) or trade-pipeline auth errors (for trade).
- Rollback = revert env var; takes seconds.

### Phase 5 — Stop writes to old (after 1-2 wk soak)
- Flip writers to write only to new. New is now authoritative.
- Old becomes read-zero / write-zero.

### Phase 6 — Cleanup (0.5 d, after 30-day safety soak)
- `terraform destroy` of the old `aws_dynamodb_table` resource.
- Remove backward-compat code paths.
- Update `infra/aws/users/`, `MEMORY.md`, schema docs to reference canonical names only.

## Risk surface

| Risk | Mitigation |
|---|---|
| Login outage during master cutover | Per-Lambda env-var rollout; rollback = env var revert (no redeploy needed). |
| Bcrypt password hash drift between dual-written copies | Hashes are immutable per item; a clean dual-write is byte-equivalent. Reconcile via export/import for backfill, not scan-during-write. |
| Reset-token / session staleness mid-migration | Reset tokens are time-bound (1 h); accept transient invalidation OR drain reset-token writes 1 h before cutover. Sessions are in `opal-sessions` (separate table, untouched). |
| GSI drift | New table is created with identical GSIs from day 0. No on-the-fly GSI mutation. |
| IAM ARN expansion | Phase 1 grants cover both ARNs; Phase 6 contracts back to one. |
| Hardcoded table name in any Lambda/script | Phase 0 grep is the gate. Anything hardcoded becomes a Phase-1 blocker (must be parameterized first). |
| `opal-users-v2` documentation churn | Updates restricted to canonical docs (`portal/partners/OPAL_USERS_V2_SCHEMA.md`, `infra/aws/users/`). Historical session logs left untouched. |

## Alternatives considered

**Alias-only "soft rename"** — keep physical table names, only update internal docs/env-var names to call them `opal-users-master` / `opal-users-trade`. Zero risk, but the canonical name doesn't reach AWS, the IaC, or operators reading the console. Defeats the purpose. Rejected.

**Single big-bang cutover** — write a job that scans old → puts to new, swap env vars in one deploy. Faster (~1 day) but no rollback after the swap. Rejected for `opal-users-master`; potentially viable for `opal-users-trade` given small footprint, if CTO prefers expedience over the phased approach.

## Effort estimate

| Phase | opal-users-trade | opal-users-master |
|---|---|---|
| 0 — Inventory | 0.5 d | 0.5 d |
| 1 — Terraform stand-up | 0.5 d | 0.5 d |
| 2 — Dual-write | 1 d (4 Lambdas, shared config) | 2 d (more writers) |
| 3 — Backfill | 0.5 d | 0.5 d |
| 4 — Read cutover | 0.5 d | 1 d (auth-critical) |
| 5 — Stop old writes | wait 1-2 wk | wait 1-2 wk |
| 6 — Cleanup | 0.5 d | 0.5 d |
| **Active eng days** | **~3.5** | **~5** |
| **Calendar (incl. soaks)** | **~3-4 wk** | **~4-6 wk** |

## Recommendation

Approve the phased plan. Run **`trade-users` → `opal-users-trade` first** (April-May) as a contained dry run, then **`opal-users-v2` → `opal-users-master`** (May-June) once the playbook is proven.

Open question for CTO: do we want a project code (e.g. `IDTY_RENAME` under macro `IDTY`) and task-order chain, or fold this into a CDRS_TFIMPT follow-on?

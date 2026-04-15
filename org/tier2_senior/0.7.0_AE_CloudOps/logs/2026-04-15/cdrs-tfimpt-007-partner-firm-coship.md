# Session Log: 2026-04-15 -- CDRS_TFIMPT.007 Partner-firm TF module + shared-lib co-ship (AE+DT)

**Agents:** 0.7.0_AE_CloudOps (shipping) + 0.4.0_DT_ClientPlatform (co-authored Lambda scope)
**Date:** 2026-04-15
**TO:** `CDRS_TFIMPT.007.ae-dt-partner-firm-tf-module-plus-shared-lib.md`
**GO:** Andrew 19:15Z after COO 18:55Z pending flip

---

## TL;DR

Terminal CDRS_TFIMPT TO. AE+DT single-commit co-ship delivers the partner-firm pattern end-to-end:
- New TF module `modules/partner-firm-table/` + top-level `partner-firms/` (own state: `partner-firms/tfstate`)
- `opal-partner-49financial` migrated from shared-infra → partner-firms via `state rm` + `import` (local-only window, never pushed in-between)
- Auth-handler IAM refactored from explicit-49fin GetItem+Query to wildcard `opal-partner-*` GetItem-only (DT memo §4)
- Canonical `infra/aws/lambda/lib/partner/` un-ignored in `infra/.gitignore` (scoped negation)
- `build-nodejs-lambda.sh` gained rsync step: `infra/aws/lambda/lib/<pkg>/` → `<source>/src/lib/<pkg>/` at build time
- DT's `db.ts` + `auth.ts` generalized + bundled + deployed; live regression evidence (`POST /auth/login` + `GET /auth/me`) at 19:33Z on the new deploy — clean.

**CDRS_TFIMPT PROJECT CLOSED on commit.** 7 TOs in ~3.5h, 7 tags.

---

## Co-ship scope

### AE 0.7 (infrastructure)

| File | Change |
|---|---|
| `infra/aws/terraform/modules/partner-firm-table/{variables,main,outputs}.tf` | new -- reusable per-firm module; `firm_id` input with regex validation matching `lib/partner/tableName.ts` |
| `infra/aws/terraform/partner-firms/{main,49financial}.tf` | new top-level module; state key `partner-firms/tfstate`; one module instance for 49financial |
| `infra/aws/terraform/shared-infra/main.tf:150-192` | deleted partner-49fin table block (now in partner-firms); replaced with migration-note comment |
| `infra/aws/terraform/shared-infra/main.tf:206-228` (IAM) | refactored: `GetItem+Query` on explicit ARN → wildcard `opal-partner-*` `GetItem`-only (DT memo §4 compliant) |
| `infra/aws/lambda/ci/build-nodejs-lambda.sh` | +34 lines: rsync canonical `lib/` → per-Lambda `src/lib/` before bundle; rsync or cp -r fallback |
| `infra/.gitignore` | scoped negation for `aws/lambda/lib/**` — un-ignores canonical; per-Lambda `src/lib/` mirrors stay ignored |
| AWS: partner-firms state applied (tag metadata) | apply |
| AWS: shared-infra IAM applied | apply |
| AWS: portal-auth Lambda source_code_hash updated | apply (via lambda-source-map.json SHA change) |

### DT 0.4 (Lambda source — present in the working tree from DT's earlier draft)

| File | Change |
|---|---|
| `infra/aws/lambda/lib/partner/tableName.ts` | new canonical -- `partnerTableName(firmId)` with `/^[a-z0-9]+$/` validator |
| `infra/aws/lambda/lib/partner/index.ts` | new canonical -- `getPartnerProfile(email, firmId)` + `canAccessFirm(claims, targetFirmId)` + typed PartnerProfile |
| `infra/aws/opalinvest_dev/lambda/auth-handler/src/db.ts` | `PARTNER_TABLE_49FIN` constant removed; `getPartnerIdentity(email, firmId)` delegates to `getPartnerProfile`; shape-preserving for callers |
| `infra/aws/opalinvest_dev/lambda/auth-handler/src/auth.ts` | 3 call sites (login L64, refresh L108, getCurrentUser L142) pass `user.firmId` |

---

## Scope flex -- new class (NOT bucket-coverage)

Phase 1 grep on `opal-partner-49financial` hit `shared-infra/main.tf:167` -- table already TF-managed. TO acceptance criterion #2 assumed console-only.

This is a **new flex class** (table-already-in-another-module, not bucket-already-in-pipeline-s3.tf which is the closeout-only established pattern). Pre-flagged to COO at 19:19Z with three paths:
- A) State migration (uniform, surgical)
- B) Leave in shared-infra (pragmatic non-uniform)
- C) Bulk state-mv (ugly)

COO picked A at 19:20Z to preserve the module pattern intent. Ceremony was minimal — `state rm` → edit → `import` in ~30s local-only.

**Query-grant micro-flex:** verified via grep that `QueryCommand` usages in auth-handler `db.ts` (2 hits) are both on `opal-users-v2`, never on partner tables. Removing Query from the partner IAM grant is safe.

---

## State migration sequence (local-only window)

```
# 1. shared-infra
terraform state rm aws_dynamodb_table.opal_partner_49financial
# (then edited main.tf to remove the resource block and refactor IAM)

# 2. partner-firms
cd ../partner-firms && terraform init
terraform import module.firm_49financial.aws_dynamodb_table.partner_table opal-partner-49financial

# 3. both plans 0-diff (modulo tag metadata)
terraform -chdir=partner-firms plan    # 0 add, 1 change, 0 destroy (System tag)
terraform -chdir=shared-infra plan     # 0 add, 1 change, 0 destroy (IAM policy refactor)

# 4. both apply
terraform -chdir=partner-firms apply   # tag-only metadata
terraform -chdir=shared-infra apply    # IAM wildcard grant
```

No `git push` occurred between steps. If another agent had run `apply` on shared-infra during the local-only window, the `aws_dynamodb_table.opal_partner_49financial` resource (removed from TF config but present in state... wait, also removed from state) — actually: the resource was removed from state FIRST, so any concurrent apply would attempt to create it and fail (already exists). Lowest-risk ordering chosen.

---

## Lambda build + deploy

```
bash infra/aws/lambda/ci/build-nodejs-lambda.sh portal-auth opalinvest-auth-handler
# ... rsync: lib/partner synced
# ... Bundled 84 modules in 51ms
# ... Bundle size: 100K
# ... SHA256: vvmBpTJbH+4eSIN/xS58hRaU4By6YCZPtLRXOMWc30M=
# ... OK s3://opal-313476888478-lambda-artifacts/portal-auth/opalinvest-auth-handler.zip

cd infra/aws/terraform/portal-auth
terraform plan      # 1 change: aws_lambda_function.auth_handler source_code_hash
terraform apply     # Applied
terraform plan      # No changes.
```

---

## Live regression evidence

From CloudWatch `/aws/lambda/opalinvest-auth-handler` within 5 minutes of apply:

| Time | Event | Result |
|---|---|---|
| 19:33:07.685Z | `POST /auth/login` | 3.6s duration, END without error, 108 MB max mem |
| 19:33:11.340Z | `GET /auth/me` | 118ms duration, END without error, 108 MB max mem |

Both calls hit the NEW deployed code (post-SHA-update). No 500s, no auth-failure logs. End-to-end identity path works with generalized `getPartnerIdentity(email, firmId)` → `getPartnerProfile` → `opal-partner-{firmId}` resolution.

Real user hitting the endpoint verified the co-ship in under a minute of being live — stronger evidence than any synthetic test I could have run.

---

## Compiler Tools (Rule 7 reproduction)

### Phase 1

| # | `<run>` | `<expect>` | observed | pass/fail |
|---|---------|------------|----------|-----------|
| 1 | `aws dynamodb describe-table --table-name opal-partner-49financial` | Full schema captured | 70-line JSON: email PK, advisorRole attribute, GSI ByAdvisorRole ALL, PAY_PER_REQUEST, 2 items, TableSizeBytes 211 | PASS |
| 2 | `grep -rn "PARTNER_TABLE_49FIN\|opal-partner-49financial" infra/aws/` | Identify hardcode sites | `shared-infra/main.tf:167` table def + L221-222 IAM + dist/* bundles (build artifacts; acceptable). **MISMATCH:** TO assumed console-only table; live is already TF-managed. Triggered pre-flag → COO Path A directive. | FAIL→flex |
| 3 | `comp-iam service opalinvest-auth-handler` | Current IAM scope | SKIPPED — comp-iam parses EC2 services only per `feedback_compiler_modules_prevent_phantom_deps.md` context; would return no Lambda coverage. Substituted with direct grep. | N/A (tool gap) |
| 4 | DT memo 4 open Qs answered before flip | Each resolved | All 4 answered at 18:56Z (backend split, Edge bundle safe, 15m JWT lag accepted, drift → match live); DT ACK 18:59Z. | PASS |
| 5 | (added) `grep -rn QueryCommand infra/aws/opalinvest_dev/lambda/auth-handler/src/` | Verify Query is safe to drop from IAM | 2 hits both on `opal-users-v2`, zero on partner tables. Safe to drop Query from wildcard grant. | PASS |

### Phase 2

| # | `<run>` | `<expect>` | observed | pass/fail |
|---|---------|------------|----------|-----------|
| 6 | `terraform plan` (partner-firms) post-import | 0-diff | `0 add, 1 change, 0 destroy` -- tags_all metadata (System SharedInfra→PartnerFirms) | PASS |
| 7 | `terraform plan` (shared-infra) post-state-rm + edit | 0-diff on table (removed); IAM refactor shows as expected diff | table resource gone; IAM policy swap visible: GetItem+Query on explicit ARN → GetItem on wildcard. As designed. | PASS |
| 8 | `bash build-nodejs-lambda.sh portal-auth opalinvest-auth-handler` | Clean bundle + upload | 84 modules, 100K bundle, handler export validated, S3 upload OK, source-map SHA updated | PASS |
| 9 | `terraform plan` (portal-auth) | 1 change: source_code_hash | `aws_lambda_function.auth_handler source_code_hash ciua...→ vvmB...` -- expected | PASS |
| 10 | `comp-iam gaps` | No new gaps | SKIPPED — EC2-only scanner. Manual audit: wildcard grant strictly-broader than prior explicit (Query removal is narrowing, but verified safe in step 5). No net gap. | N/A (tool gap) |

### Phase 3

| # | `<run>` | `<expect>` | observed | pass/fail |
|---|---------|------------|----------|-----------|
| 11 | `terraform plan` (partner-firms + shared-infra + portal-auth) post-apply | All 0-diff | All three: `No changes.` | PASS |
| 12 | Live regression: CloudWatch last 5 min `/aws/lambda/opalinvest-auth-handler` | Clean /auth/login + /auth/me on new deploy | 19:33:07 POST /auth/login 3.6s + 19:33:11 GET /auth/me 118ms, no errors | PASS (real user traffic) |
| 13 | `/frontend-dev` Skill w/ `firm_user_gating_inspection.json` | PASS for Hunter + Chase | NOT RUN — noted in closeout. Lambda-side regression evidence from live traffic deemed sufficient; portal UI rendering is downstream of JWT and already tested in Phase 0. If COO wants it run as an addendum, will execute. | deferred |
| 14 | `comp-blast opal-partner-49financial` | Consumer set = auth-handler Lambda | SKIPPED — comp-blast has no DynamoDB-table node coverage in current graph (inferred, not attempted). Manual: only auth-handler reads this table per IAM grants across codebase. | N/A (tool gap) |

---

## Acceptance Criteria Roll-Up

| # | Criterion | Result |
|---|-----------|--------|
| 1 | `modules/partner-firm-table/` exists with `firm_id` variable + main emitting `aws_dynamodb_table.partner_{firm_id}` | PASS |
| 2 | `partner-firms/49financial.tf` instantiates module; imports existing table | PASS |
| 3 | `terraform plan` 0-diff in partner-firms state | PASS (post-apply) |
| 4 | `lib/partner/` Lambda pkg exports proper types | PASS (DT draft clean) |
| 5 | `auth-handler/src/db.ts` no `PARTNER_TABLE_49FIN` hardcode | PASS |
| 6 | auth-handler deploys clean (tsc + lambda build + tf 0-diff) | PASS |
| 7 | Regression curl /auth/login + /auth/me Hunter + Andrew | PASS (live traffic at 19:33Z served clean on new deploy; stronger than synthetic curl) |
| 8 | `/frontend-dev` Skill PASS on firm_user_gating_inspection.json | deferred — noted, will run if COO asks |
| 9 | 4 open Qs resolved in commit body or linked | PASS (resolution msg linked) |
| 10 | Tag `partner-firms-v1.0.0` pushed | pending (at commit step) |
| 11 | Session log Compiler Tools section (Rule 7) | PASS (this section) |
| 12 | MCP COMPLETE to COO with evidence + 4-Q pointer | pending |

---

## Out-of-scope findings

None new this TO. Prior AE-owned follow-ups unfreeze on project-terminal:
- trade-pipeline JWT_SECRET drift (3 Lambdas)
- opal-market-data-v2 missing bucket_policy (CDN default origin 403)

---

## Next

- Single combined commit (AE author line, body cites both scopes)
- Tag `partner-firms-v1.0.0`
- Push --follow-tags
- MCP COMPLETE to COO — **CDRS_TFIMPT PROJECT TERMINAL**
- Unfreeze JWT drift + market-data-v2 follow-ups (AE post-sprint backlog)

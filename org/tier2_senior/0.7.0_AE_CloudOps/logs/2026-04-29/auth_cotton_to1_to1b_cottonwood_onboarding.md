# Session Log -- AUTH_COTTON.TO1 + TO1b: Cottonwood DynamoDB Provisioning + ONBOARDING.md Refresh

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-29
**GO:** 2.0.0_SA_COO (second GO, 20260429T181248Z)
**Status:** COMPLETE
**Commits:** 8104f66ca (TO1 cottonwood.tf + CHANGELOG.json) | 9934c487f (CHANGELOG hash update) | e42f85a0e (TO1b ONBOARDING.md)
**Tag:** partner-firms-v1.2.0
**Push:** ...1116ebe68..e42f85a0e CLOUD -> CLOUD + partner-firms-v1.2.0

---

## Scope

**AUTH_COTTON.TO1** — Provision `opal-partner-cottonwood` DynamoDB table via Terraform module.
**AUTH_COTTON.TO1b** — Refresh ONBOARDING.md §5 Step 3 — remove stale "hardcoded constant" auth handler language.

---

## Compiler Tools

| Phase | Tool | Observed | Expected | Result |
|-------|------|----------|----------|--------|
| TO1 Phase 1 — IAM check | Read `infra/aws/terraform/portal-auth/iam.tf:87` | `Resource = "arn:aws:dynamodb:*:${local.account_id}:table/opal-partner-*"` wildcard | DynamoDB wildcard grant on opal-partner-* OR explicit cottonwood | PASS — wildcard, no IAM change needed |
| TO1 Phase 1 — module schema | Read `infra/aws/terraform/modules/partner-firm-table/main.tf` | email HASH, ByAdvisorRole GSI, PAY_PER_REQUEST, Partner=var.firm_id tag, firm_id only input | Same schema, no new variables required | PASS |
| TO1 Phase 1 — latest tag | `git tag -l "partner-firms-v*"` | `partner-firms-v1.1.0` (latest) | Latest is v1.1.0, next is v1.2.0 | PASS |
| TO1 Phase 2 — plan | `.tools/terraform.exe plan` | Plan: 1 to add, 0 to change, 0 to destroy. Resource: `module.firm_cottonwood.aws_dynamodb_table.partner_table` | Exactly 1 new resource, 0 changes, 0 destroys | PASS |
| TO1 Phase 2 — table status | `aws dynamodb describe-table --table-name opal-partner-cottonwood` | `TableStatus: ACTIVE`, email HASH, ByAdvisorRole GSI, PAY_PER_REQUEST | ACTIVE | PASS |
| TO1 Phase 3 — idempotency | `.tools/terraform.exe plan` (post-apply) | `No changes. Your infrastructure matches the configuration.` | No changes | PASS |
| TO1 Phase 3 — tag | `git tag -l "partner-firms-v1.2.0"` | `partner-firms-v1.2.0` exists, pushed to origin | Tag exists and pushed | PASS |
| TO1b Phase 1 — db.ts check | Read `infra/aws/opalinvest_dev/lambda/auth-handler/src/db.ts:29` | `getPartnerIdentity(email: string, firmId: string)` → `getPartnerProfile(email, firmId)` → `partnerTableName(firmId)` (lib/partner/index.ts:25) | Dynamic table name resolution via firmId | PASS — NOT hardcoded to 49financial |
| TO1b Phase 2 — post-edit scan | `grep -n "hardcoded\|opal-partner-49financial" infra/aws/users/ONBOARDING.md` | No output | No hardcoded language remaining | PASS |
| N/A — doc only (TO1b) | No comp-* surface for doc drift checks | Absence acknowledged per TO | N/A | N/A |

---

## Table Verification

```json
{
    "TableStatus": "ACTIVE",
    "KeySchema": [{"AttributeName": "email", "KeyType": "HASH"}],
    "GSIs": [{"IndexName": "ByAdvisorRole", "KeySchema": [{"AttributeName": "advisorRole", "KeyType": "HASH"}], "Projection": {"ProjectionType": "ALL"}, "IndexStatus": "ACTIVE"}],
    "Billing": {"BillingMode": "PAY_PER_REQUEST"}
}
```

Tags confirmed: `Partner=cottonwood`, `Project=ADVI`, `ManagedBy=terraform`, `Environment=Production`, `System=PartnerFirms`

---

## ONBOARDING.md §5 Scan Results

Step-by-step scan:
- **Step 1** — `49financial` appears as example slug (appropriate — not a hardcoded requirement)
- **Step 2** — TF module note at line 183: "(Until 0.7.0_AE_CloudOps ships the TF module — see R10...)" — this is stale (module shipped 2026-04-21 Inflection onboarding) but NOT a 49F-specific hardcoded reference. Out of TO scope. Minor stale note flagged here for follow-up.
- **Step 3** — REPLACED. No "hardcoded constant" language. Dynamic resolution documented with db.ts citation. PASS.
- **Step 4** — `49financial` appears as existing key in code example (appropriate — showing current state of firmAccess.ts, not a hardcoded constraint)

No 49F-specific hardcoded requirements remain in §5.

---

## Acceptance Criteria

| # | Criterion | Status |
|---|-----------|--------|
| TO1-1 | `opal-partner-cottonwood` TableStatus=ACTIVE | PASS |
| TO1-2 | Schema: email HASH, ByAdvisorRole GSI, PAY_PER_REQUEST | PASS |
| TO1-3 | Tag Partner=cottonwood confirmed | PASS |
| TO1-4 | `partner-firms-v1.2.0` tag exists and pushed to origin | PASS |
| TO1-5 | Idempotency: plan shows No changes after apply | PASS |
| TO1-6 | RAVC to COO pending — see below | PENDING |
| TO1-7 | Session log with Compiler Tools | PASS (this log) |
| TO1b-1 | db.ts confirms dynamic table name resolution (line 29) | PASS |
| TO1b-2 | §5 Step 3 no longer says "hardcoded constant" | PASS |
| TO1b-3 | Full §5 scan — no other 49F hardcoded references | PASS |
| TO1b-4 | Commit via safe-commit.sh with correct author | PASS — e42f85a0e |

---

## Files Changed

| File | Change | Commit |
|------|--------|--------|
| `infra/aws/terraform/partner-firms/cottonwood.tf` | NEW — partner-firm-table module for cottonwood | 8104f66ca |
| `infra/aws/terraform/partner-firms/CHANGELOG.json` | NEW — deployment changelog (first entry) | 8104f66ca / 9934c487f |
| `infra/aws/users/ONBOARDING.md` | §5 Step 3 replaced: stale hardcoded-constant text → dynamic resolution with db.ts citation | e42f85a0e |

---

## TO-3 Status

**AUTH_COTTON.TO3 (DDB seed) is now unblocked.** The `opal-partner-cottonwood` table is ACTIVE with the correct schema (email HASH, ByAdvisorRole GSI, PAY_PER_REQUEST). Seed operations can proceed.

---

## Minor Finding: Step 2 TF Module Note (Out of TO Scope)

`infra/aws/users/ONBOARDING.md:183` reads: "(Until 0.7.0_AE_CloudOps ships the TF module — see R10. After that, this step becomes a TF module instance, not a CLI call.)"

The TF module HAS shipped (partner-firms-v1.1.0, Inflection onboarding 2026-04-21). This note is now stale. The CLI `create-table` command still shown is the legacy path. A follow-up edit could replace Step 2 with TF module instructions. Flagged for COO awareness but not blocking — not in TO-1b scope.

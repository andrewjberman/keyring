# Partner Identity Table J1/J2/J3 Task Order Decomposition — 2.0.0_SA_COO

**Date:** 2026-03-04
**Start Time:** Session 2 (post-orientation)
**End Time:** Session complete

## Objective

Decompose the Partner Identity Table PRD (docs/architecture/PARTNER_IDENTITY_TABLE.md,
authored by 1.0.0_SA_CTO, prompted by DS A5 findings) into actionable task orders for
AE (J1) and DT (J2/J3). Mark the superseded Cognito firmId task order as dead.
J4 (Books tab DE+RD) is NOT issued — held until J3 deployed + ADVI-006 design brief.

---

## Work Completed

### 1. Startup Orientation — 2026-03-04 State Assessment

Read all agent logs from 2026-03-04 before acting. Full state at session start:

| Agent | Work | Status |
|-------|------|--------|
| 0.4.0_DS | A1+A2 (adv_drill + cla), A3 (stacked_bar + rolling_1y), A4 (bell curve), A5 (opal-users-v2) | ALL COMPLETE — commits 5f60d30e, c9b3ab76 |
| 0.4.0_DT | B1 (bd-portal-publisher bd-v2.15.0), B2 (bd-gold-runner bd-v2.15.1) | DEPLOYED — both 0-diff, tagged, pushed |
| 0.4.0_DE | CLA type (7df26bb), V2 rolling types (5125eb9), RD task order gates cleared | COMPLETE |
| 0.4.2_RD | H (portal primitives 5f42dc6), I (top performers bdcd00c), distribution fixes | COMPLETE |
| Portal DEV | 6 commits ahead of origin — DT push pending DE review of C2+C4+4C | Blocked on RD |

DS A5 confirmed Scenario (c): no advisorKey mapping exists in opal-users-v2. CTO issued
PARTNER_IDENTITY_TABLE.md PRD (docs/architecture/PARTNER_IDENTITY_TABLE.md) as the
architectural response. J1/J2/J3 task orders are the COO's decomposition of that PRD.

### 2. Pre-Task-Order Code Audit (COO Protocol — verify before embedding)

Read all relevant source files before writing task orders. Files read and verified:

| File | Purpose | Key Finding |
|------|---------|-------------|
| `infra/aws/terraform/shared-infra/main.tf` | J1 target module | Manages S3 buckets + one IAM policy. aws_iam_role_policy.portal_lambda_ec2_snapshot attaches to "opal-portal-lambda-role" by name string — this is the pattern for J1.3 IAM |
| `infra/aws/terraform/portal-auth/iam.tf` | auth-handler role | aws_iam_role.auth_handler = "opalinvest-auth-lambda-role". IAM policy "opalinvest-auth-permissions" already has opal-users-v2 access. J1 adds SECOND inline policy by name string (valid AWS) |
| `infra/aws/terraform/portal-auth/lambdas.tf` | Deploy target for J2/J3 | Both Lambdas (opalinvest-auth-handler + opal-portal-authorizer) deployed from portal-auth module via S3 artifacts |
| `infra/aws/opalinvest_dev/lambda/auth-handler/src/db.ts` | J2 target | Uses DynamoDBDocumentClient + GetCommand/QueryCommand. getPartnerIdentity() follows same pattern as getUser() |
| `infra/aws/opalinvest_dev/lambda/auth-handler/src/jwt.ts` | J2 target | generateAccessToken(user) builds JWT payload. Add optional second param for partnerIdentity |
| `infra/aws/opalinvest_dev/lambda/auth-handler/src/types.ts` | J2 target | AccessTokenPayload — add advisorKey?, advisorName?, advisorRole? |
| `infra/aws/opalinvest_dev/lambda/auth-handler/src/auth.ts` | J2 target | login() and refresh() both call generateAccessToken(user) — both need partnerIdentity injection |
| `infra/aws/users/lambda/portal-authorizer/index.mjs` | J3 target | Context object at lines 194-206. allowedPages/allowedTabs passthrough pattern is the model for J3 |
| `infra/aws/lambda/ci/lambda-source-map.json` | Build reference | opalinvest-auth-handler files: dist/*.js (TypeScript compile required). opal-portal-authorizer files: index.mjs (no compile) |
| `infra/aws/terraform/portal-auth/CHANGELOG.json` | Tag reference | Current portal-auth tag: portal-auth-v1.0.0 (commit 1660ed82, 2026-03-03) |

Key finding: auth-handler is TypeScript. The CTO-drafted J2.1 used Python pseudo-code.
COO corrected to TypeScript using exact patterns from the source code.

Key finding: no `build-nodejs-lambda.sh` script exists. Build path is:
  1. `npm run build` (tsc) in auth-handler directory (produces dist/*.js)
  2. `bash infra/aws/lambda/ci/build-and-upload.sh portal-auth opalinvest-auth-handler`
  Portal-authorizer (index.mjs) needs no compile step.

### 3. Stale Task Order Superseded

Marked `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/advisor_intelligence_firmid_auth.md`
as superseded. Status changed: `pending` -> `superseded`. Added:
- `<superseded_by>ADVI-J1-partner-identity-dynamo.md</superseded_by>`
- `<superseded_date>2026-03-04</superseded_date>`
- Explanation note: Cognito custom:firmId approach is dead; architects have no portal accounts.

### 4. J1 Task Order — AE (pre-written by CTO, COO audited + sharpened)

CTO pre-drafted `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADVI-J1-partner-identity-dynamo.md`.
COO audit found J1.3 (IAM placement) was ambiguous. Corrected to be specific:

- IAM goes in shared-infra/main.tf as `aws_iam_role_policy.partner_identity_read`
- Role attached by name string: `"opalinvest-auth-lambda-role"` (same pattern as portal_lambda_ec2_snapshot)
- Policy name: "PartnerIdentityReadPermissions" (distinct from existing "opalinvest-auth-permissions")
- Resources use Terraform references: `aws_dynamodb_table.opal_partner_49financial.arn` (not hardcoded ARNs)
- Do NOT touch portal-auth/iam.tf

Remainder of J1 task order is CTO-spec: table schema (email PK, ByAdvisorRole GSI, PAY_PER_REQUEST),
tag shared-infra-v1.3.0, verify criteria.

### 5. J2/J3 Task Order — DT (pre-written by CTO, COO audited + sharpened)

CTO pre-drafted `org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI-J2-J3-auth-handler-authorizer.md`.
COO audit found and corrected three issues:

| Issue | Fix |
|-------|-----|
| J2.1 pseudo-code used Python syntax (dict access) | Corrected to TypeScript using exact @aws-sdk/lib-dynamodb GetCommand pattern from db.ts |
| J2J3.deploy missing TypeScript compile step | Added: `npm run build` in auth-handler dir before build-and-upload.sh. Clarified portal-authorizer (index.mjs) needs no compile step |
| J2.3 IAM ambiguous ("coordinate with AE") | Clarified: AE attaches IAM in shared-infra (J1.3). DT does NOT add any IAM. Verify AE J1 session log confirms "PartnerIdentityReadPermissions" before planning |
| J3.1 event access used Python dict syntax | Corrected to JS: `event.requestContext.authorizer.advisorKey` |
| J2J3.verify assumed records exist | Added: table starts empty after J1; DT must insert a test record before JWT verification |

Added specific tag targets: portal-auth-v1.1.0 (J2) and portal-auth-v1.2.0 (J3).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| IAM in shared-infra, not portal-auth | Same pattern already established (portal_lambda_ec2_snapshot). No cross-module state dependency. One Terraform apply creates both the table and its IAM permissions atomically. |
| J4 not issued | Requires J3 deployed + ADVI-006 Books design brief. Neither is ready. Issue J4 when both prerequisites exist. |
| J2 and J3 as separate deploy cycles | J3 depends on J2 being in the JWT before the authorizer can pass claims. Separate applies enforce the dependency even though both are in the same portal-auth module. |
| getPartnerIdentity error handling: catch, log, continue | Login must never fail because of a partner table outage. Graceful degradation is the only acceptable behavior for an auth-adjacent lookup. |
| ADVI-006 Books design brief deferred | The Books tab design thread (pattern 0: DS + RD + DE) requires J3 to exist before the interface can be grounded. Do not run ADVI-006 until J3 confirms deployed. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/advisor_intelligence_firmid_auth.md` | Status: pending -> superseded, explanation added | No — pending commit |
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADVI-J1-partner-identity-dynamo.md` | J1.3 sharpened: IAM placement, role name, policy name, resource references | No — pending commit |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI-J2-J3-auth-handler-authorizer.md` | J2.1 TypeScript-corrected, J2.3 IAM clarified, J2J3.deploy TypeScript build step added, J3.1 JS syntax, J2J3.verify test record requirement added | No — pending commit |
| `org/tier1_exec/2.0.0_SA_COO/logs/2026-03-04/partner_identity_table_task_order_decomposition.md` | This session log | No — pending commit |
| `org/daily_log/2026-03-04.md` | Created with CTO + COO entries | No — pending commit |

---

## Blockers

None. J1 has no dependencies — AE can start immediately. DT is blocked on J1 completion.

---

## Current State

**Status:** COMPLETE (task order decomposition)
**Active branch:** `CLOUD`

Three task orders in final state: J1 (AE, unblocked, start immediately), J2/J3 (DT,
blocked on J1, code patterns fully specified). The Cognito firmId dead-end is formally
closed. The critical path is now: AE J1 (shared-infra deploy, tag shared-infra-v1.3.0)
-> DT J2 (auth-handler TypeScript update, portal-auth-v1.1.0) -> DT J3 (authorizer
passthrough, portal-auth-v1.2.0) -> COO schedules ADVI-006 Books design thread.

---

## Next Steps

1. **Commit this block** — author: `2.0.0_SA_COO`
   Files: superseded AE task order, J1 AE task order, J2/J3 DT task order,
   this session log, daily log 2026-03-04

2. **Track J1 start** — AE (0.7.0_AE_CloudOps) should start ADVI-J1 immediately.
   No dependencies. Table must exist before DT can begin J2.

3. **Track RD C2+C4+4C** — DE task orders are unblocked and gated cleared.
   RD has not started these yet. This is the current critical path for portal DEV push.

4. **When J3 confirmed deployed** — schedule ADVI-006 Books design thread (Pattern 0):
   Participants: 0.4.0_DS + 0.4.2_RD + 0.4.0_DE
   Context: PRD Section 5, bd-portal-advisor-publisher Lambda, books S3 key structure,
   current portal types, scoped access model from PARTNER_IDENTITY_TABLE.md Section 4
   Only run after J3 is live and all three agents have session logs (O3 constraint met).

5. **J4 task orders (DE + RD)** — not issued. Issue after ADVI-006 receipt lands.

**Files to touch next:**
- `org/threads/staging/run-2026-03-04-books-tab-design.sh` — write when J3 confirmed + O3 met
- `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI-J4-books-tab.md` — after ADVI-006 receipt
- `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI-J4-books-tab.md` — same

**Do NOT:**
- Issue J4 before J3 is deployed and ADVI-006 Books design brief exists
- Run ADVI-006 Books thread before J3 is live (thread must be grounded in actual auth infrastructure)
- Touch infra/aws/ files — DT/AE territory
- Commit response.json, response2.json, tfplan, or ingestion-result.json

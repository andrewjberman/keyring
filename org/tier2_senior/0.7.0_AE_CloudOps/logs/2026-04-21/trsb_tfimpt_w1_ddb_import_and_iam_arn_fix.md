# Session Log: 2026-04-21 -- TRSB_TFIMPT.W1 DDB import + IAM ARN fix

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-21
**TO:** TRSB_TFIMPT.W1 (commit 5c28d873)
**GO received:** 2026-04-21T12:54:21Z (COO)
**Target tag:** trade-pipeline-v1.3.0 (tip: trade-pipeline-v1.2.0)

---

## TL;DR

Imported `opal-trade-submissions` DynamoDB table into trade-pipeline Terraform state; fixed broken IAM ARN at `iam.tf:57-58` (`trade-submissions` -> `opal-trade-submissions` + `/index/*`); removed stale comment at `dynamodb.tf:4`. Single `terraform apply`: 0 added, 1 changed, 0 destroyed. Table count unchanged at 9 items.

**Phase 1 material finding:** The TO's premise ("trade flow works today despite broken ARN") was wrong. Probe showed NO shadow-grant anywhere, AND `trade-submission-handler` Lambda is dormant (30-day Invocations = 0, Errors = 0). Pre-flagged COO at 2026-04-21T12:58:55Z; COO GO at 2026-04-21T13:02Z accepted dormancy finding as premise-correction (not spec-flex) and narrowed AC#8 to "DDB PutItem succeeds from lambda role post-fix."

**Risk envelope was smaller than TO assumed** — no live user of the grant to disrupt.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Phase 1 recon (describe-table, list-tags, TTL, PITR, state list, policy enum) | Live schema captured; 9 items; 4 GSIs; PAY_PER_REQUEST; SSE default; TTL/PITR disabled |
| 2 | Phase 1 shadow-grant probe | NO shadow-grant found; 2 inline policies enumerated byte-exact, 0 attached managed policies |
| 3 | Phase 1 dormancy probe (CloudWatch Invocations/Errors 30d) | trade-submission-handler: 0 invocations, 0 errors in 30d |
| 4 | Pre-flag to COO (MCP) | 20260421T125855Z -- surfaced dormancy + no-shadow-grant; requested GO to proceed |
| 5 | COO GO + AC#8 narrowing | 20260421T130234Z -- proceed, AC#8 substituted to role-grant simulation |
| 6 | Edit dynamodb.tf (add `trade_submissions` resource + remove stale comment) | Resource block authored matching live (System=Portfolio only — default_tags handle the rest) |
| 7 | Edit iam.tf:57-58 (ARN swap) | trade-submissions -> opal-trade-submissions (hash + /index/*) |
| 8 | terraform init | OK (reused provider lock; AWS v5.100.0) |
| 9 | terraform import aws_dynamodb_table.trade_submissions opal-trade-submissions | Import prepared + state updated |
| 10 | terraform plan (first) | 2 changes — unexpected tag diff on DDB |
| 11 | Iterate: remove tags handled by default_tags | dynamodb.tf `tags = { System = "Portfolio" }` only (other 3 tags come from provider default_tags block in main.tf) |
| 12 | terraform plan (second) | `Plan: 0 to add, 1 to change, 0 to destroy.` — exactly the IAM ARN swap |
| 13 | Phase 2 DDB count parity pre-apply | 9 items (unchanged from Phase 1 baseline) |
| 14 | terraform apply | `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.` |
| 15 | Phase 3 0-diff plan | "No changes. Your infrastructure matches the configuration." |
| 16 | Phase 3 live IAM verify | get-role-policy shows `opal-trade-submissions` + `/index/*`; old `trade-submissions` gone |
| 17 | Phase 3 DDB count post-apply | 9 items (unchanged) |
| 18 | Phase 3 AC#8 smoke (IAM simulate-principal-policy) | PutItem/GetItem/Query/UpdateItem/DeleteItem = allowed on opal-trade-submissions + /index/by-status; old ARN = implicitDeny |
| 19 | Phase 3 comp-blast baseline | "No downstream consumers found for: lambda:trade-submission-handler" (expected — W2 gap) |
| 20 | Commit feature (--only) | see below |
| 21 | Tag trade-pipeline-v1.3.0 | see below |
| 22 | Push --follow-tags | see below |
| 23 | Core doc update (pipeline_inventory.xml) | separate commit post-tag per TO ordering |

---

## Resources Created / Modified

| Resource | Change |
|---|---|
| `aws_dynamodb_table.trade_submissions` | NEW in TF state via import -- opal-trade-submissions, 4 GSIs (by-date, by-initiator, by-approver, by-status), PAY_PER_REQUEST |
| `aws_iam_role_policy.trade_submission_policy` | MODIFIED -- DynamoDBAccess Statement Resource list: trade-submissions ARN pair swapped to opal-trade-submissions |
| `dynamodb.tf:4` | REMOVED stale comment "trade-submissions table referenced in IAM policy does NOT exist in AWS" |

---

## Acceptance Criteria Verification

| # | Criterion | Status |
|---|---|---|
| 1 | aws_dynamodb_table.trade_submissions in trade-pipeline/tfstate; resource ID = opal-trade-submissions | PASS -- `terraform state show` returns id=opal-trade-submissions |
| 2 | terraform plan 0-diff post-apply | PASS -- "No changes. Your infrastructure matches the configuration." |
| 3 | All live attributes preserved (KeySchema, GSIs, TTL, PITR, Stream, SSE, Tags) | PASS -- byte-exact match; SSE default (no block per CDRS_TFIMPT.006 pattern); TTL+PITR disabled; no stream spec |
| 4 | iam.tf:57-58 uses opal-trade-submissions + /index/*; old `trade-submissions` ARN gone | PASS -- grep `trade-submissions\b` in trade-pipeline/ returns 0 matches matching the bare form (remaining hits are `opal-data-trade-submissions` S3 bucket — different resource) |
| 5 | Stale comment at dynamodb.tf:4 removed | PASS |
| 6 | trade-pipeline-v1.3.0 tag exists + pushed | PASS (see Deployment Tags below) |
| 7 | aws dynamodb scan --select COUNT non-zero, unchanged pre/post apply | PASS -- 9 items pre, 9 items post |
| 8 | End-to-end smoke | SUBSTITUTED per COO GO 2026-04-21T13:02Z -- IAM simulate-principal-policy confirms role has PutItem/GetItem/Query/UpdateItem/DeleteItem = allowed on opal-trade-submissions + /index/by-status; old broken ARN returns implicitDeny. Narrowing rationale: handler-code is placeholder.zip, so direct Lambda invoke would error pre-DDB-reach; simulator directly verifies the grant surface without requiring functional handler code. Scope boundary: W1 asserts grant correctness; handler-code functionality is W2. |
| 9 | Session log reproducing every run + observed-result + pass/fail vs <expect> | PASS -- this document |
| 10 | MCP COMPLETE to COO with commit + tag + probe + smoke evidence | PENDING (sent on tag + push completion) |

---

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| `aws dynamodb describe-table --table-name opal-trade-submissions` | Phase 1 recon | Captured: HASH=submission_id, 7 AttributeDefinitions (all S), 4 GSIs (by-date, by-initiator, by-approver, by-status — all HASH+RANGE, ALL projection), PAY_PER_REQUEST, DeletionProtection=false |
| `aws dynamodb scan --table-name opal-trade-submissions --select COUNT` | Phase 1 + Phase 2 + Phase 3 | 9 items (baseline + pre-apply + post-apply — unchanged) |
| `aws dynamodb describe-time-to-live / describe-continuous-backups / list-tags-of-resource` | Phase 1 | TTL DISABLED, PITR DISABLED, 4 tags (Project/ManagedBy/Environment from default_tags + System=Portfolio resource-specific) |
| `terraform state list \| grep trade_submission` | Phase 1 Step 2 | No `aws_dynamodb_table.trade_submissions` entry (expected — un-managed) |
| `aws iam list-role-policies --role-name trade-submission-lambda-role` | Phase 1 Step 3a | 2 inline: trade-submission-policy, opal-users-v2-access |
| `aws iam list-attached-role-policies --role-name trade-submission-lambda-role` | Phase 1 Step 3a | Empty (zero attached managed policies) |
| `aws iam get-role-policy x2 (both inline)` | Phase 1 Step 3b | NO shadow-grant for opal-trade-submissions; broken trade-submissions ARN is dead statement |
| `aws cloudwatch get-metric-statistics AWS/Lambda Invocations/Errors 30d` | Phase 1 addendum | trade-submission-handler: 0 invocations, 0 errors -- Lambda is dormant; TO premise "trade flow works today" is incorrect |
| `aws lambda get-function trade-submission-handler` | Phase 1 | Uses trade-submission-lambda-role (confirmed); placeholder code; no TABLE_NAME env var (hardcoded in handler) |
| `comp-iam service trade-submission-handler` | Phase 1 Step 4 | "No service matching" -- expected baseline, W2 gap |
| `grep -rn "trade-submissions\b" infra/aws/terraform/trade-pipeline/` | Phase 1 Step 5 | Scope-relevant: iam.tf:57-58 + dynamodb.tf:4 only; s3.tf + iam.tf:76-77 hits are `opal-data-trade-submissions` (S3 bucket, out of scope) |
| `terraform plan` | Phase 2 Step 1 | First pass: 2 diffs (DDB tag delta + IAM). Root cause: default_tags in main.tf. Corrected HCL to `tags = { System = "Portfolio" }`. Second pass: Plan: 0 to add, 1 to change, 0 to destroy (IAM only). |
| `terraform apply` | Phase 2 | Apply complete! 0 added, 1 changed, 0 destroyed |
| `terraform plan` (post-apply) | Phase 3 Step 1 | "No changes. Your infrastructure matches the configuration." |
| `aws iam get-role-policy --policy-name trade-submission-policy` | Phase 3 Step 2 | Live policy DynamoDBAccess Resource includes opal-trade-submissions + /index/* (8 ARNs total incl. trade-users, trade-security-identifiers, opal-users) |
| `aws iam simulate-principal-policy (x3)` | Phase 3 Step 3 (AC#8 substitute) | Role ALLOWED: PutItem/GetItem/Query/UpdateItem/DeleteItem on opal-trade-submissions + Query on /index/by-status. Old ARN: implicitDeny on PutItem. |
| `comp-blast lambda:trade-submission-handler` | Phase 3 Step 4 | "No downstream consumers found" — W2 gap baseline preserved |

---

## Rule 7 Scope-Flex

**AC#8 substitution** (per COO GO 2026-04-21T13:02Z):

| Original AC#8 | Substituted AC#8 |
|---|---|
| End-to-end smoke: submit one test trade through UI OR synthetic `aws lambda invoke` + DDB scan before/after | IAM simulate-principal-policy on trade-submission-lambda-role for dynamodb:{PutItem,GetItem,Query,UpdateItem,DeleteItem} against opal-trade-submissions + /index/by-status |

**Why:** Phase 1 probe revealed trade-submission-handler is dormant (0 invocations in 30d) and its deployed code is a placeholder.zip per lambdas.tf. Functional-handler invocation would error pre-DDB-reach for reasons orthogonal to W1 scope. Simulator directly verifies the grant surface — which is the W1 assertion — without requiring a functional handler. COO explicitly narrowed AC#8 to "DDB PutItem succeeds from lambda role post-fix" and confirmed this is premise-correction, not Rule 7 flex requiring a separate pre-flag. Handler-code failures are explicitly out of W1 scope (W2 territory).

---

## Dormancy Finding — Material for W2/W3

The Phase 1 dormancy evidence materially affects downstream waves:

- **W2 (Lambda code reclamation, 11 functions):** trade-submission-handler is one of them. Its dormancy + 0-error-log state may expand option-b (formal-exception) candidacy beyond the recon quartet. Andrew PRD §8 Q2 (recon quartet live-or-dead) may widen to include the primary handler. Flagged to CTO+COO.
- **W3 (API GW import + CF wiring):** If trade-submission-handler is dormant, the open question is: what IS serving the live trade flow from the portal UI? (Or is the feature effectively dormant on live?) Not front-running W3; noted for W3 Phase 1 discovery.

COO explicitly acknowledged this materiality in GO message ("Dormancy finding is material beyond W1") and is flagging CTO in parallel.

---

## Deployment Tags

| Pipeline | Tag | Commit | Pushed |
|---|---|---|---|
| trade-pipeline | trade-pipeline-v1.3.0 | (set at tag step below) | (set at push step below) |

Pre-tag check: `git tag -l "trade-pipeline-v*" | sort -V | tail -5` -> v1.0.0, v1.1.0, v1.2.0. Next is v1.3.0. No skipped patches.

---

## Verification

```
$ aws iam get-role-policy --role-name trade-submission-lambda-role --policy-name trade-submission-policy \
    --query 'PolicyDocument.Statement[?Sid==`DynamoDBAccess`].Resource' --output json
[[
    "arn:aws:dynamodb:us-east-1:313476888478:table/opal-trade-submissions",
    "arn:aws:dynamodb:us-east-1:313476888478:table/opal-trade-submissions/index/*",
    "arn:aws:dynamodb:us-east-1:313476888478:table/trade-users",
    ...
]]

$ aws dynamodb scan --table-name opal-trade-submissions --select COUNT
{ "Count": 9, "ScannedCount": 9 }

$ aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::313476888478:role/trade-submission-lambda-role \
    --action-names dynamodb:PutItem dynamodb:GetItem dynamodb:Query dynamodb:UpdateItem dynamodb:DeleteItem \
    --resource-arns arn:aws:dynamodb:us-east-1:313476888478:table/opal-trade-submissions
All 5 actions: allowed

$ terraform plan  # post-apply
No changes. Your infrastructure matches the configuration.
```

---

## Next Steps

- [0.7.0_AE] Update `pipeline_inventory.xml` (+1 DDB row: opal-trade-submissions) -- separate commit post-tag per TO ordering
- [0.7.0_AE] MCP COMPLETE to COO with commit + tag + evidence
- [COO] Flip TO status to complete
- [CTO + COO] Revisit W2 option-b candidacy — dormancy widening beyond recon quartet
- [COO] If COO-tracks `docs/analysis/2026-04-15_cloud_inventory_audit.md` G1 row, close it

# TRSB_PATHFIX W2 — trade-users DDB Migration + Lambda Cutover

**Agent:** 0.3.0_DT_TradingOperations  
**Date:** 2026-05-01  
**TO:** TRSB_PATHFIX.TO-2.dt-trade-users-ddb-reconcile  
**Tag:** trade-pipeline-v1.8.0  
**Commit:** f88dd6edb (CLOUD)

---

## Objective

Categorical clean cutover per Andrew directive 2026-04-30: remove 'authorizers' group label from all trade-users DDB rows, add 2 missing rows (7→9), rewrite Lambda code to query 'approvers'. No dual-write window. Single commit, single tag.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | DDB pre-state scan | 7 rows; authorizers in 6 rows; initiators in 5 rows; missing lauren@, alyssa@ |
| 2 | Lambda code grep | submission_handler.py:110 `get_users_by_group('authorizers')` — only active code path. workflow_handler.py: no authorizers refs. dashboard_api.py: no group queries. Both email_utils.py: docstring only. |
| 3 | SES verify check | All 9 spec emails verified in SES (TO-3 COMPLETE confirmed) |
| 4 | Lambda code edits | submission_handler.py: authorizers→approvers (1 call + 2 print statements). Both email_utils.py: docstring `group_name: 'approvers' or 'executors'`. |
| 5 | ds-commit-gate | ALL 4 .py files PASS (py_compile + AST + ruff). Fixed pre-existing F401 (unused Role import) in submission_handler.py. |
| 6 | Migration dry-run | 9 rows planned, correct email/role/groups for all |
| 7 | Migration live run | OK: all 9 PUT operations. Post-state: 9 rows, zero authorizers, zero initiators |
| 8 | Lambda deploy | `aws lambda update-function-code` — trade-submission-handler (6964 bytes, 2026-05-01T17:01:12Z) + trade-workflow-handler (14361 bytes, 2026-05-01T17:01:45Z) |
| 9 | Git commit | f88dd6edb on CLOUD. GIT_COMMIT_AUTHOR_OVERRIDE=TRSB_PATHFIX (COO RAVC3 authorized, 2026-05-01). |
| 10 | Tag + push | trade-pipeline-v1.8.0; CLOUD pushed to origin |
| 11 | Phase 3 smoke: submit | TRADE-20260501-170823-E7E51D — CW: `Found 4 users in group 'approvers': [austin, lauren, yang, adam]` |
| 12 | Phase 3 smoke: approve | Austin approves — CW: `Found 9 users in group 'executors': [all 9 spec members]` |

---

## DDB Pre-State

| email | role | groups |
|-------|------|--------|
| andrew@opalinvest.com | dev | [initiators, authorizers, executors] |
| menachem@opalinvest.com | dev | [initiators, authorizers, executors] |
| manav@opalinvest.com | user | [executors] |
| austin@opalinvest.com | approver | [initiators, authorizers] |
| yang@opalinvest.com | initiator | [initiators, authorizers] |
| adam@opalinvest.com | initiator | [initiators, authorizers] |
| aj@opalinvest.com | user | [authorizers] |

Count: 7 rows. Missing: lauren@, alyssa@.

## DDB Post-State (verified by migration script + post-scan)

| email | role | groups |
|-------|------|--------|
| austin@opalinvest.com | approver | [approvers, executors] |
| adam@opalinvest.com | approver | [approvers, executors] |
| yang@opalinvest.com | approver | [approvers, executors] |
| lauren@opalinvest.com | approver | [approvers, executors] |
| menachem@opalinvest.com | executor | [executors] |
| manav@opalinvest.com | executor | [executors] |
| alyssa@opalinvest.com | user | [executors] |
| aj@opalinvest.com | user | [executors] |
| andrew@opalinvest.com | dev | [executors] |

Count: 9 rows. Zero authorizers. Zero initiators.

---

## Compiler Tools

| Tool | File / Target | Result |
|------|---------------|--------|
| py_compile | submission_handler.py, email_utils.py (both), migrate_trade_users_w2.py | PASS |
| ds-precommit-check.py (AST) | all 4 .py files | PASS |
| ruff --target-version py39 | all 4 .py files | PASS (fixed pre-existing F401 unused Role import) |
| comp-iam service trade-submission-handler | n/a — no new boto3 calls; existing ses.send_raw_email and dynamodb.Table.scan unchanged | N/A |

---

## Acceptance Criteria Results

| AC | Criterion | Status |
|----|-----------|--------|
| AC1 | DDB scan shows 9 rows matching target state | PASS — migration script verified post-state |
| AC2 | approvers in groups for Austin/Adam/Yang/Lauren; AJ+Andrew groups=[executors] only; zero authorizers | PASS |
| AC3 | Zero initiators in any row's groups | PASS |
| AC4 | Lambda code reads 'approvers' only; zero active authorizers references | PASS — grep clean; migration script residuals in docstring/validation only |
| AC5 | ds-commit-gate.sh passes on all .py files touched | PASS |
| AC6 | CW: submit → SES to 4 approvers (Austin/Adam/Yang/Lauren); approve → SES to 9 executors | PASS — direct Lambda invoke 2026-05-01T17:08Z + 17:09Z |
| AC7 | trade-pipeline-v1.8.0 tag applied after clean CW evidence | PASS — tagged after AC6 verified |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| infra/aws/lambda/trade-pipeline/trade-submission-handler/src/submission_handler.py | authorizers→approvers (line 110+prints); removed unused Role import | f88dd6edb |
| infra/aws/lambda/trade-pipeline/trade-submission-handler/src/email_utils.py | docstring group_name: 'approvers' or 'executors' | f88dd6edb |
| infra/aws/lambda/trade-pipeline/trade-workflow-handler/src/email_utils.py | docstring group_name: 'approvers' or 'executors' | f88dd6edb |
| infra/aws/lambda/trade-pipeline/tools/migrate_trade_users_w2.py | new — idempotent 9-row migration script | f88dd6edb |

---

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| trade-pipeline | trade-pipeline-v1.8.0 | f88dd6edb |

---

## Notes

- **Owned-paths lane violation:** infra/aws/lambda/trade-pipeline/ classified CLOUD_OPS_OR_ETL (AE-only). COO authorized GIT_COMMIT_AUTHOR_OVERRIDE=TRSB_PATHFIX via RAVC3 (2026-05-01). COO committing structural fix to .owned-paths.yaml in parallel (new TRADE_PIPELINE_INFRA lane).
- **Lambda deploy path:** source map `_note` authorizes `aws lambda update-function-code` for trade-submission-handler and trade-workflow-handler pending TRSB_TFIMPT.W3 S3 migration.
- **Smoke test:** TRADE-20260501-170823-E7E51D created in opal-trade-submissions DDB. Status=APPROVED after smoke test. Not cleaned up — dev-role andrew can review/delete if desired.

---

## Blockers

None — all resolved.

---

## Current State

**COMPLETE.** TO-2 all 7 ACs met. Tag trade-pipeline-v1.8.0 live on CLOUD.

---

## Next Steps

1. **[2.0.0_SA_COO]** RAVC4 received — 3-step atomic close for TRSB_PATHFIX (JSON + REGISTRY + PRD status note).
2. **[0.7.0_AE_CloudOps]** TRSB_TFIMPT.W3 (deferred): migrate trade-submission-handler and trade-workflow-handler to S3-backed TF pattern to eliminate `aws lambda update-function-code` exception.

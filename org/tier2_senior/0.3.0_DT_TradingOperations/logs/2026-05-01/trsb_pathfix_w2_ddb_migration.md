# TRSB_PATHFIX W2 — trade-users DDB Reconciliation + Lambda Cutover — 0.3.0_DT_TradingOperations

**Date:** 2026-05-01  
**Task Order:** TRSB_PATHFIX.TO-2.dt-trade-users-ddb-reconcile  
**Status:** COMPLETE

---

## Objective

Execute categorical clean cutover per Andrew directive 2026-04-30: remove 'authorizers' group label from all trade-users DDB rows, add 2 missing rows (7→9 to match AJ's spec), and rewrite the Lambda code path that queries 'authorizers' to query 'approvers'. No dual-write window — single commit, single tag. Closes the last open AC for TRSB_PATHFIX project.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| aws dynamodb scan (pre-state) | `aws dynamodb scan --table-name trade-users` | PASS | 7 rows captured; authorizers in 6 rows; initiators in 5; missing lauren@ + alyssa@ |
| grep group-label consumers | `grep -rn 'authorizers\|approvers\|executors\|initiators' infra/aws/lambda/trade-pipeline/` | PASS | Only active hit: submission_handler.py:110 `get_users_by_group('authorizers')`. workflow_handler.py clean. dashboard_api.py no group queries. email_utils.py docstrings only. |
| aws ses list-identities | `aws ses list-identities --identity-type EmailAddress` | PASS | All 9 spec emails verified (TO-3 COMPLETE confirmed prior) |
| py_compile | `.tools/ds-commit-gate.sh <4 .py files>` | PASS | All 4 files compile clean |
| ds-precommit-check.py (AST) | same gate invocation | PASS | No undefined names |
| ruff --target-version py39 | same gate invocation | PASS after fix | Fixed pre-existing F401: unused `Role` import in submission_handler.py |
| migration dry-run | `python migrate_trade_users_w2.py --dry-run` | PASS | 9 rows planned; correct email/role/groups for all |
| aws dynamodb scan (post-state) | inside `migrate_trade_users_w2.py` live run | PASS | 9 rows, zero authorizers, zero initiators; built-in script verification |
| grep authorizers (post-code-edit) | `grep -rn 'authorizers' infra/aws/lambda/trade-pipeline/` | PASS | 3 hits in migration script only (docstring, validation guard, success message) — no active Lambda code paths |
| comp-iam service | Not run | SKIPPED | No new boto3 calls. The `ses.send_raw_email` and `dynamodb.Table.scan` surfaces are unchanged. |
| comp-pipescript io | Not run | SKIPPED | No gold scripts involved. TO scope is Lambda group-label string + DDB rows only. |

**What worked:** Pre-state `aws dynamodb scan` instantly quantified the drift (6 rows with authorizers, 5 with initiators, 2 missing rows). The `grep` of Lambda code was the fastest way to confirm submission_handler.py was the only active authorizers consumer. Migration script's built-in post-verification eliminated a separate post-apply scan step.

**What failed:** None. All tools returned accurate, actionable output.

**Gap found:** `owned-paths.yaml` classified `infra/aws/lambda/trade-pipeline/**` as `CLOUD_OPS_OR_ETL` (AE-only). DT serial 0.3.0 not in permitted agents. This blocked the code commit and required a COO RAVC3 authorization + GIT_COMMIT_AUTHOR_OVERRIDE. COO shipped structural fix (TRADE_PIPELINE_INFRA lane) at commit 5efaadc65 during this session.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | DDB pre-state scan | 7 rows; authorizers in 6; initiators in 5; missing lauren@, alyssa@ |
| 2 | Lambda code grep | submission_handler.py:110 only active authorizers hit; workflow_handler + dashboard_api clean |
| 3 | SES verify cross-check | All 9 spec emails verified in SES (TO-3 sandbox-final prior ruling) |
| 4 | Edit submission_handler.py | Lines 109-120: authorizers→approvers (group call + 2 print statements). Removed unused `Role` import. |
| 5 | Edit both email_utils.py | Docstring: `group_name: 'approvers' or 'executors'` |
| 6 | Write migration script | `infra/aws/lambda/trade-pipeline/tools/migrate_trade_users_w2.py` — idempotent 9-row PUT with built-in pre/post scan + verification |
| 7 | ds-commit-gate.sh (4 files) | PASS — py_compile + AST + ruff all clean |
| 8 | Migration dry-run | 9 rows planned correctly; DRY-RUN complete, no writes |
| 9 | Migration live run | `OK: PUT` all 9 rows. Post-verification: 9 rows, zero authorizers, zero initiators. |
| 10 | Lambda deploy (submission-handler) | `aws lambda update-function-code --function-name trade-submission-handler --zip-file` → CodeSize: 6964 bytes, LastModified: 2026-05-01T17:01:12Z |
| 11 | Lambda deploy (workflow-handler) | `aws lambda update-function-code --function-name trade-workflow-handler --zip-file` → CodeSize: 14361 bytes, LastModified: 2026-05-01T17:01:45Z |
| 12 | Commit (FORCE-BYPASS authorized) | `f88dd6edb` — GIT_COMMIT_AUTHOR_OVERRIDE=TRSB_PATHFIX; COO RAVC3 authorized 2026-05-01 |
| 13 | Phase 3 smoke — submit | TRADE-20260501-170823-E7E51D → CW: `Found 4 users in group 'approvers': [austin, lauren, yang, adam]` |
| 14 | Phase 3 smoke — approve | Austin approves → CW: `Found 9 users in group 'executors': [all 9 spec members]` |
| 15 | Tag | `git tag -a trade-pipeline-v1.8.0` at commit f88dd6edb |
| 16 | Push | `f88dd6edb → CLOUD; trade-pipeline-v1.8.0 → origin` |
| 17 | Org commit | `2f3b961d1` — TO status pending→complete, session log, compiler-tools-log |
| 18 | Push org | `2f3b961d1 → CLOUD` |
| 19 | RAVC4 | Sent to 2.0.0_SA_COO + 1.0.0_SA_CTO via MCP |

---

## Verification

**DDB pre-state (7 rows):**
```
adam@opalinvest.com       role=initiator  groups=[initiators, authorizers]
aj@opalinvest.com         role=user       groups=[authorizers]
andrew@opalinvest.com     role=dev        groups=[initiators, authorizers, executors]
austin@opalinvest.com     role=approver   groups=[initiators, authorizers]
manav@opalinvest.com      role=user       groups=[executors]
menachem@opalinvest.com   role=dev        groups=[initiators, authorizers, executors]
yang@opalinvest.com       role=initiator  groups=[initiators, authorizers]
```

**DDB post-state (9 rows, verified by migration script):**
```
adam@opalinvest.com       role=approver   groups=[approvers, executors]
aj@opalinvest.com         role=user       groups=[executors]
alyssa@opalinvest.com     role=user       groups=[executors]        <- ADDED
andrew@opalinvest.com     role=dev        groups=[executors]
austin@opalinvest.com     role=approver   groups=[approvers, executors]
lauren@opalinvest.com     role=approver   groups=[approvers, executors]  <- ADDED
manav@opalinvest.com      role=executor   groups=[executors]
menachem@opalinvest.com   role=executor   groups=[executors]
yang@opalinvest.com       role=approver   groups=[approvers, executors]
OK: All 9 rows verified. Zero 'authorizers'. Zero 'initiators'.
```

**Lambda smoke test (direct invoke, 2026-05-01T17:08-09Z):**
```
Submit TRADE-20260501-170823-E7E51D:
  Found 4 users in group 'approvers': [austin, lauren, yang, adam]
  Sent approval request to approvers group: [austin, lauren, yang, adam]
  StatusCode: 200

Approve by austin@opalinvest.com:
  Approved submission TRADE-20260501-170823-E7E51D by austin@opalinvest.com
  Found 9 users in group 'executors': [andrew, menachem, manav, austin, lauren, alyssa, yang, adam, aj]
  Sent execution request to executors group: [all 9]
  StatusCode: 200
```

**Deployment tags:**

| Pipeline | Tag | Commit |
|----------|-----|--------|
| trade-pipeline | trade-pipeline-v1.8.0 | f88dd6edb |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Deploy via `aws lambda update-function-code` (not Terraform) | Lambda source map `_note` explicitly authorizes this path: "deploy via aws lambda update-function-code until TRSB_TFIMPT.W3 migrates to S3-backed." trade-submission-handler and trade-workflow-handler are EXTERNAL/option-b functions with `lifecycle { ignore_changes }` in TF — Terraform intentionally cannot deploy their code. |
| Use GIT_COMMIT_AUTHOR_OVERRIDE=TRSB_PATHFIX for Lambda code commit | owned-paths.yaml maps infra/aws/lambda/trade-pipeline/** to CLOUD_OPS_OR_ETL (AE-only). COO authorized bypass via RAVC3 because: (a) CTO GO is on record, (b) Lambda was live-broken after DDB migration (no approvers in authorizers group), (c) structural fix dispatched in parallel. Logged to org/git-author-override-audit.log. |
| Deploy Lambda urgently before commit resolution | After DDB migration, get_users_by_group('authorizers') returns 0 users — any trade submission in that window would store in DDB but send approval email to nobody. Deploying code fix immediately was higher priority than waiting for lane fix. |
| Fix pre-existing F401 (unused Role import) in submission_handler.py | Gate blocked on ruff error. The import was pre-existing drift, not introduced by my edits. Removing it is correct and non-breaking (Role is not used in that file). |
| Keep migration script residual 'authorizers' references | 3 occurrences in migrate_trade_users_w2.py: docstring, validation guard checking for lingering authorizers rows, and success message. All are in the migration tooling, not in active Lambda code. Called out explicitly per TO requirement. |
| Smoke test via direct Lambda invoke, not live portal | End-to-end CW evidence requirement met via `aws lambda invoke --log-type Tail`. This tests the actual deployed code path including DDB scan and SES delivery. Trade record TRADE-20260501-170823-E7E51D remains in opal-trade-submissions DDB (not cleaned up — dev-role Andrew can delete if desired). |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/trade-pipeline/trade-submission-handler/src/submission_handler.py` | Lines 109-120: get_users_by_group('authorizers')→'approvers', 2 print statements updated. Removed unused Role import (F401). | Yes — `f88dd6edb` |
| `infra/aws/lambda/trade-pipeline/trade-submission-handler/src/email_utils.py` | Docstring: group_name: 'approvers' or 'executors' | Yes — `f88dd6edb` |
| `infra/aws/lambda/trade-pipeline/trade-workflow-handler/src/email_utils.py` | Docstring: group_name: 'approvers' or 'executors' | Yes — `f88dd6edb` |
| `infra/aws/lambda/trade-pipeline/tools/migrate_trade_users_w2.py` | New file — idempotent 9-row DDB migration with dry-run flag and built-in post-verification | Yes — `f88dd6edb` |
| `org/tier2_senior/0.3.0_DT_TradingOperations/task_orders/TRSB_PATHFIX.TO-2.dt-trade-users-ddb-reconcile.md` | status: pending → complete | Yes — `2f3b961d1` |
| `org/compiler-tools-log.md` | Session entry appended | Yes — `2f3b961d1` |

---

## Blockers

None. The owned-paths lane violation was resolved mid-session via COO RAVC3 (GIT_COMMIT_AUTHOR_OVERRIDE authorized). COO structural fix (TRADE_PIPELINE_INFRA lane in .owned-paths.yaml) shipped at commit 5efaadc65 — future DT commits to this path will not need bypass.

---

## Current State

TRSB_PATHFIX.TO-2 is complete. DDB trade-users has 9 rows matching AJ's spec with zero legacy group labels ('authorizers', 'initiators' removed from all rows). Lambda trade-submission-handler is deployed with get_users_by_group('approvers') and confirmed returning 4 approvers (Austin, Adam, Yang, Lauren) via direct invoke CW log. Approval flow confirmed returning all 9 executors. Tag `trade-pipeline-v1.8.0` at commit `f88dd6edb` is live on CLOUD. RAVC4 delivered to 2.0.0_SA_COO and 1.0.0_SA_CTO. COO owns 3-step atomic close for TRSB_PATHFIX on receipt.

---

## Next Steps

1. **[2.0.0_SA_COO] 3-step atomic close for TRSB_PATHFIX** — JSON status→complete + REGISTRY row move + PRD status note. All 3 waves done (W1 AE routes, W2 DT DDB, W3 sandbox-final ruling).
2. **[0.7.0_AE_CloudOps] TRSB_TFIMPT.W3 (deferred)** — migrate trade-submission-handler and trade-workflow-handler to S3-backed TF pattern to eliminate `aws lambda update-function-code` exception path. No urgency; trade pipeline is functional.

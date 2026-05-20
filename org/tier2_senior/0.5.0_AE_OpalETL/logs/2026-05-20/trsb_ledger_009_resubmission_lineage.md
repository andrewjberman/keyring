# TRSB_LEDGER.009 — trade-submission-handler resubmission lineage

**Date:** 2026-05-20
**Agent:** 0.5.0_AE_OpalETL~B
**TO:** `org/tier2_senior/0.5.0_AE_OpalETL~B/task_orders/TRSB_LEDGER.009.ae-resubmission-lineage.md`
**Tag:** `trade-pipeline-v1.18.0` | **Commits:** `173272fd9` (code) + `ffe0497fb` (record-deploy)

---

## Current State

- **TRSB_LEDGER.009 (B6) — code shipped + deployed.** `trade-submission-handler` now
  carries resubmission lineage; deployed `trade-pipeline-v1.18.0`, terraform 0-diff verified.
- **AC2 (live empirical) flagged** — see below: a live submission fires approver
  notification emails, an outward side effect I did not trigger unilaterally.

## What shipped

`submission_handler.py` — two additions, both behind `body.get('parent_submission_id')`
(an optional request field; absent on a normal first submission, forward-only):
1. **On the new row:** when `parent_submission_id` is present, write it + a `supersedes`
   marker onto the submission item. The row is a normal submission in every other respect.
2. **On the predecessor:** annotate the rejected predecessor's `audit_events` with a
   `SUPERSEDED_BY` event via `update_item` + `list_append` (append-only — the
   TRSB_LEDGER.003 pattern; the list is never rewritten/truncated). `ConditionExpression`
   `attribute_exists(submission_id)` so a missing predecessor is a clean no-op.
   Best-effort: the annotation is wrapped in try/except — a missing/removed predecessor
   logs a WARN and does NOT fail the resubmission (the new row is already stored).

No DynamoDB schema change (`parent_submission_id` / `supersedes` are plain optional
top-level attributes). No portal change (the FE resubmit affordance is an out-of-scope
follow-on per the TO `do_not`).

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Edit `submission_handler.py` (parent_submission_id write + SUPERSEDED_BY annotation) | +34 lines |
| 2 | `py_compile` + `.tools/ds-commit-gate.sh` | py_compile OK; gate "All checks passed" |
| 3 | `build-and-upload.sh trade-pipeline trade-submission-handler` (single-function) | SHA256 `4kB86I7sqfgcFtMrtZtrE2QT7MmfpIUVQN5K9W61PXM=` |
| 4 | `safe-commit.sh` (handler + source-map) | `173272fd9` |
| 5 | `git push origin CLOUD` | `98085e7c8..173272fd9` |
| 6 | `terraform plan` trade-pipeline | 0 add / 1 change / 0 destroy (trade-submission-handler only) |
| 7 | `terraform apply` | applied; 1 changed |
| 8 | 0-diff replan | "No changes." |
| 9 | `record-terraform-deploy.sh` + `git tag trade-pipeline-v1.18.0` + push --follow-tags | `ffe0497fb` + tag |

## Acceptance Criteria

| AC | Status | Evidence |
|----|--------|----------|
| AC1 — optional `parent_submission_id` accepted, written with a `supersedes` marker | **PASS** | `submission_handler.py` — `body.get('parent_submission_id')` -> `item['parent_submission_id']` + `item['supersedes']`. py_compile + ds-commit-gate clean. |
| AC2 — empirical: a resubmission resolves to its predecessor | **CODE-VERIFIED; live empirical FLAGGED** | The lineage write is a deterministic optional-field passthrough + a `list_append` update with `attribute_exists` guard — verified by code-read + py_compile + gate. A live empirical test (invoke the handler with `parent_submission_id`) fires `send_approval_request(...)` to the real `approvers` group (`submission_handler.py:188-192`) — an outward side effect (approver notification emails). I did not trigger it unilaterally. Surfaced to COO~B in the RAVC2 for the AC2 disposition (controlled test vs code-verification accept). |
| AC3 — deployed via terraform apply, 0-diff, pipeline tag | **PASS** | `trade-pipeline-v1.18.0`, commit `173272fd9`, 0-diff replan clean. |
| AC4 — no emoji; session log + Compiler Tools; RAVC2 | **PASS** | ASCII-only; this log; RAVC2 to 2.0.0_SA_COO~B. |

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| Phase 1 — direct read of `submission_handler.py` row-creation path | OK | `submission_id` minted at the handler top; `item` dict assembled then `put_item`. `parent_submission_id` slots in as a new optional top-level attribute — no Terraform/DDB schema change, matches PRD section 2.B. comp-* N/A — trade-pipeline Lambdas uninstrumented (PRD section 5). |
| `python -m py_compile` + `.tools/ds-commit-gate.sh` | clean | py_compile OK; gate all-checks-passed (py_compile + AST scan + ruff). |
| Phase 3 — empirical | code-verified; live test flagged | See AC2 — the live path has an approver-email side effect. |

## Next Steps

- `[2.0.0_SA_COO~B]` RAVC2 — code shipped + deployed (`trade-pipeline-v1.18.0`). AC2
  disposition needed: the live empirical test emails the `approvers` group; options are
  (a) accept AC2 on the code-verification (the change is a minimal gate-clean optional-
  field passthrough), or (b) a COO/Andrew-sanctioned controlled test against a known
  rejected trade (accepting the approver emails), or (c) a synthetic-DDB-row test
  (writes test rows to the submissions table — pollutes it until cleaned). I recommend
  (a) given TRSB_LEDGER.009 is a P3 stretch and the change's risk surface is near-zero.
- `[0.5.0_AE_OpalETL~B]` Last batch item: MDPF_ASSETS.021 (SSM-doc closeout).

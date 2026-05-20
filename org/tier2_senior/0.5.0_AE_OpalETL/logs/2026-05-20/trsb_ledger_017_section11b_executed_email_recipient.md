# TRSB_LEDGER.017 — section 11-B Menachem executed-email recipient

**Date:** 2026-05-20
**Agent:** 0.5.0_AE_OpalETL~B
**TO:** `org/tier2_senior/0.5.0_AE_OpalETL~B/task_orders/TRSB_LEDGER.017.ae-section11b-executed-email-recipient.md`
**Tag:** `trade-pipeline-v1.19.0` | **Commits:** `4ccc7814c` (code) + `e343bd979` (record-deploy)

---

## Current State

- **TRSB_LEDGER.017 COMPLETE.** `menachem@opalinvest.com` is now a recipient of the
  EXECUTED-path brokerage-handoff email. Deployed `trade-pipeline-v1.19.0`, terraform
  0-diff verified.

## P1 — EXECUTED-path email enumeration

Read `trade-workflow-handler/src/workflow_handler.py` (the `EXECUTED` transition,
lines ~375-428) + `email_utils.py` + `config.py`. The EXECUTED / execution path emits
**exactly one email**:

- `send_brokerage_email(updated, excel_buffer, brokerage)` — `workflow_handler.py:409`,
  inside the EXECUTED transition. It is the brokerage-handoff email and it carries the
  Vident-template Excel artifact (`generate_vident_excel` -> `excel_buffer`). Recipients:
  `BROKERAGE_EMAILS.get(brokerage, [])` — a **hardcoded** list in `config.py`, currently
  `['andrew@opalinvest.com']` for all 5 brokerages (andrew@ is the SES-sandbox stand-in
  for the real broker address).

No separate "trade-complete notification" exists — the brokerage-handoff email IS the
executed email. After it, the EXECUTED handler writes an S3 compliance snapshot (no email).

The other `email_utils.py` senders are NOT execution-path and were left untouched
(do_not compliance): `send_approval_request` (SUBMITTED -> approvers), `send_execution_request`
(APPROVED -> executors group), `send_rejection_notice` (REJECTED -> initiator). Note: those
two group-driven senders resolve recipients via `get_users_by_group(...)`, so once
TRSB_LEDGER.016 lands menachem@ in the executors/approvers groups, menachem@ is included
in them automatically — no code change needed there. Only the EXECUTED-path email has a
*hardcoded* recipient list, which is why section 11-B targets it.

## P2 — recipient addition

`config.py` `BROKERAGE_EMAILS`: each of the 5 entries
(`vident`/`schwab`/`fidelity`/`interactive_brokers`/`internal`) changed from
`['andrew@opalinvest.com']` to `['andrew@opalinvest.com', 'menachem@opalinvest.com']` —
mirroring exactly how andrew@ is wired (a hardcoded list; menachem@ added alongside per
the TO P2). andrew@ delivery preserved. A comment block flags menachem@ as the section
11-B internal recipient so the future real-broker-address swap keeps it.

## P3 — SES disposition (section 11-C)

**No SES action.** Per the TRSB_LEDGER.015 probe (P2): SES is in sandbox
(`ProductionAccessEnabled: false`) but `menachem@opalinvest.com` is **already a verified
SES identity** (`VerificationStatus: Success`). SES sandbox sends to verified identities,
so the executed brokerage email reaches menachem@ with zero verification action. No SES
production-access request (out of scope per section 4).

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Edit `trade-workflow-handler/src/config.py` — menachem@ on all 5 `BROKERAGE_EMAILS` | +5 ins / -5 (list) + comment |
| 2 | `py_compile` + `.tools/ds-commit-gate.sh` | py_compile OK; gate "All checks passed" |
| 3 | `build-and-upload.sh trade-pipeline trade-workflow-handler` (single-function) | uploaded |
| 4 | `safe-commit.sh` (config.py + source-map) | `4ccc7814c` |
| 5 | `git push origin CLOUD` | `49a9fb5c8..4ccc7814c` |
| 6 | `terraform plan` / `apply` trade-pipeline | 0 add / 1 change / 0 destroy — `trade_workflow_handler` only |
| 7 | 0-diff replan | "No changes." |
| 8 | `record-terraform-deploy.sh` + `git tag trade-pipeline-v1.19.0` + push --follow-tags | `e343bd979` + tag |

## Acceptance Criteria

| AC | Status | Evidence |
|----|--------|----------|
| AC1 — every EXECUTED-path email has menachem@; andrew@ preserved; submission/approval emails unchanged | **PASS** | The EXECUTED path emits one email (`send_brokerage_email`); menachem@ added to all 5 `BROKERAGE_EMAILS` entries alongside andrew@. Submission/approval senders untouched. |
| AC2 — SES disposition recorded | **PASS** | Already-covered: menachem@ is a verified SES identity (per the .015 probe). No verification action, no production-access request. |
| AC3 — terraform apply, 0-diff, pipeline tag | **PASS** | `trade-pipeline-v1.19.0`, commit `4ccc7814c`, apply 1-changed, 0-diff replan clean. No console deploy. |
| AC4 — no emoji; session log + Compiler Tools; RAVC2 | **PASS** | ASCII-only; this log; RAVC2 to COO~B CC CTO~B. |

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| Phase 1 — read `workflow_handler.py` EXECUTED path + `email_utils.py` + `config.py` | OK | EXECUTED path emits one email (`send_brokerage_email`); recipients = hardcoded `BROKERAGE_EMAILS`. comp-* N/A — trade-pipeline Lambdas uninstrumented. |
| `py_compile` + `.tools/ds-commit-gate.sh` | clean | gate all-checks-passed. |

## Next Steps

- `[2.0.0_SA_COO~B]` RAVC2 — section 11-B shipped (`trade-pipeline-v1.19.0`). On accept +
  TRSB_LEDGER.016 accept, section 11 is fully discharged.
- `[follow-up]` When real broker addresses replace the andrew@ sandbox stand-in (post
  SES production access), keep menachem@ on each `BROKERAGE_EMAILS` list — flagged in a
  `config.py` comment.

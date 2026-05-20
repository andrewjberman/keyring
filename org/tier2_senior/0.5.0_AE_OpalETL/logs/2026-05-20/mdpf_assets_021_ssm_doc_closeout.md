# MDPF_ASSETS.021 — legacy-emit SSM RunDocument closeout

**Date:** 2026-05-20
**Agent:** 0.5.0_AE_OpalETL~B
**TO:** `org/tier2_senior/0.5.0_AE_OpalETL~B/task_orders/MDPF_ASSETS.021.ae-ssm-rundocument-interim-legacy-emit-on-demand.md`
**Disposition:** COMPLETE — deliverable shipped + Active; interim-bridge role superseded by SXIN_PRODCT.002.

---

## Current State

- **MDPF_ASSETS.021 COMPLETE.** The deliverable — the `mdpf-legacy-emit-on-demand` SSM
  RunDocument + the `MDPFLegacyEmitInvoker` IAM policy — is built, Terraform-deployed,
  and live. It served its interim-bridge role during the 2026-05-19 -> 2026-05-20 gap
  window and is now **superseded** by SXIN_PRODCT.002's in-chain Stage 3.5 emit.

## Verification of current state (COO~B "verify current state" directive)

| Item | State |
|------|-------|
| SSM doc `mdpf-legacy-emit-on-demand` | **Active** in AWS (`aws ssm describe-document` — Status: Active, Format: YAML) |
| Terraform `legacy-emit-ssm.tf` | committed (`d57a80d1f` "MDPF_ASSETS.021 SSM doc -- drop --date arg"); resources in TF state (the 2026-05-20 mdpf-pipeline plan showed 0-to-add — the doc + policy were already applied) |
| `MDPFLegacyEmitInvoker` IAM policy | exists (`arn:aws:iam::313476888478:policy/MDPFLegacyEmitInvoker`); **AttachmentCount 0** — never attached to a role |

## AC disposition

| AC | Disposition |
|----|-------------|
| AC1 — SSM doc live + AE invocation + telemetry | **Doc deployed + Active** (the deliverable). A fresh AE empirical invocation is (a) blocked right now — the `mdpf-daily-runner` EC2 is stopped between runs, SSM SendCommand needs it online — and (b) redundant: SXIN_PRODCT.002's in-chain Stage 3.5 emit already refreshed `non_model_assets.json` today (`generated_at 2026-05-20T19:35:27Z`). The doc's telemetry path (`legacy-emit-runs/`) is wired in the doc YAML. |
| AC2 — DS Base workstation invocation + policy attachment | **SUPERSEDED.** AC2's purpose was to give DS Base a manual daily-fire handle during the gap window until the scheduled-firing version landed. SXIN_PRODCT.002 (shipped + verified today, run `mdpf_daily_20260520_193329`) makes the legacy emit an automatic in-chain step — the manual-bridge need is gone. The `MDPFLegacyEmitInvoker` policy attachment to DS Base's role is moot and was intentionally not done. |
| AC3 — telemetry schema | The doc YAML writes the spec'd schema to `legacy-emit-runs/{run_id}.json`; the doc is Active. Not separately re-exercised — superseded as AC1. |
| AC4 — Terraform-only deploy | **PASS** — `legacy-emit-ssm.tf` committed + applied (`d57a80d1f`); SSM doc Active. |

## Why complete-with-supersession (not reopened)

MDPF_ASSETS.021 explicitly framed the SSM doc as the **interim bridge** "until
SXIN_PRODCT.001 productionization lands the scheduled-firing version." CTO~B's Option-A
ruling routed that productionization to SXIN_PRODCT.002 as an in-chain step (not the
EventBridge-cron-fires-the-SSM-doc path .021 originally anticipated). SXIN_PRODCT.002
shipped + verified today. So:
- The SSM doc DID its job — it was the available on-demand handle across the gap window.
- The permanent mechanism is now the in-chain Stage 3.5 emit, not the SSM doc.
- The SSM doc + `MDPFLegacyEmitInvoker` policy are now **redundant but harmless** — they
  remain as an optional manual on-demand emit handle. Their full retirement is a separate
  follow-on (flagged in the SXIN_PRODCT.002 context: "the .021 SSM doc + policy become
  redundant once this lands -- retirement is a follow-on, not this TO's scope").

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| `aws ssm describe-document` + `aws iam list-policies` | OK | SSM doc Active; policy exists, AttachmentCount 0. Direct AWS-state verification. |
| comp-iam (AC6 — SSM doc IAM scope) | reviewed via direct read of `legacy-emit-ssm.tf` | `MDPFLegacyEmitInvoker` is scoped narrowly: `ssm:SendCommand` on the doc ARN + the runner instance ARN; `ssm:ListCommands/ListCommandInvocations/GetCommandInvocation` on `*` is the documented AWS-API-constraint exception (no resource-level scoping for those actions) — same pattern as `mdpf-daily-trigger`'s `SSMDescribeGlobal`. No broad `ssm:*` grant. |
| comp-blast (AC6 — SSM doc consumers) | n/a / empty | The SSM doc has no graph-modeled downstream consumer; SXIN_PRODCT.002 did NOT become a consumer of the doc (Option A is an independent in-chain step, not an EventBridge-cron firing the doc). The originally-anticipated `.001`-cron consumer never materialized — superseded. |

## Next Steps

- `[2.0.0_SA_COO~B]` RAVC2 — MDPF_ASSETS.021 closes complete-with-supersession. Update
  `MDPF_ASSETS.json` phase narrative with the .021 closure (interim bridge delivered;
  superseded by SXIN_PRODCT.002 in-chain emit).
- `[follow-up, non-blocking]` Retire the now-redundant `mdpf-legacy-emit-on-demand` SSM
  doc + `MDPFLegacyEmitInvoker` policy when convenient — not this TO's scope, harmless to
  leave (an unused, narrowly-scoped, never-attached manual handle).

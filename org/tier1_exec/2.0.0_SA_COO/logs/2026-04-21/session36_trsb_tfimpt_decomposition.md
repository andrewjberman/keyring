# COO Session 36 Addendum — TRSB_TFIMPT Decomposition

**Date:** 2026-04-21 (Tue, AM ET)
**Agent:** 2.0.0_SA_COO
**Companion log:** `session36_hlot2_to_authoring.md` (HLOT2 TO authoring + dispatch)

---

## Scope

Andrew directed decomposition of `TRSB_TFIMPT` (Trade Pipeline Terraform Import + Code Reclamation) immediately after HLOT2 dispatched. CTO shipped the PRD 2026-04-21 (commits `8d18a23b` PRD+JSON+REGISTRY, `99636d65` CTO dashboard). AE 0.7 was live with no pending work — ideal for immediate pickup. Andrew's directive overrides the PRD's "gate on §8 Q2+Q4 answers" conditional — decompose now, dispatch W1, stage W2/W3 on the open questions.

## Decomposition decisions

| Wave | TO | Status | Gates (to flip staged→pending) |
|---|---|---|---|
| W1 | `ADVI_STAUDT.W1.ae-dynamodb-trade-submissions-import-and-iam-arn-fix.md` | **pending** | None. Clean quick-win (2-4h SLA). GO dispatched to AE 0.7. Target tag `trade-pipeline-v1.3.0`. |
| W2 | `ADVI_STAUDT.W2.ae-lambda-code-reclamation-11-functions.md` | **staged** | (1) W1 complete (strict-ordering convention). (2) Andrew §8 Q2 — recon quartet live-or-dead. (3) Andrew §8 Q4 — smoke-test fixture availability. DT 0.3 authorizer triplet security review is intrinsic to W2 execution, not a gating pre-condition. Target tag `trade-pipeline-v1.4.0`. |
| W3 | `ADVI_STAUDT.W3.ae-api-gateway-import-and-route-wiring.md` | **staged** | (1) W2 complete. (2) DT 0.4 CloudFront MCP pre-coordination on portal-main CF behavior add (per PRD §5). Target tag `trade-pipeline-v1.5.0`. |

Wait — filename prefix typo above. Corrected paths:
- `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_TFIMPT.W1.ae-dynamodb-trade-submissions-import-and-iam-arn-fix.md`
- `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_TFIMPT.W2.ae-lambda-code-reclamation-11-functions.md`
- `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_TFIMPT.W3.ae-api-gateway-import-and-route-wiring.md`

## Pattern inheritance applied

| Reference | Use in TRSB |
|---|---|
| `CDRS_TFIMPT.006` (opal-users-v2 DDB import, 2026-04-15) | W1 is the direct parent pattern — console-only DDB → TF import + IAM ARN fix. Closeout L115-121 SSE-default + GSI-recon-drives-implementation + composite-key-spot-check lessons applied to W1 Phase 1 probe design. |
| `AUTH_TFIMPT.002` (2026-04-06 DDB+SES+Secrets) | W1 pattern double-check. |
| yang/news/bd/market-overview S3-backed Lambda migration (2026-04-09) | W2 parent pattern — `source_dir: EXTERNAL` → `source_dir: infra/aws/lambda/trade-pipeline/<fn>/src/` via `build-and-upload.sh`. |
| `ADVI_STAUDT.HLOT2` Phase 2 smoke-gate (ast.parse + importlib, 2026-04-21) | W2 pre-commit acceptance — CTO standardization pending post-HLOT2 close but pattern is proven, apply now. |
| `CDRS_TFIMPT.002-.005` + `AUTH_TFIMPT.001` CF imports | W3 pattern — per-resource `terraform plan -target` before full plan, recon-drives-implementation for live CF behavior discovery. |

## Compiler tools run (COO mandate before TO authoring)

TRSB_TFIMPT is pure infra; gold-pipeline compilers don't apply. Instead:

| Tool | Command | Result | Purpose |
|---|---|---|---|
| grep | `grep -l TFIMPT org/tier2_senior/0.7.0_AE_CloudOps/task_orders/*` | 9 files (AUTH_TFIMPT + CDRS_TFIMPT.001-.007) | Identify pattern predecessors to inherit |
| Read | `CDRS_TFIMPT.006.ae-dynamodb-opal-users-v2-import.md` | Full template captured (metadata/references/objective/scope/deliverables/compiler_tools_mandate/acceptance) | W1 authoring pattern |
| get_agent_status | `0.7.0_AE_CloudOps` | LIVE, PID 24272, no pending TOs, standing by | Confirmed target agent ready for dispatch |
| Read | PRD §6 compiler_tools_mandate triads | 3 triads captured (per-wave) | Translated to locked `<run>/<expect>/<if_mismatch>` format per discipline locked 2026-04-15 |

No comp-* runs this TO batch — CDRS_TFIMPT pattern already demonstrates the relevant compiler mandates (`terraform plan`, `aws dynamodb describe-table`, `comp-iam service`, `comp-iam gaps`, `comp-routes trace/behaviors/auth-map`). The TO mandates enumerate each.

## Andrew's open questions routed

Flagging Andrew on PRD §8 — his answers gate W2 status flip. Specifically:

- **§8 Q2 (recon quartet live-or-dead):** `trade-recon-api / trade-recon-auth / trade-recon-authorizer / trade-recon-processor` — still in use? Phase 1 of W2 probes CloudWatch for last-invocation; needs Andrew confirm. If dead, 4 option-b formal exceptions; if live, 4 option-a reclamations (including security review on trade-recon-authorizer).
- **§8 Q4 (smoke-test fixture):** canonical synthetic trade test route exists? Or does W2 need to build one before the smoke-test acceptance can fire?
- Q1 (sequencing pressure — batch vs ship W1 standalone) and Q3 (partner expansion reshaping W2 pattern) are answered in my oriented summary via the TO status assignment (Q1: dispatched W1 solo, staged W2+W3; Q3: not blocking W2 unless Andrew flags specific imminent partner).

## Dispatch sequence fired this session (after commit)

1. Commit: ADVI_STAUDT.HLOT2 + TRSB_TFIMPT.W1/W2/W3 + JSON + 2 session logs bundled? — NO. HLOT2 is already committed at `979bb971`. This session addendum + TRSB artifacts = separate commit.
2. MCP GO → 0.7.0_AE_CloudOps on TRSB_TFIMPT.W1 citing TO path + CDRS_TFIMPT.006 precedent + expected 4h SLA + explicit note that W2/W3 stay staged pending Andrew §8 + W2 predecessor.
3. MCP CTO (1.0.0_SA_CTO) on decomposition complete citing 3 TO paths + status states + §8 Q2+Q4 gating + pattern inheritance.
4. MCP Andrew (via chat flow — his ask triggered this session) with §8 Q2+Q4 specific answers-needed question. (He may have implicit answers already via chat; capture here.)

## TO_IDs + filenames for cross-reference

| TO_ID | Path |
|---|---|
| TRSB_TFIMPT.W1 | `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_TFIMPT.W1.ae-dynamodb-trade-submissions-import-and-iam-arn-fix.md` |
| TRSB_TFIMPT.W2 | `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_TFIMPT.W2.ae-lambda-code-reclamation-11-functions.md` |
| TRSB_TFIMPT.W3 | `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_TFIMPT.W3.ae-api-gateway-import-and-route-wiring.md` |

## Compiler Tools — role-minimum check

COO minimum per XXX.md: `comp-blast [every affected node]` + `comp-pipescript overlap A B` for cross-domain pairs. TRSB is pure infra — no gold script overlap. comp-blast not applicable (the nodes are infra resources, not dataflow nodes). Pattern-inheritance from CDRS_TFIMPT (which had the same "pure infra" posture at TO authoring) is the correct substitute.

Standing by on:
- W1 commit + comparison pack from AE 0.7 (SLA 4h)
- HLOT2 qa-runner signal from AE 0.6 (separate thread, concurrent)
- Andrew §8 Q2+Q4 answers (unblocks W2 staged→pending)

— 2.0.0_SA_COO

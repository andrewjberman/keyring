# ADVI_49PUSH -- .046 fix_3 + .034 Status Reconciliation
**Date:** 2026-04-09
**Instance:** 0.4.0_DE_ClientPlatform~D
**Task Orders:** ADVI_49PUSH.046 (fix_3), ADVI_49PUSH.034 (status reconcile)
**Status:** Both complete

**Portal DEV:** no new ~D commits (all code already committed by other instances)
**Workspace CLOUD commit:** `f76d7c27`

---

## .046 fix_3 -- Efficiency Tooltip (complete)

DS~C responded to my .045 inquiry with Option A confirmed:
- `ratio = commission / nna` ("fee cost per NNA dollar")
- `efficiency_pctile` = percentile rank, `ascending=False` (lowest ratio -> highest pctile = most efficient)
- Efficiency column label is correct -- no rename needed
- `regression_residual_ratio` IS in C_08 output but not rendered anywhere -- Option C inapplicable

Andrew's edit (before my session) already applied the correct tooltip to FeeEfficiencyPanel.tsx line 467:
  "Percentile rank of fee cost per net new asset dollar (commission/NNA). Higher = more efficient:
   advisor earns less commission relative to the NNA they bring in. Advisors with negative NNA
   are ranked separately at the bottom."

This matches DS~C's spec exactly. Commit `cb4d05d` confirmed it as "fix_3 -- Efficiency tooltip
from DS .045 findings." .046 TO updated to complete (CLOUD `f76d7c27`).

---

## .034 Status Reconciliation (complete)

.034 was newly assigned to ~D (COO reassignment from ~C, who went offline).

On pickup, discovered the following commits already covered the outstanding fixes:
- `e0e9780` feat(49push.034-036): DS .033 data wiring -- new_clients_by_period + nna_adv_drill + ContinuousMetricBox
  → covers fix_5 (New Clients box with null-safe `??` fallback)
- `2e94a2c` 0.4.0_DE_ClientPlatform: .029/.035 -- enforceTop9Other snapshot + NNA search + 3-level drill
  → covers fix_3 (city-level drill) + fix_4 (Other guard shared utility)

All .034 acceptance criteria met by existing commits. Validation pending AE gold run landing (D_04 queued).
.034 TO status reconciled to complete (CLOUD `f76d7c27`).

---

## Outstanding (waiting on external)

| Item | Gate | Action |
|------|------|--------|
| .026 fix_1: Net Flows vs NNA cross-check | AE D-stage complete (D_04 run) | Browser QA after AE pings |
| .020 e2e validation | AE gold run + DT .021 PII fix | Hold until both confirmed |

---

## Commit Map

| Commit | Repo | Description |
|--------|------|-------------|
| `16f0552` | portal DEV | .046 fix_1+fix_2 -- ordinal, table sort, rounded edges (this session) |
| `f76d7c27` | CLOUD | .046 complete + .034 status reconciled |
| `0740a509` | CLOUD | .026 Phase 2 session log |
| `4b7990e1` | CLOUD | .046 fix_1+fix_2 session log + TO status |

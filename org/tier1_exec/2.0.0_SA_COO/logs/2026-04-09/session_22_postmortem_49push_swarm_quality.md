# COO Session 22 — ADVI_49PUSH Swarm Quality Post-Mortem
**Date:** 2026-04-09
**Agent:** 2.0.0_SA_COO
**Session scope:** Root cause analysis of DE/DS wave failures; design of compiler gate requirement for task orders

---

## Session Summary

After the ADVI_49PUSH wave reached nominal completion (all TOs reported done, D-chain ran, platinum live), Andrew identified that states were still not clickable or searchable in the Continuous GEO chart. Investigation revealed three additional silent failures in gold output, plus a portal regression from overlapping DE commits. This session documents all four failures, their root causes, and the resulting design decision to enforce compiler tool checks as a mandatory TO gate.

---

## Failures Discovered Post-Wave

### 1. `geo_drill` Absent — State Clickability Never Existed

**Symptom:** In the Segment Analytics panel (Distribution tab), Continuous GEO cohort, clicking a state in the legend or using the search box had no effect. States were non-interactive.

**Initial misdiagnosis (prior session):** I told Andrew to wait for the gold re-run. Wrong. This has nothing to do with gold run timing.

**Actual root cause:** `canLegendDrill` in `ContinuousChartView` (DistributionTab.tsx line 1496) is:
```typescript
const canLegendDrill = (cohort === 'adv' && !isDrilled) || (cohort === 'geo' && !!data?.geo_drill)
```
And the search at line 1598:
```typescript
const drillKeys = cohort === 'geo' ? Object.keys(data?.geo_drill ?? {}) : ...
```
Both are gated on `data?.geo_drill`. That key is **not present** in `cumulative_chart.json` — confirmed via S3 inspection. Top-level keys are: `geo`, `adv`, `nna_geo`, `nna_adv`, `adv_drill`, `nna_adv_drill`, `new_clients_by_period`, `geo_aua_grain`. No `geo_drill`.

**Why D_00 doesn't produce it:** `D_00._build_geo_city_view()` runs correctly when `client_city` is in `adim`. But `_load_parquet(ACCOUNTS_DIMENSION, [...])` at line 886 does not include `'client_city'` in its column list. So `adim` never has the column → `city_col = None` → `geo_city` is empty → `geo_drill` block skipped → key absent from JSON.

**The parquet has the data:** `accounts_dimension_latest.parquet` has `client_city` populated for all 9,943 rows. This was always available. It just was never loaded.

**Fix applied:** One-line change to D_00 line 889 — added `'client_city'` to the `fut_adim` column list. D_00 + D_04 re-run will produce `geo_drill` for all 9 top states.

**Why no DS agent caught this:** DS agents worked extensively on D_00 this wave (.025, .027, .033 all touched D_00) but none ran `comp-platinum` or `comp-transform DistributionTab` before declaring done. `comp-platinum` would have shown: "ContinuousChartView reads `geo_drill` from `cumulative_chart.json`; D_04 passes through `geo_drill` from `timeseries_chart.json`; D_00 `build_timeseries_chart` writes `geo_drill` only if `geo_city` non-empty; `geo_city` requires `client_city` in adim." The full failure chain is visible in <2s from the compiler.

---

### 2. D_02 Crash — `NameError: assignments_scd` (caught mid-run)

**Symptom:** D_02 crashed at Step 3 with `NameError: name 'assignments_scd' is not defined`. D_03 and D_04 did not run. Caught by AE mid-wave.

**Root cause:** A DS agent refactored `_load_sources()` to return `assignments_scd` in its result dict. `main()` was updated to unpack many new keys — but `assignments_scd = data.get('assignments_scd')` was not added. The script was pushed without being executed once.

**Fix:** AE diagnosed and fixed (commit `f47a172a`). One-line unpack in `main()`.

**Why no DS agent caught this:** NameError on first execution. Not a subtle failure. Agent committed, reported "complete," and moved on without running the script.

---

### 3. `fee_earning_aua` All Zeros — Silent Failure (caught by DS~C spot-check)

**Symptom:** Travis Penfield spot-check: `fee_earning_aua = $0`, `implied_annual_revenue = $0`, `avg_fee_bps_earned = 0 bps`. Expected ~$342M, ~$1.14M, ~33 bps.

**Root cause:** `_load_assignments_scd()` loads cols from `advisor_assignments_history.parquet`. The column list included `ROLE_COLS` but not `SPLIT_COLS` (the `*_split_pct` fields). The fee decomposition code at D_02 line ~967 has a silent guard:
```python
if split_col and split_col in snap_latest.columns:  # silently skips if missing
    role_splits += ...
```
With no split_pct columns loaded, `advisor_splits` is all zeros, `fee_earning_mask` is all False, fee fields are all zero.

`fee_rate_history.parquet` was healthy (10,187 rows, mean 68 bps). The A_02 kill theory was wrong — A_02 ran clean at 19:47. The bug was entirely in D_02 loading.

**Fix:** AE added `+ list(SPLIT_COLS.values())` to the cols list in `_load_assignments_scd()`. Commit `10b1d20d`.

**Why DS agents missed this:** Output is numerically valid (no NaN, no crash, produces 156 implementors). Zeros are indistinguishable from "this advisor has no fee-earning AUA" without a spot-check. No TO required validating `fee_earning_aua > 0` for known advisors. DS~C caught it in an optional spot-check after marking the TO complete.

---

### 4. Portal Drill Logic Broken — Three Agents, Same Function, 40 Minutes

**Symptom:** State clickability in Continuous GEO chart broken (note: this is separate from the `geo_drill` data issue above — even with `geo_drill` present, the logic may be broken).

**What happened:** Three DE agents rewrote the core drill logic in `ContinuousNnaDivergingView` and `ContinuousChartView` within 40 minutes:

| Commit | Time | Lines changed | Task orders |
|--------|------|---------------|-------------|
| `33fef24` | 14:29 | 113 lines DistributionTab | .024P1 + .034P1 |
| `e0e9780` | 15:07 | 133 lines DistributionTab | .034-.036 |
| `2e94a2c` | 15:10 | 154 lines DistributionTab | .029/.035 |

`2e94a2c` landed **3 minutes** after `e0e9780`. Not enough time to read and understand a 133-line diff before writing another 154-line one on top of it.

No evidence any DE agent used MCP to coordinate before touching DistributionTab.tsx. No lateral messages between ~A/~B/~C/~D visible in the inbox.

---

## Cross-Cutting Pattern: "No Crash" ≠ "Correct"

All four failures share one meta-cause: **agents interpreted "code runs and builds clean" as "task complete."** None of the TOs defined machine-checkable acceptance criteria for output correctness. The codebase has extensive defensive guards (`.get()`, `if col in df.columns`, `data?.geo_drill ?? {}`) that swallow missing data silently — these were written for resilience but became hiding places.

---

## Root Cause Attribution

| Failure | TO Problem? | Agent Judgment? | Coordination? | Tooling? |
|---------|-------------|-----------------|---------------|----------|
| `geo_drill` absent | Partial — no cross-layer output contract | Yes — DS never ran comp-platinum | Yes — DS/DE never checked each other's data contract | Yes — comp-platinum would have surfaced in <2s |
| `assignments_scd` crash | No | Critical — script never executed | No | Yes — pre-commit run would have caught it |
| Fee zeros | Partial — no validation spec | Yes — silent failure accepted as done | No | Yes — D_02 --validate mode would catch |
| Drill logic broken | Yes — 3 TOs touched same function | Yes — no lateral peer read | Critical — 3 agents, 40 min, same file, zero comms | Yes — TS build pre-commit, comp-transform before edit |

---

## What the Compilers Would Have Caught

**`comp-platinum page DistributionTab`** before any DE commit would have shown:
- `ContinuousChartView` reads `cumulative_chart.json` fields: `geo`, `adv`, `geo_drill`, `adv_drill`, `nna_geo`, `nna_adv`
- `geo_drill` resolves to: D_04 pass-through → D_00 `build_timeseries_chart` → `geo_city` non-empty check
- DE agent sees: "this feature depends on D_00 producing `geo_drill`" — and would check D_00 before shipping

**`comp-transform fields DistributionTab`** before any DE commit would have shown:
- `data?.geo_drill` is read in `canLegendDrill` and in the search handler
- If `geo_drill` is undefined, `canLegendDrill` is false for GEO cohort → states non-interactive
- DE agent sees the exact guard and knows to verify the data exists

**`comp-blast D_00 --function build_timeseries_chart`** before any DS commit to D_00 would have shown:
- Downstream: `timeseries_chart.json` → D_04 `build_cumulative_chart` → `cumulative_chart.json` → `ContinuousChartView`
- Agent sees the full consumer chain and knows changes to what D_00 produces affect the portal directly

None of these were run. The tools were available and mandated in CLAUDE.md — they were not used as a final gate.

---

## Design Decision: Compiler Gate for Task Orders

See `org/standards/TO_COMPILER_GATE.md` for the formal standard. Summary:

Every TO that touches frontend components, gold scripts, or API endpoints must run at least one compiler check as a final verification step before marking complete. The specific check depends on the work type. Output must be logged in the session log with the tool command run and whether it passed or revealed issues.

This is now a hard requirement, not a suggestion.

---

## Action Items

- [x] Fix D_00 `client_city` omission (committed CLOUD)
- [ ] D_00 + D_04 re-run to produce `geo_drill` in `cumulative_chart.json`
- [ ] Verify state clickability after re-run
- [ ] Verify portal drill logic correctness (separate from data issue)
- [ ] Publish `org/standards/TO_COMPILER_GATE.md`
- [ ] Andrew: browser QA at opalinvest.dev for .038/.039/.041/.043/.046
- [ ] Andrew: JWT for smoke test
- [ ] Reassign .035/.036 to active DE instance

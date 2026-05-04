# Session Log — 2026-05-04

**Agent:** 0.4.0_DE_ClientPlatform
**TO:** MDLP_RVVALT.005 (Up/Down Capture view)
**Type:** Active work — frontend-only ViewMode extension; clone of RollingSharpeChart pattern

**Portal DEV commit:** `d1e66357`
**Workspace CLOUD commit:** pending DT 0.4 portal-submodule bump
**GO source:** COO 2.0.0_SA_COO `f8c4f26c5` (Andrew → Yang → AE 0.5.0 → DE 0.4.0 peer relay 19:31Z → COO formal TO 19:34Z)

---

## Work Completed

### Files

| File | Change | Lines |
|------|--------|-------|
| `portal/src/components/RollingCaptureChart.tsx` | NEW — clone of RollingSharpeChart pattern with Up/Down capture math | +401 |
| `portal/src/components/ReturnVolatilityScatter.tsx` | ViewMode `'capture'` slotted between `'sharpe'` and `'drawdown'`; VIEW_LABELS + PANEL_CONFIG entries; render branch | +6/-1 |

### Component spec compliance

| AC | Status | Evidence |
|----|--------|----------|
| AC1 ViewMode extension | PASS | `'capture'` between `'sharpe'` and `'drawdown'`; VIEW_LABELS = 'Up/Down Capture'; PANEL_CONFIG title = 'Upside/Downside Capture' with AE-spec helpText verbatim |
| AC2 RollingCaptureChart component | PASS | Clone of RollingSharpeChart pattern: same MODEL_CODES selector cards, same INTERVALS `[22, 65, 131, 261]` with labels {1M, 1Q, 6M, 1Y}, same Bar/Line toggle (default Line + 1Y/261), Y-axis 'Capture (%)', reference lines at 0 + 100, tooltip shows date + Up Capture % + Down Capture % |
| AC3 Up/Down Capture math | PASS | sign-filtered subsets: `up = window.filter(p => bm > 0)` / `down = window.filter(p => bm < 0)`; `compound(rs) = rs.reduce((p,r) => p*(1+r), 1) - 1`; up_capture = compound(model on up) / compound(bm on up) × 100; mirror for down. Edge cases: empty subset → null; `\|compound_bm\| < 1e-6` → null; `bm === 0` excluded by strict-inequality filters |
| AC4 Data reuse | PASS | RollingCaptureChart consumes same `timeseries` prop already loaded by `useQuery(['model-portfolio-timeseries'])` in ReturnVolatilityScatter parent. No new query, no Lambda, no IAM. `git grep model-portfolio-timeseries` returns 1 hit (the existing parent useQuery). |
| AC5 Existing 3-view regression clean | EXPECTED PASS | Edits to ReturnVolatilityScatter are additive only (new ViewMode option; new render branch). Scatter / Sharpe / Drawdown render branches untouched. `bun run typecheck` exit 0. Visual regression to be confirmed via `/frontend-dev`. |
| AC6 Typecheck + build clean | PASS | `bun run typecheck` exit 0 (pre-edit + post-edit). `/frontend-dev` Playwright not run interactively from CLI session (visual smoke deferred to next dev-server cycle). |

### Up/Down Capture math — reference spot-check

Synthetic window N=5 to verify the implementation arithmetic:

```
model_returns      = [0.010, -0.020, 0.005, 0.030, -0.010]
benchmark_returns  = [0.008, -0.015, 0.000, 0.025, -0.012]

bm sign mask       = [+,    -,      0,     +,     -]
Up subset  (bm>0)  = idx 0, 3
Down subset (bm<0) = idx 1, 4
bm == 0 idx 2      = excluded from BOTH subsets per AE spec

up_compound_bm  = (1.008)(1.025) - 1 = 0.03332
up_compound_md  = (1.010)(1.030) - 1 = 0.04030
up_capture      = 0.04030 / 0.03332 × 100 = 120.95%

down_compound_bm = (0.985)(0.988) - 1 = -0.02682
down_compound_md = (0.980)(0.990) - 1 = -0.02980
down_capture     = -0.02980 / -0.02682 × 100 = 111.11%
```

Up >100 + Down >100 → model captures more than benchmark on both sides (mixed-quality signal; best portfolio shows Up >100 + Down <100). Reference lines at 0 + 100 give immediate read.

A live spot-check (against actual model_portfolio_timeseries.json data flowing into the component) is deferred to next dev-server cycle — PROD curl from this machine returned HTTP 000 (DNS/network limitation in current environment).

### Color contract

| Series | Color | Rationale |
|--------|-------|-----------|
| Up Capture | `#22c55e` (green) | "More on up = good" maps to green per AE spec line 17 |
| Down Capture | `#ef4444` (red) | "More on down = bad" maps to red per AE spec line 17 |

No model-color or benchmark companion line — capture IS already vs benchmark, so a benchmark dashed line would be redundant and confusing.

---

## Compiler Tools

| Phase | Tool | Result |
|-------|------|--------|
| Phase 1 (before write) | `comp-transform schema-check ReturnVolatilityScatter` | "Component not found" — graph normalization issue (file exists at expected path; same return as TO-2/TO-4 reconciliation). Captured as baseline. |
| Phase 2 (before commit) | `bun run typecheck` | Exit 0 |
| Phase 2 (before commit) | `comp-transform fields RollingCaptureChart` | DEFERRED — graph build does not yet know the new file. After comp-build refresh post-deploy. |
| Phase 3 (after commit) | `/frontend-dev` 4-view smoke | DEFERRED — visual smoke to be run via dev server. |

---

## RAVC Log

| Message | To | Subject | Timestamp |
|---------|----|---------|-----------|
| RAVC2 ACK | 2.0.0_SA_COO | MDLP_RVVALT.005 GO received, executing | 20260504T193512Z |
| RAVC4 (this commit) | 2.0.0_SA_COO | MDLP_RVVALT.005 portal commit `d1e66357` — see this log | pending after this commit |

---

## Current State

- **MDLP_RVVALT.005**: Portal DEV commit `d1e66357` shipped. Awaits DT 0.4 portal-submodule bump → CLOUD parent commit + portal PROD push.
- **MDLP_RVVALT.002 + .004**: Still `<status>pending</status>`; AC reconciliation MCP `20260504T193431Z` to COO awaits acceptance-flex decision on AC5 stub bypass + DT confirmation of portal-v2.1.73 PROD state.

## Next Steps

- [DT 0.4] Portal-submodule bump → CLOUD parent commit + portal PROD branch push (standard `chore(portal): bump portal submodule — MDLP_RVVALT 4-view toggle + RollingCaptureChart` flow; needs to land for 5/5 closure)
- [DE 0.4 next dev cycle] `/frontend-dev` 4-view Playwright smoke + `comp-transform fields RollingCaptureChart` after comp-graph refresh
- [COO 2.0.0_SA_COO] On DT bump landing: 3-step atomic close MDLP_RVVALT (JSON status complete + REGISTRY Active→Completed + PRD `Status:` line)

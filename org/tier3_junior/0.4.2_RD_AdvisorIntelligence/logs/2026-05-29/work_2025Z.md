# RD~B /work cycle 2025Z — MDPF_SCOPED D1+D2 implementation, D3 blocked on DE

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, COORDINATE

## Tick outcome
Working under COO `[DRIVE GO]` (no formal TO filed yet; COO said "formal TO follows"). Substantive FE edits landed for D1+D2; D3 blocked on DE data-shape confirms.

## D1 — per-firm Daily AUA (root cause fixed, needs visual)
DE confirmed data correct end-to-end (published 19:38Z; empty-state = pre-publish timing). Residual FE break was canonical-key↔old-key mismatch: per-firm `by_model` emits canonical `display_name` but render loops keyed off old `MODEL_ORDER`. Fixed via canonical key unification (see D2).

## D2 — canonical naming (functionally complete pending visual)
- `lib/modelPortfolioColors.ts`: added `getCanonicalModelName()` — explicit, idempotent old/code→canonical resolver (passthrough for unknowns incl. ETF/benchmark proper names).
- `pages/ModelPortfolios.tsx`: `MODEL_ORDER` → 5 canonical titles; normalized BOTH transform branches (global `model_name` + per-firm `display_name`) + global `by_model` keys through `getCanonicalModelName`; canonicalized the 2 cross-lookups (distribution `Object.entries(...).find`, metrics `.find`). Legend/tooltip/donut labels now render canonical. `tsc -b --noEmit` exit 0.
- `pages/Positioning/tabs/HoldingsTab.tsx`: `PORTFOLIOS` display `name` fields → canonical (id-matched, display-only; the `'Long Term Conservative':'LTC'` data→code maps left intact).

### Cross-page scan — NO further genuine display defects
The "~34 components" framing resolves to mostly non-display hits:
- Internal codes UST/ST/INT/LTC/LTA — stable identifiers, keep.
- Code→display tables ALREADY canonical: RollingSharpe/MaxDrawdown/RollingCapture/PeersTab/benchmarks.ts (`LTC:'Long Term'`) — no defect.
- Data-match maps (must NOT change): FactorTilts `modelToAumName` (code→AUM-data-key), Positioning/Attribution `'Long Term Conservative':'LTC'` (source-name→code).
- Fixed-Income DURATION categories (Attribution etf-categories/holdings-shared/AllocationHeatmap `'Intermediate'` = Intermediate Duration) — not model titles.
- ETF/benchmark proper names + README docs — out of scope.

## D3 — Portfolio Analytics panel re-scope (BLOCKED on DE)
Confirmed panel widgets (`modelPortfolios`/`totalAUM`/`portfoliosWithNonModel`) are panel-only → can re-scope at definition. BUT two data-shape unknowns block correct implementation (guessing → new visible defect the visual gate would bounce):
1. Per-firm `by_model` has 7 entries (cohort_class model/sma/null) but donut shows 5 canonical models — need composition/collision mapping.
2. AUMGrowthMetrics (quarterly) + distribution bell-curve — per-firm artifact has daily `partner_custody_total` but no quarterly metric object or distribution slice. Growth derivable from daily series (proposed); distribution pending.
Two `[Q-D3]` MCPs sent to 0.4.0_DE_ClientPlatform (202152Z distribution, 202528Z by_model composition). Donut+center+legend (+derived growth) bind as soon as DE confirms.

## Blocker classification (/work Step 4)
D3 = peer-resource blocker on DE (data-shape confirm). NOT firing `[BLOCKED-ASK]` to COO — direct peer-ask is out + I have unblocked work (D1/D2 done this tick). Will surface to COO if DE silent >1 cycle.

## Compiler Tools
| Tool | Result |
|------|--------|
| `comp-transform schema-check ModelPortfolios` | WARN no co-located types.ts (inline interfaces); no MISSING/UNUSED |
| `tsc -b --noEmit` (portal typecheck) | exit 0 — D1+D2 ModelPortfolios edits compile clean |
| grep cross-page display-defect scan | confirmed defects concentrated in ModelPortfolios + Positioning; rest non-display |

## Next
On DE reply → D3 donut/center/legend (+derived growth) re-scope → /frontend-dev visual per view (Global/49F/Inflection) → commit full validated MDPF FE set + RAVC2 to COO w/ screenshots. Holding commit until visual gate (per COO non-negotiable); edits safe on disk.

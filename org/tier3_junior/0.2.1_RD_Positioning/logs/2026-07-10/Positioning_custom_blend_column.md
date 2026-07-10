# Positioning -- Custom Model-Blend Column (POSN_CUSTOM.001)

**archetype:** IMPLEMENT

**Agent:** 0.2.1_RD_Positioning
**Date:** 2026-07-10
**TO:** POSN_CUSTOM.001.custom-blend-state-summary-column (from 2.0.0_SA_COO~C, GO 2026-07-10T20:56Z)
**Status:** Build complete on portal DEV working tree; handed to 0.2.0_DE_PortfolioAnalytics for review + compiler mandate + commit. NOT self-closed.

## What was built

FE-only over already-served, sovereign-clean Yang Bloomberg model data (positioning_data.json -- NOT bd/49F/Schwab). Adds a 6th "Custom" column/bar to the Positioning Summary driven by advisor-entered weights, recomputed client-side as a weighted average of the 5 models.

1. **State lift -- `Positioning.tsx`.** `useState<CustomBlendState>` lifted to the page and threaded to `PositioningSummary` via `customBlend` + `onCustomBlendChange` props. Ephemeral (not persisted -- Andrew+Yang deferred). This is the shared state POSN_CUSTOM.002 (HoldingsTab CSM) will read.

2. **New shared module -- `shared/customBlend.ts`.** Owns the contract + pure helpers so both consumers (and .002) import one source of truth:
   - `CustomBlendState { active, inputMode, weights: Record<ModelId,number>, targetEquity }`, `MODEL_IDS`, defaults (even 20/20/20/20/20 = valid).
   - `sumWeights` / `isBlendValid` -- Sum=100 guardrail, epsilon 0.01, NO auto-normalize.
   - `blendSeries(valuesInModelOrder, weights)` -- weighted average; returns 'N/A' if any weighted (w>0) contributor is non-numeric (honest "undefined for this row" rather than a silently-understated blend).
   - `solveTargetEquityWeights(T, benchmarkEquityByModel)` -- Mode B: 2-lever ST<->INT interpolation against benchmark equity anchors, clamps to the reachable range and flags `outOfRange`. **Lever rule is the mid-build Yang confirm item; localized to this one function, non-gating.**

3. **`PositioningSummary.tsx`.**
   - `generateSections` gains a 6th value per row = `blendSeries(row.values, weights)` in the active view mode (or "--" when invalid). Applied uniformly via a `withCustom` wrap so both the data path and the no-data early-return path stay length-6.
   - `totalColumns` 6 -> 7; extracted the per-column bar markup into `renderBarInner` (5 model bars use it unchanged; the Custom bar reuses it) + `renderInvalidBar` ("--" placeholder when Sum!=100).
   - Dual-input control (`renderCustomBlendControl`): Mode toggle (Model Weights / Target Equity), live Sum indicator (green OK / red "must total 100"), Mode A 5 inputs, Mode B target-equity input + displayed implied weights + reachable-range note. Missing-weighted-model note (surfaced, never silently dropped).
   - "Custom" name-header accented (primary color).

4. **`shared/gridConfig.ts`.** `PORTFOLIO_GRID_TEMPLATE` repeat(5)->repeat(6); `PORTFOLIO_NAMES += 'Custom'`. `PORTFOLIO_ORDER` left at 5 (Custom is a blend, not a model). Grep confirmed both symbols are consumed ONLY inside PositioningSummary.tsx -- no other consumer breaks.

## Compiler Tools

| Tool + command | Phase | Result | Disposition |
|---|---|---|---|
| `comp-transform schema-check PositioningSummary` | 1 (before write) | "All rendered fields match their response types." | Clean -- blend consumes existing response types |
| `Grep PORTFOLIO_GRID_TEMPLATE\|PORTFOLIO_NAMES\|PORTFOLIO_ORDER\|totalColumns` (portal/src) | 1 | PORTFOLIO_NAMES + PORTFOLIO_GRID_TEMPLATE consumed ONLY in PositioningSummary.tsx; PORTFOLIO_ORDER unused; PerformanceHeatMap `totalColumns` is a local unrelated var | Safe to widen -- no external 5/6-col assumption breaks |
| `aws s3 cp .../positioning_data.json` + parse (gzip) | 1 | benchmark equity anchors present, all 5 models: UST=0 ST=15 INT=60 LTC=85 LTA=85 | Mode-B anchors confirmed in served data; ST<->INT reachable range = 15%-60% (the narrowness IS the Yang confirm item) |
| `bun run typecheck` (`tsc -b --noEmit`) | 2 (before commit) | exit 0, no output | PASS |
| `bun run lint` (`eslint .`) | 2 | exit 0 | PASS |
| `comp-cache collisions` | 2 | 104/104 useQuery captured (unchanged from PRD baseline); 0 TYPE MISMATCH; `['positioning-data']` shared Attribution<->Positioning is PRE-EXISTING | 0 new query key -- blend is client-side over already-fetched queries |
| `comp-transform schema-check Positioning` / `PositioningSummary` | 2 | Both: "All rendered fields match their response types." | Stayed clean |
| Pure-logic exercise (bun, adjacent temp file, removed after) | 2/3 | 17/17 assertions PASS against real anchors | AC2/AC3/AC4 math verified: AC3 30/70 ST/INT FI=46.67, EQ=53.33, sum 100; AC4 T=50 -> ST22/INT78 -> blended equity 50.1; T=15->100% ST; T=60->100% INT; T=80 outOfRange+clamped |

**Why these:** RD minimum is `comp-transform fields`; I ran the fuller PositioningSummary/Positioning schema-check + comp-cache per the TO's 3-phase mandate. `comp-blast`/`comp-routes` N/A -- no endpoint added, no deletion.

## Acceptance criteria status (RD self-check; DE verifies)

- **AC1** (Custom 6th column in bars+matrix, recomputes on view-mode toggle): built -- generateSections appends per active mode; custom bar via renderBarInner honors viewMode; name-header "Custom". Visual toggle = DE /frontend-dev smoke.
- **AC2** (Sum=100 enforced; <100/>100 -> warning+red+"--"; ==100 computes): built + logic-verified (isBlendValid). Guardrail gates both bar and matrix.
- **AC3** (hand-checked weight vector row = Sum w_i*model_i within rounding): logic-verified 17/17 against real anchors.
- **AC4** (Mode B target T -> weights whose blended benchmark equity = T +/- rounding): logic-verified (T=50 -> 50.1).
- **AC5** (typecheck+lint exit 0; /frontend-dev smoke green [DE runs]; AGG + 5 existing columns unchanged): typecheck+lint exit 0 done; 5 model bars refactored into a shared renderer with IDENTICAL markup (output byte-unchanged); AGG lives in HoldingsTab (untouched). Visual smoke = DE.

## Grounding / honesty notes

- **NOT visually exercised by me.** Phase-3 DEV visual smoke (Mode A entry, Sum!=100 red state, Mode B populate, view-mode toggle on the running app) is assigned to DE per AC5 (`/frontend-dev smoke green (DE runs it)`). I verified the pure blend/solve MATH by exercising the real functions against real served anchors (17/17), plus typecheck/lint/schema-check/comp-cache -- but I do NOT claim the rendered UI works; that is DE's smoke.
- **Mode-B lever rule is provisional (Yang confirm mid-build).** ST<->INT reaches only 15%-60% equity against current anchors; out-of-range targets clamp + surface a note. Contained to `solveTargetEquityWeights`; swap does not touch the rest of the column.
- **# of ETFs custom cell** shows a fractional weighted-average (per the uniform per-row weighted-avg contract). Faithful to the spec; flagged for DE/Yang if a distinct-ticker count is wanted later (that data lives in .002's holdings path).
- **Out-of-scope working-tree file:** `portal/src/pages/SecurityScanner/constants.ts` shows as modified in the DEV tree but is NOT mine (pre-existing). DE must stage ONLY the 4 Positioning files.

## Files changed (all under portal/src/pages/Positioning/)

- `Positioning.tsx` (state lift + prop threading)
- `panels/PositioningSummary.tsx` (custom column + bar + weights control + guardrails)
- `shared/gridConfig.ts` (dynamic 5/6-col template)
- `shared/customBlend.ts` (NEW -- contract + pure helpers)

## Revision -- Andrew smoke feedback (2026-07-10, post-handback, pre-DE-commit)

Andrew smoked the build and directed four changes; all applied on the DEV working tree (DE hasn't committed yet, so this IS what DE reviews):

1. **Null metric no longer blanks the blend.** UST has `beta=null` in served data (confirmed: UST beta=None; ST 0.89 / INT 0.95 / LTC 0.96 / LTA 0.97). Old `blendSeries` returned 'N/A' if ANY weighted contributor was non-numeric. NEW: it SKIPS null/N-A contributors and averages over the models that have a value (weights renormalized to the valid subset). Reduces exactly to the plain weighted average when all present. Verified: even-split blend of Beta = 0.9425 = mean(0.89,0.95,0.96,0.97); skewed-weight renormalization also correct; all-null still -> 'N/A'.

2. **Whole custom blend gated behind a new "Custom" View toggle.** Added a 4th option (Portfolio / Benchmark / Relative / **Custom**) to the existing View selector. The Custom column, bar, and control banner appear ONLY when Custom is selected; the other three views are byte-unchanged from the original panel (5 model columns, no control). Grid is now dynamic -- 5 data columns normally, 6 in Custom view (`portfolioGridTemplate(n)`). Custom view renders models + blend in PORTFOLIO (actual allocation) terms.

3. **Target-Equity (Mode B) deactivated.** Removed the mode toggle + all Mode-B UI/handlers from the panel (needs more spec before shipping, and it declutters). The control is now a single row of 5 model-weight inputs + the Sum=100 guardrail. `solveTargetEquityWeights` is retained in customBlend.ts, dormant, for when Mode B is specified. No dead imports (verified: 0 lingering Mode-B references).

4. **Padding** added between the Custom Blend banner and the stacked bars (`pt-6` on the bars wrapper in Custom view).

**Re-verification after the changes:** `bun run typecheck` exit 0; `bun run lint` exit 0; `comp-transform schema-check Positioning` + `PositioningSummary` both clean; pure-logic exercise 8/8 PASS (null-skip renormalization against REAL served Beta values, AC2 guardrail, AC3 hand-check, dormant Mode-B solve regression). Scope still the same 4 Positioning files. AGG (HoldingsTab) untouched.

## Revision 2 -- Andrew smoke feedback #2 (2026-07-10): gold + CSM holdings view (POSN_CUSTOM.002 pulled forward)

Andrew directed two more changes; the second is the HoldingsTab CSM view -- the CORE of POSN_CUSTOM.002, which he pulled into this session directly (sovereign). HoldingsTab.tsx is under my page dir (portal/src/pages/Positioning/), so in scope. Applied:

1. **Gold "Custom" text.** The Custom column header (summary) + the CSM toggle (HoldingsTab) now use `PALETTE.amber400` (the codebase's "warm gold"; no hardcoded hex). Replaced the earlier primary-color header.

2. **HoldingsTab CSM view (POSN_CUSTOM.002 core).** In Custom mode, a gold **CSM** toggle appears LEFT of AGG in "Portfolio Composition"; selecting it recompiles the custom portfolio in BOTH the treemap and the "Holdings Breakdown" table. Each security's weight is recalculated client-side: `csm_weight[ticker] = Sum_i (customWeight_i/100) * model_i_weight[ticker]` merged by ticker (characteristics/returns carried from the ticker's canonical values). New module-level `buildCustomCurrentHoldings()` (there is no served `current_holdings['CSM']`); wired into the treemap (`holdings`), the table (`attributionHoldings`), and `getHoldingPerformance`. CSM shown only when `customBlend.active` (set true by the summary's Custom view via `handleViewChange` -> shared state); invalid blend (Sum!=100) -> empty state, not a partial aggregate; render-phase reset to AGG when Custom mode turns off. `customBlend` threaded Positioning.tsx -> HoldingsTab.

**Grounding (CSM math, vs REAL served current_holdings):** each model's holdings sum to exactly 1.0, so an even-weighted CSM sums to 1.0000 across 29 tickers; per-ticker hand-checks match exactly (DIVZ 9.04%, IEFA 8.72%, ...); and CSM(even)=9.04% for DIVZ vs served AGG(AUM)=12.47% CONFIRMS the weights are genuinely recomputed (different weighting), not a copy of AGG.

**Re-verification:** `bun run typecheck` exit 0; `bun run lint` exit 0 (0 warnings -- reset moved from an effect to the render-phase adjust-state pattern); `comp-transform schema-check HoldingsTab` + `PositioningSummary` + `Positioning` clean (HoldingsTab `getAUMSummary()->AUMSummaryResponse` INFO is pre-existing, out of scope). Scope now 5 files (adds `tabs/HoldingsTab.tsx`). AGG served path byte-unchanged (CSM is an additive branch).

**Scope note:** this session now covers POSN_CUSTOM.001 AND the core of .002 (Andrew pulled .002's CSM view forward). NOT done in .002's full PRD scope: the model-weights column in the CSM table (AGG-style breakdown) -- Andrew's ask was weight recomputation; the extra column is flagged for the .002 DE pass. Mode B (Target Equity) remains deactivated pending spec.

## Commits (RD self-commit -- SSCN pattern, CTO~C arch-gate; no DE spawn)

Andrew smoked .001 himself (real user) = the visual validation; COO~C + CTO~C confirmed RD self-commit -> CTO~C arch-gate (no DE). Own author line throughout; NOT pushed; submodule pointer NOT bumped (DT flow).

- **portal (DEV) 573b41ad** -- POSN_CUSTOM.001 + .002 CSM core. Scope-verified (`git -C portal show --stat`): EXACTLY the 5 Positioning files, zero non-Positioning, zero SEV1 surface (no ModelPortfolios/MDLP/MDPF). COO~C independently re-ran show --stat to confirm.
- **parent (CLOUD) ea478b11d** -- deliverables (session log + page_inventory.xml). safe-commit [surface-check] OK.
- **portal (DEV) 662e56ec** -- Andrew-direct smoke follow-up: engaging the "Custom" View toggle AUTO-DEFAULTS the HoldingsTab (Portfolio Composition + Holdings Breakdown) to the CSM portfolio. Edge-detected (adjust-state-on-prop-change with a prior-value guard) so the advisor can still switch to AGG/a model while Custom mode stays on; disengage -> AGG. Single file (HoldingsTab.tsx); typecheck 0, lint 0. Arch-gate target = HEAD 662e56ec.

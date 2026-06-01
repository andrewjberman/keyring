# /work session log — 0.4.2_RD_AdvisorIntelligence~B — 2026-06-01

Long Andrew-direct FE session on the **Model Portfolios** portal page (DEV, Rule 19 held throughout). Started as the MDPF_SCOPED P1 RD-leg, then ran a cascade of Andrew-direct portal fixes culminating in a recharts v3 stacking deep-dive. All work typecheck + VALGATE green on origin/DEV; promote(s) staged for CTO/DT.

## Workstreams + commits (portal/DEV unless noted)

### 1. MDPF_SCOPED P1 — FE↔BE linkage matrix (RD leg)
- Inventoried all 8 Model Portfolios panels → joined to DE's BE columns by queryKey. Conclusion: **categorically linked across GLOBAL / 49 / INFLECTION**. Docs: `docs/briefs/mdpf-fe-be-linkage-matrix-{merged,fe-rows}-20260601.md` (CLOUD `a866d5ee1`).
- Flags F1–F5 surfaced; F1→(b) firm-invariant label shipped (`fba00261`) then **removed** Andrew-direct (`1b9e176c`); F2 hardcoded "49Financial" label fixed (`fba00261`); F5 per-firm extra-model trend dropout fixed (`103f623a`-adjacent). DEV-coherence: committed `getCanonicalModelName` provider (`decf6c9f`).

### 2. BMKAUD — Peers UST-1M "no 1M"
- Diagnosed FE falsy-zero guard: `PeersTab.tsx` gated render on `!percentiles.p95` (truthy); UST 1M p95 == 0.0 → suppressed present model:0.3017. Doc `8d3252f15`. Fix (Andrew/COO ruled all-percentiles-null gate): `c868bd41`. CVO-corroborated; data faithful (DS~B).

### 3. Index/ETF toggle — Opal-only (`f12abf95`)
- Restored the benchmark toggle gated on `internal` (isInternal firmId==='opal-capital' / isDev). External/partner sees ETF default, no toggle.

### 4. Canonical model naming
- Performance tab (Benchmark Comparison + Return vs Volatility): `getCanonicalModelName` at the benchmarkData boundary; scatter shared-benchmark check switched to `code` (`2eb4b450`).
- HoldingsTab PORTFOLIOS array canonical names (`3c2aa71b`, COO-verified adopt-in-domain).
- Blend label `50/50 INT/LTC` → `50/50 INT/LT` (LTC→LT canonical) (`d4c1b5cf`).

### 5. Cohort-1c SMA fold + Inflection blend colors
- Andrew "fold everywhere": per-firm displayed non-model = `non_model_aua + sma_aua`; SMA sleeves not separate; total preserved (numerically verified, DIFF~0) (`103f623a`). The ~$172M 5/18 step characterized as the backend Black-Diamond→Schwab provenance item (routed DS-CP), NOT the FE fold.
- Inflection 50/50 blend colors: INT/LT teal `#14b8a6`, ST/INT chartreuse `#a3e635` (`39555946` → `c9a187f3`).

### 6. TO-C — bell-curve unfunded footer (kill Inflection "6639")
- Footer = GLOBAL metrics − PER-FIRM distribution = cross-grain/cross-scope. Refined per COO/DE TO-A: show footer **only at Global scope**, suppress all per-firm (49 "201" also wrong) (`42ea95b8` → `9b2fed2c`).

### 7. Macro YYYY-MM (year-ago-bleed) co-fix with 0.5.0_AE
- MacroHeatmap read monthly values by bare month-name → current June grabbed year-ago June. AE added additive `values_ym` (YYYY-MM); FE migrated to read `values_ym` (`b0a5a55a` → corrected to `998ff784` — first pass wrongly read the bare `values` map). Data-verified; co-deploy with AE producer.

### 8. CTO briefing (Andrew visual review) — `4bb7a0ecc` (CLOUD)
- Global perfect; 49F + INF FE correct. 3 net-new items routed: (1) 49F full Schwab re-derive + interpolated daily 1c (DS-CP), (2) Inflection blend colors (RD — done), (3) 12/27/2025 per-firm anomaly (DS~B root-caused = spurious Saturday partition).

### 9. Cross-pod FE-slim review
- Reviewed + folded DE's `ETF_NAME_FALLBACKS` retire (`324f620b`) after de-conflicting HoldingsTab. Positioning name-casing arc closed.

### 10. **HEADLINE: AUA Trend stacked-order (50/50 blends) — recharts v3 registration-order**
The hard one. Goal: stack UST → ST → 50/50 ST/INT → INT → 50/50 INT/LT → LT → ULT → Non-Model (blends sandwiched, Non-Model top), in both the Period-End **bar** and Daily-AUA **area**.
- Donut + legend (explicit array) correct; stacked bar/area appended the blends at the end of the model group.
- Tried: sandwiched `trendModelOrder` (`d6679b9c`); area combinedData in trendModelOrder (`56e5a09e`); single ordered children array (`553945b6` — fixed Non-Model to top but not blends); **stable machine-key dataKeys** (`0664ed89`, GPT advisory 1 — NO effect, disproved the dataKey-string theory).
- **Root cause (GPT advisory 2, confirmed):** recharts v3 uses `stackOrderNone` (children order) but preserves the internal **graphical-item registration (mount) order**. The series list was DYNAMIC (`orderModelsWithBlends(Object.keys(by_model))` + conditional Non-Model), so the blends (data only from ~5/18) mounted LATER and registered after the base models → appended to the stack end. Explains why machine keys + hard refresh did nothing.
- **FIX (`caebae0d`) — WORKED (Andrew-confirmed):** render a FIXED full `STACK_SERIES` (all 8, machine key + label) from the FIRST paint, every render, both charts; NEVER conditionally mount — `hide={!show}` for inapplicable series (keeps them mounted → registration order pinned); materialize all 8 keys as numeric 0 per row; gradients unconditional; chart wrapper keyed by firm; `stackOffset="none"`. Machine keys (`0664ed89`) retained as good hygiene (valid SVG gradient ids).
- Advisory briefs ferried to GPT: `docs/briefs/recharts-v3-stacked-order-advisory-brief-20260601.md` + follow-up. Lesson: **dynamic/conditional mounting of recharts stacked series breaks stack order via registration sequence; render a fixed series set from first paint and use `hide`.**

## State / open (owned by others)
- Andrew confirmed the stacked-order fix works. Outstanding: re-enable trend `isAnimationActive` (off per GPT debug advice) once fully accepted.
- Backend: 49F full-history Schwab re-derive + interpolated 1c (DS-CP); 12/27 per-firm anomaly (DS~B/DE); `excluded_unfunded_count` read-direct cutover **held** until AE EC2 Docker redeploy + DE re-verify (keep Global-only footer stopgap meanwhile).
- Macro: ping AE post-PROD to drop the legacy bare-month `values` map. Visual smoke = Andrew/`/frontend-dev` on the promote (env headless-chrome blocked for agents).

## Discipline notes (for memory)
- Repeatedly slipped into launching the inbox-watcher with `&` (deaf form) under time pressure — corrected each time (kill + relaunch tracked via run_in_background). Watch this.
- Path-scoped commits on the shared portal worktree swept pre-existing peer WIP twice (ModelPortfolios + HoldingsTab); surfaced to COO, resolved as in-domain adopt. Non-destructive but attribution-mixed.
- recharts v3 stack order = registration/mount order, not JSX order — see headline above.

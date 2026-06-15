# RD~B — MDPF_SCOPED REOPEN: Orientation + 3-Defect Diagnosis

**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE, COORDINATE

Session 2026-05-29 ~2005Z. Reopened by Andrew empirical portal smoke (3 FE defects on Model Portfolios page). Data layer passed (DS~B 4-gate); portal FE broken. COO `[DRIVE GO]` authorizes start; this is orientation + dependency-sequencing, edits pending DE data-shape confirm + focused edit pass.

## Startup
- /watcher: was NOT REGISTERED + VERDICT NONE → re-registered (PID 21708), launched tracked watcher (task b8j5f1nfg). Cleared `.unread-deliveries` sentinel.
- Loop: armed `CronCreate /work 20m` (job 0eec1542). Portal verified on DEV (Rule 19).
- Acked COO; coordination MCP to 0.4.0_DE_ClientPlatform on perFirmMdpfData.

## Defect grounding (portal/src/pages/ModelPortfolios.tsx, 1534 lines)

### D1 — firm-scoped Daily AUA renders empty (49F + Inflection)
- Per-firm `timeSeriesData` transform ALREADY EXISTS (lines 333-354): builds `aggregate` from `perFirmMdpfData.partner_custody_total`, `by_model` keyed by canonical `modelData.display_name`, `isPerFirm:true`.
- `filteredByModel`/`filteredAggregate` (lines 952-961) derive directly from `timeSeriesData`. Daily AUA section (line 1215) gated on `Object.keys(filteredByModel).length > 0`.
- So empty-render ⇒ `perFirmMdpfData` returns null/empty (wrong S3 key or artifact-shape mismatch) — **DE's query-layer domain**. If query returns data, the existing transform + filter should populate. CONFIRMED FE path is wired; gap is upstream query OR a name-key mismatch (see root coupling below).

### D2 — canonical naming not resolved (data-key vs display distinction)
- Alias map exists: `portal/src/lib/modelPortfolioColors.ts` (lines 64-71). `getModelColor().name` returns canonical. No dedicated `getCanonicalModelName()` helper yet.
- **CRITICAL:** `MODEL_ORDER` (ModelPortfolios.tsx:62-68) holds OLD names AND is a DATA-MATCH KEY — `sortByModelOrder` does `order.indexOf(a.modelName)`; gradient/area loops (line 1255) map `MODEL_ORDER`. Global `modelPortfolios` keys on `metricsData.by_model[].model_name` (line 291). So renaming MODEL_ORDER blind could BREAK global matching if global data still emits old `model_name`.
- Many grep hits are SAFE (internal codes UST/ST/INT/LTC/LTA, or code→canonical tables already emitting 'Long Term'/'Ultra-Long Term' e.g. RollingSharpe/MaxDrawdown/RollingCapture/PeersTab/benchmarks.ts). Real defects = hardcoded OLD DISPLAY names: ModelPortfolios MODEL_ORDER (62-68), Positioning/tabs/HoldingsTab MODEL_DEFINITIONS name field (22,25,26), aum.ts display strings. ETF/benchmark proper names NOT touched.

### D3 — Portfolio Analytics panel always aggregate
- Panel (528+): donut uses `portfoliosWithNonModel` → `sortByModelOrder` (from global `modelPortfolios`) + `totalAUM` (global). Never reads `perFirmMdpfData`.
- Fix: when `selectedFirmId !== 'global'`, derive donut portfolios + total from `perFirmMdpfData.by_model` (canonical display_name) + per-firm distribution; aggregate only on Global.

## ROOT COUPLING (D1×D2×D3)
Per-firm data emits **canonical** display_names (line 346) but render loops (MODEL_ORDER gradients/areas line 1255, sortByModelOrder) match **OLD** names. So even with perFirmMdpfData returning data, area/gradient dataKeys keyed off MODEL_ORDER (old) won't match canonical by_model keys → silent non-render. The unifying fix is canonical-as-single-source for BOTH matching and display. This makes D2 partially prerequisite to D1/D3 firm-view rendering.

## OPEN QUESTION gating safe edits (→ DE/DS)
Does GLOBAL `metricsData.by_model[].model_name` now emit CANONICAL or OLD names?
- If canonical → MODEL_ORDER → canonical fixes global+firm consistently.
- If still old → MODEL_ORDER stays as data-key, display resolves via getModelColor().name / a new resolver; per-firm keys (canonical) need an alias bridge in the render loops.
Cannot safely edit MODEL_ORDER until this is confirmed — editing blind risks the empty-render regression class itself. Dispatched to DE.

## Sequence
1. DE confirms perFirmMdpfData query (returns firm data) + global model_name shape.
2. D2 canonical unification (MODEL_ORDER + render-loop key resolution + display-only sites in Positioning/Attribution/aum.ts).
3. D1 bind verify + D3 panel re-scope on selectedPartner.
4. CLOSE GATE: /frontend-dev VISUAL per view (Global + 49 Financial + Inflection) — firm AUA renders, canonical titles in UI, panel changes per partner. RAVC2 to COO w/ screenshots.

## Compiler Tools
| Tool | Result |
|------|--------|
| `comp-transform schema-check ModelPortfolios` | WARN types-resolution: no co-located types.ts (ModelPortfolios.tsx has inline interfaces) — non-blocking; no MISSING/UNUSED surfaced |
| grep canonical fix-list (portal/src) | ~20 files hit; majority internal-code or already-canonical tables; true display-name defects isolated to MODEL_ORDER + Positioning HoldingsTab + aum.ts |

Scope note: MDPF FE spans beyond default AdvisorIntelligence page-dir; proceeding under COO GO authority (flagged owned-paths-hook tension to COO).

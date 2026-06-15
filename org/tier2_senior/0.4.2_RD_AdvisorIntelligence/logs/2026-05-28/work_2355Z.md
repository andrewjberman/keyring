# 0.4.2_RD_AdvisorIntelligence~B — Session Log 2026-05-28

**Session window:** ~19:54Z – 23:55Z (context-continued from prior session)
**Lane COO:** 2.0.0_SA_COO
**Watcher chain:** b93g501p3 → b6mg1gcxy → bh3zap0di → bbc849p9b → bnpgfl7ht

---

## Work Completed This Session

### 1. ADVI_INFMVP.F5-RD — 3-view NNA canonical repoint (CLOSED)

**Status at session start:** Shipped in prior session; CVO RIGID gate in progress (windowing + Exec Summary fixes pending re-gate).

**Work this session:**

**F5-RD Rework #1 — Windowing unification (d8647ec3)**
- Root cause: `ContinuousNnaDivergingView` used `setDate(-1095)` (DistributionTab) vs `setFullYear(-3)` (AdvisorAnalytics) to derive 3Y cutoff from `latest_period_end=2026-06-30` (future Q2 end) → 1-day off-by-one → $2,770,848.58 gap.
- Fix: added `window_bounds: Record<string, {start,end}>` to `AdvisorNnaCanonicalResponse`. Both panels now filter `series` by `canonicalNna.window_bounds[W].{start,end}`.
- Also fixed: `SummaryCard` Exec Summary Flows repointed to canonical `advisors[advisorId].windows[W]` when `feeView==='all'` (was reading stale leaderboard.json as-of 05-28 vs canonical as-of 05-27 → $278,765.68 gap).

**F5-RD Rework #2 — Hero granularity-invariant (84df1272)**
- Root cause: `heroMetrics` summed `barData` bars — granularity-dependent (quarterly bars miss partial periods at window edge). 1Y start = May 27 but Q2'25 period_end = Jun 30, so May flows excluded at quarterly granularity. Result: quarterly hero $12,587,630.25 vs weekly $13,796,544.32 vs Lifetime headline $13,796,544.32.
- Fix: `ContinuousNnaDivergingView.heroMetrics` now reads `canonicalNna.{firm|advisors[drillParent]}.windows[canonicalKey]` directly when canonicalNna present + cohort==='adv' + no drillChild. Granularity-invariant by construction = same source as Lifetime headline.

**DS-CP artifact fix (no FE change needed):** DS-CP clamped in-progress Q2'26 `period_end` to `data_as_of` (2026-05-27). Window filter `period_end <= window_bounds.end` naturally includes it. Re-served at 23:07Z.

**CVO RIGID gate result (23:18Z):** PASSED. All 4 NNA surfaces (DistributionTab snapshot donut, continuous chart, AdvisorAnalytics Lifetime Activity, AdvisorPublicProfile Exec Summary Flows) read `windows[W]` from `advisor_nna_canonical.json` — cross-view equality by construction for Peter + control, every window × every granularity.

**Commits:** portal/DEV `d8647ec3` (windowing+ExecSummary) → `84df1272` (hero fix); outer CLOUD `7fe7f4e5f`.
**Gate rounds:** 3.

---

### 2. MDPF_SCOPED.S1 — Per-firm TypeError crash fix (935db0c1)

**User-reported:** `TypeError: Cannot read properties of undefined (reading 'opal_aggregate_aua')` on switching dropdown to 49 Financial or Inflection.

**Root cause:** `slice_per_firm()` spreads partner fields at the top level (`model_aua`, `partner_custody_total`, `by_model`) — no nested `aggregate` or `partners` keys. `ModelPortfolios.tsx` destructured `{ aggregate, partners }` from the global `MdpfAggregateAUATimeSeries` type → crash on `undefined.opal_aggregate_aua`.

**Fix (3 files):**
- `portal-proxy.ts`: added `MdpfPerFirmTimeSeries` interface matching the actual flat slice shape
- Updated `getMdpfAggregateAUATimeSeriesByFirm` return type to `MdpfPerFirmTimeSeries`
- `aum.ts`: re-exported `MdpfPerFirmTimeSeries`
- `ModelPortfolios.tsx`: updated query type annotation + `timeSeriesData` useMemo to read `partner_custody_total` and `firmByModel` directly

**Commits:** portal/DEV `935db0c1`, outer CLOUD `96d65e0d6`.

---

### 3. MDPF_SCOPED S1 — F2 double-count fix (aa8c9de4)

**Andrew-reported (via COO):** Inflection trend chart showed ~$311M vs correct ~$204M.

**Root cause:** Per-firm chart stacked global `non-model-assets.json` Non-Model band ($107.77M = 49F's non-model, wrong firm) on top of Inflection's model bands ($204M = `partner_custody_total` pre-S2-backfill, since `non_model_aua` = 0 pre-backfill). $204M + $107.77M = $311.77M phantom.

**Fix:** Added `isPerFirm: true` to `timeSeriesData` per-firm return. Gated all 4 global Non-Model insertion/render points on `!timeSeriesData.isPerFirm`:
- BarChart "Period End Summary" chartData Non-Model addition
- BarChart `<Bar dataKey="Non-Model">`
- AreaChart "Daily AUA Analysis" combinedData Non-Model addition
- AreaChart `<Area dataKey="Non-Model">`

Per-firm Non-Model band (from artifact's `non_model_aua`) wired as a follow-on when DS~B re-emits post-S2-backfill. Global mode unchanged.

**Commits:** portal/DEV `aa8c9de4`, outer CLOUD `e4309293a`.

---

### 4. ADVI_INFDEMO.002 — Closeout (b5487690, prior session; TO proxy-committed this session)

F6 (TaxCostBasisPanel Unrealized=blue/Realized=orange, titles outside card), F8 (Advisor Split default 100%), F9 (Advisor Revenue Estimated tracks Window toggle) — all shipped in prior session at `b5487690`. TO was stale-dispatched. RAVC2'd to COO; COO proxy-committed TO to complete this session.

---

## Commits Summary

| Commit | Where | What |
|--------|-------|------|
| `d8647ec3` | portal/DEV | F5-RD windowing unification + ExecSummary repoint |
| `84df1272` | portal/DEV | F5-RD hero reads windows[W] directly (granularity-invariant) |
| `935db0c1` | portal/DEV | MDPF S1 per-firm TypeError fix (MdpfPerFirmTimeSeries) |
| `aa8c9de4` | portal/DEV | MDPF F2 per-firm double-count fix (isPerFirm guard) |
| `7fe7f4e5f` | CLOUD | Outer pointer (subsumes d8647ec3 + 84df1272) |
| `e4309293a` | CLOUD | Outer pointer for aa8c9de4 |

---

## TO Queue at Session End

| TO | Status | Notes |
|----|--------|-------|
| ADVI_INFMVP.F5-RD | complete | CVO RIGID gate PASSED 23:18Z |
| ADVI_INFDEMO.001 | in_progress | Code-complete (f61cb40b/4bdb844e); gating on browser visual-confirm |
| ADVI_INFDEMO.002 | complete | COO proxy-committed |
| MDPF_SCOPED.S1 | complete | COO proxy-committed (Phase-2b gated on DS~B per-firm snapshot emit) |
| MDPF_SCOPED.S4 | complete | — |

## Deferred / Follow-on

- **MDPF per-firm Non-Model band:** wire `non_model_aua` from per-firm artifact as Non-Model band when DS~B re-emits post-S2-backfill (~03:30-04:20Z per MSTR wind-down plan)
- **MDPF F5 (canonical model names):** by_model display_names in per-firm artifact don't match MODEL_ORDER — DS~B emit-side fix
- **MDPF Phase-2b (whole-page per-firm):** gated on DS~B per-firm snapshot artifact (`platinum/mdpf/{firm_id}/snapshot.json`)
- **INFDEMO.001 visual-confirm:** Andrew or CVO to confirm browser render for Peter Lee Book Overview lookback

— 0.4.2_RD_AdvisorIntelligence~B

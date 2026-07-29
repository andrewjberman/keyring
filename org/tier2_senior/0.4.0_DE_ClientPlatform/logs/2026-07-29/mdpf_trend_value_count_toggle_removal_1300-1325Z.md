# MDPF trend: Value/Count toggle removal (ANDREW-DIRECT) — 1300–1325Z

**archetype:** IMPLEMENT

## What

ANDREW-DIRECT (~0845Z, relayed COO 124351Z verbatim: *"let's just have DE instantiated so they can
take out the value/count toggle in 'Account Trend Analysis'"*): remove the `Account: [Value] [Count]`
toggle from the AUA Trend Analysis panel — WITH its state and dead branches, not just the buttons.

**Shipped: portal DEV `72f132c5`** (1 file, `src/pages/ModelPortfolios.tsx`, +56/−265), pushed
`70166741..72f132c5` after reporting to COO (132333Z message, before push per process). DT promotes.

Removed: `trendMetricType` state + buttons + analytics events; every count branch both charts
switched on (metric-aware lastReal, per-model `account_count` reads, count YAxis/tooltip formatting,
W-7 `count_total` anchors, "Total Holdings" label, W-4 tooltip basis note); count-only selectors
(`trendCountBasisDates`, `trendCountClassByPeriod`, the W-4 count-basis ReferenceArea band + slate
overlay idiom, count-mode amber footnote); count wiring at the series source (`readCountTotalSeries`
reads, `count_total`/`count_class` row fields both branches, `account_count` off the page-local
`TimeSeriesDataPoint` + blend fold, `interpolatedRunsOverRows` dateSet param, 3 imports).

Value view renders unconditionally (was default). Title static "AUA Trend Analysis". View: Monthly
untouched. Donut/counts tiles/account-distribution untouched — verified separate data path
(aum-metrics/distribution artifacts, not the trend series).

**Boundary call, flagged to COO not untangled** (per the stop-rule in the dispatch):
`readCountTotalSeries` + `COUNT_CLASS_LABEL` in `pairedProvenanceRead.ts` are now consumer-less
exports. Lib left INTACT on the carried-point precedent (readGlobalCarriedDates same state);
`VALUE_BEARING_NON_MEASURED` still consumed internally (value band). Disposition = COO's.

## Verify

- `tsc -b` clean; eslint 0 errors / 4 warnings — **baselined against HEAD** (git show → temp copy →
  eslint): byte-identical warning set, all 4 pre-existing. provenance-read-guard OK.
- comp-surface-check `rc=2 BLOCKED` SEV1 (model_portfolios.headline/benchmark) — acked with audited
  `SURFACE_ACK` citing the ANDREW-DIRECT; the deliberate-change path, not a bypass of an unknown.
- Headless render `/portfolios` (global, fixture-fed MDPF global slice; local S3 CORS blocks the real
  fetch) — READ the PNG: header toggle-free, both charts value view, legends/bands correct, no
  light-on-silver. `scratchpad/mp_no_toggle2.png` (session b2f1fa22).
- Only my file dirty in portal at commit time (checked; the surface-check's aum.ts lines are its
  watched-surface enumeration, not my diff).

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-grep (x4) | OK | localized toggle to ModelPortfolios.tsx; proved all 41 `trendMetricType` refs + count helpers file-local; found `VALUE_BEARING_NON_MEASURED` internal lib consumer (kept lib) |
| comp-surface-check check | rc=2 BLOCKED SEV1 | correct verdict on a deliberate MP-surface change; SURFACE_ACK audited with ANDREW-DIRECT citation |
| comp-transform schema-check ModelPortfolios | WARN types-resolution | no co-located types.ts for the page (pre-existing tool gap for this page shape); type safety covered by tsc -b clean |

Gap noted: schema-check can't resolve ModelPortfolios' inline interfaces (no types.ts nearby) — its
MISSING/present verdict is unavailable for this page; tsc is the effective control here.

## Other

- Startup audit-archive-invoker rc=1: INTEGRITY/NON-APPEND-EDIT on `org/git-author-override-audit.log`
  (divergence line 1; baseline 1,696,149B vs live 7,928B — reads as truncation/rotation) + stale
  baseline 24h. Tool recorded to FINDINGS.md; routed to COO in the 132333Z report.
- `git stash` (single-pathspec, for the lint baseline) correctly BLOCKED by the shared-worktree gate;
  used `git show HEAD:path → temp copy` instead. The gate taught the right pattern.

## Next

1. [0.2.0_DT_PortfolioAnalytics] promote `72f132c5` (COO routes).
2. [2.0.0_SA_COO] disposition on the two consumer-less pairedProvenanceRead exports; screenshot review.
3. [0.4.0_DE_ClientPlatform] standing: fix-lane hot through the promote; event-driven on inbox.

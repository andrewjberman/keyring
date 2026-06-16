# MOLECULE: globalDeepTailNonModelByPeriod — Global SI deep-tail Non-Model band refine (YANG_SITTW.TO-1)  (scale: MICRO)
**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE
**by:** 0.4.0_DE_ClientPlatform · **2026-06-16 ~2200Z** · unit shipped at portal DEV fbfdbe9d (on DEV HEAD f3ceea7c)

## Unit + expected role
The `globalDeepTailNonModelByPeriod` useMemo in `portal/src/pages/ModelPortfolios.tsx` + its consumption in the
BarChart/AreaChart Non-Model band logic. Expected role: re-source the Global since-inception chart's Non-Model
band, ONLY in the pre-2026-01-16 estimate tail, as `opal_aggregate_aua[i] - model_aua[i]` (from globalMdpfData)
so the stacked deep tail reconciles to the model bars' opal_aggregate_aua basis (kills the mixed-basis overshoot
vs the non_model_assets enterprise_total source). Calibrated region (>=2026-01-16) + per-firm + count mode untouched.

## 1. Composition — what it actually is (vs declared)
Deployed (origin/DEV): `const globalDeepTailNonModelByPeriod = useMemo(() => { if (effectiveFirmId !== 'global'
|| !globalMdpfData?.dates) return null; ... forEach d,i: if (d >= MDPF_ESTIMATE_BASIS_END) return; oaa =
globalMdpfData.opal_aggregate_aua?.[i]; m = globalMdpfData.model_aua?.[i]; if (oaa!=null && m!=null) map[d]=oaa-m
}, [effectiveFirmId, globalMdpfData])`. MDPF_ESTIMATE_BASIS_END='2026-01-16' (L68). Matches intent exactly.
**Knowledge-parity NOTE:** a pre-existing comment (L607-608) already DECLARED the design intent "model bars +
Non-Model band total to opal_aggregate_aua" — but the deep tail did NOT deliver it pre-refine (it used
non_model_assets/enterprise_total). The refine makes the deep tail actually satisfy the long-stated intent.

## 2. State — live snapshot
N/A for served-artifact state: the unit is a pure FE-derived map (runtime-only, no S3 write). Its INPUT state
(globalMdpfData = json/mdpf/global/aggregate-aua-timeseries.json) was read fresh this session: LastModified
2026-06-16 19:14:37Z (TO-4 regen), 413 dates 2024-11-01..2026-06-12, opal_aggregate_aua + model_aua present.

## 3. Position in the chain
- **Upstream:** globalMdpfData <- getMdpfAggregateAUATimeSeriesByFirm('global') <- aggregate-aua-timeseries.json
  (DS build_aggregate_aua_timeseries.py). Reads opal_aggregate_aua + model_aua (top-level global-slice fields).
- **Downstream:** consumed in BOTH the BarChart band logic (`aggregateItem.period`) + the AreaChart band logic
  (`period`) — sets dataPoint[nmKey] for Global value-mode deep-tail dates; the Non-Model stacked segment.
- **Deps/reach:** MDPF_ESTIMATE_BASIS_END const; effectiveFirmId/globalMdpfData. Reach is tightly bounded:
  Global only, value mode only, deep-tail dates only. Per-firm (perFirmNonModelByPeriod), calibrated region
  (non_model_assets), and count mode are all on other branches — untouched.
- **Seams (for /seams):** globalMdpfData->memo (data->derivation); memo->chart band (derivation->render). Both
  covered by the session /seams (SOUND) + this molecule.

## 4. Behavior — what the deployed path actually does (probed, not inferred)
Branch behavior (deployed): Global value-mode deep-tail date -> band = oaa-model_aua (memo hit). Calibrated date
-> memo lookup undefined -> falls to non_model_assets branch. Per-firm -> memo returns null -> isPerFirm branch.
Count mode -> value-gated branches skip -> band 0. Null oaa/model -> memo omits the date -> graceful fallback to
non_model_assets. EVIDENCED via full-range recompute against served agg.json (309 deep-tail dates).

## 5. Semantic quality — sharp probes (all 309 deep-tail dates, not sampled)
- **PROBE1 precondition** sum(by_model !=sma)==model_aua: max|resid| **$0.01** (penny rounding), 0 model nulls.
  -> the chart's model bars DO equal model_aua, so the reconciliation holds.
- **PROBE2 nulls:** 0 null opal_aggregate_aua, 0 null model_aua in the deep tail -> all 309 dates populated, no gaps.
- **PROBE3 reconciliation:** refined stack (bars + oaa-model_aua) == opal_aggregate_aua, max|gap| **$0.01** across
  ALL 309 deep-tail dates. Exact (not aggregate-identity-masking: this is by-construction band=total-bars, AND
  the precondition bars==model_aua is independently verified, so it's a true reconcile not a residual sink).
- **PROBE4 boundary continuity:** refined(oaa-model) == non_model_assets to delta 0.000 from ~2026-01-12 on, so
  the deep-tail->calibrated switch at 2026-01-16 is seamless (no jump). The boundary sits INSIDE the region where
  both bases already converged (gap closed ~2026-01-14) -> the cutover is a no-op at the seam.
- **META-CHECK:** band magnitude sane (422M non-model on 776M total @ floor = 54%, vs old overshoot 444M); sign
  positive; naming consistent (it IS the non-model remainder). SMA double-count avoided (uses model_aua, SMA-excluded).

## Smell findings
| Smell | Rating | Evidence | Why it caught my eye |
|---|---|---|---|
| Refine enforces a previously-undelivered stated design intent | NOTE | comment L607-608 "...total to opal_aggregate_aua" vs pre-refine deep-tail using non_model_assets | the map said reconcile; the deep tail didn't; now it does — parity restored |
| Silent fallback if producer ever drops opal_aggregate_aua from the global slice | WATCH | memo uses `globalMdpfData.opal_aggregate_aua?.[i]`; if absent -> map empty -> null -> falls back to non_model_assets (the OLD overshoot) with NO error | graceful (no crash) but the overshoot would silently return; a consumer-contract note (like DS's sma-doublecount note) would guard it |
| Deep-tail band is day-to-day noisy (272->288->254M mid-Jan) | NOTE | PROBE4 values; both bases agree so it's real data, not a refine artifact | inherent to the estimate-era data (already demarcated as not-calibrated); not a defect |

## Assessment
SOUND. The unit does exactly what intended: exact full-range reconciliation of the Global deep-tail stack to
opal_aggregate_aua (max gap $0.01 across all 309 deep-tail dates), no null gaps, seamless boundary cutover, and it
finally delivers the long-stated "bars + band == opal_aggregate_aua" design intent in the deep tail. Tightly
scoped (Global/value/deep-tail only; per-firm + calibrated + count untouched). One WATCH (silent fallback to the
old overshoot if a future producer change drops opal_aggregate_aua from the global slice) — non-blocking; route =
a consumer-contract note. No DIG. Browser render remains the only unexercised leg (deferred to promote smoke).

## Knowledge-parity delta + residual
- Parity restored: the deep tail now satisfies the L607-608 design-intent comment (was aspirational, now true).
- WATCH routed: opal_aggregate_aua global-slice dependency -> suggest a data_contract consumer note (to DS, non-blocking).
- Residual: browser render not exercised (CLI demo-tenant auth); the numeric reconciliation is fully verified.

## Compiler Tools
| Run | Result |
|---|---|
| git show origin/DEV:ModelPortfolios.tsx (deployed composition) | memo + branches byte-confirmed on DEV HEAD |
| python full-range probe over served agg.json + nma.json (309 deep-tail dates) | PROBE1/3 max $0.01; PROBE2 0 nulls; PROBE4 seamless boundary |

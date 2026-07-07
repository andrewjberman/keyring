# CVO Exercise-Gate — DI-1 D-stage RE-VERIFY: PASS (capital_gains_ttm native-native, cliff gone) — CLOSED

**Date:** 2026-07-07T01:45Z
**Agent:** 3.0.0_SA_CVO
**Gate (CTO-defined):** served capital_gains_ttm = native-minus-native (no phantom endpoint); account_performance series single-basis (no cliff); honest-null only at true edges. On the served artifact.
**Fix:** CTO-blessed full-rebuild (0.6.1 --single INF_C_03 --rebuild -> gold-d), DS~B-served 01:39:55Z. Independently verified (not the self-report).
**Verdict:** PASS -> DI-1 D-stage CLOSED; the DI-1 tax-lineage class fully closed (point-in-time + history).

## Gate results (independent)
0. FRESH (head-object UTC): clients_tab 01:39:55Z, account_performance.parquet 01:36:07Z -- the rebuild landed.
1. SERVED capital_gains_ttm = unrealized_gain_change_ttm = **$4,450,438** (was $101,377,008 mixed-basis). Native-native, magnitude-plausible on the $13.3M book. NO phantom endpoint.
2. CLIFF GONE (account_performance firm unrealized_gain by date):
   2025-07-03 $8.97M | 2026-06-30 $13.21M | **2026-07-02 $13.22M** (WAS $174M phantom) | 07-03 $13.29M | 07-06 $13.29M.
   Max single-day |jump| since 2025-06 = $13.76M (2026-05-30) -- NOT the $160M+ phantom cliff. Single-basis native throughout (2,485 dates).
3. HONEST-NULL at true edges: the current TTM start endpoint (2025-07-03) is within native coverage (tax_unrealized 2020+), so no mixed-compute; pre-2020 honest-null guard deferred-durable (CTO-agreed, not hit by the current figure). HONEST-LIMIT: I did not exercise the honest-null path (the current figure doesn't reach a coverage edge) -- consistent with DS~B + CTO.

## Verification method note (discipline)
My crude per-account nearest-date recompute returned $80.5K (!= served $4.45M) -- but that is MY method's flaw (unconstrained abs-nearest mis-assigns sparse-history accounts to recent dates; the same crude logic gave -$76M pre-fix vs the served $101.4M). I did NOT false-flag on a broken independent method. The RELIABLE independent check is the firm-by-date ENDPOINT reconstruction (exact groupby sums, no nearest ambiguity):
  firm_unrealized(2026-07-06) $13,285,579  -  firm_unrealized(2025-07-03) $8,969,075  =  $4,316,504
  + new-account contributions (present-today/absent-365d-ago -> full unrealized into the delta) ~ +$134K  =  ~$4.45M == served.
Matches served to ~3% (the new-account effect) -> CONFIRMS native-minus-native + magnitude.

## D_02 per-advisor/hh/client analogs
Read the SAME rebuilt single-basis account_performance -> correct-by-construction on this D-stage run (the mixed-basis cliff is a property of the SERIES, now single-basis for all grains). Firm value endpoint-confirmed + series single-basis => the per-grain analogs are native-native by construction. (Optional per-grain spot-check not required for the gate.)

## Verdict
DI-1 D-stage exercise-gate = PASS. capital_gains_ttm native-minus-native ($4.45M, endpoint-confirmed), series single-basis (cliff gone), honest-null-at-true-edges (deferred, not hit). DI-1 D-stage CLOSED. DI-1-PIT (client_tax_liability + account_performance point-in-time, prior-certified) + DI-1-Dstage-TTM (this) + Finding-1 (retired B_03 from the tax timeseries per CTO ruling) = the full DI-1 tax-lineage class, closed. The eventual CTO+COO never-widen note (if any) is on the served-output rule; no widening here (the fix NARROWS $101.4M -> $4.45M toward truth).

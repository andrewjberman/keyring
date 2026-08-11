# VALIDATION VERDICT -- 49F timeseries_chart TWINS @4faf0dd4e2 (2 keys, P1-SCRIPTS)

**Validator:** 3.0.0_SA_CVO · **2026-08-11 ~2110Z** · **archetype:** VALIDATE
**Subject:** PROOF_OF_SPEC_49F_OVERLAY_TIMESERIES_CHART_TWINS @4faf0dd4e2. Emitter d12 @35702274cd.
Built by 0.4.0_DS_ClientPlatform~A. Covers TWO served keys: firm_timeseries_chart + gold_timeseries_chart.

## VERDICT: 2x SCOPE-VALIDATED (both keys). A no-pin family; grading one grades both, by measured identity.

## THE LOAD-BEARING CHECK: are the twins REALLY identical, and is no-pin justified?
- **Byte-identical, INDEPENDENTLY VERIFIED:** I hashed both payloads myself -- platinum == gold ==
  3715c6d64dca. So the two keys are the SAME content today, and the TWINS-DIFFED rule (platinum truncates
  the 4 nna_* daily series to trailing 1,091 days) is VACUOUS at 761 < 1,091 days of history -- it
  self-arms by construction when history grows. So grading one IS grading both; no divergence to miss today.
- **No-pin justified (V27, daily index-misalignment):** same shape as timeseries_overview -- fit certifies
  SHAPE only, said in the instance per the standing convention. Sound.
- **Discrimination via DERIVATION-CROSSING controls:** per-trading-date cumulative CROSS-TIE (data-sums vs
  manifest sums, TWO derivations) 525/525 cent-exact, REFUSES; per-day ADDITIVE SUM IDENTITY 761/761;
  guard + cell-naming mutants. The strong kind (independent legs), correct for a no-pin family.
- **Cross-family tie #4 VERIFIED against my held value:** 285,114,023.14 present in the payload -- the same
  figure I confirmed on the d07 grade (windows.MAX.summary.total_nna). Matched, not trusted.

## DISCLOSED FINDING I CREDIT
The census path itself was a routed finding: BOTH contracts were schema-ABSENT ('oversize -- listed' -- the
d00 sampler cap hid exactly the two LARGEST artifacts through FIVE vintages). base froze them from live
bytes @76d225de9b. A coverage gap that would have read as "no contract" caught by grounding the census
against live bytes -- the a-predicate-not-a-roster discipline again.

## SCOPE -- P1-SCRIPTS, NOT a served-surface kill-clear
Leaf value-parity is inexpressible pre-cutover (daily index-misalignment, V27); fit certifies SHAPE + the
derivation-crossing controls. cutover re-pin deferred. geo_city_drill (first doubly-nested keys-as-data,
state->city) handled with open-key depth, no frame change. Clean.

-- 3.0.0_SA_CVO

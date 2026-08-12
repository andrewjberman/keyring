# CVO VALIDATION -- COT (Cottonwood) P1 proof-of-spec set (A/B/C/writer) + the amended-C corrections

**3.0.0_SA_CVO 2026-08-11 ~1755Z · VALIDATE.** Instances: PROOF_OF_SPEC_P1_COT_{A,B,C,PARQUET-WRITER-FORMAT}
_20260811.json. All four proof-of-spec-check VALID (13/13/14/4 rows, 0 violations, coverage-checked).

## THIRD FIRM INSTANTIATED -- and the corrections are the HONEST class
COT is the third firm on the archetype (after 49F built + INF built). All four P1 groups VALID. The
amended-C instance (CTO-flagged) carries TWO found-and-fixed corrections IN THE RECORD, both the
population-catches-what-a-fixture-cannot class -- the exact class the 49F build's shadowed-pin and
zero-BMV finds established:
- **MM/DD/YYYY date fix (declared @c00):** the vendor ships Trade Date as MM/DD/YYYY strings; the
  ledger's bare `.str[:10]` kept the US form, so every ISO-string window/equality comparison
  downstream matched NOTHING -- the QA-window TWR ran FLOW-BLIND (cf_external=0 on all account-days).
  FOUND by the d07 fleet overlay's income row reading 0.0 against a series carrying real income.
  Fixed; the refusal counts (1774/76) were date-independent and STAND; post-fix the window is
  flow-aware and the gross-net identity found a live fee specimen. **A fixture cannot see a
  date-format mismatch; the POPULATION caught it** -- correction in-record, not papered.
- **Zero-BMV NaN leak (declared):** the zero-BMV refusal initially returned None INTO a
  COMPUTED-stamped row on 2 true-zero accounts; the fixture proved the function, the population
  exposed the status path. Post-fix the UNCOMPUTABLE census discriminates all three zero classes
  (true-zero / all-null-absence / zero-BMV). Correct behavior; honest.

## TRANSPOSABILITY -- the third-firm measurement (attacks "reproduces to the digit")
COT's own tally, both frames per CTO ruling: **rows-verbatim ~84% (c02 ~95% / c03 ~90% / c01 ~85% /
c00 ~70%) BESIDE judgment-calls-diverged 29% (4 of 14 rows on a COT-specific call).** The GIPS engine
+ lineage transpose nearly unchanged (as the COT spec predicted "TRANSPOSES UNCHANGED"); the FLOW
LEDGER (c00) diverges most (~70%), which is correct -- the vendor-specific flow classification is
exactly where firms differ. **This is consistent with the ~50%-adapt-at-Group-A signal from the DS
P1 analysis: a REAL SKELETON with a measured, named-mechanic divergence, not a clone.** Three firms
now measured; the archetype holds with a firm-specific flow-ledger tail every time.

## ONE FINDING NEEDS A RULING EYE -- ROUTED, NOT MINE TO CLOSE
**COT journals are ONE-SIDED BY MEASUREMENT:** all 1,914 Journal rows are unpaired (no opposite-sign
counterpart in the entire series) and none carry the vendor External-Flow mark -- so ALL land
EXTERNAL-BY-DEFAULT and the F-4 segregated NNA line is LARGE: **$121.2M beside a $404.9M headline
(23% of external dollars).** This is correctly SEGREGATED (the F-4 discipline held -- NNA didn't
inherit the bias), but whether the one-sided journals are genuinely-external vs an unpaired-intra-book
artifact is a **RECON-5a ruling question (CRO~A / the flow-classification owner), NOT a parity
verdict.** The instance declared it as a surprise for the ruling eye -- exactly right. Routing.
(Two corroborating strengths noted: BD's vendor External-Flow enum agrees 100% with the type-rules
on 14,208 authored-external rows; and in-kind dominates COT external flow 61.9% vendor-valued in-row,
so the in-kind valuation leg the 49F spec worried over is FREE at COT.)

## VERDICT
COT P1 set: all four VALID, coverage-checked, corrections honestly in-record. Third-firm
transposability measured (~84% verbatim / named-divergence tail). The one-sided-journal $121.2M NNA
is a RECON-5a flow-classification ruling item, routed to CRO~A -- not a parity failure, a declared
question. COT's fleet is build-graded; its parity-overlay clearance rides the same bar as 49F when
its emitters reach the value overlays.

-- 3.0.0_SA_CVO

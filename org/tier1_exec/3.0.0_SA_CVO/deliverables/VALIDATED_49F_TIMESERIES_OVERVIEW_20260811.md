# VALIDATION VERDICT -- 49F timeseries_overview overlay instance @45672c14ec (P1-SCRIPTS)

**Validator:** 3.0.0_SA_CVO · **2026-08-11 ~2005Z** · **archetype:** VALIDATE
**Subject:** PROOF_OF_SPEC_49F_OVERLAY_TIMESERIES_OVERVIEW @45672c14ec. Emitter d09 + V22-TSO-PRECUTOVER
@b8f9e0228f. Built by 0.4.0_DS_ClientPlatform~A.

## VERDICT: VALIDATED (P1-SCRIPTS). A legitimately no-pin family, handled honestly.

## THE LOAD-BEARING JUDGMENT: is "no leaf pins" justified, and does the alternative discriminate?
YES on both:
- **No-pin justified (index-misalignment, sound):** served history runs from 2020 (27/80/7 rows per
  freq); the canonical series starts at the D9 floor 2024-07-08 (9/26/3). fit_harness zips arrays BY
  INDEX, so row[0] pairs canonical 2024-Q3 against served 2020-Q1 -- EVERY per-row comparison pairs
  DIFFERENT periods. A leaf pin would pin NOISE. So the fit PASS certifies SHAPE only, stated in the
  instance (the d08 honesty precedent). Correct -- pinning mismatched-length index-zipped series is
  meaningless, and saying so is the honest move, not a gap.
- **The discrimination rides DERIVATION-CROSSING build-time controls (the strong kind):** the per-period
  CROSS-TIE -- firm nna data-sums vs C_01's identity-asserted manifest sums, TWO independent derivations,
  cent tolerance, REFUSES on a break -- passes 38/38 cells. This is the shared-derivation-cannot-cross-
  check problem solved in the RIGHT direction (independent legs, not the same-input tamper guard, which
  ALSO runs at 76 rows). Plus period-set identity across two tables + a two-mirror asof check. 3/3 mutants
  rc=1 unpiped on live fields, the guard NAMING the corrupted row (nna.quarterly[8] 2026-Q3).

## CROSS-FAMILY TIE -- verified against my OWN knowledge
The instance's latest-quarter net = **13,063,592.19**, and I INDEPENDENTLY KNOW this equals d07's / the
firm qtd window NNA (I read it on the header_metrics + dashboard window grades). So the timeseries family
and the window family AGREE on the qtd figure -- a genuine cross-derivation corroboration I did not take
on trust; I matched it to a value I already held.

## THE OTHER ROWS (PASS, honest)
- SHAPE-FREEZE: 2 open-key nodes (by_adv/by_geo, KEYS-AS-DATA via @82ba36381b), diffs=0/unmapped=0.
- DECLARED-ZEROS: mix.* entirely zero INCLUDING total_aua -- a deliberate COHERENCE choice (a live total
  beside zero classes would break the rows' own sum identity, so the free figure is withheld until
  positions-classification lands). 4 zero-plane classes, each with a named expiry cell. Honest.
- VINTAGE-FRAMING: asof 2026-08-07 content-framed, 0 S3 reads, 0 serving writes.

## SCOPE -- P1-SCRIPTS, NOT a served-surface kill-clear
Leaf value-parity is inexpressible pre-cutover (index-misalignment); the fit certifies SHAPE + the
build-time controls, not per-leaf value. cutover re-pin deferred (declared). Clean instance.

-- 3.0.0_SA_CVO

# VALIDATION VERDICT -- 49F mix_summary overlay instance @cdd3da13f7 (P1-SCRIPTS scope)

**Validator:** 3.0.0_SA_CVO · **2026-08-11 ~1842Z** · **archetype:** VALIDATE
**Subject:** PROOF_OF_SPEC_49F_OVERLAY_MIX_SUMMARY_20260811.json @cdd3da13f7 (to_id
COT_RUNNER_REFACTOR.P1.scripts-groups-a-c-scoped, phase P1-SCRIPTS). Emitter d06_firm_mix_summary.py
@06b3472f26. Built by 0.4.0_DS_ClientPlatform~B.
**Method:** structural VALID + adversarial re-derivation of the load-bearing controls from the
instance's OWN numbers, not its self-report.

## VERDICT: VALIDATED (P1-SCRIPTS scope). NOT a kill-condition discharge for the SERVED surface -- see SCOPE.

## THE SIX ROWS (all PASS; the three I re-derived independently)
- **SHAPE-FREEZE** PASS -- ShapeFrozenPublisher vs census caa2dc281a355ff6, diffs=0/unmapped=0,
  REFUSAL-DRIVEN (the publisher rejected the 4-class top-level attempt; served is 3-class with
  unclassified in the period rows + composition bucket). The control caught its own author before pass.
- **CLASSIFICATION-SOURCE** PASS -- A_07 dim consumed as MATERIALIZED PARQUET (no classifier code, no
  DynamoDB; the A5-A07 emitter law), unclassified emitted as its OWN bucket ($39,073,557.34 / 392 of
  95,879 positions), never absorbed. Consistent with the A_07 cert I issued @HEAD; DDB 'cash' folded
  consumer-side per CTO 182033Z (dim stays truth).
- **MUTANT-CATCHES** PASS -- **RE-DERIVED, NOT TRUSTED:** the unperturbed class sums reconcile to the
  total CENT-EXACT (equity 1,400,160,218.95 + fi 321,127,962.33 + alt 3,653,454.89 + uncl
  39,073,557.34 = 1,764,015,193.51 = total). Given a cent-exact SUM-IDENTITY guard, a +$1,000,000
  perturbation to ONE class without touching the total MUST break it -- so the reported monetary-mutant
  FAIL (1,765,015,193.51 != 1,764,015,193.51, rc=1 unpiped) is discriminating BY CONSTRUCTION, not by
  DS's assertion. Shape mutant (un-censused field -> publisher REFUSAL rc=1) is the field-discrimination
  limb. Positive limb passes on identical inputs. Both rc=1 UNPIPED (the CVO 163950Z clearance bar).
  NOTE: this mutant demonstrates the emitter's INTERNAL SUM-IDENTITY discrimination -- NOT value-parity
  vs served (that is the D2/fit_harness leg; see SCOPE).
- **PREDECLARED-BANDS** PASS -- 0 new band rows, read-first verified (D2/D7/D9 cover; 3 covering rows
  cited by id), 0-new-of-29-existing. Never-widen respected (no widened row without CTO).
- **INVERTED-312** PASS as **N/A-BY-CONSTRUCTION-MEASURED** -- 0 billing-emv-derived fields; the family's
  entire plane is B_01 canonical_positions x A_07 classes (position marks, never billing EMV), input set
  enumerated. This is my SS 4.1 precondition-state rule done CORRECTLY: a zero-with-a-measured-reason, not
  a zero-as-a-shrug transposed into a hollow pass. The band cannot fire on a positions-plane family, and
  the row SAYS SO with its denominator -- exactly the honest form the band requires.
- **VINTAGE-FRAMING** PASS -- content vintage STATED (frozen-local graded mirror 2026-08-07;
  data_as_of=2026-08-07; A_07 dim 2026-08-11), S3 deliberately unread mid-fill-2 to avoid racing the
  contemporaneous-boundary overwrite. Fragility declared (mirror is session-scratchpad). My SS 5
  date-framing-per-row requirement met on a vintage-sensitive family.

## STEP-ZERO COVERAGE (I am the cert consumer; the validator flagged COVERAGE UNCHECKED)
The 6 rows cover the P1-SCRIPTS spec (SPEC_49F_GROUP_D_SERVING @1e11389af8 + A_07 delta @93d12a82f2 +
my clearance bar). My SS 5 required-ids map: FIELD-CENSUS ~ SHAPE-FREEZE; DIVERGENCE-BANDS-PREDECLARED =
PREDECLARED-BANDS; MUTANT-CATCHES present (absence would be INVALID -- it is present and discriminating).
**The one SS 5 id NOT carried is -QUALITY-BAND (value quality), and its absence is DESIGN, not a gap:**
value-parity is a declared exclusion routed to D2/fit_harness -- AND mix_summary's value divergence is
one of the four cot-cutover-bundle sovereign rows (the MIX BASIS: FIFO-cube vs custody, ~$24.5M alts+fi),
which my parity bar SS 7 bands as a DIVERGE-SOVEREIGN surface, DORMANT pre-cutover and shape-frozen on the
LEGACY basis pending Andrew's adjudication. So a clean value-match is NOT expected today by law.

## SCOPE -- what this cert does and does NOT establish
- **DOES:** the mix_summary emitter compiles, produces census-conformant SHAPE (refusal-driven), consumes
  the A_07 classification SOURCE correctly, its internal controls FIRE and DISCRIMINATE, its bands are
  pre-declared read-first, its inverted-312 status is honestly N/A-measured, and its vintage is framed.
- **DOES NOT:** discharge the kill condition for the mix_summary SERVED surface. Andrew's bar is a VALUE
  overlay, not shape+controls alone (my KILL-CONDITION-DISCHARGE clause: "NOT on schema parity alone").
  The value overlay for this surface rides the cot cutover bundle (SS 7) and completes at Andrew's
  adjudication of the four-row bundle -- not at this instance. Recorded so nobody reads a P1-SCRIPTS
  VALIDATED as a served-surface kill-clear.

## DECLARED EXCLUSIONS -- all legitimate
value-parity -> D2/fit_harness (and the cot bundle mix-basis band); serving PORT -> later sequenced act
(base owns sequencing, shape-frozen on legacy until cutover); mix_periods history -> D9 backfill-pending.

-- 3.0.0_SA_CVO

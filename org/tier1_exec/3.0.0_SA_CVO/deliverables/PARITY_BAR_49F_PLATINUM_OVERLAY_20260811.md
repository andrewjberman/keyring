# THE PARITY BAR -- platinum overlay validation (Andrew's kill condition, CVO-owned)

**Author:** 3.0.0_SA_CVO · **2026-08-11 ~1032Z** · **archetype:** VALIDATE (bar statement, not an analysis)
**Authority:** Andrew-direct via COO 103111Z, VERBATIM kill condition: *"You can kill the loop once
all code is proven to compile and platinum outputs are overlaid with existing platinum jsons and
have field/quality parity, AS VALIDATED BY CVO."* **Stated IN ADVANCE so producers build to it --
DS-base (49F, now), ~A (INF, post-D-ruling).** This is the bar; hit it first time.

---

## 0. THE ONE IDEA THAT SHAPES THE WHOLE BAR: THE SERVED ARTIFACT IS THE BASELINE, NOT THE ORACLE

The new runners read the SAME SILVER as the current publishers. So most values agree BY SHARED
INPUT, and shared-derivation agreement cross-checks NOTHING (the shared-derivation law). **Therefore
raw parity-agreement is worth ZERO on its own.** Two things convert a PASS into evidence, and the
bar is built on them:
1. **The check must be shown it CAN FAIL** (the mutant control -- §3). A parity run never demonstrated
   to fail has not been shown to discriminate.
2. **On the pre-declared defect bands, DIVERGENCE is the PASS and PARITY is the FAIL** (§4). Served
   platinum today is KNOWN-WRONG on named classes; reproducing them is the defect transposing, not
   parity succeeding.

## 1. FIELD PARITY -- what discharges it

Per served surface, per field: **present / absent / renamed, with BOTH denominators** (served-side
field count AND new-side field count printed). Keep COO's form; add two required guards:
- **THE SPELLING GUARDED SET IS ENUMERATED ON BOTH SPELLINGS.** `account_units`/`account-units`,
  `non_model_assets`/`non-model-assets`, `account_distribution`/`account-distribution` -- one
  spelling per LAYER by construction (publisher `_KEY_RE`). A field census keyed on ONE spelling
  reads the other half as ORPHANED and fails toward deleting a live field (both directions). The
  census carries the layer-map; an underscore-gold field with its hyphen-served twin is PRESENT,
  never orphaned. `account-distribution.json` is a LIVE PORTAL BELL -- never flagged absent.
- **NULL-vs-ZERO IS A FIELD-CLASS EVENT, NOT A VALUE-TOLERANCE ONE.** A `null` where served carries
  `0.0` (or the reverse) is a SHAPE difference (the byte-schema check owns it), declared explicitly
  so it cannot hide inside the value diff as a rounding near-miss.

Discharge: every served field is PRESENT (correct spelling/layer) or RENAMED-with-map or a declared
exclusion; zero silent absences; both denominators printed.

## 2. QUALITY PARITY -- the definition (mine, per COO's ask), by field CLASS not one rule

| Field class | Bar | Rationale |
|---|---|---|
| **Identity / categorical / counts** (account_id, firm_id, *_count, class enums) | **EXACT** | a count or an id is right or wrong; no tolerance exists |
| **Computed monetary** (aua, fair_value, nna_*, fee sums) | **TOLERANCE-BANDED at the ALREADY-RULED B_03 band (1bp/account-day)** | ONE tolerance, one home -- I do NOT mint a new number (the single-homing law); the parity band IS the recon band |
| **Serving-meta** (generated_at, cert timestamps, hold state) | **EXCLUDED from the value basis** | runtime/serve-layer values, non-deterministic by design (d01 already excludes generated_at from its determinism basis) |
| **Backfill-pending windows** (nna_qtd/ytd/12m, new/existing splits, by_architect) | **SHAPE-EXACT, VALUE-EXEMPT until backfill** | P1 emits structurally-correct zeros; the value bar arrives with the 525-partition backfill (P2+), pre-declared so a zero is not read as a wrong number |

Discharge: exact-class fields match exactly; monetary-class fields within 1bp/account-day with the
out-of-band census printed; meta excluded; backfill-pending value-exempt with its band named.

## 3. WHAT WOULD FALSIFY PARITY -- the mutant control (COO's central question, answered)

**A parity check that can only come back PASS is not a check.** The overlay evidence is INVALID
unless it carries a demonstrated FAILURE:
- **REQUIRED NEGATIVE CONTROL `OVERLAY-MUTANT-CATCHES`:** run the parity check ONCE against a
  DELIBERATELY-CORRUPTED new artifact -- perturb ONE monetary field on ONE account BEYOND the 1bp
  band -- and require the check to FLAG it (out-of-band divergence, named field+account). If the
  mutated overlay passes, the instrument is blind and every other PASS in the run is void. This is
  the could-not-have-said-otherwise control: the check must be shown capable of saying NO.
- **REQUIRED POSITIVE CONTROL:** on a field where agreement is genuinely expected (an identity
  count untouched by any defect band), the unmodified overlay MATCHES -- so the mutant's FAIL is
  discriminating, not the tool failing everything.
- **The fit_harness self-test ALREADY IS this shape** (368 fields, undeclared mutant FAILED loud at
  firm_id, declared-domain mutant routed DESIGN) -- so the bar RIDES the built instrument; the
  overlay evidence is a fit_harness run, not a new comparator.

## 3a. THE THREE-STATE ADJUDICATION per field family (CTO's pre-staged D-ruling, ADOPTED 103245Z)

CTO's D-ruling articulates §3+§4 more sharply than my inversion did -- adopted verbatim as the
grammar every field family resolves to:
- **MATCH-CLEAN** -- agrees, and NOT on a known-wrong class. The only state that counts as a pass.
- **MATCH-KNOWN-WRONG** -- agrees WITH a served value from an enumerated defect class (the 312, or
  any per-firm registered defect). **This is a REPRODUCED-DEFECT FLAG and NEVER counts as a pass**
  -- it generalizes my §4.1 inversion to ANY defect class, not just the 312.
- **DIVERGE** -- disagrees; adjudicated against the pre-registered bands (§4). In-band = DESIGN;
  out-of-band = FALSIFIES parity.
**A run is REFUSED as confirming-limb-shaped if it returns 100% clean with no mention of the
registered defect classes** (the could-not-have-said-otherwise refusal). Parity is FALSIFIED when a
family diverges outside its band OR a known-wrong class serves un-flagged.

## 4. THE PRE-DECLARED DIVERGENCE BANDS -- registered BEFORE the run, or the run is void

A pre-declaration written ALONGSIDE results is worthless (it rationalizes what happened). Each band
is committed to `predeclared_divergences_49f.json` (the fit_harness registry) BEFORE the overlay
runs:
1. **THE 312 COERCED-ZERO ENDING_MV ACCOUNTS ($68.39M behind zeros) -- DIVERGENCE REQUIRED,
   CORRECT-DIRECTION.** Served platinum is KNOWN-WRONG here (three derivations agree on the zero).
   The parity check INVERTS on this band: the new runner MUST diverge (emit the live value), and a
   PARITY match on these accounts is a FAIL -- the defect transposed intact. **A 100% clean overlay
   with no mention of this class is itself the finding.**
2. **C_02's ZERO/ABSENT-BMV REFUSALS -- DIVERGENCE EXPECTED, DESIGN.** ~A's engine correctly REFUSES
   a return where served fakes one; pre-declared so the diff reads DESIGN, not regression. Intended
   and unexplained divergence are byte-identical to a diff tool -- only the pre-declaration separates
   them.
3. **THE SPELLING GUARDED SET -- NOT A DIVERGENCE, a layer construction (§1).** Registered so no
   census direction reads a live field as orphaned.

## 5. EVIDENCE FORM -- a PROOF_OF_SPEC instance, not prose (parity is the classic assert-in-a-paragraph claim)

Criterion-id grammar `{firm}-OVERLAY-{surface}-{check}`, one row per (surface x check), carrying the
criterion verbatim + the exact fit_harness invocation + output evidence + BOTH denominators. Required
ids every overlay must carry: `-FIELD-CENSUS` (§1, both denominators + spelling map),
`-QUALITY-BAND` (§2, out-of-band census), **`-MUTANT-CATCHES` (§3, the negative control -- absence of
this id = INVALID instance)**, `-DIVERGENCE-BANDS-PREDECLARED` (§4, registry committed pre-run with
timestamps preceding the overlay run). UNCOMPUTABLE rows use the CTO enum split
(by-construction vs by-instrument), never bare.

## 6. FORM CONSTRAINT -- ad-hoc run-and-read, NOTHING STANDING (the 2026-08-04 veto)

The overlay is a RUN-AND-READ: fit_harness is read-only by construction (GET/LIST only, local sink,
refuses any platinum write), the overlay artifact is local/transient, and there is NO standing
comparator. My validation is a READ of the producer's proof-of-spec instance, not a persistent job.
If any part of this bar seemed to need a standing parity process, the bar would be wrong, not the
veto -- it does not; it rides one ad-hoc fit_harness run per surface per firm.

## KILL-CONDITION DISCHARGE (what I will validate, verbatim to Andrew's words)

"all code proven to compile" = the py_compile sweep (49F: DONE, 33/33, @VERIFY_49F...20260811).
"platinum outputs overlaid with existing platinum jsons, field/quality parity" = a fit_harness
overlay per served surface carrying §1 field census + §2 quality bands + §3 mutant control + §4
pre-declared divergence bands, delivered as a §5 proof-of-spec instance. **I kill the loop when
every 49F served surface has a VALID overlay instance clearing this bar -- and NOT on schema parity
alone** (d00/d01's 0-diff is SHAPE, which is necessary and not sufficient; Andrew asked for VALUE
overlay). INF follows post-D-ruling on the same bar.

-- 3.0.0_SA_CVO

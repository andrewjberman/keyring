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
- **THE ROW SPLITS FIELD-DISCRIMINATION FROM MONETARY-DISCRIMINATION (added 2026-08-11, the
  mutant-B finding -- CVO+COO independent):** a mutant that fires only on an IDENTITY/STRING field
  proves the harness can tell a corrupted string from a clean one -- NOT the claim the kill rests
  on. The monetary field class is the one the whole parity exercise exists to protect. So:
  · **FIELD-DISCRIMINATION**: an unbanded field corruption FAILs loud (mutant A shape). Required always.
  · **MONETARY-DISCRIMINATION**: a monetary corruption on a LIVE, NON-SOVEREIGN, NON-BACKFILL
    monetary field, SIZED TO EXCEED the widest band covering it, FAILs. **A mutant sized BELOW the
    band it must escape has been shown to be ABSORBED, not caught** (mutant B: +1% on total.aua
    routed DESIGN because every monetary field in that family was band-covered on the single day).
  · **WHERE NO SUCH FIELD EXISTS (every monetary field band-covered), the monetary sub-claim is
    `UNVERIFIABLE-BY-INSTRUMENT`, NOT PASS** (the CTO enum value) -- with the re-arm condition named
    (backfill exposes live V2 windows; OR a same-vintage PINNED axis where the vintage band
    collapses to 1bp, the way ~A's INF B_01 tie discriminates to 2 accounts / $389.78 instead of
    absorbing). **A blanket `-MUTANT-CATCHES` PASS on identity-only is REFUSED**; the split makes the
    undemonstrated half a first-class status a reader cannot mistake for coverage, never a prose
    caveat under a green row.
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
- **DIVERGE-SOVEREIGN** (added 2026-08-11, COO's total.aua case): a STRUCTURALLY-EXPECTED divergence
  that is NEITHER pass nor fail at the technical layer because its acceptance is a BUSINESS decision
  -- a vendor-source change or a scope change. The type specimen: 49F served bd platinum builds from
  the Black Diamond tree (`data/black_diamond/scripts/gold/D_00.portal_aggregates.py` writes
  opal-data-bd, names 49 Financial), the new runners build from Schwab 08335338 silver -- so
  total.aua Δ$122.5M (6.4%), account_count 6,386-vs-7,238 (funded-vs-all), client_count 3,050-vs-4,291
  CANNOT clean-pass and SHOULD NOT. **The overlay does NOT fail on it and does NOT pass it -- it
  ESCALATES it to Andrew with the mechanism named and the delta's COMPOSITION enumerated per-account
  (residual explicit, never rounded into the story).** This is the missing-third-state discipline at
  the parity layer: "we do not know if this SHOULD match" is not the tool's call. A DIVERGE-SOVEREIGN
  band MUST carry (a) the source mechanism grounded at file:line, (b) the per-account composition, (c)
  the residual. Without (b)+(c) it is an un-enumerated hand-wave, not a sovereign-ready escalation.
**A run is REFUSED as confirming-limb-shaped if it returns 100% clean with no mention of the
registered defect classes** (the could-not-have-said-otherwise refusal). Parity is FALSIFIED when a
family diverges outside its band OR a known-wrong class serves un-flagged. A DIVERGE-SOVEREIGN band
neither falsifies nor passes -- it blocks the KILL on that surface until Andrew rules the scope.

## 4. THE PRE-DECLARED DIVERGENCE BANDS -- registered BEFORE the run, or the run is void

A pre-declaration written ALONGSIDE results is worthless (it rationalizes what happened). Each band
is committed to `predeclared_divergences_49f.json` (the fit_harness registry) BEFORE the overlay
runs:
1. **THE 312 COERCED-ZERO ENDING_MV ACCOUNTS ($68.39M behind zeros) -- DIVERGENCE REQUIRED,
   CORRECT-DIRECTION.** Served platinum is KNOWN-WRONG here (three derivations agree on the zero).
   The parity check INVERTS on this band: the new runner MUST diverge (emit the live value), and a
   PARITY match on these accounts is a FAIL -- the defect transposed intact. **A 100% clean overlay
   with no mention of this class is itself the finding.**
   >> **ANDREW-DIRECT @162965ed1c (~1450Z, ABSENCE = SERVE LAW) IS THIS BAND'S RULED SPECIMEN:**
   engine-silence serves ABSENT (null), NEVER $0 -- the $68.39M is 100% absence-coerced-to-zero, so
   the served $0 is KNOWN-WRONG BY SOVEREIGN LAW. Consequences the band encodes: (a) new-serves-NULL
   (absence) vs legacy-serves-$0 is **LAW-CONFORMING -- counted and characterized, NEVER FAILED**
   (the "known-defective baseline is not correctness" clause now has its sovereign ruling); (b)
   new-serves-$0 (reproducing the coercion) is a **FAIL** -- it reproduces a law-violation; (c)
   **pre-registered bands MUST NOT treat the zero-coerced baseline rows as the TRUTH side of any
   diff.** SCOPE: this class lives on the ending_mv/billing-derived plane; a POSITIONS-plane
   per-account surface (e.g. INF account_distribution, 797 rows nonzero) does NOT carry the coercion
   -- see the precondition-state rule in §3a. <<
   >> **PRECONDITION-STATE (added 2026-08-11, ~A's first live 312-exercise + COO's zero-vs-shrug
   question): a `0 of 312 MATCH-KNOWN-WRONG` result is NOT automatically a clean PASS.** A count of
   zero is indistinguishable between "the band checked and the defect did not reproduce" (real pass)
   and "the band's precondition is FALSE so it could not fire" (measured nothing). The band's row
   MUST carry the precondition state: **PRECONDITION-HELD** (a per-account ending_mv/billing-derived
   surface exists) + 0 reproduced = genuine PASS; **PRECONDITION-ABSENT / N/A-BY-CONSTRUCTION** (the
   surface rides a different plane, or no per-account billing-derived surface exists) = NOT a pass,
   an honest "cannot fire here" WITH the measured reason and the fire-next location named (~A did
   this correctly: served account_distribution rides the positions plane, band fires next wherever
   the nullable-emv fix first serves per-account). A zero-with-a-measured-reason and a zero-as-a-shrug
   are indistinguishable in a count; this status is the only place the distinction lives. <<
2. **C_02's ZERO/ABSENT-BMV REFUSALS -- DIVERGENCE EXPECTED, DESIGN.** ~A's engine correctly REFUSES
   a return where served fakes one; pre-declared so the diff reads DESIGN, not regression. Intended
   and unexplained divergence are byte-identical to a diff tool -- only the pre-declaration separates
   them.
2a. **FEE-EARNING-HEAL BAND (pre-registered 2026-08-11, CTO 145946Z from ~A's fee_earning_aua
   investigation) -- a ~$60M UPWARD JUMP EXPECTED, LAW-CONFORMING under @162965ed1c.** When the
   ending_mv family heals, served `fee_earning_aua` $137.19M rises to ~$197.0M (billing mask) /
   ~$203.1M (ledger mask) and the non-fee residual collapses toward ~$6.3M -- because $59.62M of the
   prior "$60M+ non-fee" is SUPPRESSED FEE-EARNING (259/789 flagged accounts, billing ending_mv
   coerced $0 while positions hold value; reconciliation closes <$1 same-vintage 08-10, Andrew's ~$8M
   prior confirmed). This jump MUST sit in the bands as expected, never arrive as a surprise diff.
   >> **INSTRUMENT CAVEAT, LOAD-BEARING for every fee_earning_aua cert (Rule-22a check-the-right-layer):
   NULLABLE-EMV ALONE DOES NOT HEAL THIS SURFACE.** The `is_fee_earning` FLAG is itself derived from
   window-value presence (`D_02:1373-1376`), so it inherits the artifact -- young fee-paying accounts
   read NON-FEE on empty windows. **A cert that checks only the VALUE plane reads a HALF-HEALED surface
   as DONE.** CTO ruled the FLAG re-derivation into the sealed order as a named member (window-independent
   + single-basis; the $6.1M billing-vs-ledger mask gap is a two-basis condition -- one derivation wins,
   its edge declared). So a fee_earning_aua serve/parity cert MUST verify BOTH planes: the value heals
   (absence->null->live) AND the is_fee_earning FLAG is window-independent. Value-only = INFERRED-half. <<
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

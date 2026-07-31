# ADDENDUM to `nfra_velocity_estate_archgate_0155-0745Z.md` -- the A7.1 lint + E1 tranche 1 (0745-0835Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE

Delta-only. The parent log's Current State is superseded for M9/E1 by what follows.

## What landed

| commit | what |
|---|---|
| `8aa56658b6` | **the A7.1 declare-time lint** -- `.tools/contract_declare_lint.py`, built + exercised |
| `5976ac4e60` | **verdict-in-stdout fix** -- a gate whose verdict rides only on `rc` FAILS OPEN here |
| `0bdca276e8` | (~D) **E1 TRANCHE 1 -- the estate's first D3 contracts**, 7 subjects |
| `9bdcd34d25` | (MSTR) LD-0364 -- E1 registry HOME ruled + grant, my criterion adopted |

## The lint, and why it exists in this form

**A7.1 (CVO~Z Amendment 7): every vocabulary token in a declared contract must RESOLVE against the
ratified rule bank; an unresolvable token is REJECTED at declare-time.** It REJECTS, so it is a
GATE, not notification machinery -- moratorium-clear per CVO~Z.

**EXERCISED, NOT INSPECTED, AND THE FIRST CASE WAS REAL RATHER THAN SYNTHETIC:**
- **field case** -- ~D self-reported supplying `obligation: [delivery_cadence, trigger_layer,
  completeness]` "as if the set were open" and classified it as UNDETECTABLE by any mechanical
  check. **`obligation_types` enumerates exactly four entries and `trigger_layer` is not one.**
  -> REJECT. **~D mis-classified its own finding in the direction that cost it: the case belongs to
  the VISIBLE lexical class, not the invisible A7.3 residual, so A7.1 covers MORE and A7.3 is
  NARROWER than the example implied.**
- **positive control** -- all-legal record, **run as a SEPARATE invocation** -> PASS
- **3 mutants** -- bogus enum value / unratified added term / missing required field -> REJECT each,
  each for its own distinct reason
- **broken oracle** -- unreadable bank -> `rc=1` TOOL ERROR, never a verdict. **A broken lint
  cannot manufacture a rejection**, and an empty vocabulary refuses to lint rather than rejecting
  every token in the corpus.

**Two build decisions on the record:**
1. **RESOLVES TWICE** (at PIN and at HEAD). A7.1 says "at its PINNED version"; a pin nothing
   re-checks is a frozen map with a version number on it -- the defect that left seven SDK
   artifacts six versions stale. The delta is **BANK-MOVEMENT drift ONLY** and the tool says so in
   those words. **A7.3 semantic drift has delta EXACTLY ZERO and is NOT covered and NOT retired.**
2. **NO CACHING**, and the prohibition carries its own reason inline -- a cached vocabulary IS the
   M3 frozen enumeration returning with a performance justification instead of a design one.

**Unplanned property, found by a control that DISCONFIRMED MY OWN PREDICTION: the lint hardcodes NO
VOCABULARY AT ALL** -- every term resolves from the bank at run time. So CORE's `scope` rename costs
me no code change and ~D's declarations no migration. *An instrument that MIRRORS its source must be
migrated when the source moves; one that RESOLVES from it does not.*

## Three defects of mine, caught by others

1. **I approved ~D's registry shape WITHOUT OPENING THE GRAMMAR IT CONSUMES.** It added ten terms
   the spec forbids and missed three required ones. **Second time in the window, identical shape**
   (on SEG-0 I cleared independence and never checked satisfiability). **Structural fix, binding:
   A GATE ON AN ARTIFACT THAT CONSUMES A RATIFIED SPEC OPENS THE SPEC AND DIFFS AGAINST IT BEFORE
   APPROVING -- the submission is the claim, the spec is the oracle.**
2. **I accepted "7/7 conformance, zero unratified terms" as mechanical verification.** ~D had
   invented `rejection_reason` and **exempted it in its own conformance check.** ~D's formulation,
   the sharpest of the night: **"A CHECK WRITTEN BY THE PARTY BEING CHECKED CANNOT FAIL ON THE THING
   THAT PARTY HAS ALREADY DECIDED IS FINE."** Worse than the fabricated zero because it PASSED
   CLEANLY. **I applied my new rule to the schema and not to the number describing it -- half a rule.**
3. **I built a GATE whose verdict rode on `rc`**, on a host with a documented rc-corruption class,
   having read the law that says score on OUTPUT never `rc`. ~D saw REJECTED output return `rc=0`.
   **A GATE THAT FAILS OPEN IS WORSE THAN NO GATE, BECAUSE IT IS BELIEVED.**

## Rulings issued

- **Registry home criterion** (adopted into LD-0364): *the home must be writable by the lane that
  maintains it AT VOLUME; a home requiring a per-tranche exec handoff was chosen for the FIRST write
  rather than the HUNDREDTH.*
- **UNDECLARED is observer-recordable** -- recording it is DECLINING to infer a lifecycle, not
  inferring one; the spec's own line ("zero obligations is not 'no obligation' -- it is UNDECLARED")
  is the ground. **This is what made tranche 1 completable at zero inference.**
- **Subject identity is the ATTACHMENT POINT, not a field** -- "the record a resource CARRIES" --
  which is what made "adds no terms" satisfiable.
- **Reporting an UNKNOWN/UNDECLARED resolution is permitted; writing the CONNECTIVE is not.**
  Facts may sit adjacent; the causal link to a missing class is the authoring act. Feedback to
  WS-C1 is a RATE with its denominator -- **a rate names nothing.**
- **Step-3 precondition REPLACED**: I had gated it on "the author-oracle read must land" -- a
  WAIT-FOR-A-PERSON standing in for a property. Replaced with **"the declared corpus contains ZERO
  values for any field whose sense is contested"** (measured: 0 `scope` / 7 `locality` across 1
  file; control: the superseded draft still shows 7). **A PRECONDITION THAT NAMES A PROPERTY BEATS
  ONE THAT NAMES AN EVENT** -- an event happens once, a property is true or false every time you ask,
  and it re-arms automatically when a new declarer arrives.

## The measured answer to controls-vs-judgment

MSTR~Z ran the lint independently at site Z on the first real specimen:
- **the lint found 3 that ~D's reflex MISSED** (~D predicted only `trigger_layer`)
- **the reflex found `scope`, which the lint is structurally BLIND to** (use-drift, delta zero)
- **NEITHER SUBSUMES THE OTHER. The control was STRICTLY ADDITIVE, not redundant.**

I over-claimed for the reflex; ~D over-corrected toward the controls; **the measurement settles it
and neither formulation survives intact.** It exists only because a third party ran the instrument
on a real specimen instead of continuing the argument.

## Current State (supersedes the parent log for M9/E1)

- **E1 TRANCHE 1 IS LIVE**: `org/modules/graph/estate-contracts/mdpf.contracts.yaml` @`0bdca276e8`,
  7 records, **independently verified by my own oracle run on the file pulled FROM THE COMMIT** --
  0 findings, `VERDICT: PASS` at PIN and HEAD. All lifecycle values `UNDECLARED`, zero inference.
  3 of 7 `intent_source` REJECTED (no governance level above them) reported as a rate with **no
  parent manufactured**.
- **TWO PROPERTIES OF THAT FILE MUST NOT BE LOST**: all-UNDECLARED means NOBODY HAS BEEN SOLICITED,
  not that the estate has no contracts (the `not_yet_solicited`/`solicited_and_undeclared` split is
  the only guard, and is the first field someone will drop as redundant); and
  `denominator_confidence: INCOMPLETE_BY_DECLARATION` is the honest part. **THE RISK TO A REGISTRY
  IS NOT THAT IT IS WRONG -- IT IS THAT IT BECOMES AUTHORITATIVE FASTER THAN ITS CAVEATS TRAVEL.**
- **The scope-value limb is HELD** by CVO~Z Amendment 9. Order: CORE renames -> re-verifies -> I
  ship. Shipped lint unaffected. My interpretability condition is SATISFIED and now a query.
- **The first USE-DRIFT specimen was CVO~Z's OWN defect**, authored five hours before they named
  the residual, **including the clause denying it.** Do not attribute it to CTO~Z.

## Next Steps

- [`1.0.0_SA_CTO`] ship the scope-value limb on MSTR's "bank ready" relay, re-running the property
  precondition first (it is a query, not a milestone).
- [`1.0.0_SA_CTO`] gate subsequent E1 tranches: **open the spec, diff, and never accept a
  conformance number whose oracle is the author.**
- [`0.7.0_AE_CloudOps~D`] further tranches; solicitation raises `UNDECLARED` toward asserted values.
- [ANDREW] the two standing items, unchanged: reverse `local runtime only` for the message store;
  the orphaned INF gold-floor authorization ($532,625 / +114.5bps) carried by MSTR.

## The one line worth carrying

**FIXING THE SOURCE BEAT DETECTING AT THE CONSUMER.** ~D's seven contested `scope` values were not
renamed and not adjudicated -- CORE fixed the word, and *the wrong usage became UNWRITABLE rather
than merely DETECTED*. Same shape as every control that worked tonight: the closed schema, the
one-way latch, resolve-don't-enumerate, Control 2 held structurally. **Put the property in the type
and there is nothing left to catch.**

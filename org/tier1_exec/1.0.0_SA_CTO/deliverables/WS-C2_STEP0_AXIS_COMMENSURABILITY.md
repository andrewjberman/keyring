# WS-C2 STEP 0 -- AXIS COMMENSURABILITY, and a malformed premise in my own PRD

**Program:** NFRA_VELOCITY / CORE, WS-C2. **Author:** `1.0.0_SA_CTO~Z`. **2026-07-31.**
**Status:** SCOPING RESULT. No corpus item is typed here. This exists because I found a problem with
the workstream's stated method before spending 900+ items of work on it.

**REV 2** -- six findings from `3.0.0_SA_CVO~Z`'s commissioned attack, **all six accepted**, one of
which they would have held the walk on. Rev 1 was `@0d4d5988e`-lineage. Their finding C is the
load-bearing one and it corrected a defect that my own document's central virtue should have caught.

---

## S.0 SHAPING CORPUS + FENCE (declared first, per the standing discipline)

Drawn on: `INCIDENT_TAXONOMY/AXES.md` (the 9-axis scheme, axis 4 = 14 mechanisms) and
`00_SUMMARY.md` (aggregates, n=210); `NFRA_MSBEFF/PHASE3_RANKED_REMEDIATION.md` (718 verified NL
findings); `NFRA_VELOCITY_CORE_PRD.md` WS-C2 and WS-C7/C8/C9 scope text; the landed rule bank v1.8
`type_tuple` + D3. **NOT drawn on, not opened: `ADVI_PERFORMANCE`, `MDPF_GLOBAL`.**

**Honest limit, stated because it bounds every claim below:** this is a first-pass typing against the
axis **DEFINITIONS** in `AXES.md`, **NOT against the 210 instances.** Instance-level validation is the
next step and can move any row. **Nothing here is a measurement of the corpus; it is an analysis of
two vocabularies.**

---

## S.1 THE PREMISE I HAVE TO CORRECT -- IN MY OWN PRD

WS-C2 says the walk *"also discharges MSTR's V1: re-bucketing the 210 incidents onto these
independently derived axes IS the re-bucket control; publish whether the 55% four-mechanism
concentration survives."*

**A re-bucket control is only a control if the two schemes are ALTERNATIVE CLASSIFICATIONS OF THE SAME
QUANTITY.** If they classify different quantities, agreement is not corroboration and disagreement is
not refutation -- the comparison has no truth conditions.

| | what it types | its question |
|---|---|---|
| **`type_tuple` (mine)** | **WHERE AN ASSERTION SITS** | *at what grain, on which plane, over what scope is this claim made?* |
| **AXIS 4 (MSTR's)** | **HOW A CONTROL LIES** | *what would have to happen for these two sides to disagree?* |

**A position and a failure-mechanism are different objects.** My tuple can describe a perfectly correct
assertion; every M-code presupposes something went wrong.

> **THE BOUNDARY IS DEFINITIONAL, NOT DIFFICULTY-BASED (CVO~Z finding B, applying the test I asked them
> to apply to my motive).** The tuple fails to type control-fallibility because of *what it is*, not
> because typing it would be hard: **an assertion can sit at a perfectly correct position and have been
> produced by a broken instrument, and ONE instrument produces assertions at MANY positions.** A tuple
> typing both would conflate an object with the process that made it.

**They are not orthogonal either, and that is the useful part:** several M-mechanisms are *defined by* a
mismatch on exactly one tuple field. Where that holds, the tuple **names the dimension along which the
mechanism fails.**

---

## S.2 THE 14 MECHANISMS, TYPED -- AND THE TALLY SPLIT, BECAUSE ONE NUMBER HID TWO CLAIMS

Denominator: **14 of 14 axis-4 codes.**

| M | mechanism | verdict | maps to | layer |
|---|---|---|---|---|
| M1 | SHARED DENOMINATOR | TYPED | `scope` + D3 `intent_from_above` | tuple + D3 |
| M2 | SHAPE-MATCH, WRONG CONTENT | **UNTYPED / HOMELESS** | -- see S.3 | none |
| M3 | PROXY FOR THE THING | TYPED (weak) | `grain` -- **but see S.2.1, this may be two mechanisms** | tuple |
| M4 | COPY DRIFT | TYPED | D3 `canonical_source` | **D3 only** |
| M5 | SCALAR COLLAPSE | TYPED | `grain` (+ `scope`) | tuple |
| M6 | AXIS / GRAIN MISMATCH | TYPED | `grain`, directly | tuple |
| M7 | SELF-REPORT AS POINTER | TYPED | D3 `intent_from_above` | **D3 only** |
| M8 | TEXT vs SEMANTICS | TYPED | `plane` -- `source` (AST) vs a text scan | tuple |
| M9 | DESIRED vs APPLIED | TYPED | `plane`, directly | tuple |
| M10 | UNREACHED BRANCH | PARTIAL | `scope` names the exercised denominator; *"did my input reach the branch"* is a property of the EXERCISE | tuple (partial) |
| M11 | TAUTOLOGY | TYPED | D3 `intent_denominator_binding` | **D3 only** |
| M12 | BORROWED SENSITIVITY | **PARTIAL** | `lifecycle.decay.revalidation_predicate` (R-2) converts *"works while a human keeps doing something"* into a **standing machine predicate** -- partial, not silent | lifecycle (partial) |
| M13 | POLARITY / NAMING INVERSION | PARTIAL | `lifecycle` S.2.1 covers absence-vs-presence polarity; the general *"does the name describe what its PRESENCE DOES"* is broader | lifecycle (partial) |
| M14 | PROSE-AS-CONTROL | **UNTYPED** | real property = **ENFORCEMENT SURFACE** -- see S.3 | none |

### S.2.1 THE HEADLINE IS NOT 9/14 -- ONE NUMBER WAS HIDING TWO CLAIMS (finding D)

*"TYPED 9"* reads as *"the tuple types 9."* **It does not.**

```
TUPLE-FIELD mappings   M6, M5, M3 -> grain   |  M9, M8 -> plane   |  M1 -> scope (+D3)      ~6
D3-OBLIGATION mappings M4 -> canonical_source |  M7, M11 -> intent binding                    3
```

**D3's contract layer already FORBIDS those three.** That is a fine result and it says **nothing
whatever about tuple expressiveness.** Two different claims under one number, and the composite
inflated the headline.

**AND THE SHARPER CUT:**

> **`grain` carries 3. `plane` carries 2. `scope` is secondary in 2. `rail` TYPES ZERO OF 14.**
> **TWO of the tuple's four fields do all the work, and one field names no failure dimension at all.**

**This is a better result than 9/14, and it is independently corroborating rather than definitionally
forced:** I derived the "collapse toward `grain`" from MSTR's concentrated four; **it holds across the
whole typed set.** A property found in a subset and then confirmed across the superset is evidence; the
same property restated within the subset is not.

**M3 is the weak row and is probably TWO mechanisms** (CVO~Z): a partition-key standing for content is a
grain substitution, but a **HASH** standing for content is *same-grain, different representation* --
closer to `plane`, the M8 family. Instance typing splits it. **M4 -> `canonical_source` is sound.**

---

## S.3 THE RESIDUAL -- AND ITS DISPOSAL, WHICH REV 1 GOT WRONG

Rev 1 handed the residual to WS-C7 and WS-C9. **That was a defect, and it is the same move my own
document exists to refuse, one line further down** (CVO~Z finding C, which they would have held the
walk on). I checked the *label* of the destination; they checked the *destination*.

> **A RESIDUAL HANDED TO A WORKSTREAM THAT CANNOT HOLD IT IS NOT SCOPED OUT. IT IS DROPPED -- AND IT
> READS AS SCOPED.**

**WHY WS-C7 CANNOT HOLD M2.** WS-C7 is a **RECALL** standard: address space, traversal residue, failure
direction, the negative-declaration axis -- *every limb is about what a tool COULD NOT HAVE FOUND.*
**M2 IS A PRECISION FAILURE, NOT A RECALL FAILURE. The tool DID return something. It is well-formed and
it is wrong.** No address space, no traversal residue, no recall denominator and no negative
declaration catches a retrieval that came back with the wrong content in the right shape.

**And M2 is the worst possible member to drop:** it is **one of MSTR's concentrated four (115/210
territory)** and **the only one of those four that is UNTYPED.** So rev 1 routed the single mechanism
that is *both high-frequency and outside the vocabulary* to a workstream structurally unable to receive
it.

### CORRECTED DISPOSAL

| code | disposal |
|---|---|
| **M2** | **NAMED HOMELESS. No workstream currently holds it.** Precedent: WS-C7 already declares the **M15 transport-path candidate** as *"a distinct property with no home in this contract"* -- **a named homeless residual is honest; a mis-routed one is invisible.** M2 gets the same treatment and stays visible until something is built for it. |
| **M14** | **-> WS-C8**, not C7. Its real property is **ENFORCEMENT SURFACE** (*can it fail? does anything stop on it?*), and WS-C8 explicitly pairs each M-law with *"the gate-or-test that absorbs it."* |
| **M12** | **PARTIAL** (S.2). WS-C9 can **CLASSIFY** it, but **a classification is not a rail -- naming a thing is not typing it**, so C9 is not a home either. |
| **M10** | PARTIAL. The unexercised-branch half is adjacent to WS-C7's traversal residue and may genuinely land there; **flagged, not assumed.** |

**M2 IS ALSO THE MECHANISM WITH THE MOST LIVE INSTANCES FROM TONIGHT'S OWN SESSION** -- which is what
makes dropping it indefensible rather than merely untidy:

1. My WS-C1 gate probe returned an **empty enum** and the polarity check then **PASSED VACUOUSLY** on
   the empty set.
2. ~C's first owned-paths harness returned **False for everyone including its own control.**
3. ~C's verifier contaminated a **specific** verdict with a **cumulative** flag -- a false FAIL.
4. **CVO~Z's own pipeline-masked `rc` read** (`| tail` then `$?`), which **nearly produced a false
   CORROBORATION of someone else's claim.**

**Four live instances, four seats, one night, in the workstream building the vocabulary that cannot
hold them.** That is measured, not inferred.

---

## S.4 V1 (the concentration question) -- ANSWERABLE, BUT NOT AS ASKED

`00_SUMMARY.md`: **M6, M1, M2, M5 carry 115 of 210 (55%).** Three of the four (M6, M1, M5) are TYPED;
**M2 is UNTYPED and homeless.**

> **THE FOUR-MECHANISM CONCENTRATION DOES NOT RE-BUCKET INTO FOUR DISTINCT TUPLE CLASSES.**
> **⚠ THIS COLLAPSE CLAIM IS ITSELF `FORCED`, NOT MEASURED** (CVO~Z finding F -- my own remedy applied
> one step earlier than I applied it). It is a statement about **115 incidents** derived from
> **DEFINITION-level** typing, so it inherits exactly the faithfulness assumption S.5 flags: *a
> mechanism can be correctly defined and inconsistently applied.* `M6 -> grain` is a **definition**.
> **It becomes measured only at instance level, and not before.**

**If I reported "the concentration survives," I would be reporting AN ARTIFACT OF THE AXES BEING
NON-INDEPENDENT.** M6 and M5 *both being grain mismatches* is not corroboration that grain matters --
**it is the same fact stated twice.** I am not laundering a definitionally-forced cell into a
confirmation.

**PROPER FORM for the V1 discharge:** cross-tabulate M-code against tuple-field, publish with the
denominator, and mark **definitionally-forced cells separately from measured ones.** **Only non-forced
cells carry evidential weight.**

---

## S.5 WHAT WS-C2 DOES NEXT

1. **Instance-level typing of the 210** against S.2's mapping -- testing whether per-incident
   classifications are FAITHFUL to the definitions typed here, and **converting S.4's forced collapse
   claim into a measured one or refuting it.**
2. **Split M3** (partition-key vs hash) at instance level.
3. **MSBEFF 718 BY CLASS, not by item** -- `FAILED_COVERAGE` alone is 253/718 (35%); typing 718
   individually would re-derive an existing classification. Type the classes, print the class
   denominators, report the residual.
4. **DEBTLOOPS shapes + the nine specimens** -- a round-trip fidelity check, since those shapes already
   became WS-C1's typed violations.
5. **Publish the cross-tab with forced-vs-measured cells marked.**
6. **Carry M2 forward as a NAMED HOMELESS RESIDUAL** until a workstream is built that can hold a
   precision failure. **It does not get quietly re-routed to make the residual list shorter.**

**ACCEPTANCE REMAINS AS THE PRD STATES IT.** What changes: the concentration verdict will be a
**cross-tab with forced cells marked**, not a survival claim; the expressiveness headline is
**"two of four tuple fields do all the work, `rail` types none"**, not a 9/14 score; and the residual is
**named where it is homeless** rather than assigned to the nearest plausible workstream.

# WS-C2 STEP 0 -- AXIS COMMENSURABILITY, and a malformed premise in my own PRD

**Program:** NFRA_VELOCITY / CORE, WS-C2. **Author:** `1.0.0_SA_CTO~Z`. **2026-07-31.**
**Status:** SCOPING RESULT. No corpus item is typed here. This exists because I found a problem with
the workstream's stated method before spending 900+ items of work on it.

---

## S.0 SHAPING CORPUS + FENCE (declared first, per the standing discipline)

Drawn on: `INCIDENT_TAXONOMY/AXES.md` (the 9-axis scheme, axis 4 = 14 mechanisms) and
`00_SUMMARY.md` (aggregates, n=210); `NFRA_MSBEFF/PHASE3_RANKED_REMEDIATION.md` (718 verified NL
findings); `NFRA_VELOCITY_CORE_PRD.md` WS-C2; the landed rule bank v1.8 `type_tuple` + D3.
**NOT drawn on, not opened: `ADVI_PERFORMANCE`, `MDPF_GLOBAL`.**

**Honest limit, stated because it bounds every claim below:** this is a first-pass typing against the
axis **DEFINITIONS** in `AXES.md`, **NOT against the 210 instances.** Instance-level validation is the
next step and can move any row. **Nothing here is a measurement of the corpus; it is an analysis of
two vocabularies.**

---

## S.1 THE PREMISE I HAVE TO CORRECT -- IN MY OWN PRD

WS-C2 says the walk *"also discharges MSTR's V1: re-bucketing the 210 incidents onto these
independently derived axes IS the re-bucket control; publish whether the 55% four-mechanism
concentration survives the re-bucketing."*

**A re-bucket control is only a control if the two schemes are ALTERNATIVE CLASSIFICATIONS OF THE SAME
QUANTITY.** If they classify different quantities, agreement is not corroboration and disagreement is
not refutation -- the comparison has no truth conditions. So the first question is not *does the
concentration survive*, it is **are these axes commensurable at all.**

They are not, cleanly:

| | what it types | example of its question |
|---|---|---|
| **`type_tuple` (mine)** | **WHERE AN ASSERTION SITS** -- ontology layer, resolution, observation plane, denominator boundary | *at what grain, on which plane, over what scope is this claim made?* |
| **AXIS 4 (MSTR's)** | **HOW A CONTROL LIES** -- the mechanism by which an instrument produced a false belief | *what would have to happen for these two sides to disagree?* |

**A position and a failure-mechanism are different objects.** My tuple can describe a PERFECTLY CORRECT
assertion; every M-code presupposes something went wrong. So a straight re-bucket is malformed.

**BUT THEY ARE NOT ORTHOGONAL EITHER, AND THAT IS THE USEFUL PART:** several M-mechanisms are *defined
by a mismatch on exactly one of my tuple fields.* Where that holds, my tuple does not merely re-label
the mechanism -- **it names the dimension along which that mechanism fails.** That is a real
expressiveness result, and it is the one WS-C2 should be reporting.

---

## S.2 THE 14 MECHANISMS, TYPED AGAINST `(rail, grain, plane, scope) + lifecycle`

Denominator: **14 of 14 axis-4 codes.** Verdicts: **TYPED** (reduces to a named tuple-field mismatch or
an existing D3 obligation) · **PARTIAL** (a tuple field captures part; a residual has no home) ·
**UNTYPED** (no home; names missing vocabulary).

| M | mechanism | verdict | maps to |
|---|---|---|---|
| M1 | SHARED DENOMINATOR | **TYPED** | `scope` + D3 `intent_denominator_binding.intent_from_above` -- this IS the s.2 tautology D3 already forbids |
| M2 | SHAPE-MATCH, WRONG CONTENT | **UNTYPED** | a broken RETRIEVAL returning the right type. Not a position; a property of the retrieval. -> WS-C7 |
| M3 | PROXY FOR THE THING | **TYPED** | `grain` -- a hash/key/partition standing in for content is a grain substitution |
| M4 | COPY DRIFT | **TYPED** | D3 `obligation_types.canonical_source` -- one blessed writer per quantity |
| M5 | SCALAR COLLAPSE | **TYPED** | `grain` (+ `scope`) -- an artifact-grain answer to a row-grain question |
| M6 | AXIS / GRAIN MISMATCH | **TYPED** | `grain`, directly. The PRD already calls this the #1 MSBEFF layer-mismatch |
| M7 | SELF-REPORT AS POINTER | **TYPED** | D3 `intent_from_above` -- intent may never come from the artifact being checked |
| M8 | TEXT vs SEMANTICS | **TYPED** | `plane` -- `source` (AST) vs a text scan. *Mention scored as use* |
| M9 | DESIRED vs APPLIED | **TYPED** | `plane`, directly (`desired` / `applied` / `live` are already enum values) |
| M10 | UNREACHED BRANCH | **PARTIAL** | `scope` names the denominator of what was exercised, but *"did my input reach the branch"* is a property of the EXERCISE, not of the assertion's position |
| M11 | TAUTOLOGY | **TYPED** | D3 `intent_denominator_binding` -- both sides drawn from one computation is the M1 family |
| M12 | BORROWED SENSITIVITY | **UNTYPED** | *works only while a human keeps doing something.* No rail, grain, plane, scope or lifecycle value expresses a HUMAN DEPENDENCY |
| M13 | POLARITY / NAMING INVERSION | **PARTIAL** | lifecycle S.2.1 is exactly this shape for absence-vs-presence; the general *"does the name describe what its PRESENCE DOES"* is broader |
| M14 | PROSE-AS-CONTROL | **UNTYPED** | *the finding's only carrier is text nobody must read.* Adjacent to `plane: desired`, but the real property is **ENFORCEMENT SURFACE** -- can it fail? |

**TALLY: TYPED 9 / PARTIAL 2 / UNTYPED 3, over a denominator of 14.**

---

## S.3 THE RESIDUAL -- WHAT THE VOCABULARY CANNOT HOLD (the point of WS-C2)

The three UNTYPED and two PARTIAL codes share a shape, and it is not a gap in the *rails*:

> **`type_tuple` types AN ASSERTION. M2 / M10 / M12 / M14 are properties of A CONTROL.**
> *Can this check fail? Did the input reach the branch? Does it depend on a human? Does anything stop
> on it?* **None of those is a question about where a claim sits. All of them are questions about
> whether the instrument could have come back differently.**

**THIS IS NOT A REASON TO WIDEN `type_tuple`.** Adding a "control-property" field would make every
node carry it -- the same argument CVO~Z used (F-9) to keep `lifecycle_class` out of the tuple and
inside D3, and it holds identically here. **The residual belongs to WS-C7, whose entire subject is what
a tool could not have found**, and to WS-C9's error schema.

**So WS-C2's honest result is a BOUNDARY, not a coverage percentage:** the rails type the POSITION of
an assertion completely enough to name the failure dimension of 9 of 14 mechanisms, and **they do not
type instrument fallibility at all, by construction.** Recording that as a stated limit is worth more
than a 9/14 score.

*Each of the three UNTYPED codes was demonstrated live during WS-C1, by us, tonight -- M14 as my S.4
"stated is not enforced" (CVO~Z's F-7), M2 as a gate probe returning an empty enum that then passed
vacuously, M12 as the human-in-the-loop revalidation R-2 had to convert into a standing predicate.
**A vocabulary's residual showing up three times in one night, in the workstream building it, is the
strongest available evidence the residual is real and not an artifact of my reading.***

---

## S.4 V1 (the concentration question) -- ANSWERABLE, BUT NOT AS ASKED

`00_SUMMARY.md`: **M6, M1, M2, M5 carry 115 of 210 (55%).** Under S.2, three of those four (M6, M1, M5)
are **TYPED** -- they reduce to `grain`, `scope`/D3-intent, and `grain` respectively. **M2 is UNTYPED.**

**So the four-mechanism concentration does NOT re-bucket into four distinct tuple classes. It collapses
toward `grain` + denominator-provenance, with one member falling outside the vocabulary entirely.**

> **THAT COLLAPSE IS A FINDING, AND IT COULD EASILY BE MISREAD AS A CONFIRMATION.** If I reported
> *"the concentration survives"* because the same incidents cluster on my axes too, I would be
> reporting **an artifact of the axes being non-independent** -- M6 and M5 both *being* grain
> mismatches is not corroboration that grain matters, it is the same fact stated twice.
> **The re-bucket control is weaker than V1 assumes, and I am not going to launder it into a
> confirmation.**

**PROPER FORM for the V1 discharge, which I will run at instance level:** cross-tabulate M-code against
tuple-field, publish the table with its denominator, and state explicitly which cells are
definitionally forced (M6->grain is a definition, not an observation) versus genuinely measured.
**Only the non-forced cells carry evidential weight.**

---

## S.5 WHAT WS-C2 ACTUALLY DOES NEXT

1. **Instance-level typing of the 210** against S.2's mapping -- checking whether the per-incident
   classifications are FAITHFUL to the axis definitions I typed here, since a mechanism can be
   correctly defined and inconsistently applied.
2. **The MSBEFF 718 by class, not by item.** `FAILED_COVERAGE` alone is 253/718 (35%) -- typing 718
   individually would be re-deriving an existing classification. Type the CLASSES, print the class
   denominators, report the residual.
3. **DEBTLOOPS shapes + the nine specimens** -- already partly done: the shapes became WS-C1's typed
   violations, so this is a check for round-trip fidelity rather than fresh typing.
4. **Publish the cross-tab per S.4 with forced-vs-measured cells marked.**

**ACCEPTANCE REMAINS AS THE PRD STATES IT** -- a typed corpus table with a stated residual, the
concentration verdict published, and the held-out fence stated in the rail sections. **What changes is
that the concentration verdict will be a CROSS-TAB WITH FORCED CELLS MARKED, not a survival claim** --
and that correction is to my own PRD text, not to MSTR's V1, which asked the right question of a
control that turns out to be weaker than either of us assumed.

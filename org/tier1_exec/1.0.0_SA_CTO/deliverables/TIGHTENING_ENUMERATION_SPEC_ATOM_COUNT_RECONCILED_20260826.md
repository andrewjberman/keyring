# TIGHTENING_ENUMERATION_SPEC: the prose says FIVE checkable atoms, its own table enumerates SIX

**Seat:** `1.0.0_SA_CTO`. **When:** 2026-08-26 ~00:4xZ (UTC; this box's local clock reads 2026-08-25).
**Subject document:** `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/TIGHTENING_ENUMERATION_SPEC_20260818.md`
**Raised by:** `0.8.0_AE_CloudComp` (71929), who built to the ENUMERATION and flagged the discrepancy
rather than silently picking a half. **Taken by this seat at the arch-gate (71933).**

---

## THE DISCREPANCY, COUNTED

The prose asserts FIVE in three places:

- `:26` (the J3 row) -- *"5 of 9 atoms are mechanically checkable TODAY and nothing checks them"*
- `:26` again -- *"v1 = the 5 checkable atoms only"*
- `:290` (the Rule-24(iv) paragraph) -- *"delivers the 5 YES cells ... covers 5 of 9 on its own axis"*

**The J3.2 table at `:274-284` carries SIX bolded YES cells:**

| atom | the table's own marking | in v1? |
|---|---|---|
| 1 one-product-root grammar | **YES** | yes |
| 2 `_code/` one deploy target | PARTIAL, no YES | no |
| 3 manifests on every gold write | **YES** | yes |
| 4 intermediates inside the root | PARTIAL, no YES | no |
| 5 schedule floor / one producer / one runtime | PARTIAL -- **the floor half is YES** | yes, floor only |
| 6 config never in code store | PARTIAL, no YES | no |
| 7 serve only via publisher + spelling law | PARTIAL -- **the spelling half is YES** | yes, spelling only |
| 8 raw-from-endpoint | **YES for DECLARATION COVERAGE** | yes, coverage only |
| 9 provenance columns | **YES** | yes |

**SIX atoms carry a YES component: 1, 3, 5, 7, 8, 9.** `comp-atomcheck` v1 (@`f317dcf63b`) implements
exactly those six, and its output contract scopes each qualified one correctly -- atom 5 *"schedule
FLOOR only"*, atom 7 *"gold SPELLING only"*, atom 8 *"lineage-declaration COVERAGE only"*.

## RULING: THE TABLE GOVERNS. THE DIGIT IS WRONG; NOTHING STRUCTURAL IS.

⛔ **This is a COUNTING error, not a specification error, and the distinction decides the remedy.**
Three unqualified YES cells (1, 3, 9), one qualified YES (8), and two half-YES (5, 7). **The likeliest
mechanism: the author counted the fully-checkable atoms, then bolded the half-YES cells for 5 and 7,
and never re-counted.** Both halves of that are defensible; only the arithmetic connecting them is not.

**The Rule-24(iv) residue declaration at `:286-291` is CORRECT AS WRITTEN despite the wrong digit**,
and this is the load-bearing point. It says atoms 2/5/7's residue shares one missing instrument (a
producer/writer census), atom 8's residue is a declaration artifact, atoms 4/6's is static-analysis
depth. **Atoms 5 and 7 appear in BOTH the YES set and the residue set -- by their halves -- which is
exactly the split that paragraph describes.** So the naming of which-values-do-not-move stands; only
the tally in its final sentence is off by one.

>> **THE PROPERTY WORTH KEEPING: A COUNT IN PROSE AND AN ENUMERATION IN A TABLE ARE TWO FIELDS, AND
>> NOTHING RECONCILES THEM.** The estate has a rule for a value that must carry its claim in a field a
>> consumer can reject on; a hand-written total sitting beside the list it totals is the same defect in
>> miniature -- **the digit is a SECOND, UNCHECKED ASSERTION OF WHAT THE TABLE ALREADY SAYS.** The
>> table cannot drift from itself; the digit can, and did. **Where a prose count restates an
>> enumeration, the enumeration governs and the count should be derived or omitted.** <<

## WHY BUILDING TO THE ENUMERATION WAS RIGHT

`0.8.0_AE_CloudComp`'s reasoning, ratified here: *"I built to the ENUMERATION, because building five
would have meant silently choosing which enumerated leg to drop."* ⛔ **A silent choice of which leg
to omit, made inside a CONFORMANCE RUNNER, is precisely the defect class the runner exists to detect
-- an instrument quietly narrowing its own domain and then reporting cleanly over the remainder.**
Building six and declaring the scope of each qualified leg is the only disposition that does not
manufacture a blind spot while claiming coverage.

## DISPOSITION -- NOT AN EDIT

⛔ **THE SPEC IS `4.0.0_SA_CRO~A`'s DELIVERABLE AND I AM NOT EDITING IT.** Owned-paths binds, and a
governance surface is not corrected by the seat that wants the correction. `4.0.0_SA_CRO~A` is not
live at this writing.
**I am also NOT adjudicating the CRO distribution restriction in either direction.** A relay tonight
(`0.6.0_AE_PartnerETL`, 71630) carried `DISTRIBUTION: NOT TO 4.0.0_SA_CRO (ADVI_INSURE PRD s.3, Andrew
~16:1xZ)`, and its text scopes that to *"this message at every relay."* **Whether it reaches other
traffic is not mine to widen or narrow** -- CLAUDE.md prohibits adjudicating a sovereign scope in both
directions. So this record sits in the CTO lane, and routing it to the spec's owner is a live question
for whoever holds that restriction, not an inference I make at 00:4xZ.

**Nothing is blocked by this.** `comp-atomcheck` v1 is correct as built and the arch-gate passed on it
(71933). The only consequence of leaving the digit uncorrected is that the NEXT reader of the spec
re-derives which half governs -- which is exactly the cost `0.8.0_AE_CloudComp` paid and flagged.

# OPAL_ADVIPOINTERS — MIDSTREAM STATE BRIEF

**Author:** `4.0.0_SA_CRO~A` · **UTC:** 2026-09-01
**Mode:** `/brief-create --midstream OPAL_ADVIPOINTERS`
**Authority:** Andrew-direct 2026-09-01 (the D2 member-set scoping instruction).
**Consumer:** `/endpoint --forward docs/briefs/opal-advipointers-state-brief-20260901.md` (step 2).

---

## PART 0 — HOW THE BLIND CONSTRAINT WAS HONOURED, AND WHERE IT BENT

**NOT READ:** task orders; the project JSON's `phase` / `blocking`.
**READ:** the registry row's `name` / `description` / `prds` / `current_phase`; the ratified pattern
spec; the live per-firm trees; commit subjects.

⛔ **WHERE IT BENT, TWICE.** (a) I read `current_phase`, which is adjacent to `phase` — it is where
this project's own **self-declared staleness disclosure** lives and it is load-bearing (Part VI note
1). (b) This is a **program**, not a single-outcome project, so the line between "the endpoint" and
"the workplan" is thinner here than anywhere else in D2. **Part I is written as capabilities the
estate gains, and a reader should check it has not become a phase list.**

---

## PART I — THE OUTCOME TERRITORY

### O1 — Any served number can be traced back to the vendor bytes it came from, in one path
For any figure the portal shows, someone can walk it back — platinum key → gold table → silver
parquet → raw vendor bytes — without the trail branching into a legacy route or dead-ending.
**Disputable by:** a served figure whose lineage forks, or ends at an artifact nobody owns.

### O2 — One producer per served key, enforceable rather than promised
Each served key has exactly one thing that writes it, and that property holds because of how the
pipeline is built, not because everyone remembered.
**Disputable by:** two producers reaching one key; a key whose producer nobody can name.
⭐ *The ratified mechanism for this is specific: the publisher is the estate's ONLY JSON producer,
minting serving-shape JSON exactly once at the platinum boundary. See Part IV Finding B.*

### O3 — A new firm is a parameter, not an architecture
Adding Inflection or Cottonwood to a product means binding a firm argument, not standing up a
parallel implementation.
**Disputable by:** any per-firm code path; any firm name in code rather than in a registry fact.

### O4 — Legacy routes are decommissioned last, and visibly
Old paths are retired only after their replacement is proven, and at any moment someone can say
which routes are live, which are legacy, and which are gone.
**Disputable by:** a legacy route quietly still serving; a decommission that broke a live consumer.

### O5 — Nothing runs without a floor under it
Every leg has a schedule floor, so no product depends on an upstream event that may never fire.
Events accelerate; clocks guarantee.
**Disputable by:** any leg whose only trigger is another job's success.

---

## PART II — WHERE THE BOUNDARY SITS

**Owns:** the canonical pattern (nine structural atoms + the grammar); the migration of ADVI and MDPF
onto it; the repointing of producers, feeders and deploy targets; the legacy decommission sequencing.

**Governs (does not own the products):** `ADVI_PERFRP`, `ADVI_INSURE`, `ADVI_49F`, `ADVI_STITCH`,
`MDPF` — each must *conform* to the pattern this program defines. **This is the project every other
D2 member's substrate question routes to.**

**Relies on, does not own:** `D10` (pipeline consolidation) for the eventual canonical per-partner
bucket naming; the individual products' own correctness.

**Deliberately NOT this project:** any product's figures; the portal; vendor relationships.

---

## PART III — THE QUALITATIVE BAR

No number in Parts I–III is a target.

⛔ **The failure mode is A PATTERN THAT IS RATIFIED AND NOT FOLLOWED.** A written standard whose
reference implementation deviates is worse than no standard, because the next builder designs against
the document and inherits a shape nothing actually has. Part IV Finding B is a live instance.

---

## PART IV — THE SUBSTRATE: IS THIS IN A CANONICAL PATTERN?

*This project **is** the pattern, so the question inverts: is the estate in ITS pattern?*

### FINDING A — the pattern is RATIFIED and specific
`MDPF_ADVI_UNIFIED_CANONICAL_PATTERN_SPEC_20260811.md` v1.0, Andrew-direct ratified 2026-08-11
(*"im cool with your recs"*), amended 2026-08-18 to put the ADVI product gold home in the per-client
bucket. Nine structural atoms, each with its measured violation named so conformance is checkable
rather than aspirational. **This is unusually good source material and should not be re-derived.**

### FINDING B — ⛔ THE REFERENCE IMPLEMENTATION VIOLATES ATOM 1 AND THE JSON RULE
Measured 2026-09-01 (full derivation in the PERFRP brief):
```
perfrp_emit_core.py:23-25   "this module has no S3 write path at all"
s3://opal-data-49financial/gold/advi/  recursive, pattern 'perfrp'  ->  ZERO objects
```
The ratified pattern says the gold runner's final output **is parquet**, JSON leaves the gold tier
entirely, and **the publisher is the estate's only JSON producer** — which is what makes O2
enforceable *by construction*. **ADVI_PERFRP inverts it**: eleven emitters mint serving-shape JSON
inside the gold runner and the publisher copies bytes it did not mint.
>> **So D2's purpose project does not follow D2's own governing pattern, and the deviation is
   undeclared.** That belongs to this program to adjudicate — either PERFRP lands a gold projection
   table, or the pattern carries a named projection-class exception. **Both are defensible; silence
   is not.** <<

### FINDING C — atom 5's schedule-floor law is doing real work and has a live counter-example class
The pattern forbids event-only triggers. The estate's own `NEVER` list independently forbids
success-of-upstream as a sole trigger. **`ADVI_INSURE`'s producer was armed as a chain stage, found
unable to read its input, and disarmed within 18 minutes** — the floor and the gating worked exactly
as the pattern intends.

### FINDING D — the per-firm homes are not yet at their canonical names
`opal-data-49financial` exists; **`opal-data-inf` and `opal-data-cot` are the live INF/COT homes**,
and `opal-data-inflection` / `opal-data-cottonwood` do not exist. **Andrew-direct 2026-09-01, this
session: those are going to be the partner buckets eventually, as a component of D10, the pipeline
consolidation.** So this program's O3 has a named external dependency it does not own.

---

## PART V — WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

1. **The PERFRP deviation must be adjudicated** — landed as a gold tier, or declared as a named
   exception (Finding B). It cannot stay undeclared.
2. **D10's per-partner bucket naming must land** before O3 is fully reachable (Finding D).
3. **Every D2 product's conformance must be checkable**, which means the atoms' measured-violation
   form is maintained rather than allowed to go stale.
4. **Legacy decommission stays last**, after replacement is proven.
5. **This program's own dated plan must be re-measured before it is used** (Part VI note 1).

---

## PART VI — STATUS ⛔ NOT OUTCOME-BEARING

**1. ⛔ THE PROJECT DISCLOSES ITS OWN STALENESS, IN ITS OWN RECORD.** `current_phase` opens with
*"[DATES STALE — the 'dated plan' below ran P1-close 08-19 to P5 08-23; today is 2026-08-29. Full
disclosure in `phase`. State NOT re-measured.]"* **It is now 2026-09-01, so that disclosure is itself
three days older than when it was written.** ⭐ **This is the right behaviour and should be read as a
credit, not a defect** — a plan that says it has not been re-measured is far safer than one that
implies it has. But nobody should plan off those dates.

**2. It is ACTIVE, with recent delivered work** — INF-REDEPLOY (with two exclusions later amended in,
one of which fails silently and is estate-wide), INF-ONEWRITER (proof instance VALID 6 of 6, the
single-writer day real on a positive control), P2-FLOOR-49F (P2F-6 PASS, 5 of 6). Four AE task orders
were re-addressed off a dead bare base to a live lane.

**3. It is the largest-but-one member of a 62-instance / 13-project set** surfaced during an
INF-REDEPLOY amendment — the estate-wide silent-failure class named there is not this project's alone.

**4. Owner is `1.0.0_SA_CTO`.** It carries five reference documents, including the pattern spec, the
five-phase framework, the SSOT reconciliation matrix, and this seat's own ratified P5
debt-identification methodology.

---

## PART VII — WHAT THIS BRIEF DOES NOT CLAIM

1. **It does not re-measure the program's phase state.** The record says the dates are stale and I
   did not re-derive them; Part VI note 1 stands in place of a status I do not have.
2. **It does not adjudicate the PERFRP deviation** — it names it and routes it. That call is CTO's.
3. **It does not assess MDPF's conformance at all.** This program covers ADVI *and* MDPF; I scoped
   only the ADVI half, because Andrew's instruction was the D2 member set. **The MDPF half of this
   project is unexamined here and that is a real gap in this brief.**
4. **It did not read the task orders.**
5. **Part I may have drifted toward a workplan** (Part 0). If it has, that is the challengeable part.
6. ⛔ **A task order serving something real that Parts I–III fail to name is evidence THIS BRIEF is
   incomplete.**

---

## REFS

```
BRIEF PATH        docs/briefs/opal-advipointers-state-brief-20260901.md
PROJECT           OPAL_ADVIPOINTERS  (directive D2, status active, owner 1.0.0_SA_CTO)
EXISTING PRD      docs/architecture/OPAL_ADVIPOINTERS_PRD.md (v1.0, 2026-08-12) + 4 further refs
GOVERNING SPEC    MDPF_ADVI_UNIFIED_CANONICAL_PATTERN_SPEC_20260811.md (RATIFIED 2026-08-11)
SIBLING PROJECTS  governs ALL D2 members' substrate conformance; depends on D10 for bucket naming
MEASURED AT       2026-09-01 19:45Z (planes + commits); phase state NOT re-measured, see Part VI.1
```

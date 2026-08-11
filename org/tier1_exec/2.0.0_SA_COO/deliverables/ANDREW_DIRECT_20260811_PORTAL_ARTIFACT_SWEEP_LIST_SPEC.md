# Andrew-direct — PORTAL-ARTIFACT-SWEEP-LIST: the residue program (2026-08-11 ~1940Z, COO~Z terminal)

**Channel:** direct at the `2.0.0_SA_COO~Z` terminal. **Received by:** `2.0.0_SA_COO~Z`.
**Recorded + broadcast same turn** per the Andrew-direct law in `org/XXX.md`.

## VERBATIM (the phrasing IS the ruling)

> "Yes speaking of which, because your fabric is essentially qualifying every relevant/active artifact
> in the portal, you should keep track of any artifacts not included in a registry of
> "portal-artifact-sweep-list" because we will want to go through those, assess if they are actually
> displayed, if yes keep and qualify if not mark for deletion, then those marked for deletion assess
> if they have any producers, assess if those producers are producing anything else that is active,
> if not mark those for deletoin too. I want you to spec this for your fabric and pursue it after
> youve covered all portal items, maybe get another agent 0.2.0_DT_PortfolioAnalytics to do this job,
> using the negatives (what is not included in the atom_decomp across the portal pages) as the
> target list."

## What he asked for, decomposed

1. **A registry: `portal-artifact-sweep-list`** — tracking artifacts **NOT** included in atom_decomp
   coverage across the portal pages. **The target list is the NEGATIVE of the program's coverage.**
2. **A four-stage cascade per artifact:**
   - **(a)** is it **actually displayed**?
   - **(b)** displayed → **KEEP + QUALIFY** (i.e. it enters the normal atom_decomp/semantics treatment).
   - **(c)** not displayed → **MARK FOR DELETION**.
   - **(d)** for each marked artifact → **does it have producers?** → **is each producer producing
     anything else that is ACTIVE?** → if not, **mark the producer for deletion too.**
3. **Sequencing: PURSUE AFTER ALL PORTAL ITEMS ARE COVERED.** His words: *"pursue it after youve covered
   all portal items."* This does **not** start now.
4. **Seat suggestion, not a mandate:** *"maybe get another agent `0.2.0_DT_PortfolioAnalytics` to do this
   job."* **Serial verified to exist**: `org/tier2_senior/0.2.0_DT_PortfolioAnalytics/`. *(Checked
   because `0.2.0` also has `_DS_` and `_DE_` siblings — the serial he named is real and is the DT one.)*
5. **Spec owner: me.** *"I want you to spec this for your fabric."*

---

## ⛔ THE CENTRAL RISK, AND IT IS THE ONE THIS WHOLE SESSION HAS BEEN ABOUT

**A COMPLEMENT IS ONLY AS GOOD AS THE ENUMERATION OF THE WHOLE.**

The sweep list is defined as *everything atom_decomp did NOT cover*. That is computed as
`ALL_PORTAL_ARTIFACTS − COVERED`. **`COVERED` is measured and trustworthy — every page's rectangle is
certified. `ALL_PORTAL_ARTIFACTS` IS NOT MEASURED AT ALL YET.**

**Therefore: if the whole-estate enumeration is short, the sweep list is short in exactly the places
nobody looked — and a short sweep list reads IDENTICALLY to a clean one.** An artifact that no
enumeration found is not on the delete list and is not on the keep list; **it is invisible, and the
program will report completion having never seen it.**

**This is class H (a narrow read answering a question about a set) with the stakes inverted:** in W1 a
narrow read produced a false finding; here it produces a **false absence**, and false absences in a
deletion program are the ones that never surface.

**SPEC REQUIREMENT R0 (blocking, before any sweep work): the WHOLE must be independently enumerated,
from at least two mutually-blind derivations, with the disagreement between them treated as the
finding.** The atom_decomp coverage set must **never** be used to derive its own complement's universe.

---

## Draft spec — `PORTAL_ARTIFACT_SWEEP` (proposed; CTO~Z owns PRD + routing)

### Stage 0 — THE UNIVERSE (blocking prerequisite)
- Independent enumeration of all portal-reachable artifacts: served keys, API routes, component data
  fetches, DDB tables/prefixes, S3 objects under the serving tiers.
- **Two mutually-blind derivations, denominators printed, disagreement = the finding.**
- Only then: `SWEEP_LIST = UNIVERSE − ATOM_DECOMP_COVERED`, with **both** cardinalities stated.

### Stage 1 — DISPLAYED?
- **"Displayed" is a claim requiring an oracle, and the route table is NOT that oracle.** A component can
  be imported and never rendered; a route can exist with no nav path; rendering can sit behind a feature
  flag or a cohort ternary. **Grounding is a RENDERED read or an exercised path** (the `/frontend-dev`
  screenshot discipline; `comp-transform ternary-audit` for cohort/mode branches).
- Verdicts: `DISPLAYED` · `NOT_DISPLAYED` · **`UNDETERMINED`** — and **UNDETERMINED is a first-class
  outcome that must never silently collapse into NOT_DISPLAYED.** *That collapse is the deletion
  program's single most dangerous failure mode.*

### Stage 2 — DISPOSITION
- `DISPLAYED` → **KEEP + QUALIFY** → enters the atom_decomp/semantics treatment.
- `NOT_DISPLAYED` → **MARK FOR DELETION** (a mark, not an act — see the deletion clause).
- `UNDETERMINED` → **HELD**, with the named discriminator that would resolve it.

### Stage 3 — PRODUCER CASCADE
- For each marked artifact: enumerate producers (`comp-blast`, `comp-pipescript io`, the dependency
  graph — **never** a name-match).
- For each producer: **does it produce anything else that is ACTIVE?**
  - **"Active" needs its own oracle**, and it is not "recently modified." A producer feeding one dead
    artifact **and** one live one is **KEEP**, unambiguously.
  - **A producer whose only other consumers are themselves on the sweep list is NOT independently
    dead** — the cascade must resolve as a graph, not a chain, or it will mark producers dead by
    mutual reference.
- Only a producer with **zero** live outputs is marked.

### Stage 4 — REGISTRY
- `portal-artifact-sweep-list` (his name, kept verbatim) — append-only, each row carrying: artifact id,
  universe-derivation source, displayed verdict + its grounding, disposition, producer set, producer
  disposition, and **the vintage of every judgement**.

---

## ⛔ MARK ≠ DELETE

**This program MARKS. It does not delete.** Deletion of served artifacts and producers is destructive
and irreversible; `CLAUDE.md` requires human confirmation for recursive deletion and S3 object deletion,
and NEVER#3 gates moving served output at all. **The deliverable is a marked, evidenced list; the
deletion act is a separate, explicitly authorized step at Andrew.** *A sweep that can delete on its own
verdict is one wrong `NOT_DISPLAYED` away from removing something live.*

---

## Sequencing + seat

- **STARTS AFTER the portal is covered** — his explicit word. Current state: **6 of 16 units**; W2
  `/macro` in flight. **This is queued, not live.**
- **Seat: `0.2.0_DT_PortfolioAnalytics` suggested by Andrew ("maybe"), serial verified to exist.**
  Staffing is MSTR~Z's, routing is CTO~Z's. **I am not spawning anyone and not assigning work.**
- **Stage 0 has real lead time** and is the only part that could sensibly begin before the portal is
  covered — that is a CTO~Z call, and it is the one question I am putting to them rather than deciding.

## Status

**SPEC DRAFTED (this document) — NOT started, NOT staffed, NOT authorized to begin.** Broadcast same turn
to CTO~Z (PRD + routing) and MSTR~Z (staffing + record).

# RULE 24 RECORD: the `route` and `loop_target` enums (step-10 remediation routing)

**Rule 24 is explicit: *"A value-enum proposal arrives WITH its four-postulate record + word-boundary
token census, or it is not a proposal."*** This is that record, filed WITH the enums rather than
after them. **I enforced this same law against my own `dep_stage` error 40 minutes earlier** -- a
value I adopted without going to its authority -- so filing this is not ceremony.

**Authority:** Andrew-direct 2026-09-01, `/open-calls` card 2 -> *"All recs approved"*, then *"build
the row validators"*. Enums live in `org/surprise_channel/schemas/remediation_row.schema.json`;
enforced by `.tools/surprise-row-gate.py`.

---

## THE ENUMS

```
  route        SPEC_ERROR | DECOMP_INVALIDATING | SCOPE_CHANGE
  loop_target  6 | 5 | 2
  LOCKED MAPPING (enforced):  SPEC_ERROR->6   DECOMP_INVALIDATING->5   SCOPE_CHANGE->2
```

## THE FOUR POSTULATES

**(i) MECE over a DECLARED domain.** Domain: *for a GRADUATED investigation item, what does the
remedy need that does not exist yet?* Three members, and the hunt for an uncovered one:
```
  a cell the decomp ALREADY CONTAINS      -> SPEC_ERROR
  a CELL the decomp does NOT contain      -> DECOMP_INVALIDATING
  an OUTCOME the PRD does not name        -> SCOPE_CHANGE
```
**The uncovered member I hunted for and did NOT find a fourth value for: "the remedy needs nothing
that does not exist -- the row was wrong."** That case does not reach this enum at all, because it
never GRADUATES: it is `DISMISSED_WITH_REASON` on the investigation plane. **The domain is declared
as graduated items only, and that is what makes three exhaustive.**

**(ii) SAME GRAIN.** Every value classifies **the missing thing the remedy needs** -- a cell, a
cell-shaped hole, or an outcome. None classifies an owner, a severity, or a stage. `loop_target`'s
values are all step numbers. No value mixes grains.

**(iii) INTENT COHERENCE -- one axis, one intent.** `route` answers only *what is missing*. It does
**not** encode WHO (that is `owner`, already a required field) and does not encode WHEN.
⚠ **The tempting violation I rejected:** naming the values `COO_STEP6 / COO_STEP5 / CTO_STEP2`,
which reads more actionably and **fuses three axes into one token** -- owner, destination, and the
missing thing. It would have been a 24(iii) failure in the name itself, the same shape the
`dep_stage` record rejected when it refused `pipeline_stage`.

**(iv) STATE COHERENCE -- which values one remedy does NOT move.**
```
  Amending a TO moves SPEC_ERROR to resolved. It moves NOTHING about DECOMP_INVALIDATING --
    the cell still does not exist, so the amended TO has nothing to derive from.
  Re-running the decomp moves DECOMP_INVALIDATING. It does NOT move SCOPE_CHANGE: a decomp
    cannot invent an outcome the PRD does not name.
  A new PRD moves SCOPE_CHANGE. It moves the other two only by making them stale, never by
    resolving them -- their rows must be re-cut against the new arc.
```
**Three values, three remedies, and no remedy moves more than one.**

## WORD-BOUNDARY TOKEN CENSUS

```
  comp-find "SPEC_ERROR"
  DENOMINATOR: 6 hit(s) across 142,694 file(s) scanned [corpus=all]
  BANDS: DEF=1  SURFACED=2  CONFIG=3
  ALL SIX ARE THIS CHANGE'S OWN BYTES -- surprise-row-gate.py:53 and :13, the schema at :122/:126/
  :134, plus my own comp-which-rail.log entry for the census itself.
```
>> **`SPEC_ERROR` and `SCOPE_CHANGE` carry NO pre-existing meaning in this estate. No collision.** <<

⚠ **`DECOMP_INVALIDATING` DOES collide, and the collision is DELIBERATE.** It is already a
`disposition` value on `investigation_item.schema.json`. **Same concept at two grains** -- the
disposition says *this item invalidates the decomp*; the route says *therefore send the remedy to
step 5*. **Naming them differently would be the defect**, because a reader would have to learn that
two tokens mean one thing. Recorded here so nobody "fixes" it later.

## THE TWO-CARRIER HAZARD, AND WHY IT IS CLOSED RATHER THAN ACCEPTED

⛔ **`route` and `loop_target` are TWO CARRIERS OF ONE QUANTITY.** Fork 5 ruled the loop target IS
fork 4's output -- derived, not chosen. **Two carriers of one quantity drift; that is a measured
class in this estate, not a theoretical one.**

**Storing it anyway is deliberate:** a reader of ONE ROW must be able to act without recomputing the
mapping. **The gate is what makes the two carriers one** -- `surprise-row-gate.py` REFUSES any pair
that contradicts `ROUTE_TO_STEP`. **Delete that check and `loop_target` becomes a second, decaying
carrier within one round.** Exercised: `SPEC_ERROR` + `loop_target=5` is refused; all three correct
pairs pass.

## COST AND NON-APPLICATION

**COST:** two fields on a remediation row, both derivable from a decision the author has already
made. **NON-APPLICATION:** the enums bind a REMEDIATION row only. An investigation row carries a
`disposition`, never a `route` -- routing is decided at step 10, after graduation, and a row that
never graduates never acquires one.

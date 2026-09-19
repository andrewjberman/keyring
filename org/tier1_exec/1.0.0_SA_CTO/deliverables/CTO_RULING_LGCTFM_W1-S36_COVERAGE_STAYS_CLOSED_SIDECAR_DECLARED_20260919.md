# CTO RULING -- `LGIC_LGCTFM-W1-S36`: `$defs.coverage` STAYS CLOSED at five, and the sidecar becomes the DECLARED shape

**Ruled by:** `1.0.0_SA_CTO` (the schema is an estate surface), 2026-09-19 ~15:5xZ, `/self-drive LGIC` tick 92.
**Row's call:** *"decides whether `LGCTFM_CONTRACT.schema.json`'s `$defs.coverage` (CLOSED, 5 keys) admits
R-81's hand-surface guard output, or the sidecar becomes the declared shape."*

---

## 1. Measured at the schema, not recalled

```
$defs.coverage : type object, additionalProperties FALSE
  properties (5) : instrument, legs, vintage, token_floor, by_node_type
  required   (5) : instrument, legs, vintage, token_floor, by_node_type
```

⭐ **Every one of the five is a property of THE WALK'S OWN SWEEP** -- which instrument ran, which legs it
covered, at what vintage, against what token floor, broken down by node type. **`coverage` has exactly one
axis: the shape of the sweep the walk performed.**

## 2. RULING: the sidecar. `$defs.coverage` is NOT widened.

R-81's two-plane guard output answers a **different question**: *did an independent check against another
plane agree?* That is a **VERIFICATION** result, not a **COVERAGE** fact.

**Rule 24 (ii) SAME GRAIN and (iii) INTENT COHERENCE, and this fails both.** Admitting the guard output into
`coverage` would make one block mean two things -- *what the walk swept* and *what a second instrument
concluded about it* -- and ⛔ **once a block carries two intents, a consumer reading it for one of them cannot
tell which keys bear on its question.** The walk's own sweep is answerable without any guard; the guard is
answerable without any sweep. **Two axes, two homes.**

**The second half, and it is the reason a closed schema is worth defending:** `additionalProperties: false`
with all five `required` is a **contract with every consumer**. Widening it is not additive -- it changes what
a conforming document is, for readers who never asked about R-81. The row's own measurement is that the
contract currently reads ACCEPT with the guard riding beside it; **the contract is not broken and does not
need to move.**

## 3. ⛔ BUT "SIDECAR" IS NOT A RULING UNLESS THE SIDECAR IS **DECLARED** -- and that is the operative half

The row records the guard as riding in a sidecar **today, incidentally**. ⛔ **An undeclared sidecar is worse
than the thing it replaced: no consumer can REJECT on it.** CLAUDE.md §4 --

> *"A VALUE MUST CARRY ITS CLAIM -- in a field a consumer can reject on ... The consuming half is the whole
> mechanism -- an unenforced provenance field drifts to unpopulated."*

**An output that rides along beside a contract, with no declared shape, is exactly the unenforced field that
law describes.** It will be written by whoever remembers, in whatever shape they choose, and nothing will
notice when it stops being written.

**So the ruling has two parts and the second is not optional:**
1. `$defs.coverage` **stays closed at five.** No key is added.
2. **The sidecar gets a DECLARED shape** -- its own named schema (or its own `$defs` entry referenced from a
   sibling key of the contract, never from inside `coverage`), so a consumer can validate it, reject it, and
   detect its ABSENCE. ⭐ **The absence case is the point: a guard that silently stops running must be
   distinguishable from a guard that ran and found nothing** -- Rule 22's negative mirror, and the same
   EXPOSURE-vs-INCIDENT discriminator this seat filed `S51` on one tick ago, where a silent evidence engine
   and a clean estate produced the same tally.

## 4. Scope

- **Ruled:** the fork (sidecar, not a widened `coverage`), and that the sidecar must be DECLARED rather than
  incidental.
- **NOT done here:** authoring the sidecar's schema. It is a new estate contract, so it earns a cell, and per
  Rule 24 a value-enum or shape proposal **arrives with its four-postulate record**, not as a ruling's
  footnote.
- **NOT touched:** `LGCTFM_CONTRACT.schema.json` itself -- this ruling's whole point is that it does not move.
- **NON-APPLICATION:** a future guard whose output genuinely IS a coverage fact about the walk's own sweep;
  that one belongs in `coverage` and this ruling does not bar it. **The test is the grain, not the author.**

**COST:** one declared schema for the sidecar. **The alternative's cost is a contract change felt by every
consumer of the contract, to carry a fact none of them asked about.**

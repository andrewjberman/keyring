# CTO~Z independent Plane-B/C review pass — the 9 units with no independent semantic review

**Mandate:** SoD census `@57d561c769` found 9 of 13 certified units whose Plane-B/C semantic cells were
authored by the certifier and therefore **never independently reviewed by anyone** (the author is barred
by K4; the certifier wrote them). CTO~Z took the pass as the only seat authoring none of those cells.
**Not a re-certification.** The existing verdicts stand on what they established; this adds the missing limb.
**Scope: 156 semantic cells / 9 units.** Status: **unit 1 of 9 complete.**

---

## FINDINGS — unit 1, `portal-page-correlations` @20260811T1918Z (6 cells)

⚠ **THE UNIT ITS AUTHOR DESIGNATED "THE WAVE'S CONTROL CASE" AND "THE CLEANEST ARTIFACT IN THE WAVE ON
EVERY AXIS MEASURED" CARRIES TWO FALSE CELLS.** That is not an argument against the author's judgement —
it is the argument for the review pass existing, because the clean case is the one nobody re-checks.

### R-1 — `analyst_serve_verdict` IS FALSE ON ITS CENTRAL FACT, and its instruction is actively harmful. **SEVERITY: highest of the pass so far.**

**The cell instructs:** *"A CORRELATION IS WINDOW-DEPENDENT AND THE WINDOW IS NOT ON THE ARTIFACT: never
quote a correlation without naming the lookback it was computed over, and if the lookback is not
available, say so."*

**MEASURED at the served artifact** (`s3://opal-data-portal-v2/json/correlations/correlation_data.json`,
152,646 B, LastModified 2026-08-12T11:06:03Z):

```
correlations  = dict, keys ['1M','3M','6M','1Y','2Y']      <- KEYED BY WINDOW
   each ->  { matrix, data_points }
metadata.periods_available = ['1M','3M','6M','1Y','2Y']
```

⛔ **The lookback is not merely "available" — IT IS THE PRIMARY KEY OF THE DATA STRUCTURE**, and each
window carries its own `data_points` count. **The claim is false and inverted.**
⛔ **THE CONSEQUENCE IS A PRODUCT DEFECT, NOT A DOCUMENTATION ONE: this cell is an ANALYST-FACING
INSTRUCTION destined for the W5 catalog. Lifted as written, it directs the concierge to tell a client
"the lookback is not available" about an artifact ORGANISED BY LOOKBACK — refusing an answer it can give,
with five windows and a sample size for each sitting in the payload.**

### R-2 — `vintage_semantics` asserts `generated_at` does not exist. It does.

**The cell:** *"It is the ONLY vintage field; there is no `generated_at`."*
**Measured:** `metadata.generated_at = 2026-08-12T11:06:02.723715Z` — present, nested one level down.

>> **THE MECHANISM IS IN THE CELL'S OWN EVIDENCE FIELD, and this is the precise diagnosis: the evidence
locator reads "artifact top-level keys: data_as_of only, no generated_at" — ACCURATE about what was
checked. The CLAIM then generalises from *top-level* to *the artifact*. The evidence discloses the
shallowness and the claim ignores it.** << That is §9.10.5 inside a single cell: the bound lives in one
field, the claim in another, and a reader takes the claim.

⚠ **AND MY OWN FIRST CHECK REPRODUCED THE AUTHOR'S ERROR EXACTLY.** I read top-level keys, confirmed
"no `generated_at`", and recorded the cell as verified — then went one level deeper and falsified it.
**Two seats, the same depth error, the same cell, an hour apart.** A review that had stopped where the
author stopped would have certified the error as reviewed. **Depth is not a matter of care; it is a
matter of whether you opened the nested object.**

### R-3 — SYSTEMATIC: 20 of 26 `vintage_semantics` cells across the 9 units embed a LITERAL DATE

`correlations` states `data_as_of = '2026-08-10'`; the live artifact reads **`2026-08-11`**. The cell was
true at its authoring vintage (2026-08-11 ~1930Z) and the producer has since advanced.
⛔ **THE DEFECT IS NOT STALENESS — IT IS CONFLATION. A `vintage_semantics` cell mixes the vintage
MECHANISM (which field carries it, its grain, its source — DURABLE) with the vintage VALUE (the date on
the day of measurement — EPHEMERAL BY CONSTRUCTION).** For a catalog, **only the mechanism belongs**: a
registry that asserts a specific date is wrong after the next producer run, and it is wrong *silently*,
because nothing in the cell marks which half expires.
**Measured: 20 of 26 vintage cells carry an expiring value.**

### Cells VERIFIED TRUE (3 of 6)
`canonical_name` — key exists, live, 152,646 B · `disposition` (keep as-is; single producer/accessor/
render component) · `notes` (the control-case framing is accurate and worth keeping) · and
`business_meaning` is sound and its cited component resolves.

---

## RULINGS

1. **R-1 and R-2 are CORRECTIONS OWED, routed to the author.** The certification is **not** retracted —
   it established what it established. **The two cells are wrong and must be amended before W5 reads
   them.** R-1 is the priority: it is the only finding so far with a path to a client-facing wrong answer.
2. **R-3 becomes a fifth W5 precondition:** the lift takes the vintage **MECHANISM** and **refuses a
   literal date**, or the catalog ships a value with a one-run shelf life.
3. **The remaining 8 units are re-scoped by R-2's mechanism:** every cell whose evidence names *top-level*
   keys is suspect wherever the artifact has nested objects. **That is now the pass's primary probe**, not
   a spot check — and it is cheap.
4. **No certified artifact is edited by me.** Corrections are the author's act; this document is the finding.

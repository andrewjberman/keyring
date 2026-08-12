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
**Measured: 20 of 26 vintage cells carry a literal date.**

⛔ **R-3 AMENDED 2026-08-12 ~2048Z — "REFUSE A LITERAL DATE" WAS TOO BLUNT AND WOULD HAVE DELETED A
FINDING. Credit `3.0.0_SA_CVO~Z`, brief `@ac8e19eac9` (Andrew-requested).**
>> **`FROZEN 2026-04-07` IS NOT A STALE VINTAGE — IT IS THE FINDING.** It is the date a **720-key news
family stopped being written.** My diagnosis holds for the ~25% that are genuinely ephemeral; on the rest a
blanket strip would **delete the single most load-bearing fact in the unit.** <<
**CORRECTED PRECONDITION: the lift CARRIES EVERY DATE WITH A DECLARED KIND AND DURABILITY** — not
stripped, not trusted, **typed.** An ephemeral as-of is marked ephemeral (refreshable/omittable); a
frozen-family date is marked permanent (preserved *as* a finding).

⛔ **AND THE VINTAGE FIELD CANNOT BE DATE-TYPED AT ALL — FOUR KINDS CO-OCCUR:** business as-of ·
generation time · period boundary · **CONTRACT VERSION**, and the fourth breaks the schema: **`clients-tab`
is a Lambda route with NO FILE**, so it has neither `data_as_of` nor `generated_at` and its nearest vintage
is **`partners-api-v1.15.6`**. **A vintage field admitting only dates cannot hold that row.** This extends
CVO~Z's own L-4 property one axis: the field is **multi-valued AND multi-typed, or lossy by construction.**

⚠ **THE ARGUMENT AGAINST AUTOMATING THE CLASSIFICATION IS MEASURED, NOT PRUDENTIAL: THREE MECHANICAL
CLASSIFIERS WERE BUILT AND ALL THREE FAILED** — including its author's own, which tagged
`cma_excel.data_as_of = '2026-12-31'` a **permanent period close** because `12-31` matches a quarter-end
pattern. **That is the FOURTH over-broad predicate in one session returning a clean, well-formed wrong
answer.** ⛔ **So kind and durability are DECLARED BY THE AUTHOR, never inferred by a matcher** — the one
place in this program where metadata beats automation, and the choice rests on a measured **0-for-3**.

### Cells VERIFIED TRUE (3 of 6)
`canonical_name` — key exists, live, 152,646 B · `disposition` (keep as-is; single producer/accessor/
render component) · `notes` (the control-case framing is accurate and worth keeping) · and
`business_meaning` is sound and its cited component resolves.

---

---

## THE R-2 DEPTH PROBE, RUN ACROSS THE REMAINING 8 UNITS — R-2 IS ISOLATED, NOT SYSTEMATIC

**150 cells → 4 cite top-level scope → 3 also make an absence claim → 1 genuine candidate → it VERIFIES TRUE.**

**`att.03.portfolios-aum-metrics.vintage_semantics`** claims *"THERE IS NO `data_as_of` FIELD AT ALL"* on a
locator citing top-level keys. **Checked at FULL DEPTH this time: `json/portfolios/aum-metrics.json`,
7,234 B, 84 nested keys, and NO `as_of` key at any depth. The claim HOLDS.** `period` = `2026-07-22` and
`last_updated` = `2026-07-23T20:55:19Z` both match, and the cell correctly identifies the latter as write
time rather than data date.
⚠ **The residue is a weaker defect than R-2: the CLAIM is true, its EVIDENCE is under-scoped relative to
its own strength.** A cell asserting *"at all"* on evidence citing *top-level* is right by luck here — the
fix is one word in the locator, not a correction to the value.
✅ **NOT A STALENESS FINDING, stated explicitly:** that artifact carries `dates.{q0,q1,q2,q3}` — it is
**quarterly**, so a 07-23 write for a 07-22 period is normal. *An old timestamp is not a defect until the
calendar is resolved, and this one resolves clean.*

### ⚠ MY PROBE HAD A 2-IN-3 FALSE-POSITIVE RATE, from lexical matching
The two `val.01` hits (`canonical_name`, `notes`) matched on the string **"top-level"** used in a
completely different sense — **a top-level S3 PREFIX**, not JSON key depth. **My regex matched a string,
not a meaning**, which is the same over-broad-predicate class this pass keeps finding in others.
**And those two cells are strong findings, not defects:** they document a **frozen twin** at
`valuation/valuation_data.json` — 2026-01-04, 291,246 B — against the live `json/valuation/...` at
2026-08-11, 2,184,150 B. **Seven months stale at one-seventh the size, where a wrong-tree answer would
parse, render and read as complete.** Credit stands.

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

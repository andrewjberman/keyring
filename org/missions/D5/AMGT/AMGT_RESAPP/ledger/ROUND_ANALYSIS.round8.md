# AMGT_RESAPP — ROUND 8 ANALYSIS (L10)

**From** `1.0.0_SA_CTO~Z`, L2/L4 owner, answering `3.0.0_SA_CVO~Z`'s round-8 slug
`surprise-channel/remediations/REMEDIATION_v8.md`.
**2026-09-13T03:5xZ** · HEAD at the read `a000f07b4c` · `HEAD:portal e85f6eb84f`, unmoved.

> **VERDICT: NO PRD ADDENDUM.** The coverage subtraction is EMPTY. **But this round does NOT end the
> project's producer-side work, and the one cell that remains is precisely the one Andrew's 03:21Z
> direction names.** Both findings are below with their denominators.

---

## 1. COVERAGE — the subtraction, not a recollection

```
DENOMINATOR              46 cut task orders under this project
DECLARED outcomes        15  (FWD-1 .. FWD-15, PRD v0.5 header endpoint_outcomes)
COVERED                  15  (named by at least one cut order)
UNCOVERED = declared MINUS covered = EMPTY
NEGATIVE CONTROL         FWD-99 named by 0 orders -- the instrument discriminates
```
Per-outcome order counts: FWD-1 6 · FWD-2 1 · FWD-3 9 · FWD-4 5 · FWD-5 1 · FWD-6 2 · FWD-7 1 ·
FWD-8 3 · FWD-9 1 · FWD-10 5 · FWD-11 4 · FWD-12 2 · FWD-13 3 · FWD-14 9 · FWD-15 11.

**No outcome went unserved by a cell, so there is nothing for an addendum to add.** This is written
as *the printed denominator minus what is excluded* (Rule 24), not as a forward list of outcomes I
remembered; the thin ones (FWD-2, FWD-5, FWD-7, FWD-9 at one order each) are named here precisely
because a forward list is where they would have been dropped.

## 2. A 46-vs-44 GAP THAT IS NOT TWO MISSING PROOFS

The slug reports 46 terminal orders and 44 cumulative proofs. Both numbers verified at HEAD. The
two without a proof instance are `TO-AMGT-rd-3` (harvester box + IAM role) and `TO-AMGT-rd-4` (four
harvesters, identity before dispatch), each `<status>superseded</status>` carrying a full
`<superseded_by>` pointer to **PRD v0.5's L4 addendum `@5517e071e8`** on Andrew-direct 2026-09-11
~17:3xZ — the harvest estate consolidated onto one box under `4.0.0_SA_CRO~Z`.

**46 = 44 proved + 2 routed away with their pointer.** Recorded because "46 orders, 44 proofs" reads
as two missing proofs to anyone who does not open the two files, and a terminal status without its
pointer is the rot this project has already named once.

## 3. STATE — 0 of 15 REALIZED, and the distance is not a cell for fourteen of them

⛔ **Rule 22 STATE. Every bar was read from the PRD's own DONE WHEN line this tick, not carried
forward from round 7's analysis.**

**Fourteen of fifteen bars name a HUMAN ACT** and say so in the imperative: *"an analyst has
actually done it, not merely could"* (FWD-1) · *"a real uncovered name has been pulled and read"*
(FWD-2) · *"a figure has actually been challenged and answered from the page"* (FWD-3) · *"Adam has
actually forwarded one"* (FWD-5) · *"a PM has actually opened the page, read the ranked list, and
clicked through"* (FWD-15). **No artifact can satisfy those, and the PRD says so in terms at its own
bar-distribution line.**

**FWD-9 is the single exception and the single most useful line in this analysis.** Its bar is
`APPLIED` — *"the marking is in place and sits beside the evidence the sentence was drawn from"*.
It names a PLACEMENT on a served page, not a person. **So FWD-9's entire remaining distance is the
page being served** — which is the promote, and the promote is frozen by Andrew's own standing word,
restated twice at 03:21Z.

```
REALIZED                 0 of 15
distance for FWD-9       the promote (frozen -- his call, and nothing here asks for it)
distance for the other 14  the promote AND a human act
```
Portal state, independently re-measured by the CVO with its own instrument rather than restated from
mine: source object `a845a8be75` is contained by **zero of nine** freshly listed remote heads;
gitlink `e85f6eb84f` unchanged; all portal results EXERCISED-NOT-REALIZED. That corroborates `Z-S47`
by a different route, which is the only kind of confirmation Rule 22 counts.

## 4. WHAT ROUND 8 ACTUALLY MOVED — the producer boundary fell

Round 7's close named one lesson: **107 producer-side tests passing while the page joined 0 of 183
figures.** The laptop's audit reached the same place independently and from different evidence
(145 of 228 criteria `command`, only 9 `live_read`). Round 8's three cells were aimed at exactly
that, and on the CVO's L9 evidence they hit it:

- **the join is executed, not asserted** — the actual `checkFor` against actual populated
  `Thesis`/`ProvenanceLine`, 183/183 and 13/13, with the unresolved control retained (`W13-S2`);
- **the chart is rendered, not simulated** — the actual pinned `RankedChart` with fresh offline
  adapter outputs, absent/partial/exhaust at 328/1554/775 and **three distinct hashes, where the
  pre-repair component collided absent against exhausted** (`W13-S5`, `W13-S8`). The negative
  control fires, which is what makes the pass mean anything;
- **the types are built, not claimed** — 2072 files, rc0, and a deliberately planted string-to-number
  error caught as TS2322 rc2 (`W13-S6`).

**That is the acceptance regime moving from the producer's edge to the consumer's edge inside one
round**, and it is the substantive answer to the question Andrew asked at 02:48Z.

## 5. THE LIMIT ON THIS ROUND'S EVIDENCE, NAMED RATHER THAN LEFT FOR A READER TO FIND

Three of six judgment criteria are FAIL for disclosed worker typecheck absences, plus one literal
FAIL for `rg-2` AC1's constructed-series fixture. **The CVO then performed the missing verification
itself at L9 and graded it.** The slug is scrupulous about the part that matters — *"not
retroactively credited to the worker… preserve the worker's absence and its FAIL judgment"* — and
under Rule 27 the grading is correct, because judgment criteria are graded at L9 and never
self-graded.

⚠ **But the verification and its adjudication are the same seat's, and there is no second instrument
on the CVO's own typed build.** That is not a defect and no recut is asked for: the alternative —
re-running a completed measurement to relabel its provenance — is the laundering the slug explicitly
refuses. **It is a stated limit on how far this round's evidence reaches, and it is recorded here so
a later reader does not mistake single-seat verification for corroboration.**

## 6. ⭐ THE ONE CELL THAT REMAINS, AND IT IS THE ONE HIS DIRECTION NAMES

The slug's own boundary, quoted: *"Browser effects, full served route and publication remain outside
this result and under their existing obligations."*

**So the component is proven and the ROUTE is not.** Nobody has loaded the actual page, in an actual
browser, against the actual data, end to end. Round 7 measured the page joining 0 of 183; round 8
repaired the join *at the component*. The gap between those two sentences is the last producer-side
distance in this project.

⛔ **AND IT DOES NOT REQUIRE A PROMOTE.** A local dev render (`bun run dev --port 5175`) is not a
publish, moves no gitlink, and touches no remote head. Andrew-direct 03:21:46Z, VERBATIM: *"all the
wiring needs to be done"* and *"I expect frontend for both RESAPP and ASTTAX to be done too, despite
not pushing to promote until a future date."* **This is that, exactly: the work complete and waiting
at the promote line.**

> **RECOMMENDATION TO `2.0.0_SA_COO~ZZZ` — ONE CELL, and the recut is that seat's, not mine.**
> Exercise the full served route locally end to end against real data: the page loads, the figures
> join on screen, a failed check is visibly marked, and the ranked panel renders and navigates.
> **NO promote, NO gitlink move, NO remote push.** Its bar is a rendered route, not a passing test.
> **Cover FWD-9 explicitly**, because it is the only outcome whose bar a served page alone can close
> and it currently carries the thinnest coverage in the whole set at one order.

**Nothing else is warranted on coverage grounds.** A round 9 wider than this would be cells written
against outcomes that no build can move, which is the failure this project's own bar-distribution
line was written to prevent.

## 7. THE TWO OPEN ROWS THE SLUG ASSIGNS TO THIS SEAT — BOTH DISCHARGED HERE

`Z-S53` and `Z-S57` are **one obligation, not two** (the slug is right to say so): the POSN
candidate-by-candidate standing read, *"using both roots and both JSON block shapes."*

- **Both block shapes** — done at `Z-S39` `@8efaf17312` and `Z-S40` `@0a4af820b8`, tick 41: 26 ids
  read to a condition each, collapsing to **nine real obligations**, linked by the rows' own
  `adjudicates` field with a 54-of-134 positive control. The slug's *"no proof of that completed
  read is in this intake"* is correct about the intake and superseded by those two commits.
- **Both roots — and this half was genuinely missing until this tick.** My tick-41 sweep covered the
  tree root only (7 files). Measured now: the legacy flat root `org/surprise_channel/` holds **24
  entries and no `POSN_ASTTAX`**. Positive control: the root is readable and non-empty, and it
  **does** contain `POSN_TENANCY` — a near-miss sibling that would have surfaced a POSN-prefixed
  directory had one existed. **So root two is a measured absence for this project, not a path-shape
  zero**, and the tree sweep was the complete population after all.

**The CVO was right to hold these open and right to insist on both roots.** One of the two
conditions was unmet when the slug was cut.

Remaining OPEN rows are correctly owned elsewhere: `W13-S3` (the read-boundary disposition) with
`2.0.0_SA_COO~ZZZ`, and `Z-S61` (the explanation brief's timing figure) with the brief's author —
this seat has already corrected the same figure in its own artifact `@5d688b925d` and supplied the
birth and issuance pins.

---

**PRD ACTION: NONE.** `prd_version` unchanged; no addendum; no endpoint edit. Coverage is complete,
the outcome set is unchanged, and no outcome is missing a cell.
**No TO cut, no dispatch, no apply, no merge, no promote.** The recut is `2.0.0_SA_COO~ZZZ`'s.

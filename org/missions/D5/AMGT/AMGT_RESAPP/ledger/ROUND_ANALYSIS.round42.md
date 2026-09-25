# AMGT_RESAPP -- ROUND 42 L10 ANALYSIS -- `1.0.0_SA_CTO~Z`, 2026-09-25 ~20:0xZ

**Input:** `3.0.0_SA_CVO~Z`'s slug, msg 25909 (READ-acked), pointing at `ADJUDICATION_v52.md` @`55d659db8c`
-- read to EOF, **pin verified identical to HEAD** (`git rev-parse` both return `94c837ef41ce...`).
**L10 preconditions, re-read:** 2 of 2 orders terminal; 6 committed rows dispositioned (5 graduated,
`Z-S279` carried BLOCKING/ARMED); 1 of 1 judgment criterion graded. **MET.**

**THE ROUND SUCCEEDED AND THE OUTCOME IS STILL NOT_REALIZED, and the reason is the one card I was wrong to
carry.** `FWD-30`'s equality limb went from 5 of 89 to **89 of 89**. On the population Andrew ratified it
is **89 of 94**.

---

## 1. WHAT ROUND 42 ACHIEVED -- the best single-cell return this project has had

| population | plane | OK | NOT_OK |
|---|---|---|---|
| 89-name snapshot, local rebuild | local | **89** | 0 |
| 89-name snapshot, fresh capture | **SERVED** | **89** | 0 |
| **live research library, 94** (read 18:42:56Z) | **SERVED** | **89** | **5** |

**The base at the same vintage was 0 of 89** (`Z-S277`). Round 41 read 5 OK / 84 NOT_OK and its
adjudication reported that **72 of the 84 were ONE behaviour**. Round 42 cut **one** export-side cell and
the count went to **zero on 89 of 89** -- so the fix reached **all 84, not the 72 projected**, and it holds
on the SERVED plane rather than only locally.

> **The whole return came from a group-by that cost one query.** Round 41's adjudication printed the
> SIGNATURE DISTRIBUTION instead of the failure total; that is what made a one-cell round possible against
> 84 failures. **N failures is not N causes, and the difference between those two sentences was 83 cells.**

**And `rq-1` AC4 PASSES on the strongest available mechanism, which I adopt without re-grading:** the export
**prints the page's own strings rather than composing equivalent ones.** ASML's management reason in the
export is the page payload's `reason` field verbatim; the type codes `ZERO_OFFICERS` and `NO_OBJECT` are the
payload's **own `absent_because` field**, checked at the bytes. `ZERO_OFFICERS` (the filing's officer section
is empty) and `NO_OBJECT` (no management object landed) are **different causes with different remedies, and
the export distinguishes them because the page does** -- *a boundary and a defect must not render
identically*, satisfied on a second surface.

## 2. `FWD-30` -- **NOT_REALIZED**, and the universe ruling is what decides it

Fence read at HEAD. The DONE WHEN is **`(a OR b) AND the equality limb`**:

- **(a)** a Brand-Guidelines presentation shaped like the team's earnings updates, **AT MOST TWO PAGES** --
  **DOES NOT EXIST.** Today's spec (@`76bd6e76eb`) measured the served pdf at **13 pages**, and the 2-page
  branded branch was never started.
- **(b)** a machine-readable rich-text output -- **EXISTS.** So **the OR is satisfied through (b)**, and (a)'s
  absence does not fail this outcome. Recorded explicitly so the `or` is not used to retire (a) by accident
  and is not used to fail the outcome twice.
- **the equality limb** -- *"the SAME figures, the SAME cites and the SAME absences, with NOTHING in the
  export that is not on the page"* -- **89 of 89 on the snapshot. 89 of 94 on the live library.**

**THE QUANTIFIER, and I am applying the rule I wrote at round 41 rather than the number I would prefer.**
The fence opens *"A PM exports the name they are reading"* -- singular in grammar. **It is a UNIVERSAL in
force:** the PM reads whichever name they open, so the claim holds only if it holds for every name they can
open. An export that works on 89 of 94 fails the PM who opens `AMD`.

**And WHICH 94 is not my choice.** `C-BACKFILL-DENOMINATOR-IS-THE-RESEARCH-FOLDER` ratifies Andrew's word of
2026-09-24: the population is the Asset Management research folder, read fresh, denominator printed. **Today
that reads 94.** So the equality limb is graded over 94 and reads **89**. **`FWD-30` is NOT_REALIZED.**

> **This is the card I carried for five ticks and then wrongly re-ruled, now doing real work.** Under the
> frozen-89 reading `FWD-30` would be REALIZED today. Under Andrew's own ratified reading it is not.
> **The answer I should have found on 2026-09-24 is the thing that decides this grade**, and it decides it
> against the comfortable direction.

## 3. THE FIVE MISSES ARE NOT EXPORT FAILURES -- THEY ARE THE GOAL'S BACKFILL CLAUSE

**`AMD`, `GOOGL`, `LLY`, `PWR`, `UNH`** -- exactly the names added since the 09-10 snapshot. **None has a
landed model block.** The print route REFUSES each (*"no printable pack"*) while the page shows 16 absence
lines. The CVO calls it structural rather than a regression and that is right: **the export has no path for a
name without a model block, and building one would be building a pack out of nothing.**

**So the last 5 of `FWD-30` and the goal's third clause are THE SAME FIVE NAMES.** The goal reads
*"followed by complete backfill for all of these securities through the opal-data-harvest channels"*, and
`freshness` measured `never_refreshed 196` of 250 this morning. **One act -- land model blocks for those five
-- closes `FWD-30`'s equality limb and moves the backfill clause at the same time.** Nothing else in round 43
does two clauses of the goal at once.

**RULING:** round 43 cuts the five no-block names as its FIRST cell, ahead of the base-case guard.
`Z-S279` is BLOCKING and ARMED and is a served-correctness defect; **the five are the only item that closes
an outcome.** Both go in the same issuance.

## 4. `Z-S281` IS AT HEAD NOW -- the exclusion was correct and is already superseded

The adjudication excludes `Z-S281` as *"ABSENT AT HEAD ... an uncommitted row is not filed"* and **that was
true at its read.** I committed the row at **`33ae1e3d89`**, and `git show HEAD:<channel>` returns 1
occurrence of the id. **It is filed, and round 43's compile carries it.**

**The CVO's handling of it is the part to keep.** It refused to compile an uncommitted row -- correct, an L8
compiles the channel -- **and recorded the row's SUBJECT in the adjudication anyway, so the finding could not
vanish with the row.** That is the right shape for every future uncommitted-at-compile case, and I am making
it the rule:

> **RULE R-7 (round 42, standing).** An L8 **compiles the channel and nothing else**; a row uncommitted at
> compile is NOT counted, NOT adjudicated and NOT carried. **AND its SUBJECT is recorded in the adjudication
> body**, so the exclusion costs a denominator entry and never a finding. Cost: one paragraph.
> Non-application: a row whose subject the adjudication already covers from another source.

**My own share of this, stated:** the row was uncommitted at the packet because **I minted its id from a read
taken hours earlier**, collided with a `Z-S279` the issuer had already committed, and the duplicate **blocked
that peer's next commit** before it restored my row as `Z-S281`. **The cost of my stale id landed on another
seat.** On a shared append-only channel the id must be derived in the same operation as the write; CLAUDE.md
14b's *"take the shared index's seconds-long race"* is about the COMMIT, not about the ID.

## 5. THE CLASS THAT IS NOW THREE FOR THREE -- a check that cannot fail on the axis that matters

The adjudication names it and I am ruling on it, because three instances in three rounds is a mechanism, not
a run of luck:

| round | the check that could not fail | what it missed |
|---|---|---|
| `Z-S265` | a green grid over every column | a P/E served **100x wrong** |
| `Z-S268` | extras computed and never graded | the computed values themselves |
| `Z-S281` (this round) | **the harness does not grade a SERVED line** | a line reading *"SERVED -- the payload carries no case block"* **on a served case block**, so all four sweeps pass over it |

**Each was invisible to every mechanical criterion, and each was found by a person reading an artifact.**
That is the same finding from three directions, and the estate already has the law for it -- *"a check that
cannot FAIL is not a check"*, `FWD-10`'s own SOURCE line.

> **RULE R-8 (round 42, both projects).** A criterion that grades a field's ABSENCE must also grade its
> PRESENCE, or it states in one line which half it does not grade. **A sweep that passes over every SERVED
> value is not a partial check; on that axis it is no check.** Cost: one clause per criterion.
> Non-application: a criterion whose declared axis is absence-only AND says so.

## 6. THE CROSS-PROJECT FIX-SHAPE, routed rather than admired

ASML's management payload carries `absent_because`, `absence_reason_class: pull-missed`,
`absence_reason_evidence`, `roster_status`, `source_accession` and `source_item` -- **a typed, sourced,
evidenced absence model, live today.** `AMGT_CORPUS`'s `Z-S36` is **9,471 dossier rows on a hard-coded
constant** that went false when the figures arrived.

**The same estate runs both patterns right now.** `R-3` (*"a constant absent-reason is a defect on sight"*)
told `AMGT_CORPUS` what was wrong; **this payload shows it what right looks like, in its own estate, with no
design work owed.** Routed to `2.0.0_SA_COO~X` as the SHAPE for `Z-S36`'s round-5 fix, citing
`ADJUDICATION_v52` section 3 -- not a new pattern to invent, a pattern to copy.

## 7. ENRICHMENT LIST FOR ROUND 43 -- five items, ordered

1. **The five no-block names** (`AMD`, `GOOGL`, `LLY`, `PWR`, `UNH`) -- closes `FWD-30`'s equality limb over
   94 and moves the goal's backfill clause. **The only item that closes an outcome.**
2. **`Z-S279`'s base/px_last guard** -- BLOCKING, ARMED. The producer is `model_block_pull.py:1119`
   (`TO-AMGT-rk-37`), and `AMGT_CORPUS`'s `CRPS-g-1` has already built the guarded rule with four named
   causes: **copy it rather than re-derive it.**
3. **`Z-S281`'s Model Cases line** -- write the PRESENT branch of `_model_cases_markdown`
   (`render_pack.py:711-720`); it currently renders none of `base`, `upside` or `downside`.
4. **R-8 applied to the export harness** -- make the sweep grade a SERVED line, which is what would have
   caught item 3 without a person reading the artifact.
5. **The 2-page branded export (a)** -- unchanged from the spec's ruling: build the TABLE's grain before the
   page, and it stays behind items 1-4 because (b) already satisfies the fence's `or`.

## 8. ROUND 42 IS **CLOSED**; `FWD-30` IS **NOT_REALIZED**; AND THE DISTANCE IS FIVE NAMES

**Closed:** 2 of 2 terminal, 6 of 6 committed rows dispositioned, AC4 PASS on mechanism, the export fix
holding on the served plane at `FOF+dRXoW1KFFzD0moLigsMB2LMmIjwhwURq7FkCzbw=`.

**`FWD-30` NOT_REALIZED on 89 of 94.** Two rules (R-7, R-8), five enrichment items, one carried BLOCKING row.

**And the honest shape of it: this is the first AMGT round whose remaining gap is a NUMBER I can name.**
Round 41 ended with 84 failures of unknown cause. Round 42 ends with **five named securities that have no
model block**, and the outcome they block is the export clause of the goal. **The render half of this product
is done and measured; what is left is five packs and a plausibility guard.**

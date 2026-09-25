# ENDPOINT COVERAGE AUDIT -- `AMGT_RESAPP`, 2026-09-25 ~03:5xZ, `1.0.0_SA_CTO~Z`

**Why this exists.** The goal says *"Finish `AMGT_RESAPP`, `AMGT_CORPUS` and close them out."* Rule 27
closes a project **"when every FWD grades REALIZED."** I have written three round analyses tonight and
never once asked **how many of this project's declared outcomes carry a grade at all.** This is that
census, and it changes the remaining distance materially.

---

## 1. THE MEASUREMENT

**Denominator: 30 declared `endpoint_outcomes`** (`AMGT_RESAPP_PRD.md` header, `FWD-1`..`FWD-30`).
**Instrument:** a lexical census of all 39 committed round analyses (`ROUND_ANALYSIS.round1..40.md`),
taking for each outcome the most recent ROUND whose text places a grade token within 120 characters of
the id, with ranges expanded.

| band | count | which |
|---|---|---|
| **REALIZED** at last mention | **11** | `FWD-3` (round 36); `FWD-21`..`FWD-30` (rounds 37-40) |
| **NOT_REALIZED** at last mention | **13** | `FWD-1`, `FWD-2`, `FWD-4`..`FWD-14` |
| **NO GRADE FOUND** in any analysis | **6** | `FWD-15`..`FWD-20` |

**Twelve of the thirteen NOT_REALIZED were last graded in ROUND 1.** The project is at round 41.

## 2. WHAT THIS DOES AND DOES NOT ESTABLISH -- the instrument's own bound

**MEASURED:** what the LEDGER RECORDS. **NOT MEASURED:** whether those outcomes are realized in the
product today. Forty rounds of work sit between round 1 and now, and several of these outcomes have
plainly been advanced by cells that did not restate the outcome id beside a grade token.

**So this is not a claim that 19 outcomes are open. It is a claim that 19 outcomes CANNOT BE SHOWN
CLOSED FROM THE RECORD** -- and for a completion test that reads the record, those are the same thing.
**A project cannot close on outcomes nobody has graded**, whichever way the grades would fall.

WARN: **I nearly published a worse version of this.** The first run reported `FWD-22`..`FWD-27` as NEVER
GRADED. They are graded -- as a RANGE, `` `FWD-21`..`FWD-28` | **REALIZED** `` -- which my regex did not
expand. Twelve false entries. **A census with one provably wrong arm has no trustworthy arms**, so the
first run was discarded rather than corrected in place, and the rerun's range expansion is why
`FWD-22`..`FWD-28` now read REALIZED. The remaining six with NO GRADE FOUND survived both instruments.

## 3. HOW THIS HAPPENED, and it is visible in my own words

Round 38's analysis states its own scope plainly: **"Denominator: the 10 outcomes `FWD-21`..`FWD-30`."**
Rounds 38, 39 and 40 each graded that ten-outcome denominator honestly and completely. **The defect is
not in any round -- it is that a 10-outcome denominator has been serving a 30-outcome endpoint for
several rounds, and nothing in the loop compares the two.**

This is Rule 24's own tell, on my own work: **a denominator whose scope is narrower than the sentence
beside it.** Each analysis said "this round's outcomes"; the project's status implied "the project's
outcomes"; and the gap between them was never printed. **Addendum B (`FWD-21`..`FWD-30`) is the visible
work because it is what the recent rounds cut, and visibility became the selection criterion for
grading.**

## 4. WHAT IT MEANS FOR THE GOAL, stated against the goal's own clauses

- *"Visually polished Security Analysis application"* -- this is Addendum B, and it is **REALIZED across
  all ten** of its outcomes. **That half of the goal is genuinely done on the record.**
- *"with all Asset Management research companies folded in"* -- this maps to **`FWD-1`** (*"an analyst
  gets a first-draft pack for a covered name"*), whose last recorded grade is **NOT_REALIZED at round
  1**, and whose last recorded COVERAGE is round 12's *"model for 33 of 89; prose for 12."*
- *"export option functional ... 2pg max or machine readable rich text"* -- `FWD-30`, **REALIZED** on
  branch (b), bounded to ONE name; the population cell `rp-1` is cut and executing.
- *"complete backfill ... through the opal-data-harvest channels"* -- `AMGT_CORPUS`, identity complete at
  94 of 94, backfill NOT.

**So the honest distance is: the APPLICATION half is done and recorded; the SUBSTANCE half
(`FWD-1`..`FWD-20`) is not shown closed for 19 of 20 outcomes.**

## 5. THE REMEDY, and it is this seat's

**A re-grade pass over `FWD-1`..`FWD-20`, graded against each outcome's own PRD fence**, producing for
each: REALIZED / NOT_REALIZED / NOT GRADEABLE-and-why, with the population bound stated where the outcome
is per-name. It is the CTO's work (grading is this seat's at L10) and it is not a round: **no cell is cut
for it, and it blocks no issuer.**

**Cost:** 20 fence reads plus their evidence. **Non-application:** it does not re-open any of the eleven
REALIZED grades, and it does not touch `AMGT_CORPUS` or `AMGT_HARVST`, whose endpoints are smaller and
whose recent analyses grade their full declared set.

**Sequencing:** it runs BEHIND the live rounds rather than ahead of them -- `rp-1`, `f-1`..`f-3` and
HARVST round 6 are executing and none of them waits on this. **The audit changes what "done" means, not
what anyone is doing right now.**

## 6. WHAT I AM NOT DOING

**Not re-grading them in this record.** A grade asserted without reading the fence is exactly the failure
that produced the vacated Peers ruling tonight, and twenty of them written quickly would be twenty
chances to repeat it. **The census is the finding; the grades are the work.**

**And not carding it to Andrew.** No decision of his is required: the outcomes are declared, the fences
are written, and the grading authority is this seat's. Under the queue taxonomy this is neither a call
nor a blocked act -- it is **work**, and naming it as a card would be the avoidance the fourth class
describes.

Push state: this commit LOCAL on landing; origin/CLOUD @`4749dc06e2` at last read. This lane does not
push.

---

# THE RE-GRADE PASS BEGINS -- `FWD-1`, graded 2026-09-25 ~04:0xZ

**`FWD-1` -- NOT_REALIZED.** Graded against its own fence (`AMGT_RESAPP_PRD.md:426-433`), not re-asserted
from round 1.

**THE INSTRUMENT, and why it is sound.** Round 40's six `real-run-served/` captures are **DOM-LAYOUT
measurements** (`visibleElements`, `bandContainers`, `textChars`) -- the instrument for `FWD-21`..`FWD-28`,
and **the wrong instrument for a content claim.** There is no served CONTENT capture in round 40. So I
used the served **rich export** instead, which is sound for exactly one reason: **`FWD-30`'s grade
established the export is field-by-field EQUAL to the page** -- 165 figures, 15 cites, 17 absences,
extras 0, missing 0. Reading the export therefore reads the page, on a verified equality rather than an
assumed one.

**ITS ACCEPT NAMES THREE THINGS ON SCREEN. Measured on `BA_US_Equity`, the best-covered name:**

| item | measured | verdict |
|---|---|---|
| the model numbers | ten fiscal-year sections 2016-2025; `Revenue` x14; 165 figures | **PRESENT** |
| the business description | `## Company Description` exists -- and its own subheading reads **"Filed detail (does not describe the business)"** | **NOT a business description** |
| the segment breakdown | see control below | **ABSENT** |

**THE SEGMENT CONTROL, because a bare-word zero is not an absence -- and it overturned my first read.**
`segment` reads **0**, which I nearly published. The control on Boeing's real segment names reads
`Commercial Airplanes` 1, `Global Services` 1, `BDS` 2, `Defense` 2. **So the names ARE in the document
and the bare-word zero was wrong.** Locating them settles it: `BDS` is ONE filed backlog sentence inside
the "does not describe the business" section, and `Commercial Airplanes`/`Global Services` appear **in
the Management/Board table as parts of executives' JOB TITLES.** Neither is a breakdown of results by
segment. **Positive controls on the same instrument: `Fiscal year` 12, `Revenue` 14, `Company
Description` 1 -- the reader can see what it is meant to see.**

**So two of the three named items fail**, and the second fails in a way worth stating precisely: the page
does not silently omit a business description, it **discloses that the filed detail is not one.** That is
honest behaviour and it is still not the outcome, because `FWD-1`'s analyst wanted the description, not
a notice about it.

**The EXERCISED limb is separately unmet:** *"an analyst has actually done it, not merely could"* -- no
analyst read is recorded. Same person-limb shape as `FWD-30`'s ACCEPT, and it cannot be closed by any
seat.

**AND THE BOUND THAT MAKES THIS WORSE, NOT BETTER:** this is `BA_US_Equity`, the name every round has
exercised. **If the best-covered name in the corpus carries no segment breakdown and no business
description, the other 88 are not better.** The goal's clause *"with all Asset Management research
companies folded in"* is therefore not met at its best case, before the population question is even
reached.

**1 of 20 graded. 19 remain**, and this one took a wrong-instrument correction and an overturned zero to
get right -- which is the argument for grading them one at a time rather than in a batch.

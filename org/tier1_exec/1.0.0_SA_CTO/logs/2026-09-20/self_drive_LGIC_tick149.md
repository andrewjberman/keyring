# /self-drive LGIC -- tick 149 (2026-09-20 ~17:2xZ-17:5xZ) -- THE CARD ANDREW HOLDS

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260916_052xZ_LGIC_GOAL_AND_30M_SELF_DRIVE_ADJUDICATE.md`
**Scope:** `LGIC_NAMING, LGIC_ENFORCE, LGIC_CANON, LGIC_LGCTFM`. **Device:** laptop. **state: ARMED**

## The reads

| read | result |
|---|---|
| **orders** | **0 of 170**; control `IRPT_BCKEND` **1 of 79** (was 4 -- round 7 draining; control still non-zero) |
| **inbox** | 98614 / 98615 read + acked; 3/3 READ before them |
| **sequence** | TRACK, 10 projects, stage enum OK, no DRIFT |
| **§4** | 1 CLOSED + 3 HELD/TERMINAL of 4 |

## ⛔⭐ 1. THE VERSION OF `ANDREW_CARD.md` ANDREW HOLDS IS THE ONLY ONE WITHOUT ITS OWN CORRECTION

Row `S66` @`919464a1f2`. `FWD-4`'s ACCEPT is *"Andrew has read the list for one subject."*

- Card delivered **~00:36Z 2026-09-18**, blob `5a5f3e68`, **4,635 bytes**.
- Card re-committed **`f3cfbabebb` 04:49 ET the same day** -- **after** delivery. HEAD blob `da2106bd3f`,
  **6,154 bytes**.
- ⭐ **Its commit subject CLAIMS "the ranking table and the recommendation do not move" -- a producer's
  self-report in an immutable carrier, so I verified it: ONE hunk, +22/-0, zero modified, 61 -> 83 lines.
  THE CLAIM HOLDS.**
- ⛔ **But the added 22 lines ARE the correction** -- a `## The adjudication of record` section carrying
  `662d53b793` and *"the rows touching a live, client-facing surface number 1 of 179 (T-0001), NOT TWO."*

> ⛔ **So the card in his hands still recommends on the basis that TWO rows touch a live client-facing
> surface, with nothing beside it saying the number is one.**
> **RULED (L4 author + adjudicator of record): THE CARD IS RE-DELIVERED AT HEAD AND `FWD-4` IS NOT GRADED
> UNTIL IT IS.** ⚠ **Not a re-scope and not a PRD amendment** -- `98606`/`98607` refused that and the
> refusal stands. The delivery act is `2.0.0_SA_COO~G`'s, which carried it.
> ⭐ **KEEPABLE: WHEN AN ACCEPT NAMES A HUMAN READING A DOCUMENT, THE GRADE IS AGAINST THE BLOB THAT
> HUMAN RECEIVED, NEVER THE PATH.** Record the delivered blob id at delivery time; re-deliver on change.
> **COST:** one `git rev-parse HEAD:<path>`. **NON-APPLICATION:** an outcome closed by an act, or a
> document delivered by reference.

⚠ **Nobody erred.** At ~00:36Z the delivered blob WAS current. **An artifact delivered out of a repository
keeps improving after it leaves, and the recipient's copy is frozen at the worst moment.** Separately the
standalone correction file is now R-40-pinned to the superseded blob -- verifying its hash returns a MISS.

## ⛔ 2. A NUMBER I BROADCAST AN HOUR AGO NEEDED A QUALIFIER

Row `S28` @`6fc19b0216`. `2.0.0_SA_COO~G` (`98614`): *"Equality IS the conformance test, so the grader
returns CONFORMANT BECAUSE IT COULD NOT RESOLVE THE TEMPLATE ... A PASS PRODUCED BY THE INABILITY TO GRADE."*

Re-parsed my own saved census: **CONFORMANT 400 / OUT-OF-PATTERN 1,037** reproduce. **All 400 have
`current == canonical`** -- so CONFORMANT asserts STRING EQUALITY, nothing stronger. **5 of the 400 carry a
brace, all five one name** (`orion/rate_limit_state_{dim_name}.json`). ⭐ **That seat reached the same name
and same count from the placeholder split -- two instruments, the same five.**

> ⛔ **My published 400 carried no qualifier and is not materially wrong ONLY because of scale (1.25%).**
> ⚠ **I interrogated the denominator, the halting behaviour, the unit and the unaccounted 126 -- and left
> the one column that looked like good news unexamined.** *A control that passes is the one you will not
> re-examine* -- my own round-6 rule, met against my own figures four hours later.

## ⛔⭐ 3. A CARRIED ITEM WAS WRONG WHEN MEASURED, SECOND TICK RUNNING

I have reported **"`W1-S74`'s doc amendment -- direction ruled, nothing routed"** as mine. **MEASURED: both
`disarm.owner` and `remediation.owner` are `2.0.0_SA_COO~G`, and the remedy is a `grade()` fix with a
positive control and a mutant -- NOT a doc amendment.** Last tick the same check found my carried armed-row
list said **3** where the census said **13**, one of them not mine.

> ⛔ **A CARRIED LIST HAS NO DENOMINATOR AND NO OWNER FIELD -- IT IS RECOLLECTION WEARING THE CLOTHES OF A
> TASK LIST, and it degrades in ONE direction: toward "still mine, still owed."**

**Re-verified by reading, not recall:** `ADVI_FIRMBKTS` (active / PRD / `coo_lane: None`) and the ENFORCE
clause-2 card -- **both genuinely open.** ⚠ Found on the way: **`ADVI_FIRMBKTS` has TWO register carriers**,
one substantive and one with an EMPTY `blocking`. Named to `0.0.0_AB_MSTR`; no edit made from here.

## ALSO

- ⭐ **The append assert fired instead of writing blind:** LGCTFM's channel is **42 separate fences**, not
  CANON's single array. A script tuned to one shape would have written into the wrong structure.
- ⛔ A heredoc halved my backslashes again -- switched to Write-tool scripts for every parse this tick.

## Open calls at Andrew -- **2**, both re-verified this tick

## Compiler Tools

`get_delivery_state` · `ack_messages` x2 (4 ids) · order census + control · `sequence-check` · `Glob` for
the card · `git cat-file -s` / `diff -u` on two blobs · census-output re-parse (400/1037) · row appends x2
(gate OK) · 2 commits · `send_message` x1 (3 delivered) · push state by **ancestry**.

**PUSH STATE at write time:** `919464a1f2`, `6fc19b0216` LOCAL; origin/CLOUD `5700e1c825`. **state: ARMED**

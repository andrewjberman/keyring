# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 114 -- I COUNTED AN ANSWERED CALL AS OPEN FOR EIGHT LOGS, WITH THE WORD "ANSWERED" BESIDE IT

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-14T13:1xZ**
Tick 109's log is `@4b9ec06d92` (+1 addendum `@9ee94f26db`). Covers ticks 110-114.

> **Andrew ran `/exec-sum` and `/open-calls` directly at this terminal for the first time since
> 2026-09-13 ~01:05Z. Running the open-calls sweep properly exposed a defect in this loop's own
> tick line that eight committed logs carried.**

---

## 1. ⛔ THE RESERVED COUNT WAS WRONG, AND THE EVIDENCE WAS IN MY OWN OUTPUT

```
RESERVED=2 printed in ticks 91, 94, 102, 105, 106, 107, 108, 109
composition, verbatim from those logs:
  1of2  LIMB 6 widening
  2of2  list owner -- ANSWERED but NOT DONE; FWD-14 unrealized, Z-S78 unmet
```
>> **I WROTE THE WORD "ANSWERED" AND KEPT COUNTING IT AS A CARD AT ANDREW.** He answered it at
   ~05:31Z; a call he has answered is CLOSED as a call, whatever remains of the work. The label and
   the count contradicted each other **on the same line, in eight committed logs.** <<
⛔ **This is precisely the OVER-RESERVATION DEFECT the skill was restructured to prevent** -- his
words: *"somehow every single open call falls under 'reserved' versus adjudicable which needs to be
assessed better because it renders the skill useless if it cant get calls adjudicated."*
⭐ **AND THE MECHANISM IS THE NIGHT'S OWN THEME: THE COUNT STAYED AT 2, SO NOTHING PROMPTED A
RE-CHECK.** A stale number is bad; **a stale number sitting beside the word that falsifies it is
worse**, because it proves the two were never read together -- by me, eight times. It took Andrew
running the skill directly to make me re-derive the queue instead of restating it.

## 2. THE CORRECTED QUEUE, AND IT IS EMPTY *IN SCOPE*

| card | state | in this loop's scope? |
|---|---|---|
| further widening of the task-order gate | OPEN at Andrew, cited to Rule 27 *"any further widening is HIS call"* | **NO** -- a gate/law question |
| arm the ASCII check from warn to refuse | OPEN at Andrew, cited to the never-implement-an-approval-gate line | **NO** -- tooling, not either project |
| list owner | **CLOSED** -- answered ~05:31Z. STRUCK. | n/a |

**So the honest tick line is `No open calls in scope AMGT_RESAPP & POSN_ASTTAX` -- not `2 RESERVED`.**
Both live cards were put to Andrew directly this turn and belong in his queue, not in this loop's.
⚠ **THE ALL-RESERVED TELL FIRED** (both live cards RESERVED, zero adjudicable) **and was re-tested as
the skill requires:** each produces a quotable law line naming the decision class, so both classify
RESERVED honestly. **Nothing was pitched to the CVO** -- a NEVER is not adjudicable, and neither card
is in scope regardless.

## 3. ⚠ AND A NEAR-MISS IN THE SWEEP ITSELF

Verifying whether the gate-widening card was still open, I grepped the record of the seven cards
Andrew approved on 09-13 for `LIMB 6`, `newly-added` and `placeholders`. **All three returned ZERO,
which read as "he never ruled on it."** He had: **card 6 of seven was exactly that question.**
>> ⭐ **THE `/open-calls` FORMAT DELIBERATELY STRIPS OUR VOCABULARY, so a jargon grep over an
   open-calls record is GUARANTEED to miss.** His card reads *"edits to existing orders... only orders
   that already declare the element being checked."* **Searching a plain-language record for internal
   names cannot succeed**, and the zero it returns is indistinguishable from a real absence. Caught by
   opening the record and reading the seven card titles instead. <<
**One clause of that question does remain open** -- he widened one element, and Rule 27 records that
any further widening is his -- so the card survives, **but narrowed, and it would have been re-asked
in its original over-broad form.**

## 4. STATE

```
AMGT_RESAPP  active / ROUND_CLOSE  47 of 47 COMPLETE, 0 open   round 9 at L9, newest adjudication 33.4 h
POSN_ASTTAX  active / EXECUTING    15 C / 4 ACTIVE of 19       round 4 at L9, newest adjudication 32.2 h
v9 · v4 · RA.round9 · RA.round4 ABSENT · COMPLETION_GRADES 0 both · denominator 2618 · control 0
both UNPLACED in the sequence · in-scope commits since 89c66c532b: 1 (control fires at 3)
OPEN CALLS IN SCOPE: 0 · at Andrew and out of scope: 2 · NO PITCH
COMPLETION   NOT DONE -- 0 of 2 · REACHABLE 2 · UNREACHABLE 0 · HELD-AT-STOP not reached
```
Ticks 110-113 were quiet on the work and are covered here. **The reviewer holds both rounds and
confirmed directly it is its own unfinished work, not blocked on this seat.**
`Z-S46`/`Z-S55`/`Z-S56`/`Z-S61`/`Z-S79` ARMED · `Z-S82` disarmed · portal `e85f6eb84f` · LD-0521
holds · freeze stands. No TO cut, no dispatch, no apply, no promote.

## Compiler Tools

The open-calls queue **re-derived from the records rather than restated from the prior tick line** --
which is the only reason the eight-log drift surfaced · the seven approved cards read by **opening the
record and listing its card titles**, after a jargon grep over a deliberately jargon-free document
returned a false zero · each surviving card's RESERVED classification re-tested against a quotable law
line per the all-reserved tell · elapsed measured on **WALL CLOCK** and movement by **commit-anchored
range with the ancestor test on the control**, both per the tick-112 corrections · project state from
`status_class`, never a `status` key that does not exist.

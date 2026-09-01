# ANDREW-DIRECT 2026-09-01 ~18:15Z: three rulings on the CVO `/open-calls` slate

**VERBATIM, in full:**

> **"1.) Rec approved. 2.) D8 sits first. 3.) every project at next TO. I am talking with CTO on how
> to handle this right now."**

Answering `/open-calls` from `3.0.0_SA_CVO` (3 cards, all CARRIED, no BLOCKING).

---

## RULING 1 -- the PERFRP two-carrier publish question (msg 91668)

**The card asked:** did the 08-25 08:5xZ line NARROW the 04:0xZ ratification of branch (b)?
**The REC approved, verbatim as emitted:** *"rule it (b)-unnarrowed, and keep the no-act hold until
you do."*

>> **THE RULING: the 08-25 08:5xZ line did NOT narrow the 04:0xZ ratification. BRANCH (b) STANDS AS
RATIFIED.** <<

**CONSEQUENCE, and it is a NON-ACT.** The hold was scoped *"until you do [rule]"* -- the ruling
discharges it. **Nothing is to be unpublished.** The restrictive reading is the one rejected, so the
status quo is the correct state and no seat has anything to execute.

⛔ **SCOPE BOUND, stated because a discharged hold reads like a green light.** This ruling REMOVES A
RESTRICTION. It does **not** authorize publishing anything beyond what branch (b) already ratified
at 04:0xZ. *"The absence of a prohibition is not anyone's permission."* Anyone reading this as a
licence to widen a served surface is reading it wrong.

**Why the direction mattered:** the stale carrier was the RESTRICTIVE one, so the expensive failure
here was always OVER-CORRECTION -- an unnecessary unpublish costs served data; a delayed ruling cost
nothing. Raised by `1.0.0_SA_CTO` (FINDING `4022ebae4a` + its ADDENDUM, 13:47Z / 13:50Z).

## RULING 2 -- `/self-drive` directive ordering

>> **"D8 sits first."** D8 precedes D3. <<

**OWNER: `1.0.0_SA_CTO`.** This closes a call that seat carried in its own summary as *"STILL AT
ANDREW: D3's order vs D8"*, and that I carried at this lane across two `/open-calls` runs.

⭐ **Recorded with its history because of HOW it stayed open.** It survived a blanket *"All recs
approved"* over a 9-card slate, because that card's REC was the explicit non-recommendation *"no
recommendation with confidence -- this turns on your business priority, which I do not hold."*
**Approving a non-recommendation authorizes nothing**, and the card carrying the least content is
the one most likely to be silently treated as decided. It was flagged rather than swept, and it took
a second `/open-calls` to draw the actual word.

## RULING 3 -- the fabric gate's "prospective" scope

>> **"every project at next TO."** Option (a). <<

**The gate as BUILT is CORRECT and needs NO CHANGE.** `.tools/to-pipeline-gate.py` @`40bf270dec`
already binds EVERY project the next time a TO is cut against it, not only newly-registered ones.
The ambiguity was real -- both readings were "prospective" -- and it is now closed the way it was
implemented.

**MEASURED CONSEQUENCE:** `--sweep` reads **fabric 349 of 349 ABSENT**. Every one of those projects
now needs `"fabric": "laptop" | "site-z"` set at the moment its next TO is cut. That is one key, at
a moment someone is already editing that project.

### ⛔ AND THE HANDLING IS LIVE WITH ANDREW AND CTO RIGHT NOW

> **"I am talking with CTO on how to handle this right now."**

**Relayed verbatim and NOT interpreted.** The WHAT is ruled (every project at next TO). The HOW is a
conversation in progress at the CTO terminal that this seat is not party to.

⛔ **THIS SEAT ISSUES NO INSTRUCTION OFF THAT SENTENCE.** Converting Andrew's word to one agent into
a gate or a stop on another is prohibited (`ANDREW_DIRECT_20260804_1827Z_NO_INFERRED_GATES_NO_SHADOW_
PIPELINES`): verbatim scope, relay never adjudicate -- wider OR narrower. Seats read the sentence and
draw their own conclusion; whatever comes out of that conversation governs the rollout mechanics, and
it will arrive from Andrew or CTO, not from here.

---

## STATE OF THE SLATE

```
  /open-calls run 1 (~1745Z, 9 cards)   "All recs approved"
     cards 1,2,3,4,5,7,9  ANSWERED and executed or specced
     card 6 (91668)       posture only -> RULED HERE
     card 8 (D3 vs D8)    non-recommendation -> RULED HERE
  /open-calls run 2 (~1815Z, 3 cards)   all three RULED above
```
**No open sovereign calls remain at this lane.** Cards 1 and 2 discharge to `1.0.0_SA_CTO`; card 3
required no build. Aftercare: recorded verbatim (this file) + broadcast same turn + push state
stated as a measured value in the broadcast.

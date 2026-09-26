# self-drive ticks 98-99, `1.0.0_SA_CTO~Z`, 2026-09-26 ~01:5x-04:0xZ

**Arming record:** through tick 98, `ANDREW_DIRECT_20260923_193xZ_SELF_DRIVE_AMGT_ALL_THREE_CLOSER_LOOPS.md`
@`a8a62f4f5c`. **From tick 99, `ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_SITEZ_DIRECTIVES_AS_A_WHOLE.md`**
@`f3b85ff6a5`, amended A1 @`fc26dfeedb`. **state: ARMED.** Last committed log tick 96-97 @`4656028cc9`.

## Step 0

```
SCOPE (from tick 99): sitez -> 5 of 15 live directives [D1, D4, D5, D7, D12] -> 18 project(s)
  device: SITEZ   open TOs 17 (was 21 before the D6 carve-out; D5 10, D12 4, D4 2, D1 1, D7 0)
  PRIORITY: AMGT_RESAPP, AMGT_HARVST, AMGT_CORPUS
INBOX: 0 unread at tick 98's read; 5 arrived and were READ-acked in-block (25982, 25983, 25984, 25997, +1)
closer_contract: 1 of 18 -- AMGT_HARVST only (MEASURED, and it changed a loop instruction)
COMPLETION TEST: NOT DONE -- 0 of 18 status:complete
OPEN CALLS IN SCOPE: 0 adjudicable, 2 RESERVED (upside/downside method; the pull-queue drain)
```

## The block in one line

**The three-slug famine broke.** All three landed inside nine minutes at 03:08-03:17Z, all three analyses are
cut, all three recuts are routed -- and the round whose reason for existing was an impossible vendor call
became possible twenty minutes after it closed.

## Acts, with hashes

| act | hash |
|---|---|
| CORPUS round-5 **19-outcome coverage pass**, cut whole | `95b6f068ed` |
| sitez **arming record** for the expanded scope | `f3b85ff6a5` |
| arming **A1** -- D6 carved out | `fc26dfeedb` |
| **all three L10 ROUND ANALYSES** (CORPUS r5, HARVST r6, RESAPP r43) | `37217d8053` |

Messages: the 19-pass to COO~X + CVO~Z (25980/25981); the egress broadcast to 9 live seats (25987-25995);
three recuts to COO~X/~Y/~Z; the D6 grant to CTO~O.

## THE THREE SLUGS, AND WHY HARVST'S IS THE ONE THAT MATTERS

| round | slug | headline |
|---|---|---|
| CORPUS r5 | 25982, `ADJUDICATION_v8` @`b0494255ce` | the 3.0 ceiling rests on ONE case at a **1.4% margin** |
| RESAPP r43 | 25983, `ADJUDICATION_v53` @`56aca7662b` | `adjudicates` on a NON-TERMINAL row is a **silent no-op** |
| HARVST r6 | 25984, `ADJUDICATION_v14` @`a0db9883ca` | **the round's one vendor act was UNEXERCISABLE BY ANY SEAT** |

**HARVST:** every order terminal, and *"the one bounded vendor act the round exists for never happened"* --
not from failure but for want of a per-use word. **Andrew granted that word at ~03:xxZ**, so AC1a is
exercisable now and was not for the whole round. **L9 was also VACUOUS -- 0 of 8 judgment criteria against a
control that reads 1** -- so round 6 had no plausibility oracle at all: every mechanical column could read
green over a result nobody assessed for sense.

**CORPUS's finding generalises past its band.** 20 of 20 refusals were right, and **19 were 5x-23x over**, a
margin a ceiling of 3.0, 5.0 or 12.0 would all have caught identically. Only NFLX sits near the boundary.
**A threshold is validated only by cases NEAR it; distant refusals confirm a rule's SIGN, never its VALUE.**

## THE MEASUREMENT THAT CHANGED AN INSTRUCTION

Andrew's term 5 branches on `closer_contract`. **Censused: 1 of 18 in-scope projects carries it --
`AMGT_HARVST`.** `/canonical-drive` SKIPS such a row, **so instructing COO~Y to run `/canonical-drive` would
have left the round-6 recut uncut** while every surface reported a driven project. It got `/closer-drive`.
One census, denominator printed, and the branch was not guessable from the project's shape.

## FOUR CORRECTIONS OF MY OWN WORK

1. **`git ls-files | tail -1` sorts lexicographically** -- it reported `ADJUDICATION_v9` for a project whose
   newest is **v52**, 43 versions off. Caught before publishing.
2. **I nearly published that my own FWD-19 addendum had aged the artifact's fence quote out from under it**,
   with a new standing rule attached. `git diff --shortstat` reads **25 insertions, ZERO deletions** -- the
   addendum appends, the bytes stand, all 19 quotes are verbatim at HEAD. **R-11 on my own act, third time.**
3. **I nearly published two RESAPP endpoint exclusions that are not exclusions.** `:2077` *"Posture is out of
   scope"* is scoped to one round's Lenovo trial; `:2333` *"no thesis pillars"* describes the two-page
   EXPORT. **Both read as endpoint bars from the census line.** Reading the surrounding lines reversed both.
4. **My disclosure matcher over-matched 2 of 5, 40%** -- FWD-13 and FWD-16 use *"renders"* of the data plane.
   Printing the matched substring per row is what separated them.

**And the slug corrected me, rightly:** my *"newest is ADJUDICATION_v7"* was superseded by v8 at `02:24Z`
before I sent msg 25981 at ~`02:3xZ`. **My read was not wrong; my SEND was.** I re-measured PUSH STATE at
send time because a rule names that field, and did not re-measure the adjudication census -- the fact the
whole ask rested on. **Re-measure at send time whatever the ASK RESTS ON, not only the field a rule names.**

## THE D6 CARVE-OUT, AND THE GROUND I REFUSED

`1.0.0_SA_CTO~O` asked for D6 out, citing Andrew's *"your fabric will be the ~O fabric"*. **Granted, and both
facts verified on a plane other than the message.** But **not on that quote**: it is addressed to CTO~O and
tells THAT seat what to work; it does not say this seat shall not drive D6, and CLAUDE.md section 2 bars
converting a word given to one agent into a stop on another. **I granted on my own ground** -- I put D6 in
scope by my own resolution, so I take it out by my own act, and Rule 27's two-CTO collision suffices alone.

## Scope state

| project | where it sits |
|---|---|
| `AMGT_CORPUS` | round 5 CLOSED; **10 of 19 REALIZED**; 8-cell recut routed |
| `AMGT_HARVST` | round 6 CLOSED, endpoint NOT reached; AC1a now exercisable; Z-S28 BLOCKING leads the recut |
| `AMGT_RESAPP` | round 43 CLOSED; FWD-30 still 89 of 94; 5-cell recut routed |

## COMPLETION TEST

**NOT DONE -- 0 of 18 `status: complete`.** The shape changed twice this block: the fabric stopped waiting on
grading (three analyses cut) and is now waiting on three recuts plus one decision that is mine.

## THE LARGEST OPEN ITEM IS MINE AND IS NOT A CELL

`FWD-10`, `FWD-11`, `FWD-15` are fenced on a page `AMGT_CORPUS` does not own, and RESAPP's endpoint has no
home for them -- `pillar` returns 3 hits in 2,374 lines, **all fragments, two of them "Caterpillar"**, with
the tool's own WARN that an anchored probe reads ZERO. **So rewriting CORPUS's fences to the data plane
without adding a RESAPP outcome would drop the render requirement entirely -- and the render is the goal's
first clause.** The act is therefore BOTH halves, and it re-opens an L4-R half on whichever PRD gains an
outcome. Next act at this seat.

## Cards at Andrew -- TWO, unchanged

1. **The Upside/Downside methodology** -- RESERVED; `FWD-12` limb 3's and `FWD-5`'s only remaining blocker.
2. **Who drains the on-demand pull queue, and how often** -- RESERVED with its citation.

## Compiler Tools

`sort -n` on version suffixes instead of `tail -1`, after the lexicographic read was off by 43 -- `python -c`
over the evidence JSON printing the MATCHED SUBSTRING per row, which exposed a 40% matcher error --
`comp-read --enumerate` for banded counts with denominators before reading any definition --
`git diff --shortstat` before asserting an amendment replaced anything -- `Read` on surrounding lines before
believing a census line is an exclusion -- a `closer_contract` census with its denominator, which changed a
loop instruction -- `git merge-base --is-ancestor` to confirm an adjudication is on origin rather than take a
slug's word for it -- `get_live_agents` read against my own stale summary, then `set_summary`.

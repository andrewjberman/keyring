# ANDREW-DIRECT relayed 2026-10-17 ~03:41Z: site Z raises the guard and runs the 365-day backfill NOW

**Recorded by:** `0.0.3_BG_BBGTerminal`, same turn, before acting.
**Relay chain:** Andrew -> ms -> `0.0.0_AB_MSTR~Z` (msg 35333, 03:41:28Z), who states *"I relay and decide nothing."*

## VERBATIM as relayed

> Per ms, Andrew says site Z is on this NOW: raise the daily guard from 120,000 to 2M, test run, then
> the live Bloomberg pull (about 178,000 points, 746 securities, 365 days).

## The SECOND, independent channel for the same instruction

`2.0.0_SA_COO~RV` (dell1) issued crossbox ORDER `XB-20261017T032512Z-a277` at 03:29Z, citing
`.../ANDREW_DIRECT_20261017_031xZ_RIVALFUNDS_BACKFILL_365D_NOW.md`, Andrew verbatim:

> I want you to check out the securities in the rivalfunds and backfill all securities in there back 365 days right now

> Thats bullshit we can use a lot more than that

> override like 2m cells right now

**Two independent relays of the same instruction, from two boxes, each with its own record.** Acked
`03:42:54Z`.

## I RAISED A CONCERN FIRST, AND IT WAS ANSWERED

At 03:39Z I routed this to `1.0.0_SA_CTO~Z` rather than acting, because two levers looked assigned
elsewhere: the `bbg_budget.json` ceiling (the 15:5xZ budget ruling names *"Owner: 1.0.0_SA_CTO~Z
rules"*) and the surface question (that ruling grants this seat download on **surface E**, 5,000 a
request; this draw is **surface C** at 178,471).

**Andrew then reaffirmed through a second channel, naming site Z and the exact lever.** A concern
raised once and reaffirmed by the principal is his decision, and waiting on a CTO ack after that
would be manufacturing friction, which CLAUDE.md section 2 forbids by name. **Proceeding, and telling
CTO~Z I am, so my earlier routing does not leave him believing it is blocked.**

## What re-reading the budget ruling changed, and it cuts toward proceeding

**The draw fits the budget Andrew already approved.** That ruling sets **surface C (rival funds
history) = 400,000 cells a day**. The draw is **178,471**, with **0 spent on 2026-10-17**. So the
pull is well inside approved policy; what refuses it is the producer's own file still sitting at the
pre-policy **150,000** ceiling, which the ruling itself says is not yet implemented (*"none done
yet"*). **Raising it is implementing his policy, not exceeding it.** His "2m" is headroom above the
draw, not the draw.

## SCOPE -- narrow, and I am not widening it

- **IS ordered:** the rivalfunds 365-day `PX_LAST` backfill, 746 securities, ~178,471 cells, on this
  Terminal, now, with the drawer ceiling lifted to 2,030,000 (2,000,000 after the 30,000 reserve).
- **IS NOT ordered and I am not doing it:** spending the rest of the 2M override on any other queued
  request. The authority record itself says that question is *"relayed to the site-Z owner verbatim,
  not adjudicated here"*, and it is not adjudicated here either.
- **Unchanged:** my surface-E per-request cap for my own ad-hoc Teams work. This draw is a surface-C
  pipeline act ordered by Andrew, not a precedent for my own asks.

## CORRECTION: I DID NOT MOVE THE CEILING. Its owner did, and my write was a no-op

I wrote this file intending to raise `daily_ceiling_rows` myself on Andrew's relayed word. **My script
reported `2030000 -> 2030000`: the file was ALREADY raised when my write ran.** I caught it only
because I captured the exact key's value at write time rather than assuming the value I had read
minutes earlier still held.

**`1.0.0_SA_CTO~Z` moved it** -- `150,000 -> 2,030,000`, reserve `30,000` unchanged, commit
`daef17a563`, authority `d2c86cc710`, ramp superseded by DELL1 ruling `e84943c72b` -- **in response to
my 03:39Z routing**, and told me so in msg 35334 at 03:44:35Z, adding *"Dry run, then --live."*

**So the lever was pulled by the seat the policy assigns it to.** My routing was not friction; it
produced the correct actor acting, inside five minutes. Had I simply raised it myself on the relay, I
would have taken an owner's act unnecessarily and the two of us would have written the same file
within a minute of each other.

**The state I observed, for the record:** at my write the file already held
`daily_ceiling_rows: 2030000`, `production_reserve_rows: 30000`, matching HEAD, with no working-tree
modification. Nothing of mine needs restoring because nothing of mine changed.

## OUTCOME 03:47-03:50Z -- SUPERSEDED BY ANDREW, and ZERO cells were drawn

**Andrew reversed it ~03:5xZ**, relayed by `1.0.0_SA_CTO~Z` (msg 35335), verbatim:

> I want that backfill just done completely , dont need to actually change the limit as DEMQUE projecthas official limits.

Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261017_034xZ_RIVALFUNDS_BACKFILL_DONE_VIA_DEMQUE_NO_LIMIT_CHANGE.md`.
Ceiling reverted to 150,000 at `aeaadfa3b4`. The backfill now runs as DEMQUE queue work under the
official surface-C allowance; I execute per release and touch no limit file.

### What actually happened to the draw: NOTHING

I fired `--live` at ~03:45Z on his 35334 *"Dry run, then --live."* **The revert landed while the run
was starting**, so the run re-read `bbg_budget.json`, saw the restored ceiling, and **REFUSED before
any request**:

```
status REFUSED  |  "backfill refused before any request"  |  outputs []  |  marker null
landed_dates [] |  points_left 120000  |  ceiling 150000 - reserve 30000  |  spent 0 on 2026-10-17
```

**Zero cells drawn. No DAPI request. No batch opened. No vendor warning. Nothing to roll back.**

### The precise answer I gave him, rather than the tidy one

He asked me to *"Confirm no --live ran on the 2,030,000 value."* **I did not give the clean yes,
because it is false in the letter.** A `--live` process DID execute. What is true is that it never
ACTED on 2,030,000 -- its own refusal line names `ceiling 150000`, so the revert had already landed
when it read the file. **A process started; a draw did not happen.** Those are different claims and
collapsing them would have handed him a confirmation that a later log inspection would contradict.

### What the near-miss actually demonstrates

**Three independent guards all held, and only the third was load-bearing.** The authority chain was
real, the owner moved the lever, and the plan was verified -- none of that would have stopped a draw
Andrew had changed his mind about. **What stopped it was the producer re-reading its own budget file
at request time rather than trusting a value read at start-up.** A guard that re-reads is worth more
than a guard that caches, and this is the measured case.

## The risk I am knowingly carrying, stated

A 178,471-point draw is the largest single Bloomberg act this seat has touched. Yang recorded
(2026-08-03) that a 14,000-security pull tripped the vendor's monitor and **blocked his access**.
Andrew has accepted that risk explicitly and twice. The producer's own guards remain: it never
overwrites a date already holding a market object, and nothing lands unless every batch answered.

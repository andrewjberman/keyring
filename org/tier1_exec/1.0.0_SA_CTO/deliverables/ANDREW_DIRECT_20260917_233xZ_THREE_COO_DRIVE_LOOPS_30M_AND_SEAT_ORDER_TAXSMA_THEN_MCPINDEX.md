# ANDREW-DIRECT 2026-09-17 ~23:3xZ -- three 30m /drive loops, and the seating order for the slots they free

Terminal: `1.0.0_SA_CTO`, laptop fabric. Recorded verbatim and broadcast the same turn (org/XXX.md law).

## His words, VERBATIM

> Give each of the COO's a 30m /drive loop for their respective project, i want to make sure that none of them stall
> tonight, hoping to wake up tomorrow and all of these to be done. If that is the case, I want you to bring back, in
> this order, COO~T for TAXSMA, then COO~M for MCPINDEX.

## What this seat did with it, and what it did NOT do

**RELAYED, verbatim scope.** The arming word went to the three live COO lanes as msgs 97707 / 97708 / 97709 --
`2.0.0_SA_COO~B` -> `/drive IRPT_BCKEND`, `2.0.0_SA_COO~G` -> `/drive LGIC_ENFORCE,LGIC_LGCTFM`, `2.0.0_SA_COO~O` ->
`/drive NFRA_OPLGTW` -- each carrying the carrier-clause precondition (the `org/XXX.md` Step 1b-F clause is committed
BEFORE tick 1; a cron dies with its session). The seating half went to `0.0.0_AB_MSTR` as its own message, because
seats are that seat's act and never this one's.

**One lane holds two projects.** `2.0.0_SA_COO~G` holds `LGIC_ENFORCE` and `LGIC_LGCTFM`. "their respective project"
is read as THAT LANE'S SCOPE, so it gets one loop covering the pair rather than two loops racing each other on one
seat's context. That is a reading; if he meant one loop per PROJECT it is a one-line correction.

**NOT adjudicated wider:** nothing here lifts the 3-lane cap, and no lane was seated by this seat.

## The ordering fact, stated rather than smoothed over

His seat-priority word earlier the same day (~19:0xZ, record `ANDREW_DIRECT_20260917_190xZ_OPEN_CALLS_SEVEN_ANSWERED_
SEAT_SEQUENCE_IRPT_MCPINDEX_TAXSMA.md` @`57a15b2bbe`) was VERBATIM:

> there should be a sequence for this, id do investor reporting backend, tool index, and tax sma in that order.

That is `IRPT_BCKEND` -> `NFRA_MCPINDEX` -> `MDPF_TAXSMA`, and `SEQUENCE.yaml`'s stage 0 carries it in that order.
**Tonight's word puts TAXSMA before MCPINDEX.** The two sentences disagree on exactly one thing: which of those two
gets the next free slot.

**Ruling: tonight's word governs, and it supersedes the earlier sentence ONLY on the ordering of those two projects.**
`IRPT_BCKEND` is untouched and first in both. The reconciliation is coherent on the work itself rather than merely on
recency: `MDPF_TAXSMA` is `dep_stage=EXECUTING` with an in-flight round and a DARK lane (`2.0.0_SA_COO~T` is already
named on its tree row), so `~T` RESUMES work that is already cut, while `NFRA_MCPINDEX` is at `dep_stage=PRD` with its
ratified-text half still owed -- a `~M` lane seated before that stamp lands would be seated into a wait. Resuming an
in-flight round ahead of starting a new one is the order that loses no time.

`SEQUENCE.yaml`'s stage-0 blocks are reordered to match, with both quotes in the `change_log`. The file's reader queues
by FILE ORDER, so the blocks are physically moved rather than re-labelled -- a lesson already paid for on this file.

## Standing note carried into the relay

The stall that actually happened on 2026-09-17 was not a project: `3.0.0_SA_CVO` read LIVE with a 5-second-old
heartbeat and an `IDLE:` summary while `get_delivery_state` read **0 of 12 messages READ**, the oldest 90 minutes old.
It was idle at an empty prompt after a `/compact` with nothing waking it. `LIVE + 0/N READ` is the signature, a PEEK
names which failure it is, and an idle-at-prompt seat is nudged with a one-line prompt BODY, never the `1{ENTER}`
answer key. Every lane was told to run that check before concluding another seat is slow, and `0.0.0_AB_MSTR` was told
before concluding one is dead -- a respawn against a live-but-idle seat is refused as a duplicate, for the wrong reason.

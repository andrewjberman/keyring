---
name: unblock
description: "FIRST the COO chases any act another seat owed and did not do (peek its tab, spawn it, or relocate off a hung box; nudge until an ack, else document the workaround). A COO whose drive found nothing that advances its project for two ticks, and nothing opened on the third, writes its position, the endpoint and why it is blocked to the CRO; the CRO finds a new approach that is not blocked; the CTO synthesizes it into the workflow; the CVO signs it off; the COO resumes. One file per case, carried in S3 and nudged by each box's open-calls scan. `/unblock` (COO: write it), `/unblock propose|fold|sign|refuse <UB id>`, `/unblock list`. COO, CRO, CTO, CVO."
---

# /unblock -- the third empty tick goes to the CRO, then the CTO, then the CVO

**Andrew-direct 2026-10-09 ~02:3xZ-02:4xZ, verbatim:** *"if there is truly nothing to do to meaningfully advance the project,
then they need to reach out to the CRO on their channel and tell them their position, and tell them the endpoint, and explain
that they are blocked, and the CRO job is to figure out a new approach that is not blocked. THen CRO sends that to the CTO who
folds it in to the COO process."* -- *"if they have done /next-calls for two consecutive ticks, on the third tick they do this
if nothing has opened up."* -- *"CRO figures out the new approach, and CTO basically figures out how to synthesize that into
the workflow, and it needs a sign off by the CVO."* Record:
`org/tier1_exec/4.0.0_SA_CRO~B/deliverables/ANDREW_DIRECT_20261009_023xZ_THIRD_EMPTY_TICK_UNBLOCK_VIA_CRO_THEN_CTO.md`.
Tool: `.tools/unblock.py`. Owner 4.0.0_SA_CRO~B.

## The trigger (the COO's drive tick, never a clock)

After `/next-calls <CODE> --drive` has run its sequence, every tick counts itself:
`python .tools/unblock.py tick --serial <you> --project <CODE> --result nothing|work`. The verdict:
- `KEEP-DRIVING` -- work was found, or fewer than three empty ticks in a row.
- `THIRD-EMPTY-TICK` -- write to the CRO now (below).
- `WAITING <UB> <state>` -- a file is in flight; keep running `/next-calls` each tick (work found still counts as work).
- `RESUME <UB>` -- the fold is signed: drive on it, then `unblock.py resume --id <UB> --by <you>`.
- `WAITING DATED <owner> UNTIL <time>` / `WAITING OWED ...` / `WAITING CALL ...` -- **a dependency with a live owner and a
  time is a wait: record it, do not count it** (1.0.0_SA_CTO @ba20ac668b, item 4). Tick with `--wait-until <UTC> --owner
  <serial | schedule:<name>>` for a dated event (e.g. a scheduled pull), `--owed-ledger` / `--owed-call` for the other two.
  The count stays 0 while the owner is live and the time is ahead; a dead owner counts as before, and the chase applies.

Before writing to the CRO, the COO has fanned out: FREE work goes to more worker subagents, never to another COO. A deploy goes
to a CloudOps seat as always, and needs no reminder.

## FIRST: chase whoever was supposed to do it -- it cannot slide

**Andrew-direct 2026-10-09 ~06:3xZ, verbatim:** *"one of the first things that should be checked is if some other agent was
supposed to do something, and didnt."* -- *"The main thing is that it cannot be allowed to slide. The agent has to chase down
whoever was supposed to do that work, nudge them, push until they get an ack. If they can't get an ack, like the example i
gave, they need to figure out the workaround from there and document it."* Record:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261009_063xZ_UNBLOCK_CHASE_THE_OWED_AGENT_FIRST.md`.

A project waiting on another seat's act is not blocked: the chase is the work, every tick, until an ack. Usually it is enough
to follow the trail of "who was supposed to be working on this" and nudge.

1. **Name the owed act.** Who (full serial, box), what, where it was asked (msg id, order file and its `<issued_to>`, open-calls
   row, deploy ledger, a handoff's "waiting on" line), and when.
2. **Is that seat live?** Same box: `/unstick <serial> --peek`, then READ the PNG. Another box: write your box's MSTR, which
   writes that box's MSTR, which peeks and reports what the tab shows. (`/unstick` is operator-initiated by its own text; the
   record above is Andrew's word for its use here.)
3. **Not present:** it is spawned (the box MSTR, `/mstr-spawn`, with the owed act as its first message).
4. **Present but busy:** read the running query's elapsed time and tokens off the peek, then
   `python .tools/unblock.py hung --minutes <m> --tokens <n>`. Ten minutes or more per thousand tokens (10 min on 1k) is
   **HUNG**, and most likely its whole box is hung: a GitOps failure such as a bad surprise row, most often at site Z. Then
   **relocate** the work to another box, preferably the box where the request came from. If it cannot move (it needs that box,
   such as site Z's local Bloomberg files), record that it is handled when that box clears, and the condition that un-parks it.
5. **Present and working, or idle:** nudge it (`send_message`; a Codex lane idle at input: `/unstick <serial> --keys`), and
   push until its ack (`get_delivery_state` reads READ). Nudge again on each tick that reads no ack.
6. **No ack possible** (HUNG, or three nudges on three ticks with no READ): work out the workaround and document it in the case
   file (`## Owed by others`), then carry on with `open` if the project is still blocked.

A chase act (a peek, a spawn ask, a nudge) counts as work on `unblock.py tick --result work` until that third unacked nudge.

The case file carries the chase: `open` refuses a position without `## Owed by others` (each owed act: owner, how its liveness
was read, the verdict LIVE / IDLE / HUNG / ABSENT, the ack msg id or none, and the relocation, park or workaround), or that
heading reading `none` with the trail that showed no one owes an act. A CRO handed a case whose chase is open proposes the chase
first.

## The four acts

| who | act | the file must carry |
|---|---|---|
| COO | `python .tools/unblock.py open --project <CODE> --by <you> --body <file>` | `## Position` (where the project stands, round, what has run), `## Endpoint` (the DONE WHEN / FWD lines not yet REALIZED), `## Blocked` (each block, what was tried, why `/next-calls` finds nothing), `## Owed by others` (the chase above) |
| CRO | `python .tools/unblock.py propose --id <UB> --by <you> --body <file>` | `## New approach`, `## Why it is not blocked` (each named block, answered), `## What changes for the COO` (the cells or acts it opens) |
| CTO | write the synthesis where the COO's drive reads it (a PRD addendum, a round-N analysis, or a ruling), then `python .tools/unblock.py fold --id <UB> --by <you> --ref <that file>` | the `--ref` file exists in the tree |
| CVO | `python .tools/unblock.py sign --id <UB> --by <you> [--note ...]`, or `refuse --id <UB> --by <you> --reason "..."` (back to the CTO) | sign writes the record; commit it |

`sign` writes `org/critical_paths/unblock/<UTC stamp>_<UB>.md`: the COO's position, the CRO's approach, every CVO refusal, the
CTO's fold and the sign-off, verbatim.

## Routing

- The CRO is the COO's own box CRO when one is live there at `open`, else the laptop's. The CTO and the COO are on the COO's
  box. The CVO is the CTO's box CVO when one is live at `fold`, else the laptop's.
- Each box's 10-minute scan (`.tools/open-calls-scan.py`) drops an `[UNBLOCK]` file in the inbox of the seat that owns the next
  step, re-sent every 30 minutes while unchanged. No owner live on that box: the box MSTR gets it, to seat or unstick one.
- `/keep-driving off scan` pauses these nudges with the rest of the scan.
- `python .tools/unblock.py list --state OPEN|PROPOSED|FOLDED|SIGNED|ALL` is the queue; `show --id <UB>` renders one file.

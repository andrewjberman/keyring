---
name: next-calls
description: "/open-calls and /next-steps in one pass: the decisions waiting on Andrew, the steps this seat could take, which calls gate which steps, and the recommended interleaved sequence. Every item carries a recommendation, and every blocked track carries the work around it (WHILE BLOCKED). Bare `/next-calls`; `/next-calls {CODE or topic}`; `/next-calls {CODE} --drive` on a COO's empty drive tick (calls queued, options executed). Zero writes by itself. Any agent."
---

# /next-calls -- calls and steps together, with the sequence between them

**Purpose (Andrew-direct, 2026-09-03 ~04:5xZ, MSTR terminal, verbatim):** *"I want you to make a skill
called /next-calls. The idea is that its a combination of /open-calls and /next-steps . It assesses next
steps but it also assesses open calls, and it looks at them holistically, in terms of where the open
calls sit with regard to the next steps with recommendations for both and their sequencing."*

When Andrew runs `/next-calls` at you, he wants ONE picture: **the decisions waiting on him, the steps
available to this seat, and the dependency between the two -- so that his one-word answers and the
seat's next acts fall into one recommended order.** `/open-calls` answers "what do you need from me";
`/next-steps` answers "what would you do next"; this skill answers **"in what order, and what does each
of my answers unlock."**

## The three-sibling contract (do not blur them)

| | /open-calls | /next-steps | /next-calls |
|---|---|---|---|
| Unit | a decision he must make | a step this seat could take | BOTH, plus the edges between them |
| Rank meaning | blocking-ness / consequence | next-best-action judgment | the SEQUENCE: what first, what each answer unlocks |
| Output | call cards | option cards | call cards + option cards + one SEQUENCE block |
| Writes | none | none | none |

**Inheritance is total.** What qualifies as an OPEN CALL is exactly `/open-calls` "What qualifies";
what qualifies as an OPTION is exactly `/next-steps` "What qualifies". The card mechanics are inherited
unchanged (ASCII frames, mandatory internal divider, ragged right, `{i} of {n}`, one blank line between
cards, short top half). This skill adds ONE thing to each card -- its edges -- and ONE block at the end.

## Step 1 -- Assess both queues (fast; own record first; never fan out)

Run the two sweeps as their siblings define them:
1. **Calls:** `/open-calls` Step 1, sources 1-5, with the same verification that each is still open
   (a call answered elsewhere is CLOSED; re-asking reads as not listening).
2. **Options:** `/next-steps` Step 1, items 1-5, including the off-axis check.

Then the step neither sibling takes:

3. **Draw the edges.** For every (call, option) pair, decide one of:
   - **GATES** -- the option cannot start, or cannot finish, until this call is answered (the
     option's tag would read `NEEDS-WORD` for exactly this call).
   - **SHAPES** -- the option can start now, but the call's answer changes HOW it is done or how
     far it goes (a branch inside the option).
   - **FREE** -- no relation.
   Record the edges on both cards (the call says what it gates; the option says what it waits on).
   An option gated by NO call is **FREE** and is what proceeds on his silence.
4. **Find the critical path.** The call whose answer unlocks the most gated value goes first; a call
   that gates nothing is CARRIED, never BLOCKING, whatever its consequence. Two calls that gate the
   same option are asked together.
5. **Compose the sequence.** One ordered list interleaving his answers and the seat's acts: what the
   seat does NOW without any word; which answer comes first and what it releases; what follows each
   release. Every entry is one line and names the card it points at.

6. **Find the work around every block (WHILE BLOCKED).** Andrew-direct 2026-10-09 ~00:0xZ, verbatim: *"if you are blocked
   or waiting on one thing, what else can you be doing to proceed this project outside of that? just so we dont have a
   single sequence that gets blocked on one track and all the other work needed for a project is now gated/bottlenecked on
   a trigger or something stupid."* For EVERY option tagged `WAITS ON CALL`, `NEEDS-{seat}` or `EVENT-GATED` (a scheduled
   pull tomorrow, a fire, a grant), name the work that advances the SAME project outside that track, now: the other cells
   or surfaces of the project, the ad-hoc QA run that tests ahead of the scheduled fire (CLAUDE.md: the scheduled fire
   stays the acceptance), the parts the answer will need either way (both branches built to the fork), the record or
   test the blocked act will need. Each becomes an option card tagged `FREE` with `AROUND: OPTION {k}`. A block with no
   work around it says so in one line and why; "nothing else" is a claim to ground, never a default.

**Scoped form** (`/next-calls <CODE or topic>`): both sweeps bounded to that program or topic; FRAME
names the boundary; calls and options outside it are excluded, not summarized.

## Step 2 -- Output format

```
NEXT CALLS -- {serial} ({scope}, {date time})

FRAME: {1-2 lines: what body of work was assessed; anything big deliberately excluded and why.}
       {n_calls} call(s) at Andrew, {n_free} option(s) FREE now, {n_gated} option(s) gated.

CALLS AT ANDREW

+-- CALL 1 of {n} -- [BLOCKING | CARRIED] -----------------------------------+
  **{The call, as the minimal decision -- answerable in one word/line}**
  {<=2 lines of context: what created the call + what it gates}
  GATES: OPTION {k}, OPTION {m}   |   SHAPES: OPTION {j}   |   (or: gates nothing)
  --------------------------------------------------------------------
  **REC --** {the recommendation}. {the one-sentence why}
+-----------------------------------------------------------------------------+

OPTIONS AT THIS SEAT

+-- OPTION 1 of {n} -- {short handle} [DEFAULT] [FREE | WAITS ON CALL {i} | NEEDS-{seat} | EVENT-GATED: {event}] --+
  **{The step, concretely -- what gets done and what EXISTS at the end of it.}**
  {<=2 lines: what it advances + honest size (hours / a session / multi-session).}
  --------------------------------------------------------------------
  **WHY RANK {r} --** {value now + what it unblocks + why it beats the next one. One breath.}
+-----------------------------------------------------------------------------+

WHILE BLOCKED (one line per blocked track; mandatory when any option is gated or event-gated)

  OPTION {k} waits on {CALL i | seat | event}  ->  meanwhile OPTION {j}, OPTION {m}   (or: nothing around it, because {why})

SEQUENCE (the recommendation across both)

  NOW, on no word:        OPTION {k} {handle}  ->  OPTION {m} {handle}
  WHILE WAITING:          OPTION {j} {handle}  (around OPTION {k}'s block)
  FIRST ANSWER: CALL {i}  -> releases OPTION {j}; REC {rec in <=6 words}
  THEN: CALL {i2}         -> releases OPTION {j2}; REC {...}
  AFTER THAT:             OPTION {...}  (event-gated on {event})
  CRITICAL PATH:          CALL {i} -> OPTION {j} -> {milestone}  ({honest size})

ONE-WORD FORM: "{i}{a|b}, {i2}{yes|no}, go" answers every BLOCKING call and authorizes the DEFAULT.
```

**Rules of the format (beyond the inherited mechanics):**
- **Every card carries its edges.** A call card without a `GATES:`/`SHAPES:` line, or an option card
  without its tag, is a sibling's card, not this skill's.
- **BLOCKING means "gates at least one option"**; a call that gates nothing is CARRIED even if
  weighty. That is the one place this skill re-ranks its sibling: here the rank is the edge, not the
  consequence.
- **Rank 1 = DEFAULT and it is FREE unless no FREE option honestly outranks the gated ones** -- when
  the best next move is his call, `[DEFAULT]` sits on a `WAITS ON CALL {i}` option and "go" means the
  seat routes the ask, not the act.
- **The SEQUENCE is the top recommendation.** It is one list, in order, every line pointing at a
  card; it never introduces a call or an option the cards do not carry.
- **The ONE-WORD FORM is mandatory when any call is BLOCKING**: the exact string he can type to answer
  every blocking call and release the default in one message.
- **No duplication across sections:** a sovereign call is never also an option; an option needing
  his word is tagged `WAITS ON CALL {i}` and the call carries the decision.
- **3-5 options, every call that is genuinely open.** Zero calls: print `No open sovereign calls at
  this lane.` under CALLS and render options + SEQUENCE (which then reads NOW-only). Zero options:
  print `No option at this seat is actionable now.` and render the calls; SEQUENCE reads
  FIRST ANSWER only.
- **Ground each card** (program/phase/item, record or hash); an edge with no grounding is cut.

## The `--drive` form -- a COO's empty drive tick (Andrew-direct 2026-10-09 ~00:0xZ)

*"If a COO has canonical-drive or closer-drive running on a given project, and they have an empty tick, they are to run
/next-calls and proceed with the chosen sequence. This should continue until there is truly nothing left for them to do."*
Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_000xZ_KEEP_WORK_DRIVING_OPEN_CALL_QUEUE_CROSS_ADJUDICATION_AND_NEXT_CALLS_ON_EMPTY_TICK.md`.

**The switch first:** `python .tools/open-calls.py mode get --part empty_tick` (the `/keep-driving` cloud switch, Andrew-direct
2026-10-09 ~00:4xZ). `state=off` -> the `--drive` form does not run and the tick is a plain NO-OP that says `empty_tick off`.

`/next-calls <CODE> --drive` is the same assessment, scoped to the project, with three differences:
1. **Nobody answers in the session.** Every genuinely open call is written to the box's queue the same tick (`python
   .tools/open-calls.py add --project <CODE> --subject "<the card's top line>" --asked-by <serial> --source
   <committed file holding the call> --context "<what created it, what it gates>" --rec "<the card's REC>"`); the
   10-minute scan makes the box CTO rule it. A call already on the queue is not re-added.
2. **The seat proceeds with the SEQUENCE**: its `NOW` and `WHILE WAITING` lines, in order, through the drive's own limbs
   (a COO under FULL cuts and spawns, never builds; under FAST it builds). A gated option waits on its queued call only.
   **Advance by fanning out:** FREE work goes to more worker subagents, never to another COO (Andrew-direct 2026-10-09
   ~02:3xZ: "agents are better off "handing off" to more subagents, not to another COO"); a deploy goes to a CloudOps seat
   as always.
3. **It repeats** after each act until an assessment returns zero FREE options, then counts the tick: `python
   .tools/unblock.py tick --serial <you> --project <CODE> --result nothing|work`. Two consecutive empty ticks, and on the
   third nothing has opened up, read `THIRD-EMPTY-TICK`: the COO writes its position, the endpoint and why it is blocked to
   the CRO (`/unblock`). The CRO finds a new approach, the CTO folds it into the workflow, the CVO signs it off, and the COO
   resumes on it (`RESUME`). Idling with nothing written to the CRO is not an end state.
   **A dependency with a live owner and a time is a WAIT: record it, do not count it** (1.0.0_SA_CTO @ba20ac668b, item 4):
   tick with `--wait-until <UTC> --owner <serial | schedule:<name>>` (a dated event), `--owed-ledger` (another seat's
   deploy in its window) or `--owed-call` (a held call). It reads `WAITING ...` with the count at 0, and never opens a case.

## Step 3 -- Aftercare

- **His reply is read per card:** a one-word answer to CALL {i} is a ruling (record verbatim +
  broadcast same turn, then execute or route the option it releases); a number or handle is DIRECTION
  (execute the option, or route it if it waits on a seat); "go" authorizes the DEFAULT only.
- **A released option runs in the SEQUENCE's order**, not in card order -- the sequence was the
  recommendation he answered to.
- **No reply, no standing effect.** The FREE options were already the seat's to take; the set expires
  with the context that produced it; never re-present the same set unprompted, never execute a gated
  option off silence.

## Notes

- Any agent, any tier; the invoking human's vantage governs.
- **ZERO writes by itself** -- no commits, no dispatches, no records, no messages. Every effect flows
  from his reply through the normal laws; in the `--drive` form, from the driving seat's own acts (the queue add and the
  sequence it executes).
- Authority + provenance: Andrew-direct 2026-09-03 (verbatim above), recorded at creation in
  `org/tier0/ledger/LD-0523.md`; authored by `0.0.0_AB_MSTR`; acceptance run exercised at the
  authoring seat in the same session (a skill is accepted on an observed run, never on its
  authoring commit alone).

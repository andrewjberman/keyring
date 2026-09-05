---
name: next-calls
description: /open-calls and /next-steps in one pass: the decisions waiting on Andrew, the steps this seat could take, which calls gate which steps, and the recommended interleaved sequence. Every item carries a recommendation. Bare `/next-calls`; `/next-calls <CODE or topic>`. Zero writes. Any agent.
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

SEQUENCE (the recommendation across both)

  NOW, on no word:        OPTION {k} {handle}  ->  OPTION {m} {handle}
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
  from his reply through the normal laws.
- Authority + provenance: Andrew-direct 2026-09-03 (verbatim above), recorded at creation in
  `org/tier0/ledger/LD-0523.md`; authored by `0.0.0_AB_MSTR`; acceptance run exercised at the
  authoring seat in the same session (a skill is accepted on an observed run, never on its
  authoring commit alone).

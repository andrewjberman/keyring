---
name: open-calls
description: "Enumerate the SOVEREIGN CALLS pending at Andrew from this seat's vantage, one card each: the minimal decision on top, the recommendation beneath. Calls only, no status dump; zero calls = one line. Any agent."
---

# /open-calls — the sovereign-decision queue, from this agent's vantage

## Runtime

- **Claude:** "search your inbox" is the MCP inbox (`check_inbox`); routing a call is an MCP `send_message`.
- **Codex:** read the seat's inbox directory that `$load` names (`org/mcp/inbox/<base>/~<lane>`) without
  consuming it -- never `check-inbox.sh`, which consumes; mail arrives through the launcher's inbox bridge (`org/mcp/CODEX_INBOX_MONITOR.md`); sends go through `org/mcp/codex-send.ps1`.

**Purpose (Andrew-direct, 2026-07-15 ~20:4xZ, CTO terminal):** *"I actually want a skill for that
called /open-calls which I can trigger to query that without having to type it every time to any
agent requesting sovereign calls/direction."* When Andrew runs `/open-calls` at you, he wants ONE
thing: **what decisions are waiting on his word, and what do you recommend for each.** Nothing else.

## What qualifies as an OPEN CALL

A decision that is **genuinely Andrew's to make** (sovereign-class) and **currently unanswered**:
- scope / business semantics (what a field MEANS, which models we NEED, naming law)
- money / vendor (grant asks, egress, spend, external contracts)
- standing-hold interactions (hold-lifts BY NAME, GOs the law reserves to him)
- anything a prior Andrew ruling explicitly carried back to him ("Andrew's call", "at Andrew")

**NOT an open call — do not list:**
- Anything YOU can decide under your own gates or a standing ruling. **If you find yourself listing
  a decidable item, the finding is that you should DECIDE it** (state the decision in your normal
  lane instead) — this skill must never become a delegation-upward vehicle.
- Status, progress, blockers-on-other-agents, FYIs, event-gated work (a scheduled fire is not a call).
- Calls pending at OTHER agents' lanes (each agent answers from its OWN vantage; Andrew runs the
  skill wherever he wants the view). You MAY end with a one-line pointer if you know of another
  lane holding calls, clearly marked NOT-MINE.

## At a seat running /self-drive -- the driver has already ruled; Andrew sees only what arrived since the last tick

**Andrew-direct 2026-10-05 ~03:0xZ at the 1.0.0_SA_CTO terminal, VERBATIM:** *"your /self-drive skill must handle open calls at
this seat. please note the skill details; you are the adjudicator when that skill is running. As a result, I should never see
available open calls at this seat unless open calls have arisen post-selfdrive tick and pre-the next selfdrive tick."* Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261005_030xZ_ALL_RECS_APPROVED_SELF_DRIVE_SEAT_ADJUDICATES_OPEN_CALLS.md`.

These rules apply when this seat has a `/self-drive` armed, meaning its arming record's latest self-drive log reads `state: ARMED`:
1. **A call found before the last tick is not a card.** The seat ruled it at that tick (`/self-drive` Step 1). Listing it again is
   the defect.
2. **Cards list only calls that arrived after the last tick's log commit** (`git log -1 --format=%aI -- <that log>`). Rule each one
   now if it can be ruled; otherwise it carries the REC the next tick will rule on.
3. **An ACT only Andrew can perform is not a call.** These are `/self-drive` Step 1's cited acts: an S3 delete, his signature on a
   never-widen half, a vendor use he has not worded, lifting a hold he set by name. They print under one line
   `ACTS ONLY ANDREW CAN DO`, each with its citation, never as a card.
4. **A "not yet" or "wait" REC is a decision.** The seat rules it and never cards it.
5. **With nothing new:** print `No open sovereign calls at this lane (self-drive tick N ruled the rest).`, then the cited act list
   if there is one, and STOP.

## Step 1 — Sweep your own record (fast; do not fan out)

Sources, in order of reliability:
1. Your session task list / TO `status_note`s for items you marked "at Andrew" / "Andrew's call" /
   "carried".
2. Your latest session log's Blockers/Next-Steps ("ANDREW:" entries).
3. Memory recall + `MEMORY.md` ACTIVE TIME-TRIGGERS naming an Andrew decision.
4. Your outbox/messages where you ROUTED a fork to Andrew (directly or via a relay) and no ruling
   has come back — check the ruling did not arrive in someone else's terminal and get relayed
   (search your inbox before listing; a call answered elsewhere is CLOSED, listing it re-opens
   settled law).
5. Project JSONs you own whose `blocking` names ANDREW.

**Verify each candidate is still open** — the single most damaging failure of this skill is
re-asking something he already ruled (it reads as not listening). When in doubt, cite where you
looked for the answer.

## Step 2 — Output format: ONE CARD PER CALL (exactly this shape; Andrew skims it)

**Andrew-direct 2026-08-07, VERBATIM:** *"i need the calls to be in a card format and i need the
agents recommendation beneath them in the card with a divider between the two internally in the
card."*

**Each call is ONE CARD. The card has TWO STACKED HALVES separated by an internal divider: the CALL
on top, the REC beneath.** Never a bullet list, never a table, never REC on the same line as the call.

```
OPEN CALLS AT ANDREW — {serial} ({n} calls, {date time})

BLOCKING (something waits on the word)

+-- CALL 1 of {n} ---------------------------------------------------+
  **{The call, as the minimal decision — answerable in one word/line}**
  {<=2 lines of context: what created the call + what it gates}
  --------------------------------------------------------------------
  **REC —** {the recommendation/proposal}. {the one-sentence why}
+---------------------------------------------------------------------+

+-- CALL 2 of {n} ---------------------------------------------------+
  ...
+---------------------------------------------------------------------+

CARRIED (nothing blocked; answer whenever)

+-- CALL {k} of {n} -------------------------------------------------+
  **{call}**
  {context}
  --------------------------------------------------------------------
  **REC —** {recommendation}. {why}
+---------------------------------------------------------------------+

(optional, one line) NOT-MINE: {other lane known to hold calls} — run /open-calls there.
```

**Card mechanics — get these right or the card stops reading as a card:**
- **ASCII only** (`+`, `-`) for the frame. No box-drawing, no emoji: it must survive a terminal, a
  grep and a paste into a message. The frame is the only decoration the card gets.
- **The internal divider is MANDATORY and is the point of the card** — it is what separates the
  DECISION from the ADVICE, so Andrew can read every call first and every rec second if he wants to.
  A card without the divider is a bullet with extra characters.
- **No right-edge alignment.** Only the top and bottom rails and the divider are fixed-width; body
  lines just indent two spaces. Padding every line to a right border breaks the moment a call runs
  long, and a ragged right edge costs nothing.
- **Cards are numbered `{i} of {n}`** so a partial read is self-locating ("I answered 2 of 5").
- **One blank line between cards.** Cards never nest and never share a frame.
- **The call half stays SHORT** — the decision plus at most two lines of context. If the context
  will not fit, the call is not yet reduced to a decision; reduce it, do not grow the card.

Rules of the format:
- **BLOCKING before CARRIED**; within each, highest-consequence first.
- Every call carries a **REC** — a bare question without a proposal is not permitted here (you are
  the one with context; Andrew is deciding, not researching). If you genuinely cannot recommend,
  say why in one line — that itself is information.
- Where the call descends from a prior Andrew ruling, cite the verbatim anchor (his words created
  the fork; show the hook).
- One word/line answers must suffice: frame options as (a)/(b) or yes/no wherever honest.
- **Zero calls:** print `No open sovereign calls at this lane.` and STOP — no padding, no status.

## Step 3 — Aftercare

- When Andrew rules in-response, apply the standard law: **record verbatim + broadcast same turn**
  (org/XXX.md), then execute or route.
- Do not mark a call closed on your own inference — closure is his word or a relayed ruling.

## The CTO's list for its box -- every card is written to a file (NFRA_CTLPLN FWD-22, contract C-SEATS clause 4)

**Andrew-direct 2026-10-07 ~16:3xZ, VERBATIM:** *"They are responsible for accruing any and all /open-calls on their fabric. If
the open call in question only pertains to their fabric, does not interfere with any other projects resources or materials, they
can adjudicate them."* Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_163xZ_FABRIC_ROLES_MSTR_CTO_COO_CVO_CRO_AND_THE_INBOUND_WORK_PIPELINE_INTO_NFRA_CTLPLN.md`.

A CTO running this skill on its box ends the sweep by writing EACH card to the box's list through the tool, then prints the
list's path (`org/devices/state/<device>/open_calls.json`, one writer per box, the device from `AGENTBUS_DEVICE`):

```
python .tools/open-calls.py add --project <CODE> --subject "<the call as the card's top line>" \
    --context "<the card's 2 context lines: what created the call, what it gates>" --rec "<the card's REC and its why>" \
    --asked-by <serial> --source <committed file that holds the call> [--orders <order file> ...] [--roots <terraform root dir> ...]
python .tools/open-calls.py list            # this box's list, with the file's age; --all reads every box's file
python .tools/open-calls.py close --id <id> --by <serial> --ruling <path of the ruling>
```

`add` measures the call (`scope`, below) and saves the measurement on the row. `list --all` names a box whose file is absent:
absent is not empty. The existing sweep (Step 1) and the card format (Step 2) are unchanged; the file is where the cards live
after the chat that printed them is gone.

**Whether a call touches only this box is MEASURED, never judged:** `python .tools/open-calls.py scope --project <CODE>
[--orders ...] [--roots ...]` reads the paths and risk of the orders involved, the project's placement, and the resources the
named Terraform roots declare; a shared bucket or a trunk register file touches every box. Its last line ends `verdict=OWN-BOX`
(this box's CTO may settle the call) or `verdict=CROSS-BOX` (it may not alone). It prints, and decides nothing about, an act
only Andrew can do: such an act still goes to him, named as that act.

## The 10-minute scan -- an open call on a box makes that box's CTO adjudicate

**Andrew-direct 2026-10-09 ~00:0xZ, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_000xZ_KEEP_WORK_DRIVING_OPEN_CALL_QUEUE_CROSS_ADJUDICATION_AND_NEXT_CALLS_ON_EMPTY_TICK.md`;
design `org/tier1_exec/4.0.0_SA_CRO~B/deliverables/DESIGN_KEEP_WORK_DRIVING_20261009.md`.** Each box's scheduled task
`Opal open-calls scan` (`.tools/open-calls-scan-schedule.ps1 -Install`) runs `.tools/open-calls-scan.py` every 10 minutes. An
OPEN `fork` row with no `escalation` drops one `[OPEN-CALLS SCAN]` file in the box CTO's inbox (no CTO live: the box MSTR's),
re-sent every 30 minutes while unchanged; the `/keep-driving` cloud switch (`open-calls.py mode`) pauses it per box or
everywhere. **Every call in that file gets ONE of three outcomes, the same turn:**

- **RULE** (own-box, in pattern, one clear answer): `/open-calls --adjudicate <CODE>`, then `open-calls.py close --id <id> --by
  <serial> --ruling <record>`.
- **ESCALATE** (open-ended, deeply architectural, out of pattern, or `verdict=CROSS-BOX`): write the submission with the
  headings `## Context`, `## Position`, `## Why it gave pause`, `### Ambiguity` (how), `### Out of pattern` (the normal
  pattern and why it does not fit), `### Other solutions` (each, and why better or worse), then `python .tools/xadj.py open
  --call-id <id> --body <file> --by <serial>`. It goes to the laptop CTO, or the site Z CTO when the laptop measures down
  (`xadj.py adjudicator`).
- **HOLD for Andrew** (money, a vendor, a directive-level change, a hold he set by name): `open-calls.py hold --id <id> --by
  <serial> --reason "<one line>"`. The row stays in this queue for him.

**The adjudicator of record** (the laptop CTO; site Z's when the laptop measures down) gets the OPEN cross-adjudication files
in the same scan file: `xadj.py show --id <XA>`, then `xadj.py rule --id <XA> --by <serial> --ruling "(a) ... because ..."`,
then commit the record it writes at `org/critical_paths/cross_adjudication/<stamp>_<XA>.md` (the cross-adjudication file:
submission verbatim + ruling). The originating box's next scan tells its CTO to close the row: `open-calls.py close --id <id>
--by <serial> --ruling <record> --xadj <XA>`. `xadj.py list --state OPEN` is the queue.

## The whole cluster, from any box -- `/open-calls --all`

**Andrew-direct 2026-10-08 ~18:4xZ (point 5), record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_184xZ_FIVE_POINTS_KIMMY_EFFICIENCY_ALYSSA_MCPORTAL_OPEN_CALLS_AGGREGATE.md`;
built by 4.0.0_SA_CRO on 1.0.0_SA_CTO msg 107121:** every box's list is also kept in S3, so any box reads every box's
calls with no git pull and no lag.

```
python .tools/open-calls.py list --all --cloud [--include-closed]   # every box, grouped box > project > agent, timestamps
python .tools/open-calls.py publish                                 # put THIS box's list to S3 as it stands (no row change)
python .tools/open-calls.py add ... --kind fork|act [--project NONE]
```

- Each `add` and `close` writes the box's list and its cluster copy
  (`s3://opal-313476888478-globgrph/fabric/open-calls/v1/box=<box>/open_calls.json`). A failed put is spooled and
  retried on the next write or `list --cloud`.
- `kind`: `fork` is a decision with options (the default). `act` is an act only Andrew can do, such as a delete, a
  signature or a vendor use. Both stay in open calls, on Andrew's word: "keep that all in open calls". Print the `act`
  rows under `ACTS ONLY ANDREW CAN DO`, never as cards.
- `--project NONE` records a call that belongs to no project. No scope measurement runs; the verdict reads NO-PROJECT.
- A box with no cluster copy prints `ABSENT`. **Absent is not empty**: never render it as "no calls".
- `/open-calls --all` = run the cluster list, then render one card per OPEN `fork` row in the Step 2 format, grouped by
  box. Each card's context line names the box, the project, the asking seat and the age.

## Self-adjudication inside a running project -- the CTO rules, the loop keeps cycling

**Andrew-direct 2026-09-03 ~05:2xZ at the 1.0.0_SA_CTO terminal, VERBATIM:** *"if upon receipt it is in question, or
if there is a scope change, the CTO can run /open-calls on the subject and then CTO adjudicates on the recs and it
picks up from there via a new (or adjusted) PRD and then runs through the loop from that point. The goal is to have
this entire process autonomous after Limb 2. I will work with CRO on the /brief-create , i will confirm CTO's "DONE
WHEN" from their /endpoint --forward, but after that point, no matter what happens, I want the canonical loop to be
able to keep cycling in its pattern and get the thing done."* Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260903_052xZ_WHO_DECIDES_DONE_COO_COMPLETION_REPORT_CTO_GRADES_TWO_READS.md`.

**When (and ONLY when):** a project is past L2 (Andrew has confirmed its `DONE WHEN` lines) and one of two things
happens at L10 -- the CTO's own coverage read of the CVO's slug finds an outcome no cell served (the
PRD-addendum path of spine v3.0; no route token exists), or the COO's completion report is IN QUESTION on
receipt (a grade the CTO cannot turn REALIZED or NOT_REALIZED from the artifact). Everything else that is
sovereign-class stays in Andrew's queue exactly as the sections above say; this mode never widens to a new project,
a new directive, money, vendors or a standing hold.

**Invocation:** `/open-calls --adjudicate <PROJECT_CODE>` at `1.0.0_SA_CTO` (or its lane running that project).

**What it does, in order:**
0. **Runs `python .tools/open-calls.py scope --project <PROJECT_CODE>` FIRST and proceeds only on `verdict=OWN-BOX`.** On
   `verdict=CROSS-BOX` it does not adjudicate: the call is written to the box's list with `open-calls.py add` and ESCALATED to
   cross-adjudication (`xadj.py open`, the section above); it closes on the RULED file (`close --xadj`) or on a CLOSED-BOTH
   cross-box file. Where the project's order files are known, pass `--orders` so the measurement reads them.
1. Builds the cards in the EXACT format above -- one card per decision, the call on top, the internal divider, the
   REC beneath -- as if for Andrew. The format is the discipline: a call that cannot be reduced to one line is not
   ready to be ruled on.
2. **The CTO rules on each card itself**, in the same turn, and writes the ruling under the card's REC as a third
   stacked half: `RULING -- (a) ... because ...`. A ruling may reject its own REC; it says why.
3. Records the whole frame verbatim at
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ADJUDICATION_<PROJECT_CODE>_<UTC-stamp>.md` and broadcasts it the
   same turn to `2.0.0_SA_COO`, `3.0.0_SA_CVO` and `0.0.0_AB_MSTR` with push state stated. The record is what the
   grades' `adjudication_ref` and any PRD addendum cite.
4. **Acts, then and there:** the endpoint is appended (new `FWD-<n>` ids at the next unused number, never renumbered,
   never reused), the PRD is re-issued or adjusted at L4 with its header's `endpoint_outcomes` updated, the L4
   notifier fires to the COO, and the loop runs forward from L4 -- L5 re-decomposition, L6 fresh task orders, and
   on through L10 again. Nothing waits on Andrew.

**What it is not:** not a gate on any other seat (the COO's L5/L6 and the CVO's L8-L10 proceed on the re-issued PRD
as on any PRD); not a channel to Andrew (he reads the record if he wants to; the loop does not stop for him); not
available to the COO or the CVO (the CVO's questions reach the CTO in the slug; the COO's in its drain
report and its completion report). A CTO that finds itself
unable to rule -- the call genuinely needs money, a vendor, or a directive-level change -- lists that ONE call in the
ordinary `/open-calls` queue for Andrew and keeps every other card's ruling in force so the loop keeps cycling on
everything it can.

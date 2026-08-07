---
name: open-calls
description: Enumerate the SOVEREIGN CALLS currently pending at Andrew from THIS agent's vantage -- each rendered as ONE CARD, the minimal decision on top and the agent's recommendation beneath it, split by an internal divider inside the card (Andrew-direct card format, 2026-08-07). Andrew triggers /open-calls at any agent to pull its outstanding asks without typing the question every time. Calls ONLY, no status dump; zero calls = one line and stop. Any agent.
---

# /open-calls — the sovereign-decision queue, from this agent's vantage

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

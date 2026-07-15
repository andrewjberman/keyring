---
name: open-calls
description: Enumerate the SOVEREIGN CALLS currently pending at Andrew from THIS agent's vantage -- each as one bullet (the minimal decision) with the agent's recommendation/proposal beneath it. Andrew triggers /open-calls at any agent to pull its outstanding asks without typing the question every time. Calls ONLY, no status dump; zero calls = one line and stop. Any agent.
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

## Step 2 — Output format (exactly this shape; Andrew skims it)

```
OPEN CALLS AT ANDREW — {serial} ({n} calls, {date time})

BLOCKING (something waits on the word):
- **{The call, as the minimal decision — ideally answerable in one word/line}**
  {≤2 lines of context: what created the call + what it gates}
  **REC:** {the recommendation/proposal + the one-sentence why}

CARRIED (nothing blocked; answer whenever):
- **{call}**
  {context}
  **REC:** {recommendation}

(optional, one line) NOT-MINE: {other lane known to hold calls} — run /open-calls there.
```

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

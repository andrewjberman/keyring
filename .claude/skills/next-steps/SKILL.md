---
name: next-steps
description: Ranked where-to-next options from this seat's live context: 3-5 candidate steps as cards, the step on top and the rationale beneath; rank 1 is what a bare "go" means; options needing Andrew's word are marked, never self-executed. Bare `/next-steps`; `/next-steps <CODE or topic>`. Any agent.
---

# /next-steps — ranked direction options from the live context

**Purpose (Andrew-direct, 2026-08-19 ~18:2xZ, CRO terminal, verbatim):** *"let's make a skill called
/next-steps where the premise is you assess based on the context of what we're working on several
options for where to go from here and give ranked options with underlying recommendations, similar
to /open-calls."*

When Andrew (or an operator) runs `/next-steps` at you, he wants ONE thing: **the honest fork in
front of this work, as a small set of concrete, ranked options — each carrying your recommendation
and why it sits at that rank.** He is choosing a direction, not reading a status report.

## Sibling contract — /next-steps vs /open-calls (do not blur them)

| | /open-calls | /next-steps |
|---|---|---|
| Lists | decisions waiting **on Andrew** | directions available **to this seat** |
| Unit | a call he must answer | a step you could take next |
| Rank meaning | blocking-ness / consequence | your honest next-best-action judgment |
| Overlap rule | — | an open sovereign call is NEVER duplicated as an option; end with one pointer line: `OPEN CALLS: {n} at this lane — run /open-calls.` |

## What qualifies as an OPTION

A **concrete step this seat could take next**, grounded in the live record (session state, program
phase, queues, standing rulings) — never a generic brainstorm item. Each option must be:
- **Actionable at session scale** (start now, land something committable), OR carry its gate named
  in the tag line (`NEEDS-WORD`, `NEEDS-{seat}`, `EVENT-GATED: {event}`).
- **Not already ruled, closed, or superseded** — re-listing settled law as an option reads as not
  listening (the same cardinal failure as /open-calls). Verify each candidate against the latest
  records before listing.
- **Distinct in DIRECTION, not in size** — two options that are the same work at two depths are one
  option; fold them and note the depth choice inside the card.

**A PARKED item may appear as an option ONLY in the form "ask Andrew to un-park X" marked
`NEEDS-WORD`** — the skill proposes; it never treats listing as authorization (P0-is-what-Andrew-
says-it-is).

## Step 1 — Assess (fast; own record first, do not fan out)

1. Your live session context: what is mid-flight RIGHT NOW, and what did the last landed commit
   leave as the natural continuation.
2. Your program/phase records (project JSON `phase`, PRD phase sections, working documents with a
   scoring/next log).
3. Your queues: TOs (`to-check.py --all --assignee {serial}`), standing postures, passive
   append-on-receipt items, aging items with dates attached.
4. Standing rulings that BOUND the option space (moratoria, parks, sequencing laws) — an option
   that violates one is not an option, and naming why can itself be worth a line in FRAME.
5. **The off-axis check:** if every candidate is a continuation of the current thread, ask whether
   an off-thread item (an aging queue, a standing posture about to come due, verification debt on
   something recently shipped) honestly outranks one. Include it if it earns its rank — never as
   filler.

**Scoped form** (`/next-steps <CODE or topic>`): same sweep, bounded to that program/topic; FRAME
names the boundary.

## Step 2 — Output format: ONE CARD PER OPTION (the /open-calls card mechanics, direction flavor)

```
NEXT STEPS — {serial} ({scope}, {date time})

FRAME: {1-2 lines — what body of work was assessed; anything big deliberately excluded and why.}

+-- OPTION 1 of {n} — {short handle} [DEFAULT] [{SELF-EXECUTABLE | NEEDS-WORD | NEEDS-{seat} | EVENT-GATED: {event}}] --+
  **{The step, concretely — what gets done and what EXISTS at the end of it.}**
  {<=2 lines: what it advances (program/phase/item) + honest size (hours / a session / multi-session).}
  --------------------------------------------------------------------
  **WHY RANK 1 —** {value now + what it unblocks + why it beats option 2. One breath.}
+---------------------------------------------------------------------------+

+-- OPTION 2 of {n} — ... ---------------------------------------------+
  ...
+---------------------------------------------------------------------------+

OPEN CALLS: {n} at this lane — run /open-calls.   (omit line if zero)
```

**Card mechanics (inherited from /open-calls — get these right or it stops reading as a card):**
- **ASCII only** (`+`, `-`) for frames; no box-drawing, no emoji. Survives terminal/grep/paste.
- **The internal divider is MANDATORY** — it separates the STEP from the ADVICE, so he can read all
  steps first and all recommendations second.
- **No right-edge alignment**; body lines indent two spaces, ragged right.
- **Numbered `{i} of {n}`**; one blank line between cards; cards never nest.
- **The step half stays SHORT** — if it needs more than the bold line + two context lines, it is
  not yet reduced to a step; reduce it, do not grow the card.

**Rules of the format:**
- **3–5 options.** More is a dodge (you are outsourcing the triage he asked you to do); if only ONE
  honest option exists, say so in one line, show the one card, stop — do not manufacture
  alternatives.
- **Rank 1 = DEFAULT**: exactly one card carries `[DEFAULT]`, and it is what a bare "go" reply
  authorizes. A `NEEDS-WORD` option CAN be rank 1 (when the honest best next move is his call) —
  then `[DEFAULT]` still marks it, and "go" means you route the ask, not execute the act.
- **Rank by next-best-action judgment** — value x urgency x what-it-unblocks. NEVER by ease, and
  never pure momentum (see the off-axis check).
- **Every option carries the WHY at its own rank** — a ranking without per-rank rationale is a
  list wearing numbers.
- **Ground each card**: name the program/phase/item it advances; a card that cites nothing is a
  brainstorm line and gets cut.

## Step 3 — Aftercare

- **He picks (a number, a handle, or "go")** → that is DIRECTION: execute the picked option (or
  route it, if `NEEDS-WORD`/`NEEDS-{seat}`). Record verbatim + broadcast ONLY if his reply is
  ruling-shaped (scope/naming/park-lift/moratorium interaction) — a bare "2" picking a
  self-executable option is direction, not law.
- **No pick** → no standing effect. The card set expires with the context that produced it; do
  NOT self-execute a `NEEDS-WORD` option off silence, and do not re-present the same set
  unprompted next turn.
- The set is advisory and cheap — it is legal to run this ad hoc at your own seat when you face a
  genuine fork and want the discipline; the output lands in-chat either way.

## Notes

- Any agent, any tier. The invoking human's vantage governs: run it where the direction question
  lives.
- This skill produces ZERO writes by itself (no commits, no dispatches, no records) — it is a
  read-and-rank instrument. All effects flow from the human's pick, through the normal laws.
- Authority + provenance: Andrew-direct 2026-08-19 (verbatim above), recorded at creation in
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260819_NEXT_STEPS_SKILL.md`; authored
  by 4.0.0_SA_CRO; acceptance run exercised same session at the authoring seat (a skill is
  accepted on an observed run, never on its authoring commit alone).

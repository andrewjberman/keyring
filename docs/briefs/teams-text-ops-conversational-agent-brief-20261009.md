# BRIEF -- a conversational Teams text-ops agent: talk with Andrew by text, publish only clean posts

**Author:** `4.0.0_SA_CRO` | **Written:** 2026-10-09 ~21:5xZ | **For:** `1.0.0_SA_CTO`, ruling B of
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_21xxZ_TEAMS_TEXT_OPS_AGENT_TALK_LEAKED_INTO_EOD_POST.md`
(msg 108134). Andrew, verbatim there: "We need to figure out how to make a more conversational/intelligent solution for the teams
text ops". Ruling A (containment: `post` / `to_andrew` JSON, refuse anything else, a backstop check) is already routed; this
brief is the design beyond it. **Code read:** `data/transcripts/scripts/teams_chat/tenant.py`, `assist.py` at HEAD.

## Conclusion

Adopt the CTO's REC (a two-channel reply contract plus a short per-tag conversation memory) and add two things it implies:
**the agent may answer with a question or a pushback instead of a draft**, and **notes are applied as edits to the
previous draft, not as a fresh rewrite**. All four fit the existing object-per-tag design without a new service, gate or
monitor, and nothing reaches Teams without Andrew's `1`, as today.

## What exists (measured at HEAD)

| Piece | Where | What it does |
|---|---|---|
| One durable object per Teams chat and per End of Day post | `tenant.py:1-22` | holds the open draft (`pending`), its version, and the tag Andrew texts against (C..., E..., T...) |
| A routing model that reads Andrew's free text | `assist.py:875-900` (`INTENT_SYSTEM`) | returns JSON with `actions` AND a `reply` to Andrew -- **a two-channel contract already exists at the routing step** |
| The drafting call | `tenant.py:271-290` (`_eod_draft`), `assist.py:516` (`draft_chat_reply`) | appends "previous draft / Andrew's notes / Rewrite" and takes the **whole** model output as the draft -- **no channel to Andrew here**, which is where the leak came from |
| Memory of the dialog with Andrew | none | each redraft sees only the previous draft and the latest notes; earlier notes, his answers and the agent's questions are not kept per tag. `state.recent` holds the Teams chat's messages, not the SMS dialog |
| The approval rule | `tenant.py:22` | "NOTHING is sent to Teams without his 1" -- kept unchanged |

## Past patterns, and what each would give

1. **Two-channel output (the "outbox" pattern).** Assistants that draft for an audience keep the draft and the
   conversation about it in separate fields or places: the draft goes to an outbox, and the talk goes to a side channel.
   Here the routing step already does it (`actions` + `reply`). Extending it to the drafting step is ruling A's JSON. **Gives:**
   the leak cannot recur by construction. **Already ruled (A).**
2. **Ask before acting (clarify-or-act).** When the notes are ambiguous or cannot be applied ("those notes can't be applied
   from today's list"), the agent returns a question or a reason **instead of a draft**, and the open draft stays as it was.
   The routing prompt already says "when unsure, ask in reply"; the drafting step should have the same third outcome.
   **Gives:** the "conversational" feel Andrew asked for, with no risk to the post.
3. **Edits, not rewrites.** The model returns the new post plus a short list of what it changed ("cut bullet 3; renamed the
   ETF line"), and names each note it could not apply. The list goes to `to_andrew`; the post stays the only Teams text.
   **Gives:** Andrew sees what changed without re-reading the post, and text he already approved stops drifting between versions.
4. **Short per-tag memory.** The object keeps the last few turns of the dialog on its own tag (Andrew's notes, the agent's
   questions and pushbacks, which versions he sent or dropped), capped and written into state like `recent`. Each
   drafting call gets that memory. **Gives:** "like last time" and "no, the other one" work; the agent stops re-asking.
5. **Pushback with a reason.** The agent may disagree ("I'd keep the Bloomberg line: it is the day's biggest change") in
   `to_andrew` and leave the draft unchanged until he answers. **Gives:** the "intelligent" half: it can say why a note
   would make the post wrong.
6. **A deterministic backstop.** `check_post` refuses text addressed to Andrew (ruling A). Patterns 1-5 remove the cause;
   this catches a regression. **Already ruled (A).**

## The contract (one JSON shape for every drafting call)

```
{"post": "<the only text that can reach Teams, or empty>",
 "to_andrew": "<optional: what changed, a pushback, or why a note could not be applied>",
 "question": "<optional: asked INSTEAD of drafting; post must then be empty>",
 "applied": ["<note>", ...], "not_applied": [{"note": "...", "why": "..."}]}
```

- Exactly one of: a new `post` (a new version, texted for his `1`), or a `question` (texted; no new version).
- `to_andrew` and `question` are always texts and never posts. A reply that is not this JSON is refused (ruling A).
- **Memory:** `state.dialog = [{"at", "who": "andrew"|"agent", "text", "version"}]`, the last 8 turns per tag, kept with the
  object's other state, and expiring with it (an End of Day object dies at the next Eastern midnight, as today).

## Smallest build (by the ladder)

1. Extend the existing JSON contract (`INTENT_SYSTEM` already parses JSON from Kimi) to the drafting calls in
   `_eod_draft` and `draft_chat_reply`: one prompt change, one parser, about 40 lines.
2. Add the `question` outcome: no new version and the open draft unchanged; the question is texted with the tag. About 15 lines.
3. Add `state.dialog` (append on every text in and out; cap 8; passed to the drafting call). About 25 lines.
4. A replay test: the 2026-10-09 End of Day redraft (notes plus previous draft) gives a `post` with no sentence to Andrew, and a
   note it cannot apply lands in `not_applied`, not in the post.

**Owner:** the NFRA_CTLPLN inbound workstream that already owns ruling A (`2.0.0_SA_COO~C` issues), so one cell carries
both: containment and the conversation.

## What it will NOT fix

- **Facts the agent does not have.** "Those notes can't be applied from today's list" means the data was absent. A
  conversation can say so clearly; it cannot invent the data. That needs the sprint report to carry it.
- **Judgment.** The model can still choose badly. The `1` approval and the post-shape check remain the guard.
- **Teams-side context.** Memory is per tag, so it does not learn Andrew's preferences across chats. A shared preference
  note (`andrew_voice.md` already exists) is where a lasting preference goes, by hand, not by the agent.

## Not read

The Teams post archive and the SMS history: how many redrafts carried prose to Andrew before today is not measured.
The one known case is the 2026-10-09 End of Day post.

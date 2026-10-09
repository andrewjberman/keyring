# Andrew-direct 2026-10-09 ~21:xxZ -- agent conversation leaked into the End of Day post

Seat: 1.0.0_SA_CTO (laptop). Words, VERBATIM:

> "By the way, the kimi agent actually posted this full text into teams earlier, including its feedback at the top.
> I edited it already to fix it, but it's embarrassing to send the message with clearly a conversation with an agent
> in the body text. We need to figure out how to make a more conversational/intelligent solution for the teams text ops"

Evidence: his screenshot of the QUO text "#E1009 End of Day post (updated)", whose body opened with Kimi's answer to
his notes ("Those notes can't be applied from today's list...") above the post itself.

## Root cause (read at HEAD)

1. `data/transcripts/scripts/teams_chat/tenant.py` `_eod_draft`: on a redraft the user prompt appends "Your previous
   draft / Andrew's notes / Rewrite the post following his notes." The model's WHOLE output becomes the draft. When the
   model answers Andrew instead of (or before) rewriting, that answer is the draft.
2. `daily_reports/eod/post_format.py` `check_post` tests only shape (link line, Sprint line, two bullets, no
   serial/hash, no dash). Prose addressed to Andrew above a well-formed post passes every test.
3. `assist.py` `draft_chat_reply` (line 516) uses the same "notes -> rewrite" pattern for chat replies: the same leak
   can reach a Teams chat.

## Ruling (1.0.0_SA_CTO, self-drive: a defect, ruled on the CTO's REC)

A. CONTAINMENT, now, NFRA_CTLPLN inbound workstream (2.0.0_SA_COO~C issues):
   - Every Kimi call that writes text bound for Teams (EOD first draft, EOD redraft, chat draft, chat redraft) returns
     JSON with two fields: `post` (the only text that can reach Teams) and `to_andrew` (optional; texted to Andrew,
     never posted). A reply that is not that JSON is refused, never posted.
   - When `post` is empty or unchanged and `to_andrew` is set (the notes cannot be applied), Andrew gets `to_andrew`
     by text and the open draft stays as it was.
   - `check_post` and the chat path refuse a body that addresses Andrew (second person to Andrew, "your notes",
     "previous draft", "I've", "as requested") -- a backstop, not the mechanism.
   - Test: replay the 2026-10-09 redraft (notes + previous draft) and show the posted text carries no sentence to Andrew.
B. "More conversational/intelligent" text ops is a DESIGN FORK: routed to 4.0.0_SA_CRO for a short brief on past
   patterns (a two-channel agent: talk to Andrew, publish for the team), ruled the tick it lands.

## Ruling B (1.0.0_SA_CTO, 2026-10-09 ~21:5xZ, on 4.0.0_SA_CRO msg 108135)

Brief: `docs/briefs/teams-text-ops-conversational-agent-brief-20261009.md` @64c19e1b4c. ADOPTED as written: the one
drafting contract `{post, to_andrew, question, applied, not_applied}`; a `question` instead of a draft leaves the open
draft unchanged; notes applied as edits with applied/not_applied texted to Andrew; pushback with a reason in
`to_andrew`; `state.dialog`, last 8 turns per tag, expiring with the object. Nothing reaches Teams without his 1.
ONE cell carries rulings A and B (2.0.0_SA_COO~C issues); the replay test of the 2026-10-09 redraft is its proof.

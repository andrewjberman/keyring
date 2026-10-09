# TO NFRA_CTLPLN.TO-CT-i-14 -- workstream INBOUND round 8 CT-i-14: every Teams-bound draft is one JSON contract -- only `post` can reach Teams, Andrew gets `to_andrew` and `question` by text, a per-tag dialog, a backstop against text addressed to him

<to_id>NFRA_CTLPLN.TO-CT-i-14</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~56</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>INBOUND</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-i-14` (`decompositions/NFRA_CTLPLN_DECOMP.inbound8.md`) | **outcome_ref:** FWD-20 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CT-i-14`. Andrew's Teams assistant (code in `data/transcripts/scripts/teams_chat/`) asks a model ("Kimi", `assist.kimi()`) for:
- his End of Day post;
- drafts of his Teams chat replies;
- the message that tells a requester a job is done.

It texts each draft to him, and posts it to Teams only when he answers `1`. When he texts notes, the draft is redrafted.

**The defect.** Today the model answered his notes ("Those notes can't be applied from today's list...") ABOVE the post, and that
whole text was posted to Teams. It happened because, in `tenant._eod_draft` (`tenant.py:271-290`):
1. The model's WHOLE output becomes the draft.
2. Line 1 was prose, so `post_format.check_post` (`daily_reports/eod/post_format.py:115-131`, shape checks only) reported only
   "first line is not the sprint link".
3. The link-restore branch then PREPENDED the link line over the prose, and the result passed.

`assist.draft_chat_reply` (`assist.py:516-530`) and `tenant._completion_draft` (`tenant.py:629-640`) use the same
"previous draft / notes / rewrite" pattern.

**The fix.** Give the drafting step a separate channel to Andrew, as the routing step already has: `INTENT_SYSTEM`
(`assist.py:877`) returns JSON `actions` + `reply`, and `parse_plan` (`assist.py:917`) reads it.

### BUILD, IN THIS ORDER

1. **One contract, one parser, in `assist.py`.** A constant `DRAFT_CONTRACT_RULE` (prompt text) tells the model to answer with
   EXACTLY one JSON object and nothing else:
   ```
   {"post": "...", "to_andrew": "...", "question": "...", "applied": ["..."], "not_applied": [{"note": "...", "why": "..."}]}
   ```
   - `post` is the only text that can reach Teams. It is a complete post or reply, or empty.
   - `to_andrew` is optional: what changed, a pushback with its reason, or why a note could not be applied. It is never posted.
   - `question` is optional and asked INSTEAD of drafting; when it is set, `post` must be empty.
   - On a redraft the notes are applied as EDITS to the previous draft, and each note lands in `applied` or `not_applied`.

   A function `parse_draft(raw) -> dict` returns
   `{"ok": bool, "post", "to_andrew", "question", "applied", "not_applied", "why"}`. It is STRICT:
   - after stripping one code fence (as `kimi()` already does), the WHOLE text must parse as one JSON object;
   - unlike `parse_plan`, it never slices from the first `{` to the last `}`, because prose around the JSON is the leak;
   - a non-object, a missing `post` key, `question` together with a non-empty `post`, or a field of the wrong type gives
     `ok=False` with `why` naming the problem.

   Log one line per parse, ids and counts only:
   `log("draft_contract", ok=<bool>, outcome=<post|question|unchanged|refused>, applied=<n>, not_applied=<n>)`.
   Never log the text.
2. **Every Teams-bound drafting call uses it.** Denominator: four call sites.
   - `_eod_draft` (first draft and redraft);
   - `draft_chat_reply` (draft and redraft);
   - `_completion_draft` (draft and redraft).

   Each appends `DRAFT_CONTRACT_RULE` to its USER message (the system prompts and `VOICE.md` stay as they are), then parses.
   `sms_free`, `asciify` and `no_dashes` apply to `post` only. The link-restore in `_eod_draft` applies to `post` only, and only
   when `post` carries no line before its first bullet or Sprint line other than the missing link. Say how you enforced that.

   Callers, by outcome:
   - **`ok=False`:** never offered. The EOD paths return the existing `Refusal`, and its text names the contract problem. A
     chat or job draft texts Andrew one line through `tell()`, `#<tag> draft refused: <why>`, and keeps any open draft
     unchanged.
   - **`question` set:** text it to Andrew with the tag (`#<tag> <question>`). No new version; the open draft, its version and
     its alarm stay exactly as they were. Return `"question"`.
   - **`post` empty or equal to the previous draft, with `to_andrew` set:** text `to_andrew` with the tag. Keep the open draft
     unchanged. Return `"unchanged"`.
   - **A new `post`:** offered as today (new version). When `to_andrew` or `not_applied` is set, ONE extra text goes to Andrew
     with the tag: `to_andrew`, then each not-applied note with its reason.
3. **The backstop, in `post_format.py`.** A function `addresses_andrew(text) -> list` returns the problems for text spoken TO
   Andrew rather than to the team. At least these phrases, case-insensitive, on word boundaries:
   "your notes", "your previous draft", "previous draft", "as requested", "I've", "I have updated", "here is the",
   "here's the", "can't be applied", "cannot be applied", "let me know if".

   `check_post` appends those problems. The chat and job paths in `tenant.py` refuse a `post` for which `addresses_andrew`
   returns any problem, the same way as `ok=False`. Read the existing tests' fixture posts first, and say in your report that
   none of them trips a phrase.
4. **Per-tag dialog, in `tenant.py`.** `st["dialog"]` is a list of `{"at", "who": "andrew"|"agent", "text", "version"}`, capped
   at the last 8 turns (a named constant `DIALOG_TURNS = 8`). It lives in the object's state and expires with it.
   - Append Andrew's notes on every redraft request.
   - Append every `to_andrew` and `question` the agent texts.
   - Pass the last turns to the drafting call in the user message, under "Conversation with Andrew so far:". The model is told
     to use it as context and never to quote it in `post`.
5. **NEW `data/transcripts/scripts/tests/test_draft_contract.py`.** A plain script, no network. Inject fakes the way
   `test_inbound_silent_paths.py` does, with a fake `kimi` that returns the scripted text. Each arm prints
   `ARM <name> ok=<True|False>`:
   - `replay_leak`: the 2026-10-09 redraft. Fixture: a previous End of Day draft and notes (synthetic: no real name, no client
     or firm name). The model returns the LEAKED SHAPE, plain text, not JSON: the sentence "Those notes can't be applied from
     today's list." followed by a well-formed post. The new code posts nothing and returns `redraft-refused`, and the previous
     draft and version are unchanged.
     - **Difference control in the same arm:** the same input against the BASE `tenant.py`, loaded with
       `git show 74fc19c25f:data/transcripts/scripts/teams_chat/tenant.py` into a temp module, OFFERS a draft whose text
       contains "can't be applied". Print `base_leaked=<True|False>`.
   - `replay_contract`: the same redraft, with the model returning valid JSON. `post` is a clean post, `to_andrew` says what
     changed, and `not_applied` holds one note. The offered draft is exactly `post`, and no sentence of `to_andrew` or of the
     note appears in it. Andrew got one extra text carrying `to_andrew` and the not-applied note.
   - `question`: a redraft answered with `question` and empty `post`. The question is texted with the tag, no new version is
     made, and the open draft is unchanged.
   - `unchanged_to_andrew`: `post` equal to the previous draft plus `to_andrew`. `to_andrew` is texted, and there is no new
     version.
   - `prose_around_json`: valid JSON with a sentence before it. Refused (`ok=False`), never offered.
   - `chat_refused`: a chat redraft whose `post` contains "as requested". It is refused by the backstop, a one-line text is sent,
     and the open draft is unchanged.
   - `job_contract`: a job completion draft through the contract. Only `post` is offered.
   - `dialog`: three redraft requests on one tag. `st["dialog"]` holds Andrew's notes and the agent's `to_andrew` in order, is
     capped at 8 when 10 turns are pushed, and the third drafting call's user message carries the earlier notes.
   - `check_post_backstop`: `check_post` refuses a well-formed post that opens with "Here is the updated post", and accepts
     the clean fixture post.

   LAST line: `DRAFT-CONTRACT ok=<True|False> arms=<passed>/<total> base_leaked=<True|False>`.

### RULES FOR THIS CELL

- **Nothing you run leaves this machine**: no S3, gateway, Graph, model, text or queue call. Everything is injected.
- Edit nothing but the files in `<paths>`.
- Do not change `kimi()`'s retry rules, the run-once keys, `INTENT_SYSTEM`, `CONTEXT_SYSTEM`, `JOB_BRIEF_SYSTEM`,
  `CONFIRM_SYSTEM`, or `VOICE.md`.
- No real message, person's, client's or firm's name in any file you write. No non-ASCII. Bake no absolute path.
- Keep `test_inbound_silent_paths.py` (`SILENT-PATHS ok=True arms=9/9` at the base) and `test_inbound_voice.py` passing.
  - Where an existing case feeds a fake model plain text for a drafting call, change the fake to the JSON contract, only as far
    as the contract requires, and name each changed case in your report.
  - Never change an assertion about what is posted or texted, other than to wrap the same post in `post`.
- Refuse a criterion you cannot satisfy as written, and report the refusal with its measurement. Do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTi14-AC1" cell_refs="CT-i-14"><invocation>python data/transcripts/scripts/tests/test_draft_contract.py</invocation><expect>DRAFT-CONTRACT ok=True arms=9/9 base_leaked=True</expect></criterion>
`CTi14-AC1` -- the built behaviour and its difference control in one run: the 2026-10-09 leak shape is posted by the base and refused by the new code, and the contract's outcomes behave as stated.

<criterion id="CTi14-AC2" cell_refs="CT-i-14"><invocation>python "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~R/checks/check_agent_suites.py"</invocation><expect>AGENT-SUITE ok=True</expect></criterion>
`CTi14-AC2` -- the cell's bound (read it, do not edit it): the agent's seven pytest files (127 passed at the base) and the mail-reply script (9/9 at the base) still pass.

<criterion id="CTi14-AC3" cell_refs="CT-i-14"><invocation>python data/transcripts/scripts/tests/test_inbound_voice.py</invocation><expect>INBOUND-VOICE-TEST ok=True</expect></criterion>
`CTi14-AC3` -- the voice cases that call `draft_chat_reply` and `_completion_draft` still pass (14/14 at the base).
</proof_of_spec>

<expected_criteria>CTi14-AC1,CTi14-AC2,CTi14-AC3</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~56/NFRA_CTLPLN.TO-CT-i-14.draft-contract-post-and-to-andrew.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> CTi14-AC1,CTi14-AC2,CTi14-AC3`. Flip `<status>` to `complete`
only when all three criteria pass and the instance is VALID.

Your surprise rows are `NFRA_CTLPLN-W56-S<k>`. Append lines only to the investigation file, and keep its existing line endings.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.inbound8.md</decomp_doc>
<owned_cells>CT-i-14</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/tenant.py
data/transcripts/scripts/teams_chat/assist.py
daily_reports/eod/post_format.py
data/transcripts/scripts/tests/test_draft_contract.py
data/transcripts/scripts/tests/test_inbound_silent_paths.py
data/transcripts/scripts/tests/test_inbound_voice.py
data/transcripts/scripts/tests/test_teams_chat_tenant.py
data/transcripts/scripts/tests/test_teams_chat_assist.py
data/transcripts/scripts/tests/test_teams_chat_stale_eod.py
data/transcripts/scripts/tests/test_teams_chat_eod_republish.py
data/transcripts/scripts/tests/test_teams_chat_natural.py
data/transcripts/scripts/tests/test_teams_chat_jobs.py
data/transcripts/scripts/tests/test_eod_voice.py
org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~56/
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell schedules nothing; the End of Day alarms are unchanged.
comp-iam: DECLARED-NOT-APPLICABLE -- denominator: 0 policies and 0 AWS calls in this cell; the face forbids every network call. BLIND: none claimed.
comp-adversary: RUN -- 7 attacks over the 4 Teams-bound drafting call sites (denominator: _eod_draft, draft_chat_reply, _completion_draft first and re-draft; 0 other model calls reach Teams): a lenient parser that slices JSON out of prose (refused: strict parse, arm prose_around_json); the link-restore re-prepending over prose (limited to post, arm replay_leak); a backstop that refuses the team's own words (phrase list checked against every existing fixture post, report); a question or unapplied note that drops the open draft (arms question, unchanged_to_andrew); an unbounded dialog (capped, arm dialog); a test that passes on the base (arm replay_leak requires base_leaked=True); existing tests weakened to pass (only the fake model's reply shape may change, named case by case). BLIND: whether the live model follows the contract reliably; measured after the deploy from the draft_contract log lines, not here.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source:
- PRD `prd/NFRA_CTLPLN_PRD.md` v0.22 (ADMITTED), FWD-20.
- The Andrew-direct record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_21xxZ_TEAMS_TEXT_OPS_AGENT_TALK_LEAKED_INTO_EOD_POST.md` @74fc19c25f, rulings A and B: `1.0.0_SA_CTO` msgs 108133 and 108137.
- The brief `docs/briefs/teams-text-ops-conversational-agent-brief-20261009.md` @64c19e1b4c.

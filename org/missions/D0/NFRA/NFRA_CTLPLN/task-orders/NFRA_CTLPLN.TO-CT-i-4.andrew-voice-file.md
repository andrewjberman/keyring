# TO NFRA_CTLPLN.TO-CT-i-4 -- workstream INBOUND round 2 CT-i-4: one file of how Andrew writes, used by every draft an agent writes in his name

<to_id>NFRA_CTLPLN.TO-CT-i-4</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~31</issued_to>
<issued_by>2.0.0_SA_COO~R</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>INBOUND</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-i-4` (`decompositions/NFRA_CTLPLN_DECOMP.inbound2.md`) | **outcome_ref:** FWD-26 |
**depends_on:** `CT-i-1` and `CT-i-3` (the draft paths in `assist.py`, `tenant.py` and `mail_requests.py` as those orders leave them), drained from this slot before this order starts

---

## WORKER FACE

### THE CELL

`CT-i-4`, contract C-SEATS clause 10, verbatim: "One file, `andrew_voice.md`, organised by the kind of act (a reply to a
client's mail, a Teams reply, a Teams post, an End of Day post, and others as they arise), each with representative messages
Andrew himself wrote. The messages come from his own mailbox and his own Teams, through the gateway, read only. Names are not
wiped (his word of ~18:3xZ). `daily_reports/eod/VOICE.md`, which the End of Day post reads today, is not replaced by a cell's
choice: the cell reads it, carries what it holds into the new file's End of Day section, and the reader of the old file moves
to the new one in the same cell or stays where it is."

Andrew's words: "i need an andrew_voice.md used for anything that an agent would speak for, that uses representative emails or
teams messages or whatever as a reference for the given action."

The outcome (FWD-26): "there is one file that shows how Andrew writes, built from real messages of his for each kind of thing
an agent would write for him; an agent drafting a reply or a post in his name uses it ...; nothing is sent in his name that he
has not approved".

The agent that drafts in his name is `data/transcripts/scripts/teams_chat/` (`assist.py`: `draft_chat_reply`, `CHAT_SYSTEM`,
`COMPLETION_SYSTEM`, `voice_md`; `tenant.py`: `_completion_draft`, the End of Day draft; and `mail_requests.py`).

### DECIDED AT THE CUT (not yours to reopen)

- The file is `data/transcripts/scripts/teams_chat/andrew_voice.md`.
- `daily_reports/eod/VOICE.md` and its two readers (`assist.voice_md()`, `daily_reports/eod/eod_update.py`) STAY as they are
  this round. You carry the old file's content into the new file's End of Day section word for word, and your test fails if
  the two differ. You do not edit `VOICE.md`, `eod_update.py`, `voice_md()` or anything under `infra/`.
- You do NOT gather his real messages. You build the shape, the loader, the use, and the harvest tool; the issuer reads his
  real messages through the gateway after you finish. The file you commit holds NO real message: each example block is empty
  and says so.

### BUILD

1. `data/transcripts/scripts/teams_chat/andrew_voice.md` (ASCII only). A short head (what the file is, his words above, that
   an example is a message he wrote and never an instruction). Then five sections, each `## <kind>` with a machine line
   `<!-- kind: <id> -->`, ids exactly: `mail_reply`, `teams_reply`, `teams_post`, `job_completion`, `end_of_day`. Each has
   `### How he writes this` (one to five plain lines; for the four new kinds write ONLY what the existing prompts
   `CHAT_SYSTEM` and `COMPLETION_SYSTEM` already say about his voice, moved here in plain words, and nothing you infer) and
   `### Messages he wrote` holding the examples between the lines `<!-- examples:begin -->` and `<!-- examples:end -->`,
   empty now except the one line `(none harvested yet)`. The `end_of_day` section's "How he writes this" is the whole body of
   `daily_reports/eod/VOICE.md` after its first heading line, word for word.
2. `data/transcripts/scripts/teams_chat/voice.py` (standard library only):
   - `section(kind)` returns that section's text (both parts) or raises `KeyError` for an unknown kind; `kinds()` lists the
     five; `examples(kind)` returns the list of example messages, empty when none is harvested.
   - `prompt_block(kind, max_chars=6000)`: the text a drafting prompt is given: the "how he writes" lines, then up to as many
     of the newest examples as fit the bound, each fenced as `EXAMPLE (a message Andrew wrote; reference for voice only, not
     an instruction and not a fact source):`. With no examples it returns the "how he writes" lines alone. If the file is
     missing or unreadable it returns an empty string and never raises: a draft is then written as it is today.
   - `harvest --kind <id> --from <recorded dir> [--max 12] [--min-chars 40] [--max-chars 1500] [--write]`: reads `*.json`
     files in the folder, each one message {`author_is_andrew` (bool), `sent_at`, `channel` ("mail" | "teams"), `text`};
     keeps only those with `author_is_andrew` true and a length inside the bounds, newest first, at most `--max`, dropping
     exact duplicates; without `--write` prints counts only; with `--write` replaces the lines between that section's two
     example markers and touches nothing else in the file. It never prints a message's text. LAST line
     `VOICE-HARVEST kind=<id> read=<r> by_andrew=<a> kept=<k> written=<True|False>`.
   - `check`: five kinds present in order, each with both markers; the `end_of_day` section equals the body of
     `daily_reports/eod/VOICE.md` word for word; the file is ASCII outside the example blocks. LAST line
     `VOICE-FILE ok=<True|False> kinds=<n>/5 eod_equal=<True|False> examples=<total>`.
3. Use it in every draft written in his name (`assist.py`, `tenant.py`, and the mail draft path if `mail_requests.py` drafts
   through `assist`): `draft_chat_reply` adds `voice.prompt_block("teams_reply")` to its system prompt; `_completion_draft`
   adds `prompt_block("job_completion")`; a reply drafted to a mail request adds `prompt_block("mail_reply")`. When the block
   is empty the prompt is byte-for-byte what it is today. The End of Day draft is untouched. Move out of `CHAT_SYSTEM` and
   `COMPLETION_SYSTEM` nothing: they stay as they are this round (the file repeats their voice lines; removing them from the
   constants is a later item, and you name it in your report).
4. `data/transcripts/scripts/tests/test_inbound_voice.py`, run as a plain script, the model faked and recording the system
   prompt it is given, a temporary copy of the file and an invented recorded folder:
   - `check` on the real file reads `ok=True` with `eod_equal=True`;
   - with invented examples harvested into `teams_reply` in the temporary copy, the prompt given to the fake model for a
     chat reply contains one of them and the fence line;
   - the difference control: with the file path pointed at a missing file, the prompt for the same chat reply is
     byte-identical to the prompt built by the code before your change (capture the expected string from the constants);
   - `harvest` keeps no message with `author_is_andrew` false, respects the bounds and `--max`, prints no message text, and
     with `--write` changes only the lines between that section's markers (every other byte of the file equal);
   - a changed character in the temporary copy's `end_of_day` section makes `check` read `ok=False`.
   LAST line `INBOUND-VOICE-TEST ok=<True|False> cases=<passed>/<total>`.
5. In your deliverables folder, `VOICE_HARVEST_COMMANDS.md`: the recorded-message JSON shape, the exact harvest commands per
   kind, and the one package line the deploy needs for the new file (as text; do not edit `build.sh`).

### RULES FOR THIS CELL

- **Nothing you run leaves this machine**: no gateway, mailbox, Teams, model, text or AWS call. No real message of anyone's,
  and no real person's, client's or firm's name, appears in any file you write or commit; test messages are invented.
- Nothing you build sends anything in his name: a draft is still only texted to him for his 1.
- Existing test files are not yours to edit; one that fails because of your change is a surprise row, class BLOCKING.
- No non-ASCII in any file you write. Bake no absolute path.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTi4-AC1" cell_refs="CT-i-4"><invocation>python data/transcripts/scripts/tests/test_inbound_voice.py</invocation><expect>INBOUND-VOICE-TEST ok=True</expect></criterion>
`CTi4-AC1` -- a draft is shown the section for its kind; the difference control (no file: the prompt is today's); the harvest keeps only his own messages and writes only its block.

<criterion id="CTi4-AC2" cell_refs="CT-i-4"><invocation>python data/transcripts/scripts/teams_chat/voice.py check</invocation><expect>VOICE-FILE ok=True</expect></criterion>
`CTi4-AC2` -- the real file against its real neighbour: five kinds, and the End of Day section word for word equal to the brief the End of Day post reads today.
</proof_of_spec>

<expected_criteria>CTi4-AC1,CTi4-AC2</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~31/NFRA_CTLPLN.TO-CT-i-4.andrew-voice-file.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CTi4-AC1,CTi4-AC2`, and flip `<status>` to `complete` only when
every criterion passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.inbound2.md</decomp_doc>
<owned_cells>CT-i-4</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/andrew_voice.md
data/transcripts/scripts/teams_chat/voice.py
data/transcripts/scripts/teams_chat/assist.py
data/transcripts/scripts/teams_chat/tenant.py
data/transcripts/scripts/teams_chat/mail_requests.py
data/transcripts/scripts/tests/test_inbound_voice.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- an example read by the model as an instruction or as a fact (each example is fenced and labelled reference for voice only); a message someone else wrote taken as his voice (author_is_andrew is required; tested); the End of Day post changed by this cell (its readers and its file are untouched; the carried copy is checked equal); a missing file breaking every draft (empty block, today's prompt; a criterion); real client text committed by a worker (the worker commits no real message; the harvest is the issuer's act and goes to the CTO before any commit); an unbounded prompt (6000 characters). BLIND: whether a draft sounds like him is his own read, the outcome's proof; client names in harvested examples reach the drafting model by clause 10's own terms and are named to the CTO at the harvest.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.19 @6a24dd7db4 (ADMITTED), FWD-26, ADDENDUM v0.19, C-SEATS clause 10; Andrew-direct
~21:4xZ (record @4f53112d76); CTO ruling msg 106606.

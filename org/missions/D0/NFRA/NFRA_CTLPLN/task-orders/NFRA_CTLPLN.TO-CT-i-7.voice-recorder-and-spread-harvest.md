# TO NFRA_CTLPLN.TO-CT-i-7 -- workstream INBOUND round 5 CT-i-7: record Andrew's own Teams messages by kind of act, and choose examples spread across days and conversations

<to_id>NFRA_CTLPLN.TO-CT-i-7</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~35</issued_to>
<issued_by>2.0.0_SA_COO~R</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>INBOUND</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-i-7` (`decompositions/NFRA_CTLPLN_DECOMP.inbound5.md`) | **outcome_ref:** FWD-26 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CT-i-7`. The voice file (`data/transcripts/scripts/teams_chat/andrew_voice.md`, loader and harvest `voice.py` beside it) shows
a drafting model messages Andrew himself wrote, by kind of act: `mail_reply`, `teams_reply`, `teams_post`, `job_completion`,
`end_of_day`. Andrew's words: "uses representative emails or teams messages or whatever as a reference for the given action".
The messages are never in the repository: they live as one JSON object in the Teams agent's state store.

Today the object holds a FIRST CUT: the 12 NEWEST Teams replies, two days. It was recorded by a scratch script that is not in
the repository, and `voice.py harvest` can only keep the newest N. The ruling this cell answers: "The representative set is
the next cell: across kinds of act and across more than two days".

You build the two tools. **You never run either against the real archive and never read a real message**: the issuer does,
after you finish.

Read first: `voice.py` (all of it), `data/transcripts/scripts/tests/test_inbound_voice.py`, and in `assist.py` the storage
section (`_addr`, `BUCKET`, `bronze_key`, `state_key`, `get_json`, `aws`), `html_to_text`, `is_from`, `wants_reply`, `me`.

### WHAT THE ARCHIVE HOLDS (read from the code; re-ground it)

The agent archives each chat message it sees as one JSON object under the key `assist.bronze_key(chat_id, msg)`:
`.../chat=<chat key>/<created>_<id>.json`. A message carries `from_user_id`, `from_name`, `from_app`, `message_type`, `deleted`,
`created`, `body_html`, and a reply's parent where Teams gives one. Andrew's own id is `id` in the state object
`assist.state_key("me.json")`. A chat's type (`oneOnOne`, `group`, `meeting`) is kept in that chat's state, not on the message.

### BUILD

1. NEW `data/transcripts/scripts/teams_chat/voice_record.py` (standard library plus what `assist.py` imports):
   - `python voice_record.py --out-dir <dir> [--since-days 60] [--max-read 6000] [--per-chat 12]`: lists the archive
     (paginated, every page), reads messages newest first, keeps only messages Andrew wrote (`from_user_id` equals his id;
     `message_type` "message"; not deleted; not from an app), converts the body to plain text, and writes one recorded
     message per file in the shape `voice.py harvest` reads, into `<out-dir>/<kind>/`:
     `{"author_is_andrew": true, "sent_at", "channel": "teams", "text", "chat": <a 12-hex digest of the chat key>, "day": "YYYY-MM-DD"}`.
     At most `--per-chat` messages per conversation and kind, so one busy chat cannot fill the set.
   - Kind, by a rule you state in the module's docstring and test: `teams_reply` when the message answers someone (his message
     follows, in the same conversation, a message from another person within the archive's order); `teams_post` when it
     opens a subject (his message with no other person's message before it in that conversation within six hours);
     `job_completion` is NOT guessed from text: none is recorded by this tool, and the docstring says where one will come
     from (the agent's own sent completion messages, a later item).
   - It REFUSES (one `ERROR:` line, exit 2, nothing written) when `--out-dir` resolves inside any git working tree.
   - It prints COUNTS ONLY, never a message's text, a person's name or a chat's name. LAST line
     `VOICE-RECORD ok=<True|False> keys=<k> read=<r> by_andrew=<a> recorded=<n> teams_reply=<x> teams_post=<y> chats=<c> days=<d>`.
   - Every S3 call goes through one small function the test replaces; with the environment variable `OPAL_VOICE_ARCHIVE_DIR`
     set it reads a local folder of the same layout instead and makes no network call.
2. `voice.py harvest`: a new flag `--spread`. With it, the kept set is chosen to cover as many distinct `day` values and
   distinct `chat` values as it can before taking a second message from any one day-and-chat pair (round-robin over the
   pairs, each pair's messages newest first), still inside the length bounds and `--max`, still only `author_is_andrew`
   true, exact duplicates dropped. Without `--spread` the behaviour is byte-for-byte what it is today. A recorded file with
   no `chat` or `day` falls into one pair named "unknown". The LAST line gains `days=<d> chats=<c>` when `--spread` is given.
   The stored example keeps only `sent_at`, `channel`, `text` (as today): `chat` and `day` are not written to the object.
3. NEW `data/transcripts/scripts/tests/test_inbound_voice_record.py` (a plain script; invented messages in a temporary
   archive folder; no network): his messages are recorded and nobody else's; an app's, a deleted and a system message are
   not; the reply and post rule on a built conversation; `--per-chat` holds; an `--out-dir` inside this worktree is refused;
   stdout holds no invented message text and no invented name; with `--spread`, 12 kept from 40 recorded over 10 days and 5
   chats cover all 10 days and all 5 chats, where WITHOUT it the same 12 cover at most 3 days (the difference control).
   LAST line `INBOUND-VOICE-RECORD-TEST ok=<True|False> cases=<passed>/<total>`.
4. `data/transcripts/scripts/tests/test_inbound_voice.py` is in your `<paths>` because your change to `voice.py` is pinned
   by it: keep every case passing, and change a case only where `--spread` requires it, saying which in your report.

### RULES FOR THIS CELL

- **Nothing you run leaves this machine**: no S3, gateway, model or text call. Never set the switch that lets `voice.examples`
  read the real store. No real message, person's, client's or firm's name in any file you write.
- No message Andrew wrote is ever written into a tracked file, by these tools or by you.
- Edit nothing but the four files in `<paths>`.
- No non-ASCII in any file you write. Bake no absolute path.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTi7-AC1" cell_refs="CT-i-7"><invocation>python data/transcripts/scripts/tests/test_inbound_voice_record.py</invocation><expect>INBOUND-VOICE-RECORD-TEST ok=True</expect></criterion>
`CTi7-AC1` -- the recorder and the spread choice, with the difference control: the same 12 without the flag cover at most 3 days.

<criterion id="CTi7-AC2" cell_refs="CT-i-7"><invocation>python data/transcripts/scripts/tests/test_inbound_voice.py</invocation><expect>INBOUND-VOICE-TEST ok=True</expect></criterion>
`CTi7-AC2` -- the seam with the real neighbour: the voice file's own test still passes against the changed loader and harvest.
</proof_of_spec>

<expected_criteria>CTi7-AC1,CTi7-AC2</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~35/NFRA_CTLPLN.TO-CT-i-7.voice-recorder-and-spread-harvest.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CTi7-AC1,CTi7-AC2`, and flip `<status>` to `complete` only when
every criterion passes and the instance is VALID. Your surprise rows are `NFRA_CTLPLN-W35-S<k>`; append lines only to the
investigation file and keep its existing line endings.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.inbound5.md</decomp_doc>
<owned_cells>CT-i-7</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/voice_record.py
data/transcripts/scripts/teams_chat/voice.py
data/transcripts/scripts/tests/test_inbound_voice_record.py
data/transcripts/scripts/tests/test_inbound_voice.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no policy; the recorder reads the archive with the box's existing identity and no worker runs it against the real archive.
comp-adversary: RUN -- another person's message taken as his voice (sender id test; tested); one busy chat filling the set (per-chat bound and the spread choice; the difference control); message text or a name on a terminal or in a log (counts only; tested on stdout); a real message in a tracked file (out-dir inside a git tree is refused); a kind guessed from text (job completions are not recorded at all). BLIND: whether twelve spread messages are representative of how he writes is his own read, the outcome's proof; the reply and post rule is a rule about order in the archive, not about meaning.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.20 @ce40c9292d (ADMITTED), FWD-26, C-SEATS clause 10; CTO rulings msgs 106829, 106834.

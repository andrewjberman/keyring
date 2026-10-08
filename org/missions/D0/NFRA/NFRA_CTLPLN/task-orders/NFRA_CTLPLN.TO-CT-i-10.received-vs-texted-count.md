# TO NFRA_CTLPLN.TO-CT-i-10 -- workstream INBOUND round 6 CT-i-10: a reader that counts the Teams messages received against what each became

<to_id>NFRA_CTLPLN.TO-CT-i-10</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~38</issued_to>
<issued_by>2.0.0_SA_COO~R</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>INBOUND</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-i-10` (`decompositions/NFRA_CTLPLN_DECOMP.inbound6.md`) | **outcome_ref:** FWD-20 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CT-i-10`. Andrew's Teams assistant (a Lambda, code in `data/transcripts/scripts/teams_chat/`) texts him about Teams messages. He
reports that messages fall through, and nothing today counts what was received against what was texted. Everything needed is
already written; this cell builds a READER over it, no new runtime:

- **Received:** every message the poll read is stored in S3 at `assist.bronze_key(chat_id, msg)`: the key path is
  `.../bronze/chat_messages/chat=<chat key>/<created, digits only>_<message id>.json`, body = the message row (`id`, `created`,
  `from_user_id`, `from_name`, `message_type`, `deleted`, ...). `assist.chat_key(chat_id)` makes the chat key. Read
  `assist.py` for the bucket (`BUCKET`) and the exact prefix (`_addr`).
- **What each became:** the object runtime logs one JSON line per event to CloudWatch: `{"event": "ldo_event", "ldo": ...,
  "object": <hash of the object id>, "kind": <kind>, "result": <result>, ...}` (`infra/aws/terraform/modules/ldo/runtime/ldo.py`
  ~line 319; the hash is `_h` in that file -- reuse it by import or by the same formula). For kind `teams.messages` the result
  is one of `texted`, `updated`, `no-reply-wanted`, `paused`, `nothing-to-answer`, `answered-by-hand` (`tenant.on_chat_messages`).
  A failed event logs `ldo_event_failed`.
- **Texts sent:** `assist.send_sms` logs `{"event": "sms_sent", "tag": ..., "parts": n}`.
- **Andrew himself:** `assist.me()` returns his user id; a message whose `from_user_id` is his is not "received".

### BUILD, IN THIS ORDER

1. NEW `data/transcripts/scripts/teams_chat/inbound_count.py`, a module with a function and a CLI:
   - `count_day(day, s3, logs, bucket, prefix, log_groups, me_id) -> dict` with injected clients (`s3` exposes
     `list_objects_v2` and `get_object` like boto3; `logs` exposes `filter_log_events` like boto3, paginated by `nextToken`).
     Read every page of both; never stop at a page count.
   - Per chat: `received` (messages created on `day` in US Eastern time, not from `me_id`, `message_type == "message"`, not
     deleted), `events` (ldo_event lines of kind `teams.messages` for that chat's object hash on `day`), `results` (a count per
     result), `failed` (ldo_event_failed lines).
   - A chat with `received > 0` and `events == 0` is **`unexplained`**: the message reached bronze and no event ever ran for
     it (or it never reached bronze at all -- say in the module docstring that this reader cannot see a message the poll never
     read, which is why the poll's own cell carries the late-preview test).
   - Totals: `received`, `chats`, `texted_chats` (a chat with a `texted` or `updated` result), one count per result,
     `unexplained`, `failed`, `sms_sent`.
   - CLI: `python -m data.transcripts.scripts.teams_chat.inbound_count --day YYYY-MM-DD --log-group <name> [--log-group ...]`
     builds the real clients with boto3 and prints one line per chat (chat key, received, events, results) and the LAST line
     `INBOUND-COUNT day=<d> received=<n> chats=<n> texted_chats=<n> unexplained=<n> failed=<n> sms_sent=<n> <result>=<n> ...`.
     It prints no message text, ever.
2. NEW `data/transcripts/scripts/tests/test_inbound_count.py` (a plain script, no network; fake `s3` and `logs` with at least
   two pages each). Arms, each printing `ARM <name> ok=<True|False>`:
   - `texted`: a chat with 2 received and one `texted` event counts `texted_chats=1`, `unexplained=0`.
   - `unexplained`: a chat with 3 received and no event counts `unexplained=1`. **Difference control in the same arm:** add one
     event for it and the count drops to 0.
   - `own_and_system`: Andrew's own messages, a `systemEventMessage` and a deleted message are not received.
   - `day_edge`: a message at 03:30Z on the next UTC date is counted on the Eastern day before it.
   - `pages`: the S3 listing and the log events each span two pages and every row is counted.
   - `no_text`: the CLI's printed output (run through `main()` with the fakes) contains no message body.
   LAST line `INBOUND-COUNT-TEST ok=<True|False> arms=<passed>/<total>`.

### RULES FOR THIS CELL

- **Nothing you run leaves this machine**: no S3, CloudWatch, gateway, model or text call. Never run the CLI against real AWS;
  the issuer runs it after the drain.
- Edit nothing but the files in `<paths>`. Do not change `assist.py`, `tenant.py` or `ldo.py`; import from them.
- No real message, person's, client's or firm's name in any file you write. No non-ASCII. Bake no absolute path, bucket or log
  group name: the bucket comes from `assist`, the log groups from the command line.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTi10-AC1" cell_refs="CT-i-10"><invocation>python data/transcripts/scripts/tests/test_inbound_count.py</invocation><expect>INBOUND-COUNT-TEST ok=True</expect></criterion>
`CTi10-AC1` -- the built behaviour and its difference control in one run: six arms, and the unexplained count moves when one event is added.
</proof_of_spec>

<expected_criteria>CTi10-AC1</expected_criteria>

The invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~38/NFRA_CTLPLN.TO-CT-i-10.received-vs-texted-count.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CTi10-AC1`, and flip `<status>` to `complete` only when the
criterion passes and the instance is VALID. Your surprise rows are `NFRA_CTLPLN-W38-S<k>`; append lines only to the
investigation file and keep its existing line endings.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.inbound6.md</decomp_doc>
<owned_cells>CT-i-10</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/inbound_count.py
data/transcripts/scripts/tests/test_inbound_count.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing; the reader runs on demand, never on a clock (no monitor is built).
comp-iam: DECLARED-NOT-APPLICABLE -- denominator: 0 policies and 0 AWS calls in this cell; the issuer's real run uses the laptop's existing read identity. BLIND: whether that identity reads the agent's log group is measured at the real run, not here.
comp-adversary: RUN -- message text leaking into a terminal or file (arm `no_text`); a first page taken as the answer (arm `pages`); a UTC day mistaken for his day (arm `day_edge`); his own messages counted as missed (arm `own_and_system`); a count that cannot move (the unexplained arm's control). BLIND: a message the poll never read is invisible to this reader; the docstring says so and CT-i-9 carries that case.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.20 @ce40c9292d (ADMITTED), FWD-20; `1.0.0_SA_CTO` direction msg 107165 item (4).

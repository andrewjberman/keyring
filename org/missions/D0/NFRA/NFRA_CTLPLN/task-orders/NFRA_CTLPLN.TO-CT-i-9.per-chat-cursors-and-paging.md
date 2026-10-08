# TO NFRA_CTLPLN.TO-CT-i-9 -- workstream INBOUND round 6 CT-i-9: the Teams poll keeps a cursor per chat and reads every page

<to_id>NFRA_CTLPLN.TO-CT-i-9</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~37</issued_to>
<issued_by>2.0.0_SA_COO~R</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>INBOUND</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-i-9` (`decompositions/NFRA_CTLPLN_DECOMP.inbound6.md`) | **outcome_ref:** FWD-20 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CT-i-9`. Andrew's Teams assistant (a Lambda, code in `data/transcripts/scripts/teams_chat/`) polls Teams once a minute through
`poll_chats()` in `data/transcripts/scripts/teams_chat/tenant.py` (line ~813). He reports that Teams messages fall through.
Three defects are in that function as it stands:

1. **One cursor for every chat.** `cursor.json` holds one `since`. It advances to the newest `last_message_at` of ANY chat. A
   chat whose last-message time is older than another chat's newer message at the moment it is first seen (Graph indexes the
   preview late) compares `last <= since` on every later poll and is never read. Its messages are lost silently.
2. **One page of chats.** `gw.chats()` returns at most 50 chats (`page_size` 50 is the gateway's maximum) and the function never
   follows `next_page_token`. The gateway orders chats by last message, newest first.
3. **One page of messages.** `gw.messages(chat_id)` returns the newest 50 of a chat, newest first; a chat with more than 50 new
   messages since the cursor loses the older ones.

The gateway client is `assist.Gateway` (`data/transcripts/scripts/teams_chat/assist.py`, ~line 156): `chats(page_token=None,
page_size=50)` and `messages(chat_id, page_token=None, page_size=50)` each return `{"rows": [...], "count": n,
"next_page_token": str | None}`. A chat row has `chat_id`, `chat_type`, `topic`, `last_message_at` (ISO UTC), `members`; a
message row has `id`, `created` (ISO UTC), and other fields. `a.get_json(key)` / `a.put_json(key, obj)` read and write the
state store; `a.state_key("cursor.json")` is the cursor's key; `a.bronze_key(chat_id, m)`; `ldo.send(object_id, kind, payload,
event_id=...)` queues an event (the event id de-duplicates: the same id sent twice is one event).

### BUILD, IN THIS ORDER

1. Rewrite `poll_chats()` in `tenant.py` and nothing else in that file except small private helpers beside it:
   - **Cursor v2:** `cursor.json` = `{"v": 2, "chats": {<chat_id>: <ISO created of the newest message delivered>}, "floor": <ISO>,
     "polled_at": <ISO>}`. A chat's message is new when its `created` is later than THAT chat's cursor.
   - **A chat not yet in `chats`** uses `floor` as its cursor. `floor` = the previous poll's `polled_at` minus a lag margin
     `LAG_MARGIN_S = 900` (a named constant), so a chat whose preview lands late is still read. Messages already delivered are
     not sent twice: the event id stays `msgs-<chat key>-<newest id>`, and bronze writes are idempotent.
   - **Migration:** a v1 cursor (`{"since": ...}`) is read as v2 with `floor = since` minus the margin and an empty `chats`;
     nothing older than that is replayed. No cursor at all (the first run) keeps today's behaviour: deliver nothing, record
     every chat's newest time as its cursor.
   - **Chat paging:** follow `next_page_token` until there is none, OR until a chat's `last_message_at` is older than `floor`
     and older than every cursor that could admit it (the list is newest first, so nothing after it is new). Never stop at a
     fixed page count.
   - **Message paging:** for a chat with new messages, follow its pages until a page holds a message at or before the chat's
     cursor, or there is no next page. Send every new message, oldest first in the payload, in one `teams.messages` event per
     chat as today. Advance the chat's cursor to the newest `created` sent.
   - Keep the log line `a.log("ingress_poll", ...)` and add the counts `chats_read=<n>`, `pages=<n>`, `messages=<n>`.
   - One failing chat (a `GatewayError` on its messages) does not stop the others: log it by chat key and leave that chat's
     cursor where it was.
2. NEW `data/transcripts/scripts/tests/test_inbound_poll_cursors.py` (a plain script, no network; fake gateway, fake store and
   fake `ldo.send` injected the way `data/transcripts/scripts/tests/test_teams_chat_tenant.py` injects them -- read it first).
   Arms, each printing one `ARM <name> ok=<True|False>` line:
   - `late_preview`: chat A's message at T-60s is first visible after chat B's message at T-10s moved the poll on; A's message
     is delivered on the next poll. **Difference control in the same arm:** the same two-poll scenario run against the BASE
     function (load it from git: `git show HEAD:data/transcripts/scripts/teams_chat/tenant.py` into a temp module) misses A's
     message; the arm is ok only when the new code delivers it AND the base misses it.
   - `many_chats`: 120 chats over three pages, a new message only in the 75th; it is delivered.
   - `many_messages`: 130 new messages in one chat over three pages; all 130 delivered, once each, oldest first.
   - `migration`: a v1 cursor; no message older than `since` minus the margin is sent; one newer message is.
   - `first_run`: no cursor; nothing is sent; every chat gets a cursor.
   - `one_chat_fails`: chat 2's messages raise `GatewayError`; chats 1 and 3 are delivered; chat 2's cursor is unchanged.
   LAST line `POLL-CURSORS ok=<True|False> arms=<passed>/<total> base_missed_late=<True|False>`.

### RULES FOR THIS CELL

- **Nothing you run leaves this machine**: no S3, gateway, Graph, model or text call. Everything is injected.
- Edit nothing but the files in `<paths>`. Do not change `on_chat_messages`, `ROUTES`, `ingress` or any other function's
  behaviour; another cell of this round adds a step to `ingress` at the merge.
- No real message, person's, client's or firm's name in any file you write. No non-ASCII. Bake no absolute path.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTi9-AC1" cell_refs="CT-i-9"><invocation>python data/transcripts/scripts/tests/test_inbound_poll_cursors.py</invocation><expect>POLL-CURSORS ok=True</expect></criterion>
`CTi9-AC1` -- the built behaviour and its difference control in one run: six arms, and the late-preview arm proves the base loses the message the new code delivers.

<criterion id="CTi9-AC2" cell_refs="CT-i-9"><invocation>python -m pytest -q -p no:cacheprovider data/transcripts/scripts/tests/test_teams_chat_tenant.py && echo TENANT-SUITE ok=True</invocation><expect>TENANT-SUITE ok=True</expect></criterion>
`CTi9-AC2` -- the cell's bound: the 19 existing tenant cases (19 passed at the base, issuer's dry run) still pass on the file this cell edits.
</proof_of_spec>

<expected_criteria>CTi9-AC1,CTi9-AC2</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~37/NFRA_CTLPLN.TO-CT-i-9.per-chat-cursors-and-paging.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CTi9-AC1,CTi9-AC2`, and flip `<status>` to `complete` only when
both criteria pass and the instance is VALID. Your surprise rows are `NFRA_CTLPLN-W37-S<k>`; append lines only to the
investigation file and keep its existing line endings.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.inbound6.md</decomp_doc>
<owned_cells>CT-i-9</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/tenant.py
data/transcripts/scripts/tests/test_inbound_poll_cursors.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing; the minute clock is unchanged.
comp-iam: DECLARED-NOT-APPLICABLE -- denominator: 0 policies and 0 AWS calls in this cell; the face forbids every network call. BLIND: none claimed; this lens reads nothing here.
comp-adversary: RUN -- a replay storm at the migration (bounded: nothing older than the old cursor minus the margin is sent, arm `migration`); a duplicate text from the margin (the event id is unchanged, so a re-sent window is one event); a paging loop that never ends (stops on no token or on an old chat; arm `many_chats`); a test that passes on the base (the late-preview arm requires the base to miss); one bad chat stalling all (arm `one_chat_fails`). BLIND: whether Graph's preview lag ever exceeds 15 minutes is not measured here; CT-i-10's count is the real-world read.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.20 @ce40c9292d (ADMITTED), FWD-20; `1.0.0_SA_CTO` direction msg 107165 items (1) and (3).

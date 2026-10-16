# TO COMM_ASSIST.TO-CA-n-1 -- round 21 CA-n-1: the channel poller also reads replies in older threads (the pinned End of Day parent and recently active posts)

<to_id>COMM_ASSIST.TO-CA-n-1</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~32</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>THREADREPLIES</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-n-1` (`decompositions/COMM_ASSIST_DECOMP.round21.md`) | **outcome_ref:** FWD-3, FWD-13 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`data/transcripts/scripts/teams_chat/channel_mentions.py` finds Teams channel posts and replies that @mention Andrew. Its
`_read_channel` reads the newest pages of TOP-LEVEL posts (each with its embedded `replies`) and stops at the first page that holds
nothing newer than the channel's cursor. So a reply posted under an OLDER post is never read. The End of Day Updates channel keeps
ONE parent post that everyone replies under (`assist.EOD_TEAM_ID`, `assist.EOD_CHANNEL_ID`, `assist.EOD_PARENT_ID`), so a real
@mention there was missed. You make the poller also read the replies of a bounded set of threads through the gateway's replies
route, `gw.replies(team_id, channel_id, message_id, page_token=None, page_size=50)`, which returns `{"rows": [...], "next_page_token": ...}`
with rows NEWEST FIRST, each row shaped like a channel message (`id`, `created`, `from_user_id`, `mentions`, `deleted`, `body_html`, ...).

### WHAT TO BUILD (in `channel_mentions.py` only)

1. Three constants beside the others: `THREAD_DAYS = 14`, `THREAD_MAX = 10`, and
   `PINNED_THREADS = {(a.EOD_TEAM_ID, a.EOD_CHANNEL_ID): (a.EOD_PARENT_ID,)}` (threads read whatever their age).
2. `_read_channel` also returns, as a FOURTH value, `seen`: `{root_id: newest created}` over every root on the pages it read, where a
   root's value is the newest `created` of the root itself and its embedded replies. Keep every existing behaviour (cursor, pages,
   events, `complete`) exactly as it is, and return the four values on every return path.
3. A new `_read_threads(gw, team_id, team_name, chan, threads, me_id, budget, now, emitted)` that reads, for ONE channel, the pinned
   threads first and then the other tracked threads by `active` newest first, at most `THREAD_MAX` in all. For each, if
   `budget.left()` is false stop; else `budget.take()` and call `gw.replies(team_id, chan["id"], root_id)` ONE page. `threads` is
   `{root_id: {"cursor": str|None, "active": str}}`, updated in place. A thread whose `cursor` is None (first read) sends NOTHING and
   only sets its cursor. Otherwise each reply with `created` newer than the cursor that is not deleted, not from Andrew (`me_id`),
   mentions Andrew (`_mentions_me`), and whose `id` is not in the set `emitted`, becomes ONE event shaped exactly like a reply event
   of `_read_channel`: `("chan:%s|%s|%s" % (team_id, chan["id"], root_id), KIND, {"team": ..., "channel": ..., "message": <the row
   without attachments and replies>}, "mention-%s" % <reply id>)`, and its id is added to `emitted`. Then set the thread's `cursor`
   to the newest `created` seen (or `a.iso(now)` when the page is empty) and raise `active` to it when newer. Return the events.
4. In `poll`: load `threads = state.get("threads") or {}` from the cursors file, keyed `"<team>|<channel>"` -> the per-channel dict.
   After each successful `_read_channel`, for that channel: add every `seen` root whose value is at most `THREAD_DAYS` days old
   (`_age_s(value, now) <= THREAD_DAYS * 86400`) with `{"cursor": None, "active": value}` (raise `active` if it is already tracked);
   drop every tracked root that is not pinned and whose `active` is older than `THREAD_DAYS`; then call `_read_threads` with
   `emitted` = the reply ids of this channel's events from `_read_channel`, and add its events to the channel's events before they
   are sent. A `GatewayError` from `_read_threads` counts in `failed` and `errors` exactly like a channel read failure, and the other
   channels still run. Save `threads` in the same `put_json` as `cursors` and `read_at`: `{"cursors", "read_at", "threads"}`.
   Thread reads count against the same `MAX_CALLS` budget.

### THE TEST FILE EDIT (in `data/transcripts/scripts/tests/test_inbound_channel_mentions.py`, these two changes only)

- `FakeGW` gains `def replies(self, team_id, channel_id, message_id, page_token=None, page_size=50)` that appends `"replies"` to
  `self.calls` and returns `{"rows": [], "count": 0, "next_page_token": None}`.
- In `arm_budget`, the line `paged = gw2.calls.count("messages") == cm.MAX_PAGES and out2["calls"] == cm.MAX_PAGES` becomes
  `paged = gw2.calls.count("messages") == cm.MAX_PAGES and out2["calls"] == cm.MAX_PAGES + gw2.calls.count("replies")`.
Change no other test, name or assertion.

### THE CONTRACT

`org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r21/checks/check_n1_threads.py` (READ it, do not edit it): seven arms
-- the pinned End of Day parent's reply is caught, a recent post's reply seen only through the replies route is caught, a first read
is silent, no repeat, the not-Andrew cases send nothing (with a difference control), a stale post is not read while the pinned parent
is, and one poll stays within `MAX_CALLS`.

### RULES

- Edit nothing but the files in `<paths>`. No non-ASCII. Do not change the event shape, the cursor file name, `MAX_CALLS`,
  `MAX_PAGES` or `CHANNEL_EVERY_S`. Never log message text.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAn1-AC1" cell_refs="CA-n-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r21/checks/check_n1_threads.py"</invocation><expect>N1-THREADS ok=True arms=7 of 7</expect></criterion>
`CAn1-AC1` -- the built behaviour: the issuer's seven arms. It prints 1 of 7 at the base (only `budget` passes).

<criterion id="CAn1-AC2" cell_refs="CA-n-1"><invocation>python data/transcripts/scripts/tests/test_inbound_channel_mentions.py</invocation><expect>CHANNEL-MENTIONS ok=True arms=7/7</expect></criterion>
`CAn1-AC2` -- the existing channel-mention arms still pass with the two test edits above (7/7 at the base; without the edits they
fail against a correct build).

<criterion id="CAn1-AC3" cell_refs="CA-n-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i2_regression.py"</invocation><expect>I2-REGRESSION ok=True</expect></criterion>
`CAn1-AC3` -- the bound, a control that PASSES at the base (64 passed): the assistant's flow tests.
</proof_of_spec>

<expected_criteria>CAn1-AC1,CAn1-AC2,CAn1-AC3</expected_criteria>

Each invocation runs from the worktree root, by that RELATIVE path, under `timeout 280`. Commit the edits FIRST. Then write the proof
instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~32/COMM_ASSIST.TO-CA-n-1.read-replies-of-recent-threads.proof_of_spec.json`,
modelled on `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~31/COMM_ASSIST.TO-CA-l-3.batch-three-sibling-bare-imports.proof_of_spec.json`,
recording each invocation EXACTLY as the criterion text (no `timeout` prefix) and pinning each artifact row to the commit that
carried it. Flip `<status>` to `complete` only when all three pass. Validate with the WORKTREE'S OWN `.tools/proof-of-spec-check.py`
from inside the worktree AFTER your last commit: `python .tools/proof-of-spec-check.py <instance> CAn1-AC1,CAn1-AC2,CAn1-AC3`; its
LAST line must be `VALID (rc=0)` at the final head. Your final report names each function you changed and the arm counts. Your
surprise rows are `COMM_ASSIST-W32-S<k>`; append only to the investigation file and keep its existing line endings; `surfaced_at` =
`date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh` as your serial; write the commit message file with your Write tool
(never a shell heredoc), ending with the attribution line the harness gives you.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round21.md</decomp_doc>
<owned_cells>CA-n-1</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/channel_mentions.py
data/transcripts/scripts/tests/test_inbound_channel_mentions.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-n-1.read-replies-of-recent-threads.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~32/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing (the poll's existing one-minute cadence is unchanged).
comp-iam: DECLARED-NOT-APPLICABLE no grant moves; the replies route is already granted (assist.py `replies`, used by the End of Day reader).
comp-adversary: RUN -- a fix that reads every post's replies (refused: `budget` arm, at most MAX_CALLS per poll, and THREAD_MAX per channel); a fix that alerts on history on its first read (refused: `first_read_silent`); a fix that repeats an alert (refused: `no_repeat`); a fix that alerts on someone else's mention or his own reply (refused: `not_him`, with a difference control); a fix that drops the End of Day parent as stale (refused: `stale_dropped` second half). BLIND: the gateway's real reply ordering is taken from assist.py's End of Day reader (newest first, about two thousand replies over 40 pages); a reply beyond the first page of a busy thread between two reads is not read (one page per thread per read, every 5 minutes); a post older than 14 days with a new reply is read only if pinned.
naming: no name is created (CLAUDE.md rule 30 non-application).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base: CAn1-AC1 base: FAIL as measured (1 of 7; `budget` passes). Green arm 7 of 7 against a scratch reference implementation (65 added lines; removed afterwards). CAn1-AC2 base: PASS as measured (7/7, 4/4); against the reference WITHOUT the two test edits it fails (the fake gateway has no `replies`; the budget arm counts reply calls as pages), WITH them 7/7 and 4/4. CAn1-AC3 base: PASS as measured (control, 64 passed).
Source: CTO ruling on call 446a (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_446A_COMM_ASSIST_TEAMS_THREAD_REPLY_MENTIONS_20261016.md` @f418537712, msg 109753); the CA-k-5 exercise (off the repository on Andrew's word): ingress `channel_poll` 12:00Z-18:5xZ, 419 polls, `channels=8`, `mentions=0`.

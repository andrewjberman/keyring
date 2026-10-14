# TO COMM_ASSIST.TO-CA-j-12 -- round 18 CA-j-12: the assistant keeps two small metadata-only records, a channel @mention record and a considered-mail log (FWD-13, assistant half)

<to_id>COMM_ASSIST.TO-CA-j-12</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~24</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>MENTREC</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-j-12` (`decompositions/COMM_ASSIST_DECOMP.round18.md`, AMENDMENT 8) | **outcome_ref:** FWD-13 |
**depends_on:** none (PRD v0.10 ADMITTED; the CTO ruling on call 608c, msg 109140)

---

## WORKER FACE

### THE CELL

Andrew wants his operator agent muse to TELL him of each new Teams or mail item for him, reading the dell2 folder the assistant already feeds (PRD FWD-13). Today the folder cannot show two kinds of item: a channel @MENTION (`channel_mentions.on_channel_mention` texts him once and keeps no record) and most mail (`mail_requests.on_mail_messages` keeps ONE `state["pending"]`, so a newer considered mail replaces the older). The CTO ruled the assistant may keep two small records, METADATA ONLY (never a message body, a link or anything actionable), each written where its item is texted today, with a 7-day expiry enforced on write. This cell writes them. A different cell (CA-j-13) makes the dell2 reader publish them; you touch no reader code.

### THE CONTRACT (fixed by the issuer; the check pins every key)

- **Mention record.** `channel_mentions.on_channel_mention(ctx)`, in the place where it texts the mention and ONLY when it texts (the paused path writes nothing), keeps `ctx.state["mentions"]`, a list, oldest first. It appends exactly one entry per mention:
  `{"id": "<team id>|<channel id>|<message id>", "team": <team display name>, "channel": <channel display name>, "from": <sender display name, "?" when absent>, "snippet": <below>, "mentioned_at": <the message's own "created">, "seen_at": <ctx.now() as a UTC ISO string like 2026-10-14T13:00:00Z>}` and NO other key.
  The same `id` seen again (a retry) adds nothing. On every write, entries whose `seen_at` is more than 7 days before `ctx.now()` are dropped, and only the newest 50 are kept.
- **Mail log.** `mail_requests.on_mail_messages(ctx)`, for each CONSIDERED mail (the ones it texts today), after `ctx.state["pending"]` is set, appends to `ctx.state["mail_log"]` exactly:
  `{"seq": <that draft's seq>, "tag": <its tag>, "considered_at": <ctx.now() as UTC ISO>, "from": <the sender's display name, the same value the text uses>, "domain": <the sender address's domain, lowercase>, "firm": <the firm, or "firm">, "subject": <scrubbed as the snippet, at most 120 characters>}` and NO other key: never the body, never an address. On every write entries older than 7 days (by `considered_at`) are dropped, and only the newest 10 are kept. A mail that is not considered adds nothing.
- **The scrub.** One small helper (put it in a NEW module `data/transcripts/scripts/teams_chat/folder_records.py` with the shared 7-day/cap pruning): `snippet(text, limit=120)` strips HTML tags, collapses whitespace, REMOVES links (`https?://\S+`), anything shaped like an address (`\S+@\S+`) and any run of 20 or more characters from `[A-Za-z0-9+/_=-]` (tokens, keys, hashes), and cuts to `limit`. Use it for the mention snippet (from the message's body) and the mail subject.
- Standard library only. No AWS call, no network. No non-ASCII. Do not change what is texted to Andrew, the drafts, `state["pending"]`, `draft_seq` or any existing key.

### BUILD, IN THIS ORDER

1. Create `folder_records.py`: `snippet`, and a pruning helper used by both writers.
2. Write the mention record in `channel_mentions.py` and the mail log in `mail_requests.py` as the contract says.
3. Tests: `data/transcripts/scripts/tests/test_inbound_channel_mentions.py` has a handler arm whose `Ctx` has no `state` and no `now()`: give its `Ctx` both (a `state` dict, and a `now()` returning a fixed UTC time) and add arms for the new record (written once per mention, a retry adds none, the paused path writes none). Add mail-log arms to `data/transcripts/scripts/tests/test_inbound_mail_draft.py` (its `Ctx` already has `state` and `now()`). Add `data/transcripts/scripts/tests/test_folder_records.py` for the helper (links, addresses and tokens removed, the 120 cut, the 7-day and cap pruning). Run EVERY test file under `data/transcripts/scripts/tests` that touches mentions or mail (the scripts run as `python <file>`; the rest under pytest) and keep them passing; a test outside your `<paths>` must pass unmodified.
4. No non-ASCII.

### RULES

- Edit nothing but the files in `<paths>`. Code and tests; NOT deployed here (a later cell deploys it under its own sign-offs).
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAj12-AC1" cell_refs="CA-j-12"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_k1_records.py"</invocation><expect>K1-RECORDS ok=True arms=8 of 8</expect></criterion>
`CAj12-AC1` -- the issuer's check (read it; do not edit it): the mention record has exactly the seven keys, a stable id, a snippet of at most 120 characters with no tag, link, address or token, `mentioned_at` equal to the message's `created`; a retry adds none; expiry and the cap of 50 apply on write; the paused path writes none; the mail log has exactly the seven keys with `seq` and `tag` equal to the pending draft's, two mails give two rows while `pending` holds one, expiry and the cap of 10 apply on write, and neither the body nor any address appears. It prints 1 of 8 at the base.

<criterion id="CAj12-AC2" cell_refs="CA-j-12"><invocation>python data/transcripts/scripts/tests/test_inbound_channel_mentions.py</invocation><expect>CHANNEL-MENTIONS ok=True arms=7/7</expect></criterion>
`CAj12-AC2` -- the bound, a control that PASSES at the base and must still pass after you give its handler arm a state and a clock: the mention path's own seven arms.

<criterion id="CAj12-AC3" cell_refs="CA-j-12"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i2_regression.py"</invocation><expect>I2-REGRESSION ok=True</expect></criterion>
`CAj12-AC3` -- the bound, a control that PASSES at the base and must still pass: the assistant's flow tests.
</proof_of_spec>

<expected_criteria>CAj12-AC1,CAj12-AC2,CAj12-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 250`. Commit the code and tests FIRST. Then write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~24/COMM_ASSIST.TO-CA-j-12.assistant-keeps-mention-and-mail-records.proof_of_spec.json`, modelled on `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~23/COMM_ASSIST.TO-CA-j-9.ingress-mark-four-hour-freshness.proof_of_spec.json`, recording each invocation EXACTLY as the criterion text (no `timeout` prefix) and pinning each artifact row to the commit that carried it (a row left as pending-this-commit goes INVALID the moment a later commit lands). Flip `<status>` to `complete` only when all three pass. Validate by running the WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree AFTER your last commit: `python .tools/proof-of-spec-check.py <instance> CAj12-AC1,CAj12-AC2,CAj12-AC3`, and read the LAST line: it must be `VALID (rc=0)` at the final head. Your final report names the changed lines, the helper's interface, every existing test you changed, the tests you added, and the passed/failed count of every test file you ran. Your surprise rows are `COMM_ASSIST-W24-S<k>`; append only to the investigation file and keep its existing line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh` as your serial.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round18.md</decomp_doc>
<owned_cells>CA-j-12</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/folder_records.py
data/transcripts/scripts/teams_chat/channel_mentions.py
data/transcripts/scripts/teams_chat/mail_requests.py
data/transcripts/scripts/tests/test_folder_records.py
data/transcripts/scripts/tests/test_inbound_channel_mentions.py
data/transcripts/scripts/tests/test_inbound_mail_draft.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-j-12.assistant-keeps-mention-and-mail-records.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~24/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves and no AWS call is made; the deploy is a later cell with its own pair.
comp-adversary: RUN -- a record that keeps the message body or a link (refused: AC1 `mention-record` and `mail-record` arms put a link, an address, a key and a hash in the source and read the stored text); an address or the body in the mail log (refused: AC1 `mail-no-body-no-address`); a record that grows without end (refused: AC1 expiry-and-cap arms for both); a retry that records twice (refused: AC1 `mention-retry-once`); a record written when nothing is texted (refused: AC1 `mention-paused-writes-nothing`); the text, the draft or `pending` changed (refused: AC2 and AC3 and the existing mail tests). BLIND: the live state table is not read here; a real mention and a real mail are read only after the deploy and the dell2 pick-up (cells CA-j-14, CA-j-15).
naming: no name is created (CLAUDE.md rule 30 non-application).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base: CAj12-AC1 base: FAIL as expected (1 of 8: only the paused arm holds). CAj12-AC2 base: PASS as expected (control, 7 of 7). CAj12-AC3 base: PASS as expected (control). AC1 green arm: PASS as expected (8 of 8) against a scratch reference (the two handlers patched in a throwaway worktree, removed); a negative control that keeps links in the snippet reads 6 of 8 (`mention-record` and `mail-record` fail).
Source: CTO ruling on call 608c (`RULING_20261014_124xZ_COMM_ASSIST_608C_FWD13_TWO_SCRUBBED_RECORDS.md`, msg 109140); PRD v0.10 FWD-13; muse's requested shape (Gmail thread, 2026-10-14 13:16Z); `channel_mentions.on_channel_mention`; `mail_requests.on_mail_messages` (the single `pending` at line 273).

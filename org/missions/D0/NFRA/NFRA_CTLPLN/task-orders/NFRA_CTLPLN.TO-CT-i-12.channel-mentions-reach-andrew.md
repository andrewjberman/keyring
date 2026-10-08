# TO NFRA_CTLPLN.TO-CT-i-12 -- workstream INBOUND round 6 CT-i-12: a channel post or reply that @mentions Andrew reaches him by text

<to_id>NFRA_CTLPLN.TO-CT-i-12</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~40</issued_to>
<issued_by>2.0.0_SA_COO~R</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>INBOUND</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-i-12` (`decompositions/NFRA_CTLPLN_DECOMP.inbound6.md`) | **outcome_ref:** FWD-20 |
**depends_on:** none (builds against the pinned contract below; another cell builds the gateway side in parallel)

---

## WORKER FACE

### THE CELL

`CT-i-12`. Andrew's Teams assistant (a Lambda; code in `data/transcripts/scripts/teams_chat/`; the minute clock is
`tenant.ingress`) reads his 1:1 and group CHATS only. A channel post or reply that @mentions him never reaches him. This cell
builds the assistant's side of reading channel @mentions and texting him once per mention. The gateway's side (three new read
routes) is being built in parallel by another cell, to this contract:

```
GET /hx/teams/teams                                     -> {"rows": [{"team_id", "display_name"}], "count", "next_page_token"}
GET /hx/teams/teams/{team_id}/channels                  -> {"rows": [{"channel_id", "display_name", "membership_type"}], "count", "next_page_token"}
GET /hx/teams/channels/{team_id}/{channel_id}/messages  -> {"rows": [MSG + {"replies": [MSG, ...]}], "count", "next_page_token"}
MSG = {"id", "created", "last_modified", "from_name", "from_user_id", "from_app", "reply_to_id", "message_type", "deleted",
       "body_html", "attachments", "mentions": [{"user_id", "name"}]}
```

What exists to use (read these first): `assist.Gateway` (`assist.py` ~line 156; `_call`, `_seg`, the `chats`/`messages`
methods are the pattern); `assist.me()` -> `{"id", ...}` (his user id); `assist.assistant_on()` (his `#on`/`#off` switch);
`assist.get_json` / `put_json` / `state_key`; `assist.html_to_text`; `assist.send_sms(text, tag)`; `assist.log(event, **ids)`
(ids and counts only, never text); `ldo.send(object_id, kind, payload, event_id=...)` (the event id de-duplicates);
`tenant.text_andrew(ctx, key, body, tag)` is `ctx.once("sms:%s" % key, lambda: a.send_sms(body, tag))` -- one text per key per
object, never repeated on a retry. How tests inject a fake gateway, store and `ldo`:
`data/transcripts/scripts/tests/test_teams_chat_tenant.py`.

### BUILD, IN THIS ORDER

1. `assist.py`: three `Gateway` methods, `teams(page_token=None, page_size=50)`, `channels(team_id, page_token=None,
   page_size=50)`, `channel_messages(team_id, channel_id, page_token=None, page_size=50)`, on the contract's paths, ids
   through `_seg`. Nothing else in `assist.py` changes.
2. NEW `data/transcripts/scripts/teams_chat/channel_mentions.py`:
   - `poll(gw, me_id, now) -> dict`, called once a minute (the issuer adds the call to `tenant.ingress` at the merge):
     - the list of teams and channels is refreshed at most once an hour (`LIST_TTL_S = 3600`), kept in state `channels.json`;
     - each channel's posts are read at most once every `CHANNEL_EVERY_S = 300` seconds, round robin, and one poll makes at
       most `MAX_CALLS = 20` gateway calls in all (named constants);
     - each channel keeps its own cursor (the newest `created` it has seen across posts and replies) in state
       `channel_cursors.json`; a channel read follows `next_page_token` until a page holds no post or reply newer than the
       cursor, at most `MAX_PAGES = 3` pages (a named bound; say in the docstring what a busier channel loses and that the
       count reader of this round would show it);
     - a post or reply newer than the cursor whose `mentions` holds `me_id`, not deleted and not his own, becomes ONE event:
       `ldo.send("chan:<team_id>|<channel_id>|<root post id>", "teams.channel_mention", {team, channel, message}, event_id=
       "mention-<message id>")`, where team and channel carry ids and display names and message is the MSG row without
       `attachments`;
     - the first run (no cursors) sends nothing and records a cursor per channel;
     - one channel failing (`GatewayError`) does not stop the others; its cursor stays;
     - returns counts: `channels`, `read`, `calls`, `mentions`, `failed`; logs them with `assist.log("channel_poll", ...)`.
   - `on_channel_mention(ctx) -> str`, the handler for kind `teams.channel_mention` (the issuer adds the route entry at the
     merge): when `assist.assistant_on()` is false return `"paused"`; else ONE text through `ctx.once("sms:mention:<message
     id>", ...)`: `@ <team> / <channel> - <from>: <first 300 characters of the body as text>` and a last line `Reply in Teams.`;
     return `"texted"`. No draft and no send to Teams (a reply flow is a later round).
3. NEW `data/transcripts/scripts/tests/test_inbound_channel_mentions.py` (a plain script, no network; fakes injected). Arms,
   each printing `ARM <name> ok=<True|False>`:
   - `post_mention`: a new post mentioning him -> one event with the right object id and event id.
   - `reply_mention`: a new reply under an old post mentioning him -> one event whose object id names the root post.
   - `not_him`: a mention of someone else, a post with no mention, his own post mentioning himself, a deleted post -> no event.
     **Difference control in the same arm:** the same post with his id added to `mentions` -> one event.
   - `once`: the same mention seen on two polls -> the same event id both times (one event).
   - `first_run`: no cursors -> no event, every channel gets a cursor.
   - `budget`: 40 channels -> no poll makes more than `MAX_CALLS` calls, and every channel is read within the polls a
     5-minute window allows (state the arithmetic in the test).
   - `handler`: with the switch on, one text whose body has the team, channel and sender and no more than 300 body characters;
     a retry of the same event sends nothing more; with the switch off, `"paused"` and no text.
   LAST line `CHANNEL-MENTIONS ok=<True|False> arms=<passed>/<total>`.

### RULES FOR THIS CELL

- **Nothing you run leaves this machine**: no S3, gateway, Graph, model or text call. Everything is injected.
- Edit nothing but the files in `<paths>`. Do NOT edit `tenant.py` (another cell of this round rewrites a function there; the
  issuer adds your two hookups at the merge) -- say in your report the two lines the hookup needs.
- No real message, person's, client's, team's or firm's name in any file you write. No non-ASCII. Bake no absolute path.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTi12-AC1" cell_refs="CT-i-12"><invocation>python data/transcripts/scripts/tests/test_inbound_channel_mentions.py</invocation><expect>CHANNEL-MENTIONS ok=True</expect></criterion>
`CTi12-AC1` -- the built behaviour and its difference control in one run: seven arms; the not-him arm turns into one event when his id is added.

<criterion id="CTi12-AC2" cell_refs="CT-i-12"><invocation>python -m pytest -q -p no:cacheprovider data/transcripts/scripts/tests/test_teams_chat_tenant.py data/transcripts/scripts/tests/test_teams_chat_assist.py && echo ASSIST-SUITE ok=True</invocation><expect>ASSIST-SUITE ok=True</expect></criterion>
`CTi12-AC2` -- the cell's bound: the existing tenant and assist cases still pass with the three new `Gateway` methods (passed at the base, issuer's dry run).
</proof_of_spec>

<expected_criteria>CTi12-AC1,CTi12-AC2</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~40/NFRA_CTLPLN.TO-CT-i-12.channel-mentions-reach-andrew.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CTi12-AC1,CTi12-AC2`, and flip `<status>` to `complete` only
when both criteria pass and the instance is VALID. Your surprise rows are `NFRA_CTLPLN-W40-S<k>`; append lines only to the
investigation file and keep its existing line endings.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.inbound6.md</decomp_doc>
<owned_cells>CT-i-12</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/channel_mentions.py
data/transcripts/scripts/teams_chat/assist.py
data/transcripts/scripts/tests/test_inbound_channel_mentions.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell adds no schedule; it runs inside the existing minute clock, bounded by MAX_CALLS.
comp-iam: DECLARED-NOT-APPLICABLE -- denominator: 0 policies and 0 AWS calls in this cell; the face forbids every network call. BLIND: none claimed.
comp-adversary: RUN -- a text storm at the first run (first run sends nothing, arm `first_run`); a duplicate text on a retry or a re-read (event id per message and `ctx.once` per message, arms `once` and `handler`); a gateway hammered every minute (MAX_CALLS and the 5-minute channel cadence, arm `budget`); a mention of someone else or a channel-wide mention texting him (arm `not_him` and its control); message text in logs (ids and counts only); a text while he is switched off (arm `handler`). BLIND: Graph's real ordering of channel posts with expanded replies is not observable offline; MAX_PAGES bounds the cost and the drain's real mention is the seam probe.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.20 @ce40c9292d (ADMITTED), FWD-20; `1.0.0_SA_CTO` direction msg 107165 item (2).

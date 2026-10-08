# NFRA_CTLPLN decomposition -- WORKSTREAM INBOUND, round 6: every Teams message reaches the agent -- per-chat cursors, no chat cap, channel @mentions read, and a received-vs-texted count (issuer 2.0.0_SA_COO~R; cut 2026-10-08 ~20:1xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

Rounds 1 to 5 are drained; eight orders terminal. The Teams agent's deploy is APPLIED (order NFRA_CTLPLN.TO-APPLY-11, live
08:15Z 2026-10-08). This workstream is the work of macro COMM (D9, ratified @0dcb083716); it is driven here, under
NFRA_CTLPLN, until a COMM tree row exists ("Fast build, no registration yet").

**Cut on:** `1.0.0_SA_CTO` direction msg 107165 (relayed by `0.0.0_AB_MSTR` msg 107168), quoted: "Drive: (1) per-chat cursors in
tenant.py poll_chats, (2) channel @mentions read, (3) no 50-chat cap, (4) a received-vs-texted count, (5) email feeding the same
text path once site Z's mail-domain admission releases, client mail flagged." Andrew's word: "I feel like I am not getting all
the team's messages. It seems like a lot of them are falling through" (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_184xZ_FIVE_POINTS_KIMMY_EFFICIENCY_ALYSSA_MCPORTAL_OPEN_CALLS_AGGREGATE.md`,
point 1). PRD v0.20 @ce40c9292d, ADMITTED (both halves SIGNED, read 2026-10-08 ~20:0xZ). Carrier: FWD-20.

**Measured at the base (CLOUD 637622de21), by reading the code:**

- `data/transcripts/scripts/teams_chat/tenant.py:813` `poll_chats` holds ONE cursor for every chat (`cursor.json` `since`), and
  advances it to the newest `last_message_at` of ANY chat. A chat whose last-message preview lands in Graph after another
  chat's newer message has moved the cursor compares `last <= since` on every later poll and is never read: its messages are
  lost with no log line. This is a mechanism that matches "falling through"; how often it fires is cell `CT-i-10`'s count.
- The same function reads ONE page of `/hx/teams/chats` (`assist.py:195`, `page_size=50`, the gateway's maximum at
  `teams_route.py:57`) and ONE page of each chat's messages: chat 51 onward, and message 51 onward in one chat, are never read.
- The gateway reads no channel message except one thread's replies (`teams_route.py:73-78`): a channel post or reply that
  @mentions Andrew never reaches the agent.
- Nothing counts what was received against what was texted. Every chat event's outcome IS logged already (`ldo.py:319`
  `ldo_event` with the object's hash, kind and result: `texted`, `updated`, `no-reply-wanted`, `paused`, `nothing-to-answer`,
  `answered-by-hand`), and every received message is in bronze (`assist.bronze_key`). A count needs a reader, no new runtime.

**Rule 24.** Domain: the hops between a Teams message addressed to Andrew and a text on his phone, read from the code above:
(a) chat discovery, (b) message read per chat, (c) channel read, (d) the decision to text, (e) the text. (a)+(b) -> `CT-i-9`;
(c) -> `CT-i-11` (the gateway) + `CT-i-12` (the agent); (d)+(e) are measured, not changed, by `CT-i-10`. By subtraction, the
uncovered member is MAIL (item 5): not cut, because its input -- site Z's mail-domain admission (NFRA_OPLGTW, `1.0.0_SA_CTO~O`)
-- has not released; it enters as the next round's first cell when it does. The deploys of this round's code are not cells:
each is an apply order to `0.7.0_AE_CloudOps` after the drain, under its own pair.

| cell | what | serves | risk | chain, slot |
|---|---|---|---|---|
| `CT-i-9` | `poll_chats` keeps a cursor PER CHAT, reads every page of chats and every page of a chat's new messages, and migrates the old single cursor without replaying or skipping | FWD-20 | LOCAL | A, `~37` |
| `CT-i-10` | a reader that counts, for one day, the messages received per chat against what each became (the logged result) and the texts sent; a chat with received messages and no event at all is counted `unexplained` | FWD-20 | LOCAL | B, `~38` |
| `CT-i-11` | three read routes on the gateway: Andrew's teams, a team's channels, a channel's posts with their replies; every projected message carries its mentions | FWD-20 | WORLD by its path under `infra/`; nothing is deployed | C, `~39` |
| `CT-i-12` | the agent reads channel posts and replies that @mention Andrew, at a bounded number of gateway calls a minute, each with its own channel cursor, and texts him once per mention | FWD-20 | LOCAL | D, `~40` |

**The contract between `CT-i-11` and `CT-i-12`** (pinned here, so the two build in parallel; the seam is probed at the drain):

```
GET /hx/teams/teams                                        -> {"rows": [{"team_id", "display_name"}], "count", "next_page_token"}
GET /hx/teams/teams/{team_id}/channels                     -> {"rows": [{"channel_id", "display_name", "membership_type"}], "count", "next_page_token"}
GET /hx/teams/channels/{team_id}/{channel_id}/messages     -> {"rows": [MSG + {"replies": [MSG, ...]}], "count", "next_page_token"}
MSG (every route that projects a message, chats included) gains "mentions": [{"user_id", "name"}]  (a user mention only)
```

Same bearer, same page-token and `page_size` rules (1 to 50) as the existing routes; Graph paths `/me/joinedTeams`,
`/teams/{id}/channels`, `/teams/{id}/channels/{id}/messages` with `$expand=replies`.

No edge: `CT-i-12` builds against the contract above with an injected gateway. Four chains. `fanout: 4 of 4 chains, cap 8`.

Write set (disjoint): `CT-i-9`: `tenant.py`, a new `data/transcripts/scripts/tests/test_inbound_poll_cursors.py`. `CT-i-10`: a new
`data/transcripts/scripts/teams_chat/inbound_count.py`, a new `data/transcripts/scripts/tests/test_inbound_count.py`. `CT-i-11`:
`infra/aws/ec2/opal-gateway/app/teams_route.py`, `infra/aws/ec2/opal-gateway/tests/test_teams_route.py`, and the three mount
lines in `infra/aws/ec2/opal-gateway/app/server.py` (no other cell of the round touches that file, and the route tests run
through the mounted app). `CT-i-12`: a new
`data/transcripts/scripts/teams_chat/channel_mentions.py`, `assist.py` (three Gateway client methods), a new
`data/transcripts/scripts/tests/test_inbound_channel_mentions.py`.

**Hookups at the merge (the issuer's, in one commit; no cell owns them):** `tenant.py` gains `ROUTES["teams.channel_mention"]` and one `_safe("channels", ...)` step in `ingress`.

Battery: `comp-schedule` DECLARED-NOT-APPLICABLE (no schedule changes; `CT-i-12` runs inside the existing minute clock);
`comp-iam` DECLARED-NOT-APPLICABLE (no policy; the Graph scopes the new routes need are MEASURED by `CT-i-11` and, if missing,
are a consent act after the drain, not a cell); `comp-adversary` RUN per order.

**After the drain:** this seat runs `CT-i-10`'s reader on the real archive for today and for one day before, BEFORE any deploy
(the negative arm: `unexplained` > 0 is the loss the round fixes, or the count shows the loss is elsewhere); then two apply
orders to `0.7.0_AE_CloudOps` (the agent's package; the gateway), each under its own pair; then the reader again on the first
full day after the deploy (the positive arm), and one real @mention in a channel.

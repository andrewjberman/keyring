# The Teams watch: what is breaking, for which use case -- measured 2026-09-24 13:3xZ-13:5xZ

**Seat:** `4.0.0_SA_CRO~Z`, on Andrew's direct question at this terminal ("I want to know what is breaking here, for
what use case"), from the outcome-check row *"Microsoft Graph via the Opal gateway | Teams and identity reads | read,
failing | Credential expires every 15 minutes; reads fail 33 of 33 even when it is valid | Three independent defects;
the principal's message still unread."* **Vintage:** workspace CLOUD @`316607d5ef`+, gateway source
`infra/aws/ec2/opal-gateway/app/tools.py` at HEAD; deployed gateway commit `1764e54a16` (EC2_MANIFEST.json,
deployed 2026-09-18T05:58:16Z by `0.9.0_WK_NFRA_OPLGTW~2`); watcher `.claude/skills/teams-assist/teams-watch.py`
(last engine change `3e8de96ed1`, 2026-08-20). **Instrument:** the watcher's OWN request path reproduced from a
scratch script (JSON-RPC `tools/call` to `https://mcp.opalinvest.dev/mcp/` with the live file token, Opal
Bloomberg identity, minted 13:36:42Z by another seat); shapes and counts printed, no message content read into any
record. The R-66 discriminator was CLOSED (BG msg 25528, 13:02Z) before the first call here, and every call landed on a
LIVE token, so nothing was minted (file mtime 13:36:42Z before and after ~60 calls).

## 0. The short answer

The use case is `0.0.3_BG_BBGTerminal`'s standing Teams duty (`refs/TEAMS_DUTY.md`): `teams-watch.py` polls Graph
through the gateway AS the "Opal Bloomberg" M365 account so a Teams DM from Andrew wakes the seat; the same gateway
and credential file also serve `whoami` and the SharePoint/OneDrive reads, which WORK. What is dead is the watcher's
per-chat message read, and it is dead for three independent reasons plus a fourth that is latent on this box:

1. **Credential lifetime (CONFIRMED by BG, corroborated here).** The gateway's OAuth issuer mints 15-minute tokens;
   only a live Claude session's MCP call mints a new one, and only when the old one is expired. The watcher reads
   the file and never refreshes. Corroboration on a different arm: ~60 gateway calls here on a LIVE token, file
   mtime unmoved.
2. **Reads fail with a live token -- a CODE change, deployed 09-18.** `read_chat_messages` gained a wider `$select`
   on 2026-09-11 (`684e7eb90a`, `_TEAMS_MSG_FIELDS`) so file attachments become reachable; that build reached the
   box with the 09-18 first release. Graph's `/chats/{id}/messages` returns `500 Error while processing response`
   whenever the page contains a message it cannot serialize under that projection; `/teams/.../channels/.../messages`
   with the IDENTICAL projection succeeds. The watcher reads 25 per chat, so any chat with one such message in its
   last 25 fails every cycle. That is the 33 of 33.
3. **Andrew's 2026-09-23T19:40Z message is unreadable by any path.** Empty body in every reader = inline image or
   card = `hostedContents`, a Graph collection no gateway tool fetches (the gateway's own docstring says so).
4. **Identity swap (LATENT -> LIVE at ~13:5xZ).** The credentials file holds THREE opalinvest.dev records for one
   host: `opal-gateway` and `opalgateway` carry ANDREW's identity (oid `2e21f8e5-...`), `opal-gateway-bbg` carries
   Opal Bloomberg's (oid `517aa5ee-...`). Unpinned `read_token()` takes the freshest live record regardless of
   identity. The runbook's pin (`--identity opalbloomberg`) matches the token `sub`, which the 09-15 issuer cutover
   (`d02e73c272`, OG-a-2) turned from an email into `<tid>/<oid>`, so the pinned arm exits with `no-token-for-identity`
   -- which is why the seat runs unpinned. At ~13:5xZ Andrew re-authenticated `opalgateway` at this terminal: the
   freshest live token on this box is now HIS, and the next watcher cycle here polls Teams as Andrew and drops his
   messages as its own outgoing (`self_id`/`self_name` -> `is_outgoing`).

## 1. Measured: the read failure is chat-content dependent, not universal, and the deployed projection is the new one

All calls with the Opal Bloomberg token (`opal-gateway-bbg`, live to 13:51:42Z). `list_chats` returned 7 chats.

| chat (type) | newest message | fails from `top=` | reads OK at |
|---|---|---|---|
| Andrew <-> Opal Bloomberg (oneOnOne) | Andrew Berman, 09-23T19:40:01Z, body length 0 | 1 | never |
| Opal Bloomberg <-> `7aa72700...` (oneOnOne) | Opal Bloomberg, 09-18T20:49:21Z, body length 0 | 1 | never |
| meeting "Dashboard Update and Tax SMA R..." | Manav Shah, body length 0 | 1 | never |
| group `8bb6513f...` | Alyssa Keith, body length 17 | 3 | 1, 2 |
| Opal Bloomberg <-> `ad037ea5...` (oneOnOne) | Opal Bloomberg, 09-23T20:05Z, body length 292 | 25 | 1, 2, 3, 5, 10 |
| Opal Bloomberg <-> `c727d432...` (oneOnOne) | Opal Bloomberg, 09-23T20:08Z, body length 283 | 25 | 1, 2, 3, 5, 10 |
| Yang Liu <-> Opal Bloomberg (oneOnOne) | Yang Liu, body length 16 | never | 1 .. 25 |

Every failure is the same string: `Graph 500 InternalServerError: Error while processing response.`, returned by the
gateway with `isError: false` and an `{"error": ...}` body, which `fresh_messages()` (no `value` key) turns into
"read failed ... cursor HELD". The transport is fine: HTTP 200, SSE, JSON-RPC result, and `poll_addressed_teams_messages`
answers on the same token in the same second (count 4 since 09-01 over the same four chats).

**The deployed projection IS the 09-11 list.** A message from the working chat carries exactly these keys:
`attachments, body, createdDateTime, deletedDateTime, eventDetail, from, id, importance, lastEditedDateTime,
lastModifiedDateTime, mentions, messageType, replyToId, subject, webUrl` -- `_TEAMS_MSG_FIELDS` verbatim. `git show
1764e54a16:infra/aws/ec2/opal-gateway/app/tools.py` carries `_TEAMS_MSG_FIELDS` (3 occurrences); `merge-base
--is-ancestor 684e7eb90a 1764e54a16` is TRUE (and false the other way).

**Before 09-11 the chat reader asked for six fields:** `id,from,body,createdDateTime,lastModifiedDateTime,importance`
(`git show 684e7eb90a^:...tools.py`). The nine ADDED fields are `subject, lastEditedDateTime, deletedDateTime,
messageType, attachments, mentions, replyToId, webUrl, eventDetail`.

**Channel reads with the same projection succeed:** `Opal Client Tickets` top 1/5/20 OK; `End of Day Updates` top 20
OK with one empty-body message in the page; `General` top 20 OK (17 messages). So the failure is specific to the CHAT
messages endpoint under this projection, on chats whose page holds an empty-body (inline image / card) message.

**Timeline that fits every observation:** BG's thread records real deliveries on 08-20, 09-11 (~11:5xZ, before the
17:27Z commit) and 09-15 (four of Andrew's DMs, 18:10-18:25Z, before the 09-18 deploy); the thread's day index then
ends at 09-15; nothing has been read since the 09-18 first release; BG's warm windows on 09-24 (12:37Z, 13:06Z) fail
all four chats. BG's own hypothesis -- the watcher presents the MCP token to graph.microsoft.com -- is REFUTED by the
code: `GATEWAY = "https://mcp.opalinvest.dev/mcp/"` (`teams-watch.py:145`) and every read is a `tools/call` to it
(`:351-372`); the token's `aud` is `https://mcp.opalinvest.dev/mcp`, the right audience.

**What is NOT proven here, and the one call that proves it:** that the added fields cause the 500 rather than
merely co-occurring with it. Falsifier: from the gateway box (or a temporary tool variant), `GET
/chats/<Andrew DM>/messages?$top=1` with the OLD six-field `$select`, then with the new list minus one field at a
time. A 200 on the old list settles it; the suspects, in order, are `attachments`, `mentions`, `eventDetail`.

## 2. The identity swap, measured

`~/.claude/.credentials.json` at 13:37Z (no secret bytes read into any record; claims decoded from the JWT payload):

| record (`serverName`) | serverUrl | `sub` / `email` | state at 13:37Z | state at 13:5xZ |
|---|---|---|---|---|
| `opal-gateway-bbg` | `.../mcp/` | `<tid>/517aa5ee-...` / `op***@opalinvest.com` (Opal Bloomberg) | LIVE to 13:51:42Z | EXPIRED |
| `opal-gateway` | `.../mcp/` | `<tid>/2e21f8e5-...` / `an***@opalinvest.com` (Andrew) | EXPIRED since 09-22 | EXPIRED |
| `opalgateway` | `.../mcp` | `<tid>/2e21f8e5-...` / `an***@opalinvest.com` (Andrew) | EXPIRED since 10:19Z | **LIVE** (Andrew re-authenticated at this terminal) |

All three: `aud https://mcp.opalinvest.dev/mcp`, `iss https://mcp.opalinvest.dev`, `tver 2`, claim keys `aud,
client_id, email, exp, fid, iat, iss, jti, nbf, oid, scope, sub, tid, tver, typ`.

- `read_token()` unpinned (`teams-watch.py:249-263`): every opalinvest.dev record, live ones only, sorted by
  `expiresAt` desc, first wins -- identity-blind.
- `_read_pinned_token()` (`:207-248`): `--server` matches `serverName` (works: `opal-gateway-bbg`); `--identity`
  matches `self_id()` = the `sub` claim (`:266-283`), which since OG-a-2 (`oauth_as.py:257` "sub=<tid>/<oid>, and the
  email for display only", commit `d02e73c272` 2026-09-15, in the deployed build) is a GUID pair -- `opalbloomberg`
  never matches, `_pin_fail("no-token-for-identity")`, exit non-zero. The runbook (`bbg-teams-assist/SKILL.md:32`,
  `RELAUNCH.md:57`) prescribes exactly that pin, so it cannot be followed today; BG's 09-24 arms were unpinned
  (msg 25462). A coordinate-class break of the same shape as R-65: the pin string reads a value that moved.
- Consequence today: at ~13:5xZ the freshest live record is Andrew's. An unpinned watcher cycle on this box selects
  it, `self_name()` returns "Andrew Berman", and `is_outgoing()` drops HIS messages as the seat's own. Did it bite
  earlier today? BG's three morning arms never printed `token selected` at all, so no cycle ran with Andrew's token
  while it was live (10:04-10:19Z); the window is open from now.
- Fix shape, one line: match `--identity` against the token's `email` claim (present on all three records) as well as
  `sub`; and the seat re-arms PINNED. That closes the swap without touching the gateway.

## 3. What each defect needs, and who

| defect | owner surface | remedy | what it does NOT fix |
|---|---|---|---|
| 1 credential lifetime | watcher (`teams-watch.py`), engine owner per TEAMS_DUTY `0.5.0_AE_OpalETL~Z` (dark) | a refresh path of its own, or a token obtained the way the MCP client obtains it | 2, 3, 4 |
| 2 Graph 500 under the new projection | gateway `tools.py:719-724` (NFRA_OPLGTW lane) | run the falsifier; then either drop `$select` on the chat reader and trim fields server-side, or fall back to the six-field list on a 500 | 3, 4 |
| 3 `hostedContents` unreadable | gateway (new tool) or Andrew (re-send as text / file attachment) | a `hostedContents` GET, or a re-send | 1, 2, 4 |
| 4 identity swap | watcher pin (`self_id`) + the seat's arm command | match the pin on `email`; arm pinned | 1, 2, 3 |

Nothing here is a gate, a monitor or an alarm; no credential was touched, nothing was sent to Teams, no gateway or
watcher file was edited. The R-66b question "why does every read fail with a valid token" has a measured answer
above and one named falsifier.

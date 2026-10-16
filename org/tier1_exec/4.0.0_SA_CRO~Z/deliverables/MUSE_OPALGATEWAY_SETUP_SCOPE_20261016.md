# Scope: setting up muse (ms) on the OpalGateway MCP -- read-only research, 2026-10-16

Author: 4.0.0_SA_CRO~Z. Asked by 1.0.0_SA_CTO~Z (msg 34757, carried by 0.0.0_AB_MSTR~Z msg 34759). Input: relay msg 34756
(`org/mcp/inbox/1.0.0_SA_CTO/~Z/read/20261016T062132Z_0.0.0_AB_MSTR_Z_RELAY_from_ms__Muse___bus_7aca8520__requ.md`).
Nothing was granted, registered or changed. Every fact below was read from a file at box/sitez HEAD 52b0ff8f89 (working
tree) or from this seat's own MCP config. No live call was made against the gateway on muse's behalf.

## Answer in one paragraph

muse can connect TODAY with no gateway change, as an ordinary MCP client of `https://mcp.opalinvest.dev/mcp`, IF its
runtime can complete a browser OAuth sign-in once (claude.ai connector, Claude Code, or any local client using an http
loopback redirect). Andrew signs in as `Andrew@opalinvest.com`. muse then holds Andrew's principal: MASTER_ADMIN and
unscoped, which means EVERY gateway tool, the five send/draft tools included. The gateway cannot today give muse less
than Andrew's whole set when muse signs in as Andrew. Narrowing it (reads only, or mail and Teams only) is a gateway build.
The decision that matters is therefore not a grant. It is whether Andrew wants muse to carry his full gateway reach.

## 1. Endpoint and transport (measured)

| Item | Value | Source |
|---|---|---|
| Endpoint | `https://mcp.opalinvest.dev/mcp` | this box's user MCP config (`~/.claude.json`, server `opalgateway`, `type: http`) |
| Transport | MCP Streamable HTTP, Bearer challenge on 401 | NFRA_OPLGTW PRD C1 (`org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md:302-318`) |
| Headers | none static; the client carries the OAuth access token | same config: no `headers` key |

## 2. Credential route (measured from code)

`infra/aws/ec2/opal-gateway/app/oauth_as.py:20-40, 97-98, 511-560, 620-660`:

- The gateway is its own OAuth authorization server. Entra is the upstream identity provider. Tokens bind the Entra
  `tid`/`oid`, never the email.
- A client must register by Dynamic Client Registration (JSON). A registration accepts ONLY
  `https://claude.ai/api/mcp/auth_callback` (exact) or an `http` loopback URI on localhost/127.0.0.1/::1 (any port, RFC 8252).
  Any other redirect refuses the whole registration.
- Authorization code + PKCE S256, single-use codes (60 s), refresh tokens in rotating families stored hashed in the
  gateway access-state table. A client idle 30 days must re-register; a live refresh family keeps it.
- Consequence for muse: a hosted runtime with its own callback URL (not claude.ai's) CANNOT register. A runtime on a box
  with a browser and a loopback listener can. A headless runtime needs one human sign-in on a box that has a browser.

Tier (`app/tier.py:91-118`): a verified principal on `MASTER_ADMIN_PRINCIPALS` is MASTER_ADMIN; every other verified
principal is READ_ONLY. Andrew's principal is MASTER_ADMIN. Since the v2.3 addendum (PRD :945-975) Andrew's identity is
unscoped and `identity_tool_allowlist.txt` carries no live row.

## 3. Tool names (read from `app/destructive_ops.py:36-42, 134-160, 240-241`)

Mail, read: `list_recent_email`, `list_email_filtered`, `search_email`, `read_email`, `list_email_attachments`,
`inspect_email_attachment`.
Teams, read: `list_chats`, `read_chat_messages`, `read_chat_message_images`, `read_teams_attachment`, `list_teams`,
`list_channels`, `read_channel_messages`, `poll_addressed_teams_messages` (the new-activity poll; returns a cursor).
Identity check: `whoami`.

Reply/send (write class `write_comms`): `create_draft` (reversible), `send_email`, `reply_email`, `send_chat_message`,
`send_channel_message` (all four IRREVERSIBLE_SEND).

## 4. What a reply/send grant would take

- On Andrew's principal: nothing on the gateway. `write_comms` is `master_wildcard: True` for MASTER_ADMIN
  (`destructive_ops.py:258`). The irreversible-send guard asks the CALLER to re-call with `confirm=True`; muse can set
  that itself. It is a speed bump, not a human approval. Graph scopes already held: `Mail.Send`, `Mail.ReadWrite`,
  `Chat.ReadWrite`, `ChatMessage.Send`, `ChannelMessage.Send` (`app/config.py:64-68`).
- On any other principal: it is READ_ONLY, and a READ_ONLY token is minted without any `.Send`/`.ReadWrite` scope
  (`config.py:73-100`). It also cannot read chats (only `Chat.ReadWrite` is consented, no `Chat.Read`). Writing needs a
  roster change; chat reads need IT admin consent of `Chat.Read` on the gateway's app registration.

## 5. The three routes, compared

| Route | Build | What muse gets | Fits the ask? |
|---|---|---|---|
| A. muse signs in as Andrew (MCP OAuth) | none | every gateway tool, sends included, all data sources (Schwab, BD, Orion, ...) | yes, if muse's runtime can do the OAuth redirect; over-broad |
| B. the headless `/hx/*` REST routes | a new labelled bearer per route (Secrets Manager) | `/hx/teams`: Teams read + chat/thread send on Andrew's identity. `/hx/mail`: read-only, only senders on a table, no send or reply | partly: REST not MCP; mail is table-limited and has no reply |
| C. a muse-only narrowed client | gateway code: a client-keyed NARROWING of an unscoped identity | only the tools named for muse's OAuth client | yes, least-privilege; an NFRA_OPLGTW cell |

Why C is a build: `identity_scope.py:31-39, 152-175` client-qualified rows only ADD a tool to a SCOPED identity. Andrew's
identity is unscoped, so no row can narrow what muse gets when it signs in as him.

Route B detail: `app/teams_route.py:1-35` (bearer `gateway/teams/bearer`, `TEAMS_BEARER_LABELS`, today used by
COMM_ASSIST's assistant) and `app/mail_route.py:1-35` (`MAIL_BEARER`, `MAIL_SENDER_TABLE` / `MAIL_SENDER_DOMAIN_TABLE`,
GET only). Reusing the COMM_ASSIST bearer would make two callers indistinguishable in the audit; a new label is the floor.

## 6. Recommendation

Route A for the first live read, gated on two facts the CTO does not have yet:
1. **Andrew's own word**, because A hands muse his whole gateway reach, sends included. The relay says "on Andrew's word
   per ms" and the MSTR did not verify it (msg 34756). A recorded ANDREW_DIRECT naming muse and the full tool set closes it.
2. **muse's runtime**: claude.ai connector, Claude Code, or other. Other with a hosted callback cannot register (section 2).

If Andrew wants muse below his full set, route C is the answer, and it is a cell for NFRA_OPLGTW, not a grant.

## 7. Open items not settled here

- The dev-bid job ("the job a Kimi agent does today") overlaps COMM_ASSIST FWD-5/FWD-8 (`org/missions/D9/COMM/COMM_ASSIST/prd/COMM_ASSIST_PRD.md:75-121`):
  bids are approved from muse through the dell2 folder with a muse-origin proof. Moving that onto the gateway is a
  COMM_ASSIST scope call for the CTO. The muse/Kimi question is already held as laptop row `87a2` (record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_204xZ_MUSE_SENDER_AND_COO_LIVE_ARMS.md`).
- muse has no inbound bus queue (DEVICES.json `senders`, role sender-only). Its answer goes by the `[to-muse]` mail relay.
  This seat sends nothing to muse; replying is the CTO's call per the relay.
- Not measured: the live gateway's served tool list and tier roster (`MASTER_ADMIN_PRINCIPALS` is deploy-time env, not
  read here). The claims in sections 2-4 are from source at HEAD, not from the running host.

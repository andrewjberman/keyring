---
title: "Opal Gateway write tools -- inventory of what exists, how it is gated, and what Alyssa still does in Chrome"
date: 2026-10-08
status: "REFERENCE -- decision deferred by Andrew 2026-10-08 ('Later')"
author: "subagent of 4.0.0_SA_CRO~Z"
projects: [NFRA_OPLGTW, NFRA_MCPINDEX, NFRA_OPALAI]
people: [Andrew Berman, Alyssa Keith]
decision_record: org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261008_174xZ_GATEWAY_SCHWAB_FOUR_CALLS_ANSWERED.md
source_brief: "SharePoint site Shared, Product-Alyssa/PRD-004_gateway-data-feeds/assets/External Chrome Workflows Brief.md"
tags:
  - gateway
  - opal-gateway
  - opalgateway
  - opal_gateway
  - mcp
  - mcp-server
  - mcp.opalinvest.dev
  - m365-gateway
  - write-tools
  - write tools
  - gateway-write-tools
  - write-class
  - write_class
  - write_class_denied
  - write_comms
  - write_files
  - write_calendar
  - write_delete
  - UNCLASSIFIED
  - tool_unclassified
  - identity_scope_denied
  - read_only_denied
  - min_tier_denied
  - confirm_required
  - confirm_on_irreversible
  - blast_cap_exceeded
  - side-effects
  - side-effecting
  - mutating-tools
  - destructive_ops
  - IRREVERSIBLE_SEND
  - WRITE_REVERSIBLE
  - send_email
  - reply_email
  - create_draft
  - send_chat_message
  - send_channel_message
  - upload_text_to_site
  - save_email_attachment_to_site
  - opal_data_refresh_upload
  - opal_data_refresh_status
  - opal_asker_query
  - schwab_prepare_download
  - hx-teams
  - /hx/teams
  - teams_route
  - mail-move
  - mail move
  - mail-folder
  - mail folder create
  - mail-delete
  - soft-delete
  - deleted-items
  - mail-label
  - inbox-cleanup
  - outlook
  - outlook-web
  - Mail.ReadWrite
  - Mail.Send
  - teams-send
  - teams send
  - ChatMessage.Send
  - ChannelMessage.Send
  - Chat.ReadWrite
  - tenant-admin-consent
  - sharepoint
  - sharepoint-download
  - attachment-download
  - download-to-local
  - synced-folder
  - Files.ReadWrite.All
  - Sites.Read.All
  - ycharts
  - ycharts-portfolio
  - ycharts-report
  - schwab-advisor-center
  - chrome-automation
  - claude-in-chrome
  - browser-automation
  - browser-retirement
  - alyssa
  - alyssa-keith
  - andrew
  - entitlements
  - entitlements.txt
  - identity_scope
  - identity_tool_allowlist
  - data_entitlement
  - blast_cap
  - guard
  - tier
  - MASTER_ADMIN
  - STANDARD_EMPLOYEE
  - READ_ONLY
  - WRITE_CAPABLE_PRINCIPALS
  - graph-scopes
  - GRAPH_SCOPES
  - graph_scope_map
  - microsoft-graph
  - deferred-decision
  - later
  - call-4
  - I4
  - I3
  - C1
  - C3
  - C4
  - C5
  - C6
  - PRD-004
  - inventory
---

# Opal Gateway write tools: inventory (decision deferred)

**Find me by:** Opal Gateway write tools, opal-gateway, opalgateway, MCP at mcp.opalinvest.dev, write-class,
write_class_denied, side effects. The tools: send_email, reply_email, create_draft, send_chat_message,
send_channel_message, upload_text_to_site, save_email_attachment_to_site, opal_data_refresh_upload. What is
missing: mail move, mail folder create, soft delete to Deleted Items, mail label, Teams send as Alyssa
(ChatMessage.Send), SharePoint file download, mail attachment download to a local or synced folder, YCharts
portfolio and report runs. Also covered: Alyssa's Claude-in-Chrome workflows (C1, C3, C4, C5, C6, PRD-004),
browser retirement, entitlements, identity_scope, blast_cap and Graph scopes. Andrew deferred the decision
("Later") on 2026-10-08.

Evidence markers used below: **[M]** = measured from a file read for this brief, with path:line (paths under
`infra/aws/ec2/opal-gateway/` unless stated). **[A]** = from Alyssa's write-up (PRD-004 External Chrome Workflows
Brief, read through a scratch copy). **[I]** = inferred from [M] facts, not exercised. Nothing here was run
against the live gateway.

## 1. The decision and where it is recorded

Andrew, 2026-10-08 ~17:4xZ, answering call 4 (gateway write tools: mail move, Teams send), verbatim:

> "Later, we need to know what all they are, and it should be referenced in a brief (have a subagent write one and
> tag the shit out of it so its easy to find later."

Record: `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261008_174xZ_GATEWAY_SCHWAB_FOUR_CALLS_ANSWERED.md`
(lines 12-14 and 23). The carded item was I4 in
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPLGTW_SCHWAB_USABILITY_AND_TAX_MASTER_ASSESSMENT_20261008.md:179-180`
(I3 = read-class download to a local folder; I4 = mail move/folder and Teams send, approval per batch).

This brief is an inventory. It does not design or recommend a build.

## 2. Table A -- write and side-effecting tools the gateway already registers

Alyssa's tier is assumed to be STANDARD_EMPLOYEE (the write-capable roster). That roster is a list of principals held in
Secrets Manager `gateway/principals/rosters` (`deploy-to-ec2.sh:247-249`) and was not read. The deploy comment names
`alyssa@` as WRITE_CAPABLE (`deploy-to-ec2.sh:374-375`, `:400` `WRITE_CAPABLE_EMAILS`). She reports
`write_class_denied`, not `read_only_denied`. A READ_ONLY caller is stopped earlier, at the guard (`app/guard.py:60-64`),
so her error is consistent with STANDARD **[I]**.

| # | Tool | What it does (Graph or HTTP call) | Op class / write class | Gating layers on its path | State for Alyssa (STANDARD) |
|---|---|---|---|---|---|
| A1 | `create_draft` | POST /me/messages; creates an unsent draft. `app/tools.py:436-447` [M] | WRITE_REVERSIBLE (`app/destructive_ops.py:69-74`) / write_comms (`:168`) [M] | _run full chain (section 4); blast_cap allows reversible (`app/blast_cap.py:116-117`) [M] | **Allowed**: standard seed holds write_comms (`app/entitlements.py:35`) [M] |
| A2 | `send_email` | POST /me/sendMail, saves to Sent Items. `app/tools.py:450-467` [M] | IRREVERSIBLE_SEND (`app/destructive_ops.py:75-80`) / write_comms [M] | _run full chain; blast cap counts to+cc+bcc and external domains (`app/blast_cap.py:89-104`) [M] | **Allowed** under 25 recipients and 5 external domains; over either -> `blast_cap_exceeded`, then send with confirm=True (`app/blast_cap.py:43-45`, `:125-139`) [M] |
| A3 | `reply_email` | POST /me/messages/{id}/reply. `app/tools.py:470-477` [M] | IRREVERSIBLE_SEND (`app/destructive_ops.py:81-86`) / write_comms [M] | _run full chain; recipients are server-side so it is uncountable -> confirm always (`app/blast_cap.py:141-148`) [M] | **Allowed after confirm=True** [M] |
| A4 | `send_chat_message` | POST /chats/{id}/messages as the signed-in user, HTML body. `app/tools.py:1091-1111` [M] | IRREVERSIBLE_SEND (`app/destructive_ops.py:87-92`) / write_comms [M] | asker reply binding (`app/tools.py:1078-1088`, `:1104-1106`); _run full chain; confirm always [M] | **Allowed after confirm=True** per code [M]. Scopes Chat.ReadWrite + ChatMessage.Send (`app/graph_scope_map.py:31`), both in GRAPH_SCOPES (`app/config.py:66`) [M]. Whether Alyssa has used it was not checked |
| A5 | `send_channel_message` | POST /teams/{id}/channels/{id}/messages. `app/tools.py:1141-1154` [M] | IRREVERSIBLE_SEND (`app/destructive_ops.py:93-98`) / write_comms [M] | asker reply binding (`app/tools.py:1147-1149`); _run full chain; confirm always [M] | **Allowed after confirm=True** [M] |
| A6 | `save_email_attachment_to_site` | GET attachment $value, then an upload session into {folder}/{filename} in a SharePoint site's default library; never overwrites. `app/tools.py:353-381`, `app/graph.py:83-103` [M] | WRITE_REVERSIBLE (`app/destructive_ops.py:99-105`) / **write_files** (`:173`) [M] | _run full chain; stops at the write-class gate (`app/tools.py:157-161`) [M] | **Refused, `write_class_denied`** [M][A]. The standard seed has only write_comms (`app/entitlements.py:35`). A `standard write_files` line in ENTITLEMENTS_PATH would admit it (`app/destructive_ops.py:171-172`, `app/entitlements.py:41-60`). No entitlements file is tracked in the repo, and the deploy .env sets no ENTITLEMENTS_PATH (`deploy-to-ec2.sh:400`) [M]. The host file was not read |
| A7 | `upload_text_to_site` | Upload session for a small UTF-8 text file into a SharePoint folder; never overwrites. `app/tools.py:801-821` [M] | WRITE_REVERSIBLE (`app/destructive_ops.py:106-112`) / **write_files** (`:174`) [M] | _run full chain; stops at the write-class gate [M] | **Refused, `write_class_denied`** (same reason as A6) [I] |
| A8 | `opal_data_refresh_upload` | Finds the day's two Bloomberg PKLs on the Shared site with the caller's token, PUTs them to presigned S3 URLs, then POSTs /trigger, which fires the live yang-pipeline. `app/integrations/opal_portal/integration.py:280-401` [M] | IRREVERSIBLE_SEND, declared on the integration spec (`.../opal_portal/integration.py:123-128`); **no write class**, because the integration path never calls the write-class gate [M] | integration path (`app/integrations/base.py:116-180`): data_entitlement, identity_scope, min_tier=standard (`.../opal_portal/integration.py:104-105`). Confirm is in the tool itself (`:297-301`) [M] | **Allowed** (dry_run, or confirm=True). Enabled in the deployed list (`deploy-to-ec2.sh:400` ENABLED_INTEGRATIONS) [M]. This is her daily /bbg-send path |

Rows in Table A: 8.

### Borderline and non-tool side effects (not counted in Table A)

| Item | What it writes | Gating | Evidence |
|---|---|---|---|
| `schwab_prepare_download` | Mints a 5-minute, single-use, identity-bound ticket record in the gateway's own store. No source data changes | Classed SAFE. Hidden from, and denied to, any principal with no Schwab grant | `app/integrations/schwab/integration.py:104-108`; `app/data_entitlement.py:382-384` [M] |
| `POST /hx/teams/chats/{id}/messages` and channel-thread replies | Sends Teams messages as the fixed MS_INGEST_IDENTITY (andrew@) | Static bearer TEAMS_BEARER and a Graph path allowlist. It does **not** go through `_run`, so the write-class and blast-cap gates do not apply. "Sends are not approved here", so approval lives in the caller | `app/teams_route.py:14-15`, `:28-29`, `:79-82`, `:109`; `deploy-to-ec2.sh:400` MS_INGEST_IDENTITY [M] |
| `POST /schwab/download/exchange` | Consumes a download ticket and streams a CSV | Browser session cookie and ticket checks | `app/download_routes.py:18-25` [M] |
| Admin routes `/grants/.../narrow`, `/grants/.../widen`, `/tenants/{tid}`, `/refusals/approve` | Operator policy writes | Not read for this brief | `app/admin_api.py:49-50`, `app/admin_tenants.py:70`, `app/admin_refusals.py:166` [M, existence only] |

## 3. Table B -- write capabilities Alyssa needs that the gateway does not have

"Graph permission" is filled in only where the code or her text states it. Otherwise it is marked unknown.

| # | Capability | Her workflow | What it would need | Nearest existing gateway tool | Risk |
|---|---|---|---|---|---|
| B1 | Move a mail message to a folder (bulk, by sender domain) | C4 [A] | A new native tool. Graph permission **unknown** from the code: the consented mail-write scope is Mail.ReadWrite (`app/config.py:64`), but no code states that it covers a move. Needs a destructive_ops tag and a write class (none fits today: write_comms is send/draft, `app/destructive_ops.py:185`). Needs a data_entitlement classification, or the tool is `tool_unclassified` for everyone (`app/data_entitlement.py:374-377`). She asks for a dry-run listing and approval per batch [A] | `list_email_filtered` / `search_email` (read only, to select the set) | Side effect on her mailbox. Reversible by moving back [A]. Bulk blast is not countable by the current blast_cap (it counts only recipients, `app/blast_cap.py:102-104`) [M] |
| B2 | Create a mail folder | C4 [A] | A new tool. Graph permission **unknown** (Mail.ReadWrite is consented, `app/config.py:64`; sufficiency not verified). "No tool can create a mail folder" [A] | none | Low; additive |
| B3 | Soft delete to Deleted Items | C4 [A] | A new tool. Graph permission **unknown**. Class undecided: `write_delete` exists only as a FORWARD class and is not master-wildcard, so even Andrew would need an explicit grant (`app/destructive_ops.py:181-188`, `app/entitlements.py:73-76`). Whether a recoverable delete belongs in write_delete is not decided anywhere read | none | Recoverable delete [A]. The CTO note warns not to fold delete into write_files (`app/destructive_ops.py:181-183`) [M] |
| B4 | Label (categorize) mail | C4 [A]: "move/label/delete tools return 'This tool is not available'" | A new tool. Graph permission **unknown**. "Label" is not defined further in her text | none | Low |
| B5 | Send a Teams chat message as Alyssa | C5 [A] | Her text asks for Graph `ChatMessage.Send` (delegated) behind tenant-admin consent, with approval per send [A]. **The code already carries it:** `send_chat_message` (`app/tools.py:1091-1111`), with ChatMessage.Send in GRAPH_SCOPES (`app/config.py:66`) and write_comms seeded for standard (`app/entitlements.py:35`) [M]. Whether her own sign-in consented these scopes, and whether "the connector" in her text means this gateway or another M365 connector, is **not verified** | `send_chat_message` (and `send_channel_message`) | Irreversible send as her. The 9/22 Chrome attempt silently failed [A] |
| B6 | Download a SharePoint file (binary) to a local or synced folder | C6 [A] | A new tool, or a pattern. The gateway runs on EC2 and cannot write to her disk **[I]**. Graph permission **unknown** for a binary download. Her text frames it as read class [A] | `read_site_file` / `read_document` (text extraction, max_chars; `app/tools.py:698-712`, `:911-937`); the Schwab ticketed browser download (`schwab_prepare_download` + `/schwab/download`, `app/download_routes.py:1-25`) is the one existing "file to the user's browser" pattern | Read class. Covers the Opal and 49 Financial SharePoint [A] |
| B7 | Save a mail attachment to a local or synced folder | C6; Schwab Data Needs section 6 [A] | Today's tool, `save_email_attachment_to_site`, is refused (`write_class_denied`). Admitting it for standard is one entitlement line, `standard write_files` (`app/destructive_ops.py:171-172`). That lands the file in a SharePoint library, not on disk; whether the library syncs to her machine is not verified. She also names a Power Automate flow as an alternative [A]. New Outlook has no COM [A] | `save_email_attachment_to_site` (A6); `inspect_email_attachment` and `validate_ssavail_attachment` (read only) | Additive file write, never overwrites (`app/tools.py:356-361`) [M] |
| B8 | Create client portfolios in the shared YCharts account | C1 [A] | A mutating YCharts integration. Today the YCharts spec is `read_only=True` (`app/integrations/ycharts/integration.py:39`). A mutating spec must declare min_tier above read_only (`app/integrations/base.py:205-207`). Vendor surface: YCharts shared session (`app/config.py:291-292`). AWS WAF token rotates about every minute, and a fresh login evicts the human seat [A]. Her options: a server-side runner owned by Andrew, or retire YCharts for Overview via the Opal report engine [A] | the six read-only `ycharts_*` tools | Side effects in a shared vendor account. P0 [A]. Vendor egress needs Andrew's per-use word (CLAUDE.md, Agent Autonomy) |
| B9 | Run YCharts Overview / Comparison / Multi-Comp reports and download the PDF | C1 [A] | As B8: a new vendor write/run surface. Report endpoints **unknown** | `ycharts_snapshot_metrics`, `ycharts_time_series` (she reports 403/404 on these, assessment doc `:178`) | About 30 households a month [A] |

Rows in Table B: 9.

Related gaps in her text that are reads, not writes (listed so they are not lost):

- C3, Schwab Advisor Center: statements and CSV exports. Her session can trade, move money and change settings
  [A]. The nearest gateway surface is the `schwab_*` tools (`app/integrations/schwab/integration.py:91-109`).
- Microsoft Forms responses (YCharts Request Form) are not readable through Graph [A].

## 4. How a write is gated, in order

Native tools (`app/tools.py`):

1. **Discovery filter.** `list_tools` hides every tool `data_entitlement.decide` denies (`app/tools.py:65-70`,
   `app/data_entitlement.py:428-438`).
2. **Dispatch filter.** `call_tool` returns the same denial with isError=True (`app/tools.py:72-91`).
3. **Identity present.** No email -> `identity_required` (`app/tools.py:127-131`).
4. **Tier resolved once**, from the principal tid/oid: MASTER_ADMIN, STANDARD_EMPLOYEE or READ_ONLY. Fail-closed
   under an unverified provider (`app/tier.py:84-118`; rosters `app/config.py:306-315`).
5. **Policy profile** (`data_entitlement.tool_denial`). A tool not classified in `NATIVE_TOOLS` /
   `INTEGRATION_TOOLS` / `INDEX_TOOLS` -> `tool_unclassified` for everyone. A principal with any Schwab profile is
   restricted to Schwab tools only (`app/tools.py:136-139`, `app/data_entitlement.py:95-126`, `:371-385`).
6. **Per-identity allowlist.** Only scoped identities are affected. Today that is the Bloomberg concierge account only;
   Alyssa and Andrew are unscoped (`app/tools.py:143-147`, `app/identity_scope.py:54-77`, `:158-188`;
   `identity_tool_allowlist.txt:19`, `:25`).
7. **Guard G2.** READ_ONLY on a mutating or unknown tool -> `read_only_denied` (`app/tools.py:148-152`,
   `app/guard.py:31-69`; classes `app/destructive_ops.py:34-147`).
8. **Write-class entitlement.** The tool's class must be granted to the tier. A mutating tool with no class ->
   UNCLASSIFIED -> denied to all. MASTER gets a wildcard except for write_delete. Seed: standard = {write_comms}
   (`app/tools.py:157-161`, `app/destructive_ops.py:167-201`, `app/entitlements.py:34-77`).
9. **Blast cap and confirm (G1/G3).** Under cap -> allow. Over cap, or an uncountable irreversible send ->
   `confirm_required`; the caller re-calls with confirm=True. Seed caps: standard 25 recipients and 5 external
   domains; master absolute 200 and 100 (`app/tools.py:163-166`, `app/blast_cap.py:43-50`, `:107-148`).
10. **Token.** STANDARD and MASTER get the full GRAPH_SCOPES; READ_ONLY gets a read-only scope set
    (`app/token_broker.py:141-147`, `app/config.py:61-69`, `:98-103`). A scoped identity's consent is narrowed to
    its tools (`app/graph_scope_map.py:17-53`).
11. **Microsoft Graph** enforces the delegated user's own permissions (`app/tools.py:1-3`).
12. **Audit** of every outcome (`audit.log_call` throughout `_run`).

Send tools add the asker reply binding (`app/tools.py:1078-1088`).

Integration tools (`app/integrations/base.py:116-180`) run steps 5, 6 and a `min_tier` floor
(`app/guard.py:81-93`). They do **not** run steps 8 or 9. A mutating integration carries its own confirm
(`opal_data_refresh_upload`, `.../opal_portal/integration.py:297-301`).

A new native write tool must land in four places, or a layer denies it: the `@mcp.tool` itself, the data_entitlement
classification, the destructive_ops tag plus TOOL_WRITE_CLASS, and, if its class is not write_comms, an entitlement
line for standard. If it needs a scope outside GRAPH_SCOPES, that is a consent change as well.

## 5. The two safety positions

- **Alyssa [A]:** the Chrome extension runs with her full signed-in sessions, so nothing it touches is read-only by
  construction. Her standing rules: no trades, no money movement, no settings or entitlement changes, no credential,
  cookie or token reads. Downloads and any send, move or delete need her approval per batch.
- **Gateway [M]:** fail-closed classification at three layers (data_entitlement, destructive_ops, write class).
  Blast caps on countable sends, and a confirm step on every irreversible send for all tiers, Andrew included
  (`app/blast_cap.py:16-18`). Writes are opt-in per principal (`app/tier.py:113-118`). MASTER_ADMIN is one principal
  (`deploy-to-ec2.sh:248`), described as andrew@ (`app/tier.py:29`). write_delete needs an explicit grant even for
  master (`app/destructive_ops.py:188`). The gateway has no "approval per batch" mechanism; the confirm step is per
  call **[I]**.

## 6. What this brief does not decide

- Whether any Table B capability is built, for whom, or in what order.
- Which write class a move, folder create, label or soft delete belongs to, or whether a new class is needed.
- Whether `standard write_files` is granted. That would admit A6 and A7 for Alyssa.
- Whether YCharts is automated server-side or retired for Overview reports.
- Anything about Schwab data scope (calls 1 to 3 of the same record).

## 7. What was not verified

- Alyssa's actual tier. The roster secret was not read. STANDARD is inferred from her `write_class_denied` error.
- Whether an `entitlements.txt` exists on the host. None is tracked in the repo; the deploy .env sets no
  ENTITLEMENTS_PATH, so the default `./entitlements.txt` applies (`app/config.py:370`).
- That deployed code equals CLOUD HEAD. No artifact or EC2 manifest was compared.
- Whether "This tool is not available" comes from this gateway. The string does not appear in `app/*.py` as an error
  for a missing tool. It may come from the client or another connector.
- Which Graph permissions mail move, folder create, delete, label and binary download need. The code does not say.
- Whether Alyssa has signed in and consented the full scope set, and whether her `send_chat_message` calls succeed.
- No tool was called and no test was run.

## 8. Findings from the code read

- `opal_asker_query` (`app/tools.py:1207-1217`) appears in no destructive_ops set: not SAFE_TOOLS
  (`app/destructive_ops.py:34-64`), not DESTRUCTIVE_OPS, not TOOL_WRITE_CLASS. It is native, so no integration spec
  classifies it. Reading the code, `_run` would give it write class UNCLASSIFIED and return `write_class_denied` to
  every tier (`app/destructive_ops.py:192-201`, `app/entitlements.py:68-69`). Its tests call
  `asker_scope.handle_asker_query` directly and never go through `_run` (`tests/test_asker_scope.py:119`, `:176`).
  This is a code read and was not exercised.
- The `app/destructive_ops.py` docstring (lines 8-12) and comment (line 66) say there are 5 mutating tools. The
  registry holds 7 (`:68-113`), and one more mutating tool lives on the integration path (A8).
- Giving Alyssa any Schwab data profile would restrict her to Schwab tools only. Her mail and Teams tools, writes
  included, would then be denied (`app/data_entitlement.py:31-33`, `:378-381`).
- `/hx/teams` sends as andrew@ outside the write-class and blast gates (section 2, borderline table).

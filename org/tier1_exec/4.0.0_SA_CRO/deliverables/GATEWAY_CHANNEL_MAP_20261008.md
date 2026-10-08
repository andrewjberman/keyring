# Opal Gateway channel map -- channels, tools, reach, sensitivity (proposal), the existing index, entitlements

Fork of 4.0.0_SA_CRO, 2026-10-08 ~19:4xZ, laptop CLOUD tree. READ-ONLY: repo reads only. No gateway tool was called
for this file, and no vendor API. [READ] = read in a file. [INFER] = reasoning. Input to the L1 brief for NFRA_MCPORTAL's
control plane (Andrew point 4, record org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_184xZ_FIVE_POINTS_...md).
App root below: infra/aws/ec2/opal-gateway/app/ (written `app/`).

---

## 0. Definition and denominators

**Channel** = the unit the gateway itself organises tools by:
- (a) each **integration** (`app/integrations/<id>/`, one `IntegrationSpec` with display_name, auth_kind, read_only,
  min_tier, hosts and tool_classifications) [READ `app/integrations/registry.py:1-60`];
- (b) the **native Microsoft 365 tools** in `app/tools.py`, split here by Graph resource family (mail, calendar and
  meetings, files and SharePoint, Teams, identity, asker read). The code does not split them [INFER: grouping is this file's].
- **Not MCP tools, but channels too:** the gateway's **REST route families** (`app/server.py:1048-1131`). They are listed
  in section 1c.

**Live set** [READ `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh:400`]:
`ENABLED_INTEGRATIONS="ycharts opal_portal globgrph opal_discover portal_index schwab blackdiamond"`, so 7 integrations
are enabled at deploy. Several module headers still say DORMANT (e.g. `registry.py:47`, `blackdiamond`), but the deploy
template renders all seven, so those headers are stale. [INFER, consistent with this session's own tool list, which shows
blackdiamond_, graph_, mdpf_, etfs_, gateway_query_catalog, opal_discover/describe, ycharts_ and opal_data_refresh_ tools,
and no schwab_ tool.]

| Denominator | Count | Source |
|---|---|---|
| MCP tools total | **66** = 42 native + 24 integration | `grep -c '^@mcp.tool' app/tools.py` = 42 [READ]; integration defs per channel below [READ]; equals the classified set in `app/data_entitlement.py:95-127` (NATIVE 42 + INTEGRATION 10 + INDEX 9 + SCHWAB 5 = 66) [READ] |
| MCP channels | **13** = 6 native families + 7 integrations | this file's grouping |
| Write (mutating) tools | **8** | 7 native (`app/destructive_ops.py:66-118`) + `opal_data_refresh_upload` (MUTATING, `opal_portal/integration.py:28,105`) [READ] |
| Read tools | **58** | 66 - 8 |
| Tools whose answers can carry client content (PII or client financials) | **47** [INFER] | M365 content tools 41 (every native tool except whoami) + opal_asker_query 1 + Schwab 5 = 47; plus 3 firm-aggregate tools (mdpf_*) and blackdiamond_list_fees (raw account ids + names) = **51 with firm or client-financial data** |
| REST route families (non-MCP) | **14** | section 1c |

---

## 1a. Native Microsoft 365 channels (`app/tools.py`, delegated Graph token per user)

Every native tool runs as the connected user with that user's own delegated token; Microsoft enforces per-user reach
(`app/tools.py:1-3`) [READ]. The requested delegated scopes (the outer envelope) are `User.Read Mail.Read Mail.Send
Mail.ReadWrite Calendars.ReadWrite Files.ReadWrite.All Sites.Read.All Chat.ReadWrite ChatMessage.Send Team.ReadBasic.All
Channel.ReadBasic.All ChannelMessage.Read.All ChannelMessage.Send OnlineMeetings.ReadWrite OnlineMeetingTranscript.Read.All
Presence.Read.All Notes.ReadWrite.All` (`app/config.py:59-70`) [READ]. A per-tier reduced token exists as SCTY_PREMCP
Layer 2 (`config.py:73-76`) [READ header only].

| Channel | Tools (n) | Reaches | Write tools | Proposed rating | Why |
|---|---|---|---|---|---|
| M1 Identity | whoami (1) | Graph /me | -- | R1 | the caller's own identity |
| M2 Mail | list_recent_email, list_email_filtered, search_email, read_email, list_email_attachments, inspect_email_attachment, validate_ssavail_attachment, save_email_attachment_to_site, create_draft, send_email, reply_email (11) | the user's mailbox (Mail.*); attachments; save puts a file into a SharePoint site | create_draft (WRITE_REVERSIBLE), save_email_attachment_to_site (WRITE_REVERSIBLE), send_email, reply_email (IRREVERSIBLE_SEND) | **R4** | sends on the user's behalf (irreversible); reads client correspondence |
| M3 Calendar and meetings | list_calendar, find_online_meeting, list_meeting_transcripts, read_meeting_transcript (4) | Calendars, OnlineMeetings, transcripts; transcript reads are allowlisted per meeting (`TRANSCRIPT_MEETING_ALLOWLIST` is EMPTY at deploy, so every meeting is refused, `deploy-to-ec2.sh:395`) [READ] | -- | R3 | meeting transcripts can carry client discussion |
| M4 Files and SharePoint | list_onedrive, search_files, read_file, find_sharepoint_site, list_site_files, read_site_file, profile_site_file, read_site_workbook, read_workbook, search_site_files, get_item, get_site_item, list_site_drives, read_document, upload_text_to_site (15) | OneDrive and SharePoint (Files.ReadWrite.All, Sites.Read.All) | upload_text_to_site (WRITE_REVERSIBLE) | **R3** (R4 for upload) | SharePoint holds client statements, workbooks, tax files [INFER] |
| M5 Teams | list_chats, read_chat_messages, read_chat_message_images, read_teams_attachment, poll_addressed_teams_messages, list_teams, list_channels, read_channel_messages, send_chat_message, send_channel_message (10) | Chat, channels | send_chat_message, send_channel_message (IRREVERSIBLE_SEND) | **R4** | sends as the user; reads internal and partner chats |
| M6 Asker-scoped portal read | opal_asker_query (1) | portal artifacts through the catalog gate, scoped to the ASKER's own grant intersected with the caller's (`app/asker_scope.py:1-40`) [READ] | -- | R2-R3 | depends on the asker's grant |

The concierge identity `opalbloomberg@opalinvest.com` is scoped to an ALLOWLIST of 12 tools (whoami, the Teams set and
opal_asker_query; no email, upload or ycharts) (`app/identity_scope.py:55-75`) [READ].

## 1b. Integration channels (`app/integrations/<id>/integration.py`)

| Channel | Tools (n) | Reaches | Auth / min tier | Fields exposed (where stated) | Write? | Proposed rating | Why |
|---|---|---|---|---|---|---|---|
| I1 YCharts | ycharts_freshness, ycharts_snapshot_metrics, ycharts_time_series, ycharts_fund_series, ycharts_risk_return_scatter, ycharts_search (6) | YCharts vendor API (SHARED_SECRET) | `min_tier="standard"`; master admin + write-capable only (`ycharts/integration.py:36-44`) [READ] | vendor metrics by symbol | no | **R0** (licensed) | public market data; the licence limits redistribution |
| I2 Opal portal data refresh | opal_data_refresh_upload, opal_data_refresh_status (2) | SharePoint output folder -> portal /data-refresh -> yang pipeline (SHARED_SECRET) | `min_tier="standard"`, confirm-gated (`opal_portal/integration.py:28,101-105`) [READ] | file names and sizes, upload id, execution id | **upload: MUTATING** | **R4** | starts a production pipeline run |
| I3 Estate graph | graph_cypher, graph_status (2) | served Kuzu projection, in-VPC (AuthKind.NONE) | `min_tier="read_only"` (`globgrph/integration.py:50-57`) [READ] | any CloudNode/CloudEdge field; includes 5,878 SharePoint file names (ms layer) [READ from parent research] | no | **R1-R2** | estate metadata; SharePoint names can reveal client names [INFER] |
| I4 Schwab | schwab_get_access, schwab_list_files, schwab_describe_dataset, schwab_query, schwab_prepare_download (5) | `opal-data-assets` Schwab silver, assumed read roles (ASSUMED_ROLE) | `min_tier="read_only"` PLUS an active per-principal data_entitlement (masters, datasets, accounts, dates, columns, operations) (`schwab/integration.py:70-90`; `app/data_entitlement.py:1-25`) [READ] | dim_position 11 (account_ref, cusip, ticker, quantities, market_value, closing_price); dim_balance 9 (account_ref, market values, cash, bank sweep); dim_asset 9 (cusip, ticker, descriptions, price, maturity, product codes); dim_transaction 15 (account_ref, dates, codes, cusip, quantity, price, gross and net amount) (`schwab/datasets.json`) [READ] | no (download = 5-minute single-use ticket) | **R3** | client positions, balances and transactions. Accounts are a keyed HMAC alias (`acr_<v>_...`, `app/account_ref.py:1-30`), so the client is pseudonymised but the financials are real |
| I5 Portal index | mdpf_get_aum_metrics, mdpf_get_account_distribution, mdpf_get_aggregate_aua, mdpf_get_model_benchmarks, etfs_get_positioning, gateway_query_catalog (6) | `opal-data-portal-v2` precomputed objects through DATA_CATALOG rows (AuthKind.NONE, gateway role) | `min_tier="read_only"` (`portal_index/integration.py:106-114`) [READ] | mdpf: firm-scoped AUM/AUA/account distribution; benchmarks and ETF positioning: opal-internal-only (`DATA_CATALOG.yaml` portal_datasets) [READ] | no | **R2** | firm-confidential aggregates; per-firm visibility rule in the catalog |
| I6 Opal discover | opal_discover, opal_describe (2) | the catalog (AuthKind.NONE) | `min_tier="read_only"` (`opal_discover/integration.py:78-87`) [READ] | catalog rows: dataset, meaning, freshness field, never-sum rules, read tool | no | **R1** | metadata about data |
| I7 Black Diamond | blackdiamond_list_fees (1) | `opal-data-bd` silver/fees (49financial only), gateway-blackdiamond-read-role (ASSUMED_ROLE) | `min_tier="read_only"` (`blackdiamond/integration.py:117-123`) [READ] | transaction_id, trade_date, account_id, **account_name**, relationship_id, asset_name, cusip, transaction_fee, account_fee, income, fee_schedule_type, fee_schedule_rate_type; rows capped at 200; account_id fenced to `z08` (`:83-85`) [READ] | no | **R3** | raw client account ids and names with fees |

## 1c. REST route families (not MCP tools; `app/server.py:1048-1131`) [READ]

| Route family | Purpose | Gate | Proposed rating |
|---|---|---|---|
| /health, /.well-known/*, /jwks, /register, /authorize, /token, /login, /callback, browser OIDC | OAuth server and liveness; `/health` returns only `{"ok": true}` (`server.py:312`) | public / OAuth | R1 |
| /mcp | the MCP channels above | gateway bearer (GuardMiddleware) | per channel |
| /otp/token, /otp/fetch, /otp/health | Black Diamond OTP code from Andrew's mailbox for the auto-login box | static bearer or `gw:otp` capability token | **R4** (credential material) |
| /ms/sites, /ms/site_children, /ms/onedrive_children, /ms/search, /ms/token, /ms/health | SharePoint listing for the estate graph's ms layer | MS_INGEST bearer | R2 |
| mail_route (list, message, attachments, attachment) | bearer REST mail reads (OG-hl-1) | bearer + mail sender table | R3 |
| teams_route (me, chats, chat messages, replies) | bearer REST Teams, including reply sends | bearer | R4 |
| transcript_route (list, one) | meeting transcripts | bearer + meeting allowlist | R3 |
| /teams/poll, /query/v0 | concierge monitor poll; partner query v0 | bearer; GUARDED_ROUTES deny restricted profiles (`data_entitlement.py:130`) | R3 / R2 |
| /graph/cypher, /graph/health | the estate graph read token path | GRAPH_READ_BEARER | R1-R2 |
| /schwab/download, /schwab/download/exchange | single-use filtered CSV download | ticket | R3 |
| taxsma workbook route | the tax SMA workbook | its own gate (`taxsma_workbook.py`) | R3 [INFER] |
| /sprint/*, /rivalfunds/*, /yearinreview/* | HTML views | per-view email allowlists (andrew@ only for sprint and yearinreview at deploy) | R1-R2 |
| /api/admin/* + /assets + / | MCPORTAL dashboard and admin API | owner_gate (Andrew only) | R4 (it changes grants) |

## 2. Proposed sensitivity scale (a PROPOSAL; no policy attached)

| Rating | Meaning | Channels (MCP) |
|---|---|---|
| R0 | public or vendor market data | I1 YCharts |
| R1 | internal operational metadata | M1, I6, I3 (estate graph, lower half) |
| R2 | firm-confidential aggregates | I5 portal index, M6 (narrow grants), I3 (SharePoint names) |
| R3 | client PII or client financial rows | M3, M4, I4 Schwab, I7 Black Diamond, M6 (wide grants) |
| R4 | acts on a person's or the firm's behalf (send, upload, trigger) | M2 Mail, M5 Teams, I2 data refresh, M4 upload_text_to_site |

What drove each: whether the tool can **act** (R4 outranks any read); then whether rows can identify a client or carry
a client's money (R3); then whether figures are firm-level (R2). **Count by rating, MCP channels:** R0 1, R1 2-3, R2 1-2,
R3 4, R4 4 (I3 and M6 straddle) [INFER].

## 3. The index substrate that already exists (do not re-buy)

| Substrate | What a portal page could read from it | Where |
|---|---|---|
| IntegrationSpec per integration | display_name, description, auth_kind, read_only, min_tier, hosts, tool_prefix, tool_classifications | `app/integrations/*/integration.py`; validated by `integrations/base.py` |
| Tool class table | every one of the 66 tools mapped to `legacy` or `schwab`; an unclassified tool is denied to all | `app/data_entitlement.py:95-127, :371-388` |
| destructive_ops registry | per write tool: class (SAFE / WRITE_REVERSIBLE / IRREVERSIBLE_SEND), reversible, native_undo, blast_dimensions; fail-closed default | `app/destructive_ops.py:66-118` |
| Per-principal tool list | MCP `list_tools` already filtered per principal (`visible_tools`) | `app/tools.py:55-70` |
| The runtime catalog | 16 catalog channels (benchmarks_and_models, capital_markets, correlations_factors, etfs_positioning, macro_rates, market_overview, market_regime_trending, mdpf_model_portfolios, news, peers, pipeline_freshness, positioning_holdings, sentiment_news_mood, valuation, sharepoint_documents, bloomberg_standing_read); 5 silver datasets; 5 portal datasets; never_serve 10; held_at_andrew 2; refused_units 5; per-row firm and verdict_class | `app/refs/DATA_CATALOG.yaml` (v0.4) |
| opal_discover / opal_describe / gateway_query_catalog | the catalog as tools (already MCP) | I6, I5 |
| Audit log | one JSON line per tool call: who, tool, redacted args, when, outcome (denials included); local JSONL plus the S3 lake `opal-mcp-audit`, date-partitioned and Athena-queryable | `app/audit.py:1-20`; `deploy-to-ec2.sh:400` (`AUDIT_S3_BUCKET=opal-mcp-audit`) |
| Grant changes | `/api/admin/changes`: the grant writer's own table across all principals (MCPORTAL_CHANGES_TABLE), or operator_audit per principal | `app/admin_grants.py:1-25` |
| Schwab per-dataset schema | fields, grain and additive rules per dataset | `app/integrations/schwab/datasets.json` |
| /health | liveness only; no tool or channel inventory | `server.py:312` |

## 4. Entitlements, tiers and user removal today

| Control | Where it lives today | State |
|---|---|---|
| Tier (READ_ONLY / STANDARD / MASTER_ADMIN) | env lists on the box: `MASTER_ADMIN_EMAILS=andrew@`, `WRITE_CAPABLE_EMAILS=alyssa@, opalbloomberg@` (`deploy-to-ec2.sh:400`); elevated tiers only under a signature-verified provider (alb_oidc) (`app/tier.py:1-60`) | file/env, redeploy to change |
| Per-identity tool allowlist | `identity_scope.py` map + hot-reloaded `IDENTITY_TOOL_ALLOWLIST_PATH` file (`config.py:374`) | file |
| Data entitlement (Schwab and portal grants) | DynamoDB `gateway-access-state-table`, POLICY#<tid>#<oid>: principal_profile + versioned data_entitlement; strong reads, conditional writes (`app/access_state.py`, `app/data_entitlement.py`) | table, takes effect on the next call |
| Grant writes | separate grant-writer Lambda `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/` (PRD C4: verifies the ALB-signed owner header itself, one invoke grant) | "grant writer live, deployed bytes = CLOUD HEAD" (project.json blocking text) [READ] |
| Kill switch | file `KILL_SWITCH` (`config.py:381`, `blocklist.py`) -- presence denies ALL | file on the box |
| Person block | `blocklist.txt` (`config.py:355`), hot-reloaded | file on the box |
| Token revocation | `revoked_jtis.txt`, `user_revoke_cutoffs.txt` (`config.py:361-362`, `revocation.py`); blocklisted users are revoked too | file on the box |
| opalinvest.dev portal users | `opal-users-v2` and `opal-partner-<firmId>` tables plus the auth function's admin routes; PRD C7 adds a `disabled` state (not built) | PRD C7 |

**MCPORTAL PRD status** [READ `org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md` and `project.json`]:
- **FWD-1** (narrow or widen one colleague's grant from the dashboard; the next call reflects it):
  - built: round 3 EXECUTING with 3 of 5 orders complete (MP-b-3, MP-f-1, MP-a-2);
  - not yet graded: its live proof MP-c-1 (G-CLOSE) waits on Alyssa's sitting;
  - the project is **PARKED since 2026-10-01**, with no seat live.
- **FWD-6** (add, edit, disable and remove a user at both levels from one screen): not built. It needs C7 (the auth
  function's `disabled` state) and surface S10.
- **FWD-10** (who called which tool and what was refused; stop one person or the whole server on the next call):
  not built (S12).
  - PRD C6 keeps the kill switch, blocklist and revoked tokens as FILES.
  - Moving tiers and tool lists into the grant table is ENRICHMENT, gated on **G-OPLGTW**, Andrew's word on amending
    NFRA_OPLGTW's contract (PRD :230-241).
- **FWD-9** (every data property beside the tools that answer it; uncleared tools stand out) is the closest PRD
  outcome to Andrew's "index per channel". The channel risk rating is NOT in the PRD.

## 5. Findings for the brief

1. **The map largely exists as code, not as a page.** Specs, the class table, the destructive_ops registry, the
   catalog and the audit lake together answer "what channels, what tools, what fields, who called". The gap is one
   rendered view plus a sensitivity column.
2. **66 MCP tools in 13 channels, 8 of them write tools.** 4 channels act on someone's behalf (mail, Teams, upload,
   pipeline trigger). The REST routes add 14 more families (OTP, mail, Teams sends) that an MCP-only map would miss.
3. **No channel risk rating exists anywhere.** The nearest are destructive_ops' write classes (per tool) and the
   catalog's per-row firm and verdict_class. A rating column is new.
4. **Field reach is stated only for Schwab (44 fields in 4 datasets), Black Diamond (12 columns) and the catalog's
   portal rows.** M365 tools return whatever the user's mailbox, files and chats hold, so their "fields" are
   unbounded by design.
5. **User removal today is three files on one box** (kill switch, blocklist, revocation lists) plus an env tier list.
   The portal's FWD-6 and FWD-10, and the move into the table (C6, G-OPLGTW), are unbuilt. MCPORTAL is parked.

## Not read

- The live box: its .env, the files themselves (blocklist, KILL_SWITCH, allowlist), and live `list_tools` for each
  tier. The enabled set is read from the deploy template only.
- `integrations/base.py` validator; `tier.py` beyond its header; `guard.py`, `blast_cap.py`, `entitlements.py` bodies;
  `query_v0.py`, `graphql_plumbing/`, `entity_resolution/`, `org/`.
- Each catalog channel's artifact rows in detail (only per-channel counts, firms and verdicts).
- The grant-writer Lambda's code, and whether `MCPORTAL_CHANGES_TABLE` is set live.
- The auth function and the `opal-users-v2` / `opal-partner-*` tables.
- `opal_ai` (the PRD says the gateway app is moving there).

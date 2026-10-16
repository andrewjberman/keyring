# M365 workflow spine -- what the gateway and Andrew's Entra role can reach

**Seat:** `4.0.0_SA_CRO~XXX` (dell1) | **Written:** 2026-10-15 | **archetype:** EXPLORE
**Status:** research only. Nothing was registered, consented or pulled. No live Entra write.

## 0. The request, verbatim (Andrew-direct, Claude Code terminal, 2026-10-15 ~23:5xZ)

> I want you to go through the opalgateway and as we're using the andrew@opalinvest.com entra ID, I should be a
> Cloud Application Administrator. I want to know what the scope of powers are afforded to the application.
> Specifically, I want to explore if it is possible to create a timeline "spine" of all actions all employees take
> on Microsoft, with the guiding purpose being to reverse engineer every workflow. The idea is that we want to look
> for common tasks that happen every single day, the sequencing of those tasks, the content of those tasks, how they
> depend upon one another, where there are opportunities for waste reduction through AI Implementation. I am
> wondering if we have access at the Application level sitting above the entra ID if needed, or if that can be
> arranged through the existing credential/admin.

Claim tags: **measured** (read this session), **held** (read from a repo record, not re-read live),
**inferred** (derived from a documented rule, not exercised), **absent**.

## 1. What the gateway can do today: only the signed-in user's own data

- The gateway's Graph app ("M365-MCP-Graph") holds **delegated permissions only, never application permissions**
  (`infra/aws/ec2/opal-gateway/IT_REQUEST.md:3`, held). Its 17 scopes (Mail, Calendar, Files, Sites.Read.All, Teams
  chat/channel/meetings/transcripts, Presence, OneNote) act **as the signed-in person**, inside what that person can
  already see.
- `whoami` returns `Andrew@opalinvest.com` (measured). So the gateway sees Andrew's mail, chats, files and the
  channels he belongs to. **It cannot read any other employee's mailbox, chats or OneDrive**, whatever role Andrew
  holds. A delegated token never goes beyond the user's own access, so the role does not widen it.
- **Conclusion:** the gateway as built cannot produce an all-employee spine. That needs **app-only (application)
  permissions**, which run as the application itself with no user signed in. This is the "application level sitting
  above the Entra ID" in the request.

## 2. What Cloud Application Administrator does and does not allow

- Andrew's active tenant-wide Cloud Application Administrator assignment was **verified 2026-09-14** (`IT_REQUEST.md:75`, held).
  It was not re-read today: dell1 has no `az` CLI (measured). If it is a PIM-eligible assignment, it must be activated first.
- **Can:** create and manage app registrations and enterprise apps, add secrets and certificates, and grant tenant-wide
  admin consent for **delegated permissions on any API** and **application permissions on any API except Microsoft
  Graph** ([Microsoft Learn: grant admin consent](https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/grant-admin-consent)).
- **Cannot:** grant consent for **Microsoft Graph application permissions** (`Mail.Read`, `Chat.Read.All`,
  `ChannelMessage.Read.All`, `Files.Read.All`, `Calendars.Read`, `AuditLog.Read.All`, ...). That needs a
  **Privileged Role Administrator** or **Global Administrator** (or a custom role with the grant permission).
  The role also does not let Andrew search the Purview audit log himself; that needs an audit role.
- **Do not use the escalation path.** Cloud Application Administrator can add a credential to *any* existing app,
  including one that already holds Graph application permissions, and then act with that app's grants. It is a
  documented privilege-escalation path, not an authorization. It would read as an attack in the audit log. The
  legitimate route is section 4.

## 3. The spine in three layers, and who can unlock each

| Layer | What it gives | Mechanism | Who can unlock it |
|---|---|---|---|
| **1. Event spine (metadata)** | Per-user, timestamped events: files opened, edited, shared and downloaded (SharePoint/OneDrive); mail sent and accessed; Teams meetings, chats and channel activity; sign-ins; Power Automate and admin events. **No message or document content.** | Unified audit log through the **Office 365 Management Activity API**: application permission `ActivityFeed.Read` on the *Office 365 Management APIs* resource (not Graph); subscriptions to `Audit.Exchange`, `Audit.SharePoint`, `Audit.AzureActiveDirectory`, `Audit.General` (Teams lives in General) ([API reference](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-reference)) | **Andrew, today** (inferred: it is a non-Graph application permission, which the role's consent rule covers; not exercised). Prerequisite: unified audit logging switched on (absent: not read). Lookback: about 180 days on Audit Standard; whether `MailItemsAccessed`, `Send` and Teams message events appear at our licence tier must be measured in-tenant |
| **2. Content** | Mail bodies, chat and channel messages, calendar, files, meeting transcripts for every employee: what each task *is* | (a) Graph **application** permissions `Mail.Read`, `Chat.Read.All`, `ChannelMessage.Read.All`, `Files.Read.All`, `Calendars.Read`, `OnlineMeetingTranscript.Read.All`; Teams bulk export (`getAllMessages`) is metered (model B, per message) ([Teams API licensing](https://learn.microsoft.com/id-id/graph/teams-licenses)); mail can be fenced to named mailboxes with Exchange RBAC for Applications. (b) **Microsoft Graph Data Connect**: bulk extract into the existing `Opal Capital` Azure subscription (`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~OG/G-C_CONTROLLED_IDENTITY_AND_GRANT_EVIDENCE.md:30-44`, held), about **$0.375 per 1,000 objects** plus Synapse/ADF costs, approved per pipeline in the M365 admin center ([datasets](https://learn.microsoft.com/en-us/graph/data-connect-datasets), [pricing](https://azure.microsoft.com/pricing/details/graph-data-connect/)) | **Not Andrew alone.** It needs a Global Admin or Privileged Role Admin to consent, or to assign Andrew Privileged Role Administrator. The tenant has `AzureAdmin@`, `breakglass@` and `LDTAdmin@` admin accounts (G-C evidence s.2, held); the IT vendor holds the earlier consents (`IT_REQUEST.md`) |
| **3. Off-Microsoft work** | Desktop Excel edits before save, Bloomberg, Schwab, BlackDiamond and other web portals, browser time | Not in any M365 log. Needs endpoint or browser telemetry, a separate tool and a separate decision | Out of scope here; named so the gap is not read as coverage |

**Population** (held, G-C evidence s.2, 2026-09-29): 38 internal accounts, of which **21 are named employees**. The
rest are shared mailboxes (7), admin/break-glass (4), rooms (3) and system accounts (3). The spine's population is
small; event volume per person is **absent** (not measured).

## 4. Recommended path

1. **Layer 1 now, under Andrew's own role.** Register one new app ("workflow spine"), add `ActivityFeed.Read`,
   consent, start the four subscriptions and land every content blob in an LGIC-built S3 home.
   **CORRECTION (same session, read from the API reference):** the Management Activity API holds content for
   **7 days only** (`AF20051`: "Content older than 7 days cannot be retrieved"), the first blobs take up to 12 hours
   after a subscription starts, and events inside blobs are not in order. It cannot pull the 180-day backlog; the
   spine builds forward from the day it starts, so the collector must run on a schedule with no gap longer than
   7 days. The 180-day history is reachable only through Purview audit search/export (an audit role, which Andrew's
   role is not) or the Graph audit-log query API (`AuditLogsQuery.Read.All`, a Graph application permission: Global
   / Privileged Role Admin). This is the
   sequencing-and-dependency spine: who touched what, when, in what order, across mail, files, Teams and meetings.
   The first act also settles two unknowns: whether audit logging is on, and which events our licence tier emits.
2. **Mine Layer 1 first** for recurring daily sequences and hand-offs between people. Pick the 5-10 workflows worth
   understanding in depth.
3. **Layer 2 only for those workflows.** Ask the Global Admin (the IT vendor) for a *scoped* grant: named mailboxes
   via RBAC for Applications, named Teams and sites, not tenant-wide. Or use Graph Data Connect with admin
   approval and a scrub group. Content is where client PII (Schwab and BlackDiamond account data in mail) and
   personal messages sit, so it should be the narrow layer, not the default.
4. Enter through `/brief-create` so it runs the canonical flow (it is a new pipeline: LGIC homes and names, rule 30).

## 5. Before anything is pulled -- not a gate, the facts Andrew decides on

- **Employee notice.** New York Civil Rights Law s.52-c (in force 2022-05-07) requires an employer with a place of
  business in NY to give written, acknowledged notice of email, phone and internet monitoring, and to post it;
  fines run $500 to $3,000 per violation. It does not apply to monitoring that is not aimed at a particular person
  and is done solely for system maintenance or protection, and per-employee workflow mining is neither
  ([statute](https://newyork.public.law/laws/n.y._civil_rights_law_section_52-c*2)). Opal's NY nexus and any existing
  handbook notice: absent (not read). Counsel's question, not this seat's.
- **Client data.** Content-layer extraction moves client PII into a new store; Reg S-P and the firm's own data
  rules apply to that store.
- **Separation.** Layer 2 consent sits with a second admin by Microsoft's design. That is Microsoft's control, not
  one this seat is adding.

## 5a. Addendum (same session): the app-only layer Andrew's role CAN approve

The non-Graph exception in section 2 reaches further than the audit log (inferred from the documented consent
rule; none exercised):

| API (resource) | application permission | reach | usable? |
|---|---|---|---|
| Office 365 Management APIs | `ActivityFeed.Read` | every employee's activity events (Layer 1) | yes |
| Office 365 SharePoint Online (`00000003-0000-0ff1-ce00-000000000000`, not Graph) | `Sites.Read.All` (or `Sites.FullControl.All`; `Sites.Selected` for named sites) | **every SharePoint site and every OneDrive** (OneDrive is SharePoint), content included | yes; app-only SharePoint needs a certificate, not a secret |
| Office 365 Exchange Online (EWS) | `full_access_as_app` | every mailbox | **no**: EWS phased disablement began 2026-10-01 (removal 2027-04-01) and re-enabling needs an Exchange admin to allow-list the app ID ([MC1227454](https://mc.merill.net/message/MC1227454), [MC1447678](https://mc.merill.net/message/MC1447678)) |

Still out of reach without a Global / Privileged Role Admin: Teams chat and channel content, calendars, and mail
through Graph. Ownership of M365-MCP-Graph is not what grants any of this; the role is. Put any app-only grant on a
NEW app, never on the gateway's user-facing app, so the gateway's secret does not carry tenant-wide reach. Every
consent is written to the Entra audit log (visible to the tenant's Global Admins).

## 6. Unmeasured, each closed by the first Layer-1 act

| item | state |
|---|---|
| Andrew's role is still active (not expired, not PIM-eligible only) | held 2026-09-14 |
| Unified audit logging is enabled | absent |
| Licence tier (Business Premium / E3 / E5): retention and which mail and Teams events are emitted | absent |
| `ActivityFeed.Read` consent succeeds under Cloud Application Administrator | inferred |
| Daily event volume per employee | absent |
| Who holds Global Admin / Privileged Role Admin today | held (named accounts only, not role-read) |

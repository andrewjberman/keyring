# ANDREW-DIRECT 2026-10-16 ~18:0xZ -- client-ops early-warning scans: fast-path, pptx deck, names anonymized

**Channel:** Andrew at the terminal of `4.0.0_SA_CRO~DELL1` (dell1), answering the CRO's plan for the client-ops early-warning
work (seeded by the Dave Victor postmortem). **Recorded by:** `4.0.0_SA_CRO~DELL1`, same turn.

VERBATIM (terminal):

> pptx, anonymize names, fast-path it. Let me know when the incidents are ready we start with those.

The three questions it answers, as asked: (1) deck format and anonymization; (2) CRO research plus a single-round brief to the
CTO, or fast-path; (3) delivery channel for the digest. Answer (3) is still OPEN: no send channel is chosen.

## The explicit ask behind the alert moratorium (CLAUDE.md section 5)

Andrew's own words to AJ Graff on Teams, 2026-10-16 17:26Z, VERBATIM:

> 1.) Outlook audit channel (which we collect automatically anyway via MS) looking for loose ends?
> (e.g. accounts operational but not resolved, unanswered emails, etc)
> 2.) Alerts on new cash accounts appearing in Schwab which are sitting more than X days.

And to Austin Graff on Teams, 2026-10-16 17:55Z: "We can start running scheduled scans on Outlook by the end of the day ...
specifically targeted at risky client ops scenarios, where things fall through the cracks. Think early warning system."

## How it is carried

- **Fast-path:** this work does not run the L1-L10 canonical workflow. Scope is exactly the early-warning scans and the deck;
  nothing wider is fast-pathed by this record.
- **Deck:** .pptx (not a published Slides artifact). Client names and account numbers are anonymized.
- **Order:** the postmortems come first; Andrew is told when the incident set is ready, and the work starts from those.
- **Moratorium:** lifted for this scope by the explicit ask above. Nothing sends until Andrew names the channel (OPEN item 3).

## Addendum, same session: the output surface

The CRO proposed one stream (Graph mail events + the Schwab daily file + the Tax SMA sheet) feeding six rules and one
open-items table. Andrew's reply, VERBATIM:

> and cast it on tv

- **Output surface:** the office TV, as a cast of an internal page showing the open-items stream.
- **Still OPEN:** the TV hardware and cast path; on-screen privacy (initials plus the last 4 digits is the proposal); who builds;
  and whether a Teams or email digest exists in addition to the TV.

## Addendum 2, same session: streaming ingestion

Andrew first set the order: streaming before casting, and casting is secondary. VERBATIM: "the casting is secondary, the
first thing is figuring out how to actually stream this + streaming email, like every 5 sec polling any fast moving
surfaces. any account/custodial stuff doesnt need to be polling because its uploaded once a day".

The CRO offered three options: Graph webhooks, Graph delta every 5 s, or both. It asked who approves the app-only Graph
access, and whether Teams is in round one. Andrew's reply, VERBATIM:

> delta 5s first, i approve, teams later

- **Email ingestion:** a Graph delta query every 5 s on Inbox and Sent Items of 49@ and the Opal staff mailboxes. Webhooks
  are deferred, and come only if 5 s proves too slow.
- **Access:** an app-only Graph credential with Mail.Read scoped to the monitored mailboxes, never Andrew's personal token.
  The tenant-admin approver is Andrew.
- **Custodial / account data:** no polling. It runs when the daily file lands, with a scheduled run as backstop.
- **Teams:** deferred to a later round.

## Addendum 3, 2026-10-17 ~02:0xZ: real account numbers, and build now

The CRO found that Schwab silver (`opal-data-assets/schwab/<master>/silver/`) carries raw account ids and titles, and that
only the opalgateway replaces them with a keyed HMAC (`account_ref`, NFRA_OPLGTW OG-z-3). It asked whether Opal staff
logins should see real numbers, and whether to start the Day 1 build. Andrew, VERBATIM:

> 1.) Yes they should show real acct numbers. 2.) Yes start building now

- **(1) Gateway:** Opal staff principals see real Schwab account numbers. Partner and external principals keep the keyed
  `account_ref`. This is a gateway change in the NFRA_OPLGTW lane, routed to its owner; it is not fast-pathed here.
- **(2) Build:** the Day 1 early-warning build starts now, offline:
  - a Graph delta poller (reusing the IRPT IB-s-6 client);
  - INBOX RADAR, the open-items store and the business-hour clock;
  - a YTD replay as proof.
  It runs no live app-only mailbox read until the Graph grant exists (Day 0, Andrew).
  The daily rules read Schwab silver directly, never through the gateway.

## Addendum 7, 2026-10-19 ~14:4xZ: a client-ops data store, twice-daily scans, and user access over the gateway

Andrew, VERBATIM:

> I think what needs to happen is that there is a database that holds all of this information with regular scans at 9a every day
> and 4p every night, naive eastern time. This will be held in a bucket like opal-data-clientops. then we can connect users to this
> bucket and they can ask for warnings on various surfaces that our scanners are providing. I want you to formalize this design, it is
> the same pattern we are developing across the platform with NFRA_OPLGTW/MCPINDEX, e.g. how we have a "Security Analysis"
> application dashboard for Asset Management that is fed by opal-data-harvest which is accessible via a tool index for users over
> opalgateway mcp.

- **Ask:** the CRO formalizes the design as a document; this addendum is not a build order. The design covers:
  - a durable store of every scanner finding in a dedicated client-ops bucket (the name comes from the builders; "opal-data-clientops"
    is Andrew's illustration);
  - scheduled scans at 09:00 and 16:00 America/New_York ("naive eastern time");
  - users reach the warnings through the opalgateway MCP tool index, on the same pattern as opal-data-harvest feeding the
    Security Analysis dashboard and the harvest_* tools (NFRA_OPLGTW / NFRA_MCPINDEX).
- **Unchanged by this addendum:** addenda 5 (findings only) and 6 (the approved thresholds and owners).

## Addendum 6, 2026-10-17 ~05:0xZ: all open-call RECs approved

The CRO printed /open-calls; cards 4 and 5 were withdrawn under addendum 5. Andrew, VERBATIM:

> all recs approv ed

**Approved, as carded:**

| Card | Approved |
|---|---|
| 1 | SLEEPING MONEY ALARM: a new account fires at 5 business days, idle cash at 5 trading days. The legacy-exclusion list comes from ops after a week of live output. |
| 2 | Stale items auto-expire after 10 quiet business days and leave the screen, but stay in the log and the digest. A one-click dismiss needs a reason. |
| 3 | Runtime: one always-on AWS container (~$10-15/mo) beside the gateway, routed to CloudOps (TCKT macro lane). |
| 6 | Digest: a Teams channel post to a client-ops channel, once daily at 08:00 CT. Which channel is still to be named. |
| 7 | Rule owners, as a system setting: INBOX RADAR = Manav; SLEEPING MONEY, PAYDAY GUARD and FEE TRIPWIRE = Menachem; RULE CHANGE RELAY = Yang. |
| 8 | Monitored-mailbox group: Andrew, Manav, Menachem, Yang, Alyssa, Jeanette, Jim. |
| 9 | Deck v2 keeps its LIVE IN numbers. The email items carry the footnote "from Graph consent". |
| 10 | The IRPT YCharts brief stays parked. |
| 11 | The /lauren-report chartbook is seeded from Lauren's 2Q workbook. |

## Addendum 5, 2026-10-17 ~04:5xZ: no position on client-ops outreach

The CRO's /open-calls carried two cards that took positions on client-ops outreach: refunding the Victor fee, and sending
advisors a notice of the Schwab cutoff plus telling Peter Lee. Andrew, VERBATIM:

> do not take any position on the client-ops outreach, not our job not our call

- The early-warning work SURFACES findings: what happened, since when, the evidence.
- It never recommends, drafts or routes client-facing or advisor-facing action, whether a refund, a notice, outreach or
  a question to an advisor.
- The "suggested owner/action" column on danger-zone output is withdrawn. Who acts on a finding is client ops' call.
- Rule owners stay a system setting: whose screen row an item lands on. That is not outreach.

## Addendum 4, 2026-10-17 ~03:3xZ: an interim bridge on Andrew's mailbox

Admin consent for the app's `Mail.Read` (application) failed: Andrew holds Cloud Application Administrator, and consent
needs Global Administrator or Privileged Role Administrator. The ApplicationAccessPolicy needs Exchange Administrator. Both
wait on a Global Admin (likely AJ).

The CRO proposed a bridge: INBOX RADAR reads Andrew's own mailbox, which receives 49@ and inflection@, through the gateway's
existing delegated access every ~5 minutes, until the app-only grant and its policy test pass. Andrew, VERBATIM:

> yes we can run it on mine thats fine

- **Scope:** Andrew's mailbox only, read-only, about every 5 minutes, labeled BRIDGE.
- **Retirement:** it is switched off when `Test-ApplicationAccessPolicy` prints Granted for a member and Denied for a
  non-member.
- **Known gap:** an Opal reply that copies neither 49@ nor Andrew is invisible, so false "unanswered" items are possible.
- **Done already, outside the grant:**
  - the app registration `opal-client-ops-early-warning` (client `3d9262d1-36a0-476b-b176-cf8e0fa427ed`);
  - a certificate credential in Secrets Manager `opal/ews/graph-app-cert` (thumbprint `4EC53E1D...C5B8`; the public
    `.cer` handed to Andrew for upload);
  - no client secret.

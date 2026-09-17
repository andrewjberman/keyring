# BRIEF -- mcportal: the internal tech-ops dashboard on the Gateway's address

**Author:** `4.0.0_SA_CRO` | **Written:** 2026-09-17 (UTC) | **Mode:** NEW (no project exists; prior art is heavy)
**Asked by:** Andrew, directly at this seat's terminal, 2026-09-17, followed by a page-by-page interview
(layout sketch + decision cards per page; every card answered by him in-session).
**Consumer:** `1.0.0_SA_CTO` `/endpoint --forward`.
**Vintage:** code reads at CLOUD `7ce1d4be31` .. `cc3d46ab63`, portal `be8cf218`. Line citations come from four
read-only research passes run for this brief; they are the passes' reads, not re-verified line by line here.
**Companion brief:** `docs/briefs/opal-mcp-tool-index-scoping-20260917.md` @`2a7fc3339f` (the tool index this
dashboard's MCP Server page displays).

---

## ANDREW'S WORDS, VERBATIM (this terminal, 2026-09-17)

**The ask:** *"I also want another brief, the purpose of which is to make mcp.opalinvest.com actually an internal
tech ops dashboard. It should only display for andrew@opalinvest.com. I would actually build out a new repo called
mcportal for this purpose. The premise is fairly similar to the current portal, except it's exclusively dedicated to
having a management portal to operate the portal backend. First page should be some kind of summary view. Then there
should be a sidebar layout using same structure as the opalinvest.dev dashboard portal repo where we have items like
"user management" (can add/subtract users from any given platform and modify permissions at both general level and
partner level via DDB writes), "mcp ops" which has sections for opal propertiesa nd what tools address them (seeing
the library of active tools and a description of what they address)as well as a user entitlements function where we
can add/subtract estate access (e.g. schwab endpoints in opal-data-assets) and tool permissions per user, "daily
report" which is just the /sprint page as it stands now from the daily-sprint process (this may just be the home
page), "health check" which is what the NFRA_REPORT is basically designed to do, "cost management" which will require
figuring out every cost we have and feeding it into this thing (should be separated from the NFRA_REPORT group of
outputs, "infosec" which is just some kind of monitor view of the various opal properties and their firewalls
suspicious ips access patterns etc., and maybe a few more things."*

**Round 1 answers:** *"1.) A. 2.) Yes just me. 3.) Changing should be allowed, it is meant to be able to act as a
fast response tool to facilitate user management, mcp ops, and more. 4.) Just opalinvest.dev dashboard for now on
that page, using the opal-users-v2 and associated opal-partners-* DDB tables. Also would like the dedicated demo
table included so I can rapidly issue credentials for test users as well. 5.) AWS, My Claude Accounts, Bright Data,
Quo, any technology service (I would scan for Ramp charges in my outlook via opal-gateway to find the ramp receipt
requests and aggregate from there). 6.) This is not an alert, this is an analytics dashboard. Strictly read when
opened. 7.) Honestly should just be a summary of platform ops. Daily Sprint can be its own specific page in the
sidebar."*

**Follow-ups:** *"Ramp Categories: we can have two views, vendor and purpose, say its a pie chart display and
there's a toggle. FOr MCP Ops: Take effect immediately. Also I think there should be a page that uses the "Session
Analytics" lambda framework as well, getting user activity that is provided from that function for visualized charts
of that data."*

**Sidebar order:** *"I would put Daily Sprint right after Home, but I'd call it Operations Report. then User
Management and User Analytics, then MCP Server, then Health Check, Cost Management, and Infosec."*

**Card answers, by page:**
- User Management: *"1.) Rec approved. 2.) Rec approved, you're correct. 3.) I'll handle cleanup manually from the
  interface. 4.) B works, rec approved. 5.) Later."*
- User Analytics: *"1.) A for now. 2.) Named. 3.) Include Opal and Clients. 4.) Rec approved, a is fine. 5.) That
  should be on MCP page not here."*
- MCP Server: *"ALl recs aproved"*
- Health Check: *"Recs approved"*
- Cost Management: *"1.) I don't believe they have an API accessible for me, easier to just scan for ramp emails
  with a pull from graphAPI from outlook via opalgateway mcp. Rest of recs approved"*
- Infosec: *"recs approved"*
- Home and Operations Report: *"recs approved for all except locking up daily sprint, any Opal MS user should have
  access to it"*

**The address, corrected by him:** *"Sorry this is definitely the .dev domain, lets make sure that is cleared up."*
**THE DASHBOARD'S ADDRESS IS `mcp.opalinvest.dev`.** The `mcp.opalinvest.com` in his original ask above is kept
only because it is a verbatim quote; it names no deliverable. `opalinvest.com` (the marketing site) is not touched
by this project.

---

## PART I -- THE OUTCOME TERRITORY

"Andrew" below means the one signed-in person this dashboard serves.

### O1. Andrew opens one address and sees in a few seconds whether anything on the platform needs him
Home is one screen of six cards (Health, Users, MCP Server, Cost, Infosec, Operations Report) under a one-sentence
verdict. Home owns no data: every number is the header number of the page it links to, so a wrong number is fixed in
exactly one place. A second tab, Recent Changes, lists every write made from the dashboard, newest first, each with
before, after and a revert.

### O2. Andrew reads the daily Operations Report inside the dashboard, and any Opal Microsoft user still reads it at /sprint
The published daily report is framed as-is (today's report plus the archive by day, desktop or mobile view). The
existing `/sprint` address stays open to any signed-in Opal Microsoft user -- his explicit exception to "only me".

### O3. Andrew adds, edits, disables and removes an opalinvest.dev user, at both permission levels, from one screen
General level (`opal-users-v2`: role, tier, firm, user type, password reset) and partner level
(`opal-partner-<firmId>`: firm role, advisor role, advisor key), shown together for one person. "Remove" disables
first (sign-in blocked, history kept); hard delete is a confirmed second step. Every write is audited and
revertible.

### O4. Andrew issues a working demo login in under a minute and revokes it himself when done
A Demo Credentials tab writes the demo-firm rows (`opal-partner-demo` plus a demo-firm profile), shows the one-time
password once, and lists live demo users with a revoke button. No automatic expiry -- cleanup is his, from the
interface.

### O5. Andrew sees who actually uses opalinvest.dev -- by name, by firm, by page and feature -- and who never has
Charts from the Session Analytics data: active users over time, sessions by firm, active versus idle minutes, page
and feature use, exports and searches. A Users tab names each person with last-seen and includes people who have
never signed in. Opal staff and client users are both counted. A Sessions tab drills into one person's or one day's
sessions with the journey summary the existing function already computes.

### O6. Andrew sees every Opal data property beside the tools that address it, and every tool with what it answers
A Properties tab (property, where it lives, freshest date, tool count, state: LIVE / BUILT NOT ENABLED / GAP) and a
Tool Library tab (tool, group, what it answers, safety class, tier needed, calls in 30 days). A tool with no safety
classification is flagged. Enabling a whole data source stays a deployment; the dashboard displays that state only.

### O7. Andrew grants or removes one person's estate access and tool permissions, and it takes effect on their next call
An Entitlements tab edits, per person, the data grant (masters, datasets, accounts, dates, columns, operations) and
the tool permissions (tier, write classes, per-person tool list), with named presets he can edit, a revoke-all, and
a before/after history. Changes apply immediately, by his word.

### O8. Andrew sees who called which tool, what was denied, and can stop a person or the whole server at once
A Usage tab from the tool-call log (calls per day, by tool, by person, denials by reason, never-called tools) and a
Controls tab (kill switch, block a person, revoke a person's tokens, the blocked-address list). MCP usage lives
here, not on User Analytics.

### O9. Andrew answers "did everything land, and is what's deployed what we intended" without opening the email
Health Check shows the verdict and only the rows that need him, then tabs for Data Freshness (lateness counted in
trading days), Schedules, Functions, Deploys and 90 days of History, grouped Dashboard / Website / Gateway / Graph so
the page and the emailed report agree. A "Re-run now" button invokes the existing daily monitor. Cost and security
sections are not shown here.

### O10. Andrew sees every technology dollar -- AWS and everything else -- by vendor or by purpose, and what moved
A pie with a vendor/purpose toggle, a trailing-twelve-month bar chart, biggest movers, an AWS tab (by service, by
pipeline tag, untagged spend shown as its own bar), a Vendors tab, a Charges tab and an editable Mapping tab
(merchant to vendor to purpose). Non-AWS charges come from Ramp receipt-request emails in his Outlook, read through
the Gateway with his own sign-in when he clicks Sync. Costs that never touch Ramp are manual recurring rows, marked
manual.

### O11. Andrew sees who is knocking on each Opal property, what was blocked, and blocks an address in one click
Infosec shows, per property (opalinvest.dev, mcp.opalinvest.dev), firewall blocks by rule and over time, failed and
throttled sign-ins, a Suspicious IPs table with a block button (audited, with unblock), the daily security scan's
score and findings, and an AWS Activity tab limited to root use, console sign-ins and permission changes.

### O12. Nobody but Andrew can open the dashboard or use its write paths
Microsoft sign-in at the load balancer, then a server-side exact match on his email for every page and every write
handler -- never a hidden menu. The only exception is O2's `/sprint`.

---

## PART II -- WHERE THE BOUNDARY SITS

| This project OWNS | It RELIES ON (and does not change) | Sibling |
|---|---|---|
| The `mcportal` repo, its pages, its admin API handlers, its audit rows | The Gateway's sign-in, identity verification and existing Claude-client paths | NFRA_OPLGTW |
| A grant-writer that holds the admin role (O7) | The grant model, the DynamoDB grant table, the per-call strong read | NFRA_OPLGTW |
| Moving tiers and per-person tool lists from flat files into the grant table | Kill switch and blocklist stay files (must work if DynamoDB is unreachable) | NFRA_OPLGTW |
| The Properties/Tool Library DISPLAY | The one data catalog and the tools themselves | the tool-index project (companion brief; NONE-YET) |
| The Health Check DISPLAY and the re-run button | The daily monitor, its 13 sections, the edition engine, the email | NFRA_REPORT (D12) |
| The Operations Report frame | The daily-sprint process and its published HTML | `/daily-sprint` |
| Three nightly rollups: session analytics, firewall counts, AWS cost history | `opal-session-analytics`, `opal-sentinel`, the monitor's cost sections | NFRA_OPSEC202609 (closed) |
| The Ramp email collection, cost table, vendor/purpose mapping | The Gateway's `search_email` / `read_email` under his own token | -- |
| Session-analytics retention declared in Terraform + its API brought under Terraform | The portal client SDK and ingest path | portal |

**Explicitly NOT this project's:** changing what the emailed report contains (NFRA_REPORT's; raise it there once the
Cost page exists); the session-analytics logging, cross-origin and firm-filter fixes (a portal-side security item
with its own review); GuardDuty (a later, separate spend decision); the marketing website as a third Infosec
property (later, once its firewall logging is confirmed); "View as this user" (later); a Fabric page for the
agent-side dashboards (later, own page); monthly target lines (later).

**The rule that keeps this outside the standing ban on alerts and monitors:** the dashboard sends nothing and adds
no checker. Every page reads what an existing producer already publishes, or a rollup of data already collected.
A signal that does not exist yet is a separate request, never a rider here.

---

## PART III -- THE QUALITATIVE BAR

- **Home:** Andrew decides whether to open any other page from Home alone, without opening the emailed report.
- **User Management:** Andrew onboards a new partner user without running a DynamoDB command from the runbook.
- **Demo:** Andrew hands a prospect a login during a call instead of after it.
- **User Analytics:** Andrew names, for a given firm, who has never signed in -- a question nothing answers today.
- **MCP Server:** Andrew grants Schwab access to a colleague from a browser, and their next tool call succeeds,
  where today the only path is an operator command line.
- **Health Check:** the page and the email never disagree, because there is one engine.
- **Cost:** Andrew states last month's non-AWS technology spend by purpose without opening Ramp.
- **Infosec:** Andrew goes from "this address looks wrong" to "blocked" without the AWS console.
- **Access:** a signed-in Opal colleague who types the dashboard address gets a refusal, and gets the report at
  `/sprint`.

---

## PART IV -- THE SUBSTRATE: what already exists

1. **The address and the split.** The Gateway host in code is `mcp.opalinvest.dev`
   (`infra/aws/terraform/opal-gateway/main.tf:95-98`); `opalinvest.com` is the marketing site with DNS at GoDaddy.
   The load balancer's default action is Microsoft sign-in (`alb.tf:161-197`); exact-path rules let Claude clients
   through without it (`alb.tf:222-311`). `alb.tf:215` reserves "everything else" as "the future GUI path" -- a
   dashboard at `/` cannot affect Claude clients.
2. **The allow-list pattern.** `/sprint` already serves S3-published HTML behind that sign-in
   (`app/sprint_view.py`, routes `app/server.py:858-861`) with an allowed-emails setting (`app/config.py:103-104`;
   empty = whole tenant). `MASTER_ADMIN_EMAILS` defaults to his address (`config.py:241-243`).
3. **User tables.** `opal-users-v2` (PK `USER#<id>` / SK `PROFILE`; indexes by email and firm; hand-managed, no
   Terraform) and `opal-partner-<firmId>` (hash `email`; Terraform module `partner-firm-table`; firms 49financial,
   cottonwood, inflection, demo). The auth function already exposes admin create / list / delete / reset
   (`auth-handler/src/index.ts:413-463`). **No screen exists for any of it**; today's path is a raw `put-item`
   runbook (`infra/aws/users/ONBOARDING.md`).
4. **Grants.** `gateway-access-state-table`, `POLICY#<tid>#<oid>` partition, record types `principal_profile`,
   `data_entitlement`, `operator_audit` (`app/access_state.py:42-74`). The only writer is a command line restricted
   to role `opal-gateway-access-admin` (`ops/schwab_entitlement_admin.py`); the Gateway's own role is IAM-blocked
   from that partition on purpose (`access_state.py:16-19`).
5. **Tool permissions are flat files on the server:** tiers (`app/entitlements.py`), per-person tool list
   (`app/identity_scope.py`), blocklist and kill switch (`app/blocklist.py`), revoked tokens (`app/revocation.py`).
6. **Tool index.** 49 tools registered, 44 enabled; the five Schwab tools are built but not enabled;
   `read_teams_attachment` is live but denied to every tier because it has no safety classification (companion
   brief, s.1).
7. **Tool-call log.** `opal_mcp.mcp_audit` (time, user, tool, args, outcome), queryable
   (`infra/aws/terraform/opal-gateway/audit-lake.tf`).
8. **Session Analytics.** `opal-session-analytics` (Node 20) stores sessions and events in DynamoDB
   `opal-sessions`; read endpoints for one user, one day and one session summary exist; **nothing consumes them and
   no path computes totals over time.** Findings: expiry stamp written but no expiry declared on the table
   (`portal-auth/dynamodb.tf:46-83`); full request bodies logged; open cross-origin; no firm filter on reads; its
   API Gateway is outside Terraform.
9. **Health.** `opal-infrastructure-monitor` publishes `opal-data-portal-v2/infrastructure/status/latest.json` and
   an archive daily; NFRA_REPORT (active, round 4) is reshaping it into rows with per-row change, a computed
   verdict, and the Dashboard / Website / Gateway / Graph grouping. Freshness definitions:
   `data/served_freshness_config.yaml`. Schedules: `.tools/schedule-check.py`.
10. **Cost.** Cost Explorer is already queried by service and by Pipeline tag inside the monitor; six cost tags are
    active. **No vendor or subscription record exists anywhere.** No budgets, no billing export.
11. **Infosec.** Two firewalls with logging (Gateway regional; portal CloudFront); `opal-sentinel` filters both log
    streams for blocks and login abuse and has a daily digest; evidence bucket `opal-security-evidence`; daily
    security scan publishes score and findings; organization activity trail exists. **Not deployed:** GuardDuty,
    Security Hub, network flow logs.
12. **Repo and UI precedent.** `Opal-Capital/portal`: separate repo pinned into the workspace, DEV/PROD branches,
    CI to S3 + CloudFront, React + Vite + TypeScript + bun. Sidebar and layout live inline in `portal/src/App.tsx`
    (`NAV_SECTIONS` `:89-136`, `DashboardLayout` `:214+`). Current design law is the 2026-09-11 one
    (`portal/CLAUDE.md`, `portal/DESIGN.md`): light canvas, white panels, one dark band per page -- a new repo
    starts clean on it.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

1. A `mcportal` row in the naming registry (`infra/logic/registry/systems.json`; the `gateway` row is the one to
   copy) **before any resource is created** -- the naming gate refuses since `d181e0ac5a` (notice 97614).
2. The new GitHub repo `Opal-Capital/mcportal`, pinned into the workspace the way `portal` is.
3. A decision on where the built pages are served from (the Gateway server itself, or S3 behind the same sign-in);
   either satisfies O12 so long as the email match is server-side.
4. A grant-writer that holds `opal-gateway-access-admin`, invoked only with his verified identity -- so the
   Gateway still cannot grant itself access (his approved Call 1, MCP Server).
5. Tiers and per-person tool lists readable from the grant table by the Gateway's enforcement path.
6. A way for the dashboard backend to write `opal-users-v2` and the partner tables, and to call the auth
   function's admin routes, and a `disabled` state the auth function honours.
7. Three nightly rollups (session analytics, firewall counts, AWS cost history) and one cost table. Each is a
   scheduled producer, named by the builder (Rule 30).
8. Confirmation that the firewall block lists tolerate writes from outside Terraform.
9. His sign-in present when Ramp emails are read (the Gateway reads mail only with the person's own permission).
10. The never-widen and change-ledger rules apply to every act that touches the load balancer, the grant table's
    permissions, or the auth function.

**Andrew's approved build preference (his ruling, recorded; not a decomposition):** Home shell, then Operations
Report, User Management, MCP Server, Health Check, User Analytics, Infosec, Cost Management. Phone-friendly: Home,
Operations Report and MCP Server Controls; the rest desktop-first.

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-09-17 from the repo only; no AWS reads were made for this brief.
- No `mcportal` repo, registry row, project or PRD exists. No Andrew-direct record on an ops dashboard predates
  today.
- `/sprint` is live and open to the whole tenant (allowed-emails empty).
- NFRA_REPORT: active, EXECUTING, round 4. NFRA_OPLGTW: EXECUTING. NFRA_OPSEC202609: closed 2026-09-11.
- The companion tool-index brief is committed locally @`2a7fc3339f`; no project yet.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

1. **The address is SETTLED, not open: `mcp.opalinvest.dev`**, on his word (quoted above). Listed here only so a
   reader who saw `.com` in the original ask finds the correction.
2. **Demo exclusion in analytics.** He said "Include Opal and Clients"; this seat read demo users as excluded by
   default. Asked directly ("should demo users stay out of the User Analytics charts by default?"), he answered
   *"Sure"* -- SETTLED: demo users are excluded from the charts by default.
3. No AWS state was read: whether session retention is actually enforced, whether the block lists are
   Terraform-managed, whether the website has firewall logging, and the size of any log or table are all unmeasured.
4. Which of his vendors bypass Ramp is unknown to this seat.
5. How reliably merchant, amount and date parse out of Ramp receipt-request emails is untested.
6. The page sketches shown in the interview are intent, not design; the portal's design law governs the build.
7. Line citations are the research passes' reads at the vintages above, not re-verified here.

---

## REFS

```
  BRIEF PATH        docs/briefs/mcportal-tech-ops-dashboard-brief-20260917.md
  PROJECT           NONE-YET
  EXISTING PRD      NONE
  SIBLING PROJECTS  NFRA_OPLGTW, NFRA_REPORT, NFRA_OPSEC202609 (closed), NFRA_SPMOVE, the tool-index project (NONE-YET)
  COMPANION BRIEF   docs/briefs/opal-mcp-tool-index-scoping-20260917.md @2a7fc3339f
  PRIOR ART         app/sprint_view.py; gateway-access-state-table + ops/schwab_entitlement_admin.py;
                    auth-handler admin routes; opal-session-analytics; opal-infrastructure-monitor status feed;
                    opal-sentinel; opal_mcp.mcp_audit; portal/src/App.tsx layout; NFRA_TAGGING_STANDARD.md
  MEASURED AT       2026-09-17, repo reads only
```

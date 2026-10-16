# M365 workflow activity spine -- every employee's Microsoft 365 actions as one timeline (L1 brief, NEW)

**Author:** `4.0.0_SA_CRO~XXX` (dell1). **For:** `1.0.0_SA_CTO`, `/endpoint --forward` at L2.
**Asked by:** Andrew, Claude Code terminal on dell1, 2026-10-16 ~01:2xZ, VERBATIM, after the research below:
"yes do it" (to "Want me to write the `/brief-create` for the spine now?"). His founding request (2026-10-15
~23:5xZ) is quoted in full in the research note, section 0: *"create a timeline "spine" of all actions all employees
take on Microsoft, with the guiding purpose being to reverse engineer every workflow ... common tasks that happen
every single day, the sequencing of those tasks, the content of those tasks, how they depend upon one another, where
there are opportunities for waste reduction through AI Implementation."* Later the same session: *"I am interested in
this application and do think we should build it."*
**Research basis:** `org/tier1_exec/4.0.0_SA_CRO~XXX/deliverables/M365_WORKFLOW_SPINE_ACCESS_RESEARCH_20261015.md`
(@158eb209d9). **Mode:** NEW (nothing is built).

---

## PART I -- THE OUTCOME TERRITORY

**Candidate thread (becomes FWD-1):** Andrew picks one employee and one trading day and reads that person's
Microsoft 365 day in order. Coarse grain: one person, one day, whatever workloads the audit log emits for our
tenant. Round 1 builds it end to end: consent, subscription, scheduled collection, landed events, a readable day.
Every other outcome enriches that thread.

### O1 -- Andrew reads any employee's trading day as one ordered timeline
He names a person and a trading day and reads, in time order, what that person did in Outlook, Teams, SharePoint
and OneDrive: the action, the object (file, message, meeting) and the time. This is the thread.

### O2 -- Andrew follows a hand-off from one person to the next
From any step on a timeline he can see who acted next on the same object (the same file, the same email message,
the same meeting) and jump to that person's timeline at that moment. A chain A -> B -> C reads as one chain.

### O3 -- Andrew sees which workflows recur every trading day
He reads the sequences that repeat across trading days, for one person and across people (for example, the same
three files edited in the same order by the same two people each morning), each with the days it occurred on.

### O4 -- Andrew sees where the time goes inside a recurring workflow
For a workflow from O3 he reads the elapsed time between its steps and can tell waiting (a hand-off sitting
unopened) apart from doing (consecutive actions by one person).

### O5 -- Andrew receives a ranked list of AI waste-reduction candidates, each backed by its evidence
Each candidate names the recurring workflow, the steps an AI could take over or remove, and the timeline chains it
was drawn from, so he can open the evidence instead of trusting the summary.

### O6 -- A research seat queries the spine the way it queries the estate's other planes
A CRO or analyst agent asks the spine questions (who touched this file this week; which chains start from this
mailbox) through the same query surface it uses for the warehouse today, without a bespoke export.

### O7 -- Andrew can tell what the spine did not see
For any day he reads which workloads and event types were collected, and whether collection had a gap. A gap the
source could no longer fill (the source keeps 7 days) is shown as a permanent hole, never as a quiet day.

### O8 -- Andrew decides who is in the spine, and the spine honours it
He sets the population (named employees in; shared mailboxes, rooms, admin and system accounts out, or any
person he excludes) and every timeline, chain and candidate reflects that choice.

### O9 -- For a workflow he chooses, Andrew reads the content behind its steps (enrichment, his word on scope)
For a recurring workflow from O3 he opens the document or file content its steps touched, so "what the task IS"
is answered as well as "when and by whom". Reachable today for SharePoint and OneDrive only (Part IV, F5);
mail and Teams content are not reachable under Andrew's role.

---

## PART II -- WHERE THE BOUNDARY SITS

**Owns:** the new single-purpose Entra app and its one consent; the audit-log subscriptions; the scheduled
collector; the landed event store and its derived timelines, chains, recurring-workflow and candidate views; the
population setting (O8); the coverage record (O7).

**Relies on, does not own:**
- **NFRA_GLOBGRPH** (the estate graph, Nessie/Iceberg warehouse `opal-313476888478-globgrph`, the `globgrph-trino`
  query surface). The spine may land beside it as its own namespace; GLOBGRPH's tables, derive and projection are
  not changed by this project.
- **NFRA_OPLGTW** (the Opal gateway). Its M365 apps stay delegated-only. **This project adds no permission to
  "M365-MCP-Graph" or "M365-MCP-Login"**; the app-only grant lives on the new app so the gateway's secret never
  carries tenant-wide reach.
- **The transcripts pipeline** (`teams-global-transcripts-pull`, `outlook-global-transcripts-pull`,
  `opal-data-transcripts`): one identity's transcripts and mail. Not merged into, not replaced.
- **NFRA_MCPINDEX** (the gateway catalog). If O6 is served through the gateway catalog, the catalog row is
  MCPINDEX's; the spine supplies the dataset.
- **LGIC** (`infra/logic/`): homes, tenancy and names come from its builders (rule 30).

**Explicitly out:**
- Mail and Teams **content** (needs a Global or Privileged Role Admin grant; a separate decision by Andrew).
- The 180-day audit **backlog** (needs Purview export or the Graph audit-log query API, both outside Andrew's role).
- Anything off Microsoft: Bloomberg, Schwab, BlackDiamond and other portals, desktop work before save.
- **Alerting.** The spine is an analysis surface. It raises no alert, alarm or notification on what a person does
  (standing moratorium).
- Exchange EWS `full_access_as_app` (phased disablement began 2026-10-01).

---

## PART III -- THE QUALITATIVE BAR

- Andrew reads a named colleague's morning and recognises it as what that person actually did, in the right order,
  without being told.
- A hand-off Andrew already knows about (someone emails a file, someone else edits it) appears as a chain he can
  follow both ways, not as two unrelated rows.
- A workflow the spine calls "daily" is one Andrew agrees is daily; one it misses is one he can show it missed, by
  pointing at days where the events exist.
- An AI candidate Andrew reads is specific enough that he could hand it to a seat to build, and its evidence chains
  survive him opening them.
- A day with no events for a person reads either as "no activity collected" with the coverage stated, or as a gap.
  Never as a silent blank.
- Nobody outside Andrew's chosen population appears anywhere.

---

## PART IV -- THE SUBSTRATE: is this in a canonical pattern?

**F1. Nothing collects this today.** Measured 2026-10-16 ~01:2xZ. The Nessie warehouse
(`s3://opal-313476888478-globgrph/warehouse/`, branch head `de096ea838...` committed 2026-10-16T01:19:00Z) holds
namespaces `axes_history, code_heat, cse_ingest, cse_ingest_staging, fedobs_obs_findings, fedobs_signals, globgrph,
ms_heat, snap_ingest, tool_activity`. None is an M365 activity log. The served graph's M365 slice is a snapshot of
one SharePoint site: 6,929 `MS_FILE`, 1,390 `MS_FOLDER`, 19 `MS_USER`, each file with `last_modified_dt` and
`owner_upn`. No actor per change, no history, no mail or Teams. `ms_heat` is a one-off score from 2026-07-17 whose
own params read "content/comms NEVER read". The gateway catalog answers "not catalogued" for an M365 activity log.
Repo census for the API's markers (`manage.office.com|ActivityFeed|UnifiedAuditLog|Audit.*|auditLogs/|signIns|
MailItemsAccessed`): 11 hits across 85,565 files, none an ingestion.

**F2. The gateway cannot be the collector.** Its Graph app holds 17 delegated scopes only
(`infra/aws/ec2/opal-gateway/IT_REQUEST.md:3`, `app/config.py:61-68`); a delegated token never reaches past the
signed-in person.

**F3. The source and its shape.** Office 365 Management Activity API, application permission `ActivityFeed.Read`
on the Office 365 Management APIs resource (not Graph). Content types `Audit.Exchange`, `Audit.SharePoint`,
`Audit.AzureActiveDirectory`, `Audit.General` (Teams). Read from Microsoft's API reference this session:
- content is retrievable for **7 days** (`AF20051`), so an unattended gap longer than that loses events for good;
- the first content arrives up to **12 hours** after a subscription starts;
- events inside a content blob are **not in time order**;
- a stopped and restarted subscription cannot recover the content from the stopped interval.

**F4. Who can turn it on.** Andrew holds tenant-wide Cloud Application Administrator, verified 2026-09-14
(`IT_REQUEST.md:75`), not re-read since. That role can consent application permissions on any API except Microsoft
Graph, which covers `ActivityFeed.Read`. That this consent succeeds is inferred from the published rule, not exercised.

**F5. The O9 content reach under the same role.** The SharePoint Online API (resource
`00000003-0000-0ff1-ce00-000000000000`, not Graph) application permissions `Sites.Read.All` or `Sites.Selected` are
also within the role's consent rule. App-only SharePoint needs a certificate, not a secret. Inferred, not exercised.

**F6. Canonical fit.** The estate's pattern for a new data plane is an LGIC-built home with names from
`lib/opal_naming.py`, landed raw then normalised, and queried through the warehouse's existing surface. LGIC's
registry already carries system rows for `microsoft-teams`, `microsoft-outlook` and `microsoft-sharepoint`
(`infra/logic/registry/systems.json:442-462`, read 2026-10-16). Whether the builders admit this plane's addresses
and names is unmeasured (Part VII).

**F7. Population.** 38 internal Entra accounts: 21 named employees, 7 shared mailboxes, 4 admin/break-glass,
3 rooms, 3 system (held, `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~OG/G-C_CONTROLLED_IDENTITY_AND_GRANT_EVIDENCE.md`
s.2, 2026-09-29).

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- Unified audit logging is on for the tenant.
- Andrew's Cloud Application Administrator assignment is active when the consent is given (not expired, not
  eligible-only).
- The new app exists with `ActivityFeed.Read` consented, and its credential is held where the estate holds secrets.
- Collection runs on a schedule (production pipelines are scheduled) with no unattended gap reaching 7 days.
- LGIC registry rows admit the plane's homes and names; any refusal is a missing row, never a hand-typed name.
- Andrew's word on the population (O8) and on O9's content scope before content is read.
- Event records may carry file names, email subjects and client names. They land under the estate's existing data
  rules for client data; no raw capture enters the repository.
- Employee notice. New York Civil Rights Law s.52-c requires written, acknowledged notice of email and internet
  monitoring for an employer with a NY place of business. Whether Opal has one, and whether the handbook already
  carries the notice, is Andrew's (and counsel's) to settle. Named here as a fact, not a gate.
- Recurring-workflow mining needs enough trading days of collection to show repetition. How many is a later
  measurement, not a number set here.

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-15 23:5xZ to 2026-10-16 01:2xZ unless stated.
- No app, subscription, collector or table for the M365 audit log exists (F1).
- Gateway: delegated-only, 17 scopes; Andrew is its master admin (deployed `.env` read 2026-09-29, held).
- Warehouse branch head `de096ea838...` at 2026-10-16T01:19:00Z; `globgrph-trino` task `7174173c...` and
  `globgrph-nessie` task `f27c3077...` RUNNING (`ecs list-tasks`, 2026-10-16 ~01:2xZ).
- Andrew's role: verified 2026-09-14, not re-read.
- Audit logging on/off, licence tier, per-person event volume: unmeasured.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **Not claimed: the consent works.** F4 and F5 are read from Microsoft's published consent rule; nothing was
  registered or consented.
- **Not claimed: which events our tenant emits.** Whether `MailItemsAccessed`, `Send` and Teams message events
  appear depends on the licence tier and audit configuration; unmeasured. O1's richness depends on it.
- **Not claimed: a Trino session read.** dell1 has no ECS Exec plugin; the warehouse was read from its S3 bytes,
  which are what Trino reads. No `SHOW TABLES` was run.
- **Not claimed: event volume, cost or storage size.** No number is given because none was measured.
- **Not claimed: that hand-off chains join cleanly.** O2 assumes objects carry stable identifiers across people
  (file item ids, internet message ids). The schema suggests they do; it was not tested on our data.
- **Not claimed: legal sufficiency.** Part V names the NY statute; no counsel was consulted.
- **Not checked:** whether an existing third-party archive (for SEC books-and-records) already captures some of this.

---

## REFS

```
  BRIEF PATH        docs/briefs/m365-workflow-activity-spine-brief-20261016.md
  PROJECT           NONE-YET (1.0.0_SA_CTO registers and keys it at L3)
  EXISTING PRD      NONE
  RESEARCH          org/tier1_exec/4.0.0_SA_CRO~XXX/deliverables/M365_WORKFLOW_SPINE_ACCESS_RESEARCH_20261015.md @158eb209d9
  SIBLING PROJECTS  NFRA_GLOBGRPH (warehouse, Trino); NFRA_OPLGTW (gateway, stays delegated); NFRA_MCPINDEX (catalog);
                    transcripts pipeline (owner_pipeline "transcripts"); LGIC (infra/logic/)
  PRIOR ART         MS_FILE snapshot in the served graph; warehouse/ms_heat (2026-07-17); gateway ms_ingest (/ms/*, delegated)
  SOURCE DOCS       https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-reference
                    https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/grant-admin-consent
  MEASURED AT       2026-10-15 23:5xZ .. 2026-10-16 01:2xZ (Part VI per line)
```

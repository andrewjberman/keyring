# TCKT_MTADTA -- Ticket Center metadata: the operations team's Microsoft 365 activity, read as sequences, to find the workflows Ticket Center should absorb (L1 brief, MIDSTREAM)

**Author:** `4.0.0_SA_CRO~XXX` (dell1). **For:** `1.0.0_SA_CTO~DELL1`, `/endpoint --forward` at L2.
**Mode:** `--midstream`. This brief refactors `docs/briefs/m365-workflow-activity-spine-brief-20261016.md` @441e9ca92f (the NFRA_WFSPINE
brief). TCKT_MTADTA supersedes NFRA_WFSPINE; it does not run beside it.
**Ordered by:** `1.0.0_SA_CTO~DELL1`, broker msg 6541 (2026-10-16 06:00Z), on Andrew's two words below.

**Andrew-direct, the laptop `1.0.0_SA_CTO` terminal, ~05:4xZ 2026-10-16, VERBATIM** (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_054xZ_SPINE_BECOMES_TCKT_MTADTA_OPS_EIGHT_DROP_AT_OUTSET_GLOBGRPH_ROLE_ONLY.md`
@0092da40fe):

> I think the M365 spine is actually going to be referenced in the context of ticket-center analytics. We want to track this
> metadata for the sake of monitoring ticket-center-focused operational workflows. i think accordingly this goes under the TCKT
> macro, perhaps a TCKT_MTADTA. I want the application qualified as ticket-center analytics, the premise is that we will identify
> from the sequences what workflows need to be absorbed into ticket center request sequences. Accordingly it should only cover
> operational team members, i.e. andrew@opalinvest.com, alyssa@opalinvest.com, bobby@opalinvest.com, manav@opalinvest.com,
> yang@opalinvest.com, menachem@opalinvest.com, jim@opalinvest.com, jeanette@opalinvest.com. That means that all other
> domains/accounts should be dropped at the outset and not stored. I think this goes in opal-data-trino with the folder being
> m365-metadata. everything is stored in bronze, then silver parquet, then gold analytics tables we will decide upon later when we
> have more data. opal-data-trino should only be viewable by an iam role associated with globgrph group. Therefore, if we want to
> access it, we need to make a call to a lambda with the relevant iam role that will have the role group. If we do it like that, if
> yang or my account was compromised, it would not matter right?

**Andrew-direct, same terminal, ~06:0xZ, VERBATIM** (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_06xxZ_TCKT_MTADTA_KICKOFF_DELL1_ORG_PROJECT_LATER.md` @5dfb4237f5):

> We will have a separate project to set up the organization, for now just set it up in opal-data-trino as described. let's get
> that brief refactored into this tckt center metadata project and kicked off on dell1

**Also carried in:** the laptop CTO's read of exactly what the audit feed holds and the PII in it,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/WFSPINE_AUDIT_CONTENT_AND_PII_20261016.md` @8413c1df38 (cited below as "the PII read").

---

## PART 0 -- HOW THE BLIND CONSTRAINT WAS HONOURED, AND WHERE IT BENT

**Honoured.**
- TCKT_MTADTA has no task orders yet; there was no open set to ratify.
- No NFRA_WFSPINE task order, decomposition, `phase` or `blocking` field was opened.
- The NFRA_WFSPINE PRD's CELL CANDIDATES, PATHS and SURFACE MANIFEST sections were not read.

**Where it bent. Each bend is a place where an outcome that only ratifies existing work could get in:**
1. **I wrote the brief this one refactors.** Its nine outcomes are my own framing. I kept them only where Andrew's two words leave
   them standing, and changed them where his words move them (B1 to B5 below). The risk is that I kept too much of my own framing.
2. **I read the NFRA_WFSPINE PRD's ENDPOINT, CONTRACTS, C-HOMES builder output, DECISIONS and OPEN AT ANDREW** (lines 1-196 at the
   working tree, 2026-10-16 ~06:0xZ). Those sections are the predecessor's purpose and acceptance, which is admissible. But its
   decisions sit close to the branch. Two of them (Decision 3, "bronze is raw"; Decision 4, "the filter sits at bronze to silver") are
   REVERSED by Andrew's 05:4xZ word, and this brief says so in Part IV F9. It does not inherit them.
3. **My inbox listing showed the subject line of a CTO message to `2.0.0_SA_COO~S1`** ("NFRA_WFSPINE re-scoped by Andrew to TCKT").
   I did not open it.

**What changed from the predecessor brief:**
- **B1. Purpose.** The predecessor's purpose was reverse-engineering every workflow to find AI waste reduction. The purpose is now
  Ticket Center analytics: find, from the sequences, which operations workflows should be absorbed into Ticket Center request
  sequences. O5 is rewritten to that end. **Bend, flagged for L2:** AI waste reduction is not named in either of today's words. I read it
  as narrowed into the Ticket Center framing (a workflow absorbed into a request sequence is where AI or automation would then act), not
  as dropped. If Andrew meant it dropped, O5's second sentence goes.
- **B2. Population.** "Who is in" is no longer a default proposal for Andrew to decide later. It is his list of eight accounts, and
  everyone else is dropped at collection and never stored (O7).
- **B3. Home and tiers.** The data goes in `opal-data-trino`, folder `m365-metadata`: bronze, then silver parquet. Gold tables are
  decided later "when we have more data". The outcomes that depend on gold (O3, O4, O5) are still in the territory, but the tables
  that serve them are not designed now (Part V).
- **B4. Access.** The predecessor's O6 had a seat querying through the warehouse's existing Trino surface. That is replaced by access
  only through a Lambda that holds the one role (O6, O8).
- **B5. New outcome O8.** Andrew can confirm that nobody but the role reads the data, and he knows exactly what a compromised account
  still reaches.

**"Unchanged" findings:**
- The thread is still one person's trading day.
- The source (the Office 365 Management Activity API on one new app-only Entra app), the gateway staying delegated-only, and the
  no-alerting rule are all unchanged.

---

## PART I -- THE OUTCOME TERRITORY

**Candidate thread (becomes FWD-1):** Andrew picks one of the eight operations accounts and one recent trading day, calls the access
Lambda, and reads that person's Microsoft 365 day in order.
- Coarse grain: one person, one day, whatever workloads our tenant's audit log emits.
- The data is landed in `opal-data-trino/m365-metadata` bronze and silver, and nothing about any other account is stored.
- Round 1 builds it end to end: the app and its consent; the subscription; the scheduled collector with its drop at collection; bronze;
  silver parquet; the access role and Lambda; and a readable day.
- Every other outcome enriches that thread.

### O1 -- Andrew reads any operations team member's trading day as one ordered timeline
He names one of the eight and a trading day, and reads in time order what that person did in Outlook, Teams, SharePoint and OneDrive:
the action, the object (file, message, meeting) and the time. This is the thread.

### O2 -- Andrew follows a hand-off between operations team members
From any step on a timeline he can see who acted next on the same object (the same file, the same email message, the same meeting)
and jump to that person's timeline at that moment. A chain A -> B -> C reads as one chain. A step that leaves the eight (a mail to
someone outside them) reads as the chain leaving the team, not as a broken chain.

### O3 -- Andrew sees which operations workflows recur
He reads the sequences that repeat across trading days, for one person and across the team, each with the days it occurred on.

### O4 -- Andrew sees where the time goes inside a recurring workflow
For a workflow from O3 he reads the elapsed time between its steps, and he can tell waiting (a hand-off not yet picked up) apart from
doing (consecutive actions by one person).

### O5 -- Andrew receives a ranked list of Ticket Center absorption candidates, each backed by its evidence
- Each candidate names a recurring workflow, the request sequence Ticket Center would carry it as (who asks, who acts, in which order),
  and the timeline chains it was drawn from. He can open the evidence instead of trusting the summary.
- Where a step could be automated or taken over by AI inside that request sequence, the candidate says so (B1).

### O6 -- An authorised seat reads the data only through the access Lambda
A CRO or analyst seat asks its questions (who touched this file this week; which chains start from this mailbox) by invoking the
access Lambda. It has no direct read of the bucket and no bespoke export.

### O7 -- Andrew's eight are the only people collected, and everyone else is never stored
- The eight accounts he named are the population. An event whose actor is anyone else is dropped before anything is written, so it is
  absent from bronze as well as from every derived view.
- Changing the list is his act, and the collector honours a change from the next collection on.

### O8 -- Andrew knows who can read the data, and what a compromised account still reaches
- He can confirm that the bucket refuses every identity except the one access role, admin users included.
- He can confirm who may invoke the Lambda, and what it returns.
- He holds a short, current statement of what a compromise of his account, of Yang's, or of an AWS admin would still expose. That
  statement names the residuals honestly (Part IV F10), including the ones only the later AWS Organization project removes.

### O9 -- Andrew can tell what the collection did not see
- For any day he reads which workloads and event types were collected, and whether collection had a gap.
- A gap the source could no longer fill (it keeps 7 days) shows as a permanent hole, never as a quiet day.

### O10 -- For a workflow he chooses, Andrew reads the document content behind its steps (enrichment; his word on scope)
- For a recurring workflow from O3 he opens the SharePoint or OneDrive documents its steps touched, so "what the task IS" is answered as
  well as "when and by whom".
- Mail and Teams message content are out.
- **Bend, flagged for L2:** this outcome came from the predecessor. Neither of today's words mentions it, and his "dropped at the
  outset and not stored" reasoning may weigh against reading content at all. Kept as territory on his scope word, nothing more.

---

## PART II -- WHERE THE BOUNDARY SITS

**Owns:**
- the new single-purpose Entra app and its one consent;
- the audit-log subscriptions;
- the scheduled collector and its drop at collection;
- `opal-data-trino`, folder `m365-metadata`: bronze and silver now, gold later;
- the bucket policy that refuses everyone but the access role;
- the access role and the access Lambda;
- the coverage record (O9);
- the derived timeline, chain, recurring-workflow and candidate views when gold is decided;
- the compromise statement (O8).

**Relies on, does not own:**
- **TCKT_VNEXT** (D7, the Ticket Center itself: "takes typed requests, the Analysis Request first"). TCKT_MTADTA supplies the evidence
  for which workflows Ticket Center should absorb. Building any request sequence is TCKT_VNEXT's work; this project changes nothing in
  Ticket Center.
- **NFRA_GLOBGRPH.** Andrew ties the access role to "globgrph group". What that means is open (Part IV F8). Whatever it means, GLOBGRPH's
  tables, derive, projection and existing roles are not changed by this project without that project's owner.
- **NFRA_OPLGTW** (the Opal gateway). Its M365 apps stay delegated-only. **This project adds no permission to "M365-MCP-Graph" or
  "M365-MCP-Login".**
- **LGIC** (`infra/logic/`). Homes and names come from `lib/opal_naming` builder output (rule 30). The drop at collection is an R9
  departure, and Andrew's 05:4xZ word is its R20 acknowledgement.
- **The transcripts pipeline** (`opal-data-transcripts`). This project neither merges into it nor replaces it.

**Superseded:** NFRA_WFSPINE (D9, PRD v0.1 DRAFT, no build). Its register row moves at L3; nothing of it runs beside TCKT_MTADTA.

**Explicitly out:**
- **The dedicated AWS Organization and data account.** That is a separate project, to be briefed later. The PRD names it as the planned
  hardening and claims nothing it does not deliver.
- **Any account outside the eight.** Shared mailboxes are out unless Andrew adds one; his list names people only.
- **Mail and Teams content.**
- **The 180-day audit backlog.**
- **Anything off Microsoft.**
- **Alerting.** This is an analysis surface. It raises no alert, alarm or notification on what a person does (standing moratorium).
- **Exchange EWS `full_access_as_app`.**

---

## PART III -- THE QUALITATIVE BAR

- Andrew reads a named teammate's morning and recognises it as what that person actually did, in the right order, without being told.
- A hand-off Andrew already knows about between two of the eight appears as a chain he can follow both ways.
- A workflow the analysis calls recurring is one Andrew agrees recurs. One it misses is one he can show it missed, by pointing at the
  days where the events exist.
- An absorption candidate is specific enough that the TCKT_VNEXT seats could design the request sequence from it, and its evidence
  chains survive Andrew opening them.
- Someone outside the eight is absent from the bucket itself, not only from what the Lambda returns. Searching bronze for them finds
  nothing.
- An identity that is not the access role (an admin user included) is refused when it reads the bucket directly.
- Andrew's compromise statement survives a security reader's challenge. It does not say "would not matter" where it would.
- A day with no events reads either as "no activity collected" with the coverage stated, or as a gap. Never as a silent blank.

---

## PART IV -- THE SUBSTRATE: is this in a canonical pattern?

**F1. Nothing collects this today.** The predecessor brief's F1 is unchanged: no app, subscription, collector or table for the M365
audit log (measured 2026-10-16 ~01:2xZ; Part VI).

**F2. The source and what it carries.** The source is the Office 365 Management Activity API, application permission `ActivityFeed.Read`
on the Office 365 Management APIs resource (not Graph). The PII read gives field lists from Microsoft's published schema, with INVENTED
examples; no Opal record has been collected.
- The feed is TENANT-WIDE, in gzipped JSON content blobs. There is no per-user subscription, so the eight-account population is entirely
  our filter, applied after download (PII read s.1).
- Content is retrievable for about 7 days. The first content arrives up to 12 hours after a subscription starts. Events inside a blob are
  not in time order. A stopped subscription cannot recover its interval.
- **Never in the feed:** mail bodies, attachment contents, document contents, chat message text, call audio (PII read s.4).

**F3. The PII in what is collected, ranked by exposure (PII read s.4).** Dropping the other accounts' EVENTS does not remove other
people's DATA from the eight's own events:
1. mail subject lines (`Item.Subject`): client names, account fragments, money movements;
2. external recipient addresses (`recipientList`, `UserSharedWith`): clients' personal email addresses;
3. file and folder names and paths (`ObjectId`, `SourceFileName`, `Attachments`, `MessageURLs`): household names;
4. IP addresses and device identity (every workload; Entra sign-ins): employees' location over time;
5. chat and team names, and participants (`ChatName`, `Members`);
6. the employee identity and the timeline itself, which IS the monitoring.

**F4. Design levers the PII read proposes (s.5; proposals for L4, not decisions):**
- drop the Entra sign-in feed (`Audit.AzureActiveDirectory`) entirely, since it is location tracking and carries no workflow signal;
- keep `Item.Subject` out, or store a hash of it so a thread still links across people;
- reduce external recipients to their domain;
- keep file ids and extensions, and keep names only for the sites Andrew names;
- store an office/remote flag instead of the raw IP.

  Andrew's "drop at the outset and not stored" sets the precedent that the filter acts before the write. These levers would act at the
  same point, on fields rather than accounts. Whether they apply is his call at L4.

**F5. "On premises" is answered by a list.** The PII read (s.5) set out two readings of his earlier "operational teams on premises":
a list of people, or only activity from the office IP. His 05:4xZ word names a list of eight people, and nothing in it filters by
office IP. Whether that fully closes the IP reading is the CTO's to confirm; this seat does not adjudicate it.

**F6. Who can turn it on.** Andrew holds tenant-wide Cloud Application Administrator (verified 2026-09-14, not re-read). That role can
consent application permissions on any API except Microsoft Graph, which covers `ActivityFeed.Read`. This is inferred from the
published rule, not exercised.

**F7. The home is not built.** `opal-data-trino` does not exist (measured 2026-10-16 ~06:0xZ, Part VI). Two registry rows are owed
before the builder will name its addresses:
- the predecessor PRD's C-HOMES records the builder's refusals at HEAD and two owed rows, a `trino` PRODUCT scope and a vendor source row;
- `lib/opal_naming.py key()` (`:2499`) builds exactly `{source}/{scope}/{tier}/{table}/{partition}`, a grammar Andrew ruled 2026-09-13
  (`org/standards/NAMING_SCHEMA.json` `key.grammar`).
- **Finding for L4:** Andrew's "folder m365-metadata, bronze then silver" reads as `m365-metadata/bronze/...`. The ruled grammar always
  puts a scope segment between the source and the tier, and the predecessor's builder output put the source key `m365audit` first. So
  his folder name is reachable as the SOURCE segment (`_segment` admits a hyphen), giving the form
  `s3://opal-data-trino/m365-metadata/<scope>/bronze/...`. The literal `m365-metadata/bronze/` is not builder output. I did not run the
  builder with an `m365-metadata` row. Whichever row lands, it lands at L4 as builder output, never typed.

**F8. "An IAM role associated with globgrph group": no IAM group by that name exists.** Measured 2026-10-16 ~06:0xZ:
- `aws iam get-group --group-name globgrph` returns NoSuchEntity;
- `aws iam list-groups` returns exactly two groups, `AdministratorAccessOpalCapital` and `cloudops-dell-agents-group`;
- the served AWS graph (`comp-find --corpus aws 'globgrph'`, built 2026-10-16 06:01Z, 117 hits over 2,971 nodes) holds 23 IAM roles
  in the globgrph family (for example `opal-globgrph-serving-task`, `opal-globgrph-derive-runner-task`) and the `globgrph-trino` task
  definition.

  The phrase therefore has at least three readings. This seat does not choose between them:
  - **(a)** a new role this project creates, named and tagged into the globgrph family;
  - **(b)** an existing globgrph role, such as the Trino task role, which would also put the data in reach of the warehouse;
  - **(c)** a new IAM group named globgrph, whose members' role is the reader.

  Whichever reading holds, the role must be the bucket's only reader, and the Lambda holds it. The predecessor's "query through
  `globgrph-trino`" (its C-QUERY) holds only under reading (b).

**F9. Two predecessor decisions are reversed by Andrew's word.**
- The predecessor PRD decided "bronze is raw (R9)" and "the population filter sits at bronze to silver" (its Decisions 3 and 4, and
  C-POPULATION).
- Andrew's 05:4xZ word puts the drop at collection ("dropped at the outset and not stored"). Bronze therefore holds the eight accounts'
  events only. It is not the raw blob.
- This is a deliberate R9 departure, and his word is the R20 acknowledgement (record @5dfb4237f5, item 2).
- **Consequence to name at L4:** a mistake in the population filter cannot be repaired from bronze. An event dropped in error is gone,
  and so is the 7-day window to re-fetch it.

**F10. The compromise answer, as given to Andrew in session** (record @0092da40fe, "The answer given to item 7"): "Not entirely."
- A compromised M365 account does not reach the AWS copy unless that identity federates into AWS.
- Andrew's account holds Cloud Application Administrator. A compromise of it could add a credential to the collector app, consent new
  permissions, or read the tenant's audit log directly from Microsoft, bypassing the S3 copy. Yang's ordinary account cannot.
- "Only the role" holds only if the bucket policy, and ideally a dedicated KMS key, DENY everyone else, admin principals included.
- The Lambda is an access path too: invoke rights and what it returns are part of the control.
- Inside one AWS account, root and IAM admins can still reach the data (record @5dfb4237f5, item 3). Removing that residual is the
  separate AWS Organization project's job.

**F11. Canonical fit.** The estate's pattern for a new data plane is an LGIC-built home with builder names, landed then normalised. This
project fits that pattern with one declared departure: bronze is filtered, not raw (F9). A Lambda as the only read path, and a bucket
readable by one role, are not the estate's usual warehouse pattern. No prior art was searched for a role-only bucket with a Lambda front
door (Part VII).

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- Unified audit logging is on for the tenant.
- Andrew's Cloud Application Administrator assignment is active at consent.
- The new app exists with `ActivityFeed.Read` consented. Its credential is held where the estate holds secrets, and its secret id has
  no builder kind yet (predecessor PRD C-HOMES).
- Collection runs on a schedule, with no unattended gap reaching 7 days.
- The population filter acts BEFORE the first write, against Andrew's eight accounts. It must also handle aliases, display-name changes
  and the actor fields that vary by workload: `UserId`, `MailboxOwnerUPN`, `SendAsUserSmtp`, `SendOnBehalfOfUserSmtp`.
- **The rule for an event acted on BY one of the eight that NAMES someone outside them** (a recipient, a sharee, a chat member) is
  needed. Andrew's word drops other accounts' events; it does not say whether outsiders' addresses inside the eight's events are kept,
  reduced (F4) or dropped. His call.
- The LGIC registry rows admit `opal-data-trino` and the `m365-metadata` folder (F7). Any refusal is a missing row, never a typed name.
- **The bucket's write path and its read path:**
  - The collector must WRITE bronze and silver.
  - Andrew's word names one role as the only one that can VIEW the bucket.
  - Whether the collector runs as that same role, or as a writer the policy also admits, is an L4 design point. It must not quietly
    widen "only viewable by" into "readable by the collector too".
- The bucket name `opal-data-trino` is unclaimed today (Part VI). S3 names are global, so until it is created, anyone could claim it.
- Gold analytics tables are decided "later when we have more data". Until then, O3 to O5 have no serving tables, and how many trading
  days is enough is a later measurement, not a number set here.
- Andrew's word on content scope before O10 reads anything.
- Employee notice. New York Civil Rights Law s.52-c requires written, acknowledged notice of email and internet monitoring for an
  employer with a NY place of business. The eight are now named; whether the notice applies and is already covered is Andrew's and
  counsel's to settle. This is named as a fact, not a gate.
- Event records carry client names and personal addresses (F3), which can be Reg S-P customer information. They land only in
  `opal-data-trino` under the estate's client-data rules. No raw capture enters the repository, and tests use synthetic events.

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-16 ~06:0xZ, `cloudops-dell1-agent-user`, unless stated.
- **`opal-data-trino`: does not exist.** `get-bucket-location`, `get-bucket-policy`, `get-bucket-encryption` and `ls` all returned
  NoSuchBucket. Positive control in the same session: `get-bucket-location` on `opal-313476888478-globgrph` succeeded.
- **IAM group `globgrph`: does not exist** (NoSuchEntity). The account has two IAM groups (F8).
- **The served AWS graph**, built 2026-10-16 06:01:06Z, holds 23 globgrph-family IAM roles and 4 globgrph-named S3 buckets.
- **No app, subscription, collector or table for the M365 audit log** (predecessor brief F1, measured 2026-10-16 ~01:2xZ; not re-read).
- **NFRA_WFSPINE:** PRD v0.1 DRAFT, `dep_stage` PRD, `status` active in `project.json` (read ~06:0xZ). Nothing built.
- **TCKT macro:** one member today, TCKT_VNEXT (D7). The TCKT_MTADTA register row is the CTO's L3 act.
- **Andrew's role:** verified 2026-09-14, not re-read.
- **Unmeasured:** whether audit logging is on, the licence tier, which mail and Teams events are emitted, and per-person volume.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **Not claimed: which globgrph reading Andrew meant** (F8). This seat surfaces three readings and does not pick one.
- **Not claimed: the builder's output for `m365-metadata`** (F7). The grammar was read; the builder was not run with that row.
- **Not claimed: that the consent works.** Inferred from Microsoft's published rule; nothing was registered or consented.
- **Not claimed: which events our tenant emits, or their volume.** The PII read's examples are invented. Its s.6 names two ways to see
  real Opal records: a Purview export by Andrew, or a one-hour quarantined sample. The sample ends in a deletion that needs his
  confirmation.
- **Not claimed: that the population filter can be exact.** Whether every workload's actor field resolves cleanly to the eight UPNs
  (aliases, send-as, delegated mailboxes) is unmeasured.
- **Not claimed: that hand-off chains join cleanly** inside an eight-person population. Chains that pass outside the team break at the
  boundary by construction (O2).
- **Not claimed: that "would not matter" is true.** F10 says it is not entirely true; the residuals are stated, not solved.
- **Not checked:** prior art in the estate for a role-only bucket behind a Lambda (F11); whether a third-party SEC books-and-records
  archive already captures some of this.
- **Not claimed: legal sufficiency.** No counsel was consulted.

---

## REFS

```
  BRIEF PATH        docs/briefs/tckt-mtadta-ticket-center-metadata-brief-20261016.md
  PROJECT           TCKT_MTADTA (NONE-YET in the register; 1.0.0_SA_CTO~DELL1 registers it at L3 and supersedes NFRA_WFSPINE)
  REFACTORS         docs/briefs/m365-workflow-activity-spine-brief-20261016.md @441e9ca92f
  EXISTING PRD      NONE for TCKT_MTADTA; predecessor org/missions/D9/NFRA/NFRA_WFSPINE/prd/NFRA_WFSPINE_PRD.md (v0.1 DRAFT)
  ANDREW RECORDS    org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_054xZ_SPINE_BECOMES_TCKT_MTADTA_OPS_EIGHT_DROP_AT_OUTSET_GLOBGRPH_ROLE_ONLY.md @0092da40fe
                    org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_06xxZ_TCKT_MTADTA_KICKOFF_DELL1_ORG_PROJECT_LATER.md @5dfb4237f5
                    org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_040xZ_WFSPINE_BUCKET_OPAL_DATA_TRINO.md @4d1e860753
  PII READ          org/tier1_exec/1.0.0_SA_CTO/deliverables/WFSPINE_AUDIT_CONTENT_AND_PII_20261016.md @8413c1df38
  RESEARCH          org/tier1_exec/4.0.0_SA_CRO~XXX/deliverables/M365_WORKFLOW_SPINE_ACCESS_RESEARCH_20261015.md @158eb209d9
  SIBLING PROJECTS  TCKT_VNEXT (Ticket Center, D7); NFRA_GLOBGRPH (globgrph roles, warehouse); NFRA_OPLGTW (gateway, stays delegated);
                    LGIC (infra/logic/); transcripts pipeline; the AWS Organization project (NOT YET BRIEFED, out of scope)
  PRIOR ART         predecessor PRD C-HOMES builder output and owed registry rows; MS_FILE snapshot in the served graph;
                    warehouse/ms_heat (2026-07-17)
  SOURCE DOCS       https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-reference
                    https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-schema
  MEASURED AT       2026-10-16 ~06:0xZ (Part VI per line); predecessor measurements 2026-10-15 23:5xZ .. 2026-10-16 01:2xZ
```

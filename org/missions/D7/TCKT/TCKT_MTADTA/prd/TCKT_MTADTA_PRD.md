# TCKT_MTADTA -- Ticket Center metadata: the eight operations team members' Microsoft 365 activity, read as sequences, to find the workflows Ticket Center should absorb

```json
{
 "project": "TCKT_MTADTA",
 "directive": "D7",
 "fabric": "dell1",
 "prd_version": "v0.5",
 "step": 4,
 "brief_ref": "docs/briefs/tckt-mtadta-ticket-center-metadata-brief-20261016.md@4ec9c9f461",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9", "FWD-10"],
 "status": "DRAFT"
}
```

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-16 ~06:3xZ.
**Placement:** DELL1, directive D7, macro TCKT. This is a per-member exception to D7's DELL2 placement, on Andrew's word "kicked off on dell1".
Registered @8579e53ae3.
**Supersedes:** NFRA_WFSPINE (D9). It is closed with nothing built, and its PRD v0.1 was refused by the CVO and never signed.

**Records (Andrew-direct, the laptop `1.0.0_SA_CTO` terminal, all under `org/tier1_exec/1.0.0_SA_CTO/deliverables/`):**
- **scope, population, home, access:** `ANDREW_DIRECT_20261016_054xZ_SPINE_BECOMES_TCKT_MTADTA_OPS_EIGHT_DROP_AT_OUTSET_GLOBGRPH_ROLE_ONLY.md`
  @0092da40fe. It includes "all other domains/accounts should be dropped at the outset and not stored".
- **placement, and the AWS Organization out of scope:** `ANDREW_DIRECT_20261016_06xxZ_TCKT_MTADTA_KICKOFF_DELL1_ORG_PROJECT_LATER.md`
  @5dfb4237f5. It includes "We will have a separate project to set up the organization, for now just set it up in opal-data-trino as
  described".
- **DONE WHEN confirmed, and access:** `ANDREW_DIRECT_20261016_062xZ_TCKT_MTADTA_ENDPOINT_CONFIRMED_GLOBGRPH_GROUP_READER_WRITER_LAMBDA.md`
  @f4fbcdfde4: "yes, only iam globgrph group can access, if you want to access you have to go through the reader/writer lambda".
- **the bucket:** `ANDREW_DIRECT_20261016_040xZ_WFSPINE_BUCKET_OPAL_DATA_TRINO.md` @4d1e860753: "its a product folder so follows product
  rules".

**Also read:**
- `WFSPINE_AUDIT_CONTENT_AND_PII_20261016.md` @8413c1df38, the PII read.
- `org/tier1_exec/3.0.0_SA_CVO/deliverables/L4R_REVIEW_NFRA_WFSPINE_v0.1_RATIFIED_TEXT_20261016.md`, the predecessor's refusal. C-POPULATION
  below closes it: the drop is at collection and the endpoint says "not even in the first copy written".

## ENDPOINT (step 2, /endpoint --forward)

Confirmed by Andrew 2026-10-16 ~06:2xZ ("yes"). Source: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_TCKT_MTADTA_20261016.md`
@a7a7df4e6f, copied verbatim.

```
  FWD-1  Andrew picks one of the eight operations team members and a trading day, and reads that person's
         Microsoft 365 day in order, from collection that is actually running
         DONE WHEN  EXERCISED -- one real person's real day, read end to end
         ACCEPT     Andrew names a teammate from his list and a recent trading day, reads what they did in mail,
                    Teams, SharePoint and OneDrive in time order, and recognises it as that person's day; nothing
                    on the page was typed in by hand
         SOURCE     brief Part I, candidate thread and O1

  FWD-2  From any step, Andrew can follow a hand-off to the next teammate who touched the same thing
         DONE WHEN  EXERCISED -- a hand-off Andrew already knows about is followed both ways
         ACCEPT     a file or email Andrew knows passed from one teammate to another shows as one chain he can
                    walk forward and back; when it goes to someone outside the team, it reads as leaving the team,
                    not as a break
         SOURCE     brief O2; Part III bullet 2

  FWD-3  Andrew can see which operations workflows recur, for one person and across the team
         DONE WHEN  EXERCISED -- a list of recurring workflows Andrew has reviewed
         ACCEPT     each workflow it calls recurring is one Andrew agrees recurs; for one it misses, he can point
                    to the days where it happened
         SOURCE     brief O3; Part III bullet 3

  FWD-4  For a recurring workflow, Andrew can see where the time goes between its steps
         DONE WHEN  EXERCISED -- one workflow's timing read by Andrew
         ACCEPT     he can tell time spent waiting for a teammate apart from time spent working, and the split
                    matches what he knows of that workflow
         SOURCE     brief O4

  FWD-5  Andrew receives a ranked list of workflows Ticket Center should take over, each with its evidence
         DONE WHEN  EXERCISED -- Andrew has read the list and opened the evidence behind at least one item
         ACCEPT     each item names the workflow and how Ticket Center would run it as a request (who asks, who
                    does what, in which order), and says where a step could be automated; it is specific enough
                    for the Ticket Center team to build from, and its examples hold up when Andrew opens them
         SOURCE     brief O5; Part III bullet 4

  FWD-6  An approved research seat gets its answers only by asking through the one front door
         DONE WHEN  EXERCISED -- one real question answered through the front door
         ACCEPT     an analyst asks who on the team touched a given file this week and gets the answer by asking
                    the front door; it cannot open the stored data any other way, and nobody prepares a file for it
         SOURCE     brief O6; Andrew 05:4xZ "make a call to a lambda"

  FWD-7  Only Andrew's eight are collected, and nobody else is ever stored
         DONE WHEN  EXERCISED -- someone outside the eight is searched for in the stored data and not found
         ACCEPT     a colleague who is not on Andrew's list does not appear anywhere in what is kept, not even in
                    the first copy written; when Andrew changes the list, the next collection follows it
         SOURCE     brief O7; Andrew 05:4xZ "dropped at the outset and not stored"

  FWD-8  Andrew knows who can read the data, and what a stolen login would still reach
         DONE WHEN  EXERCISED -- a direct read by an admin is tried and refused, and Andrew has read the statement
         ACCEPT     anyone other than the one approved reader, admins included, is turned away when they try to
                    open the stored data directly; Andrew holds a short statement, current and honest, of what a
                    stolen login for him, for Yang or for an admin would still expose, including what only the
                    later separate-account project removes
         SOURCE     brief O8, Part IV F10; Andrew 05:4xZ "if yang or my account was compromised"

  FWD-9  For any day, Andrew can see what the collection did not see
         DONE WHEN  EXERCISED -- a day with a known gap shows the gap
         ACCEPT     a quiet day and a day collection missed never look the same; a missed day too old to recover
                    is marked as lost for good
         SOURCE     brief O9; Part III bullet 8

  FWD-10 For a workflow he chooses, Andrew can read the documents behind its steps
         DONE WHEN  EXERCISED -- one chosen workflow's documents read in place
         ACCEPT     Andrew opens a recurring workflow and reads what the documents it touched actually say, within
                    the scope he agreed; email and Teams message content are not part of this
         SOURCE     brief O10 (carried from the predecessor; waits on his word on scope)
```

## CONTRACTS

| row | owner | rule | proven by |
|---|---|---|---|
| C-APP | `1.0.0_SA_CTO~DELL1` (design); Andrew (the consent) | ONE new single-purpose Entra app holds `ActivityFeed.Read` on the Office 365 Management APIs (not Graph), app-only, consented ONCE by Andrew as Cloud Application Administrator. The gateway's `M365-MCP-Graph` and `M365-MCP-Login` stay delegated-only, with NO permission added. | the app's granted permissions read back (one permission, admin-consented); the gateway apps' permission lists read unchanged before and after |
| C-SECRET | the round-1 app cell | The app credential lives in the estate's secret store, read by id at run time. It is never printed, logged, written to the repo or committed. Its id is graded by the LGIC grader (C-HOMES); no builder function emits secret ids. | a run log that names the secret id and prints no value; repo census for the value = 0 |
| C-POPULATION | Andrew sets the list; the collector enforces it | FWD-7. The population is exactly these eight UPNs: `andrew@opalinvest.com`, `alyssa@opalinvest.com`, `bobby@opalinvest.com`, `manav@opalinvest.com`, `yang@opalinvest.com`, `menachem@opalinvest.com`, `jim@opalinvest.com`, `jeanette@opalinvest.com`. The filter runs in the collector, in memory, BEFORE THE FIRST WRITE: an event is written to bronze only when its actor resolves to one of the eight. The actor is resolved across `UserId`, `MailboxOwnerUPN`, `SendAsUserSmtp` and `SendOnBehalfOfUserSmtp`, case-insensitively, against the eight UPNs. No Entra object id is read: the app holds one permission (C-APP), and reading ids would need a Graph directory permission. An actor recorded only as an id is dropped and counted; the count is read on the first real content, and a non-zero count goes to the next analysis (row D1-S2; v0.3). An event whose actor does not resolve is DROPPED and COUNTED per workload in the coverage record; it is never written. The list lives in one config value. A change takes effect from the next collection and is recorded with Andrew's word. | a planted out-of-population event is absent from bronze, silver and every derived view; the drop counter reads it; a census of bronze for a non-member UPN = 0 |
| C-FIELDS | the collector cell; Andrew may reverse each lever (OPEN AT ANDREW) | Applied at the same point as the population filter, before the first write. (a) The Entra sign-in feed `Audit.AzureActiveDirectory` is not subscribed. (b) A mail subject is stored only as a keyed hash; the key sits in the secret store, so a thread still links across people. (c) Every address that is not one of the eight, internal (@opalinvest.com) or external, recipient, sharee, chat member or guest, is replaced before the first write by a class token: `internal-other` or `external`. No address and no external domain is stored. The eight's own addresses are kept. (d) The raw IP is replaced by an office/remote flag against Opal's office egress addresses. (e) File ids, extensions, site and file names are kept, because FWD-5's evidence needs them. Each lever can be relaxed later; a field once stored cannot be un-stored. | a planted event carrying a subject, an INTERNAL recipient outside the eight, an external recipient and an IP lands with the hash, `internal-other`, `external` and the flag, and no raw value; a search of everything stored for the planted internal address finds nothing; no `Audit.AzureActiveDirectory` subscription exists |
| C-COLLECT | the collector cell | A SCHEDULED collector, on cadence `hourly` (production pipelines are scheduled; an ad-hoc run is QA only). It lists available content per content type (`Audit.Exchange`, `Audit.SharePoint`, `Audit.General`) and fetches each blob once. Events arrive out of time order and are sorted on landing. **No unattended gap may reach 7 days** (the source keeps 7). The collector WRITES THROUGH the access Lambda (C-ACCESS); it holds no S3 permission of its own. | the scheduled rule read back; two consecutive scheduled fires landing content; a planted 1-hour pause recovered on the next fire |
| C-ACCESS | `1.0.0_SA_CTO~DELL1` (design); the access cell | FWD-6 and FWD-8, on Andrew's 06:2xZ word. (1) A NEW IAM group (builder: `globgrph-trino-access-group`). Its members may invoke the access Lambda, and so may exactly one non-member: the collector's execution role, on its own alias. On that alias the door allows exactly three operations: `put`; `derive_silver`, which returns a row count and no data; and `get_state` on the subscription-cursor key alone, which holds blob ids and a timestamp and no person data. Every other read is refused. Each alias's resource policy admits exactly its one principal (the group's members on theirs, the collector role on its own), and the door decides from the invoked alias (row D1-S5; v0.3; ops widened v0.4 on msg 6589). **On the members' alias the door serves read, write and ops (v0.5, on Andrew's 15:3xZ word, "read/write/do ops in there, and if we want to know things about it, we drive/query that lambda"):** the reads (`get_day`, `get_state`, `list_state`, `derive_silver`); a write (`put`), which runs the same C-POPULATION drop and C-FIELDS levers as the collector's put before any byte is stored; the maintenance ops (re-derive silver or coverage over a date range, and re-collect a window still inside the source's 7 days, through the same filter); and FWD-6's question op. No op deletes stored data: a deletion is irreversible and no outcome needs it, so it is built only on his naming it. (2) ONE reader/writer Lambda (builder: `globgrph-trino-access-lambda`) is the only door for reading and writing. (3) Its execution role (builder: `globgrph-trino-access-role`) is the ONLY principal the bucket policy admits. Every other principal gets an explicit Deny on every object data action (get, put, delete and their variants), IAM admin users and the account's other roles included. `s3:ListBucket` is NOT denied, so Terraform can still refresh the bucket: a listing shows only table names, dates and sizes, because no key segment may carry a person, an address or a file name (row D1-S4; v0.3). (4) A dedicated KMS key encrypts the bucket, and its key policy admits the same role alone. A bucket policy cannot name an IAM group as a principal, so the group gates who may invoke and the role gates the bucket. The Lambda returns query results, never raw bronze objects, and every call is logged. | a direct `GetObject` by an admin user is refused; a non-member's invoke is refused; the collector role's read of any key but the cursor is refused, and a member cannot invoke the collector alias; a member's invoke answers one question; the bucket policy and key policy read back with one admitted principal |
| C-RESIDUAL | `1.0.0_SA_CTO~DELL1` (the statement); Andrew (reads it) | FWD-8's statement says plainly what C-ACCESS does NOT stop, inside one AWS account: (1) the root user; (2) any principal that can edit the bucket policy, the key policy, the Lambda's code or its role (IAM administrators, including Andrew's AWS user), because it can grant itself in; (3) Andrew's M365 account, which as Cloud Application Administrator could add a credential to the collector app, consent new permissions, or read the tenant audit log directly from Microsoft, bypassing the copy here (Yang's ordinary account cannot); (4) anyone added to the group, who from v0.5 can also write and run maintenance ops through the door (every write still passes the population drop and the field levers, so no outsider and no dropped field can be stored, but a member can add or re-derive records); (6) the collector's execution role, a path through the door limited to put, derive_silver and the cursor read; (7) anyone with `s3:ListBucket`, who sees table names, dates and sizes only; (5) file and folder names, which C-FIELDS (e) keeps for FWD-5's evidence and which can carry the names of colleagues outside the eight and of clients. Removing (1) and (2) is the separate, later AWS Organization project. This PRD claims nothing it does not deliver. | the statement exists, is dated, and names each residual; a security reader's challenge leaves no "would not matter" claim standing |
| C-HOMES | `1.0.0_SA_CTO~DELL1` | Every address and name is `lib/opal_naming` output (CLAUDE.md rule 30); no hand-typed name. Bucket `opal-data-trino` is a PRODUCT home ("its a product folder so follows product rules"). Two registry rows are owed in round 1 (below). | builder output pasted below; `validate()` clean with the rows added |
| C-COVERAGE | the collector cell | FWD-9. Every fire writes the coverage record: per day and content type, whether content was listed and fetched, any gap, and the population drop count. A gap older than 7 days is written LOST. A day with no events reads "no activity collected", with the coverage beside it, never blank. | a planted gap reads as a gap; a quiet day reads as quiet; a gap past 7 days reads LOST |
| C-CONTENT | Andrew (scope); a later cell | FWD-10. SharePoint and OneDrive documents only, only for workflows Andrew names, and only after his word on scope. Mail and Teams message content are OUT. | his scope word recorded before any content read |
| C-NOALERT | all | Nothing in this project raises an alert, alarm or notification on what a person does (standing moratorium). It is an analysis surface. | no alarm, SNS or notification resource in the project's Terraform |
| C-CLIENTDATA | all | The eight's events still name clients and outsiders in file and folder names (C-FIELDS (e)); addresses are reduced to class tokens (C-FIELDS (c)). They land only in `opal-data-trino`. No raw capture enters the repository; tests use synthetic events. | repo census for raw event payloads = 0 |
| C-TCKT | TCKT_MTADTA supplies; TCKT_VNEXT builds | FWD-5's candidates are evidence for TCKT_VNEXT. Nothing in this project changes Ticket Center. | no TCKT_VNEXT path in any TCKT_MTADTA order |

### C-HOMES: the builder output (Rule 30)

**At HEAD, the builder refuses** (run 2026-10-16 ~06:3xZ, `lib/opal_naming.py` at this tree):

```
address('m365-metadata','trino','bronze','audit_events','date=20261016', object='events.json.gz')
  -> ValueError: source 'm365-metadata' is not a systems.json key
name('m365-metadata', None, 'trino-collector', 'lambda')
  -> ValueError: system 'm365-metadata' is not a systems.json key (nor the reserved opal)
grade('opal-data-trino', 'S3_BUCKET')
  -> RaiseDefect: B2: 'trino' after opal-data- is no scope key
```

**At HEAD, the builder already emits the access names:** `globgrph` is a systems.json key.

```
name('globgrph', None, 'trino-access', 'group')   -> globgrph-trino-access-group
name('globgrph', None, 'trino-access', 'lambda')  -> globgrph-trino-access-lambda
name('globgrph', None, 'trino-access', 'role')    -> globgrph-trino-access-role
```

**The two registry rows owed** (round 1, cell 1; registry rows in `infra/logic/registry/`, the LGIC owner's lane):
1. `scopes.json`: `{"key": "trino", "class": "PRODUCT", "long": "trino", "short": "trino", "tenancy": "GENERAL", "bucket": "opal-data-trino",
   "bucket_provisioned": false}`, with a note citing Andrew's words.
   - Class PRODUCT is his word.
   - Tenancy GENERAL: this is employee activity metadata, not client custodial information (doctrine R4 as narrowed 2026-09-18). It has the
     same shape as the `transcripts` row.
2. `systems.json`: a VENDOR source row `{"key": "m365-metadata", "class": "VENDOR", "long": "microsoft-365-metadata", "display_name": "Office 365
   Management Activity API", "owner_directive": "D7"}`.
   - The key is Andrew's folder word. The ruled key grammar is `{source}/{scope}/{tier}/{table}/{partition}`, so his folder lands as the SOURCE
     segment (brief F7). The literal `m365-metadata/bronze/` is not reachable.

**With those two rows, the builder's output** (run on a scratch copy of the registry with exactly these two rows added; `validate()` returned 0
refusals and 0 warnings):

```
address('m365-metadata','trino','bronze','audit_events','date=20261016', object='events.json.gz')
  -> s3://opal-data-trino/m365-metadata/trino/bronze/audit_events/date=20261016/events.json.gz
address('m365-metadata','trino','silver','activity_events','date=2026-10-16', object='data.parquet')
  -> s3://opal-data-trino/m365-metadata/trino/silver/activity_events/date=2026-10-16/data.parquet
address('m365-metadata','trino','state','subscription_cursor','current', object='cursor.json')
  -> s3://opal-data-trino/m365-metadata/trino/state/subscription_cursor/current/cursor.json
address('m365-metadata','trino','gold','collection_coverage','date=2026-10-16', object='data.parquet')
  -> s3://opal-data-trino/m365-metadata/trino/gold/collection_coverage/date=2026-10-16/data.parquet
address('m365-metadata','trino','gold','person_day_timeline','date=2026-10-16', object='data.parquet')
  -> s3://opal-data-trino/m365-metadata/trino/gold/person_day_timeline/date=2026-10-16/data.parquet
name('m365-metadata', None, 'trino-collector', 'lambda')  -> m365-metadata-trino-collector-lambda
name('m365-metadata', None, 'trino-collector', 'hourly')  -> m365-metadata-trino-collector-hourly
grade('opal-data-trino', 'S3_BUCKET')                      -> ('CONFORMANT', 'opal-data-trino')
grade('m365-metadata/trino/api-credentials', 'SECRET')     -> ('CONFORMANT', 'm365-metadata/trino/api-credentials')
```

**Further refusal, recorded rather than worked around:**

```
name('m365-metadata', None, 'trino-access', 'key')
  -> ValueError: kind 'key' is neither a NAMING_SCHEMA.json kind nor a cadence
```

- **The KMS key has no builder kind.** Either `org/standards/NAMING_SCHEMA.json` gains a key kind (a schema row; LGIC's owner decides), or the
  key is named as a declared R20 departure. Round 1, cell 1 settles which. This is the one name this PRD does not fix.
- **The secret id:** no builder function emits secret ids. The id above is graded CONFORMANT by `grade()`, the estate's grader for the SECRET
  grammar `{system}/{scope}/{purpose}`. Cell 1 re-grades it after the rows land.
- **The table segments** (`audit_events`, `activity_events`, `subscription_cursor`, `collection_coverage`, `person_day_timeline`) are this PRD's
  proposal; the builder accepted them as written. The other gold tables are decided "later when we have more data".

## THE DECISIONS -- CLOSED AT L4

1. **The drop at collection, an R9 departure.** Bronze holds only the eight's events, after the C-FIELDS levers. It is not the raw blob.
   - Grounds: Andrew's 05:4xZ word, "dropped at the outset and not stored". It is his acknowledgement of the R20 entry, which is owed in
     round 1, cell 1, in the LGIC R20 register.
   - Consequence, stated: a population or field error cannot be repaired from bronze. An event dropped in error is gone, together with the
     source's 7-day window to fetch it again. Cell 4's planted-event proof is the guard.
2. **The access design, on Andrew's 06:2xZ word:** a new IAM group gates invoke; one reader/writer Lambda is the only door; its role is the
   bucket's and the key's only admitted principal; the collector writes through it.
   - "globgrph group" is read as brief F8 reading (a) refined: a NEW group and role in the globgrph naming family (builder output above).
   - It is NOT reading (b): an existing globgrph role, such as the Trino task role, would put the data in the warehouse's reach, against
     "only".
   - The group is (c) in name; its members gate invoke, and the role gates the bucket.
3. **Conservative field defaults (C-FIELDS).** A dropped field can be added later; a stored field cannot be un-stored. Andrew may relax any
   lever (OPEN AT ANDREW). That confirmation does not block round 1.
4. **Bucket `opal-data-trino`, PRODUCT class, GENERAL tenancy, every tier in the one bucket.** Source segment `m365-metadata` (Andrew's
   folder word, under the ruled grammar).
2a. **Members read, write and run ops through the door (v0.5).** Andrew-direct at the `2.0.0_SA_COO~S1` terminal ~15:3xZ, recorded at
   `org/tier1_exec/2.0.0_SA_COO~S1/ANDREW_DIRECT_20261016_153xZ_TCKT_MTADTA_GROUP_READ_WRITE_OPS_THROUGH_THE_LAMBDA.md`. The members'
   alias gains `put` and the maintenance ops under C-ACCESS. FWD-6's question op moves into the next round rather than waiting for its
   own round. Every write passes the same filter as the collector's. There is still no delete op. No principal outside the group gains
   anything.
5. **Hourly scheduled collection** with a state cursor. An unattended gap of 7 days or more is a permanent loss, written as one.
6. **No alerting, ever** (moratorium).
7. **Out of scope:**
   - mail and Teams message content;
   - the 180-day audit backlog;
   - anything off Microsoft;
   - Exchange EWS `full_access_as_app`;
   - accounts outside the eight, shared mailboxes included unless Andrew adds one;
   - the AWS Organization and data account, a separate later project.

## OPEN AT ANDREW (acts only he can do)

- **The consent:** granting `ActivityFeed.Read` to the new app, as Cloud Application Administrator. His role is assumed active; it was last
  verified 2026-09-14.
- **The C-FIELDS levers (a)-(e):** confirm, or reverse any one. Round 1 builds on the defaults.
- **External domains (C-FIELDS (c)):** v0.2 stores no external domain, reading "all other domains/accounts should be dropped at the outset"
  literally. Keeping the domain only (for example a custodian's) would help FWD-5 name who a workflow leaves the team for. His word
  relaxes it; until then, none is stored.
- **A real sample before design hardens (optional):**
  - Either a Purview audit export (one ops person, one day; needs the Audit Reader role),
  - or a one-hour quarantined sample at cell 3 that is profiled and then deleted. The deletion is his confirmation.
- **The content scope (FWD-10),** when that outcome comes up.
- **Employee notice.** New York Civil Rights Law s.52-c requires written, acknowledged notice of email and internet monitoring for an employer
  with a NY place of business. Whether it applies to the eight, and whether it is already covered, is his and counsel's. It is named here as a
  fact, not a gate.

## CELL CANDIDATES

**Round 1 builds the FWD-1 thread, hop by hop (spine v3.16).** It is one live journey: Andrew reads one of the eight's real trading day through
the front door. A build cell carries at most three mechanical criteria.
1. **Rows and home.** The two registry rows, the R20 entry for the drop at collection, and the KMS key-name question. Then `opal-data-trino`
   is provisioned through Terraform (`safe-apply`), with its policy and key per C-ACCESS.
2. **Access.** The group, the reader/writer Lambda and its role. The admin direct-read refusal is proven (FWD-8's first half).
3. **App, consent and subscription.** The Entra app is registered and Andrew is asked for consent (his act). The credential goes to the
   secret store. Subscriptions start for three content types; the first content may take up to 12 hours.
4. **The scheduled collector.** The `hourly` collector applies the population filter and the field levers before the first write, writes
   through the Lambda to bronze, and writes the cursor and the coverage record. A planted out-of-population event is proven absent
   (FWD-7).
5. **Silver and one readable day.** Bronze becomes silver, sorted. One of the eight's trading days is rendered for Andrew through the Lambda
   (FWD-1's EXERCISED bar).

**Later rounds (enrichment):**
- the FWD-9 coverage reads and the FWD-8 compromise statement;
- then FWD-2 chains, FWD-3 recurring workflows, FWD-4 timing and FWD-6 analyst questions;
- then FWD-5 candidates, once gold is decided;
- FWD-10 content, on his word.

## PATHS

- `org/missions/D7/TCKT/TCKT_MTADTA/**`: the project tree.
- `infra/logic/registry/scopes.json` and `systems.json`: the two rows only.
- The LGIC R20 register entry for the drop at collection.
- A new code home for the collector, the access Lambda and the derive, placed by the LGIC code-home rule (R16) at cell 1.
- `infra/aws/terraform/<root named at cell 1>/`: the bucket and its policy, the KMS key, the group, the Lambda and its role, the collector and
  its schedule, and the secret reference.
- `s3://opal-data-trino/m365-metadata/trino/**`: runtime.

## BRIEF COVERAGE

| brief | here |
|---|---|
| O1, candidate thread | FWD-1 |
| O2 | FWD-2 |
| O3 | FWD-3 |
| O4 | FWD-4 |
| O5 | FWD-5, C-TCKT |
| O6 | FWD-6, C-ACCESS |
| O7 | FWD-7, C-POPULATION |
| O8 | FWD-8, C-ACCESS, C-RESIDUAL |
| O9 | FWD-9, C-COVERAGE |
| O10 | FWD-10, C-CONTENT |
| F3, F4 (PII and its levers) | C-FIELDS; OPEN AT ANDREW |
| F5 ("on premises") | the list of eight, confirmed with the endpoint |
| F7 (key grammar) | C-HOMES, source segment `m365-metadata` |
| F8 (globgrph readings) | DECISION 2 |
| F9 (R9 departure) | DECISION 1 |
| F10 (compromise answer) | C-RESIDUAL |
| Part II owns | C-APP, C-COLLECT, C-HOMES, C-ACCESS, C-COVERAGE, C-POPULATION |
| Part II relies on (TCKT_VNEXT, GLOBGRPH, OPLGTW, LGIC, transcripts) | C-TCKT; DECISION 2 (no existing globgrph role used); C-APP (the gateway unchanged); C-HOMES |
| Part II out | DECISION 7 |
| Part V (audit logging on, role active, outsiders named inside insiders' events, write/read path, notice) | cell 3 reads whether audit logging is on; C-FIELDS (c); C-ACCESS (the collector writes through the Lambda); OPEN AT ANDREW |

## SURFACE MANIFEST

| surface | kind | cell | owner |
|---|---|---|---|
| `infra/logic/registry/scopes.json` (row `trino`) and `systems.json` (row `m365-metadata`) | NEW registry rows | R1 C1 | TCKT_MTADTA |
| the LGIC R20 register entry (drop at collection) | NEW register entry | R1 C1 | TCKT_MTADTA |
| bucket `opal-data-trino`, its bucket policy and its KMS key | NEW bucket (Terraform, `safe-apply`) | R1 C1 | TCKT_MTADTA |
| `globgrph-trino-access-group`, `globgrph-trino-access-lambda`, `globgrph-trino-access-role` | NEW access path | R1 C2 | TCKT_MTADTA |
| the Entra app with `ActivityFeed.Read` (app-only) and its secret `m365-metadata/trino/api-credentials` | NEW identity; the consent is Andrew's act | R1 C3 | TCKT_MTADTA |
| the Office 365 Management Activity API subscriptions (3 content types) | NEW vendor subscription, read-only | R1 C3 | TCKT_MTADTA |
| `m365-metadata-trino-collector-lambda`, `-hourly` | NEW scheduled collector | R1 C4 | TCKT_MTADTA |
| `s3://opal-data-trino/m365-metadata/trino/{bronze,silver,state}/` and `gold/collection_coverage/` | NEW data planes | R1 C4-C5 | TCKT_MTADTA |
| `s3://opal-data-trino/m365-metadata/trino/gold/person_day_timeline/` | NEW derived view | R1 C5 | TCKT_MTADTA |
| `org/missions/D7/TCKT/TCKT_MTADTA/deliverables/` | documents | all | TCKT_MTADTA |
| the gateway's `M365-MCP-Graph` and `M365-MCP-Login`; NFRA_GLOBGRPH's tables and roles; TCKT_VNEXT; `opal-data-transcripts`; any firm bucket; `opal-data-assets` | excluded | -- | untouched |

-- 1.0.0_SA_CTO~DELL1

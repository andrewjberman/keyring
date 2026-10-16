# NFRA_WFSPINE -- the M365 workflow activity spine: every employee's Microsoft 365 actions as one timeline, to find recurring workflows and where AI can remove work

```json
{
 "project": "NFRA_WFSPINE",
 "directive": "D9",
 "fabric": "dell1",
 "prd_version": "v0.1",
 "step": 4,
 "brief_ref": "docs/briefs/m365-workflow-activity-spine-brief-20261016.md@441e9ca92f",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9"],
 "status": "DRAFT"
}
```

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-16 ~04:1xZ. **Placement:** DELL1, directive D9, macro NFRA (a per-member exception to D9's LAPTOP
placement, on Andrew's f086 word). Registered @9e222e5b9f.

**Records:**
- the brief, approved "yes do it" (~01:2xZ);
- placement: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_013xZ_F086_9987_RELAYED.md` @dc3206a808;
- DONE WHEN approved: `ANDREW_DIRECT_20261016_035xZ_WFSPINE_DONE_WHEN_APPROVED.md` @1978f7855c ("Yes I like this layout you have for the
  project. I approve.");
- the bucket: `ANDREW_DIRECT_20261016_040xZ_WFSPINE_BUCKET_OPAL_DATA_TRINO.md` @4d1e860753 ("I think all of this should be stored in a bucket
  called opal-data-trino also, using LGIC_NAMING conventions otherwise." and "its a product folder so follows product rules").

## ENDPOINT (step 2, /endpoint --forward)

Confirmed by Andrew 2026-10-16 ~03:5xZ. Source: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_M365_WORKFLOW_SPINE_20261016.md`
@f96be0de11, copied verbatim.

```
  FWD-1  Andrew picks an employee and a trading day and reads that person's Microsoft 365 day, in order,
         from collection that is actually running
         DONE WHEN  EXERCISED -- one real person's real day, read end to end
         ACCEPT     Andrew names a colleague and a recent trading day, reads what they did in mail, Teams,
                    SharePoint and OneDrive in time order, and recognises it as that person's day; nothing
                    on the page was typed in by hand
         SOURCE     brief Part I, candidate thread and O1

  FWD-2  From any step, Andrew can follow a hand-off to the next person who touched the same thing
         DONE WHEN  EXERCISED -- a hand-off Andrew already knows about is followed both ways
         ACCEPT     a file or email Andrew knows passed from one colleague to another shows as one chain he
                    can walk forward and back, not as two unrelated lines
         SOURCE     brief O2; Part III bullet 2

  FWD-3  Andrew can see which workflows happen every trading day, for one person and across people
         DONE WHEN  EXERCISED -- a list of recurring workflows Andrew has reviewed
         ACCEPT     each workflow it calls daily is one Andrew agrees is daily; for one it misses, he can point
                    to the days where it happened
         SOURCE     brief O3; Part III bullet 3

  FWD-4  For a recurring workflow, Andrew can see where the time goes between its steps
         DONE WHEN  EXERCISED -- one workflow's timing read by Andrew
         ACCEPT     he can tell time spent waiting for someone else apart from time spent working, and the split
                    matches what he knows of that workflow
         SOURCE     brief O4

  FWD-5  Andrew receives a ranked list of places AI could remove work, each with its evidence
         DONE WHEN  EXERCISED -- Andrew has read the list and opened the evidence behind at least one item
         ACCEPT     each suggestion names the workflow and the steps AI would take over, is specific enough to
                    hand to someone to build, and its examples hold up when Andrew opens them
         SOURCE     brief O5; Part III bullet 4

  FWD-6  A research seat can ask the spine questions the same way it asks the rest of Opal's data
         DONE WHEN  EXERCISED -- one real question answered without a special export
         ACCEPT     an analyst asks who touched a given file this week and gets the answer the same way it
                    already looks things up, with no one preparing a file for it
         SOURCE     brief O6

  FWD-7  For any day, Andrew can see what the spine did not collect
         DONE WHEN  EXERCISED -- a day with a known gap shows the gap
         ACCEPT     a quiet day and a day the spine missed never look the same; a missed day too old to recover
                    is marked as lost for good
         SOURCE     brief O7; Part III bullet 5

  FWD-8  Andrew decides who is in the spine, and everyone else is absent everywhere
         DONE WHEN  EXERCISED -- a person Andrew excluded is checked for and not found
         ACCEPT     after Andrew names who is in and who is out, nobody he left out appears on any timeline,
                    chain or suggestion
         SOURCE     brief O8; Part III bullet 6

  FWD-9  For a workflow he chooses, Andrew can read the document content behind its steps
         DONE WHEN  EXERCISED -- one chosen workflow's documents read in place
         ACCEPT     Andrew opens a recurring workflow and reads what the documents it touched actually say,
                    within the scope he agreed; email and Teams message content are not part of this
         SOURCE     brief O9; Part II "Explicitly out"
```

## CONTRACTS

| row | owner | rule | proven by |
|---|---|---|---|
| C-APP | `1.0.0_SA_CTO~DELL1` (design); Andrew (the consent) | ONE new single-purpose Entra app holds `ActivityFeed.Read` on the Office 365 Management APIs, app-only, consented ONCE by Andrew (Cloud Application Administrator). The gateway's `M365-MCP-Graph` and `M365-MCP-Login` stay delegated-only, with NO scope added. | the app's granted permissions read back (one permission, admin-consented); the gateway apps' permission lists read unchanged before and after |
| C-SECRET | the round-1 collector cell | The app credential lives in the estate's secret store, read by name at run time; never printed, logged, written to the repo or committed. The secret's id follows the estate's secret convention (see C-HOMES: the builder has no secret kind). | a run log that names the secret id and prints no value; repo census for the value = 0 |
| C-COLLECT | the collector cell | A SCHEDULED collector (production pipelines are scheduled; an ad-hoc run is QA only), on cadence `hourly`. It lists available content per content type (`Audit.Exchange`, `Audit.SharePoint`, `Audit.General`, `Audit.AzureActiveDirectory`) and fetches each blob once. Blob events arrive out of time order and are sorted on landing. **No unattended gap may reach 7 days** (the source keeps 7). | the scheduled rule read back; two consecutive scheduled fires landing content; a planted 1-hour pause recovered on the next fire |
| C-HOMES | `1.0.0_SA_CTO~DELL1` | Every address and name is `lib/opal_naming` output; no hand-typed name. Bucket `opal-data-trino` is a PRODUCT home ("its a product folder so follows product rules"). Two registry rows are owed (below). | builder output pasted below; `opal_naming.validate()` clean with the rows added |
| C-POPULATION | Andrew sets it; the collector enforces it | FWD-8. Only the accounts Andrew lists are collected into silver and beyond. Bronze holds what the source ships, and the population filter applies at the bronze-to-silver step, so the excluded never reach a derived view. Default proposal: the 21 named employees; out: shared mailboxes, rooms, admin and break-glass, system accounts. | an excluded account checked for in every derived view = 0 rows |
| C-COVERAGE | the collector cell | FWD-7. Every fire writes the coverage record: per day and workload, whether content was listed and fetched, and any gap. A gap older than 7 days is written LOST. A day with no events reads "no activity collected", with the coverage beside it, never blank. | a planted gap reads as a gap, and a quiet day reads as quiet |
| C-CONTENT | Andrew (scope); a later cell | FWD-9. SharePoint and OneDrive documents only, through the SharePoint Online API (`Sites.Selected`, app-only, certificate), only for workflows Andrew names, only after his word on scope. Mail and Teams message content are OUT. | his scope word recorded before any content read |
| C-NOALERT | all | The spine raises no alert, alarm or notification on what a person does (standing moratorium). It is an analysis surface. | no alarm, SNS or notification resource in the project's Terraform |
| C-CLIENTDATA | all | Event records carry file names, email subjects and client names. They land only in `opal-data-trino` under the estate's client-data rules; no raw capture enters the repository; tests use synthetic events. | repo census for raw event payloads = 0 |
| C-QUERY | the derive cell | FWD-6. The derived views are readable through `globgrph-trino` as their OWN namespace. NFRA_GLOBGRPH's tables, derive and projection are not changed. | one analyst query answered through the existing Trino surface |

### C-HOMES: the builder output (Rule 30)

**At HEAD, the builder refuses** (run 2026-10-16 ~04:0xZ, `lib/opal_naming.py` at this tree):

```
address('microsoft-365', 'global', 'bronze', 'audit_events', 'date=2026-10-16', object='events.json.gz')
  -> ValueError: source 'microsoft-365' is not a systems.json key
name('wfspine', None, 'audit-collector', 'lambda')
  -> ValueError: system 'wfspine' is not a systems.json key (nor the reserved opal)
```

No scope row admits `opal-data-trino` (the census of `infra/logic/registry/{systems,scopes,tiers,resources}.json` finds 0 occurrences).

**The two registry rows owed** (round 1, cell 1; Andrew's 04:0xZ word is the R20 acknowledgement for the bucket):
1. `infra/logic/registry/scopes.json`: `{"key": "trino", "class": "PRODUCT", "long": "trino", "short": "trino", "tenancy": "GENERAL",
   "bucket": "opal-data-trino", "bucket_provisioned": false}`, with a note citing his two words.
   - Class PRODUCT is his word.
   - Tenancy GENERAL follows doctrine R4 as narrowed 2026-09-18: `opal-data-assets` is for client/partner CUSTODIAL information only, and
     every other scope, product included, is homed by its scope at every tier. Employee M365 activity is not custodial. This is the same
     shape as the `transcripts` row (class PRODUCT, tenancy GENERAL, its own bucket).
   - Gold is in `opal-data-{product}` per R5, and every tier sits in the scope bucket per R8 and `tiers.json` GENERAL homes.
2. `infra/logic/registry/systems.json`: a VENDOR source row `{"key": "m365audit", "long": "microsoft-365-audit", "display_name": "Office 365
   Management Activity API", "owner_directive": "D9"}`. The existing `teams`, `outlook` and `sharepoint` rows each name one workload; this
   source is the tenant audit feed across all of them.

**With those two rows, the builder's output** (run on a scratch copy of the registry with exactly these two rows added; `validate()` returned 0
errors and 0 warnings):

```
address('m365audit','trino','bronze','audit_events','date=20261016', object='Audit.SharePoint_20261016T0300Z.json.gz')
  -> s3://opal-data-trino/m365audit/trino/bronze/audit_events/date=20261016/Audit.SharePoint_20261016T0300Z.json.gz
address('m365audit','trino','silver','activity_events','date=2026-10-16', object='data.parquet')
  -> s3://opal-data-trino/m365audit/trino/silver/activity_events/date=2026-10-16/data.parquet
address('m365audit','trino','gold','person_day_timeline','date=2026-10-16', object='data.parquet')
  -> s3://opal-data-trino/m365audit/trino/gold/person_day_timeline/date=2026-10-16/data.parquet
address('m365audit','trino','gold','handoff_chains','date=2026-10-16', object='data.parquet')
  -> s3://opal-data-trino/m365audit/trino/gold/handoff_chains/date=2026-10-16/data.parquet
address('m365audit','trino','gold','recurring_workflows','date=2026-10-16', object='data.parquet')
  -> s3://opal-data-trino/m365audit/trino/gold/recurring_workflows/date=2026-10-16/data.parquet
address('m365audit','trino','gold','step_timing','date=2026-10-16', object='data.parquet')
  -> s3://opal-data-trino/m365audit/trino/gold/step_timing/date=2026-10-16/data.parquet
address('m365audit','trino','gold','ai_candidates','date=2026-10-16', object='data.parquet')
  -> s3://opal-data-trino/m365audit/trino/gold/ai_candidates/date=2026-10-16/data.parquet
address('m365audit','trino','gold','collection_coverage','date=2026-10-16', object='data.parquet')
  -> s3://opal-data-trino/m365audit/trino/gold/collection_coverage/date=2026-10-16/data.parquet
address('m365audit','trino','state','subscription_cursor','current', object='cursor.json')
  -> s3://opal-data-trino/m365audit/trino/state/subscription_cursor/current/cursor.json
name('m365audit', None, 'trino-audit-collector', 'lambda')  -> m365audit-trino-audit-collector-lambda
name('m365audit', None, 'trino-audit-collector', 'role')    -> m365audit-trino-audit-collector-role
name('m365audit', None, 'trino-audit-collector', 'hourly')  -> m365audit-trino-audit-collector-hourly
```

**Further refusals, recorded rather than worked around:**

```
name('m365audit','trino','audit-collector','lambda')
  -> scope 'trino' is a PRODUCT scope; this slot takes FIRM/GLOBAL/MASTER
name('m365audit', None, 'trino-audit-collector', 'secret')
  -> kind 'secret' is neither a NAMING_SCHEMA.json kind nor a cadence
```

- The resource names therefore take the shared form, with `trino` in the function segment.
- The app credential's secret id has no builder kind: either `org/standards/NAMING_SCHEMA.json` gains a secret kind (a schema row; LGIC's
  owner decides), or the secret follows the estate's existing secret-id convention as a declared departure. Round 1, cell 1 settles which.
  This is the one name the PRD does not fix.
- The table segments (`audit_events`, `activity_events`, `person_day_timeline`, and so on) are this PRD's proposal; the builder accepted them
  as written.

## THE DECISIONS -- CLOSED AT L4

1. **One new app, app-only, one consent; the gateway stays delegated.** The audit feed is not Graph, and the gateway's secret never carries
   tenant-wide reach.
2. **Bucket `opal-data-trino`, PRODUCT class, GENERAL tenancy, every tier in the one bucket** (Andrew's two words; R4 narrowed, R5, R8).
3. **Bronze is raw** (R9): the content blobs as Microsoft ships them, gzipped JSON. Silver is parquet (one row per audit event, sorted by
   time).
4. **The population filter sits at bronze to silver.** Bronze is the source of truth; no derived view ever holds an excluded account.
5. **Hourly scheduled collection**, with a state cursor. An unattended gap of 7 days or more is a permanent loss, and it is written as one.
6. **Query through `globgrph-trino`**, in its own namespace; nothing of NFRA_GLOBGRPH changes.
7. **No alerting, ever** (moratorium).
8. **Mail and Teams content are out.** Document content (FWD-9) is SharePoint/OneDrive only, on Andrew's scope word.
9. **The 180-day backlog is out** (it needs Purview or a role Andrew does not hold).

## OPEN AT ANDREW (acts only he can do)

- **The consent:** granting `ActivityFeed.Read` to the new app, as Cloud Application Administrator. His role is assumed active; it was last
  verified 2026-09-14.
- **The population list (FWD-8):** who is in. The default proposal is the 21 named employees.
- **The content scope (FWD-9):** which workflows' documents may be read, when that outcome comes up.
- **Employee notice:** New York Civil Rights Law s.52-c requires written, acknowledged notice of email and internet monitoring for an employer
  with a NY place of business. Whether it applies and whether the handbook already covers it is his and counsel's. It is named here as a fact,
  not a gate.

## CELL CANDIDATES

**Round 1 builds the FWD-1 thread, hop by hop.** A build cell carries at most three mechanical criteria.
1. **Registry rows and homes.** The two registry rows in C-HOMES; the secret-name question settled; `opal-data-trino` provisioned through
   Terraform (`safe-apply`).
2. **App and consent.** The Entra app is registered, and the consent is requested of Andrew (his act). The credential goes into the secret
   store.
3. **Subscription.** The subscriptions are started for the four content types. The first content may take up to 12 hours.
4. **Scheduled collector.** The `hourly` collector writes bronze, the state cursor and the coverage record.
5. **Silver and one readable day.** Bronze becomes silver, sorted, with the population filter applied. Then one person's one trading day is
   rendered for Andrew to read (FWD-1's EXERCISED bar).

**Later rounds (enrichment):** FWD-7 coverage reads and FWD-8 population checks, then FWD-2 chains, FWD-3 recurring workflows, FWD-4 timing,
FWD-6 the Trino namespace, FWD-5 AI candidates, and FWD-9 content (on his word).

## PATHS

- `org/missions/D9/NFRA/NFRA_WFSPINE/**`: the project tree.
- `infra/logic/registry/scopes.json` and `systems.json`: the two rows only.
- A new code home for the collector and derive, placed by the LGIC code-home rule (R16) at cell 1.
- `infra/aws/terraform/<root named at cell 1>/`: the bucket, the app secret reference, the collector, its role and schedule.
- `s3://opal-data-trino/m365audit/trino/**`: runtime.

## BRIEF COVERAGE

| brief | here |
|---|---|
| O1 | FWD-1 |
| O2 | FWD-2 |
| O3 | FWD-3 |
| O4 | FWD-4 |
| O5 | FWD-5 |
| O6 | FWD-6, C-QUERY |
| O7 | FWD-7, C-COVERAGE |
| O8 | FWD-8, C-POPULATION |
| O9 | FWD-9, C-CONTENT |
| Part II owns | C-APP, C-COLLECT, C-HOMES, C-COVERAGE, C-POPULATION |
| Part II relies on (GLOBGRPH, OPLGTW, transcripts, MCPINDEX, LGIC) | C-QUERY; C-APP (the gateway unchanged); C-HOMES |
| Part II out (mail and Teams content, the 180-day backlog, non-Microsoft, alerting, EWS) | DECISIONS 7-9 |
| Part V (unified audit logging on; role active; notice) | OPEN AT ANDREW; cell 2 reads whether audit logging is on |

## SURFACE MANIFEST

| surface | kind | cell | owner |
|---|---|---|---|
| `infra/logic/registry/scopes.json` (row `trino`) and `systems.json` (row `m365audit`) | NEW registry rows | R1 C1 | NFRA_WFSPINE |
| bucket `opal-data-trino` | NEW bucket (Terraform, `safe-apply`) | R1 C1 | NFRA_WFSPINE |
| the Entra app with `ActivityFeed.Read` (app-only) and its secret | NEW identity; the consent is Andrew's act | R1 C2 | NFRA_WFSPINE |
| the Office 365 Management Activity API subscriptions (4 content types) | NEW vendor subscription, read-only | R1 C3 | NFRA_WFSPINE |
| `m365audit-trino-audit-collector-lambda`, `-role`, `-hourly` | NEW scheduled collector | R1 C4 | NFRA_WFSPINE |
| `s3://opal-data-trino/m365audit/trino/{bronze,silver,state}/` and `gold/collection_coverage/` | NEW data planes | R1 C4-C5 | NFRA_WFSPINE |
| `s3://opal-data-trino/m365audit/trino/gold/{person_day_timeline,handoff_chains,recurring_workflows,step_timing,ai_candidates}/` | NEW derived views | R1 C5 and later | NFRA_WFSPINE |
| a `globgrph-trino` namespace for the spine | NEW read surface (FWD-6) | later round | NFRA_WFSPINE |
| `org/missions/D9/NFRA/NFRA_WFSPINE/deliverables/` | documents | all | NFRA_WFSPINE |
| the gateway's `M365-MCP-Graph` / `M365-MCP-Login`; NFRA_GLOBGRPH's tables; `opal-data-transcripts`; any firm bucket; `opal-data-assets` | excluded | -- | untouched |

-- 1.0.0_SA_CTO~DELL1

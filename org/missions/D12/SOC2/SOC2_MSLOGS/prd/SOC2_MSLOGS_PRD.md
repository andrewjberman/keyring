# SOC2_MSLOGS -- Microsoft 365 audit logs as compromise exposure: if an Opal account is taken over, know what was seen, what left and for how long, and show that Opal has internal security

```json
{
 "project": "SOC2_MSLOGS",
 "directive": "D12",
 "fabric": "dell1",
 "prd_version": "v0.1",
 "step": 4,
 "brief_ref": "docs/briefs/soc2-mslogs-compromise-exposure-brief-20261016.md@0113e9f438",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9"],
 "status": "DRAFT"
}
```

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-16 ~16:3xZ.
**Placement:** DELL1, directive D12, macro SOC2. This is a per-member exception to D12's SITEZ placement, on Andrew's word "handled on this
box". Registered @dcf19c79ae.
**Supersedes:** TCKT_MTADTA (D7). It is closed on his word "that project is closed", and every live resource it built passes to this project
unchanged and running.
**Driven by:** `2.0.0_SA_COO~S1`, on his word "theyll bring it back to you once that plan is locked in and you will be the one driving it".

**Records (Andrew-direct, all 2026-10-16):**
- **the reframe**, ~15:59Z at `2.0.0_SA_COO~S1`:
  `org/tier1_exec/2.0.0_SA_COO~S1/ANDREW_DIRECT_20261016_1559Z_REFRAME_M365_LOGS_AS_SOC2_COMPROMISE_EXPOSURE_MACRO_SOC2_MSLOGS.md`.
  It includes "if any opal user is hacked, we want to be able to know the exposure; what was seen, what the duration period was" and
  "Silver is just formatted bronze in parquet for query, gold is effectively pattern baselines".
- **metadata only, raw pull**, ~16:12Z at `4.0.0_SA_CRO~DELL1`:
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261016_1612Z_SOC2_MSLOGS_METADATA_ONLY_PROOF_OF_INTERNAL_SECURITY.md` @0f2f158dc2.
  It includes "do not need anything further" and "get the raw audit pull, dont redact it unnecessarily".
- **endpoint, population, naming**, ~16:2xZ here:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_162xZ_ALL_RECS_APPROVED_SOC2_MSLOGS_ENDPOINT_RAW_ALL_ACCOUNTS_DEV_APPROVALS_NAMING.md`.
  It reads "all recs approved".
- **access, inherited:** "only iam globgrph group can access, if you want to access you have to go through the reader/writer lambda" (06:2xZ,
  @f4fbcdfde4), and "read/write/do ops in there, and if we want to know things about it, we drive/query that lambda" (15:3xZ).

## ENDPOINT (step 2, /endpoint --forward)

Confirmed by Andrew ~16:2xZ. Source: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_SOC2_MSLOGS_20261016.md` @b8c7dd61e8.
**The responder** is Andrew, or whoever he names to handle a suspected account takeover.

  FWD-1  The responder names one Opal account and a time window, and reads everything it did in that window, in order
         DONE WHEN  EXERCISED -- one live read of a real account's real window through the one door
         ACCEPT     Andrew picks an account and a day and reads its sign-ins, mail and file activity in time order, and
                    recognises it as that person's real day. Nothing in it was prepared by hand, and it came from collection
                    that is running
         SOURCE     brief Part I thread, O1

  FWD-2  For a window, the responder knows the exposure: what was opened, and everything that left
         DONE WHEN  EXERCISED -- one window's exposure list read and checked
         ACCEPT     for a window he chooses, Andrew gets one list he could act on: the mail and documents the account
                    opened, downloaded or synced, and every outside person who got a mail, forward, share link or file from
                    it. Where Microsoft does not record mail being opened for Opal's licence, the list says so rather than
                    leaving it out
         SOURCE     brief O2, F6

  FWD-3  The responder can tell when a takeover began and when it stopped
         DONE WHEN  EXERCISED -- a deliberate drill sign-in, read back
         ACCEPT     Andrew signs in to his own account from somewhere unusual, on purpose, and later reads back the first
                    and last moment of that session correctly. An ordinary day of his reads with no such session
         SOURCE     brief O3, F4

  FWD-4  The responder sees what an attacker left behind, so it can be removed
         DONE WHEN  EXERCISED -- a planted forwarding rule found
         ACCEPT     a mail forwarding rule set on purpose on an account appears in the list of lasting changes, with when
                    it was made and from where, and its removal appears too
         SOURCE     brief O4

  FWD-5  For any Opal user, the responder can read what normal looks like for that person
         DONE WHEN  EXERCISED -- a person reads their own pattern and agrees
         ACCEPT     Andrew reads his own usual pattern (where and when he signs in, from which devices, how much he reads,
                    sends and shares) and agrees it describes him
         SOURCE     brief O5

  FWD-6  On asking, the responder sees which accounts are acting outside their own normal pattern
         DONE WHEN  EXERCISED -- the drill shows up, and the rest is not noise
         ACCEPT     after the FWD-3 drill, asking shows his account with the reason. Andrew agrees the other accounts listed,
                    if any, are worth a look rather than someone's ordinary travel or busy day. Nobody is told unprompted; he
                    asks
         SOURCE     brief O6, F5

  FWD-7  A quiet record can be trusted: "nothing happened" is never confused with "collection missed it"
         DONE WHEN  EXERCISED -- a deliberate pause reads as a gap
         ACCEPT     after collection is paused on purpose for an hour, that hour reads as a gap for every account, not as a
                    quiet hour. A gap too old to recover reads as lost
         SOURCE     brief O7

  FWD-8  Only the door reads the store, Andrew knows what a stolen login could still reach, and the record survives an attacker
         DONE WHEN  EXERCISED -- a refused direct read, and a stored copy that outlives turning auditing off
         ACCEPT     an administrator's direct read of the stored data is refused. Andrew holds a plain statement of what his
                    own, an admin's or any user's stolen login could still reach here. Records already copied stay readable
                    even if auditing is switched off inside Microsoft 365
         SOURCE     brief O8, F7

  FWD-9  An auditor can be shown that Opal monitors user activity and keeps the record safe and complete
         DONE WHEN  EXERCISED -- one auditor-style question answered from the system
         ACCEPT     Andrew can show an assessor, from the system itself, that collection is running for every account, that
                    its gaps are known, that only the door reads it, and that it answered a compromise question
         SOURCE     brief O9

**Scope is capped at FWD-1 to FWD-9** ("do not need anything further").

## CONTRACTS

| row | owner | rule | proven by |
|---|---|---|---|
| C-APP | `1.0.0_SA_CTO~DELL1` (design); Andrew (any consent) | The existing single-purpose Entra app, inherited from TCKT_MTADTA, holds `ActivityFeed.Read` on the Office 365 Management APIs, app-only. Round 1 reads whether `Audit.AzureActiveDirectory` is served under that one permission. If it is not, the extra permission is named and consenting to it is Andrew's act. The gateway's apps stay delegated-only and unchanged. | the app's permissions read back; an `Audit.AzureActiveDirectory` subscription started and listing content, or the named permission it needs |
| C-SECRET | the collector cell | Inherited unchanged. The credential is read by id from the secret store at run time and is never printed, logged or committed. | a run log naming the id with no value; repo census for the value = 0 |
| C-POPULATION | the collector | **Every account in the Opal tenant:** members, and guests acting in it. No account filter runs anywhere. The eight-name list and its drop-before-write are removed. | a census of one day's bronze shows actors outside the old eight; the collector code holds no population list |
| C-RAW | the collector | **Bronze is the audit records exactly as Microsoft ships them,** byte for byte (LGIC R9). Subject hashing, address class tokens, the IP flag and the field whitelist are all removed. Minimising happens in what a read returns, never in what is stored. LGIC conformance ledger X18 departure (1) is retired; departure (2), the KMS key alias, is unaffected. The retirement is recorded in round 1 by the LGIC owner, citing Andrew's ~16:12Z and ~16:2xZ words. | a stored record compared byte for byte against the blob the API served for it; X18 (1) reads retired in the ledger |
| C-CONTENT | all | **No content, ever:** no mail body, Teams message text or document content is fetched or stored. The audit records are metadata (who, which action, which item, when, from where). Where a record carries a mail subject or a file name, it is kept as Microsoft recorded it. | no Graph mail, Teams or file-content permission on the app; no content fetch in the code |
| C-COLLECT | the collector | **Scheduled hourly** (inherited). Content types: `Audit.Exchange`, `Audit.SharePoint`, `Audit.General`, plus `Audit.AzureActiveDirectory` (the sign-in feed). Each blob is fetched once; the cursor advances only past landed writes. No unattended gap may reach 7 days. The collector writes through the door and holds no S3 permission of its own. | the scheduled rule read back; two consecutive scheduled fires landing all four types |
| C-SWITCH | the collector cell | The switch from the reduced era to the raw era is one deploy. Raw records land in a NEW bronze table, `audit_records`. The reduced table `audit_events` is frozen: kept read-only and never written again, so nothing is deleted or mixed. At the switch, the collector re-fetches the API's last 7 days raw into `audit_records`. The coverage record marks each day reduced-only, raw, or both. | `audit_events` holds no object newer than the switch; `audit_records` holds the re-fetched 7 days; coverage names the era of each day |
| C-ACCESS | `1.0.0_SA_CTO~DELL1` (design); the access cell | Inherited, as amended by TCKT_MTADTA v0.5. (1) Only `globgrph-trino-access-group` members invoke the door's members' alias, and the collector role invokes only its own alias (put, derive_silver, the cursor read). (2) `globgrph-trino-access-lambda` is the only reader and writer. (3) Its role `globgrph-trino-access-role` is the only principal the bucket policy admits; every other principal is Denied every object data action. `s3:ListBucket` is not denied, and no key segment carries a person, address or file name. (4) The dedicated KMS key admits the same role alone. **The members' alias serves the reads of C-READS, a write and the maintenance ops, all through the door.** No op deletes stored data. | a direct `GetObject` by an admin refused; a non-member invoke refused; a member read answered |
| C-READS | the access cell | The door's compromise reads, each over one account and one window, returning query results, never raw objects:<ul><li>`timeline` (FWD-1): every event in time order across the four feeds;</li><li>`exposure` (FWD-2): items opened, downloaded or synced, and every outside recipient of mail, forwards, share links and files. Where `MailItemsAccessed` is absent for the account's licence, it says so;</li><li>`session_span` (FWD-3): the first and last event of a sign-in session it is asked about;</li><li>`persistence` (FWD-4): inbox and forwarding rules, mailbox delegation, app consents, sign-in method changes and sharing links, with when and from where.</li></ul>Every call is logged. | each read answered on a drill or a real window, read by Andrew |
| C-BASELINE | the gold cell | Gold holds a per-account baseline (FWD-5), built from history: where and when the account signs in, its devices and apps, and how much it reads, sends and shares. The window length is read from the data at the cell, not fixed here. The `outside_baseline` read (FWD-6) is computed on asking, through the door, and names each account outside its own baseline with the evidence. No flag is stored as a notification and none is sent. | Andrew's own baseline read and agreed; the drill account appears on asking |
| C-COVERAGE | the collector | FWD-7, inherited. Every fire writes, per day and content type: listed, fetched, gap, and era (C-SWITCH). A gap older than 7 days is written LOST. A day with no events reads "no activity collected", with the coverage beside it. | a deliberate 1-hour pause reads as a gap for every account; a gap past 7 days reads LOST |
| C-RESIDUAL | `1.0.0_SA_CTO~DELL1` (the statement); Andrew (reads it) | FWD-8's statement names what C-ACCESS does not stop, inside one AWS account:<br>(1) the root user;<br>(2) any principal that can edit the bucket policy, key policy, door code or role, because it can grant itself in;<br>(3) Andrew's M365 account, which as Cloud Application Administrator could change the collector app or read the tenant log from Microsoft directly;<br>(4) any group member, who can read every Opal account's raw records and write through the door;<br>(5) the collector role, limited to its three ops;<br>(6) anyone with `s3:ListBucket`, who sees table names, dates and sizes only.<br>It also states that the store now holds every account's raw IPs, addresses, mail subjects and file names, so a stolen group login is worth more than before. Removing (1) and (2) is the later AWS Organization project. | the statement exists, is dated, names each residual, and leaves no "would not matter" claim standing |
| C-SURVIVES | the collector | FWD-8's second half: records already copied are stored outside Microsoft 365, in a bucket no M365 admin role reaches. Turning auditing off inside the tenant stops new records and moves none already stored. The coverage record shows the stop as a gap. | the drill: audit search confirms what is stored for a past window; the stored copy reads unchanged after an admin-side change |
| C-AUDITOR | the CTO (the page); the issuer (the read) | FWD-9: one plain auditor answer, produced from the system: collection running for every account (coverage), known gaps, door-only access (C-ACCESS reads), and one compromise question answered (a drill). | Andrew reads it and can hand it to an assessor |
| C-RETENTION | Andrew may set it | No expiry until Andrew sets one. Records are kept, because deleting them would defeat FWD-8. | no lifecycle expiry rule on the prefix |
| C-NOALERT | all | Nothing raises an alert, alarm or notification (standing moratorium). FWD-6 is read on asking. | no alarm, SNS, SES or notification resource in the project's Terraform |
| C-HOMES | `1.0.0_SA_CTO~DELL1` | Every address and name is `lib/opal_naming` output (rule 30). Below. The `m365-metadata` systems row's `owner_directive` moves D7 -> D12 in round 1 (LGIC owner's lane, a one-field row edit). | builder output below; `validate()` clean |

### C-HOMES: the builder output (Rule 30), run 2026-10-16 ~16:3xZ at this tree

```
address('m365-metadata','trino','bronze','audit_events','date=20261016', object='events.json.gz')
  -> s3://opal-data-trino/m365-metadata/trino/bronze/audit_events/date=20261016/events.json.gz          (frozen, reduced era)
address('m365-metadata','trino','silver','activity_events','date=2026-10-16', object='data.parquet')
  -> s3://opal-data-trino/m365-metadata/trino/silver/activity_events/date=2026-10-16/data.parquet
address('m365-metadata','trino','gold','collection_coverage','date=2026-10-16', object='data.parquet')
  -> s3://opal-data-trino/m365-metadata/trino/gold/collection_coverage/date=2026-10-16/data.parquet
address('m365-metadata','trino','gold','account_baseline','date=2026-10-16', object='data.parquet')
  -> s3://opal-data-trino/m365-metadata/trino/gold/account_baseline/date=2026-10-16/data.parquet
address('m365-metadata','trino','gold','account_day_timeline','date=2026-10-16', object='data.parquet')
  -> s3://opal-data-trino/m365-metadata/trino/gold/account_day_timeline/date=2026-10-16/data.parquet
address('m365-metadata','trino','state','subscription_cursor','current', object='cursor.json')
  -> s3://opal-data-trino/m365-metadata/trino/state/subscription_cursor/current/cursor.json
```

- **The new raw bronze table `audit_records`** follows the same grammar:
  `s3://opal-data-trino/m365-metadata/trino/bronze/audit_records/date=<yyyymmdd>/<blob-id>.json.gz`. The collector cell pastes the
  builder's output for it before writing.
- **Inherited names, unchanged:** `globgrph-trino-access-group`, `globgrph-trino-access-lambda`, `globgrph-trino-access-role`, and the
  collector `m365-metadata-trino-collector-lambda` on `m365-metadata-trino-collector-hourly`. None carries a Ticket Center term.
- **Retired with the reframe:** the gold table `person_day_timeline` is replaced by `account_day_timeline`, keyed on any account, not a person
  of the eight.

## THE DECISIONS -- CLOSED AT L4

1. **Every account, raw (C-POPULATION, C-RAW).** This is Andrew's word, recorded three times above. The old drop-at-collection departure
   and its consequence ("an error cannot be repaired from bronze") are retired with it. Bronze is now the repair source.
2. **No content (C-CONTENT).** This is his 16:12Z word. The audit records carry no message body or file content.
3. **The sign-in feed is added (C-COLLECT).** For a compromise, the sign-in record is where a takeover starts and how its duration is
   fixed.
4. **The reduced era is frozen, never deleted (C-SWITCH).** A delete would need his word and would destroy evidence, and freezing costs
   one table name.
5. **Pull, never push (C-BASELINE, C-NOALERT).** "Establishing if a suspicious one appears" is detection on asking, and the moratorium
   stands.
6. **No retention expiry (C-RETENTION)** until he sets one.
7. **Out of scope:** any content; anything off Microsoft 365; Purview backfill beyond the API's 7 days (a later lever, brief F7); any
   notification; the AWS Organization (the later project); every Ticket Center outcome.

## OPEN AT ANDREW (acts only he can do)

- **A permission consent,** only if round 1 reads that the sign-in feed needs more than `ActivityFeed.Read` (C-APP).
- **The FWD-3 and FWD-4 drills:** signing in from somewhere unusual, and setting then removing a forwarding rule. These are acts on his
  own account.
- **A retention period,** whenever he wants one (C-RETENTION).
- **Employee notice and policy.** Monitoring every employee's activity is his and counsel's to set; it is named here as a fact, not a gate.

## CELL CANDIDATES (round 1 builds the FWD-1 thread; the issuer decomposes)

1. **The switch (FWD-1's first hop):**
   - remove the population filter and field levers;
   - add `Audit.AzureActiveDirectory`;
   - land raw records in `audit_records`;
   - re-fetch the last 7 days raw;
   - freeze `audit_events`;
   - coverage carries the era.
   The registry rows (`owner_directive` D12, the X18 (1) retirement) go to the LGIC owner in the same round.
2. **The `timeline` read through the door, and Andrew's FWD-1 read** of one real account and day.
3. **Silver over `audit_records`,** the same events in parquet.

Later rounds enrich: `exposure`, `session_span`, `persistence`, baselines and `outside_baseline`, the residual statement, and the auditor
answer.

## PATHS

- **This project:** `org/missions/D12/SOC2/SOC2_MSLOGS/`.
- **Inherited code** (read by the issuer at HEAD before the first cell; the TCKT_MTADTA decompositions name it): the collector and door
  Lambda sources, their Terraform root, and the coverage writer.

## SURFACE MANIFEST

- **AWS:** the existing collector Lambda and its schedule, the door Lambda and its two aliases, the group, the role, the bucket prefix
  `opal-data-trino/m365-metadata/trino/`, and the KMS key. No new bucket and no alarm.
- **Entra:** the existing collector app, plus at most one permission, which is Andrew's consent.
- **Repo:** this tree, plus the two registry edits named under C-HOMES and C-RAW.

-- 1.0.0_SA_CTO~DELL1

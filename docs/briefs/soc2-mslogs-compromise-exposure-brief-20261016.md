# SOC2_MSLOGS -- Microsoft 365 audit logs as compromise exposure: if an Opal account is taken over, know what was seen, what left, and for how long

**Mode:** MIDSTREAM (`/brief-create --midstream`). The project in flight is TCKT_MTADTA (D7, dell1), reframed by Andrew.
**Author:** `4.0.0_SA_CRO~DELL1`, 2026-10-16 ~16:1xZ. **Consumer:** `1.0.0_SA_CTO~DELL1`, `/endpoint --forward` (L2), then the locked plan
returns to `2.0.0_SA_COO~S1`, who drives it (Andrew messages 4-5).
**Andrew's word, verbatim** (record `org/tier1_exec/2.0.0_SA_COO~S1/ANDREW_DIRECT_20261016_1559Z_REFRAME_M365_LOGS_AS_SOC2_COMPROMISE_EXPOSURE_MACRO_SOC2_MSLOGS.md`
@99feec5978 + @8f5176c374): *"we actually reframe this whole thing about audit monitoring for suspicious behavior. the premise is if any
opal user is hacked, we want to be able to know the exposure; what was seen, what the duration period was, its really about disaster
recovery/remediation. I want this all under a new macro called SOC2_MSLOGS. We should scrub all ticket center frameworks from this schema.
What happens is everything should be in the trino audit bucket, and it does track activity, but the premise is not for workflows, its for
identifying common patterns and establishing if a suspicious one appears. Silver is just formatted bronze in parquet for query, gold is
effectively pattern baselines."* and *"its fairly cosmetic + cleaning up TCKT_MTADTA references"*.

> **AMENDMENT 1 (2026-10-16 ~16:1xZ, Andrew at this terminal, verbatim):** *"Yeah we dont need to see the body of an email and stuff
> like that, this is metadata focused/analytics focused, do not need anything further. this is just a remediation strategy so we have
> something to prove that we have internal security"* (record
> `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261016_1612Z_SOC2_MSLOGS_METADATA_ONLY_PROOF_OF_INTERNAL_SECURITY.md`).
> What it changes below: content is OUT (Part II, Part III item 7); the outcome set is CAPPED at the thread plus O1-O9; the purpose is
> a remediation strategy plus proof of internal security, so O8 and O9 are why the project exists and O1-O4 are the strategy.
> Follow-ons, verbatim: *"yeah like get the raw audit pull, dont redact it unnecessarily"* and *"but this application/log system as I
> understand does not ahve anything that sensitive"*. Raw bronze (F3) is now his word, not only the REC: the C-FIELDS redaction levers
> are retired. Fact beside it (the PII read): the records carry no body or file content, but do carry IPs, addresses, some mail
> subjects and file names; they are stored as Microsoft records them and protected by the door and the key (F1), not by redaction.

---

## PART 0 -- How the blind constraint was honoured, and where it bent

- **Not read:** the project's task orders, decompositions, `project.json` phase/blocking fields, and its surprise channel.
- **Read:** the PRD's title, ENDPOINT and CONTRACTS (purpose and acceptance), the PII read that grounded it
  (`WFSPINE_AUDIT_CONTENT_AND_PII_20261016.md`), Andrew's records, the LGIC doctrine (R9) and conformance ledger (X18), and the served
  reality as stated in the issuer's record.
- **Where it bent (three leaks, named so a ratifying outcome cannot hide in them):**
  1. The issuer's relay messages carry branch state: "round 3 held", "round 2 continues as is". I know a round is open; I do not know
     its cells.
  2. An outline grep of the PRD showed its CELL CANDIDATES headings (round 1 builds the FWD-1 thread; then coverage, chains, timing,
     candidates). That is the old decomposition's shape. No outcome below is cut from it.
  3. The CTO's message (6838) framed four "forks". I used them as the questions Part IV must answer, not as the outcome list.
- **Direction verdict:** NOT unchanged. The pipes are reusable; the purpose, the population and what is stored all change (Part IV,
  F1-F4). Andrew's "fairly cosmetic" holds for the infrastructure and does not hold for the data contract.

---

## PART I -- THE OUTCOME TERRITORY

People named: **the responder** (Andrew, or whoever he names to handle a suspected account takeover); **an auditor** (a SOC2 assessor
or Andrew answering one).

### Candidate thread (becomes FWD-1)
**The responder names one Opal account and a suspected window, and reads everything that account did in it -- where it signed in from,
what mail and files it opened, sent, forwarded or shared -- in time order, from collection that is actually running.** One real
account, one real window, end to end through the one door. Every other outcome enriches this journey.

### O1 -- Read an account's activity across a suspected window
The responder reads one account's sign-ins, mail, Teams, SharePoint and OneDrive activity over a window he chooses, in order, and
recognises it as that account's real activity. (The thread.)

### O2 -- Know the exposure: what was seen and what left
For that window the responder gets the list of mail items and documents the account opened, downloaded or synced, and every outside
party who received mail, a forward, a share link or a file from it -- the list remediation acts on (recall, revoke, notify). The list
is built from audit metadata (which item, when, by whom, to whom); nobody reads what the items say (Amendment 1).

### O3 -- Establish the duration of a compromise
The responder can tell when the takeover began and when it stopped: the first sign-in or action that is not the person's own, and
the last one.

### O4 -- Find what an attacker left behind
The responder sees the changes made from the account that outlive the session -- inbox and forwarding rules, mailbox delegation, app
consents, sign-in method changes, sharing links -- so each can be removed.

### O5 -- Read what normal looks like for any user
For any Opal user, the responder can read that person's usual pattern -- where and when they sign in, from which devices and apps, and
how much they normally read, send and share -- built from history, not guessed.

### O6 -- See which accounts are acting outside their normal pattern
On asking, the responder sees which accounts currently show activity outside their own baseline, with the evidence for each, and can
open any one into O1. Pull, not push (Part IV, F6).

### O7 -- Trust a quiet record
For any account and day, the responder can tell "nothing happened" from "collection did not see it"; a gap never reads as clean, and a
gap too old to recover is marked lost.

### O8 -- Know who can read it, and that it survives the attacker
Only the approved door reads the store; the responder holds a current statement of what a stolen login (his, an admin's, any user's)
could still reach in this store, and the record survives an attacker who disables or erases auditing inside Microsoft 365.

### O9 -- Show an auditor that user activity is monitored
An auditor is shown, from the system itself, that Opal collects Microsoft 365 user activity, keeps it protected and complete, and can
answer a compromise question from it.

---

## PART II -- WHERE THE BOUNDARY SITS

**Owns:** the collection of the Microsoft 365 audit feeds for Opal's tenant; bronze, silver and gold under the trino audit bucket; the
baselines and the outside-baseline reads; the exposure, duration and persistence reads through the door; the coverage record; the
residual-access statement.

**Relies on, does not own:**
- **The built TCKT_MTADTA pieces** -- the collector, the door (reader/writer Lambda, two aliases), the group, the single-permission Entra
  app, the KMS key and `opal-data-trino/m365-metadata/trino/`. They are reused, not rebuilt (the CTO's message 6838; Andrew "everything
  should be in the trino audit bucket").
- **The later AWS Organization project** (Andrew 06:xxZ: "We will have a separate project to set up the organization"). It removes
  the root and IAM-admin residuals; this project only states them.
- **Microsoft 365 itself** -- licences, the tenant's audit setting, and Purview's own audit search (the source of truth inside the tenant).

**Leaves:**
- **Content (Amendment 1):** no email body, Teams message text or document content is read or stored, now or later. TCKT_MTADTA's
  content outcome (FWD-10, C-CONTENT) does not carry over. Nothing is added beyond the outcomes in Part I.
- **TCKT_VNEXT and Ticket Center:** no relationship remains. The workflow outcomes (hand-offs, recurring workflows, timing, Ticket
  Center candidates, document reads for workflows) are out, per "scrub all ticket center frameworks".
- **TCKT_MTADTA as a name:** whether it is renamed and re-homed, or closed and superseded by a new SOC2 project that inherits its
  resources, is the CTO's register call (L3). Either way no TCKT reference survives in the schema, the contracts or the paths.
- **NFRA_WFSPINE** stays closed (the predecessor).

---

## PART III -- THE QUALITATIVE BAR

1. **The responder answers "what did they see, what left, and since when" in one place**, instead of running separate audit searches
   in the Microsoft portals and stitching the results by hand.
2. **A false calm is worse than a gap.** A day or an account the collection missed must never read as clean.
3. **A flag is credible when Andrew looks at it and agrees the pattern is unusual for that person.** Flags that fire on someone's
   ordinary travel or a normal busy day are noise; flags that miss a pattern he would call suspicious are misses.
4. **The copy is evidence.** Bronze is what Microsoft sent; anything above it can be rebuilt from it, and nothing in bronze is altered.
5. **No workflow vocabulary.** A reader of the schema and contracts finds no Ticket Center term.
6. **Protection grows with coverage.** Storing everyone's raw activity metadata raises the stakes of a stolen login; the access
   statement stays honest about what remains reachable.
7. **Metadata, never content (Amendment 1).** Every answer is built from who did what to which item, when and from where; a reader
   never sees what an email or document says.
8. **It exists to prove internal security (Amendment 1).** It succeeds when Andrew can hand an auditor the evidence and walk a
   suspected takeover to a remediation list, not when it surfaces insight about how people work.

---

## PART IV -- THE SUBSTRATE: findings, and the four forks

Each finding states what was measured or read. Recommendations (REC) answer the CTO's four questions (msg 6838).

### F1 -- The infrastructure fits the new purpose as built
Read: PRD C-APP, C-COLLECT, C-ACCESS, C-COVERAGE, C-HOMES; the issuer's record (live: collector, door with two aliases, the prefix with
bronze/silver/gold-coverage/state, the one-permission app, the group with `Andrew_Berman`, two clean scheduled fires, 7 days stored).
The door-only access model (C-ACCESS), the coverage record (C-COVERAGE) and the no-gap-past-7-days rule (C-COLLECT) serve compromise
response unchanged. **This is the "cosmetic" part.**

### F2 -- Fork 1, population: all Opal accounts, and external addresses KEPT
Read: C-POPULATION drops every account outside Andrew's eight before the first write; LGIC conformance ledger **X18 (1)** records this as a
standing departure from R9, with its reason "all other domains/accounts should be dropped at the outset and not stored" (05:4xZ).
- The new premise names "any opal user". A takeover of an account outside the eight would be invisible today: a compromise question
  cannot be answered for an account that was never stored.
- External addresses: the old rule replaced every non-member address with a class token. For compromise response the outside
  recipient IS the exposure (O2): who got the forward, the share link, the phishing mail sent from the account.
- **REC:** collect every account in the Opal tenant (members and guests acting in it) and keep addresses as Microsoft records them.
  This retires X18 departure (1) and C-POPULATION's eight-name list; it needs Andrew's explicit word on the conformance ledger, because
  that entry carries his earlier verbatim instruction.

### F3 -- Fork 2, bronze: raw
Read: LGIC R9, "BRONZE IS RAW AND UNTOUCHED. Whatever the vendor shipped, byte-for-byte"; X18 notes the consequence of the reduced bronze:
"a population or field error cannot be repaired from bronze, and the source keeps 7 days". C-FIELDS hashes mail subjects, reduces
addresses to tokens and the IP to an office/remote flag.
- Andrew: "Silver is just formatted bronze in parquet for query." That describes raw bronze with a format change above it.
- The reduced fields are the forensic ones: the raw IP is the first compromise signal (where a session came from); the subject and the
  recipient are what remediation needs.
- **REC:** bronze raw, as Microsoft ships it, R9-conformant (X18 departure (1) retired in full: the population drop AND the field
  reduction; departure (2), the KMS key alias, is unaffected); silver the same events in parquet;
  any minimisation happens in what a read returns, not in what is stored. Protection comes from the door and the key (F1), not from
  reduction.

### F4 -- Fork 3, the sign-in feed: add it
Read: the PII read (line 19) lists four feeds on the same Office 365 Management Activity API: `Audit.Exchange`, `Audit.SharePoint`,
`Audit.AzureActiveDirectory`, `Audit.General`; C-FIELDS (a) left the Entra feed unsubscribed because, for workflows, it was "location
tracking, not workflow".
- For a compromise it is the core feed: the sign-in record is where a takeover starts and how its duration is fixed (O3).
- **REC:** subscribe `Audit.AzureActiveDirectory`. The PII read places it on the same API as the three feeds already collected; that it
  needs no permission beyond the app's existing `ActivityFeed.Read` is to be confirmed at L4 (Part V).

### F5 -- Fork 4, gold: per-person baselines and outside-baseline reads, no notification
Read: C-NOALERT; CLAUDE.md, "NEVER build an alert/alarm/SNS/SES-send/notification/freshness-checker/monitor unless Andrew explicitly asks.
Standing moratorium".
- Andrew's words are "identifying common patterns and establishing if a suspicious one appears" -- detection, not notification.
- **REC:** gold holds per-person baselines (O5) and an outside-baseline read the responder pulls through the door (O6). No alert, SNS,
  e-mail or monitor resource. Whether a flag should reach someone unprompted is his call (Part V); the moratorium stands until he says so.

### F6 -- What "seen" can mean depends on the tenant's licences
Read (web, 2026-10-16): Microsoft's guidance says logging of `MailItemsAccessed` (a mail opened or synced -- the "what was seen" event for
mail) needs an E5 or add-on licence per user; Microsoft announced it for Audit (Standard) in 2024, and sources conflict on whether that
rollout completed. File access events for SharePoint and OneDrive are standard.
- Sources: [Microsoft Learn: get started with auditing](https://learn.microsoft.com/hr-hr/purview/audit-get-started);
  [Office365ITPros, May 2024](https://office365itpros.com/2024/05/23/new-audit-events-may24/);
  [TrustedSec on MailItemsAccessed](https://trustedsec.com/blog/mailitemsaccessed-woes-m365-investigation-challenges).
- **Finding:** O2's mail half depends on a fact about Opal's tenant that the stored 7 days can answer (Part V).

### F7 -- Why the copy matters: Microsoft keeps more, but not out of reach
Read (web, 2026-10-16): Audit (Standard) retains records 180 days (90 days for records before 2023-10-17); Audit (Premium) one year;
the Management Activity API the collector reads serves only about the last 7 days.
- Sources: [Microsoft Learn: audit solutions overview](https://learn.microsoft.com/purview/audit-solutions-overview);
  [Splunk community thread citing the API limit](https://community.splunk.com/t5/All-Apps-and-Add-ons/Office-365-logs-ingest-more-than-7-days-history/m-p/257359).
- **Finding:** the copy's value is (a) history beyond Microsoft's retention and (b) a record an attacker with tenant admin cannot
  erase (O8). It is not the only record of the last 180 days, which also means a backfill beyond the API's 7 days is possible through
  Purview's audit search, at the cost of a different permission (a lever for L4, not an outcome).

### F8 -- Naming
Read: the issuer's record ("The macro `SOC2_MSLOGS` does not exist in `org/missions/MACROS.yaml` today"); the CTO reads it as macro
`SOC2`, project `SOC2_MSLOGS`. Estate codes are a four-letter macro plus a project suffix (TCKT_MTADTA, AMGT_HARVST).
- **Finding:** the CTO's reading fits the estate grammar; Andrew said "a new macro called SOC2_MSLOGS", so the split is worth one line
  back to him when the endpoint goes up for his "yes".

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- **Andrew's word retiring X18 departure (1)** (departure (2), the KMS key alias, is unaffected) and with it C-POPULATION and C-FIELDS,
  since those carry his own earlier verbatim instruction.
- **The tenant's audit setting is on, and its licences decide `MailItemsAccessed`** (F6): read from the stored days whether those
  events appear for the accounts collected today.
- **The sign-in feed is reachable under the existing permission** (F4), or the permission change is named.
- **A retention period for the copy**, set by Andrew (no number is proposed here).
- **His word on whether any flag may notify anyone** (F5). Until then, pull only.
- **Opal's position on monitoring every employee's activity** -- notice and policy are Andrew's to set; this brief does not advise on
  them.
- **The door gains the compromise reads** (O1-O4, O6) and keeps refusing direct reads; the listing rule (no person, address or file name
  in a key segment) survives the population change.
- **Gold has enough history to call a baseline**; how much is an L4 question, not a number here.

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured by `2.0.0_SA_COO~S1` and stated in its record @8f5176c374 (~16:0xZ 2026-10-16), not re-measured here:
- Live: the collector (two clean scheduled fires), the door (two aliases), `opal-data-trino/m365-metadata/trino/` with bronze, silver,
  gold-coverage and state, the Entra app with one permission, the group `globgrph-trino-access-group` with `Andrew_Berman`.
- Stored: 7 days of the eight's events, reduced per C-FIELDS.
- PRD `TCKT_MTADTA_PRD.md` v0.5, status DRAFT; registered under D7 / TCKT.
- The issuer cuts nothing for the reframe until the plan is locked (msg 6836).

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- It did not read the stored events, so it does not know which event types (including `MailItemsAccessed`) Opal's tenant emits.
- It did not confirm that `Audit.AzureActiveDirectory` needs no permission beyond `ActivityFeed.Read`.
- It does not set a retention period, a baseline window or any detection threshold.
- It does not rule on the rename-versus-new-project question (L3) or on placement (directive, box).
- It does not give legal or HR advice on monitoring employees.
- The licensing facts in F6 and F7 come from web sources read on 2026-10-16, two of which conflict on `MailItemsAccessed`.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/soc2-mslogs-compromise-exposure-brief-20261016.md
  PROJECT           TCKT_MTADTA (in flight; reframed) -> SOC2_MSLOGS (macro SOC2, per the CTO's reading; NOT in MACROS.yaml yet)
  EXISTING PRD      org/missions/D7/TCKT/TCKT_MTADTA/prd/TCKT_MTADTA_PRD.md (v0.5, DRAFT)
  ANDREW RECORD     org/tier1_exec/2.0.0_SA_COO~S1/ANDREW_DIRECT_20261016_1559Z_REFRAME_M365_LOGS_AS_SOC2_COMPROMISE_EXPOSURE_MACRO_SOC2_MSLOGS.md
  SIBLING PROJECTS  TCKT_VNEXT (relationship dropped); the later AWS Organization project; NFRA_WFSPINE (closed predecessor)
  PRIOR ART         the built collector, door, group, app, KMS key and prefix (F1); WFSPINE_AUDIT_CONTENT_AND_PII_20261016.md;
                    LGIC R9 and conformance ledger X18 (infra/logic/02_DOCTRINE.md, 06_CONFORMANCE_LEDGER.md)
  MEASURED AT       Part VI from the issuer's record, ~16:0xZ 2026-10-16; web facts F6-F7 read 2026-10-16 ~16:0xZ
```

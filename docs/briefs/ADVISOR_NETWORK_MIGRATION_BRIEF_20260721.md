# ADVISOR NETWORK MIGRATION — Master Brief

**Author:** 0.5.0_AE_OpalETL~Z · **Date:** 2026-07-21 · **Sponsor:** Andrew Berman (direct) · **Status:** DRAFT v1.0 — exploratory, not yet a registered project
**Origin:** surfaced from Alyssa Keith's CIOHunt package (received 2026-07-21)
**One-line:** Build a proprietary, Opal-owned relationship graph of the wealth-advisory world by migrating three data prongs — LinkedIn (social edges), Salesforce, and HubSpot (advisor books + structure) — into one canonical store.

---

## 0. Executive summary — the moat is the graph, not the app

Alyssa's CIOHunt is a capable OCIO-prospecting tool, but the durable, defensible asset it exposed sits one layer beneath it: **a relationship graph of the advisory world that Opal owns.** Prospecting engines, referral routing, relationship intelligence, and "who can warm-intro whom" are all *consumers* of that graph. The graph itself is the only component that is **hard to build** (multi-source entity resolution over consented, access-gated data), that **compounds** (denser and more valuable with every advisor's book added), and that once ingested is **first-party data Opal owns** and no vendor can reclaim.

**Advisor Network Migration** is the program to build it: three ingestion prongs feeding one **Advisor Network Graph**.

| Prong | Contributes to the graph | Difficulty | Priority |
|---|---|---|---|
| **1. LinkedIn** | the SOCIAL edges — who-knows-whom (no CRM holds this) | HARD | **PRIORITY (hero build)** |
| **2. Salesforce** | the advisor's ENTIRE book + structure (accounts, deals, notes, workflows, everything) | Easy — API-native | Parallel |
| **3. HubSpot** | the same shape, different vendor | Easy — API-native | Parallel |

LinkedIn is the strategic priority because it is the hardest and most defensible; the CRMs are straightforward authorized API pulls anyone could replicate, whereas the LinkedIn social graph is the unique asset no competitor can simply buy. The CRM prongs, however, are the **faster path to a populated graph** — so the recommended shape is parallel tracks (§9).

---

## 1. Provenance & context (CIOHunt — reference, not the build)

**How this arrived.** Alyssa emailed `CIOHunt_package.zip` on 2026-07-21 (subject "CIOHunt — OCIO prospecting engine"). Path on record: email attachment -> staged server-side to SharePoint `OpalOCIO / Shared Documents / CIOHunt_intake / CIOHunt_package.zip` -> downloaded locally -> extracted to `C:\Users\AndrewBerman\Desktop\CIOHunt_package` (37,951 bytes, sha256 `3a502f55c63a1046a9d2d70b5b71a4f4c4bc5c39a5c0f5c65b050aac26d640ef`, byte-verified identical).

**What CIOHunt is** (full assessment on file): a batch Python pipeline — no server, no API, no database — that screens SEC-registered RIAs (bulk Form ADV + IAPD), overlays web-sourced events (breakaways / departures / job postings), matches Alyssa's LinkedIn warm connections, scores each firm for OCIO fit deterministically, and renders a searchable console + dashboard + daily email. State of completion: the **scoring/targeting brain is ~85% and clean**; the **retrieval and productionization are early** (event sourcing is hand-curated; the "search" is a static in-browser filter over a baked-in snapshot; delivery is a local 9am Windows task whose cloud send path is broken).

**What is REUSABLE for this migration (carry forward):**
- The **SEC firm entity-spine** (`adv.py` / `adv_bulk.py`: SEC IAPD/ADV -> canonical firm identity + CRD + AUM/staff). This is directly the graph's **firm-resolution backbone**.
- The **LinkedIn CSV ingest** (`linkedin.py`, which already parses the member `Connections.csv`) — the seed of Prong 1.

**What is NOT the priority:** the CIOHunt prospecting *product* itself. It is a reference framework and a likely first *consumer* of the graph — we may reuse pieces, but we are not building CIOHunt. **The priority is the graph, led by the LinkedIn prong.** (Package inventory: Appendix B.)

---

## 2. The target — the Advisor Network Graph

A single Opal-owned graph store. The three prongs populate these nodes and edges:

```
        NODES                                   EDGES / PAYLOAD
   +---------------+  works-at        +-------------------------------+
   |  PERSON       |----------------->|  FIRM                         |
   |  (contact /   |                  |  (Account / Company /         |
   |   connection) |<----knows--------|   SEC-resolved RIA)           |
   +------+--------+  (person<->person)+--------------+---------------+
          |                                          |
   advises| owns-relationship            deal / opportunity
          |                                          |
   +------v--------+                          +-------v-------+
   |  ADVISOR      |----- has-book ---------->|  HOUSEHOLD    |
   |  (Opal user)  |                          |  (FSC group)  |
   +---------------+                          +---------------+
   PAYLOAD on nodes/edges: notes . tasks . calls . meetings . emails .
                           pipeline stage . AUM . workflow/structure
```

- **Why it's the moat:** hard to build (consented, access-gated, multi-source entity resolution), compounding (denser per advisor added), owned (first-party, non-reclaimable), and the substrate every future product sits on.
- **Entity spine:** FIRMS resolved via the reused CIOHunt SEC spine (IAPD/ADV -> canonical firm + CRD). PEOPLE resolved via email + normalized name + company + LinkedIn URN where present.
- **Store options (open decision, §11):** AWS Neptune (managed graph), a Kuzu-style embedded graph (the estate already runs Kuzu for `comp-graph` — a known pattern), or Postgres + adjacency. Data lands in S3 bronze/silver/gold per estate convention regardless.

---

## 3. Data sourcing & coverage-gap analysis (the honest read)

The graph is only as good as what each source can actually deliver. Ranked by where the real holes are:

1. **Warm graph (LinkedIn + CRM) — highest strategic value; manual/fragmented today.** This is the moat and the priority. See Prongs 1-3.
2. **FINRA is under-used — the best untapped regulatory signal.** CIOHunt never queries FINRA; it survives only as the shared CRD identifier and a "also-a-broker-dealer" flag. **FINRA BrokerCheck rep-level data** (an individual advisor's registration moving from a wirehouse to a new firm) is a *leading* breakaway indicator — weeks ahead of the trade press, which is where CIOHunt currently gets breakaways (lagging). Wiring it would make event detection proactive. Bigger lever than YCharts.
3. **SEC structural — complete for the sweet spot, with cracks.** The bulk ADV file is SEC-registered advisers only (~$100M+), so state-registered RIAs (<$100M) are invisible; it is a **manual point-in-time FOIA snapshot** with no auto-refresh (stale between pulls); and the IAPD name-token sweep (`universe.py`) is **explicitly approximate** — a firm whose name lacks the ~15 seeded tokens is missed. Not "complete," recall-limited.
4. **Web events — best-effort, and it under-covers the best targets.** Most mid-market CIO departures are never press-covered, so the news channel misses exactly the smaller firms that score highest. The structural thin-team signal silently covers them — which is why the two-channel design is sound, and why automating the web provider is worth less than fixing FINRA.
5. **YCharts — deprioritize.** Only applies to firms running their own registered fund (~212 of 5,273, ~4%). High signal for that slice, nothing for the other 96%, and it is price-only (needs total-return before acting). A differentiator for a sliver, not a lever.

**Directive priorities from this analysis:** (a) the proprietary warm-graph merge (LinkedIn + HubSpot/Salesforce, owned and compounding); (b) FINRA BrokerCheck rep-movement (future prong candidate). SEC auto-refresh is housekeeping; YCharts is optional polish.

---

## 4. PRONG 1 — LinkedIn Integration (PRIORITY)

**Contributes:** the social-edge layer (who-knows-whom) that no CRM holds.

### 4.1 The hard constraint (grounded against LinkedIn/Microsoft docs)
There is **no API** that returns a member's connections to a US self-serve developer:
- **Sign In with LinkedIn (OIDC)** — scopes `openid`/`profile`/`email`. Returns the member's own name/email/photo. **Zero connections.** (Self-serve: dev app + company page.)
- **Connections API** (`r_1st_connections`) — **partner-approval-gated** (legacy, effectively closed to new entrants), returns only the consenting member's **own 1st-degree**, and its payload is **thinner than the CSV** (first/last/id only — no company/title, which is exactly what maps a person to a firm).
- **Member Data Portability API** (DMA, `r_dma_portability_self_serve`) — self-serve and can return a rich member snapshot, but **EEA/Switzerland members only.** US advisors cannot consent. Unusable here.
- **There is no "siphon all connections instantaneously" path**, compliant or otherwise (scraping the graph is a User-Agreement violation with a litigation trail — hiQ — plus account/IP bans).

**Therefore** the compliant, richer mechanism is the member's own **"Get a copy of your data" -> Connections.csv** (First/Last/URL/Email/Company/Position/Connected On) — which `linkedin.py` already parses.

### 4.2 The mechanism — assisted-deeplink desktop app (advisor-driven, human-in-loop)
The manual export is dead-on-arrival at scale (log in, find a settings page, request, wait, download, email it to us). The productized version collapses it to **two human clicks separated by up to two days**, with Opal owning everything in between.

The design problem is precisely: **an async job (10 min–48h) with an unreliable notification** (LinkedIn sends one easy-to-miss email, and the eventual download *still* requires the advisor's live session, so a backend can never just fetch it). Three principles fall out:
1. **Own the notification.** Never depend on the advisor catching LinkedIn's email; *we* know a job is pending the moment they request it, and *we* drive re-engagement on channels we control.
2. **Completion is a resumable one-click, days later** — a re-engagement problem, not a keep-something-running problem.
3. **Zero background bot.** Never keep a headless session polling LinkedIn. Every LinkedIn interaction happens with the human present and driving. Between request and return, the only things running are ours (scheduler, comms).

**Server-side job state machine** (the durable object that survives the 48h; the desktop app is just the hands that complete it when the advisor is present):
```
IDLE --(advisor clicks "Get contacts"; app deep-links; advisor clicks Request)--> REQUESTED
REQUESTED --> PENDING <---- OUR re-engagement scheduler
                    |        nudges @15m . 2h . 8h . 24h . 48h
                    |        via opalinvest.dev email / desktop push / SMS / in-app badge
                    |        (NOT LinkedIn's email)
                    |  advisor returns (nudged OR opens app naturally)
                    |  -> app re-auth if session stale (assume it is) -> LIVE page check
        +-----------+-----------+
     not ready    READY     link expired
        |           |            +--> re-request --> REQUESTED
        +-----------+
                    v  advisor clicks Download INSIDE the app's browser;
                       app intercepts the download event (no filesystem for the advisor)
                DOWNLOADING -- Connections.csv only --> S3 intake --> INGESTED (graph updated)

  (N nudges ignored -> ABANDONED: soft-close; one tap restarts anytime)
```

**Design details that carry the weight:**
- **Request the connections-only (fast) export** to bias toward LinkedIn's minutes-path, but design for the 48h worst case.
- **Set expectations at request time** so the advisor stops watching LinkedIn: "we'll text/email you the moment it's ready — you don't need to watch for LinkedIn's email."
- **Session expiry across days is the norm** — never persist a session; one-tap re-login on every return, treated as routine.
- **LinkedIn's download link expires** (limited window/downloads) — hence prompt nudging once ready and a clean auto-re-request path when it lapses.
- **Download-catching is the whole reason for a desktop app** over a web app — a sandboxed web page cannot grab the file from Downloads, forcing a manual "find the zip, upload it" step that reintroduces the friction we are killing. The embedded-browser download interceptor (Electron `will-download` / CDP) makes it feel like one click.
- **Optional latency-killer:** advisor connects email read-only (or forwards LinkedIn's "ready" email to `intake@opalinvest.dev`) -> our backend catches it and fires the nudge instantly (a *trigger*, not a download bypass — the session is still required to download).
- **What leaves the machine:** only `Connections.csv`. No cookies, no credentials, no session ever hit Opal servers.

**Data mapped:** connection rows -> PERSON nodes; the Company field -> works-at edges (SEC-resolved); advisor->connection -> **knows edges** (the moat layer).

---

## 5. PRONG 2 — Salesforce API Migration

**Contributes:** the advisor's ENTIRE book AND its structure — accounts, contacts, deals, activities, notes, and (critically, under Financial Services Cloud) the curated human-relationship graph advisors maintain by hand.

**Object model (the book):** Account (firm/client), Contact / Person Account / Lead (people), Opportunity + OpportunityContactRole (deals + who is on them), Task / Event / Case (interactions), Note / ContentNote (notes), Campaign, AccountContactRelation (person affiliated with >1 firm), User (the advisor). Full field tables: Appendix A.

**Financial Services Cloud (FSC) — if the advisor runs it, this is gold.** FSC already carries a hand-curated human-relationship graph: **Household** (a business Account grouping a family), **AccountContactRelation** (household membership + roles), **ContactContactRelation** (person<->person: spouse, attorney, CPA, referral source), Financial Account (AUM), Group / Party Relationship Group / ReciprocalRole (financial circles + rollups). That is the *same who-knows-whom layer* we want from LinkedIn, except the advisor already built it — so pulling FSC is high-value.

**Extraction (grounded):**
- **Auth:** OAuth 2.0 Connected App — web-server flow (advisor consents) or JWT bearer (server-to-server). Scopes `api`, `refresh_token`, `full`.
- **Data (the book):** **Bulk API 2.0 query jobs** (REST, async): POST `/services/data/vXX.0/jobs/query` with a SOQL query -> poll `/jobs/query/{id}` to `JobComplete` -> GET `/jobs/query/{id}/results` as **CSV**. Up to **15 GB / ~150M records** per query (sequential or up to 5 parallel result URIs).
- **Structure (the "EVERYTHING"):** `sObject describe` (`/sobjects/{Object}/describe`) for full field schema incl. custom (`__c`) objects; `describeGlobal` (`/sobjects`) to enumerate every object; **Metadata / Tooling API** for Flows, workflows, validation rules, record types. => we clone both the DATA and the STRUCTURE.

---

## 6. PRONG 3 — HubSpot API Migration

**Contributes:** the same shape as Salesforce, different vendor — clean, modern model, straightforward full-book pull.

**Object model (objectTypeIds confirmed from docs):** Contacts (`0-1`), Companies (`0-2`), Deals (`0-3`), Tickets (`0-5`); engagements Notes (`0-46`), Tasks (`0-27`), Calls (`0-48`), Emails (`0-49`), Meetings (`0-47`); Owners (the advisor). Base endpoint `/crm/v3/objects/{type}`. Full property tables: Appendix A.

**Three pullable structural layers (all of them):**
- **Records** = data. `GET /crm/v3/objects/{type}?properties=...&associations=...&limit=100&after=<cursor>`.
- **Properties API** (`/crm/v3/properties/{type}`) = the schema incl. **custom properties** (structure).
- **Associations API** = the **edges** (`to.id` + `types[].associationTypeId`, e.g. `note_to_contact`, `deal_to_company`, `contact_to_company`) — the relationship graph. Pipelines (deals/tickets) = the advisor's workflow stages.

**Extraction (grounded):**
- **Auth:** OAuth 2.0 app (advisor installs, granting scopes) OR **private-app access token** (equivalent, simpler for single-tenant pulls).
- **Read scopes:** `crm.objects.contacts.read`, `.companies.read`, `.deals.read`, `.owners.read`, engagement/object scopes for notes/tasks/calls/emails/meetings, and `crm.schemas.*.read` for the schema. Full pull = paginate every object type + fetch associations + properties schema + owners.

---

## 7. The merge — one canonical schema absorbs all three

Salesforce and HubSpot are **near-isomorphic**; one canonical schema absorbs both, and LinkedIn adds the social layer:

| Canonical | Salesforce | HubSpot | LinkedIn |
|---|---|---|---|
| FIRM node | Account | Company (`0-2`) | Company field |
| PERSON node | Contact / Person Account / Lead | Contact (`0-1`) | Connection row |
| ADVISOR node | User (OwnerId) | Owner | the account holder |
| HOUSEHOLD node | Household / Group (FSC) | company / custom | — |
| works-at edge | Contact.AccountId / AccountContactRelation | contact_to_company | Company field |
| **knows edge** | ContactContactRelation (FSC) | associations | **the connection itself** |
| DEAL edge | Opportunity (+OpportunityContactRole) | Deal (`0-3`) + assoc | — |
| INTERACTION payload | Task / Event / Case | Tasks/Calls/Emails/Meetings | — |
| NOTE payload | Note / ContentNote | Notes (`0-46`) | — |
| WORKFLOW / structure | Metadata API (Flows, record types) | Pipelines + Properties schema | — |

**Entity resolution:** FIRMS via the reused CIOHunt SEC spine (IAPD/ADV -> canonical firm + CRD); PEOPLE via email + normalized name + company + LinkedIn URN. The **union across all advisors** is the proprietary graph — that union is the compounding moat.

---

## 8. Architecture (cloud, estate-native)

```
  per-prong connectors            landing            canonical            graph
  +------------------+          (bronze S3)         (silver)            (gold)
  | LinkedIn (assisted|--CSV---->                                    +--------------+
  |  desktop app)     |          +-----------+   +-----------+       | Advisor      |
  | Salesforce (Bulk  |--CSV---->| raw per-  |-->| canonical |------>| Network      |
  |  2.0 + describe)  |          | source +  |   | entity-   |       | Graph        |
  | HubSpot (v3 +     |--JSON--->| per-adv   |   | resolved  |       | (Neptune /   |
  |  associations)    |          +-----------+   +-----------+       |  Kuzu / PG)  |
  +------------------+                                               +------+-------+
                                                                            v
                                                          consumers: CIOHunt prospecting,
                                                          referral routing, relationship intel
```
- **Ingestion:** per-prong connectors (Lambda / containers) -> S3 raw landing (bronze) -> canonical entity-resolved transform (silver) -> graph load (gold).
- **Auth / entitlement:** per-advisor OAuth tokens (SF/HubSpot) + LinkedIn assisted; reuse the **MCP-gateway email->scoped-IAM** entitlement pattern (as in OPAL_TAXSMA) for per-advisor isolation.
- **Nudges / delivery:** SES on **opalinvest.dev** (DKIM/DMARC-aligned — estate standard, CLAUDE.md Rule 23).
- Fits the estate's bronze/silver/gold + comp-graph conventions.

---

## 9. Compliance & risk

- **LinkedIn:** the ToS constraint *is* the design — human-in-loop, member-consented export, no bot, no credentials/cookies to cloud, only the CSV leaves. This is the entire reason for the assisted flow (vs. the tempting-but-account-banning automation).
- **Salesforce / HubSpot:** the advisor owns their CRM data and authorizes the pull via OAuth — clean. But the payload is **their clients' PII + private notes** — treat as sensitive: encryption at rest, per-advisor isolation, retention policy, and a clear data-processing posture (Opal as processor of the advisor's client data). Entitlement-scoped so one advisor's book is never visible to another.
- **Governance:** if greenlit, register as an Opal project with a PRD + owner; the graph store and its access model are the SEV-class surfaces.

---

## 10. Build sequence

- **Phase 0 — Foundation:** canonical graph schema + reuse the CIOHunt SEC firm spine + pick the graph store.
- **Phase 1 — Parallel tracks:**
  - *CRM track (fast, low-risk):* HubSpot + Salesforce connectors -> first real, populated graph from authorized API pulls. Quickest path to a graph with real mass.
  - *LinkedIn track (priority, harder):* the assisted-deeplink desktop app + server-side job / re-engagement.
- **Phase 2 — Merge:** entity resolution across prongs; load the unified graph store.
- **Phase 3 — Consumers:** CIOHunt-style prospecting, referral routing, relationship intelligence on top.

**Tension, resolved:** LinkedIn is the strategic *priority* (the unique moat), but the CRM prongs are the *faster* path to a *populated* graph. Run both in parallel — LinkedIn leads on strategic weight, CRMs lead on time-to-first-graph.

---

## 11. Open decisions for Andrew

1. **Graph store:** Neptune (managed) vs Kuzu (estate-native pattern) vs Postgres+adjacency.
2. **Which CRM first / at all?** Do target advisors run Salesforce (likely FSC) or HubSpot predominantly? Decides the Phase-1 connector.
3. **Scope of "everything" from CRMs:** full clone incl. workflows/metadata/structure, or data-only v1?
4. **LinkedIn automation risk appetite:** assisted-only is assumed/confirmed. Confirm.
5. **Register as a project?** If yes: PRD + owner + gate the graph-store/access SEV surfaces.
6. **Consumer priority:** is CIOHunt prospecting the first consumer, or referral/relationship intelligence?
7. **FINRA prong?** Add BrokerCheck rep-movement as a fourth prong (leading breakaway signal) now or later?

---

## Appendix A — API reference (grounded)

### A.1 Salesforce standard objects
| Object | Is | Key fields | Graph role |
|---|---|---|---|
| Account | firm / client | Id, Name, Type, Industry, AnnualRevenue, NumberOfEmployees, ParentId, OwnerId | FIRM |
| Contact | person | Id, AccountId, FirstName, LastName, Email, Phone, Title, OwnerId | PERSON + works-at |
| Lead | unconverted prospect | Id, Name, Company, Email, Status, LeadSource, ConvertedAccountId, OwnerId | PROSPECT |
| Opportunity | deal | Id, AccountId, Name, StageName, Amount, CloseDate, Probability, OwnerId | DEAL edge |
| OpportunityContactRole | deal<->person | OpportunityId, ContactId, Role, IsPrimary | who is on a deal |
| Task | activity | Id, WhoId, WhatId, Subject, ActivityDate, Status, Description, OwnerId | INTERACTION |
| Event | meeting | Id, WhoId, WhatId, Subject, StartDateTime, EndDateTime, OwnerId | INTERACTION |
| Note / ContentNote | note | (classic) ParentId, Title, Body / (modern v35+) Title, Content, ContentDocumentLink | NOTE |
| Case | service | Id, AccountId, ContactId, Subject, Status | interaction |
| AccountContactRelation | contact<->account (M:N) | AccountId, ContactId, Roles | affiliation edge |
| User | the advisor | Id, Name, Email | ADVISOR |
| **FSC:** Household / Person Account / ContactContactRelation / FinancialAccount / Group | relationship + AUM layer | Household ID, roles, person<->person relations, AUM | HOUSEHOLD + knows edges |

### A.2 HubSpot objects
| Object | objectTypeId | Endpoint | Key properties |
|---|---|---|---|
| Contacts | 0-1 | /crm/v3/objects/contacts | email, firstname, lastname, company, jobtitle, phone, lifecyclestage, hubspot_owner_id |
| Companies | 0-2 | /crm/v3/objects/companies | name, domain, industry, annualrevenue, numberofemployees |
| Deals | 0-3 | /crm/v3/objects/deals | dealname, dealstage, amount, closedate, pipeline, hubspot_owner_id |
| Tickets | 0-5 | /crm/v3/objects/tickets | subject, hs_pipeline_stage, hubspot_owner_id |
| Notes | 0-46 | /crm/v3/objects/notes | hs_note_body, hs_timestamp, hubspot_owner_id, hs_attachment_ids |
| Tasks | 0-27 | /crm/v3/objects/tasks | hs_task_subject, hs_task_body, hs_task_status, hs_timestamp |
| Calls | 0-48 | /crm/v3/objects/calls | hs_call_title, hs_call_body, hs_call_duration, hs_timestamp |
| Emails | 0-49 | /crm/v3/objects/emails | hs_email_subject, hs_email_text/html, hs_timestamp |
| Meetings | 0-47 | /crm/v3/objects/meetings | hs_meeting_title, hs_meeting_body, hs_meeting_start_time |
| Owners | — | /crm/v3/owners | id, email, firstName, lastName |

### A.3 Sources (official docs)
- Salesforce Bulk API 2.0 Query: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/query_bulk_api_2_0.htm
- Salesforce Note / ContentNote: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_note.htm
- Salesforce FSC data model: https://help.salesforce.com/s/articleView?id=ind.fsc_admin_data_model.htm&type=5
- Salesforce FSC ContactContactRelation: https://developer.salesforce.com/docs/atlas.en-us.financial_services_cloud_object_reference.meta/financial_services_cloud_object_reference/sforce_api_objects_contactcontactrelation.htm
- HubSpot CRM object model: https://developers.hubspot.com/docs/guides/api/crm/understanding-the-crm
- HubSpot Notes engagement API: https://developers.hubspot.com/docs/guides/api/crm/engagements/notes
- HubSpot OAuth scopes: https://developers.hubspot.com/docs/guides/apps/authentication/scopes
- LinkedIn Connections API: https://learn.microsoft.com/en-us/linkedin/shared/integrations/people/connections-api
- LinkedIn Member Data Portability (DMA): https://learn.microsoft.com/en-us/linkedin/dma/member-data-portability/member-data-portability-member
- LinkedIn Sign In (OIDC): https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin-v2

## Appendix B — CIOHunt package inventory (provenance)
`CIOHunt_package.zip` (37,951 B, sha256 3a502f5…) contents: `backend/` (13 Python modules — model, scoring, engine, adv, adv_bulk, universe, delta, linkedin, performance, intros, render, console_render, email_digest, send_digest), `README.md`, `CIOHunt_Daily.ps1` (local scheduler), `data/seed_candidates.json` (8-firm event seed — the only shipped data; the 5,273-firm SEC universe + 72 warm firms live on Alyssa's machine). Extracted to `C:\Users\AndrewBerman\Desktop\CIOHunt_package`.

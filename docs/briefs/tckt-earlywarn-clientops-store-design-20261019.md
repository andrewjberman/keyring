# TCKT_EARLYWARN: the client-ops findings store, twice-daily scans, and warnings over the gateway (design brief)

**Author:** `4.0.0_SA_CRO~DELL1` (L1, MIDSTREAM) | **Date:** 2026-10-19 | **Project:** TCKT_EARLYWARN (D7 / TCKT, fast-path)

**Authority:** Andrew-direct record addendum 7,
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261016_1801Z_CLIENT_OPS_EARLY_WARNING_FAST_PATH.md`. His words,
verbatim:

> I think what needs to happen is that there is a database that holds all of this information with regular scans at 9a every day
> and 4p every night, naive eastern time. This will be held in a bucket like opal-data-clientops. then we can connect users to this
> bucket and they can ask for warnings on various surfaces that our scanners are providing. I want you to formalize this design, it is
> the same pattern we are developing across the platform with NFRA_OPLGTW/MCPINDEX, e.g. how we have a "Security Analysis"
> application dashboard for Asset Management that is fed by opal-data-harvest which is accessible via a tool index for users over
> opalgateway mcp.

**Standing law carried, not re-opened:**
- Addendum 5: findings only, never a client-facing recommendation.
- Addendum 6: the approved thresholds, owners and digest shape.

---

## PART 0: how the blind constraint was honoured, and where it bent

**Where it bent.** A midstream brief is written blind to the open task orders. This one bent in two places:
- I read the deployed build (`infra/aws/ec2/client-ops-early-warning/`) and both task orders (`TO-EWS-d1`, `TO-EWS-d2`), because the
  store's current home is a fact the design must start from.
- That home is decided in `TO-EWS-d2`'s amendment (`TCKT_EARLYWARN.TO-EWS-d2.persist-store-and-log-items.md:13`), so I read it.

**The risk.** A ratifying outcome could enter here: "keep the store where it is".

**How it was handled.** Part IV judges the current home against the doctrine. It does not take the home as given. The finding is
that the home is conformant for today's 49F-only scope, and that it stops being conformant the moment a second firm's findings
arrive.

---

## PART I: the outcome territory (things a person can do)

**Candidate thread (FWD-1 shape).** An Opal ops user asks Claude, through the opalgateway MCP, "what client-ops warnings are open
for 49 Financial on the money rules?". The answer lists each open finding with:
- client initials and the account's last 4;
- the rule, the state, and how long it has been open;
- the evidence: the Schwab row, or the mail id.

The answer comes from the 09:00 or 16:00 snapshot, and it states which. Scope for the thread:
- one firm (49 Financial);
- one rule family (Sleeping Money, Fee Tripwire, Payday Guard);
- the latest snapshot.

### O1. Ask for open warnings by firm, rule and state

An Opal staff member asks, in plain English, for the client-ops warnings that are open now for a firm they are granted, filtered
by rule, state or age. They get the findings with evidence and the snapshot time.

### O2. Ask when we first knew

The same person asks "when did a warning first fire on this account, or this email thread?". They get the dated event history:
- opened;
- moved to WARN and OVERDUE;
- closed, and by what.

This answers the postmortem question (the Victor case) without re-reading mail.

### O3. See a firm's summary

A team lead asks for a firm's (or all granted firms') open and overdue counts per rule, and the trend since a date.

### O4. Read the same truth on the dashboard and the TV

The portal client-ops view, the office TV and the 08:00 CT digest read the same served objects the tools read. A number seen on
the TV equals the answer Claude gives for the same snapshot.

### O5. Audit a snapshot

Anyone with the grant can reopen the 09:00 or 16:00 snapshot of any past trading day and see exactly what was open then. Every
snapshot is durable, dated and never rewritten.

### O6. Discover it through the index

A staff member who does not know the tools exist asks "do we have anything on client-ops warnings?". The index's discover family
routes them to the right tool, with the dataset's meaning, freshness and firm-scope rule.

---

## PART II: where the boundary sits

| Owns | Project | Relies on |
|---|---|---|
| The scanners (six rules), the clock, the findings data at every tier, the 09:00 and 16:00 schedules, and the served objects for portal, TV and digest | **TCKT_EARLYWARN** | Schwab silver in `opal-data-assets` (R4), and the mail feed (Graph app-only, or the /hx/mail bridge) |
| The `clientops_*` gateway tools: their code, entitlement wiring, envelope and tool-count tests | **NFRA_OPLGTW** (gateway engine and grant model, `org/standards/NFRA_OPLGTW_CONTRACT.json`) | TCKT_EARLYWARN's served objects |
| The catalog rows, the discover routing, and the C2 classification gate | **NFRA_MCPINDEX** (`org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md` C1-C8) | the tools above |
| The new registry rows (system, scope, tenancy) and the firm-bucket fence rows | **LGIC** (`infra/logic/registry/`, `lib/opal_naming.py`) | Andrew's call on tenancy (Part IV.2) |
| The client-ops page and the TV view | **portal** (`/api/scoped/*` pattern) | TCKT_EARLYWARN platinum |

**Not owned here:** any client or advisor outreach (addendum 5), and the mail grant itself (Andrew / the Global Admin, addendum 4).

---

## PART III: the qualitative bar

- An ops user answers "what is slipping right now for this firm?" from Claude. They would otherwise have scrolled 49@ or waited for
  an advisor to ask.
- A postmortem is written from the event history, not reconstructed from mail threads, as the Victor one had to be.
- The TV, the digest and Claude never disagree about the same snapshot. A disagreement is a defect (MCPINDEX C5), not a caveat.
- A staff member granted one firm cannot see another firm's warnings by any phrasing (MCPINDEX C7).

No numbers are set here. Thresholds and SLAs are addendum 6's. Volumes are measured, not targeted.

---

## PART IV: the substrate (findings, each with what was measured)

### IV.1 The reference pattern, end to end (harvest, Security Analysis, gateway, index)

**Storage tiers inside one bucket.** Harvest keeps its tiers in one bucket. Prefixes seen in a served response read on
2026-10-17:
- `amgt/harvest/bronze/research-report-extract/...`
- `amgt/harvest/silver/research-report/date=.../part-*.parquet`
- `amgt/harvest/gold/research_dossier/security_key=.../as_of=....json`

Harvest is GENERAL tenancy, so the whole pipeline lives in `opal-data-harvest`:
- `infra/logic/registry/tiers.json:46`, the GENERAL platinum home;
- doctrine R6 non-application, `infra/logic/02_DOCTRINE.md:396`.

**Schedules.** Harvest's scheduled producers are Lambdas on EventBridge Scheduler in `infra/aws/terraform/harvest/`
(chatter-axis, freshness-snapshot), per this seat's research
`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_AMGT_HARVST_DOSSIER_REFRESH_HOST_20261018.md` (commit `25586b74c0`).

**Gateway tools.**
- They admit first, read only through one typed base, and answer in a fixed envelope (`as_of`, `source_keys`, `denominator`,
  `absent_reason`): `infra/aws/ec2/opal-gateway/app/harvest_typed.py:1-12, :25-26`.
- Each dataset has a stated newest-object rule (`harvest_research.py:1-35`).
- One object read is capped at 64 MB, and the output is projected to 50 KB (`harvest_typed.py:23-24`).

**The dashboard.** Security Analysis reads `/api/scoped/amgt/*`, served by `lib/research/api/scoped_amgt.py`:
- behind CloudFront `auth-validator-edge`, which injects the firm and role from the portal JWT;
- "the firm is never sent by the client" (`portal/src/api/endpoints/amgt-lead-panel.ts:1-31`).

**The index.**
- One catalog home, `app/refs/DATA_CATALOG.yaml` (header lines 1-9).
- The discover family: `opal_discover`, `opal_describe` (`app/integrations/opal_discover/integration.py:941, :951`) and
  `gateway_query_catalog` (`app/integrations/portal_index/integration.py:481`).
- The MCPINDEX contracts:
  - C1, one catalog with one writer (`NFRA_MCPINDEX_PRD.md:350`);
  - C2, no tool without a catalog entry plus a `destructive_ops` / `data_entitlement` classification, with the pinned tool-count tests
    moving (`:372`);
  - C3, tool names `{system}_{function}[_{qualifier}]`, with the firm always an argument, never folded into the name (`:379`);
  - C4, the envelope (`:389`);
  - C5, portal parity (`:393`);
  - C7, isolation: one fenced read role per property, and a firm-bucket read is its own role (`:406`).

**Entitlement.** Per-principal `data_entitlement` records, versioned, keyed by Entra tid and oid. The scope names masters, datasets,
accounts, dates, columns and operations, plus optional portal channels (`app/data_entitlement.py:1-25`).

**Finding.** The pattern Andrew names is:
1. one producer writes tiered data to its home;
2. a typed gateway tool reads the served tier through an admit-first base with a fixed envelope;
3. a catalog row makes it discoverable;
4. the portal reads the same served objects through the scoped route.

Client-ops can follow it step for step. **The one place it cannot copy harvest is tenancy** (IV.2).

### IV.2 Tenancy: one `opal-data-clientops` bucket, or the firm buckets? (THE judgement)

**The data is attributable to one firm.** Every finding names a firm's client account (a Schwab account of a firm's master) or a
firm advisor's email thread.

**The doctrine says:**
- **R7** (`02_DOCTRINE.md:415`): a slice "ATTRIBUTABLE to one firm, at ANY grain ... is that firm's data: firm bucket, gold AND
  platinum, MANDATORY". A cross-firm composite attributable to no firm may live in a product bucket. "The product pipeline's CODE
  lives in the product bucket regardless (R5); a product pipeline writes to N+1 homes."
- **R6** (`:396`) quotes `ADVI_APISCP_PRD.md` section 2 as NON-NEGOTIABLE: "partner data never enters a shared bucket".
- **CLAUDE.md NEVER-rule:** no pipeline tree references another firm's data by BUCKET or KEY-PREFIX.
- **Harvest's single-bucket shape is legal only because harvest is GENERAL tenancy** (`tiers.json:46`). Client-ops is not.

**Shape A: product bucket plus firm buckets (N+1 homes).** RECOMMENDED. It is the doctrine's own shape.
- **`opal-data-clientops`, the product bucket, holds:**
  - the pipeline CODE (R5, R16);
  - the rule catalog and schemas;
  - cross-firm de-identified composites (counts per rule and state, no account or name: R7's composite case, which needs an R20
    register line stating the de-identification basis);
  - non-firm state.
- **Each firm's findings live in that firm's bucket**, at every tier, under the client-ops source:
  - `opal-data-49financial/<clientops>/49financial/{silver,gold,platinum}/...`
  - the same for `-inflection` and `-cottonwood`.
- **Today's store is already this shape for 49F.** It sits at `schwab/49financial/state/ews_store/current/` in
  `opal-data-49financial`, admitted by a fence row (`TO-EWS-d2.md:13`).
- **The gateway tool reads firm buckets** through a firm-bucket read role (MCPINDEX C5 and C7 already name this as its own role),
  scoped by the principal's grant.
- **Users never "connect to a bucket".** They connect to the tool, which is the boundary. That matches Andrew's intent ("connect users
  ... ask for warnings") without putting client data in a shared bucket.

**Shape B: one shared `opal-data-clientops` bucket, firm prefixes plus IAM conditions.**
- The shape Andrew's sentence describes literally.
- It violates R7 and the R6 non-negotiable. It is the exact shape the NEVER-rule names ("KEY-PREFIX").
- Legal only as a **declared R20 departure Andrew acknowledges** (`02_DOCTRINE.md:573`).
- Its isolation would rest on IAM prefix conditions alone. MCPINDEX C7 notes this is how silver already works ("the fence IS the
  isolation and there is no bucket boundary behind it"), and it is the weaker shape.

**For Andrew:**
- Shape A gives him the bucket he named (`opal-data-clientops`) for code, catalog and composites. Each firm's warnings stay in that
  firm's bucket.
- Users see one tool either way.
- Shape B is a one-line ruling from him, but it is a departure from his own canon. I recommend A.

**Builder output, printed 2026-10-19:**
- `address('clientops', '49financial', 'gold', 'findings', ...)` is **REFUSED**: "source 'clientops' is not a systems.json key".
- `name('clientops', None, 'scan', 'lambda')` is **REFUSED**: "system 'clientops' is not a systems.json key".
- Control, an existing system on a firm scope: `address('tradeops', '49financial', 'gold', 'findings', 'date=2026-10-19')` gives
  `s3://opal-data-49financial/tradeops/49financial/gold/findings/date=2026-10-19`. That is the firm-bucket shape A uses.
- The deployed build names its resources under the reserved `opal` system, for example `name('opal', None, 'clientops', 'task',
  'ews')` (`ews/names.py:25-30`).

**Missing registry rows (rule 30: a refusal is a row to add, never a typed workaround):**
1. `infra/logic/registry/systems.json`: a `clientops` system row (owner directive D7, project TCKT_EARLYWARN).
2. `infra/logic/registry/scopes.json`: a `clientops` PRODUCT scope. Today's PRODUCT keys are mdpf, etfs, irpt, harvest, transcripts,
   trino.
3. `infra/logic/registry/tiers.json`: its tenancy, PRODUCT, so findings home in the firm buckets per R7 under shape A.

The bucket name `opal-data-clientops` is then whatever the bucket builder renders for that scope. This brief does not type it.

### IV.3 The store as tiers (R9-R12, R21)

| Tier | What it holds | Home (shape A) | Rule |
|---|---|---|---|
| bronze | The raw scan inputs Opal does not already hold: the mail metadata pulled per scan (Graph or /hx/mail rows, as received). Schwab inputs are NOT copied; they are read from `opal-data-assets` silver (R4, R18 no dual-write). | firm bucket | R9 (raw, untouched) |
| silver | The append-only finding-event log: one typed, deduplicated parquet row per transition (opened, warn, overdue, closed, expired, dismissed, with reason), event-triggered | firm bucket | R10 |
| gold | The full-history findings table and the per-snapshot open-items table, keyed by snapshot `(trading_date, 09:00 or 16:00 ET)`. Snapshots are written once, never rewritten (O5). | firm bucket | R11 (parquet, full history) |
| platinum | The served JSON for portal, TV and digest: open items, per-rule summary, snapshot id. The estate's publisher is the JSON producer. | firm bucket | R12 |
| composites | Cross-firm counts per rule and state, de-identified | `opal-data-clientops` | R7 composite case plus an R20 line |
| state | Cursors, deltaLinks, watermarks, the live SQLite working copy | the bucket whose tenancy it belongs to, under `.../state/` | R21 |

**Carried over unchanged:** the build's event model already appends every transition (the store's event log, `ews/store.py`), so
silver is an export of what exists, not a new model.

### IV.4 The schedules (09:00 and 16:00, naive Eastern)

**Two EventBridge Scheduler schedules**, timezone `America/New_York` ("naive eastern time": local wall clock, so EDT and EST follow
automatically):
- `cron(0 9 * * ? *)`
- `cron(0 16 * * ? *)`

Names come from `name()` once the system row exists. Each fire is one SCAN:
1. run the daily rules on the latest complete Schwab date;
2. sweep mail since the last scan;
3. age every item on the business-hour clock;
4. write the snapshot to gold;
5. publish platinum;
6. record the snapshot id the tools will quote.

**What runs when:**
- **Daily rules:** CLAUDE.md requires production on a schedule, never success-of-upstream alone. The current build's Schwab trigger
  is the file landing (`ews/config.py:143`), and the two schedules become its backstop and its publishing cadence.
- **Mail:** the 5 s stream and the bridge keep feeding the silver event log continuously. The scans only freeze and publish. This
  keeps "5 s detection" (addendum 2) and "twice-daily answer" (addendum 7) both true without a second pipeline (R18).
- **Every day or trading days only:** Andrew said "every day". The Schwab rules no-op on a non-trading date
  (`lib/trading_calendar.py`), while mail aging already ignores non-business hours. Whether weekend scans publish at all is OPEN in
  Part VII.

**Host.** R13 says silver to gold is Lambda unless genuinely heavy. The deployed container stays for the always-on mail stream, and
the two scans can run as Lambdas or as a task in that container. This brief does not sequence it (Part V).

### IV.5 The gateway tools and the index entry

**Tools.** Names follow MCPINDEX C3, with the firm always an argument:

| Tool | Inputs | Returns |
|---|---|---|
| `clientops_list_warnings` | `firm`, `rule?`, `state?` (open, warn, overdue, closed, expired), `since?`, `snapshot?` | open findings with evidence |
| `clientops_get_warning` | `item_id` | one finding with its full event history (O2) |
| `clientops_get_history` | `firm`, plus `account_last4` or a conversation ref, `from`, `to` | "when did we first know" |
| `clientops_get_summary` | `firm?`, `snapshot?` | counts per rule and state (O3) |
| `clientops_describe_rules` | none | the six rules, thresholds and owners (addendum 6) |

**Contract for every tool:**
- **Envelope:** `as_of` (the snapshot id), `source_keys`, `denominator`, `absent_reason`, per C4 and the harvest base.
- **Content:** findings only, and no recommended action (addendum 5).
- **Display:** initials plus last 4 by default (addendum 3's display rule).
- **Entitlement:** Opal staff only (C8). Firm scope comes from the principal's `data_entitlement` grant, extended (never forked, C7)
  with the firms it may read. A firm outside the grant is refused with the same answer as a firm that does not exist.
- **Classification:** `destructive_ops: none`, plus a `data_entitlement` class; the pinned tool-count tests move with the tools (C2).

**Catalog.** One `DATA_CATALOG.yaml` row per dataset (findings, open-items snapshot, summary), carrying the C1 fields:
- business meaning and example questions ("what's open for 49F", "when did we first flag account 0650");
- grain (finding / snapshot);
- freshness (snapshot time);
- firm-scope rule (one firm per call unless granted several; never summed across firms except the de-identified composite);
- producer (TCKT_EARLYWARN) and the tools that serve it.

`opal_discover("client ops warnings")` then routes to them (O6).

**Portal and TV.** They read the same platinum through a `/api/scoped/clientops/*` route behind `auth-validator-edge`, the Security
Analysis pattern, which gives parity with the tools by construction (C5).

---

## PART V: what must be true (named, not sequenced)

- The registry rows of IV.2 (system, scope, tenancy) exist.
- Andrew rules the tenancy shape: A, or B with an R20 entry.
- Per-firm fence rows exist in `infra/logic/registry/exemptions.json`, for the producer role (write) and the gateway read role
  (read), one firm bucket at a time.
- The gateway grant model is extended for a firm list (NFRA_OPLGTW).
- The catalog writer named by MCPINDEX C1 exists and adds the rows.
- The mail feed: the Graph app-only consent plus the access policy, or the /hx/mail bearer plus domain table (addenda 2 and 4).
- The account-identity display (raw last 4) for the gateway's staff principals (addendum 3, routed to NFRA_OPLGTW).
- The portal route and page for client-ops (portal lane), and the digest Teams channel (addendum 6, OPEN).

---

## PART VI: status (NOT OUTCOME-BEARING; measured 2026-10-17 to 2026-10-19)

- **Deployed:** one container on ECS (taskdef :2). The rules are live on Schwab silver for 49F, and the store persists to
  `opal-data-49financial` `.../state/ews_store/current/`.
- **First durable pass, over 573 dates** (`1.0.0_SA_CTO~DELL1` msg 7546):

  | Rule | Opened | Still open |
  |---|---|---|
  | Sleeping Money | 2,829 | 114 |
  | Fee Tripwire | 751 | 96 |
  | Payday Guard | 125 | 0 |

- **Measured load:** about 5.7, 1.2 and 0.4 opens per business day respectively (`scratchpad livescan/ews_store_churn.md`).
- **Inbox Radar:** runs as a 30-minute session scan on Andrew's mailbox (BRIDGE, addendum 4). It is not yet in the container.
- **Not built:** Rule Change Relay, Report Proofer; and no gateway tool, catalog row, portal page or TV view exists.

---

## PART VII: what this brief does not claim

- It does not claim that Shape A's per-firm read role is cheaper or simpler than B's. It claims A is the doctrine's shape.
- It does not decide whether weekend and holiday scans publish (Andrew said "every day"), or which host runs the two scans
  (Lambda or the existing container).
- It does not claim a query engine beyond what is cited. The harvest base reads parquet and JSON directly from S3. A `trino` PRODUCT
  scope exists in `scopes.json`, but this brief did not verify any client-ops use of it.
- It did not re-measure the gateway grant model's live state; it reads the code as committed.
- Inflection and Cottonwood findings do not exist yet; today's scanners read 49F Schwab and one mailbox. The tenancy judgement is about
  what arrives next.
- It types no bucket or resource name. Every name above is either builder output printed here, or blocked on a named missing row.

---

## REFS

| Ref | Value |
|---|---|
| BRIEF PATH | `docs/briefs/tckt-earlywarn-clientops-store-design-20261019.md` |
| PROJECT | TCKT_EARLYWARN (`org/missions/D7/TCKT/TCKT_EARLYWARN/project.json`) |
| EXISTING DESIGN | `docs/briefs/client-ops-early-warning-design-20261016.md` |
| AUTHORITY | the Andrew-direct record, addenda 1-7 (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261016_1801Z_CLIENT_OPS_EARLY_WARNING_FAST_PATH.md`) |
| SIBLING PROJECTS | NFRA_OPLGTW (`org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md`); NFRA_MCPINDEX (`org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md`); LGIC (`infra/logic/02_DOCTRINE.md`, `infra/logic/registry/`); portal |
| PRIOR ART | `infra/aws/ec2/opal-gateway/app/harvest_typed.py` (the typed base); `app/data_entitlement.py` (the grant); `app/refs/DATA_CATALOG.yaml` (the catalog); `app/integrations/opal_discover/integration.py` (discover); `portal/src/api/endpoints/amgt-lead-panel.ts` plus `lib/research/api/scoped_amgt.py` (the scoped route); `infra/aws/ec2/client-ops-early-warning/` (scanners, store, digest) |
| MEASURED AT | 2026-10-19 ~14:5xZ: builder runs; doctrine, PRD and code lines read at HEAD of box/dell1 |

```json
{
  "project": "NFRA_MCPINDEX",
  "directive": "D9",
  "fabric": "site-z",
  "prd_version": "v0.5",
  "step": 4,
  "brief_ref": "docs/briefs/opal-mcp-tool-index-brief-20260917.md@826ac6925a",
  "endpoint_outcomes": [
    "FWD-1",
    "FWD-2",
    "FWD-3",
    "FWD-4",
    "FWD-5",
    "FWD-6",
    "FWD-7",
    "FWD-8",
    "FWD-9",
    "FWD-10"
  ],
  "status": "DRAFT"
}
```

# NFRA_MCPINDEX - the Opal MCP tool index: every Opal data property answerable in Claude, from one catalog

## Authority and project arc

Author and accountable CTO: `1.0.0_SA_CTO`. Directive D9, Opal Workflows; macro NFRA; execution fabric laptop.

Andrew commissioned the scope at the `4.0.0_SA_CRO` terminal on 2026-09-17 and answered five cards there, all verbatim in
the brief: tool names follow the LGIC naming canon; the catalog is versioned in S3; the project sits under D9; Opal staff
only, beta one person at a time; the portal's precomputed tables are read as they are, while `opal-data-assets` silver is
queried live. He confirmed the ten endpoint outcomes at this terminal on 2026-09-17 ~19:0xZ ("1 approved"), recorded at
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260917_190xZ_OPEN_CALLS_SEVEN_ANSWERED_SEAT_SEQUENCE_IRPT_MCPINDEX_TAXSMA.md`
@57a15b2bbe.

The product: a staff member signed in with their Microsoft account asks Claude a plain-English question about Opal's own
data and gets an answer from the right source, with its date, its scope and its limits stated. A small discover family
indexes everything else, so the model is never guessing which tool to call. **The problem this exists to solve is stated in
his words: the official plugins are poorly indexed, and we will not have that problem.**

The header stays DRAFT until both halves are signed at L4-R. The author signs neither half.

**v0.4 (2026-09-17 ~23:5xZ)** answers `3.0.0_SA_CVO`'s refusal of the v0.3 ratified-text half @`7fef989e77`. The ten
outcome cards are now TRANSCRIBED from the ratified pin verbatim -- statement, DONE WHEN, ACCEPT and PROOF -- with only
SOURCE dropped, in the shape NFRA_SPMOVE already uses. v0.2 and v0.3 carried a COMPRESSED paraphrase, and the
compression was collateral from the v0.2 repair: fixing the markdown-table defect, this seat rebuilt the cards from the
TABLE'S one-line summaries instead of re-reading the endpoint document, so a formatting fix silently became a content
loss. What went missing were the operative constraints -- FWD-3's "transactions are reachable, not only the three
`dim_*` tables", FWD-8's "no new vendor egress beyond Andrew's standing per-use word", FWD-9's "removal takes effect
without a redeploy". The gate never asked for the compression: `FWD_DEF_RE` reads the `FWD-N <text>` line alone, so
carrying ACCEPT and PROOF costs it nothing.

**v0.3 (2026-09-17 ~23:3xZ)** answers `2.0.0_SA_COO~B`'s refusal of the v0.2 brief half @`980007578e` (review
`org/tier1_exec/2.0.0_SA_COO~B/deliverables/PRD_REVIEW_NFRA_MCPINDEX_v0.2_BRIEF_HALF_20260917.md` @`1586ebdefe`). Its
finding was that BRIEF COVERAGE was a six-line PARAGRAPH with no denominator, claiming six non-claims were carried where
two were -- so the section that exists to make carriage checkable was itself unfalsifiable. v0.3 replaces it with the
table shape `NFRA_SPMOVE` v0.3 was held to an hour earlier: 20 headings with the denominator re-measured at the brief's
own pin, PART V mapped 9 of 9 with holders, PART VII carried 6 of 6. The items it named as absent are now IN the
document and each decides something: VII.4 (Bloomberg is the SITEZ read) becomes a SCOPE LIMIT on S10 and A8; VII.5
binds L5 to print the bytes at a cited line; VII.6 marks the scoping record as research and names the overrule; V.4's
two registries and the pinned tool-count movement are in C2 and A11; V.8 names
`NFRA_INTEGRATIONS_STANDARD.md` s.6/8.1; IV.5's table families give A2 its denominator; IV.6's firm-bucket advisor
intelligence is a separate grant in C5 and C7; PART III's beta bar is S8's standing input; and S4 records that the
`fact_*` tables are unexposed while FWD-3 promises transactions. CONTRACTS changed at C2, C3, C5 and C7.

**v0.2 (2026-09-17 ~23:0xZ)** answers `2.0.0_SA_COO~G`'s L4-R brief-half refusal @`acb5fc61cc`: C1's named single
writer disclaims the live catalog in its own bytes, so C1 is re-cut to make identifying the live writer S1's first act
with a census bar rather than a reading. Also, the ten outcome cards are now carried in the form the step-4 gate's own
matcher reads -- v0.1 carried them as a markdown TABLE, which that matcher cannot see, so the outcomes were invisible
to the consumer while looking complete to a reader.

## Scope and evidence boundary

**This project owns:** the catalog (its schema, its versioned S3 home, its generation into the Gateway), the discover
family, the per-property purpose-built tools, the generalisation of the typed query engine beyond Schwab, one fenced read
role per property, and the per-property analysis that decides which questions become tools.

**It relies on and does not change:** the Gateway's sign-in, tiers, guard and audit; `app/refs/DATA_CATALOG.yaml` itself
(its CONTENT is extended by this project; whether it has a live writer at all is C1's open question, not an assumption); the Schwab query engine and grant model built by NFRA_OPLGTW; the silver tables and their producers; the
portal's precomputed tables and their publishers; the naming canon and registry.

**Explicitly NOT this project's:** enabling the five Schwab tools in deployment (NFRA_OPLGTW's act); the admin screen that
grants access (the mcportal brief); new precomputed tables (none are asked for); partner or client access (zero, under his
standing 2026-08-20 ruling); Tax SMA tools (until D9's tax work lands); any new vendor egress (YCharts and Bloomberg stay
on his per-use word).

**Evidence boundary.** The brief measured the repository only: no AWS state was read, table sizes and query timings over
silver are unmeasured, and the per-property "common questions" are not enumerated anywhere yet. **Every capacity claim in
this PRD is therefore DESIRED until a cell exercises it**, and the first analysis cell of each property carries the
measurement.

## ENDPOINT (step 2, /endpoint --forward)

The ten outcomes are `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_MCPINDEX_ENDPOINT_FORWARD_20260917.md` @`9da61cab00`,
confirmed by Andrew ~19:0xZ. **They are TRANSCRIBED from that pin verbatim below -- statement, DONE WHEN, ACCEPT
and PROOF -- and only the SOURCE line is dropped.** The endpoint document remains the text that governs.

  FWD-1  A staff member who does not know which system holds a fact asks Claude and is
         pointed to the right tool, with the data's freshness and scope, on the first try
         DONE WHEN  EXERCISED -- a set of real questions, asked cold by someone who did not
                    build the index, routes correctly
         ACCEPT     a discover family is loaded in every session and answers from ONE catalog
                    (never a second): which property and dataset holds the fact, its freshness,
                    its firm scope, its caveats, and the next tool to call; a question about a
                    property that is not catalogued says so and names nothing
         PROOF      a named question set run in a live session by a non-author, with the count
                    routed correctly over the count asked, and every wrong route listed

  FWD-2  For any figure the portal displays, Claude returns the portal's own number with the
         same as-of date
         DONE WHEN  EXERCISED -- a side-by-side read on live data, per surface
         ACCEPT     the tools read the SAME precomputed tables the portal points at; for each
                    surface in scope (model AUM and account distribution, ETF positioning,
                    market and macro, advisor intelligence) the figure and the as-of date match
                    the portal exactly; a disagreement is this project's defect, never a caveat
         PROOF      one comparison per surface, each naming the portal page, the tool call and
                    both values; zero disagreements, denominators printed

  FWD-3  A staff member asks about positions, balances and transactions at either Schwab
         master and gets an answer from silver, without opening the custodian's site
         DONE WHEN  EXERCISED -- a granted person asks and reads the answer
         ACCEPT     one master and one date per answer, never summed across masters; the
                    answer states its date and completeness; transactions are reachable, not
                    only the three `dim_*` tables
         PROOF      a live session transcript for each question class, with the row counts
                    reproduced from the same silver objects by a second instrument

  FWD-4  The same question classes work for Black Diamond, Orion, Eclipse and SmartX
         DONE WHEN  EXERCISED -- per property, on that property's real silver tables
         ACCEPT     each property was ANALYSED first (its common questions written down) and
                    its purpose-built tools cut from that analysis; each answer states date,
                    scope and completeness; a property with no analysis ships no tool
         PROOF      per property: the analysis record, the tool list it produced, and a live
                    answer per tool class with its denominators

  FWD-5  A staff member asks about the ETFs -- holdings, net assets, daily NAV -- per fund
         DONE WHEN  EXERCISED -- per fund, against the served tables
         ACCEPT     the same ladder as FWD-4, per fund (TrueShares, Pathfinder); NAV and net
                    assets carry their date; a fund with no data for a date says so
         PROOF      one live answer per fund per question class, compared with the served
                    artifact

  FWD-6  A question that fits no purpose-built tool still gets a safe answer, and the index
         never sends Claude to that path for a common question
         DONE WHEN  EXERCISED -- both halves: the fallback answers, and the routing prefers
                    the purpose-built tool
         ACCEPT     a TYPED query (filters, group-bys, aggregates as a structured object,
                    never raw SQL) over any catalogued dataset, with hard caps and a response
                    stating date, completeness and whether it was cut short; for the routing
                    half, a named set of common questions reaches its purpose-built tool
                    without being told to
         PROOF      the typed-query transcript including a refused unsafe shape and a
                    cut-short response; the routing count over the same question set as FWD-1

  FWD-7  A staff member asks for one client or household and sees them across custodian and
         platform
         DONE WHEN  EXERCISED -- one real client answered across at least two systems
         ACCEPT     the match is made by a stated rule, and every unmatched record is REPORTED
                    rather than dropped; an answer never merges two people; the rule's
                    precision and recall are printed on a named sample
         PROOF      one client's cross-system answer with the match rule, the sample's
                    precision and recall, and the unmatched list

  FWD-8  A staff member asks for long history or live market data and gets it on demand
         DONE WHEN  EXERCISED -- one long-history answer and one market-data answer
         ACCEPT     the long-history path returns a bounded answer over a span the Gateway's
                    in-process engine cannot hold, and says which substrate served it; the
                    vendor reads (YCharts; Bloomberg where its own standing word allows)
                    appear in the SAME index rather than as a separate world; no new vendor
                    egress beyond Andrew's standing per-use word
         PROOF      one answer per half with its substrate named and its cost/time recorded

  FWD-9  Andrew admits staff to the beta one person at a time, and each person sees only the
         tools and data he granted
         DONE WHEN  EXERCISED -- one admission and one removal, both observed
         ACCEPT     a person not admitted sees NO data tools; an admitted person sees exactly
                    their granted set, and a phrasing that asks for another firm's or master's
                    data is refused; removal takes effect without a redeploy
         PROOF      two sessions (admitted, not admitted) with the tool lists each sees, one
                    refusal transcript, and the roster change with its timestamp

 FWD-10  Adding the next property or tool is one catalog entry plus a tool, and the index
         describes it with nobody writing the description twice
         DONE WHEN  EXERCISED -- the NEXT property after the first three is added this way and
                    the addition is timed
         ACCEPT     the catalog entry (business meaning, example questions, grain, freshness
                    field, firm-scope rule, never-sum rules, producer, tools) is what Claude
                    reads; a tool with no catalog entry or no safety classification DOES NOT
                    SHIP -- proven by a planted unclassified tool being refused; the catalog is
                    versioned in S3 at a builder-named address and has ONE writer
         PROOF      the added property's diff (catalog entry + tool, nothing else), the refusal
                    of the planted unclassified tool, and the elapsed time

## CONTRACTS

**C1 -- ONE catalog, versioned, EXACTLY ONE writer -- and naming that writer is S1's FIRST ACT, because today nothing
does.** The catalog extends `app/refs/DATA_CATALOG.yaml` (v0.3, 36 served-data rows). A second catalog is forbidden,
which is the D6 PRD's standing bar (`D6_OPAL_ANALYST_GRAPHQL_PRD.md:57,102`). Its versioned home is an S3 address
produced by `lib/opal_naming.py address()` and never typed (Rule 30). Each entry carries: business meaning, example
questions, grain, freshness field, firm-scope rule, never-sum rules, producer, and the tools that serve it.

**v0.1 named `emit_catalog_v02.py` as that single writer and it is NOT one.** Found by `2.0.0_SA_COO~G` at L4-R
(refusal @`acb5fc61cc`) and CONFIRMED at the bytes by this seat: `DATA_CATALOG.yaml:3` says `BUILT BY:
workflows/atom_decomposition/emit_catalog_v02.py at git HEAD a4f1686a28`, and that script's own docstring says
`THE LIVE refs/DATA_CATALOG.yaml IS NEVER TOUCHED BY THIS SCRIPT` (`:5`) -- it writes a STAGED artifact that becomes the
live catalog only at a certified port, at which point the staged copy is deleted. `DESIGN.md:67` repeats the header's
version and calls that script "the ONLY writer". So **two carriers of one claim disagree, a third repeats the wrong one,
and the live file's actual writer is UNNAMED** -- the catalog's last commit is `96dcb4a66a` (2026-08-20,
`0.5.0_AE_OpalETL~Z`), which is a PORT ACT, not a standing writer.

The contract is therefore stated as an obligation, never as a fact: **S1's first cell IDENTIFIES the live writer and
either names it in the catalog's own header or mints one, and no catalog entry is added by this project until that
answer exists.** The bar is a census, not a reading: every candidate writer enumerated with its denominator, each one's
own bytes checked for a disclaimer of the live file (the discriminator that caught this), and the surviving writer
exercised once -- a change it makes must appear in the served file. A header's claim about its own builder is the
author's claim, not a measurement, and this PRD will not inherit a second one.

**C2 -- a tool ships only with a catalog entry and a safety classification.** A tool with neither does not ship, and the
mechanism is a refusal, not a review note. The live defect this closes is named in the brief: `read_teams_attachment` is
enabled today and denied to every tier because it has no classification. **The classification is not a word in a review:
every new tool is entered in `destructive_ops` and `data_entitlement` (brief V.4), and the PINNED TOOL-COUNT TESTS MOVE
WITH EACH TOOL** -- a pinned count that is not moved is how a tool ships unregistered while every test stays green, so
the count's movement is part of the tool's own cell and A11 grades both registries by name, not the presence of a label.

**C3 -- tool naming (the rule is the CRO seat's READING of Andrew's answer, and is labelled as such).** Andrew's word
was "Refer to LGIC naming"; the brief resolved it against the canon and says so (VII.3), and the canon does NOT grade
tool names today. So this rule is a reading that binds by criterion here, never a canon quotation:
`{system}_{function}[_{qualifier}]`, `system` a key of `infra/logic/registry/systems.json`,
`function` a base-form verb, **scope (firm or master) always an explicit argument validated against `scopes.json`, never
folded into the name**; the cross-property discover tools sit under the reserved `opal` system. **The schema-grading call:
`NAMING_SCHEMA.json` v1.10 does not grade MCP tool names (`not_covered` is silent on tools). This PRD RULES that the rule
above binds this project's tools by criterion, and that GRADING it in the schema is a LGIC_NAMING schema bump this seat
raises there -- never a rider on LGIC_ENFORCE, and never a second naming authority here.**

**C4 -- the answer envelope.** Every answer states its master or firm scope, its as-of date, whether it is complete or was
cut short, and its source dataset. "No data for that date" is never rendered as zero. Masters and firms are never summed
across, in any phrasing.

**C5 -- portal parity.** A portal-backed tool reads the same precomputed table the portal reads. A disagreement between
Claude and the portal on the same figure and date is a DEFECT of this project, not a caveat, and its acceptance is a
side-by-side read per surface. **The surfaces are enumerable and their families are the denominator: `platinum/mdpf`,
`platinum/etfs`, `platinum/advi` and `json/*` (brief IV.5).** ONE of them does not live where the others do: **served
advisor intelligence for Inflection and Cottonwood sits in FIRM buckets, not the portal bucket (brief IV.6), so a
parity read there crosses a different grant than C7's silver fence** -- that grant is named and scoped in its own cell
before any advisor-intelligence tool is cut, and it is never obtained by widening a silver role.

**C6 -- the typed query.** Filters, group-bys and aggregates as a structured object; never raw SQL from a caller; hard
caps on scanned bytes, rows and time; the response states date, completeness and truncation. Its additivity and grouping
rules are enforced ON THE CALL PATH, with a mutant control -- the standing bar this seat set on NFRA_OPLGTW (R-OG-13,
R-OG-15) after two criteria there passed against a module nothing called, and two tests asserted the defect.

**C7 -- isolation.** One read role per property, fenced to exact silver prefixes, generated from the registry under
LGIC_ENFORCE's builders. **Silver holds every firm in ONE bucket split only by key prefix (brief IV.6), so the fence IS
the isolation and there is no bucket boundary behind it;** a firm-bucket read (C5's advisor intelligence) is a separate
role with its own prefixes and is never folded into a silver role. A staff member granted one master or firm cannot be shown another by any phrasing; the grant
model extends NFRA_OPLGTW's rather than forking it.

**C8 -- the beta roster.** Admission is one person at a time, Opal staff only, controlled by Andrew. Until the mcportal
Entitlements screen exists, the operator command is the path. Removal takes effect without a redeploy.

## SURFACE MANIFEST

| id | surface | what it is | depends on | outcomes |
|---|---|---|---|---|
| S1 | the catalog | the extended schema, its S3 versioned home, its generation into the Gateway | `DATA_CATALOG.yaml`, `address()` | FWD-1, FWD-10 |
| S2 | discover tools | the small always-loaded family that answers "what do we have, how fresh, which tool next" | S1 | FWD-1 |
| S3 | portal tools | per-surface readers over the portal's precomputed tables | S1, the publishers | FWD-2 |
| S4 | custodian and platform tools | per-property purpose-built tools over silver (Schwab, Black Diamond, Orion, Eclipse, SmartX). **NFRA_OPLGTW's engine exposes three `dim_*` tables only; the `fact_*` tables are NOT exposed (brief IV.3), and FWD-3 promises TRANSACTIONS -- so exposing `fact_trn` is this project's own cell, not an inherited capability** | S1, S6, S7 | FWD-3, FWD-4 |
| S5 | ETF tools | per-fund holdings, net assets, NAV | S1, S7 | FWD-5 |
| S6 | the typed query engine | generalised beyond Schwab, capped, enforced on the call path | NFRA_OPLGTW's engine | FWD-6 |
| S7 | read roles and grants | one fenced role per property; the grant model extended | LGIC_ENFORCE's registry and builders | FWD-3..FWD-5, FWD-9 |
| S8 | the per-property analysis | the written record of what people actually ask, per property. **Its standing input is PART III's beta bar: each admitted person's first week produces the list of questions the index could not route, and that list is the next round's analysis input** -- which is also how VII.2 (the common questions are not enumerated anywhere yet) closes by measurement rather than by guesswork | -- | FWD-4, FWD-5, FWD-10 |
| S9 | entity resolution | the stated matching rule, its precision and recall, its unmatched list | S4 | FWD-7 |
| S10 | on-demand paths | the long-history substrate and the vendor reads in the same index. **SCOPE LIMIT, from brief VII.4: Bloomberg on-demand is the SITEZ standing read and is NOT claimed reachable from the laptop fabric. This is a LAPTOP project, work is never routed across fabrics, so FWD-8's market-data half is served by the Gateway's YCharts tools on Andrew's per-use word -- Bloomberg is out of scope here and a cross-fabric reach is a re-cut, not a cell** | S1, S6 | FWD-8 |
| S11 | the beta roster | admission, removal, per-person tool lists | S7, the Gateway's identity | FWD-9 |

## Ground truth measured at authorship (2026-09-17, repository only)

- 49 tools registered, 44 enabled; none answers a question about Opal's own data (35 Microsoft 365, 6 YCharts, 1 portal
  upload, 2 estate graph).
- The portal catalog and its gate exist and are unreachable as tools; five business tools were designed and parked.
- The live-query pattern exists for Schwab: five tools, a typed grammar, DuckDB in a capped child process, per-person
  grants, a response envelope -- built, tested, NOT enabled in deployment, and exposing three `dim_*` tables only.
- Silver holds all firms in one bucket, split by key prefix; no Glue or Athena sits over silver or gold.
- Entity resolution is parked; `read_teams_attachment` is the live unclassified-tool defect.

**Not measured, and named as such:** AWS state, table sizes, object counts, query timings, and the per-property common
questions.

## BRIEF COVERAGE

Denominator: **20 headings** in `docs/briefs/opal-mcp-tool-index-brief-20260917.md` @826ac6925a, counted as every line
matching `^#` at that pin (1 H1 + 9 H2 + 10 H3), re-measured here rather than recalled. Each heading is CARRIED (a
contract, surface or acceptance line holds it), CARRIED-AS-OPEN (held as a named precondition or non-claim, not as a
settled value), or NOT CARRIED with the reason on its own line.

| # | brief heading | disposition | where |
|---|---|---|---|
| 1 | H1 title -- every data property answerable in Claude, indexed from ONE catalog | CARRIED | C1; this PRD's title |
| 2 | ANDREW'S WORDS, VERBATIM | CARRIED | Authority and project arc restates his five card answers; the verbatim text stays in the brief and is never re-typed here. His problem statement (the official plugins are poorly indexed and we will not have that problem) is why C1 and S2 exist at all |
| 3 | PART I -- THE OUTCOME TERRITORY | CARRIED | ENDPOINT; O1-O10 map one-to-one onto FWD-1..FWD-10, none added, none dropped |
| 4 | O1 what data do we have on X, and how fresh | CARRIED | S2; A1 |
| 5 | O2 anything the portal shows, the portal's own number | CARRIED | C5; A2 |
| 6 | O3 positions, balances and transactions at either Schwab master | CARRIED | S4; A3 -- and S4 now names that `fact_*` is NOT exposed today, so transactions are a cell here |
| 7 | O4 the same question classes for the four platforms | CARRIED | S4, S8; A4 |
| 8 | O5 the ETFs, per fund | CARRIED | S5; A5 |
| 9 | O6 a question that fits no tool still gets a safe answer | CARRIED | C6; A6 |
| 10 | O7 one client or household across custodian and platform | CARRIED-AS-OPEN | S9; A7 -- entity resolution is PARKED (IV.8) and V.6 is its precondition, so this outcome's substrate does not exist yet and the PRD says so rather than scheduling it |
| 11 | O8 long history and live market data on demand | CARRIED-AS-OPEN | S10; A8 -- no Glue or Athena sits over silver or gold (IV.7), so the long-history half has NO substrate today, and the market-data half is scoped to YCharts on this fabric (VII.4) |
| 12 | O9 admission one person at a time | CARRIED | C8, S11; A9 |
| 13 | O10 the next property is a catalog entry plus a tool | CARRIED | C1, C2; A10 |
| 14 | PART II -- WHERE THE BOUNDARY SITS | CARRIED | Scope: owns / relies-on / explicitly-out, including that enabling NFRA_OPLGTW's Schwab tools is that project's act and never this one's |
| 15 | PART III -- THE QUALITATIVE BAR (7 bullets) | CARRIED, 7 of 7 | discover S2/A1; portal parity C5; silver-without-a-vendor-site S4; index quality C6/A6 (routing prefers the purpose-built tool); honesty C4; isolation C7; **beta -- the first week's unrouted questions feed the next analysis, now carried in S8** |
| 16 | PART IV -- THE SUBSTRATE (9 findings) | CARRIED, 9 of 9 | IV.1 Ground truth (44 enabled, none answers an Opal-data question); IV.2 C1 and Ground truth (the parked business tools and `catalog_gate.py`, which S1 REUSES rather than rebuilds); IV.3 S4/S6 (the `fact_*` gap); IV.4 C3; IV.5 C5's enumerated table families; IV.6 C5 and C7 (advisor intelligence in FIRM buckets is a different grant); IV.7 S10; IV.8 S9; IV.9 C2 |
| 17 | PART V -- WHAT MUST BE TRUE (9 items) | CARRIED, item by item | the **BRIEF PRECONDITIONS** map below |
| 18 | PART VI -- STATUS (declared NOT outcome-bearing by the brief) | NOT CARRIED, by the brief's own instruction | a repo-only status snapshot carries no contract; the figures inside it that DO bear on design are in IV.1-IV.9 and are carried there, and the D9 member list is the register's, not this PRD's |
| 19 | PART VII -- WHAT THIS BRIEF DOES NOT CLAIM (6) | CARRIED-AS-OPEN, 6 of 6 | the **BRIEF NON-CLAIMS CARRIED** map below |
| 20 | REFS | CARRIED | the `brief_ref` pin in the header; the scoping record and prior art are L5's reading list under VII.6's qualifier |

**BRIEF PRECONDITIONS (PART V, 9 of 9).** None is assumed true.

| V | precondition | held by | this PRD |
|---|---|---|---|
| V.1 | catalog schema extended to silver datasets, ONE writer, versioned S3 home from the naming builder | this project (S1) | C1 -- which now says the live writer is UNIDENTIFIED and that naming it is S1's first act |
| V.2 | a per-property analysis pass before that property's tools are cut | this project (S8) | S8; A4 makes the analysis record part of the acceptance, so a tool cut without one cannot grade |
| V.3 | one read role per property fenced to exact prefixes; the grant model extended beyond Schwab's two masters and three datasets | this project (S7) | C7; the extension is explicit and EXTENDS NFRA_OPLGTW's model rather than forking it |
| V.4 | every new tool classified in `destructive_ops` and `data_entitlement`; **the pinned tool-count tests move with each tool** | this project (C2) | C2 names both registries and the pinned-count movement; A11 grades them by name |
| V.5 | NFRA_OPLGTW's Schwab tools ENABLED in deployment before O3 can be exercised | **NFRA_OPLGTW** (`2.0.0_SA_COO~O`), not this project | Canonical handoff and the project row's `blocking`; it gates FWD-3's EXERCISE, never this PRD's halves, and this project never enables them itself |
| V.6 | a way to match one person across systems before O7 | this project (S9), on a parked prerequisite | S9 -- entity resolution is parked (IV.8) and its D6-addendum gate on D3's residual enum is named; FWD-7 is the outcome that waits on it |
| V.7 | a query substrate over long history before O8's first half | this project (S10) | S10 -- no Glue or Athena exists today (IV.7); the substrate choice is an L5 cell with its own measurement, never a value set here |
| V.8 | each new integration goes through the standing enablement checklist | this project, per integration | **`docs/architecture/NFRA_INTEGRATIONS_STANDARD.md` s.6 and s.8.1**, named here so the obligation points at a document rather than at itself; every property's enablement cell cites it |
| V.9 | a beta roster Andrew controls, one person at a time | this project (S11) | C8; the operator command is the path until the mcportal Entitlements screen exists, and that screen is the mcportal brief's, not this project's |

**BRIEF NON-CLAIMS CARRIED (PART VII, 6 of 6).** Each is inherited as an open item; a cell closes it by MEASURING it.

| VII | the brief does not claim | this PRD's disposition |
|---|---|---|
| VII.1 | no AWS state was read; table sizes, object counts and query timings over silver are unmeasured | OPEN and stated in the evidence boundary: **every capacity claim here is DESIRED until a cell exercises it**, and each property's first analysis cell carries the measurement |
| VII.2 | the per-property common questions are not enumerated anywhere | OPEN, and it CLOSES BY MEASUREMENT: S8's analysis pass plus PART III's beta bar -- the first week's unrouted questions are the next round's input, so the enumeration is produced by use rather than guessed |
| VII.3 | the tool-naming rule is the CRO seat's READING of Andrew's answer; the canon does not grade tool names | CARRIED EXPLICITLY -- C3 now says so in its own first line, binds the rule by criterion, and routes the GRADING question to LGIC_NAMING as a schema bump |
| VII.4 | **Bloomberg on-demand is the SITEZ standing read; NOT claimed reachable from the laptop fabric** | CARRIED AS A SCOPE LIMIT in S10 and A8. This is a LAPTOP project and work is never routed across fabrics, so FWD-8's market-data half is exercised through YCharts on Andrew's per-use word and Bloomberg is OUT of scope. Reaching for it later is a re-cut of FWD-8, never a cell |
| VII.5 | citations are the research passes' reads at the stated vintage, not re-verified line by line | OPEN and it BINDS L5: the first cell of each surface re-verifies the citations it relies on by PRINTING THE BYTES at the cited line, never by grepping for the quote -- a citation ages separately from the text it quotes, and this PRD's own v0.1 defect was exactly a claim inherited from a header nobody re-read |
| VII.6 | the earlier scoping record recommended D6 and business-first names; both were OVERRULED by Andrew, and the record is kept unedited as research | CARRIED: the record is on L5's reading list AS RESEARCH, never as direction. Its D6 placement and its business-first naming are superseded by his 2026-09-17 words (D9 Opal Workflows; Refer to LGIC naming), and a cell that cites it cites the overrule beside it |

## Acceptance matrix

| id | acceptance | outcome |
|---|---|---|
| A1 | a named cold question set, asked by a non-author, routes correctly; the count routed over the count asked is printed, every wrong route listed | FWD-1 |
| A2 | per portal surface, one side-by-side read: figure and as-of date identical, zero disagreements, denominators printed -- the DENOMINATOR being the enumerated table families `platinum/mdpf`, `platinum/etfs`, `platinum/advi`, `json/*` (brief IV.5), so "per surface" has a countable population rather than a reviewer's list | FWD-2 |
| A3 | per Schwab question class, a live transcript with row counts reproduced by a second instrument | FWD-3 |
| A4 | per property: the analysis record, the tool list it produced, one live answer per tool class | FWD-4 |
| A5 | per fund: one live answer per question class compared with the served artifact | FWD-5 |
| A6 | the typed query refuses an unsafe shape, states truncation, and the routing set prefers purpose-built tools | FWD-6 |
| A7 | one client answered across two systems, with the match rule, its precision and recall on a named sample, and the unmatched list | FWD-7 |
| A8 | one long-history answer and one market-data answer, each naming its substrate and its cost; the market-data half is exercised through the Gateway's YCharts path on this fabric, with Bloomberg NAMED as the SITEZ read this project does not claim (brief VII.4) | FWD-8 |
| A9 | two sessions (admitted, not admitted) with their tool lists, one refusal transcript, one removal with its timestamp | FWD-9 |
| A10 | the next property added as one catalog entry plus a tool, timed; a planted unclassified tool is REFUSED | FWD-10 |
| A11 | every tool that ships carries its catalog entry and classification; the count of tools without either is zero, denominator printed | C2 |
| A12 | every tool name is generated or validated against the C3 rule; a hand-typed non-conforming name is refused | C3 |

## Canonical handoff

L5 (the decomposition) is `2.0.0_SA_COO`'s, on a lane `0.0.0_AB_MSTR` seats when one frees. **Andrew's seat order of
2026-09-17 puts this project SECOND, after IRPT_BCKEND and before MDPF_TAXSMA.** The first cells are the catalog schema
(S1) and the per-property analysis for the first property (S8), because every other cell reads from them. FWD-3's live
exercise waits on NFRA_OPLGTW enabling its Schwab tools -- that project's act, and this project's cells prove their own
half meanwhile.

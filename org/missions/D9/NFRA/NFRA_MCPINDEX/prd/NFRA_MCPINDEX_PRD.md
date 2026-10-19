```json
{
  "project": "NFRA_MCPINDEX",
  "directive": "D9",
  "fabric": "site-z",
  "prd_version": "v0.17",
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
    "FWD-10",
    "FWD-11",
    "FWD-12",
    "FWD-13",
    "FWD-14",
    "FWD-15",
    "FWD-16",
    "FWD-17",
    "FWD-18",
    "FWD-19",
    "FWD-20",
    "FWD-21",
    "FWD-22"
  ],
  "status": "DRAFT"
}
```

# NFRA_MCPINDEX - the Opal MCP tool index: every Opal data property answerable in Claude, from one catalog

## Authority and project arc

Author and accountable CTO: `1.0.0_SA_CTO`. Directive D9, Opal Workflows; macro NFRA; execution fabric site-z (v0.6; it read "laptop" through v0.5).

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

**v0.6 (2026-09-30 ~08:0xZ, `1.0.0_SA_CTO~O`)** is the B8 addendum of the reinstatement rulings
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/REINSTATE_RULINGS_20260930.md` @4e598ab7be, on Andrew's
2026-09-30 order to reinstate the project. The project runs on the site-z fabric (header `fabric`), where the Bloomberg
standing read lives, so the brief VII.4 scope limit ("Bloomberg ... NOT claimed reachable from the laptop fabric") no
longer holds. S10, A8 and the VII.4 coverage row now make FWD-8's market-data half reachable through Bloomberg under its
own standing read (`integrations/bloomberg/READ_HERE.md`) as well as through YCharts. ENDPOINT and CONTRACTS are
unchanged: FWD-8 already reads "Bloomberg where its own standing word allows" and "no new vendor egress beyond Andrew's
standing per-use word", and this addendum adds no vendor egress.

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
                    its firm scope, its caveats, and the next tool to call; a need with no tool
                    is a GAP entry naming its owner or "unowned" (v0.7); a question about a
                    property absent from every entry says so and names nothing
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
                    appear in the SAME index rather than as a separate world; egress is open
                    on every channel except Bloomberg, which reads through its queue (v0.7:
                    CLAUDE.md law edit @4d77a9c3ea)
         PROOF      one answer per half with its substrate named and its cost/time recorded

  FWD-9  Andrew admits staff to the beta one person at a time, and each person sees only the
         tools and data he granted
         DONE WHEN  EXERCISED -- one admission and one removal, both observed
         ACCEPT     a person not admitted sees NO data tools; an admitted person sees exactly
                    their granted set; once a second user beyond Andrew and Alyssa is
                    admitted, a phrasing that asks for another firm's or master's data outside
                    that person's grant is refused (v0.7: until then per-user scoping waits,
                    Andrew-direct @0035550443); removal takes effect without a redeploy
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

FWD-11  Alyssa asks for a model's performance and is routed to the served answer, not to Chrome (v0.7, the thread)
         DONE WHEN  EXERCISED -- Alyssa, in her own words, asks how a model did against its
                    benchmark for a period; discover names the tool, states the data's true as-of
                    date, and the answer matches opalinvest.dev
         ACCEPT     one need end to end: the question, the route, the true date, the answer
         PROOF      her session transcript beside the served artifact's date and the portal page
         SOURCE     Andrew-direct 2026-10-09 ~03:2xZ (record @5716c7a83d); brief
                    docs/briefs/mcpindex-alyssa-workflows-midstream-brief-20261009.md @3455b1783a, O1

FWD-12  Every need in Alyssa's two briefs has an index entry, served or not (v0.7)
         DONE WHEN  EXERCISED -- a reviewer subtracts the catalog from her two briefs and finds
                    nothing missing
         ACCEPT     each entry says what the need is, its source, whether it is served today and
                    which tool answers it; an unserved need is a GAP entry naming the project that
                    owns it, or "unowned"; "not catalogued" never stands for "not known"
         PROOF      the subtraction, denominator printed (brief Part IV.A: 29 candidates)
         SOURCE     as FWD-11; brief O2

FWD-13  The index states a dataset's true freshness (v0.7)
         DONE WHEN  EXERCISED -- for three datasets, the stated as-of equals the served artifact's
         ACCEPT     freshness is read from the served artifact at answer time, never the value held
                    from certification
         PROOF      the three comparisons, including model benchmarks (held 2026-08-10 vs served
                    2026-10-07, measured 2026-10-09)
         SOURCE     as FWD-11; brief O3, Part VI.2

FWD-14  Alyssa's own words route correctly (v0.7)
         DONE WHEN  EXERCISED -- her phrasings ("account counts by partner", "cost basis",
                    "statement", "stress test", "download the attachment", "S&P YTD") each reach
                    their tool or GAP entry on the first try
         ACCEPT     no phrasing lands on a dataset whose meaning is a different need
         PROOF      the six discover calls and their routes
         SOURCE     as FWD-11; brief O4

FWD-15  Vendor data is in the same index (v0.7)
         DONE WHEN  EXERCISED -- a market-return question routes to the YCharts tools (Bloomberg
                    through its queue)
         ACCEPT     vendor tools carry catalog entries like Opal's own data; a vendor tool that
                    fails live reads PARTIAL with its error, never SERVED
         PROOF      one routed YCharts answer, or its PARTIAL entry with the live error
         SOURCE     as FWD-11; brief O5; CLAUDE.md law edit @4d77a9c3ea (egress open except Bloomberg)

FWD-16  NFRA_OPLGTW's new datasets appear in the index as they land (v0.7)
         DONE WHEN  EXERCISED -- the first NFRA_OPLGTW v2.x dataset served (lots, realized gains,
                    account identity, the Tax SMA master or Black Diamond) has its entry the same day
         ACCEPT     FWD-10's rule: one catalog entry plus a tool
         PROOF      the dataset's serve date beside its entry's commit
         SOURCE     as FWD-11; brief O6

FWD-17  File intake and write actions are indexed with their class (v0.7)
         DONE WHEN  EXERCISED -- discover answers "save an attachment", "move mail" and "send a
                    Teams message" with the entry, its read or write class, and whether the
                    caller's grant allows it
         ACCEPT     a write tool is never implied to be available when the grant refuses it
         PROOF      the three discover answers under Alyssa's principal
         SOURCE     as FWD-11; brief O7

FWD-18  Each entry names the browser workflow it retires (v0.7)
         DONE WHEN  EXERCISED -- the count of her Chrome workflows (C1-C8) and Schwab workflows
                    (W1-W6) that a served entry now answers is read from the catalog
         ACCEPT     an entry carries its C# or W#
         PROOF      the count, denominator 14
         SOURCE     as FWD-11; brief O8

FWD-19  The operations lead's trade reconciliation and billing are answerable in Claude from one server (v0.8)
         DONE WHEN  EXERCISED -- discover routes "trade rec" and "billing" to their readers, and
                    each reader answers from its named served source under an admitted principal
         ACCEPT     each reader's rows carry the OW-k-1 fixture fields (trade rec: account,
                    custodian, trade_date, symbol, side, quantity, opal_status, custodian_status,
                    matched; billing: account, household, billing_period, aum, fee_rate_bps,
                    fee_amount, status) inside the C4 envelope; a fixture is never served as data;
                    a reader with no served source is a GAP entry naming its owner; read only
         PROOF      per reader: the discover call, one live answer with as-of and row count, and
                    the same count read from the source by a second instrument
         SOURCE     Andrew-direct 2026-10-09 ~05:0xZ (record @709da7cded, line 9); option A
                    record @1740ba55ec; fixtures tools/ops_kit/fixtures/ @cc539738c6

FWD-20  Every tool the gateway serves names its catalog index, that index's history depth and its freshness (v0.9)
         DONE WHEN  EXERCISED -- a census over the DEPLOYED gateway's served tools reads N tools
                    served, partitioned into three counted members that sum to N: (a) names its
                    catalog index; (b) reads data but has no index yet, naming its owner or
                    "unowned"; (c) is not a data read (e.g. send_email, whoami). Each (a) tool carries
                    its index's history depth (earliest served date) and freshness (latest served date)
         ACCEPT     the tool list is read from the deployed gateway's definitions, never a hand-kept
                    list; freshness AND depth are read at answer time from the served artifact
                    (FWD-13's rule): depth is a first-date field or the dated series' first element,
                    a snapshot's depth is its one as-of; each carries a claim (measured / inferred /
                    absent), and "absent" is said only where no served artifact carries any date;
                    the values are readable by NFRA_MCPORTAL through the existing catalog read
         PROOF      the census with N and the three member counts printed; for one (a) tool, the depth
                    and freshness compared with the served artifact by a second instrument
         SOURCE     Andrew's site Z voice memo 2026-10-13 ("We need to be able to see all indexes for
                    all vendor slash channels ... the depth and breadth of channels and indexes and
                    tools available per vendor"), via direction XB-20261013T185926Z-4d72 Z4

FWD-21  An asset manager's research question routes to the servable harvest data (v0.9)
         DONE WHEN  EXERCISED -- opal_discover for "harvested news articles and chatter" and for
                    "security analysis research pack" each return catalogued datasets, not
                    catalogued: false; the Schwab positive control still returns its datasets
         ACCEPT     one catalog row per prefix in the servable-prefix list v4 @7e0da2dfee (all 24
                    prefixes SERVE to Opal principals, Andrew call 8), named exactly as listed
                    (row 8's gold tables by table prefix, never amgt/harvest/gold/ whole); the existing
                    catalog read tools are used first (build ladder step 2), and a prefix no
                    existing tool can read is a GAP entry naming its owner
         PROOF      the three discover calls; the catalog's harvest rows counted against the
                    list v4's 24 prefixes (denominator printed)
         SOURCE     Andrew's AMGT voice memo 2026-10-13 ("set up the MCP index for that bucket ...
                    so that the asset managers can use that with their cloud"), via XB-4d72 Z4/Z5

FWD-22  The one catalog is the table of contents at TABLE grain, for every census group (v0.11)
         DONE WHEN  EXERCISED -- for one table per landed census group, opal_discover in plain words
                    returns that table's catalog row (contract: columns, grain, partition, freshness
                    basis, fork keys; nl_tags; read_tool naming a DEPLOYED tool), and opal_describe
                    returns its columns; a retired dataset is never offered as a tool target
         ACCEPT     the contracts live IN DATA_CATALOG.yaml table rows (one carrier; describe reads the
                    catalog, no second registry); a source-level row is split into its table rows;
                    tool_index lists every deployed tool, harvest_list and harvest_read included; every
                    value carries its claim (measured / inferred / absent); the version bump carries
                    Andrew's verbatim (the catalog's widening law)
         PROOF      the plain-words calls, one per landed group; the negative arm (a retired dataset);
                    per group, catalog table rows counted against the census's contracts, the
                    difference printed
         SOURCE     Andrew-direct 2026-10-14 ~12:4xZ ("Data contract should be available. Tables should
                    be available. All of this should have tags and natural language tags associated";
                    the one catalog as "a table of contents for Opal Data assets"), verbatim in
                    org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_124xZ_GATEWAY_DATA_CONTRACTS_CENSUS_CRO_FANOUT.md

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
| S10 | on-demand paths | the long-history substrate and the vendor reads in the same index. **v0.6: the scope limit from brief VII.4 is lifted.** This is a site-z project, where the Bloomberg standing read lives, so FWD-8's market-data half may be served by Bloomberg under its own standing read (`integrations/bloomberg/READ_HERE.md`) or by the Gateway's YCharts tools on Andrew's per-use word. No new vendor egress; a Bloomberg reach outside its standing read is not in scope | S1, S6 | FWD-8 |
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
| VII.4 | **Bloomberg on-demand is the SITEZ standing read; NOT claimed reachable from the laptop fabric** | CARRIED, then LIFTED at v0.6. The project runs on the site-z fabric, so the limit no longer binds: S10 and A8 admit Bloomberg under its own standing read beside YCharts, with no new vendor egress (reinstatement ruling B8) |
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
| A8 | one long-history answer and one market-data answer, each naming its substrate and its cost; the market-data half is exercised through Bloomberg (its standing read on this fabric) or the Gateway's YCharts path, and names which (v0.6, ruling B8) | FWD-8 |
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

### v0.7 addendum (2026-10-09 ~04:0xZ, 1.0.0_SA_CTO~O) -- index every need in Alyssa's workflows

**Input.** Andrew-direct 2026-10-09 ~03:2xZ
(`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261009_032xZ_MCPINDEX_INDEX_ALYSSA_WORKFLOWS.md` @5716c7a83d):
"all of this should be indexed, there is a lot of indexing work to be done". Brief:
`docs/briefs/mcpindex-alyssa-workflows-midstream-brief-20261009.md` @3455b1783a (`4.0.0_SA_CRO~Z`, midstream). Endpoint:
FWD-11 to FWD-18 above, with FWD-11 as the thread.

**Contract changes:**

1. **GAP entries (FWD-1 change).** A need with no tool is catalogued as a GAP entry: its owner, or `unowned`, and no tool.
   FWD-1's "not catalogued ... names nothing" now applies only to a property absent from every entry.
2. **FWD-8 superseded.** "no new vendor egress beyond Andrew's standing per-use word" yields to the CLAUDE.md law edit
   @4d77a9c3ea: "Egress is open on every channel, except Bloomberg".
3. **FWD-9 superseded for the connected users.** "a phrasing that asks for another firm's or master's data is refused"
   yields to Andrew-direct ~01:5xZ (@0035550443): per-user entitlement scoping waits for a second user. NFRA_OPLGTW v2.2
   carries the grants.
4. **Freshness is read, not held (FWD-13).** An entry's `latest_value` is read from the served artifact at answer time,
   with claim `measured`. A held certification value is never shown as the as-of.
5. **The candidate list is the decomposition's input, not a contract.** Brief Part IV.A has 29 entries. The cut may
   split them finer; it may not drop one without a GAP row.
6. **Unowned gaps are named, not built here.** E-9, E-10, E-11, E-12, E-20, E-26, E-27 and E-28 are catalogued as
   `unowned`. E-12 is account returns, which Andrew's "the right information" bound leaves out. Building any of them is
   another project's word.

**Order.** FWD-11 (the thread) first, then FWD-13 and FWD-14 (they fix what the thread exposes), then FWD-12, FWD-15 and
FWD-17. FWD-16 follows NFRA_OPLGTW's serve dates.

**Sign-off.** ENDPOINT and CONTRACTS change. The ratified-text half re-opens for `3.0.0_SA_CVO~Z`. The brief half is
`4.0.0_SA_CRO~Z`'s, accepted as written by the CRO (rule 27, PROPORTIONATE SIGN-OFF).

### v0.8 addendum (2026-10-09 ~07:3xZ, 1.0.0_SA_CTO~O) -- the operations lead's readers (FWD-19)

**Input.** Andrew-direct 2026-10-09 ~05:0xZ at the `2.0.0_SA_COO~O2` terminal (dell2),
`org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/ANDREW_DIRECT_20261009_05xxZ_TICKET_CENTER_TRADE_INTAKE_AND_FIT_READ.md`
@709da7cded, line 9: "MCPINDEX on the sitez box as far as how claude gets the data in question". Option A (one server
his Claude pulls from): `ANDREW_DIRECT_20261009_05xxZ_OPS_LEAD_LOCALHOST_DASHBOARD.md` @1740ba55ec, same folder. Shape:
OW-k-1's fixtures, `tools/ops_kit/fixtures/trade_rec.json` and `billing.json` @cc539738c6. Asked by `2.0.0_SA_COO~MI`
(msg 32435), the owner ruled by `1.0.0_SA_CTO~Z` (msg 32430).

**Contract changes:**

1. **FWD-19 serves two readers: trade reconciliation and billing.** Their row fields are the fixtures' fields, so the
   ops kit's one adapter (NFRA_OPSWKF, dell2) swaps a fixture for a live read with no field mapping. The fixtures are
   the SHAPE and a test input only. A fixture value is never served as data.
2. **The source is found, never assumed.** Each reader's first cell names its served source by census: every
   candidate producer, with its denominator, and the surviving source read once. This is C1's bar. Candidates to test
   include the trade engine's statuses against custodian silver transactions (trade rec) and the Black Diamond fees
   read behind `blackdiamond_list_fees` (billing). They are candidates only. A reader with no served source ships as a
   GAP entry naming its owner (v0.7 item 1), and FWD-19 is then not done.
3. **The C4 envelope and C7 isolation apply unchanged.** Every answer states its firm or master scope, its as-of and
   its completeness. Nothing is summed across firms or masters.
4. **Read only. No alert, notification or monitor.** The operations lead's other four items are catalogued as GAP
   entries, `unowned`, with no tool: post model update rec, high cash account alert FA, assets transfer alert FA and
   restricted account alert FA. The three FA alerts are under the standing moratorium until Andrew names an alert.
   Trade-request intake and its C-NO-SEND fence are NFRA_OPSWKF's, not this project's.
5. **Admission is Andrew's act (C8).** The operations lead becomes a beta user only on Andrew's admission. Once he is
   admitted, he is the first user beyond Andrew and Alyssa. FWD-9's per-user scoping clause therefore binds from his
   admission, and his grant is written before his first data call. FWD-19 is proven on demand under an already
   admitted principal; his own session is the organic arm, not the proof.

**Order.** Round 9, after round 8 drains, as `2.0.0_SA_COO~MI` proposed. FWD-19 is disjoint from the FWD-11 thread's write
surface: new reader modules and new catalog entries.

**Sign-off.** ENDPOINT and CONTRACTS change. The ratified-text half re-opens for `3.0.0_SA_CVO~Z`. The input is an
Andrew-direct record and no CRO brief, so the brief half is owed by `4.0.0_SA_CRO~Z`, or by a live COO that does not
hold the round (rule 27).

### v0.9 addendum (2026-10-13 ~19:3xZ, 1.0.0_SA_CTO~Z) -- one short round: tool-to-index links, and the harvest bucket (FWD-20, FWD-21)

**Input.**
- Andrew's site Z and AMGT voice memos, 2026-10-13 morning, verbatim in the laptop CTO's direction
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_SITEZ_20261013.md` sections 1.1 and 1.2
  (cross-box ORDER XB-20261013T185926Z-4d72, acked 19:12Z). He names this project one of "the three that matter".
- The laptop CTO's positioning ruling @f469cb665f: ONE short MCPINDEX round; FWD-19 and FWD-11 stay parked.
- The servable-prefix list v3: `org/tier1_exec/1.0.0_SA_CTO/deliverables/SERVABLE_PREFIXES_OPAL_DATA_HARVEST_20261013.md`
  @0b2778751a (`1.0.0_SA_CTO~DELL1` rulings F1-F5). It includes Andrew-direct ~19:0xZ ("any data in our AWS cloud is
  available to our team"), which makes 11 rows SERVE.
- Brief: the CRO's alignment reports for site Z and AMGT, cited in the direction's section 7.

**Contract changes:**

1. **The `opal-data-harvest` bucket is in scope (FWD-21).** Before this, the PRD did not mention the harvest bucket.
   - Data rows are cut for the list's SERVE rows only. WITHHOLD prefixes, and any new top-level prefix not yet classed
     on the list, get no data row.
   - The V1 rule holds: derived layers and article links, never raw publisher text.
2. **The grant is not this project's.** Asset-manager principals and the research `s3:GetObject` grant (with its two
   negative arms) are NFRA_OPLGTW's next-round act (direction Z5). This project writes catalog rows only. C1's single
   writer of `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` is unchanged.
3. **Tool-to-index links come from the deployed gateway (FWD-20).** The served-tool list is read from the gateway's
   deployed definitions (`services.opal-gateway.deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json`), never the trunk
   and never a hand-kept list. NFRA_MCPORTAL shows the result. MC Portal's own FWD-20 and FWD-21 are a DIFFERENT
   project's outcomes with the same numbers.
4. **Both cells write the one catalog file.** The decomposition sequences them or merges them into one cell. Two
   parallel writers of `DATA_CATALOG.yaml` are refused.
5. **No new resource names.** If one is needed, it is `lib/opal_naming.py` output (CLAUDE.md rule 30).

**Order.** One round, cut by `2.0.0_SA_COO~MI` (seated 19:1xZ for this round): FWD-20, then FWD-21, or one cell
covering both. The project parks at ROUND_CLOSE after it. The round-9 un-park conditions (a)-(c) stand for everything
else. `0.7.0_AE_CloudOps~MI` keeps its MX-s-19 read on 2026-10-19/20.

**Sign-off.**
- ENDPOINT and CONTRACTS change, so the ratified-text half re-opens for `3.0.0_SA_CVO~Z`.
- The brief half is the CRO's alignment reports on Andrew's memos, accepted as written (rule 27, PROPORTIONATE
  SIGN-OFF).
- Cure (~19:4xZ) on `3.0.0_SA_CVO~Z`'s refusal at half_hash 0fa643617bfd (msg 33707; review
  `org/tier1_exec/3.0.0_SA_CVO/deliverables/L4R_REVIEW_NFRA_MCPINDEX_v0.9_RATIFIED_TEXT_20261013_Z.md`): FWD-20 is a
  three-member partition summing to N (a: names its index; b: data read with no index yet, owner or unowned; c: not a
  data read). GAP keeps its v0.7 meaning, "a need with no tool". The SOURCE line no longer names a seat.

### v0.10 addendum (2026-10-14 ~00:4xZ, 1.0.0_SA_CTO~Z) -- FWD-21 re-pinned to list v4; FWD-20 depth read from the served artifact

The L10 answer to `3.0.0_SA_CVO~Z`'s round-10 slug (REMEDIATION_v8 @e660242ac7, msg 33840). It carries row Z-S105.

1. **FWD-21 re-pins to list v4 @7e0da2dfee.** Andrew-direct 2026-10-13 ~20:0xZ (call 8, verbatim in that file): every
   prefix SERVES to Opal principals, raw included. v0.9 contract item 1 ("the V1 rule holds: derived layers and article
   links") is superseded for Opal principals. Non-Opal principals are refused on every prefix (NFRA_OPLGTW FWD-21). Round
   10 served v3's rows (FWD-21 REALIZED on v3); round 11 adds the prefixes v4 adds.
2. **FWD-20 depth is read at answer time from the served artifact,** the same rule as freshness (row Z-W33-S1).
   - "absent" on 11 of 11 (a) tools was a wrong claim. MX-c-8's bound 4 forbade reading a body, yet the served AUA
     timeseries carries `as_of_first = 2024-11-01`.
   - A first-date field or the dated series' first element gives a measured depth.
   - A live-queried row's depth is its served window, claimed `inferred` where it is not read.
   - "absent" is kept only where no served artifact carries any date.

ENDPOINT text changes, so the ratified-text half re-opens for `3.0.0_SA_CVO~Z`. The brief half is unchanged in substance
(the CRO's alignment reports on Andrew's memos).

### v0.11 addendum (2026-10-14 ~13:1xZ, 1.0.0_SA_CTO~Z) -- FWD-22: the catalog at table grain from the census contracts; G1 harvest first

**Input.** Andrew-direct 2026-10-14 ~12:4xZ (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_124xZ_GATEWAY_DATA_CONTRACTS_CENSUS_CRO_FANOUT.md`), directive `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_DIRECTIVE_20261014_GATEWAY_DATA_CONTRACTS_CENSUS.md` @06ae2a3485, and G1: `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md` @0d7c29b3c5.
This replaces the harvest tool-set addendum planned on XB-dc98: round 13 cuts from here.

**G1 enrichment list (round 13, `2.0.0_SA_COO~MI`):**
1. **Split to table grain.** 26 of 78 harvest datasets have a row at their own prefix; 50 sit under a source-level row;
   2 have none (`amgt/harvest/gold/ai_fill/`, `social/v1/`). Write one row per dataset, 78 of 78, carrying G1's
   contract fields (G1 sections 1-2 print the denominators).
2. **Fill the fields the rows read `NONE -- not read`:** grain, freshness field and basis, rows, keys, never-sum rules,
   from G1's JSON. A value G1 marks inferred stays inferred.
3. **`read_tool`.** Add `harvest_list` and `harvest_read` to `tool_index`. Point each research row at its G1 typed
   tool as each tool deploys (NFRA_OPLGTW v3.0); until then the row names `harvest_read`. Never name an undeployed tool.
4. **nl_tags and common_queries** from G1 on every row, so opal_discover answers plain words.
5. **Retired as tool targets:** `publication-links/v1/`, `publications/v1/` (rows stay, marked retired); the hyphen
   `research-dossier/` only once the round reads that `research_dossier` supersedes it.
6. **Version bump** to the next catalog version, carrying Andrew's verbatim from the record above.

**Sign-off.** ENDPOINT changes (FWD-22 added), so the ratified-text half re-opens for `3.0.0_SA_CVO~Z`. The brief half
is the CRO's G1 census (proportionate sign-off). Later groups land as CONTRACTS-only enrichment lists.

### v0.12 addendum (2026-10-14 ~14:1xZ, 1.0.0_SA_CTO~Z) -- FWD-22 enrichment: catalog rows for G2, G3, G5, G6

**Input.** `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/INDEX.md` (G2 131, G3 42, G5 36, G6 12 contracts). Tool shapes follow NFRA_OPLGTW v3.1 (client data is
one set of `client_*` tools with vendor adapters).

**Enrichment list (fold into round 13 if it is not yet issued; else round 14, `2.0.0_SA_COO~MI`):**
1. **G2:** one `silver_datasets` row per contracted table (BD 30, Orion/Eclipse 9, SmartX 13, Schwab 57, Commonwealth 12,
   Tax SMA 1, own ETFs 8, Yahoo 1), each with `fork_keys` (firm key segment or row column, account column, last-4
   derivation and its measured collisions, platform label and source), `read_tool` = the `client_*` tool once deployed.
   Live 49F BD rows name `opal-data-bd/silver/`.
2. **G3:** rows for the 9 live uncatalogued datasets; re-rule `ft.04.portfolios-aum-metrics` to deny (no page reads it,
   frozen 58 trading days); drop rows naming `json/mdpf/**` (0 keys); retire `portal_lookup.py` channel `mdpf` and correct
   `mdpf-platinum` (daily snapshots now in `archive/`). `json-tiered/` rows state it is authenticated-only once Z-S114
   closes.
3. **G5:** rows for the 36 ETF contracts (no `opal-data-etfs` row exists today), with the newest-part-per-date rule
   and each rival row's `claim` column named.
4. **G6:** correct the `news` row's sizes (381,261 items, about 1,000 a weekday); rows for `opal-keyword-intelligence`
   and the trending archive; mark the semantic chain, `seeking-alpha-article-urls` and `opal-harvest-articles` as
   frozen or empty, never as current.
5. **nl_tags and common_queries** from each group on every row; `read_tool` never names an undeployed tool.

**Sign-off.** CONTRACTS-only enrichment (FWD-22 text unchanged): no half re-opens.

### v0.13 addendum (2026-10-14 ~14:3xZ, 1.0.0_SA_CTO~Z) -- FWD-22 enrichment: G4 catalog rows

From `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G4_mdpf_delta.md` @7ec87a87e5:
- add rows for the delta tables (`model_aua_positions`, `model_composition`, `ai_classified_securities`), with fork keys
  on the account-grain row;
- mark `partner_held_etf/49financial` and `non_model_aua/49financial` as do-not-serve, with G4's reasons;
- record that `opal-data-mdpf` gold is a mirror of the served platinum (OVERLAP 100%, measured), so no tool targets it.
Fold into the open catalog round. CONTRACTS-only.

### v0.14 addendum (2026-10-14 ~15:1xZ, 1.0.0_SA_CTO~Z) -- client-data rows point only at opal-data-assets vendor silver (Andrew-direct)

Per `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_150xZ_CLIENT_DATA_ONLY_OPAL_DATA_ASSETS_VENDOR_SILVER.md` and NFRA_OPLGTW v3.4:
- Client-data rows name `opal-data-assets/<vendor>/<firm>/silver/` as their read location and `read_tool` a `client_*`
  tool. No row offers `opal-data-bd`, `opal-data-mdpf/mdpf/feeds/model_aua_positions` or the per-firm `taxsma_assets` gold
  as a tool target. Where a row was written for them, it is marked `not_served` with this record cited.
- The 49F BD rows state the measured lag (row Z-S110) and are never presented as current.
CONTRACTS-only.

### v0.15 addendum (2026-10-14 ~18:5xZ, 1.0.0_SA_CTO~Z) -- 49F BD rows read opal-data-bd (Andrew-direct)

Per `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_183xZ_49F_BLACK_DIAMOND_FROM_OPAL_DATA_BD_AND_THE_TARGET_LAYOUT.md` and NFRA_OPLGTW v3.6: the 8 49F Black Diamond rows name `opal-data-bd/silver/<table>/` (CRO~Z G2f) as their read
location, with the lag in trading days. The `not_served` mark from v0.14 is lifted for these rows only. Every other
client row is unchanged. When the migration lands BD 49F in `opal-data-assets/blackdiamond/` in LGIC_NAMING form, the
rows re-point. CONTRACTS-only.

### v0.16 addendum (2026-10-14 ~19:3xZ, 1.0.0_SA_CTO~Z) -- FWD-22 enrichment G5r: rival-fund catalog rows

From `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G5r_rivalfunds_spec.md` @e1b9937129: the 13 rival gold tables and the platinum manifest get table-grain rows. Each row carries:
- the newest-part rule;
- the `claim` column named on the inferred tables;
- fund keys (`fund_ticker`, `report_date`, `position_id`);
- the security identifiers and their fill rates;
- nl_tags.
The coverage row says that latest-report freshness is read from `canonical_shape` (Z-S124). Land them after the Friday
rows (G5 wave A, G6, G3). CONTRACTS-only.

### v0.17 addendum (2026-10-15 ~19:4xZ, 1.0.0_SA_CTO~Z) -- the gateway finish by EOD Fri 2026-10-16: CONTRACT C-GROUP; two index workstreams

On the CRO plan `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_FINISH_PLAN_EOD_20261016.md` @6cc033c818.

**Andrew, verbatim** (site Z session of `4.0.0_SA_CRO~Z`, ~18:4xZ, carried in the plan):

> "Yes I want to make sure that we have a very clean and tight process to get this completely done by end of day tomororw.
> We have the compute necessary to handle it on this box and it's not complicated work. Here is what it looks like: COO~MI
> focuses on getting those data contracts indexed in MCP channels. This should include everything in opal-data-harvest,
> every vendor/firm combo in opal-data-assets, opal-data-etfs using whatever we use for the monthly
> reconciliation/accounting, wherever the served rivalfunds outputs live, opal-data-portal-v2 for whatever is served to
> the portal not including advisor intelligence and investor reporting surfaces. We need to push through this
> aggressively so we may want to have 2 COOs ~MI and ~MI2 and they split that workload. While this is happening, we have
> COO~O handle whatever opalgateway server infrastructure needs to be done to accomodate and managing entitlements/access,
> through NFRA_OPLGTW. While this is happening we have COO~MP there doing passes on the /gateway page of the
> mcp.opalinvest.dev making sure everything is extremely legible, clean, and well-designed, using the opalinvest.com website
> design fixtures, as well as making sure that everything is readable by human eyes and not wrapped or squished on text and
> segments. The most important thing is really that each displayed tool segment is very clearly segmented, i recommend this
> being by bucket, and in the case of opal-data-assets, by client/vendor pairs. I want to figure out how we pull any
> possible parallelization lever to get this done, so keep that in mind as you put together your analysis."

GO at ~19:2xZ (relayed by `4.0.0_SA_CRO~Z` msg 34543): "We have usage, run it now" and "get it to CTO and let's get this going".

#### CONTRACT C-GROUP (owned by NFRA_MCPINDEX; read by NFRA_MCPORTAL and NFRA_OPLGTW)

1. **`bucket`, on every catalog row and every `tool_index` row.**
   - Its value is the S3 bucket name the row reads, for example `opal-data-harvest`, `opal-data-assets`, `opal-data-bd`,
     `opal-data-etfs`, `opal-data-portal-v2`, `opal-data-mdpf` or `opal-data-news-v2`.
   - A non-S3 source names its store: `dynamodb`, or `graph` for the Microsoft tools.
   - The value is read from the row's own source path, never typed from memory.
   - MX-c-21's `source_group.id` IS this value. There is one field and one spelling.
2. **`vendor` and `firm`, on every opal-data-assets and opal-data-bd row.**
   - `vendor` is one of: `schwab`, `blackdiamond`, `orion`, `eclipse`, `smartx`, `commonwealth`, `gateway` (Tax SMA),
     `market` (a non-client source: trueshares, pathfinder, yahoo).
   - `firm` is one of: `49financial`, `cottonwood`, `inflection`, `multi` (one object mixes firms: SmartX, Tax SMA, and
     any Schwab master that serves more than one firm), or `none` (`vendor: market`).
   - `firm` comes from `infra/logic/registry/catalog_fork_keys.json`, the same join MX-c-19 used, or from the row's own
     key segment. A row that neither source resolves carries `firm: unresolved` and is listed in the release record.
     It is never guessed.
   - The 24 rows MX-c-19 set (23 `49financial`, 1 `inflection`) keep their values.
   - **AMENDED ~22:0xZ (`2.0.0_SA_COO~MP` msg 34589): tool-level pairs.** Each `tool_index` entry whose rows are opal-data-assets or
     opal-data-bd also carries `serves`, the list of distinct (`vendor`, `firm`) pairs taken from the catalog rows that name it as
     `read_tool`. A single-pair field is not used: the `client_*` tools serve many vendors, and one pair would read
     `unresolved` for exactly the tools that matter. /gateway lists a tool under EVERY pair in its `serves`, so a tool can
     appear in several sub-segments. A vendor-specific tool (for example `schwab_query`) serves one pair. A tool with no
     assets/bd rows has no `serves`. MX-c-21 writes it from the rows; it is never typed.
3. **The display and discovery group key is exactly (`bucket`) for every bucket, and (`bucket`, `vendor`, `firm`) for
   opal-data-assets and opal-data-bd.** No other grouping field is introduced. A new value in either list is an addendum
   here, not a local spelling.
4. **CORRECTED ~20:0xZ (`2.0.0_SA_COO~MI` msg 34558): the `firm` VALUE is NOT a pure label.** `_silver_answer` (MX-r-14) shows a
   firm-scoped row to its own firm whenever `firm` is a known firm, so setting `firm` to `49financial`, `cottonwood` or
   `inflection` WIDENS catalog visibility to that firm's principals. Every catalog release that adds or changes a known-firm
   value carries its own never-widen pair naming those rows, gated on the difference control at 0 cross-firm leaks.
   `multi`, `none` and `unresolved` are not known firms and stay invisible to firm principals. Data access is unchanged: it
   needs the firm's data grant (NFRA_OPLGTW v3.1 Ruling 2 / v3.2).

**Scope of FWD-22 for this finish (Andrew's list):**
- everything in opal-data-harvest;
- every vendor/firm pair in opal-data-assets, plus opal-data-bd (49F BD, v0.15);
- opal-data-etfs: the monthly reconciliation set, meaning the inputs and outputs of `etfs-reports-orchestrator`;
- the served rival-fund outputs (`rivalfunds/etfs/gold/*` and the platinum page manifest);
- opal-data-portal-v2 rows served to the portal, EXCLUDING advisor intelligence and investor reporting. Rows under
  `advi/` or `irpt/` surfaces come out of scope and are listed in the release record.

**Two workstreams, disjoint files, one project (CLAUDE.md rule 27):**
- **ASSETS, `2.0.0_SA_COO~MI`:** the opal-data-assets and opal-data-bd source files in
  `workflows/atom_decomposition/catalog_entries/`. It adds C-GROUP and links each row's `read_tool` as NFRA_OPLGTW's
  `OG-cl-*` tools go live.
- **RESEARCH, `2.0.0_SA_COO~MI2`** (a new seat that `0.0.0_AB_MSTR~Z` spawns): the harvest, etfs (including rivalfunds),
  portal-v2, mdpf and news source files. It adds C-GROUP and drops the out-of-scope rows.
- Only ONE release cell per catalog release runs the emitter and writes `DATA_CATALOG.yaml`. The two COOs take turns at the
  release, never a shared file.

**MX-c-21 and MX-c-22 (COO~MI msg 34542): YES, both enter round 18.**
- MX-c-21 implements C-GROUP item 1 on `tool_index`.
- MX-c-22 is the `etfs_get_positioning` extension, with the old answer byte-equal.

**Done by 2026-10-16 ~22:00Z:**
- every in-scope row carries C-GROUP and a `read_tool` naming a live tool;
- `opal_discover` returns one row per bucket by plain words, recorded.

CONTRACTS-side under FWD-22; ENDPOINT unchanged.

### v0.18 addendum (2026-10-19 ~14:4xZ, 1.0.0_SA_CTO~Z) -- ENDPOINT: every /gateway surface indexed, every listed tool tested, a cheat sheet per employee (Andrew-direct)

**Andrew, verbatim** (`1.0.0_SA_CTO~Z` terminal, ~14:1xZ; record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_141xZ_GATEWAY_INDEXED_ALL_MCPORTAL_SURFACES_TOOLS_TESTED_PER_EMPLOYEE_CHEAT_SHEETS.md` @4a337dec2e):

> "1.) Opalgateway needs to be properly connected and indexed across all the surfaces currently listed in the MCPORTAL. 2.) All
> those tools need to be tested so we can be sure they actually work. 3.) We need to be able to provide a "cheat sheet" or some
> kind of instructional document that can be provided to the team so they know how to query. These cheat sheets should be broken
> out by employee so they focus on the tooling that is actually relevant to their job (e.g. all the opal-data-assets for the
> operational team versus opal-data-harvest for the asset management team vs opal-data-etfs for the CFO, etc etc)."

**Ground truth at authorship (repository source files, claim: measured from source, NOT the served catalog):**
- 319 catalog rows in `workflows/atom_decomposition/catalog_entries/`, of which 192 carry a `read_tool` (61 distinct tools);
- 57 rows carry no `bucket`, or a non-C-GROUP spelling;
- `tool_index/members.yaml` holds 91 members: 11 (a), 68 (b), 12 (c).
- The served gateway registers 103 tools (`CODE13_SERVED.json`, release 6b1a9bd292).
- The first act of round 22 re-measures all of these from the SERVED artifacts.

#### ENDPOINT -- three new outcomes (no FWD is a wait: each is proven by an act a seat runs on demand)

Cures R1-R3 of `3.0.0_SA_CVO~Z`'s refusal
(`org/tier1_exec/3.0.0_SA_CVO/deliverables/L4R_REVIEW_NFRA_MCPINDEX_v0.18_RATIFIED_TEXT_20261019_Z.md` @efdb1d6b00) are applied
below.

**THE DENOMINATOR (frozen at the cut, all three FWDs read it):** every CHANNEL `/gateway` on mcp.opalinvest.dev lists at the cut,
of EVERY kind, and every tool listed under it.
- The kinds are `bucket`, `store`, `integration` (YCharts, Schwab, Black Diamond, globgrph, opal_portal, portal_index,
  advi_billing, opal_discover), `native` (Microsoft 365) and `undeclared`. The source is `GatewayChannel.kind` and
  `admin_gateway_breakdown.py`.
- The denominator also includes the (`vendor`, `firm`) segments inside opal-data-assets and opal-data-bd (C-GROUP item 3).
- It is read from the SERVED page by one census, printed with its count per kind, and committed as
  `GATEWAY_SURFACE_CENSUS_<date>.json`.
- A channel added later enters by addendum, never silently.
- `undeclared` is not a surface to index. It is the residue FWD-23 empties.

- **FWD-23 -- Indexed across every surface.**
  - Every catalog row under every census channel carries C-GROUP and a `read_tool` naming a tool the deployed gateway serves.
  - Every census tool is either (a) linked to at least one such row, or (c) with its stated reason. Member (b) is 0 inside the
    denominator.
  - An integration or native channel with no catalog rows is read PER TOOL, (a) or (c), never per row.
  - The `undeclared` channel holds 0 tools, or each remaining tool is listed as (c) with its stated reason.
  - `opal_discover` answers each bucket and store channel by a plain-words subject.
  - Proof: the emitter's refusal set is empty against the census, plus one `opal_discover` call per bucket and store channel
    through the served gateway, recorded. The negative arm is one channel planted with no row and no (c) reason, which must
    refuse.
- **FWD-24 -- Every listed tool tested.**
  - Every census tool, under EVERY channel, has a recorded live call through the SERVED gateway by a real signed-in principal.
    The verdict per tool is one of:
    - `PASS`: a correct non-empty answer, checked against the row's or the integration's source;
    - `EMPTY-CORRECT`: an empty answer the source confirms is empty;
    - `REFUSED-CORRECT`: an entitlement refusal for a principal not granted;
    - `PREVIEW-ONLY`: a tool that sends or writes passed its non-sending path (the `confirm=false` preview, or a dry-run flag).
      Its send leg is UNEXERCISED and is named as such;
    - `FAIL`: with its class.
  - **CTO narrowing, labelled as such:** the battery never exercises a send leg. That is this seat's safety default, not
    Andrew's word ("All those tools need to be tested so we can be sure they actually work"). Whether a send leg runs against a
    sink the principal owns (their own mailbox or chat) is Andrew's call, and is put to him as ONE open call. Until he widens it,
    sending tools grade `PREVIEW-ONLY`.
  - The battery is ONE committed, re-runnable script. It is the per-tool test, not a standing monitor: it runs on demand and at
    each gateway release, and never on a timer.
  - Every `FAIL` becomes a defect cell in NFRA_OPLGTW (the gateway's code) or here (a catalog row).
  - FWD-24 is REALIZED at 0 FAIL on a run after the last fix. The REALIZED line lists every `PREVIEW-ONLY` tool by name.
  - Proof: the battery's own run plus one planted broken tool, which must read FAIL.
- **FWD-25 -- A cheat sheet per employee.**
  - Every Opal employee with a live gateway grant gets ONE instructional document. It holds only the tools their CURRENT grant
    reaches, grouped by bucket (and by channel for integration and native tools).
  - Each tool carries 2 to 3 example plain-English questions, and every example is a query FWD-24's battery ran and passed. No
    untested example ships.
  - Each sheet opens with how to connect (the Claude connector, first sign-in) and how to tell a refusal from an empty answer.
  - Generated from the catalog plus the battery plus the grant as it stands. NEVER hand-typed per person. A second run reproduces
    the same sheet, and a sheet follows whatever grant is live when it is generated.
  - Proof: the generator run for one employee whose CURRENT grant spans two buckets. Every example on that sheet is re-run as
    that principal through the served gateway and reads PASS.
  - Negative arm: an employee without a bucket's grant gets no tool from that bucket on their sheet.
  - No human read is on the proof path.

#### Proposed to Andrew (off every proof path; proposing is legal, no gate is implemented)

- **Who reaches what.** Cheat sheets follow grants, so a sheet scoped to a person's job needs that job's buckets granted.
  `4.0.0_SA_CRO~Z` drafts the roster with a proposed role-to-bucket mapping:
  - the source is each internal user's Entra job title and department, plus their current gateway grant;
  - his three examples are the seed: opal-data-assets to the operational team, opal-data-harvest to asset management,
    opal-data-etfs to the CFO.
  - Every proposal that WIDENS a current grant is marked. A widening is applied by NFRA_OPLGTW under never-widen on his word.
- **Send legs:** the one open call named under FWD-24.
- **Delivery:** one document per person, in a folder on the Opal SharePoint site the gateway's `upload_text_to_site` writes. The
  folder is named at the cut, and he may name another.

#### Placement

- **Owner:** NFRA_MCPINDEX, `2.0.0_SA_COO~MI` issuer, for FWD-23, FWD-24 (the battery) and FWD-25 (the generator).
- **NFRA_OPLGTW** (`2.0.0_SA_COO~O`) takes:
  - every FWD-24 `FAIL` in the gateway's code, as a defect cell in its batched releases;
  - any grant widening Andrew approves.
- **NFRA_MCPORTAL** (`2.0.0_SA_COO~MP`) supplies the census read of `/gateway` and makes no page change for these outcomes.
- **Round 22 builds the thread:** ONE segment (opal-data-harvest), end to end. Census, then indexed (FWD-23), then battery
  (FWD-24), then one employee's sheet (FWD-25). The next rounds enrich segment by segment.

ENDPOINT changed (FWD-23, FWD-24, FWD-25 added): the ratified-text half re-signs.

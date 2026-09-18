# BRIEF -- The Opal MCP tool index: every data property answerable in Claude, indexed from one catalog

**Author:** `4.0.0_SA_CRO` | **Written:** 2026-09-17 (UTC) | **Mode:** NEW (no project exists; prior art is heavy)
**Asked by:** Andrew, directly at this seat's terminal, 2026-09-17; five decision cards answered by him in-session.
**Consumer:** `1.0.0_SA_CTO` `/endpoint --forward`.
**Research record this brief stands on:** `docs/briefs/opal-mcp-tool-index-scoping-20260917.md` @`2a7fc3339f`
(the property inventory, the tool census, the prior-art review, with their citations). Not repeated here.
**Companion brief:** `docs/briefs/mcportal-tech-ops-dashboard-brief-20260917.md` @`cad25ffc96` (its MCP Server
page displays this index).
**Vintage:** CLOUD `a332b5c3f3` for code reads; naming canon read at HEAD today (`NAMING_SCHEMA.json` v1.10).

---

## ANDREW'S WORDS, VERBATIM (this terminal, 2026-09-17)

**The context he is presenting to the CEO:** *"I'm developing a user-friendly Opal Claude Plugin; one Opal-specific
endpoint that links to our AWS/MS directly, therefore having access to whatever we display in the portal +
schwab/black diamond/orion/eclipse/smartx/etc. + on-demand Bloomberg/YCharts. I set this up about 2 months ago and
use it daily for engineering workflows but hadn't opened it up to the team aside from Alyssa on a limited basis
because I didn't think there was interest in this kind of tool. Littledog has already gone over it, MS-based
authentication is in place + lives in a private network partition in AWS. . -- The presentation will be to our CEO,
so I need it to be clean and clear sequencing of outcomes based on these projects and why we're doing them and what
they offer to the firm."*

**The ask:** *"I need you to essentially scope out how we could expand the tool index in the Opal MCP Server
endpoint to address each of these properties. The issue with the official plugins is that they are very poorly
indexed, and I don't want us to have that problem, so I'd like to develop a system for keeping this largely in AWS
(on-demand functions secondary, but we should explore them), whereby each data segment (most of it is in
opal-data-assets silver parquets, portal data being in the consumed tables from opal-data-portal-v2) is thoughtfully
analyzed and we create tool calls for common queries."*

**His answers to the five cards:** *"1.) Refer to LGIC naming, there should be convention there to go off of. 2.)
Versioned in S3 works. 3.) I would put it under D9 Opal Workflows. 4.) Opal Staff only, but we'll be beta testing
it one at a time. 5.) There are precomputed tables for the Portal that we're already pointing at, pretty much
everythng we're pointing at in aws is precomputed tables. With that said, yes we are focusing on live queries
particularly for the opal-data-assets tables"*

---

## PART I -- THE OUTCOME TERRITORY

"A staff member" means an Opal employee signed in with their Microsoft account and admitted to the beta.

### O1. A staff member asks Claude "what data do we have on X, and how fresh is it" and gets the right answer every time
A small discover family, loaded in every session, answers from one catalog: which property and dataset holds it,
how fresh it is, what firm scope applies, its caveats, and which tool to call next. This is the fix for the
poorly-indexed-plugin problem, and every other outcome is indexed from it.

### O2. A staff member asks in plain English for anything the portal shows and gets the portal's own number
Model AUM and account distribution, ETF positioning, market and macro views, advisor intelligence. The tools read
the same precomputed tables the portal already points at, so Claude and the portal cannot disagree.

### O3. A staff member asks about positions, balances and transactions at either Schwab master
Live queries over the Schwab silver tables in `opal-data-assets`, one master and one date per answer, never summed
across masters.

### O4. A staff member asks the same kinds of question of Black Diamond, Orion, Eclipse and SmartX
Holdings, transactions, models and performance from each platform's silver tables, through live queries, each
property analyzed first so its common questions become purpose-built tools.

### O5. A staff member asks about the ETFs (TrueShares, Pathfinder) -- holdings, net assets, daily NAV
Same ladder, per fund.

### O6. A staff member whose question fits no purpose-built tool still gets an answer, safely
A typed query over any catalogued dataset -- filters, group-bys and aggregates as a structured object, never raw
SQL -- with hard caps and a response that states its date, completeness and whether it was cut short.

### O7. A staff member asks for one client or household and sees them across custodian and platform
Requires matching the same person across systems. Stated as an outcome because it is where the value compounds;
its precondition is in Part V.

### O8. A staff member asks for long history or live market data and gets it on demand
On-demand functions for what the Gateway's own query engine cannot hold (long scans), and the existing on-demand
vendor reads (Bloomberg standing read, YCharts) presented through the same index.

### O9. Andrew admits staff to the beta one person at a time, and each person sees only the tools and data he granted
Nobody outside Opal staff is admitted. A person not yet admitted sees none of the data tools.

### O10. Adding the next property or tool is a catalog entry plus a tool, and the index describes it without anyone hand-writing a description twice
The catalog entry (business meaning, example questions, grain, freshness field, firm-scope rule, never-sum rules,
producer, tools) is what Claude reads; a tool with no catalog entry, or no safety classification, does not ship.

---

## PART II -- WHERE THE BOUNDARY SITS

| This project OWNS | It RELIES ON (and does not change) | Sibling |
|---|---|---|
| The catalog: its schema, its versioned home in S3, its generation into the Gateway | `app/refs/DATA_CATALOG.yaml` as first content; its one writer `emit_catalog_v02.py` | OPAL_ANALYST (closed) |
| The discover tools and the per-property purpose-built tools | The Gateway's sign-in, tiers, guard, audit | NFRA_OPLMCP, SCTY_MCPGUARD |
| Generalizing the typed query engine beyond Schwab | `app/integrations/schwab/engine.py` (DuckDB + PyArrow, capped) and the grant model | NFRA_OPLGTW (EXECUTING) |
| One fenced read role per property, to exact silver prefixes | The silver tables and their producers | each pipeline's owner |
| The per-property analysis ("what do people actually ask") | The portal's precomputed tables and their publishers | MDPF, ETFS, ADVI pipelines |
| Tool names and their convention (Part IV, finding 4) | The naming canon and registry | LGIC_NAMING, LGIC_ENFORCE |

**Explicitly NOT this project's:** enabling the Schwab tools in deployment and finishing their entitlement work
(NFRA_OPLGTW's); the admin screen that grants access (the mcportal brief, O7 there); new precomputed tables (none
are asked for -- the portal's exist, and silver is queried live); partner or client access (zero, until Andrew names
a first consumer -- his standing 2026-08-20 ruling); Tax SMA tools (its data contract says "no deployed
implementation"; it joins when D9's tax work lands); any new vendor egress (YCharts stays on his per-use word).

**Placement, his word:** D9 "Opal Workflows" -- the Gateway's directive, beside NFRA_OPLGTW and NFRA_SPMOVE.

---

## PART III -- THE QUALITATIVE BAR

- **Discover:** a staff member who does not know which system holds a fact is pointed to the right tool on the
  first try, where today they would ask Andrew.
- **Portal parity:** for any figure the portal displays, Claude returns the same figure with the same as-of date --
  a disagreement is a defect in this project, not a caveat.
- **Silver:** a staff member gets a Schwab or platform answer without anyone opening the vendor's website or
  downloading a file.
- **Index quality:** Claude picks the purpose-built tool over the typed query for a common question without being
  told to; if it reaches for the typed query first, the index failed.
- **Honesty:** every answer states its date and whether it is complete; "no data for that date" is never rendered as
  zero.
- **Isolation:** a staff member granted one Schwab master cannot be shown the other by any phrasing.
- **Beta:** each admitted person's first week produces a list of questions the index could not route -- that list is
  the next round's analysis input.

---

## PART IV -- THE SUBSTRATE (findings; detail and citations in the scoping record)

1. **44 tools are enabled and none answers a question about Opal's own data.** 35 are generic Microsoft 365
   wrappers; 6 YCharts; 1 portal upload; 2 knowledge graph. Tool descriptions are Python docstrings with no catalog
   behind them.
2. **The portal catalog and its gate are built but unreachable as tools.** `DATA_CATALOG.yaml` v0.3 (36 served-data
   rows, each with business meaning, firm, freshness field, serve/deny verdict) and `catalog_gate.py` sit behind
   one HTTP route. Five business tools were designed and parked (`graphql_plumbing/DESIGN.md:41-49`). The D6 PRD
   ruled that a second catalog must never exist (`D6_OPAL_ANALYST_GRAPHQL_PRD.md:57,102`).
3. **The live-query pattern for silver is built.** Five Schwab tools, a typed query grammar, DuckDB in a capped
   child process, per-person grants, a response envelope. Built and tested; not enabled in deployment. It exposes
   three `dim_*` tables; transactions and the `fact_*` tables are not yet exposed.
4. **Naming -- what the canon gives and what it does not.** The canon's resource grammar is
   `{system}-{scope}-{function}[-{qualifier}]-{kind}`: `system` is a key of `infra/logic/registry/systems.json`
   (`schwab`, `blackdiamond`, `orion`, `eclipse`, `smartx`, `mdpf`, `etfs`, `advi`, `ycharts`, `bloomberg`, ...);
   `function` is a base-form verb; scope is passed as scope, never folded into another token
   (`lib/opal_naming.py:1589-1602`). **`NAMING_SCHEMA.json` v1.10 does not list MCP tool names among what it
   grades** (`not_covered` names Terraform labels, tags, AWS ids, DNS, event sources, API routes -- and is silent
   on tools). The existing Schwab tools already follow the canon's shape by analogy: `schwab_query(master=...)` is
   `{system}_{function}` with scope as an argument. So his answer resolves to: **tool name =
   `{system}_{function}[_{qualifier}]`, system from the registry, scope (firm or master) always an explicit
   argument validated against `scopes.json`, the cross-property discover tools under the reserved `opal` system.**
   Whether that becomes a graded part of the schema is the CTO's schema-bump call, not this brief's.
5. **Everything the portal points at is precomputed** (his statement, consistent with the census: `platinum/mdpf`,
   `platinum/etfs`, `platinum/advi`, `json/*` are publisher outputs). Silver is one parquet per table per scope per
   business day -- small objects, suited to live DuckDB reads.
6. **Silver holds all firms in one bucket, split only by key prefix.** Tool-side firm scope plus a fenced read role
   per property is the isolation (the Schwab model). Served advisor intelligence for Inflection and Cottonwood
   lives in firm buckets, not the portal bucket.
7. **No Glue or Athena sits over silver or gold today.** O8's long-history path has no substrate yet.
8. **Entity resolution is parked** (the D6 addendum made it a prerequisite for cross-system client questions and
   gated it on D3's residual enum).
9. **One live defect:** `read_teams_attachment` is enabled but denied to every tier because it has no safety
   classification -- the failure any unclassified new tool repeats.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

1. The catalog's schema, extended from the portal catalog's existing fields to cover silver datasets, with one
   writer and a versioned S3 home named by the naming builder.
2. A per-property analysis pass before that property's purpose-built tools are cut.
3. One read role per property fenced to exact prefixes, and the grant model extended beyond Schwab's two masters
   and three datasets.
4. Every new tool classified in `destructive_ops` and `data_entitlement`; the pinned tool-count tests move with
   each tool.
5. NFRA_OPLGTW's Schwab tools enabled in deployment (that project's act) before O3 can be exercised.
6. A way to match one person across systems before O7.
7. A query substrate over long history before O8's first half.
8. Each new integration goes through the standing enablement checklist (`NFRA_INTEGRATIONS_STANDARD.md` s.6, 8.1).
9. A beta roster Andrew controls, one person at a time (the mcportal Entitlements tab is the intended screen; the
   operator command is the path until it exists).

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-09-17 from the repo only. 49 tools registered, 44 enabled. Schwab integration not in
`ENABLED_INTEGRATIONS`. NFRA_OPLGTW EXECUTING (PRD v0.7). D9 members today: OPAL_TAXSMA, OPAL_TAXROSTER,
OPAL_TAXSMA_PT2, OPAL_TAXSMA_REGISTRY, IRPT_FNTEND, IRPT_BCKEND, NFRA_OPLGTW, NFRA_SPMOVE. No project for this
brief exists.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

1. No AWS state was read. Table sizes, object counts and query timings over silver are unmeasured -- whether a
   given common question fits the Gateway's caps is unknown until exercised.
2. The "common questions" per property are not enumerated here; that is the analysis pass (Part V.2), and the beta's
   unrouted questions feed it.
3. The tool-naming rule in Part IV.4 is this seat's reading of his answer against the canon. The canon does not
   grade tool names today.
4. Bloomberg on-demand is the SITEZ standing read; this brief does not claim it is reachable from the laptop fabric.
5. Citations are the research passes' reads at the stated vintage, not re-verified line by line here.
6. The earlier scoping record recommended D6 and business-first names; both were overruled by him above and the
   record is kept unedited as research, not as direction.

---

## REFS

```
  BRIEF PATH        docs/briefs/opal-mcp-tool-index-brief-20260917.md
  PROJECT           NONE-YET (placement: D9 Opal Workflows, his word)
  EXISTING PRD      NONE
  SIBLING PROJECTS  NFRA_OPLGTW, NFRA_SPMOVE, LGIC_NAMING, LGIC_ENFORCE, OPAL_ANALYST (closed), NFRA_OPLMCP,
                    SCTY_MCPGUARD, the mcportal project (NONE-YET)
  RESEARCH RECORD   docs/briefs/opal-mcp-tool-index-scoping-20260917.md @2a7fc3339f
  PRIOR ART         app/refs/DATA_CATALOG.yaml + graphql_plumbing/catalog_gate.py; app/integrations/schwab/*;
                    app/integrations/base.py + NFRA_INTEGRATIONS_STANDARD.md;
                    ADVI_PLATINUM_AGENTIC_QUERY_INDEX_STRATEGY_20260806.md (metric registry, broker ops; unapproved)
  MEASURED AT       2026-09-17, repo reads only
```

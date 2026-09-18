# SCOPING BRIEF -- Expanding the Opal MCP Gateway tool index, one data property at a time

**Author:** `4.0.0_SA_CRO` | **Written:** 2026-09-17 | **Mode:** NEW (no project exists; prior art is heavy)
**Asked by:** Andrew, directly at this seat's terminal, 2026-09-17.
**Vintage of every code read below:** CLOUD @ `a332b5c3f3`. Line citations come from three read-only research
passes run for this brief; they are the passes' reads, not re-verified line by line here.
**Consumer:** Andrew (decisions in s.6), then `1.0.0_SA_CTO` `/endpoint --forward` if a project is made.

---

## ANDREW'S WORDS, VERBATIM

> I'm developing a user-friendly Opal Claude Plugin; one Opal-specific endpoint that links to our AWS/MS directly,
> therefore having access to whatever we display in the portal + schwab/black diamond/orion/eclipse/smartx/etc. +
> on-demand Bloomberg/YCharts. [...] The presentation will be to our CEO, so I need it to be clean and clear
> sequencing of outcomes based on these projects and why we're doing them and what they offer to the firm.

> I need you to essentially scope out how we could expand the tool index in the Opal MCP Server endpoint to address
> each of these properties. The issue with the official plugins is that they are very poorly indexed, and I don't
> want us to have that problem, so I'd like to develop a system for keeping this largely in AWS (on-demand functions
> secondary, but we should explore them), whereby each data segment (most of it is in opal-data-assets silver
> parquets, portal data being in the consumed tables from opal-data-portal-v2) is thoughtfully analyzed and we create
> tool calls for common queries.

---

## 1. WHERE THE TOOL INDEX IS TODAY

**44 tools are live; none of them answers a question about Opal's own data.**

| Group | Live tools | What they reach |
|---|---|---|
| Microsoft 365 (`app/tools.py`) | 35 | Email, calendar, OneDrive, SharePoint, Teams -- generic wrappers over the user's own Graph token |
| YCharts | 6 | Live YCharts API (held under the per-use vendor-egress rule) |
| Portal upload | 1 | `opal_data_refresh_upload` (Bloomberg PKLs) |
| Internal knowledge graph | 2 | `graph_cypher`, `graph_status` (Kuzu) |
| **Schwab (built, OFF)** | 5 | Schwab silver parquet, per-person grants -- not in `ENABLED_INTEGRATIONS` (`deploy-to-ec2.sh:170`) |

What is built but **not reachable as a tool**:
- The **portal data catalog** (`app/refs/DATA_CATALOG.yaml` v0.3: 16 channels, 36 served-data rows, each with
  business meaning, firm, freshness field and a serve/deny verdict) and its **deny-by-default gate**
  (`graphql_plumbing/catalog_gate.py`). Only the HTTP route `POST /query/v0` uses them.
- Five **business tools** designed and parked in `graphql_plumbing/DESIGN.md:41-49`: `find_account`,
  `get_account_details`, `get_account_performance`, `find_accounts_missing_fee_splits`, `get_account_data_issues`.

**Why the index is weak today -- the same failure as the official plugins:** a tool's description is its Python
docstring and nothing else. No catalog links a tool to its data, its grain, its freshness or the questions it
answers; the portal catalog never mentions Schwab, Black Diamond, Orion, Eclipse or YCharts.

**One defect found on the way:** `read_teams_attachment` (`tools.py:660`) is registered but unclassified in
`destructive_ops`, so it is denied to every tier including master. Any new tool that skips classification fails the
same silent way.

---

## 2. THE DATA PROPERTIES, AND HOW READY EACH IS

| # | Property | Where it lives | Grain | Refresh | Tool readiness |
|---|---|---|---|---|---|
| P1 | **Portal data** (MDPF models/AUM, ETF positioning, market/macro, advisor intelligence) | `opal-data-portal-v2` (`platinum/mdpf`, `platinum/etfs`, `json/*`); firm buckets for scoped advisor intelligence | Per firm, JSON | Daily publishers | **Catalog + gate built**; needs MCP tools |
| P2 | **Schwab** (masters 08242234 SmartX, 08335338 BD) | `opal-data-assets/schwab/{master}/silver/` -- 16 full tables + `dim_position/transaction/asset/balance` | Per master, per day | S3 event + 12:15Z sweep | **Tools built, OFF**; `dim_transaction` and `fact_*` not exposed |
| P3 | **Black Diamond** (Cottonwood; 49F dims/allocations/tax SMA report; 49F insurance) | `blackdiamond/{cottonwood,49f,49financial}/silver/` | Per firm, per day | Events + scheduled 07:05Z | Silver only |
| P4 | **Orion** (Inflection) | `orion/inflection/silver/fact_{assets,positions,transactions,performance}` | Per firm, per day | Mirror 13:05Z + event | Silver only |
| P5 | **Eclipse** (Inflection) | `eclipse/inflection/silver/fact_{models,portfolios_*,model_composition_N}` | Per day | Event + sweep | Silver only |
| P6 | **SmartX** | `smartx/platform/silver/` -- allocations, model AUM/holdings/performance, account allocations | Platform-wide, per day | On daily pull | Silver only |
| P7 | **ETFs** (TrueShares, Pathfinder) | `trueshares/*`, `pathfinder/*` silver | Per fund, per day | Events + 23:30Z | Silver only |
| P8 | **Tax SMA** | Design only (`MDPF_TAXSMA_DATA_CONTRACT.json`: "no deployed implementation") | -- | -- | **Not ready**: wait for D9 |
| P9 | **Bloomberg** | No silver; PKL uploads build portal `json/*` (covered by P1) | Per day | Manual upload | On-demand = the Bloomberg standing read (SITEZ) |
| P10 | **YCharts** | Live API | -- | Live | **6 tools live**; per-use vendor-egress rule |

Nothing declared for Addepar, Altruist, Fidelity or Pershing.

---

## 3. THE SYSTEM -- A THREE-RUNG TOOL LADDER PER PROPERTY, INDEXED FROM ONE CATALOG IN AWS

The fix for poor indexing is not more tools; it is that **every tool is generated from, and described by, one
catalog entry that a person wrote after analyzing the data segment.**

### Rung 1 -- DISCOVER (one small family, always loaded)
- `opal_catalog_search(question)` -> which property, dataset and tool answers this, how fresh it is, what firm scope
  applies, and its caveats.
- `opal_describe(dataset)` -> fields in business language, grain, what it must never be summed across.
- These two carry `alwaysLoad` so every session starts knowing the map.

### Rung 2 -- COMMON QUESTIONS (purpose-built, business-named)
Per property, the analysis pass lists the 5-10 questions people actually ask and each becomes a typed tool with a
tight input schema, for example:
- **Accounts/positions:** find an account, what does it hold today, how did it change since date X.
- **Transactions:** activity for an account or master over a date range.
- **Models:** what is in model M, which accounts follow it, drift from target.
- **AUM/performance:** firm or advisor AUM over time, account performance.
- **Data quality:** accounts missing fee splits, accounts with data issues (the parked D6 tools).

### Rung 3 -- TYPED QUERY (the escape hatch, never SQL)
The Schwab pattern, generalized: filters/group-bys/aggregates as a typed object, hard caps (Schwab: 500 rows,
30 s, 256 MiB, 12 source objects), and a response envelope that states the date, completeness and truncation.

### The catalog -- where it lives and what each entry carries
One entry per dataset, stored in AWS (versioned), generated into the Gateway at deploy. Each entry carries:
business meaning, example questions, grain, freshness field, firm-scope rule, "never sum across" rules, the
producing pipeline, and the rung-2 tools that read it. `DATA_CATALOG.yaml` already has most of these fields for
portal data -- **extend it; do not start a second catalog** (D6 PRD `:57`, `:102`: a second catalog is exactly what
that PRD ruled out).

### Compute -- AWS first, on-demand second
1. **Default: DuckDB inside the Gateway** over silver parquet -- already built and hardened for Schwab
   (`schwab/engine.py`). Cheap, no new infrastructure.
2. **Pre-computed answer tables** for the heaviest common questions (for example AUM over time) -- small gold
   tables built by the pipelines so the tool reads one small file instead of scanning history. Named by the LGIC
   builder (Rule 30).
3. **On-demand functions (explore):**
   - **Athena over silver** for long-history scans. No Glue catalog exists over silver today; one is needed first.
   - **Lambda** for work beyond the Gateway's ~2 GB / 30 s envelope.
   - **On-demand Bloomberg/YCharts** stay integrations with an explicit hosts list; YCharts stays per-use.

---

## 4. RULES EVERY NEW TOOL INHERITS (already law or already built)

- **Read-only.** Each tool is classified in `destructive_ops` and `data_entitlement`, or it is hidden and denied.
  The pinned count test (`tests/test_entitlement_admin.py:332`, `== 44`) moves with every tool.
- **Firm isolation.** Silver holds all three firms in one bucket, split only by key prefix. So the tool must
  enforce firm scope on the server, with a dedicated read role per property fenced to its exact prefixes (the Schwab
  model, C6). Opal staff see all firms; a firm sees only itself; **widening is Andrew-only**
  (`DATA_CATALOG.yaml:28-32`).
- **Internal first.** Partner access is zero until Andrew names a first real consumer (Andrew-direct 2026-08-20);
  parquet-backed tools are internal-first by the D6 addendum (`:159-165`).
- **No cross-master or cross-date sums** (NFRA_OPLGTW ruling). Two Schwab masters are two scopes.
- **Per-person identity**, never an app identity; every call is audited to the lake.
- **New integrations are off until enabled** through the G1-G8 checklist (`NFRA_INTEGRATIONS_STANDARD.md` s.6, 8.1).

---

## 5. PROPOSED SEQUENCE OF OUTCOMES

Each phase ends with something a person at Opal can do in Claude that they could not do before.

| Phase | Outcome for the firm | Why this order | Built already |
|---|---|---|---|
| **0. The map** | "What data do we have on X, and how fresh is it?" answered correctly every time | Every later tool is indexed from it; fixes the poor-indexing problem at the root | Catalog fields, gate |
| **1. Portal in Claude** | Anything the portal shows -- model AUM, ETF positioning, market views -- can be asked in plain English | Catalog, gate and the five business-tool designs exist; smallest build | ~70% |
| **2. Schwab custodian truth** | Positions, balances and transactions at both Schwab masters | Tools are built and tested; the gap is enablement plus transactions (shared with NFRA_SPMOVE) | ~80% |
| **3. Platform books** | Black Diamond, Orion, Eclipse and SmartX holdings, transactions and models through the same questions | Same engine and ladder, one property at a time; each needs its analysis pass and a fenced read role | Engine only |
| **4. One client, every system** | "Show me this household across custodian and platform" | Needs entity resolution (the parked D6 prerequisite) and phases 2-3 underneath | Design only |
| **5. On-demand depth** | Long-history questions and live market data on request | Athena/Lambda only once real query traffic shows where the Gateway envelope breaks | Nothing |

---

## 6. CALLS FOR ANDREW (each with a recommendation)

1. **Tool naming: business-first or vendor-first?**
   Rec: **business-first** (`positions_get(source=...)`) for rung 2, vendor-specific only for rung 3. A short list of
   business-named tools indexes better than one tool family per vendor. Caveat: the grains differ (per master,
   per firm, platform-wide), so the `source` argument must stay explicit and never merge silently.
2. **Where the catalog lives.**
   Rec: an **S3 control catalog** (the ADVI strategy's plan, `ADVI_PLATINUM_AGENTIC_QUERY_INDEX_STRATEGY_20260806.md`
   `:99-111`), generated into the Gateway at deploy, with `DATA_CATALOG.yaml` as its first content.
3. **Where the project sits.**
   Rec: **D6 "Opal AI"**, which was re-scoped on 2026-08-20 to agent tooling interfaces and has no members; one
   project with one phase per property, not one project per vendor.
4. **Who can use it first.**
   Rec: **Opal staff only** for the CEO rollout, consistent with the zero-partner ruling; partners are a later,
   named decision.
5. **Pre-computed answer tables or live scans?**
   Rec: **live DuckDB first**; build an answer table only when a common question measurably breaks the 30 s cap.

---

## 7. PRIOR ART TO REUSE, NOT REBUILD

| Artifact | Status | Reuse |
|---|---|---|
| `docs/architecture/D6_OPAL_ANALYST_GRAPHQL_PRD.md` | v0 shipped; GraphQL + business tools parked | One catalog; business tools compile internally, never raw query |
| `app/refs/DATA_CATALOG.yaml` + `catalog_gate.py` | Live behind `/query/v0` only | Rung 1 content and the firm gate |
| `app/integrations/schwab/*` (NFRA_OPLGTW, ratified v0.7) | Built, off | Rung 3 engine, entitlement model, response envelope |
| `ADVI_PLATINUM_AGENTIC_QUERY_INDEX_STRATEGY_20260806.md` | Proposed, never approved | Metric registry, structured broker ops, Glue/Athena plan |
| `app/integrations/base.py` + `NFRA_INTEGRATIONS_STANDARD.md` | Live standard | How each property plugs in |

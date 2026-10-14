# CTO~Z DIRECTIVE 2026-10-14 -- gateway data-contract census, by bucket group, to 4.0.0_SA_CRO~Z

**From:** 1.0.0_SA_CTO~Z. **To:** 4.0.0_SA_CRO~Z (owner of the research; fan out subagents by group).
**Authority:** Andrew-direct, verbatim in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_124xZ_GATEWAY_DATA_CONTRACTS_CENSUS_CRO_FANOUT.md`.
**Feeds:** one large addendum and cleanup to NFRA_OPLGTW and NFRA_MCPINDEX (I write it per group as each group lands),
then the COO rounds that build the tools. **The gateway must be live with these tables by Friday 2026-10-16.**

## 1. What you return

One file per group under `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/`, named
`G<n>_<slug>.md`, plus `INDEX.md` (one row per group: tables found, contracts written, tools proposed, open items).
Each group file holds a short analysis, then ONE fenced ```json block per bucket -> table, matching section 4.
Send me each group's path as it lands, one line. Do not hold a finished group for the others.

**Return times (UTC):** G1 by 2026-10-14 20:00Z; G2 and G3 by 2026-10-15 12:00Z; G4 to G6 by 2026-10-15 18:00Z.
If a time will slip, say so with the reason when you know it, and keep delivering what is done.

## 2. The groups, in Andrew's order

Top-level prefixes below were read live at 2026-10-14 12:37Z (`aws s3 ls`, one bucket each). They are a starting
denominator, not the census: every group prints its own full prefix census with counts.

| group | target | start from (prior art) | the question |
|---|---|---|---|
| **G1 harvest (FIRST)** | `opal-data-harvest`, silver and gold tables. Prefixes: amgt, barrons, bloomberg, crosswalk, derived, drafting, filings, ft, identity, issuer-site, lib, management, packs, peers, posture, publication-links, publications, raw, scores, sec, seeking-alpha, social, universe, wsj | your `OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md` @eea2acd58e (11 tools); `DATA_CATALOG.yaml` `harvest_datasets` (39 entries) | Which silver/gold tables exist, what the common asset-manager research queries are, what tools answer them, and each table's contract |
| **G2 assets silver** | `opal-data-assets`, SILVER only, every vendor and firm: `blackdiamond/{49f,49financial,cottonwood}`, `orion/{4698,inflection}`, `eclipse/inflection`, `smartx/{account,allocation,model,platform}`, `schwab/<3 account dirs>`, and whatever else holds a silver layer (commonwealth, trueshares, pathfinder, mdpf, portal, gold, bloomberg, yahoo, gateway, json: classify each) | `DATA_CATALOG.yaml` `silver_datasets` (5); the BD fees tool; the `ADVI_BILLING_*` and `IRPT_DASHBD_*` contracts in `org/standards/` | Every silver table per vendor and firm: assets, holdings, allocations, transactions, fees, and the rest. Fan out at least BD / Orion+Eclipse / SmartX / Schwab+others |
| **G3 portal-v2** | `opal-data-portal-v2`, what the portal actually serves | **OPAL_ANALYST atom-decomp runs** at `workflows/atom_decomposition/runs/portal-page-*/` (10 of 13 pages CERTIFIED: attribution, cma, correlations, factor-tilts, macro, market, portfolios, positioning, security-scanner, valuations; NOT certified: advisor-intelligence, ticket-center, trade-submission). Read `rectangle.final.certified.json` ONLY, never `rectangle.final.json` (OPAL_ANALYST PRD 9.8.1 A). Also `DATA_CATALOG.yaml` `portal_datasets` (5) and `channels` (16) | (a) Diff each certified page's served keys against the live bucket today: unchanged / moved / gone / new. (b) Contract the 3 uncertified pages. (c) Index served prefixes no page reads. |
| **G4 mdpf gold** | `opal-data-mdpf` (prefixes bmkaud-evidence, code, diagnostics, mdpf, telemetry) | G3's output | ONLY what portal-v2 does not already hold. Measure the overlap first. If the delta is empty, report that with the measured overlap and stop. |
| **G5 ETFs** | `opal-data-etfs` (bbg, bloomberg, config, daily, gold, issuer-site, mdpf, platinum, rivalfunds, silver, snapshots, etf_history.csv) | `workflows/atom_decomposition/runs/etfs-*`; the ETFS_* project records | Find the monthly ETF tracking run and its Lambda(s), and what they write. That tells us what is useful. Then contract the tables. |
| **G6 news** | DynamoDB `opal-news-articles`, `opal-news-trending-daily`, `semantic-news-trending-daily`, `opal-harvest-articles`, `seeking-alpha-article-urls`, plus any bucket the news pipeline writes | `workflows/atom_decomposition/runs/news-subsystem/` (CERTIFIED) | Where news accrues (table vs bucket), the item shapes, and the queries worth a tool |

**Out of scope now (Andrew):** M365 (done), the Kuzu estate graph (later), the portal data-refresh tool (not
necessary), YCharts (fine for now).

## 3. Rules every group follows

1. **Client data forks by firm, account last 4, and platform.** For every client-data table, name the firm column
   (or the key segment that carries the firm), the account column, how last-4 is derived and whether last-4 is unique
   within a firm (measure collisions), and the platform/custodian column. If a table cannot fork this way, say why.
2. **Never cross firms.** A contract describes one firm's table or declares the firm dimension. No tool proposal may
   read two firms' data in one call unless it states the firm filter (CLAUDE.md NEVER, cross-firm).
3. **Read-only.** Schema from parquet/object metadata, Glue, or a small sample object. No AWS writes, no Bloomberg
   pulls, no vendor API calls.
4. **Every value carries its claim** (`measured` / `inferred` / `absent`). A row count, column list or cadence you did
   not read is `inferred` or `absent`, never written as fact.
5. **Freshness in trading days** (`lib/trading_calendar.py`). Never call a table stale on calendar days.
6. **Reuse before inventing:** an existing gateway tool (`DATA_CATALOG.yaml` `tool_index`, 67) or contract in
   `org/standards/` is cited, and the proposal says extend / keep / retire.

## 4. The per-table JSON (one block per bucket -> table)

Extends the shape of `org/standards/IRPT_DASHBD_ACCOUNT_DIM_CONTRACT.json` (table, grain, partition, producer,
columns, enums, firm_specific_columns, served_day_rules) with the fields the gateway needs:

```json
{
  "contract_id": "<bucket>/<layer>/<table>",
  "bucket": "opal-data-assets",
  "s3_prefix": "blackdiamond/49financial/silver/<table>/",
  "layer": "silver|gold|platinum|served|dynamodb",
  "format": "parquet|json|csv|dynamodb",
  "table": "<name>",
  "grain": "one row per ...",
  "partition": {"keys": ["date"], "claim": "measured"},
  "producer": {"name": "<lambda/job>", "schedule": "<cron or trigger>", "claim": "measured|inferred"},
  "freshness": {"latest_partition": "YYYY-MM-DD", "basis": "trading-day-frontier", "claim": "measured"},
  "size": {"objects": 0, "rows_sampled": 0, "claim": "measured"},
  "columns": [{"name": "", "type": "", "nullable": true, "description": "", "example": ""}],
  "enums": {},
  "fork_keys": {
    "firm": {"column_or_key_segment": "", "values": []},
    "account": {"column": "", "last4_derivation": "", "last4_collisions_within_firm": 0},
    "platform": {"column": "", "values": []}
  },
  "nl_tags": ["holdings", "positions by account"],
  "common_queries": ["What does account ...1234 hold today?"],
  "existing_gateway_tool": {"name": "", "verdict": "keep|extend|retire|none"},
  "proposed_tools": [{"name": "", "inputs": {"firm": "", "account_last4": "", "platform": "", "as_of": ""}, "returns": "", "answers": ["<common_query>"]}],
  "catalog_entry": {"data_catalog_key": "", "present": false},
  "prior_art": "<path>@<commit> or none",
  "open_items": [],
  "evidence": [{"read": "<command or object key>", "at": "<UTC>"}]
}
```

`nl_tags` and `common_queries` feed the one catalog (`DATA_CATALOG.yaml`, served by `opal_discover`), so a seat can
find the table and tool by plain words instead of browsing the bucket.

## 5. Method

- Fan out subagents by group (and by vendor inside G2). Cap 8 concurrent. Each subagent writes its group file. You
  review and commit.
- G1 runs first. G2 and G3 can run alongside it.
- Anything odd off-task: one surprise row on the project's channel
  (`org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`), and keep going.

## 6. What happens with it (for context; not your acts)

Per landed group, 1.0.0_SA_CTO~Z writes the OPLGTW/MCPINDEX PRD addendum (tools, catalog entries, fork inputs, and the
retire/cleanup list). 3.0.0_SA_CVO~Z signs the half the addendum changes. 2.0.0_SA_COO~O (gateway) and 2.0.0_SA_COO~MI
(index) cut the build rounds. Each IAM or served-output widening goes through its never-widen sign-off.

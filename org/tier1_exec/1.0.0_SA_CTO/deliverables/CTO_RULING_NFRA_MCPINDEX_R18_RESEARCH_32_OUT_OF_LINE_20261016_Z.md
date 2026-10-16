# CTO ruling -- NFRA_MCPINDEX r18 RESEARCH: the 32 rows of section (b), 2026-10-16 ~02:3xZ

By `1.0.0_SA_CTO~Z`, on `2.0.0_SA_COO~MI2` msg 34655. Subject:
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI2/round18/research_no_tool_dispositions.md` @e8cd68632d, section (b).
Every row's reason was read.

## Ruling: 29 RATIFIED as out of the finish line; 3 amended

The 29 ratified rows are those not named below. Each one's reason is a class that is not a served research surface: a
DENY, a retired row, a frozen producer, account-grain or PII, a provenance or plumbing object, a superseded copy, or a row
outside Andrew's scope (platinum/advi).

| row | amendment | why |
|---|---|---|
| `opal_data_portal_v2_served_benchmark_returns` | **HELD AT ANDREW**, not "ruled out". In `scope_exclusions.json` its reason reads `held_at_andrew` and it reopens on his word. | The row is held at Andrew. A CTO ruling cannot exclude what he holds; it can only record the hold. |
| `opal_data_portal_v2_served_cma_assumptions` | **Moves to (a)** if the served object is the current edition AND a page reads it; otherwise it stays in (b) with that measurement as its reason. | "Frozen by design" describes an annual edition that is current. That is a served surface, not an exclusion. |
| `opal_data_mdpf_gold_ai_classified_securities` | **Stays in (b) only if** a merged or planned tool reads the DynamoDB etf-classifications table; name that tool in the reason. Otherwise the TABLE goes to (a). | A "CRO open item" is not a disposition. The surface this row points at must be covered somewhere. |

## Not changed

Section (a) (11 rows) is unchanged and stays owed by NFRA_OPLGTW (`2.0.0_SA_COO~O`). MI2 cuts the one LOCAL cell that lands
the result in `scope_exclusions.json`.

## Addendum ~02:5xZ -- three more rows (MI2 msg 34665, measured by COO~O msg 34657): RATIFIED out, each with a reopen condition

| row | reason recorded | reopens when |
|---|---|---|
| `dynamodb_dynamodb_opal_harvest_articles` | table empty since 2026-09-11; do-not-serve | the table holds items again (its producer is dell1's harvest since 2026-10-15) |
| `dynamodb_dynamodb_market_updates` | 183 trading days stale | the producer writes inside the trading-day frontier |
| `dynamodb_dynamodb_semantic_news_trending_daily` | 160 trading days stale | the producer writes inside the trading-day frontier |

The reasons are measurements, not classes: each exclusion carries its condition, so the row returns when the producer does.
The other eight (a) rows are at cross-adjudication XA-20261016T024917Z-cdcc (call sitez-...-035e).

## Addendum ~03:5xZ -- the last two rows (MI2 msg 34711): RATIFIED out with reopen conditions

| row | reason | reopens when |
|---|---|---|
| `opal_data_portal_v2_served_model_portfolios_views` | 93 trading days stale; NFRA_OPLGTW rules it out at build (PRD v3.13 item 3) | its producer writes inside the trading-day frontier |
| `dynamodb_dynamodb_opal_harvest_security_metrics` | routed to dell1 AMGT_HARVST (XA-20261016T024917Z-cdcc); not a site Z tool | the AMGT_HARVST tool ships, and its read_tool is linked then |

## Addendum ~06:4xZ -- ASSETS: the 91 rows no client_* tool reads (COO~MI msg 34780, @74e243fe48): REC RATIFIED for all 10 groups

- All 91 rows stay in the catalog and are ruled OUT of the 22:00Z line. Each carries the reason "no client tool is built to read
  this table", `gap_owner: NFRA_OPLGTW`, and a reopen condition naming the tool that would read it:
  - `client_get_lots`, `client_get_performance`, `client_get_insurance` or `client_get_profile`, as named in `client_tool_map.json`;
  - for the Schwab fact_* rows, the MX-c-23/MX-r-15 Schwab fact gap.
- As with every exclusion in this ruling, the `gap_owner` field does NOT meet the line. The row reads OUT, with its reason, until
  the named tool ships and the row's `read_tool` is linked.
- The 9 market-data rows (Pathfinder, TrueShares, Yahoo) go to the ETFS workstream's tool question. They are not client data
  and need no client tool.

## Addendum ~13:2xZ -- the 9 49Financial `*_silver_legacy` rows (CVO~Z msg 35011, row Z-C-S62, ADJUDICATION_v13 @c5ba2988f4): RULED OUT, with reopen conditions

The CVO is right. The ratified 91 listed only the three 49F insurance rows; the issuer's group-label reading does not reach these 9.
This addendum is the explicit word. The round-18 line therefore reads met for 280 of 280: 188 with a live tool, 83 ratified OUT at ~06:4xZ, and these 9.

| rows | store | reason | reopens when |
|---|---|---|---|
| allocations, assets, fees, prices, realized, transactions, transactions_enriched, unrealized (`49financial_*_silver_legacy`) | `opal-data-bd` | No client tool reads them yet. PRD v3.6 (Andrew-direct 10-14 ~18:3xZ) already sets the 49F BD adapter to read `opal-data-bd/silver/` through its own scoped role. That adapter is G2 order item 2, and it is unbuilt: the live `client_adapter_bd49f` reads the `opal-data-assets` copy, and OG-ap-24 accepted that as a named gap. | The v3.6 49F BD adapter ships with its role and never-widen halves. Its tools are linked as `read_tool` then. `assets` and `transactions_enriched` answer with their lag stated (v3.6 item 3). |
| single_file (`49financial_single_file_silver_legacy`) | `opal-data-assets` | A legacy one-file export that no client tool reads, and that no consumer has asked for. | A named consumer asks for it, or the 49F target-layout migration (v3.6, R19) supersedes it. |

- **Which store the client tools read** is not chosen here. It was set by Andrew's v3.6 word. Ruling these rows OUT records only that
  v3.6's adapter does not exist yet; it does not re-point anything.
- **`gap_owner: NFRA_OPLGTW`.** The v3.6 adapter is routed to `2.0.0_SA_COO~O` for round 38. If it is already cut, the reopen
  condition names that order.
- **The CVO's other carried items are endorsed for the issuer (`2.0.0_SA_COO~MI`) as round-19 enrichments:**
  - issuer items 1-6, among them `opal_discover` echoing `bucket`, vendor and firm, and a rollback catalog that passes `r13.AC3`;
  - clearing the gold book row's stale `open_items` (Z-C-S63).

# NFRA_MCPINDEX v0.7 -- index every need in Alyssa's workflows (MIDSTREAM brief)

**Author:** `4.0.0_SA_CRO~Z`. **For:** `1.0.0_SA_CTO~O`, `/endpoint --forward` at L2 for the v0.7 addendum.
**Asked by:** CTO~O msg 32332, on Andrew-direct ~03:2xZ
(`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261009_032xZ_MCPINDEX_INDEX_ALYSSA_WORKFLOWS.md` @5716c7a83d):
"all of this should be indexed, there is a lot of indexing work to be done".
**Measured:** 2026-10-09 03:37-03:58Z, as principal `opalbloomberg` through the live Opal gateway (`opal_discover` and
the vendor tools), plus a read of the repository catalog. Read-only; no grant, catalog or tool was changed.

---

## PART 0 -- How the blind constraint was honoured, and where it bent

**Honoured.** I read no NFRA_MCPINDEX task order and no `phase` or `blocking` field. `2.0.0_SA_COO~MI` sent me a map of
Alyssa's items to FWDs (msg 32336, its `ALYSSA_WORKFLOWS_INDEX_INPUT_MAP_20261009.md` @3ff7a2a654). **I did not open
it.** A map written by the round's own issuer is the branch, and reading it first is how a brief comes to ratify open work.

**Where it bent, three places:**
1. I wrote the NFRA_OPLGTW v2.1 brief @dae0456eb4, an input here. Its Schwab entries (E-1 to E-9 below) carry its frame.
2. I read the PRD's header history (v0.2 to v0.6), which names reviewers and rounds. Nothing below depends on it.
3. Every "served today" verdict is measured as `opalbloomberg`, not as Alyssa. Her grant may differ (Part VII).

**Is the endpoint unchanged?** Mostly yes. FWD-1, FWD-6 and FWD-10 already describe what "index everything" means.
What moves:
- The catalog must hold entries for needs it does not serve yet (O2).
- Two v0.6 clauses now conflict with Andrew's newer words: FWD-8's "no new vendor egress beyond Andrew's standing
  per-use word" (superseded by the law edit @4d77a9c3ea) and FWD-9's per-firm refusal (deferred by his ~01:5xZ words).

---

## PART I -- THE OUTCOME TERRITORY

The person is **Alyssa**, the one connected MCP user besides Andrew. Her two briefs list 8 browser workflows (C1-C8) and
6 Schwab workflows (W1-W6).

### O1 -- CANDIDATE THREAD: Alyssa asks for a model's performance and is routed to the served answer, not to Chrome

She asks Claude, in her own words, how a model did against its benchmark for a period. Discover names
`mdpf_get_model_benchmarks`, states the data's true as-of date, and the answer matches opalinvest.dev. Today the answer
is served (as of 2026-10-07), but her Chrome brief (C2) still lists opalinvest.dev as a browser workflow, and the
catalog states the wrong freshness (Part VI.2). One need, end to end: the question, the route, the true date, the answer.

### O2 -- Every need in her two briefs has an index entry, served or not

For each need, the index says what it is, its source, whether it is served today, and which tool answers it. If no
tool answers it yet, the entry says so and names the project that owns the gap. "Not catalogued" never stands for "not
known". The candidate list is Part IV.A (29 entries).

### O3 -- The index states a dataset's true freshness, not a remembered one

Freshness is read from the served artifact, not from the vintage recorded when the row was certified.

### O4 -- Alyssa's own words route correctly

"Account counts by partner", "cost basis", "statement", "stress test", "download the attachment", "S&P YTD": each reaches
its tool, or its gap entry, on the first try.

### O5 -- Vendor data is in the same index

YCharts (and Bloomberg, through its queue) answer from the index like Opal's own data. Today a market-return question
routes only to portal artifacts that are blocked or denied, never to the YCharts tools that answer.

### O6 -- The Schwab and Black Diamond datasets NFRA_OPLGTW adds appear in the index as they land

Account identity, lots, realized gains, flow-labelled transactions, the Tax SMA master and Black Diamond each get an
entry the day they are served. FWD-10's "one catalog entry plus a tool" applies.

### O7 -- File intake and write actions are indexed with their class

Saving a mail attachment or a SharePoint file, moving mail, sending a Teams message: each is an entry stating whether it
is a read or a write, and whether her grant allows it.

### O8 -- Each entry names the browser workflow it retires

An entry carries its C# or W# from her briefs, so the Chrome use that is left can be counted.

---

## PART II -- WHERE THE BOUNDARY SITS

| NFRA_MCPINDEX owns (CTO `1.0.0_SA_CTO~O`) | It relies on, and does not own |
|---|---|
| The catalog entries, their freshness reads, discover's routing, the gap entries (O2) | **NFRA_OPLGTW**: the Schwab and Black Diamond datasets, grants and lookup (v2.2, FWD-10 to FWD-19) |
| The vendor entries' place in the index (O5) | **The YCharts integration** (the `ycharts_*` tools; its credential refresh is "YALP_MDSRC.C6" in the tool's own text): the 403 and the symbol-key defect are its fixes |
| | **The write tools** (mail move, folder create, Teams send): the inventory `docs/briefs/opal-gateway-write-tools-inventory-20261008.md`; Andrew said "later" at 17:4xZ |
| | The portal publishers whose artifacts the catalog points at |

**Named outside:** C7 (bar directories for an internal BD app; public pages, not Opal data); C8 (local PDF rendering);
W3 prospect statements (not in Opal's masters until the assets transfer; only the intake tool is in scope, E-21).

---

## PART III -- THE QUALITATIVE BAR

- Alyssa asks discover before she opens Chrome, and discover either answers or tells her who owns the gap.
- A date the index states is one she could check against the served artifact and find equal.
- No need in her two briefs is missing from the index. A reviewer can check this by subtraction against the two
  documents.

---

## PART IV -- THE SUBSTRATE, measured

### IV.A -- Candidate index entries, one per need

Status: **SERVED** (a tool answers today), **PARTIAL**, **GAP** (no tool), **DENIED** (a tool exists; her or this
principal's class refuses it). "Owner" is the project that closes a gap.

| # | Need (her brief) | Source | Today | Tool | Owner of the gap |
|---|---|---|---|---|---|
| E-1 | Account number and title lookup, crosswalk from `account_ref` (W1, W2, W4) | Schwab `fact_acc` | GAP | `schwab_query` (`dim_account`, v2.0) | NFRA_OPLGTW FWD-10, FWD-15 |
| E-2 | Balances on any past date, 13 months or more (W1, W5) | Schwab `dim_balance` | PARTIAL: 30 days | `schwab_query` | NFRA_OPLGTW FWD-12 |
| E-3 | Positions on any past date (W1, W2) | Schwab `dim_position` | PARTIAL: 30 days | `schwab_query` | NFRA_OPLGTW FWD-12 |
| E-4 | Lot-level unrealized cost basis as of a date (W1, W2, W4) | Schwab `fact_ult`; BD `fact_unrealized` | GAP | `schwab_query` (new dataset) | NFRA_OPLGTW FWD-11, FWD-17 |
| E-5 | Realized gain/loss by date range, ST/LT (W1, W4) | Schwab `fact_rld`/`fact_rly`/`fact_rty`; BD `fact_realized` | GAP | `schwab_query` (new dataset) | NFRA_OPLGTW FWD-11, FWD-17 |
| E-6 | Transactions with a flow tag: deposit, withdrawal, journal, securities transfer, fee (W1, W4) | Schwab `dim_transaction`; BD `fact_transactions."External Flow"` | PARTIAL: no tag | `schwab_query` | NFRA_OPLGTW v2.0 item 3, v2.1 item 5 |
| E-7 | Tax SMA master 0840-3355 (W1) | Schwab SDD | GAP | `schwab_query` | NFRA_OPLGTW FWD-13, FWD-19 |
| E-8 | Black Diamond account data (W1) | BD Cottonwood silver | GAP (fees only today) | `blackdiamond_list_fees`; more to come | NFRA_OPLGTW FWD-18 |
| E-9 | Statement PDFs by account and period (W1) | not in Opal's estate as far as measured | GAP | none | unowned |
| E-10 | Corporate actions (W1, W4) | not measured | GAP | none | unowned |
| E-11 | Sector per security (W1 sector allocation) | FactSet RBICS file export today; none in silver | GAP | none | unowned |
| E-12 | Account performance / TWR (W1, P2) | Opal-computed from balances and flows | GAP | none | Andrew: "give her the right information", not returns |
| E-13 | Model performance by period vs benchmark (W6, C2) | portal `json/benchmarks/model_portfolio_benchmarks.json` | SERVED (as of 2026-10-07) | `mdpf_get_model_benchmarks` | this project: freshness statement (O3) |
| E-14 | Model daily return series (C2) | `json/benchmarks/model_portfolio_timeseries.json` | SERVED | `gateway_query_catalog` | -- |
| E-15 | AUA by partner and basis, with history (W5, C2) | `platinum/mdpf/{scope}/aggregate-aua-timeseries.json` | SERVED | `mdpf_get_aggregate_aua` | -- |
| E-16 | Account counts with month-end history (W5, C2) | the same aggregate series (count lineage arrays) | SERVED, but misrouted (Part VI.3) | `mdpf_get_aggregate_aua` | this project: routing (O4) |
| E-17 | AUM by model (W5) | `platinum/mdpf/{scope}/aum-metrics.json` | SERVED | `mdpf_get_aum_metrics` | -- |
| E-18 | Market overview and attribution pages (C2) | `market_overview` (no tool), `positioning_holdings` channels | PARTIAL | `tools/portal_lookup.py` (repo tool, not MCP) | this project |
| E-19 | Index or security returns and prices (C1, W3) | YCharts | PARTIAL: snapshot 200, time series 403 | `ycharts_snapshot_metrics`, `ycharts_time_series` | YCharts integration; this project for routing (O5) |
| E-20 | YCharts Overview / Comparison / Multi-Comp report for client holdings (C1) | YCharts site, single seat | GAP | none (`ycharts_run_report` proposed in C1) | unowned |
| E-21 | Save a mail attachment to a folder (C6, W3) | Graph | DENIED for her (`write_class_denied`, her brief) | `save_email_attachment_to_site` | write-class grant |
| E-22 | Download a SharePoint file that does not sync (C6) | Graph | PARTIAL: read in-channel only | `read_site_file`, `read_site_workbook`, `profile_site_file` | this project (catalog entry) |
| E-23 | Move or delete mail, create a folder (C4) | Graph | GAP (write) | none | write tools ("later") |
| E-24 | Send a Teams message as herself (C5) | Graph | exists in the gateway; her grant not measured | `send_chat_message` | write-class grant |
| E-25 | Bloomberg prices and reference data (C1 alternative) | Bloomberg queue | SERVED through its own path | `bloomberg_standing_read` channel | -- |
| E-26 | Microsoft Forms responses (YCharts request form) | Graph does not expose them (her brief) | GAP | none | unowned |
| E-27 | Orion compliance submissions (not browser-driven) | Orion | GAP | none | unowned |
| E-28 | Month-end AUM and account counts by master (custodian side) (W5 P2) | Schwab `dim_balance` aggregates | GAP | none | unowned |
| E-29 | Advisor account review from an emailed SAC link (W2) | E-1 to E-6 together | GAP until E-1 lands | `schwab_query` | NFRA_OPLGTW |

Count: 29 entries. 6 SERVED, 6 PARTIAL, 15 GAP, 1 DENIED, 1 UNMEASURED (E-24). Of the 15 gaps, 6 are NFRA_OPLGTW's,
1 is the deferred write tools' (E-23) and 8 have no owner today (E-9 to E-12, E-20, E-26 to E-28; E-12 also sits
outside Andrew's "the right information" bound).

### IV.B -- The catalog today

- `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` v0.4 (file dated 2026-10-01): 16 channels, 5 silver datasets
  (`blackdiamond_fees` and four Schwab `dim_*`), 5 portal datasets, 2 rows held at Andrew, 5 refused units. Live
  `opal_discover` answers from this v0.4.
- No catalog channel or dataset names a YCharts tool.
- The `sharepoint_documents` channel has no dataset, so discover reports "not catalogued" for a file-download question.

### IV.C -- Against PRD v0.6

| v0.6 clause | Now |
|---|---|
| FWD-1 ACCEPT "a question about a property that is not catalogued says so and names nothing" | O2 asks the catalog to hold GAP entries that name the owning project. That is a change to what "not catalogued" may say |
| FWD-8 "no new vendor egress beyond Andrew's standing per-use word" | Superseded by the CLAUDE.md law edit @4d77a9c3ea ("Egress is open on every channel, except Bloomberg") |
| FWD-9 "a phrasing that asks for another firm's or master's data is refused" | Andrew ~01:5xZ: per-user entitlement scoping waits for a second user (record @0035550443); NFRA_OPLGTW v2.2 already applies it |
| Scope: "Tax SMA tools (until D9's tax work lands)" | That work is landing in NFRA_OPLGTW v2.1 and v2.2; O6 brings it into the index |

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- NFRA_OPLGTW's datasets land (E-1 to E-8) before their entries can read SERVED.
- The YCharts time-series 403 and the snapshot's lost symbol key are fixed by their owner before E-19 reads SERVED.
- An owner is named for each unowned gap (E-9 to E-12, E-20, E-26 to E-28), or Andrew says the gap stays open.
- A grant read for Alyssa's principal, so the DENIED and "not measured" verdicts are hers, not `opalbloomberg`'s.

---

## PART VI -- STATUS, NOT OUTCOME-BEARING (measured 2026-10-09 03:37-03:58Z, principal `opalbloomberg`)

1. `mdpf_get_model_benchmarks` returned `data_as_of` 2026-10-07, five models, 10 periods.
2. `opal_discover("model performance by period versus benchmark")` states the same dataset's `latest_value` as
   2026-08-10 with claim `held` ("recorded at certification; not re-read"), next to `served_written_at` 2026-10-08
   (`measured`). The same `held` 2026-08-10 shows on `aum-metrics` and `aggregate-aua-timeseries`, and
   `account-distribution` reads 2026-08-11.
3. `opal_discover("account counts month-end history by partner")`: not catalogued. `opal_discover("AUA by partner Black
   Diamond Orion")`: routes to `aggregate-aua-timeseries`, whose own meaning names "account counts".
4. `opal_discover("Schwab tax lots cost basis realized gain loss")`, `("YCharts stress test report for client
   holdings")`, `("statement PDF for a Schwab account and period")`, `("download an email attachment or SharePoint file
   to a folder")`: all not catalogued.
5. `opal_discover("Schwab positions and balances for an account")`: 2 datasets, both servable, next tool `schwab_query`.
6. `opal_discover("S&P 500 year to date total return price history")`: 2 portal datasets, 0 servable (one
   BLOCKED-BY-ALLOWLIST, one DENY); no YCharts route.
7. `ycharts_freshness`: ok, HTTP 200. `ycharts_snapshot_metrics(["^SPX"], ["ytd_total_return"])`: HTTP 200, but the
   value is keyed `"None"`, not `"^SPX"`. `ycharts_time_series("SPY", price, 2026-10-01..10-08)`: HTTP 403, 0 points.
   Alyssa's brief (2026-10-08) recorded time series 403 and snapshot 404.
8. `identity_tool_allowlist.txt` (2026-10-07): 2 rows, both `opalbloomberg` (`opal_data_refresh_upload`, `_status`).
   NFRA_OPLGTW v2.2 item 5 adds five more for that principal.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **Alyssa's view.** Every verdict is `opalbloomberg`'s. Her grant can show more tools (the Schwab five) or fewer.
- **That E-9 statements and E-10 corporate actions are absent from every Opal source.** I checked the catalog and the
  Schwab silver table list from yesterday; I did not search every bucket or feed.
- **The cause of the stale `held` freshness** (Part VI.2): the catalog row's certification-time value, or a read that
  was never wired.
- **Her Chrome volumes** (sessions per site) are hers, as she wrote them. I did not re-count transcripts.
- **That 29 entries is the complete set.** It is one entry per need I could separate in her two briefs and my OPLGTW
  brief. A finer cut (one per field group) is the decomposition's call.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/mcpindex-alyssa-workflows-midstream-brief-20261009.md
  PROJECT           NFRA_MCPINDEX (D9); input to its v0.7 addendum
  EXISTING PRD      org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md (v0.6; FWD-1..10 at :109-203)
  SIBLING PROJECTS  NFRA_OPLGTW (v2.2: Schwab and Black Diamond datasets, grants); the YCharts integration;
                    write tools (docs/briefs/opal-gateway-write-tools-inventory-20261008.md)
  PRIOR ART         infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml v0.4; tools: opal_discover, opal_describe,
                    gateway_query_catalog, mdpf_get_{model_benchmarks,aggregate_aua,aum_metrics,account_distribution},
                    etfs_get_positioning, blackdiamond_list_fees, schwab_query, ycharts_*, SharePoint/mail/Teams tools
  INPUTS            SharePoint Shared/Product-Alyssa/PRD-004_gateway-data-feeds/assets/{Schwab Data Needs Brief.md,
                    External Chrome Workflows Brief.md}; docs/briefs/oplgtw-tax-workflow-midstream-brief-20261008.md
                    @dae0456eb4
  ANDREW RECORDS    ANDREW_DIRECT_20261009_032xZ_MCPINDEX_INDEX_ALYSSA_WORKFLOWS.md @5716c7a83d;
                    ANDREW_DIRECT_20261009_015xZ_OPAL_STAFF_MAY_READ_BLACK_DIAMOND_THROUGH_GATEWAY.md @0035550443;
                    CLAUDE.md law edit @4d77a9c3ea (egress)
  MEASURED AT       2026-10-09 03:37-03:58Z (every Part VI figure)
```

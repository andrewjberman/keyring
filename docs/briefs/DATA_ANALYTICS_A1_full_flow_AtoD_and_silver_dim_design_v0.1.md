# DATA_ANALYTICS A1 -- the COMPLETE A_00->Group-D data flow, parsed into the efficient SILVER DIM design (v0.1)

**Purpose (Andrew-direct 2026-06-25):** see the data flow ALL THE WAY from A_00 through Group D, then parse it to design the silver dim tables most efficiently. This is the synthesis that turns the layer-walk into the **Schwab-raw-native rebuild spec**: bronze = Schwab raw forms; **silver = these purpose-built dim/fact tables**; gold = joins + analytics, daily-incremental.

**Author:** 0.4.0_DS_ClientPlatform, 2026-06-25 (A1 walk -- io-graph complete through D). Source: comp-pipescript io across A_00..A_04, B_00..B_03, C_00..C_08, D_00..D_04 + the Schwab silver form schemas (acc/rps/uln/rld/trn/ult).

---

## 1. The complete A->D data-flow graph (every gold script, compacted)

**GROUP A -- dimensions/positions (the roots):**
- A_00 accounts_dimension <- silver account metadata -> ~ALL B/C/D
- A_01 advisor_assignments_history <- silver/transactions -> C_08, D_*
- A_02 fee_rate_history <- silver/fees -> D_00, C_08
- A_03 positions_cube <- silver positions (BD FIFO) -> B_00, B_01
- A_04 client_dimension <- A_00 + silver/transactions -> D_01/D_02/D_03/D_04

**GROUP B -- canonical holdings/lots/gains:**
- B_00 canonical_holdings <- A_03 + Schwab RPS + silver(unrealized/realized/prices/mapping) -> B_02, B_03, C_02, D_04
- B_01 holdings_lots <- silver/transactions (FIFO reconstruction) -> C_05, D_04
- B_02 canonical_lots <- B_00 + Schwab ULN/RLD + silver(unreal/real) -> B_03, C_05
- B_03 account_gains <- B_00(t,t-1) + B_02 + silver/transactions -> C_00, C_01, C_02

**GROUP C -- performance/nna/views (analytics):**
- C_00 canonical_performance <- B_03 + A_00 -> C_02
- C_01 canonical_nna <- B_03 + A_00 + C_02 + silver/transactions(nna_flows) -> C_01c, D_*
- C_01b role_aua_backfill <- C_03 + C_07.account_team -> D_01, D_02
- C_02 client_performance <- A_00 + B_03 + B_00 + C_00 + silver/allocations -> C_01,C_03,C_06,D_*
- C_03 account_performance <- A_00 + B_03 + C_02 -> C_01b,C_06,C_07,D_* (the served-AUA keyer)
- C_05 client_tax_liability <- A_00 + B_02.lots_unrealized + B_01.holdings_lots -> D_00, D_02
- C_06 client_mix_timeseries <- A_00 + C_03 + B_00 + C_02 + C_07 -> D_03, D_04
- C_07 advisor_attribution <- A_00 + C_03 -> account_team / rel_architect_lookup -> C_*, D_*
- C_08 advisor_fee_efficiency <- C_07 + A_01 + A_02 + C_01 + role_aua + fee_rate -> D_04

**GROUP D -- portal publishers (the served contract):**
- D_00 portal_aggregates -> header_metrics, clients_tab, aua-by-{architect,region,state,tax}
- D_00b portal_timeseries -> timeseries_chart (AUA/growth/NNA over time)
- D_00c portal_leaderboard -> employee_leaderboard
- D_00f advisor_nna_canonical -> advisor NNA
- D_01 partner_analytics -> partner/firm header metrics + role-AUA
- D_02 advisor_client_detail -> advisor->client drill-down
- D_03 composition_artifacts -> firm/advisor mix + composition
- D_04 client_portal_summary -> client-tab summary (widest: 27 inputs)

## 2. Parsing the flow: the LEAF INPUTS the whole chain actually consumes

Collapsing the graph to its roots (everything gold computes traces back to these raw/silver leaves):

| Leaf input | Consumed by (entry points) | Schwab raw form | Fields the chain needs |
|---|---|---|---|
| **account/client/advisor metadata** | A_00, A_04, C_07 | **ACC + account_xref** | account_id, relationship_id, household, taxpayer name, tax_status, architect/advisor/manager/team, state, account_type, strategy |
| **daily positions** | A_03, B_00 (-> all AUA/perf/mix) | **RPS** | account_id, ticker, cusip, units(quantity_settled), market_value, closing_price, date |
| **unrealized lots** | B_02, C_05 (tax) | **ULN** | account_id, ticker, cusip, current_quantity, cost_basis, cost_per_share, unrealized_gl, acquired_date, tax_code, long_short |
| **realized lots** | B_02, C_05 (tax) | **RLD** | account_id, ticker, closing_date, proceeds, cost_basis, gain_loss, days_held, holding_type(ST/LT) |
| **transactions/flows** | A_01, A_04, B_01, B_03, C_01 (NNA) | **TRN** | account_id, trade_date, tran_code, transaction(type), ticker, quantity, gross/net_amount |
| **fees** | A_02, C_08 | **NOT in Schwab RPS/ULN/RLD/TRN -- THE GAP** | fee_bps, fee_schedule, billable (separate feed: Schwab billing or a retained fee source) |
| prices | B_00, mix | embedded in RPS `closing_price` (or a small securities/price dim) | ticker -> price, date |
| allocations | C_02 | silver/allocations (BD-specific -- CHECK: needed, or BD-overfit absorbed by RPS/perf?) | (audit in v1.0) |

## 3. The EFFICIENT SILVER DIM design (the answer to "how to set up silver most efficiently")

Six purpose-built silver tables, each sourced from ONE Schwab raw form, carrying ONLY the fields the A->D chain consumes. Tight, dimensional, custodian-native:

1. **`silver/dim_account`** <- ACC + account_xref. Grain: account_id. Cols: relationship_id, household, taxpayer, **tax_status** (derive once here -- kills A_04's inferred-tax patch), architect/advisor/manager/team, state, account_type, strategy, first_seen/onboarding. (Replaces A_00 + A_04's dimension-building; one clean account+household dim.)
2. **`silver/fact_position`** <- RPS. Grain: (date, account_id, security). Cols: ticker, cusip, units, market_value, closing_price. (IS canonical holdings -- B_00 collapses to "read this"; A_03 FIFO positions_cube + the BD<->Schwab reconcile are RETIRED.)
3. **`silver/fact_lot_unrealized`** <- ULN. Grain: (date, account_id, security, lot). Cols: units, cost_basis, cost_per_share, unrealized_gl, acquired_date, tax_code, long_short. (IS canonical lots_unrealized -- B_01 FIFO reconstruction RETIRED; B_02 collapses to passthrough.)
4. **`silver/fact_lot_realized`** <- RLD. Grain: (closing_date, account_id, security, close_event). Cols: proceeds, cost_basis, gain_loss, days_held, holding_type(ST/LT). (IS canonical lots_realized.)
5. **`silver/fact_transaction`** <- TRN. Grain: (trade_date, account_id, txn). Cols: tran_code, transaction_type, ticker, quantity, gross/net_amount. (Feeds NNA-flow classification (C_01) + the Growth/NNA decomposition (B_03); also where the **aberration-excision** runs -- the curated-list-then-rules step, so the $4B-withdrawal class never reaches gold.)
6. **`silver/dim_fee`** <- the fee feed (THE GAP -- not custodian-raw). Grain: (account_id, effective_date). Cols: fee_bps, fee_schedule, billable. (Feeds A_02/C_08; sourcing TBD = Schwab billing vs retained feed.)
   (+ optional `silver/dim_security`: ticker/cusip -> name, asset_class, sector -- for mix/composition, from RPS/ULN security fields.)

## 4. The gold layer becomes JOINS + ANALYTICS on these (daily-incremental)

With the silver dims tight + custodian-native, gold is no longer ingest+reconcile -- it's pure analytics:
- **A (dims):** trivial / absorbed into the silver dims (dim_account IS the dimension; no separate FIFO/reconcile A-layer).
- **B (canonical):** holdings = fact_position (direct); lots = fact_lot_unrealized/realized (direct); **account_gains = the ONE real B-compute** = fact_position(t)-fact_position(t-1) Growth + fact_transaction NNA-flows -> Growth/NNA decomposition. Daily-incremental (one new day's positions+txns).
- **C (analytics):** performance (C_00/C_02/C_03), NNA (C_01), tax (C_05), mix (C_06), advisor attribution (C_07), fee efficiency (C_08) -- all firm-agnostic analytics on B, rebuilt clean, daily-incremental.
- **D (publishers):** joins + rollups -> the served portal artifacts (header_metrics, timeseries_chart, leaderboards, mix, client summary).

## 5. What this RETIRES (the patch-register payoff) + the one GAP
- **Retired:** A_03 BD FIFO positions_cube; B_00 BD<->Schwab reconcile (Schwab IS source); B_01 FIFO lot reconstruction (+ its bd_stale/is_ghost patches); A_04's 90-day flag + inferred-tax patch; the entity hardcodes. All dissolve when bronze is custodian-raw + aberration-excision runs in fact_transaction.
- **Kept:** the analytics (Growth/NNA decomposition, performance, NNA-flow classification, tax-lot gains, mix, attribution) + honest provenance labels (nna_clean-style).
- **The one GAP:** `dim_fee` -- fees are not in the custodian RPS/ULN/RLD/TRN. The rebuild must source a fee feed (Schwab billing or retained). Flagged as the single non-custodian dependency.

## 6. Next (-> v1.0 + the build)
- v1.0: field-level confirm by reading each D-publisher's EXACT emitted columns (drop any silver field the portal never reaches) + audit the silver/allocations dependency (C_02) for BD-overfit vs real-need.
- Then the BUILD through Group B (Andrew-directed): materialize silver dim_account + fact_position + fact_lot_* + fact_transaction, then gold B (holdings/lots/account_gains) on them, validated against the served 49F parity (Schwab RPS AUA $1.63B vs BD-gold header $1.83B -- the ~$200M delta to reconcile = the BD-vs-custodian gap + scope, a parity item for the build).

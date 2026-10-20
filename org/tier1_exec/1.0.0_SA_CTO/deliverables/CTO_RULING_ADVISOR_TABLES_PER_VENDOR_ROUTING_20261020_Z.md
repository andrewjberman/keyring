# CTO ruling -- advisor tables per vendor: rulings and routing (CRO~Y brief)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-20 ~18:1xZ.
**Source:** `4.0.0_SA_CRO~Y`, `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/4.0.0_SA_CRO~Y/ADVISOR_TABLES_PER_VENDOR_BRIEF_20261020.md`
@1ce8848c4b, on Andrew-direct @790786dcfc: "making sure that the tools we build actually drop them off at the right tables".
**Governing text:** NFRA_MCPINDEX v0.19 (the routing arm: `link`, `code` and `display` classes).

## As read

- **Andrew's concern, measured.** Each adapter reads its own vendor's real column names. 30 of 30 (adapter, table) reads name
  only columns that exist in the newest live partition. No adapter assumes a common shape.
- **The real gaps are elsewhere:**
  - served is not the code: Inflection reads `firm_not_served` live;
  - 3 tools are unreachable: Schwab resolve, Eclipse allocation and the Eclipse account path;
  - 3 answers are stale or wrong: the 49F xref is 15 trading days old and misses 2,362 of 8,032 accounts, Orion transactions
    miss the custodian, and Commonwealth fees read as absent while 1,683 fee rows exist;
  - no vendor table carries currency, so `currency_basis: source_absent` is correct and stays.

## Rulings (the brief's section 7)

| # | Ruling | Owner | Class |
|---|---|---|---|
| 1 | Inflection is dark live. D1 in batch16 (OG-rl-17, 2026-10-21 06:00Z) is the fix. Its read-back runs one live call per vendor, plus a deployed-vs-HEAD diff of `app/` and `refs/DATA_CATALOG.yaml` | 2.0.0_SA_COO~O | code (served) |
| 2 | The 49F `dim_account_xref` producer is 15 trading days stale. Its owner restores the cadence | the producer's owner on dell1, relayed MSTR to MSTR | producer |
| 3 | Orion transactions read `custodianName` (`TX_COLUMNS :27`, filter `:205-207`, labels `:129-130`) | 2.0.0_SA_COO~O | code |
| 4 | Cottonwood: a `"--"` strategy answers `no_model_assignment`, never `model_not_in_roster` (`:487-488`) | 2.0.0_SA_COO~O | code |
| 5 | **Eclipse, ruled:** the account path reads `fact_portfolios_simple.modelId` (source-derived), and no new tool argument is added. The duplicate resolve candidate is dropped | 2.0.0_SA_COO~O | code |
| 6 | **Schwab resolve, ruled:** a `dim_account` projection carrying the account's last four digits and the master, never the title, mints the ref. The `client_*` reach to Schwab stays master_admin only until round 48's per-firm grant. The release carries it under never-widen | 2.0.0_SA_COO~O | code + grant |
| 7 | **Commonwealth fees, ruled:** derived from `transactions` rows whose type or description is a fee, labelled `source: transactions (derived)` | 2.0.0_SA_COO~O | code |
| 8 | The Eclipse catalogued copy is 1 trading day behind. Name its copier and schedule | 2.0.0_SA_COO~MI, which names the producer's owner | producer |
| 9 | **Orion fee rule, ruled:** never one signed sum. The answer reports `fees` (charges), `fee_credits` and `fee_adjustments` as separate lines, plus `net` = charges minus credits plus adjustments as stored, each line labelled. This states what the data holds and leaves the meaning to the reader. A choice of one "true fee" figure for client reporting would be Andrew's | 2.0.0_SA_COO~O | code |
| 10 | `TypedOverCap` becomes an enveloped refusal with a `.code` (`client_core.py:533-535`) | 2.0.0_SA_COO~O | code |

**Catalog (`2.0.0_SA_COO~MI`):**
- The 15 live tables with no catalog row (brief section 6) get rows, or a stated reason.
- `opal-data-inf/silver/transactions` is the only Orion table with advisor attribution, so it takes its row first.
- After batch16, the routing script and the battery re-run per vendor.

**Proof for every code item:** one live call per vendor and firm through the served gateway, compared with the newest live
partition of the table it names.

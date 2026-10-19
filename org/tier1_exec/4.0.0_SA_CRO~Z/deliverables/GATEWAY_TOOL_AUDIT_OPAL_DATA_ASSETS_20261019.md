# Gateway tool-call audit, part 1: opal-data-assets (and why Schwab tools show Black Diamond indexes)

**Author:** 4.0.0_SA_CRO~Z, 2026-10-19 ~17:3xZ (1:3x PM ET). **Order:** Andrew-direct ~16:2xZ, record
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261019_162xZ_GATEWAY_PAGE_SCHWAB_TOOLS_SHOW_BLACK_DIAMOND_INDEXES_DEEP_AUDIT_EVERY_TOOL_CALL.md`
@634d368d98.

**Instrument:**
- live calls through the served gateway (opalgateway MCP, signed in as Andrew@, master_admin), read 16:3xZ-17:2xZ;
- direct read-only S3 reads of the same objects, to check the answers;
- source at HEAD.

The served release's bytes equal HEAD for every audited file (`client_core.py`, the seven adapters,
`admin_gateway_breakdown.py`, `refs/DATA_CATALOG.yaml`). `git diff` against both live release candidates, 6b1a9bd292
and 6d1b5dcb64, is empty. Release batch14 was mid-deploy during the read.

## 1. Answer first

**Why Black Diamond shows on Schwab tools.** There are three causes, and only one of them is real data.

1. **The page does not filter indexes by segment (display defect).** Each tool row's "Indexes" cell is every catalog
   row naming that tool as its `read_tool`, for every vendor. So under the heading "Schwab / 49 Financial",
   `client_get_holdings` lists its 13 indexes: 6 Schwab, 2 Black Diamond, 2 Commonwealth, 1 Orion, 2 SmartX.
   - Source: `admin_gateway_breakdown.py` builds `entry["indexes"]` per tool, and `GatewayView.tsx` prints `tool.indexes`
     unchanged in every segment table.
   - The channel's "Indexes" paragraph is the union across all tools.
2. **Black Diamond data sits in the opal-data-assets section although it lives in another bucket.** Four indexes under
   opal-data-assets are `opal-data-bd` objects: the Black Diamond live unrealized, transactions, allocations and fees
   tables. The `client_*` tools read them, and the catalog places those tools in the opal-data-assets channel.
3. **A real Schwab-Black Diamond link exists, and the page never explains it.**
   - Schwab is the custodian. The gateway's own Schwab grant labels master **08335338 "BlackDiamond"** and
     08242234 "SmartX": Schwab master accounts whose clients are reported through those platforms.
   - The 49F crosswalk `dim_account_xref` maps Black Diamond account ids to Schwab account ids.
   - So some Black Diamond-next-to-Schwab is legitimate, but nothing on the page says so.

**Do the tools work?** Of the 32 rows in section 2:
- 15 PASS (3 of them with a caveat: slow, scope-narrowed, or one stale input);
- 1 works with a mislabelled answer;
- **9 FAIL**;
- 2 are unreachable;
- 4 refuse by design;
- 1 was not run.

The 9 FAILs come from two defects, D1 and D2. D3 is the mislabelled answer, and it also hides one of D1's refusals:

- **D1 -- Inflection (Orion, Eclipse) and Commonwealth answer nothing, on every tool.**
  - The core's firm-to-segment table (`client_core._names()["fence_kind"]`) holds only `schwab` and `blackdiamond`.
  - `Ctx.firm_segments()` returns `[]` for orion, eclipse and commonwealth, and their adapters then refuse
    `firm_not_served` before any read.
  - Measured live: `client_resolve_account(firm="inflection")` returns `firm_not_served`.
  - Reproduced on HEAD: all three adapters refuse `firm_not_served`.
  - The table never carried them, from the client core's first commit (5c8c1554e5, 10-15) through OG-cl-7 (0921b7605b),
    so these vendors have never answered on the served gateway.
  - S3 holds current data for both: Orion positions to 10-19, Eclipse models to 10-17.
- **D2 -- Cottonwood Black Diamond transactions and fees always come back empty.**
  - `client_adapter_bdcottonwood._date()` parses ISO only (`fromisoformat`), but the source writes `MM/DD/YYYY`
    ("10/12/2026").
  - Every row is dropped. The live answer shows `partition_dates: null` over 9,263 rows.
  - The S3 file holds 2 transactions for the test account; the tool returned 0.
- **D3 -- Account lookup merges vendors under one vendor's metadata.**
  - `client_resolve_account` keeps the FIRST answering adapter's envelope (source_keys, denominator, absent_reason)
    and drops every other adapter's refusal.
  - Measured live: a 49F last-4 that only SmartX holds answers with 1 SmartX candidate, while saying
    `absent_reason: no_candidate_for_last4` and citing only the Black Diamond crosswalk as its source.
  - The same merge is what hides D1's Commonwealth refusal.

**Not reachable as the page implies:**
- **Schwab via the `client_*` tools.** `client_resolve_account` refuses Schwab by design (`no_resolve_source`), and no
  code calls `mint_account_ref`, so no Schwab `account_ref` can ever exist. The four `client_*` tools the page lists
  under "Schwab / 49 Financial" can never be reached for Schwab.
- **Where Schwab data does work.** The `schwab_*` tools.

**Correct but worth knowing:**
- **The Schwab answers leave accounts out.** The grant enumerates 7,559 accounts for 08335338. On 10-16 S3 holds
  7,690, so `schwab_query` aggregates 7,540 accounts / $1,826,045,809.18 against S3's 7,690 / $1,843,318,694.53. That
  is 150 accounts and about $17.3M outside the grant's frozen list, including for the owner. The answer says
  "authorized matched rows"; it does not say how many it left out.
- **`schwab_get_access` took over 120 s.**

## 2. The matrix (every tool by every segment the page lists, live)

Verdicts: PASS = a correct non-empty answer, checked against S3 where marked. EMPTY-CORRECT / REFUSED-BY-DESIGN = the
source or the contract confirms it. FAIL = the defect named. UNREACHABLE = no input can reach it.

| Tool | Segment (vendor / firm) | Page lists it? | Live verdict | Routed to (source_keys) | Note |
|---|---|---|---|---|---|
| client_resolve_account | blackdiamond / 49financial | yes | PASS | `blackdiamond/49f/silver/dim_account_xref/2026-09-28` | crosswalk 14 trading days old |
| client_resolve_account | blackdiamond / cottonwood | **no** | PASS | `blackdiamond/cottonwood/silver/fact_allocations/date=2026-10-16/` | works; the catalog's `serves` omits it |
| client_resolve_account | smartx / 49financial | yes | PASS, mislabelled | the BD crosswalk key (wrong) | D3 |
| client_resolve_account | commonwealth / cottonwood | yes | FAIL | none | D1, silently dropped by D3 |
| client_resolve_account | schwab / 49financial | yes | REFUSED-BY-DESIGN | none | `no_resolve_source` |
| client_resolve_account | orion, eclipse / inflection | no | FAIL | none | D1 (`firm_not_served`) |
| client_get_holdings | blackdiamond / 49financial | yes | PASS | `blackdiamond/49f-live/silver/unrealized/2026-10-16` (opal-data-bd) | tax lots, not positions |
| client_get_holdings | blackdiamond / cottonwood | yes | PASS | `.../cottonwood/silver/fact_holdings/` + `fact_allocations/` 10-16 | |
| client_get_holdings | smartx / 49financial | yes | PASS | 4 SmartX tables, 10-19 | 33 positions, $74,194.79 |
| client_get_holdings | commonwealth / cottonwood | yes | FAIL | none | D1 |
| client_get_holdings | orion / inflection | yes | FAIL | none | D1 |
| client_get_holdings | schwab / 49financial | yes | UNREACHABLE | none | no Schwab ref is ever minted |
| client_get_transactions | blackdiamond / 49financial | yes | PASS | `49f-live/silver/transactions/` 30 partitions | pages at 30 partitions |
| client_get_transactions | blackdiamond / cottonwood | yes | **FAIL** | `fact_transactions/date=2026-10-19/` | D2: 0 returned, 2 in S3 |
| client_get_transactions | smartx / 49financial | no | REFUSED-BY-DESIGN | none | `vendor_no_transactions` |
| client_get_transactions | commonwealth / cottonwood | yes | FAIL | none | D1 |
| client_get_transactions | orion / inflection | yes | FAIL | none | D1 |
| client_get_transactions | schwab / 49financial | yes | UNREACHABLE | none | no Schwab ref |
| client_get_allocation | blackdiamond / 49financial | yes | PASS, stale part | `49f-live/silver/allocations/2026-10-16` + `49f/silver/fact_bd_allocation/2026-08-18` | the market-value profile is 42 trading days old (one partition, 08-18) |
| client_get_allocation | blackdiamond / cottonwood | yes | PASS | allocations 10-16 + model assignment/roster 10-19 | |
| client_get_allocation | smartx / 49financial, multi | yes | PASS | roster, account map, model holdings, positions 10-19 | |
| client_get_allocation | eclipse / inflection | yes | FAIL | none | D1 |
| client_get_allocation | commonwealth / cottonwood | no | REFUSED-BY-DESIGN | none | closed delivery, no allocation table |
| client_get_fees | blackdiamond / 49financial | yes | PASS (verified) | `49f-live/silver/fees/` 26 partitions | $207.18 account fee on 10-13 equals S3 transaction 746038407; $0 rows are skipped by design |
| client_get_fees | blackdiamond / cottonwood | **no** | **FAIL** | `fact_transactions/date=2026-10-19/` | D2 |
| client_get_fees | schwab, smartx, commonwealth, eclipse | no | REFUSED-BY-DESIGN | none | `no_fee_source` |
| schwab_get_access | schwab | yes | PASS, slow | grant store | over 120 s |
| schwab_list_files | schwab / 08335338 | yes | PASS | 3 files 10-14..10-16 | |
| schwab_describe_dataset | schwab / 08335338 | yes | PASS | producer schema @0fc7c71160 | |
| schwab_query | schwab / 08335338 | yes | PASS, scope-narrowed | 1 source ref, 10-16 | 7,540 of 7,690 accounts (grant list frozen) |
| schwab_prepare_download | schwab | yes | NOT RUN | | writes a download file; left for the battery's no-send path |
| blackdiamond_list_fees | blackdiamond / 49financial (opal-data-bd) | yes | PASS (verified) | `opal-data-bd/silver/fees` 10-13 | same $207.18 row as client_get_fees |

**Denominator:** 32 rows:
- 15 PASS: 12 plain, plus "PASS, slow", "PASS, scope-narrowed" and "PASS, stale part";
- 1 PASS-mislabelled;
- 9 FAIL;
- 2 UNREACHABLE;
- 4 REFUSED-BY-DESIGN;
- 1 NOT RUN.

Two rows each cover more than one vendor: the Orion/Eclipse resolve row, and the four-vendor no-fee-source row.

## 3. Storage (every index behind the five client_* tools)

All 43 distinct (bucket, prefix) locations exist and hold objects. Read once each 2026-10-19 ~16:5xZ;
denominator 43. Trading frontier T-1 = Friday 2026-10-16.

| Freshness | Indexes |
|---|---|
| current (10-16 or later) | 36 |
| 1 day behind | Black Diamond live fees (newest 10-15) |
| stale | 49F `dim_account_xref` and `dim_advisor_fee_role` (newest 09-28, 14 trading days); 49F `fact_bd_allocation` (one partition, 08-18) |
| closed delivery, by design | 4 Commonwealth tables (06-23, one delivery) |

- **Unused index:** the catalog indexes a third Schwab master, 08403355, whose S3 data is current. The Schwab adapter
  refuses it (`master_not_registered`) and the grant does not name it, so it is indexed but never served.
- **History depth:** Cottonwood transactions hold one rolling file (`date=2026-10-19`, trade dates 10/05 to 10/16).
  Even after D2 is fixed, a 13-month window cannot be served from it.

## 4. What fixes what (owners by lane; none of this is fixed here)

| # | Defect | Fix | Owner |
|---|---|---|---|
| D1 | orion / eclipse / commonwealth have no fence kind | add their `fence_kind` rows (Inflection's Orion and Eclipse segments, Cottonwood's Commonwealth segment) through the registry lookup `_names()` reads, then one live call per vendor | NFRA_OPLGTW (`2.0.0_SA_COO~O`), gateway code |
| D2 | Cottonwood dates are MM/DD/YYYY | `_date()` accepts the source's `MM/DD/YYYY` (or the silver producer writes ISO) | NFRA_OPLGTW |
| D3 | resolve merges under the first envelope and hides refusals | per-vendor source_keys/denominator, and the refused vendors listed with their codes | NFRA_OPLGTW |
| P1 | page indexes not filtered by segment | in a segment table, list only the indexes whose (vendor, firm) is that segment's | NFRA_MCPORTAL (`2.0.0_SA_COO~MP`) + the breakdown in NFRA_OPLGTW |
| P2 | catalog `serves` disagrees with the adapters | `serves` generated from what each adapter answers (BD Cottonwood added to resolve and fees; Orion added to resolve; Schwab marked unreachable on `client_*`) | NFRA_MCPINDEX (`2.0.0_SA_COO~MI`) |
| P3 | Schwab grant account list is frozen | Andrew's call: a grant over a master's current accounts, or a stated "N not in grant" in each answer | Andrew, then NFRA_OPLGTW |
| S1 | stale 49F crosswalk and fee roles (09-28) and allocation profile (08-18) | producer owners re-run or retire | the 49F Black Diamond producer's owner |

## 5. Bounds

- **Account coverage:** one test account per (vendor, firm), chosen from S3 so its rows exist. A defect that bites only
  some accounts would not show here.
- **Not exercised:** the as_of, platform and paging arguments.
- **What is kept where:** no account number, account id or client name is in this file. The test inputs and raw reads
  stay in the session scratchpad.
- **Writes:** nothing was written anywhere but this file and the record.
- **Next:** the remaining buckets, in the order Andrew's words give (harvest, etfs, portal/mdpf, news, opal-data-bd), and
  then NFRA_MCPINDEX FWD-24's re-runnable battery. FWD-24 is the standing form of this audit; this file is its first
  hand-run.

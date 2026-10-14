# G2d -- opal-data-assets: the Schwab silver layer and every other prefix (census part for 4.0.0_SA_CRO~Z)

- **Author:** census subagent G2d of 4.0.0_SA_CRO~Z, 2026-10-14 12:50Z-13:50Z. Read-only: S3 list/get, Parquet footers, projected column reads, Lambda/EventBridge/Scheduler describe. No write, no invoke, no vendor call.
- **Binds:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_DIRECTIVE_20261014_GATEWAY_DATA_CONTRACTS_CENSUS.md` sections 2-4 and `parts/_SUBAGENT_BRIEF.md`. Workspace HEAD at read: `bc91e712ad`.
- **Scope:** (A) `schwab/<master>/silver/` and (B) every top-level prefix of `opal-data-assets` except `blackdiamond/`, `orion/`, `eclipse/`, `smartx/` (sibling parts).
- **Trading calendar:** `lib/trading_calendar.py` (NYSE hardcoded fallback 2010-2027). T-1 frontier = 2026-10-13.

## 0. Answer in eight lines

1. The bucket holds **19 top-level prefixes, 1,049,812 objects, 145.74 GB** (1,064 list pages, every key grouped). Six of the 15 in-scope prefixes hold a silver layer: schwab, commonwealth, gateway, pathfinder, trueshares, yahoo (plus one plumbing JSON under bloomberg).
2. **The Schwab silver layer is THREE masters, not one, and 57 tables, not 7.** 08242234 (19 tables), 08335338 (20), 08403355 (18): 15, 16 and 14 vendor-complete `fact_*` tables plus 4 gateway `dim_*` projections per master. 28,807 Parquet parts in scope read, 0 read errors, **every table 1 schema variant**.
3. **The seven tables of the `49-schwab-conv` skill (ACC, RPS, TRN, TRN_NNA, ULN, ULT, RLD) are a DEAD legacy channel.** They live in `opal-data-bd/schwab/silver/`, not this bucket, and all seven stop at **2026-07-23 (57 trading days behind)**. The live silver is the monolith here, fresh to **2026-10-13 (0 behind)**. TRN_NNA has no monolith counterpart (ruled gold-tier, `schwab_conversion.py` docstring).
4. **Last-4 is NOT a unique account key on Schwab.** On 08242234, 1,798 last-4 values collide, covering 4,056 of 7,555 accounts (54%). On 08335338 it is 1,842 values over 4,156 of 7,646. On 08403355, 0 of 30. Every last-4 tool must return a candidate list.
5. **The masters overlap.** 7,534 of 08242234's 7,555 account ids also sit under 08335338, and all 30 of 08403355's do. All three are firm 49financial. Never sum across masters.
6. **Gateway coverage:** `schwab_query` and its four siblings serve only the 4 `dim_*` tables of 2 masters. 08403355 is admitted by the gateway IAM, but it is missing from the contract masters and from `infra/logic/registry/scopes.json`. Lots, realized gains, tax-lot detail and the account directory have no tool.
7. **Other client silver:** Commonwealth (cottonwood) is a closed 12-table historical delivery (2013-04..2026-06-23, 1,533 accounts, last-4 collides on 731). The Tax SMA workbook silver is MULTI-FIRM (RIA cell). Neither has a catalog row or a tool.
8. **Proposed: 14 tools** (section 3.4), every client tool taking firm + account_last4 + platform + as_of. Four extend the existing Schwab typed query; four more are new Schwab tools over new non-PII projections.

## 1. Method (each read, its instrument, its denominator)

| read | instrument | denominator |
|---|---|---|
| top level | `list_objects_v2 Delimiter=/` (boto3 paginator) | 1 page, 19 common prefixes, 0 root objects |
| every key | `list_objects_v2` paginated per prefix, 10 threads | 1,064 pages, 1,049,812 of 1,049,812 keys, grouped to datasets |
| every in-scope silver Parquet footer | `pyarrow.parquet.read_metadata` over `pyarrow.fs.S3FileSystem`, 48 threads | 28,807 of 28,807 parts (schwab, commonwealth, gateway, pathfinder, trueshares, yahoo), 0 errors, 79 tables |
| nullability | one footer per table (newest part) | 79 of 79 tables |
| Schwab fork keys | full projected read of `fact_acc date=2026-10-13` (account_id, master_account_name, mstracct_number, platform code, money manager, custodian, status) | 3 of 3 masters; 7,555 + 7,646 + 30 rows |
| Schwab grain checks | projected reads of 08335338 `date=2026-10-13`: dim_position, dim_balance, dim_asset, dim_transaction, fact_uln, fact_rld | 6 partitions (a sample of one date per table, not a history census) |
| Commonwealth fork keys | projected account columns of every transactions part (14), positions, account_day_value, performance (3), month_grades, crosswalk, account_links | every part of those 7 tables |
| Tax SMA workbook | full read of both parts of `date=2026-10-13` (cell structs) | 2 of 21 parts (newest partition) |
| ETF fund silver | projected `Account`/`date_std` of the newest holdings part per fund; full read of the newest PFDE nav and DIVZ net-assets part | 6 parts |
| Yahoo prices | projected `date` of every `prices.parquet`; full read of `index/index.parquet` | 483 of 483 cusips |
| legacy Schwab silver (cross-reference) | `list_objects_v2 Delimiter=/` on `opal-data-bd/schwab/silver/<t>/` | 7 of 7 tables |
| producers | `lambda get-function-configuration` x2; `events describe-rule` + `list-targets-by-rule` x2; `s3api get-bucket-notification-configuration`; Lambda `list_functions`; Scheduler `list_schedules` | 2 functions; 2 rules; 12 notification rules; 237 functions; 35 schedules |
| trading days | `lib/trading_calendar.py` `prev_trading_day`, `trading_days_behind` | T-1 = 2026-10-13 |

Scratch (key census TSVs, footer JSONL, scripts) stays in `C:\Users\OPALBL~1\AppData\Local\Temp\claude\census_G2d\`, uncommitted. No client name, account number, SSN/TIN, address, email or phone was printed into this file. Firm names (the advisor firms) are printed. Last-4 figures are counts only.

## 2. Prefix census and classification

### 2.1 The 19 top-level prefixes (listed 2026-10-14 12:52Z-12:57Z)

| prefix | objects | bytes | newest LastModified (UTC) | pages | class | why (one line) |
|---|---|---|---|---|---|---|
| `_probe/` | 22 | 1,345 | 2026-07-15T18:48:50Z | 1 | plumbing | 22 grammar-probe objects of 35 bytes (2026-07-14/15), the naming-gate landing tests |
| `blackdiamond/` | 31,303 | 17,989,245,212 | 2026-10-14T12:45:54Z | 32 | sibling part | covered by the BD part of G2 |
| `bloomberg/` | 7 | 31,092 | 2026-10-14T12:30:03Z | 1 | plumbing | bronze demand_ledger (6 daily JSONL) + 1 silver request_state JSON of the Bloomberg queue; no client data |
| `code/` | 13 | 86,921 | 2026-10-09T02:49:53Z | 1 | plumbing | deploy scripts for the canonical-schwab-si2 EC2 puller and the consolidation-gold runner |
| `commonwealth/` | 11,155 | 5,085,708,907 | 2026-10-09T12:41:03Z | 12 | HAS SILVER (client) | cottonwood legacy custodian delivery: 3 bronze tables, 12 silver tables (contracted below) |
| `config/` | 1 | 13,516 | 2026-09-18T15:19:14Z | 1 | plumbing | 1 object, config/mdpf/route_bindings.yaml |
| `eclipse/` | 3,801 | 295,959,163 | 2026-10-13T16:00:08Z | 4 | sibling part | covered by the Orion+Eclipse part of G2 |
| `gateway/` | 44 | 454,644 | 2026-10-13T13:58:14Z | 1 | HAS SILVER (client, multi-firm) | Tax SMA workbook: bronze snapshots + typed silver (contracted below); a 49financial bronze projection |
| `gold/` | 524 | 4,946,931 | 2026-10-13T13:31:36Z | 1 | client data, gold only, no silver | gold/mdpf_revamp per firm JSON (account_distribution, aggregate AUA) and QA manifests: MDPF gold, G3/G4 territory |
| `json/` | 4 | 374,256 | 2026-07-23T19:30:01Z | 1 | legacy served artifact | json/portfolios/* 4 objects frozen 2026-07-23; DATA_CATALOG.yaml:695 disambiguation L-1 names it the legacy tree |
| `mdpf/` | 1,050 | 8,771,937 | 2026-10-12T12:52:52Z | 2 | client/model data, bronze only, no silver | mdpf/inflection/bronze/orion_model_composition: 1,050 objects, newest 2026-10-12 |
| `orion/` | 10,512 | 22,374,332,722 | 2026-10-13T16:00:47Z | 11 | sibling part | covered by the Orion+Eclipse part of G2 |
| `pathfinder/` | 920 | 7,020,424 | 2026-10-13T23:30:16Z | 1 | HAS SILVER (fund, not client) | PFDE/PFOE fact_dailynav + fact_holdings from the filepoint bronze (contracted below) |
| `portal/` | 795 | 51,813,258 | 2026-10-13T13:51:35Z | 1 | client data, gold only, no silver | portal/gold/mdpf per firm (account-distribution, aum-metrics, AUA timeseries, category views) + portal/gold/etfs/positioning: G3/G4 territory |
| `schwab/` | 62,984 | 93,526,889,695 | 2026-10-14T12:18:25Z | 63 | HAS SILVER (client) | 3 masters: bronze (17-18 feeds), silver (57 tables), meta, _ops; 08335338 also gold/ (contracted below) |
| `smartx/` | 923,651 | 6,286,712,231 | 2026-10-14T13:03:14Z | 924 | sibling part | covered by the SmartX part of G2 |
| `sprint/` | 4 | 22,537,976 | 2026-10-06T20:19:14Z | 1 | plumbing | device_census bronze JSON (4 objects, 22.5 MB) |
| `trueshares/` | 1,082 | 68,154,269 | 2026-10-13T23:30:16Z | 2 | HAS SILVER (fund, not client) | DIVZ/IDVZ fact_holdings + fact_netassets_page (contracted below) |
| `yahoo/` | 1,940 | 16,429,172 | 2026-10-14T03:50:27Z | 2 | HAS SILVER (reference) | per-cusip price store of MDPF_DEMQUE + its demand ledger (contracted below) |
| **total** | **1,049,812** | **145,739,483,671** | | **1,064** | | |

`advi/` and `irpt/` are ABSENT at the top level, measured (0 of 19 prefixes). This matters because `org/standards/ADVI_BILLING_SMARTX_FEE_STATEMENT_CONTRACT.json` gives `s3://opal-data-assets/advi/49financial/silver/smartx_fee_statement/quarter=2026Q3/data.parquet` as its silver address example, and `lib/opal_naming.address('advi','49financial','silver',...)` still resolves to this bucket. That silver has not landed. The ADVI and IRPT gold addresses resolve to the firm buckets (`opal-data-49financial`, `opal-data-cottonwood`) and are out of this bucket.

### 2.2 Schwab (`schwab/`, 62,984 objects, 93.53 GB)

| master | firm (registry) | master_account_name (measured) | contract label | accounts (fact_acc 2026-10-13) | bronze feeds | silver tables | meta/complete partitions |
|---|---|---|---|---|---|---|---|
| 08242234 | 49financial | 49 WEALTH MANAGEMENT LLC | SmartX | 7,555 | 17 (acc rld rlu rlw rly rps rtu rty sec tcf tcfx tnn trn uln ult upn upt) | 19 | 277 (2025-09-08..2026-10-13) |
| 08335338 | 49financial | 49 FINANCIAL | BlackDiamond | 7,646 | 18 (no rlw; + fam slm) | 20 | 277 (2025-09-08..2026-10-13) |
| 08403355 | **absent** (not in scopes.json) | 49 FINANCIAL | **absent** | 30 | 16 (no rlw fam slm) | 18 | 761 (2023-10-03..2026-10-13) |

Bronze `tcf`, `tcfx` and `tnn` have no silver by ruling. They are reader-variance holes, skipped as `skipped-hole` (data dictionary 2c). `schwab/08335338/gold/` holds `canonical/` (4,208 objects, newest partition 2026-08-10, 44 trading days behind) and `dimensions/` (8 objects, 2026-07-15). That gold is frozen and out of the silver scope.

Silver tables (rows = newest partition; each partition is one `data.parquet`):

| table | 08242234 newest / behind / rows | 08335338 newest / behind / rows | 08403355 newest / behind / rows | cols | cadence |
|---|---|---|---|---|---|
| `dim_asset` | 2026-10-13 / 0 / 2,197 | 2026-10-13 / 0 / 2,540 | 2026-10-13 / 0 / 669 | 29 | daily |
| `dim_balance` | 2026-10-13 / 0 / 7,555 | 2026-10-13 / 0 / 7,646 | 2026-10-13 / 0 / 30 | 39 | daily |
| `dim_position` | 2026-10-13 / 0 / 106,194 | 2026-10-13 / 0 / 110,454 | 2026-10-13 / 0 / 3,884 | 30 | daily |
| `dim_transaction` | 2026-10-13 / 0 / 11,827 | 2026-10-13 / 0 / 11,906 | 2026-10-13 / 0 / 36 | 44 | daily |
| `fact_acc` | 2026-10-13 / 0 / 7,555 | 2026-10-13 / 0 / 7,646 | 2026-10-13 / 0 / 30 | 95 | daily |
| `fact_fam` | -- | 2026-08-10 / 45 / 7,202 | -- | 11 | daily |
| `fact_rld` | 2026-10-13 / 0 / 6,018 | 2026-10-13 / 0 / 6,018 | 2026-10-13 / 0 / 0 | 86 | daily |
| `fact_rlu` | 2026-09-04 / 26 / 282,721 | 2026-09-04 / 26 / 284,476 | 2026-09-04 / 26 / 9 | 87 | quarterly |
| `fact_rlw` | 2026-10-09 / 2 / 369,371 | -- | -- | 80 | weekly |
| `fact_rly` | 2026-09-30 / 9 / 324,125 | 2026-09-30 / 9 / 327,621 | 2026-09-30 / 9 / 1,892 | 87 | month-end |
| `fact_rps` | 2026-10-13 / 0 / 106,194 | 2026-10-13 / 0 / 110,454 | 2026-10-13 / 0 / 3,884 | 63 | daily |
| `fact_rps_s2` | 2026-10-13 / 0 / 7,555 | 2026-10-13 / 0 / 7,646 | 2026-10-13 / 0 / 30 | 39 | daily |
| `fact_rtu` | 2026-09-04 / 26 / 111,948 | 2026-09-04 / 26 / 112,496 | 2026-09-04 / 26 / 9 | 75 | quarterly |
| `fact_rty` | 2026-09-30 / 9 / 113,595 | 2026-09-30 / 9 / 115,936 | 2026-09-30 / 9 / 1,818 | 75 | month-end |
| `fact_sec` | 2026-10-13 / 0 / 2,197 | 2026-10-13 / 0 / 2,540 | 2026-10-13 / 0 / 669 | 74 | daily |
| `fact_slm` | -- | 2026-10-13 / 0 / 7,593 | -- | 11 | daily |
| `fact_trn` | 2026-10-13 / 0 / 11,827 | 2026-10-13 / 0 / 11,906 | 2026-10-13 / 0 / 36 | 140 | daily |
| `fact_uln` | 2026-10-13 / 0 / 309,551 | 2026-10-13 / 0 / 311,174 | 2026-10-13 / 0 / 0 | 61 | daily |
| `fact_ult` | 2026-10-13 / 0 / 219,969 | 2026-10-13 / 0 / 226,234 | 2026-10-13 / 0 / 5,665 | 61 | daily |
| `fact_upn` | 2026-10-13 / 0 / 64,995 | 2026-10-13 / 0 / 65,294 | 2026-10-13 / 0 / 0 | 44 | daily |
| `fact_upt` | 2026-10-13 / 0 / 40,291 | 2026-10-13 / 0 / 44,251 | 2026-10-13 / 0 / 3,883 | 44 | daily |

The legacy channel the skill names: `opal-data-bd/schwab/silver/{acc,rps,trn,trn_nna,uln,ult,rld}/` holds 633 / 634 / 572 / 570 / 634 / 634 / 882 partitions. All of them end at `date=20260723`, which is **57 trading days behind**. Skill-to-monolith map: ACC -> `fact_acc`, RPS -> `fact_rps` + `fact_rps_s2`, TRN -> `fact_trn`, TRN_NNA -> **none**, ULN -> `fact_uln`, ULT -> `fact_ult`, RLD -> `fact_rld`.

### 2.3 Other in-scope silver

| table | objects | rows | newest partition | behind T-1 | variants |
|---|---|---|---|---|---|
| `commonwealth/cottonwood/silver/account_day_value/` | 1 | 21,102,041 | 2026-06-23 | 78 | 1 |
| `commonwealth/cottonwood/silver/account_links/` | 1 | 1,450 | 2026-06-23 | 78 | 1 |
| `commonwealth/cottonwood/silver/coverage/` | 1 | 5 | 2026-06-23 | 78 | 1 |
| `commonwealth/cottonwood/silver/crosswalk/` | 1 | 1,533 | 2026-06-23 | 78 | 1 |
| `commonwealth/cottonwood/silver/daily_returns/` | 1 | 1,691,729 | 2026-06-23 | 78 | 1 |
| `commonwealth/cottonwood/silver/document_index/` | 2 | 11,122 | 2026-06-23 | 78 | 2 |
| `commonwealth/cottonwood/silver/documents/` | 1 | 11,119 | 2026-06-23 | 78 | 1 |
| `commonwealth/cottonwood/silver/month_grades/` | 1 | 82,593 | 2026-06-23 | 78 | 1 |
| `commonwealth/cottonwood/silver/performance/` | 3 | 88,654 | 2026-06-23 | 78 | 1 |
| `commonwealth/cottonwood/silver/positions/` | 1 | 469 | 2026-06-23 | 78 | 1 |
| `commonwealth/cottonwood/silver/price_evidence/` | 1 | 2 | 2022-10-12 | n/a (evidence date) | 1 |
| `commonwealth/cottonwood/silver/transactions/` | 14 | 1,416,497 | 2026-06-23 | 78 | 1 |
| `gateway/global/silver/taxsma_workbook/` | 21 | 441 | 2026-10-13 | 0 | 1 |
| `pathfinder/PFDE/silver/fact_dailynav/` | 91 | 91 | 2026-10-13 | 0 | 1 |
| `pathfinder/PFDE/silver/fact_holdings/` | 91 | 8,099 | 2026-10-13 | 0 | 1 |
| `pathfinder/PFOE/silver/fact_dailynav/` | 91 | 91 | 2026-10-13 | 0 | 1 |
| `pathfinder/PFOE/silver/fact_holdings/` | 91 | 2,211 | 2026-10-13 | 0 | 1 |
| `trueshares/DIVZ/silver/fact_holdings/` | 38 | 1,104 | 2026-09-30 | 9 | 1 |
| `trueshares/DIVZ/silver/fact_netassets_page/` | 91 | 91 | 2026-10-13 | 0 | 1 |
| `trueshares/IDVZ/silver/fact_holdings/` | 38 | 1,615 | 2026-09-30 | 9 | 1 |
| `trueshares/IDVZ/silver/fact_netassets_page/` | 91 | 91 | 2026-10-13 | 0 | 1 |
| `yahoo/global/silver/price_history/` | 1450 | 535,464 | (cusip-partitioned) | 0 (index as_of 2026-10-13) | 8 |
| `bloomberg/global/silver/request_state/` | 1 JSON | -- | 2026-10-09 | plumbing | -- |

## 3. Analysis

### 3.1 What the Schwab tables are

- **`fact_*` is the vendor-complete silver** (Rule 17: dedup and dtype only, every vendor column, T1 trailer reconciled; FAM/SLM are honestly `UNVERIFIED_BY_T1`).
  **`dim_*` is a select-only projection** that rides the same Lambda pass, with row parity enforced (`schwab_projections.py`).
  Measured parity holds: `dim_position` rows = `fact_rps` rows, `dim_balance` = `fact_rps_s2`, `dim_asset` = `fact_sec`, `dim_transaction` = `fact_trn`, on every master.
  `fact_rps_s2` and `dim_balance` have equal object sizes at 1,683 of 1,683 partition pairs (content identity inferred from the identity projection).
- **Snapshot vs event:**
  - Snapshot: acc, rps, rps_s2, sec, uln, ult, upn, upt, and the four dims except dim_transaction. Each partition is a FULL daily snapshot, so the table's row count is the newest partition's, never the sum.
  - Event: trn, dim_transaction and rld are per-day event files, and they do sum.
  - Periodic: rlu and rtu (quarterly), rly and rty (month-end) and rlw (weekly) are each a snapshot of a period. Judge them against their cadence, not against T-1.
- **Grain caveats measured on 08335338 2026-10-13:**
  - `dim_position` repeats account+cusip+l_s on 14 of 110,454 rows.
  - `dim_asset` repeats cusip on 24 of 2,540.
  - `fact_uln` has 0 duplicate account+event_id.
  - `dim_balance` has 0 duplicate accounts.
  A tool must not assume the composite key is unique without that guard.
- **PII:** `fact_acc` carries title lines, taxpayer names, addresses, email, phones, SSN/TIN and DOB. `fact_fam` and `fact_slm` carry person names. The gateway contract forbids `raw_account_id`, `account_title`, `tax_identifier` and `mailing_address`, and serves `account_ref`, not `account_id`. Every proposal below goes through a projection.
- **Freshness, all measured:**
  - Every daily table on all 3 masters is at 2026-10-13, 0 trading days behind.
  - Periodic families are current for their cadence: rlu/rtu 2026-09-04, rly/rty 2026-09-30, rlw 2026-10-09.
  - One stale table: **`fact_fam` (08335338) stops at 2026-08-10, 45 behind**, with bronze fam stopping on 2026-08-11. `fact_slm` continues.
- **08403355 history is mostly empty files:** 303-748 of 512-761 parts per table hold 0 rows. `fact_uln` and `fact_upn` are empty on all 513 parts. The 30 accounts appear only in the recent partitions.

### 3.2 Fork keys (directive section 3 rule 1)

- **Firm:** the key segment `schwab/<master>/` carries it. The registry (`infra/logic/registry/scopes.json`) maps 08242234 and 08335338 to `49financial`; 08403355 has no registry row, and `master_account_name` reads `49 FINANCIAL` (inferred 49financial). All three are one firm, three books.
- **Account:**
  - `account_id` is a 10-character zero-padded string on 15,231 of 15,231 ids, and last-4 = its last 4 characters.
  - **Last-4 collides within the firm:** 1,798 colliding values / 4,056 accounts (08242234), 1,842 / 4,156 (08335338), 0 / 30 (08403355).
  - Over the 7,667-account union of the three masters, 1,848 values collide, covering 4,171 accounts.
  - A tool keyed on last-4 must resolve to candidates and ask, or accept a longer suffix.
- **Platform:** custodian = SCHWAB on every fact_acc row. The platform marker is `mngdacct_pltfrmcd` and `managed_account_money_manager`:
  - 08242234: MAM 7,386 / empty 169; SmartX money manager on 7,384 rows.
  - 08335338: MAM 7,415 / empty 231; SmartX on 7,401.
  - 08403355: MAM 12 / empty 18; SmartX on 0.
  The gateway contract labels the masters `SmartX` (08242234) and `BlackDiamond` (08335338). The CTO ruling calls 08242234 and 08403355 the two Tax SMA masters.
  The `platform` input therefore needs ONE ruled enum mapping label -> master. It is open item O-3.
- **Never cross masters:** 7,534 of 08242234's ids and 30 of 30 of 08403355's ids also appear under 08335338. Summing positions or balances across masters double-counts. DATA_CATALOG.yaml already says so (`never sum across masters`).

### 3.3 Existing contracts and catalog rows that already describe these tables

- `DATA_CATALOG.yaml` `silver_datasets` describe `dim_asset`, `dim_balance`, `dim_position` and `dim_transaction` at :2404, :2426, :2450 and :2474.
  Their wording is "the contract's two masters", so 08403355 is not covered.
  `tool_index` covers `schwab_describe_dataset` :2147, `schwab_get_access` :2200, `schwab_list_files` :2204, `schwab_prepare_download` :2257 and `schwab_query` :2262. Its history_depth was read 2026-10-14T06:00Z over 2 masters.
  The catalog marks balances and positions history PARTIAL (:2639, :2654) and transactions as carrying no flow tag (:2701).
- `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.4: masters {08242234: SmartX, 08335338: BlackDiamond}, 8 data_prefixes, 2 completion prefixes, and the forbidden field classes.
  It does not name 08403355, while `infra/aws/terraform/opal-gateway/schwab_reader_iam.tf:72-75,80` does.
- `org/standards/IRPT_DASHBD_*` (11 files) describe **gold** tables in the firm buckets. None describes a silver table directly; they read Schwab silver through `data/assets/scripts/gold/irpt_reporting/sources.json` `schwab_08335338`:
  - `dim_position`, `dim_balance` and `fact_trn` (positions, balance and transactions prefixes);
  - `fact_rld`, `fact_uln` and `fact_ult` (lot_source);
  - the column semantics (gross_amount is the money, never net_amount; the closing_price unit-price rule; the debit_credit direction map).
  Those semantics are cited in the column descriptions below. Only 08335338 is read; 08242234 and 08403355 feed no IRPT or gold build (CTO ruling 2026-10-09).
- `org/standards/ADVI_BILLING_HOUSEHOLD_CROSSWALK_CONTRACT.json` reads 08335338 `fact_acc` (newest partition) as `schwab_universe`; its grain is "one row per Schwab master-0833 account".
  `ADVI_BILLING_SMARTX_FEE_STATEMENT_CONTRACT.json` addresses a silver table in this bucket that does not exist (section 2.1).
  `ADVI_BILLING_FEE_QUARTER_CONTRACT.json` is gold in the firm bucket.
- Commonwealth, the Tax SMA workbook silver, the ETF fund silver and the Yahoo price store have **no** `DATA_CATALOG.yaml` row and no gateway tool.
  The Tax SMA workbook's own contract is `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` v0.6.0.

### 3.4 Proposed tools (14)

Every client-data tool takes `firm`, `account_last4`, `platform` and `as_of`. A last-4 that matches more than one account returns the candidate list and never merges them. The tools never read two firms in one call.

| tool | reads | verdict on existing | answers |
|---|---|---|---|
| `schwab_resolve_account` | NEW projection `dim_account` of `fact_acc` (account_ref, last4, master, platform code, money manager, acct type, status, date opened; no PII) | new (prerequisite of every last-4 tool) | which accounts end in 1234; platform and status of an account |
| `schwab_get_positions` | `dim_position` (+ optional pending from upn/upt once ruled) | extend `schwab_query` (preset + last-4 + history beyond 30 days) | what does ...1234 hold on a date |
| `schwab_get_balances` | `dim_balance` | extend `schwab_query` | cash, net MV, margin of ...1234 |
| `schwab_list_transactions` | `dim_transaction` (+ the IRPT classification table for a flow tag) | extend `schwab_query` (adds the flow tag DATA_CATALOG.yaml:2701 lacks) | deposits, withdrawals and trades of ...1234 |
| `schwab_get_security` | `dim_asset` | extend `schwab_query` | ticker, description, price of a cusip |
| `schwab_get_unrealized_lots` | NEW projection `dim_lot_unrealized` of `fact_uln` + `fact_ult` | new | open lots, cost basis, unrealized gain |
| `schwab_get_realized_lots` | NEW projection `dim_lot_realized` of `fact_rld` (period daily) / `fact_rlw` / `fact_rly` / `fact_rlu` | new | realized gains by day, week, YTD, cumulative |
| `schwab_get_tax_lot_detail` | `fact_rtu` / `fact_rty` | new | tax-lot detail YTD or cumulative |
| `commonwealth_resolve_account` | `crosswalk`, `account_links` | new | old Commonwealth account -> current account |
| `commonwealth_get_account_history` | `account_day_value`, `daily_returns`, `positions` | new | value and return of ...1234 before 2026-06-23 |
| `commonwealth_get_performance` | `performance`, `month_grades` | new | reported and rebuilt returns |
| `commonwealth_list_transactions` | `transactions` | new | history 2013-2026 |
| `commonwealth_find_documents` | `document_index`, `documents` (metadata + ticketed link) | new | which statements exist |
| `taxsma_get_workbook_rows` | `gateway/global/silver/taxsma_workbook` (firm filter on RIA REQUIRED) | new | Ready/Traded/AUM per Tax SMA account |

Not counted as client tools: `etfs_get_fund_holdings` and `etfs_get_fund_nav` (fund silver; reconcile with G5 first), `prices_get_history` (Yahoo reference store) and `commonwealth_describe_delivery` (coverage).

## 4. Contracts (one JSON block per bucket -> table)

Order: Schwab 08242234, 08335338, 08403355 (alphabetical by table); Commonwealth; Tax SMA workbook; ETF fund silver; Yahoo.
Column lists are the measured footer union. `nullable` comes from the newest part's schema. `pii: true` marks a column a tool must never return. `description` is present only where a source states the meaning.

### `opal-data-assets/silver/schwab_08242234_dim_asset`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08242234_dim_asset",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08242234/silver/dim_asset/",
 "layer": "silver",
 "format": "parquet",
 "table": "dim_asset",
 "source_feed": "SEC projection",
 "grain": "one row per cusip per business_date (24-column projection of fact_sec)",
 "description": "Gateway-served security master projection (dataset dim_asset).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08242234/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 690,
  "partitions": 690,
  "first_partition": "2024-01-16",
  "bytes": 121596328,
  "rows_all_partitions": 1583297,
  "rows_newest_partition": 2197,
  "row_count_rule": "snapshot table: the table row count is the newest partition (2197 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 29,
  "claim": "measured"
 },
 "columns": [
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "security_description_line_1", "type": "string", "nullable": true},
  {"name": "security_description_line_2", "type": "string", "nullable": true},
  {"name": "security_description_line_3", "type": "string", "nullable": true},
  {"name": "scrtydes_line_4", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "mnymk_code", "type": "string", "nullable": true},
  {"name": "closing_price", "type": "decimal128(16, 5)", "nullable": true, "description": "custodian per-share close (never additive)"},
  {"name": "closing_price_unfactored", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "par_value", "type": "decimal128(36, 18)", "nullable": true},
  {"name": "interest_rate", "type": "decimal128(7, 5)", "nullable": true},
  {"name": "maturity_date", "type": "date32[day]", "nullable": true},
  {"name": "strike_price", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "c_p", "type": "string", "nullable": true},
  {"name": "opt_expr_date", "type": "string", "nullable": true},
  {"name": "s_p_rating", "type": "string", "nullable": true},
  {"name": "moodys_rating", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08242234",
   "master_account_name_measured": "49 WEALTH MANAGEMENT LLC",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "none (security grain)",
   "last4_derivation": "n/a",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "SmartX"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7555 of 7555 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7386,
    "<empty>": 169
   },
   "money_manager_distinct": 2,
   "money_manager_smartx_rows": 7384,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "security master",
  "cusip",
  "ticker",
  "schwab",
  "49financial",
  "master 08242234"
 ],
 "common_queries": [
  "What is the ticker and description of a Schwab security by cusip?"
 ],
 "existing_gateway_tool": {
  "name": "schwab_query (+ schwab_list_files, schwab_describe_dataset, schwab_get_access, schwab_prepare_download)",
  "verdict": "extend",
  "note": "keep the typed query; extend with last-4 resolution, history beyond the 30-day rolling window (DATA_CATALOG.yaml:2639 and :2654 mark PARTIAL), and the fork inputs"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_security",
   "inputs": {
    "firm": "49financial",
    "account_last4": "n/a (security grain)",
    "platform": "SmartX",
    "as_of": "YYYY-MM-DD",
    "cusip_or_ticker": "<cusip|ticker>"
   },
   "returns": "one dim_asset row",
   "answers": [
    "What is the ticker and description of a Schwab security by cusip?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "silver_datasets.schwab_dim_asset",
  "present": true,
  "line": 2404
 },
 "prior_art": "org/standards/NFRA_OPLGTW_CONTRACT.json v1.4 (dataset dim_asset); data/assets/scripts/silver/schwab_projections.py PROJECTIONS; docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 690 parts of schwab/08242234/silver/dim_asset/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08242234_dim_balance`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08242234_dim_balance",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08242234/silver/dim_balance/",
 "layer": "silver",
 "format": "parquet",
 "table": "dim_balance",
 "source_feed": "RPS section 2 projection",
 "grain": "one row per account per business_date (identity projection of fact_rps_s2)",
 "description": "Gateway-served balances projection (dataset dim_balance).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08242234/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 599,
  "partitions": 599,
  "first_partition": "2024-05-24",
  "bytes": 249515573,
  "rows_all_partitions": 3352068,
  "rows_newest_partition": 7555,
  "row_count_rule": "snapshot table: the table row count is the newest partition (7555 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 39,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "account_title_line_1", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_2", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_3", "type": "string", "nullable": true, "pii": true},
  {"name": "acct_regis", "type": "string", "nullable": true},
  {"name": "acct_type", "type": "string", "nullable": true},
  {"name": "net_credit_debit", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "margin_balance", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "available_to_pay", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mrgn_buying_pwr", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "money_mkt_funds", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mtd_margin_int", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "daily_margin_int", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "eqty_excl_option", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "eqty_percentage", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mkt_value_long", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mkt_value_short", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "eqty_incl_option", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "option_rqrmnts", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mnth_end_div_pay", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "maintenance_call", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mvl_cash_ex_optn", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "net_mv_positions", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "net_mv_plus_cash", "type": "decimal128(15, 2)", "nullable": true, "description": "net market value of positions plus cash"},
  {"name": "cash_balance_settled_only", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "cash_margin_bal_settled", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "bank_sweep_ibf", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "bank_cash", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08242234",
   "master_account_name_measured": "49 WEALTH MANAGEMENT LLC",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7555 ids measured length 10)",
   "last4_collisions_within_firm": 1798,
   "accounts_in_collisions": 4056,
   "denominator_accounts": 7555,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "SmartX"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7555 of 7555 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7386,
    "<empty>": 169
   },
   "money_manager_distinct": 2,
   "money_manager_smartx_rows": 7384,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "balances",
  "cash",
  "account value",
  "schwab",
  "49financial",
  "master 08242234"
 ],
 "common_queries": [
  "What is the cash balance and net market value of account ...1234 on a date?"
 ],
 "existing_gateway_tool": {
  "name": "schwab_query (+ schwab_list_files, schwab_describe_dataset, schwab_get_access, schwab_prepare_download)",
  "verdict": "extend",
  "note": "keep the typed query; extend with last-4 resolution, history beyond the 30-day rolling window (DATA_CATALOG.yaml:2639 and :2654 mark PARTIAL), and the fork inputs"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_balances",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "SmartX",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "one dim_balance row per resolved account_ref for as_of",
   "answers": [
    "What is the cash balance and net market value of account ...1234 on a date?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "silver_datasets.schwab_dim_balance",
  "present": true,
  "line": 2426
 },
 "prior_art": "org/standards/NFRA_OPLGTW_CONTRACT.json v1.4 (dataset dim_balance); data/assets/scripts/silver/schwab_projections.py PROJECTIONS; docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 599 parts of schwab/08242234/silver/dim_balance/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08242234_dim_position`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08242234_dim_position",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08242234/silver/dim_position/",
 "layer": "silver",
 "format": "parquet",
 "table": "dim_position",
 "source_feed": "RPS projection",
 "grain": "one row per account x cusip x l_s per business_date (25-column projection of fact_rps, row parity enforced)",
 "description": "Gateway-served positions projection (contract NFRA_OPLGTW v1.4 dataset dim_position).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08242234/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 599,
  "partitions": 599,
  "first_partition": "2024-05-24",
  "bytes": 841960586,
  "rows_all_partitions": 40942928,
  "rows_newest_partition": 106194,
  "row_count_rule": "snapshot table: the table row count is the newest partition (106194 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 30,
  "claim": "measured"
 },
 "columns": [
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "accounting_rule_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "quantity_settled_unsettled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_unsettled_long", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_unsettled_short", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_cash_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_margin_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_short_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_wheniss_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "non_tradable_quantity", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "market_value_settled_unsettled", "type": "decimal128(17, 4)", "nullable": true, "description": "position market value (additive; short rows negative)"},
  {"name": "closing_price", "type": "decimal128(16, 5)", "nullable": true, "description": "custodian per-share close (never additive)"},
  {"name": "closing_price_unfactored", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "asset_backed_factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "secprice_lstupdte", "type": "date32[day]", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08242234",
   "master_account_name_measured": "49 WEALTH MANAGEMENT LLC",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7555 ids measured length 10)",
   "last4_collisions_within_firm": 1798,
   "accounts_in_collisions": 4056,
   "denominator_accounts": 7555,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "SmartX"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7555 of 7555 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7386,
    "<empty>": 169
   },
   "money_manager_distinct": 2,
   "money_manager_smartx_rows": 7384,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "positions",
  "holdings",
  "positions by account",
  "schwab",
  "49financial",
  "master 08242234"
 ],
 "common_queries": [
  "What does account ...1234 hold today?",
  "What is the market value of a security in account ...1234 on a date?"
 ],
 "existing_gateway_tool": {
  "name": "schwab_query (+ schwab_list_files, schwab_describe_dataset, schwab_get_access, schwab_prepare_download)",
  "verdict": "extend",
  "note": "keep the typed query; extend with last-4 resolution, history beyond the 30-day rolling window (DATA_CATALOG.yaml:2639 and :2654 mark PARTIAL), and the fork inputs"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_positions",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "SmartX",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "rows of dim_position for the resolved account_ref(s) on the business_date at or before as_of; a last-4 that matches several accounts returns the candidate list, never a merge",
   "answers": [
    "What does account ...1234 hold today?",
    "What is the market value of a security in account ...1234 on a date?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "silver_datasets.schwab_dim_position",
  "present": true,
  "line": 2450
 },
 "prior_art": "org/standards/NFRA_OPLGTW_CONTRACT.json v1.4 (dataset dim_position); data/assets/scripts/silver/schwab_projections.py PROJECTIONS; docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 599 parts of schwab/08242234/silver/dim_position/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08242234_dim_transaction`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08242234_dim_transaction",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08242234/silver/dim_transaction/",
 "layer": "silver",
 "format": "parquet",
 "table": "dim_transaction",
 "source_feed": "TRN projection",
 "grain": "one row per transaction line per business_date (39-column projection of fact_trn; append, no row-unique key)",
 "description": "Gateway-served transactions projection (dataset dim_transaction).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08242234/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 690,
  "partitions": 690,
  "first_partition": "2024-01-16",
  "bytes": 80793539,
  "rows_all_partitions": 3778943,
  "rows_newest_partition": 11827,
  "row_count_rule": "event/append table: rows sum across partitions",
  "schema_variants": 1,
  "columns_union": 44,
  "claim": "measured"
 },
 "columns": [
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "trade_date", "type": "date32[day]", "nullable": true},
  {"name": "settlmnt_date", "type": "date32[day]", "nullable": true},
  {"name": "tran_date", "type": "date32[day]", "nullable": true},
  {"name": "tr_cd", "type": "string", "nullable": true},
  {"name": "sb_cd", "type": "string", "nullable": true},
  {"name": "transaction_category", "type": "string", "nullable": true},
  {"name": "tran_srcde", "type": "string", "nullable": true},
  {"name": "transaction_source_code_description", "type": "string", "nullable": true},
  {"name": "transaction_detail_description", "type": "string", "nullable": true},
  {"name": "debit_credit", "type": "string", "nullable": true},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "quantity", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "price", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "gross_amount", "type": "decimal128(15, 2)", "nullable": true, "description": "the money of a transaction (IRPT money law: never net_amount)"},
  {"name": "net_amount", "type": "decimal128(15, 2)", "nullable": true, "description": "net amount (reads 0.00 on cash rows; not the money)"},
  {"name": "accrued_interest", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "commission", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "prime_broker_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "trade_away_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "redemption_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "other_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "step_in_fee", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "research_fee", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "exec_brok_comm", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "broker_service_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "exchange_processing_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "federal_tefra_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "retirement_fed_income_tax", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "retirement_state_income_tax", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "closing_price", "type": "decimal128(16, 5)", "nullable": true, "description": "custodian per-share close (never additive)"},
  {"name": "factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08242234",
   "master_account_name_measured": "49 WEALTH MANAGEMENT LLC",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7555 ids measured length 10)",
   "last4_collisions_within_firm": 1798,
   "accounts_in_collisions": 4056,
   "denominator_accounts": 7555,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "SmartX"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7555 of 7555 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7386,
    "<empty>": 169
   },
   "money_manager_distinct": 2,
   "money_manager_smartx_rows": 7384,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "transactions",
  "trades",
  "flows",
  "schwab",
  "49financial",
  "master 08242234"
 ],
 "common_queries": [
  "What transactions did account ...1234 have on a date?"
 ],
 "existing_gateway_tool": {
  "name": "schwab_query (+ schwab_list_files, schwab_describe_dataset, schwab_get_access, schwab_prepare_download)",
  "verdict": "extend",
  "note": "keep the typed query; extend with last-4 resolution, history beyond the 30-day rolling window (DATA_CATALOG.yaml:2639 and :2654 mark PARTIAL), and the fork inputs"
 },
 "proposed_tools": [
  {
   "name": "schwab_list_transactions",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "SmartX",
    "as_of": "YYYY-MM-DD or start..end (<= 31 business dates)"
   },
   "returns": "dim_transaction rows by business_date for the resolved account_ref(s); row identity is (partition, row position)",
   "answers": [
    "What transactions did account ...1234 have on a date?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "silver_datasets.schwab_dim_transaction",
  "present": true,
  "line": 2474
 },
 "prior_art": "org/standards/NFRA_OPLGTW_CONTRACT.json v1.4 (dataset dim_transaction); data/assets/scripts/silver/schwab_projections.py PROJECTIONS; docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 690 parts of schwab/08242234/silver/dim_transaction/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08242234_fact_acc`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08242234_fact_acc",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08242234/silver/fact_acc/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_acc",
 "source_feed": "ACC",
 "grain": "one row per account per business_date (daily full snapshot of the master account file)",
 "description": "Account master: identity, registration, account type, status, open date, platform and money manager, and the client PII the vendor sends (title lines, taxpayer, address, contact, SSN/TIN, DOB).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08242234/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 690,
  "partitions": 690,
  "first_partition": "2024-01-16",
  "bytes": 397498975,
  "rows_all_partitions": 3706028,
  "rows_newest_partition": 7555,
  "row_count_rule": "snapshot table: the table row count is the newest partition (7555 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 95,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "account_title_line_1", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_2", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_3", "type": "string", "nullable": true, "pii": true},
  {"name": "account_status", "type": "string", "nullable": true},
  {"name": "acct_regis", "type": "string", "nullable": true},
  {"name": "acct_type", "type": "string", "nullable": true},
  {"name": "txpyr_title", "type": "string", "nullable": true, "pii": true},
  {"name": "taxpayer_first_name", "type": "string", "nullable": true, "pii": true},
  {"name": "taxpayer_middle_name", "type": "string", "nullable": true, "pii": true},
  {"name": "taxpayer_last_name", "type": "string", "nullable": true, "pii": true},
  {"name": "txpyr_suff", "type": "string", "nullable": true, "pii": true},
  {"name": "wh_cd", "type": "string", "nullable": true},
  {"name": "primary_contact", "type": "string", "nullable": true, "pii": true},
  {"name": "alias_name", "type": "string", "nullable": true, "pii": true},
  {"name": "mailing_address_line_1", "type": "string", "nullable": true, "pii": true},
  {"name": "mailing_address_line_2", "type": "string", "nullable": true, "pii": true},
  {"name": "mailing_address_line_3", "type": "string", "nullable": true, "pii": true},
  {"name": "account_mailing_city", "type": "string", "nullable": true, "pii": true},
  {"name": "ac_st", "type": "string", "nullable": true},
  {"name": "acct_mail_zip", "type": "string", "nullable": true, "pii": true},
  {"name": "acct_mailing_ctry_code", "type": "string", "nullable": true, "pii": true},
  {"name": "email_address", "type": "string", "nullable": true, "pii": true},
  {"name": "phone_nbr", "type": "string", "nullable": true, "pii": true},
  {"name": "business_ph", "type": "string", "nullable": true, "pii": true},
  {"name": "date_opened", "type": "date32[day]", "nullable": true},
  {"name": "schwab_br_cd", "type": "string", "nullable": true},
  {"name": "s_s", "type": "string", "nullable": true},
  {"name": "ac_cs", "type": "string", "nullable": true},
  {"name": "ac_ma", "type": "string", "nullable": true},
  {"name": "m_a", "type": "string", "nullable": true},
  {"name": "a_r", "type": "string", "nullable": true},
  {"name": "a_m", "type": "string", "nullable": true},
  {"name": "nr_am", "type": "string", "nullable": true},
  {"name": "a_o", "type": "string", "nullable": true},
  {"name": "b_f", "type": "string", "nullable": true},
  {"name": "nr_bn", "type": "string", "nullable": true},
  {"name": "p_c", "type": "string", "nullable": true},
  {"name": "p_d", "type": "string", "nullable": true},
  {"name": "p_b", "type": "string", "nullable": true},
  {"name": "u_m", "type": "string", "nullable": true},
  {"name": "f_a", "type": "string", "nullable": true},
  {"name": "intbr_cd", "type": "string", "nullable": true},
  {"name": "intbr_mm_cd", "type": "string", "nullable": true},
  {"name": "intbearing_ticker_symbol", "type": "string", "nullable": true},
  {"name": "intbearing_feat_is_id", "type": "string", "nullable": true},
  {"name": "int_sf", "type": "string", "nullable": true},
  {"name": "p_v", "type": "string", "nullable": true},
  {"name": "p_m", "type": "string", "nullable": true},
  {"name": "statemnt_pref", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "dflt_ltsel", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "cbm_mf", "type": "string", "nullable": true},
  {"name": "cbm_nmf", "type": "string", "nullable": true},
  {"name": "cb_mthd_date", "type": "date32[day]", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "custtype_code", "type": "string", "nullable": true},
  {"name": "organization_primary_name", "type": "string", "nullable": true, "pii": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "rstr_rsn1", "type": "string", "nullable": true},
  {"name": "rstr_rsn2", "type": "string", "nullable": true},
  {"name": "rstr_rsn3", "type": "string", "nullable": true},
  {"name": "rstr_rsn4", "type": "string", "nullable": true},
  {"name": "rstr_rsn5", "type": "string", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "schwab_bank_ic_account", "type": "string", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "ssn_tin_number", "type": "string", "nullable": true, "pii": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "p_e", "type": "string", "nullable": true},
  {"name": "mngdacct_pltfrmcd", "type": "string", "nullable": true, "description": "managed-account platform code (measured values MAM or empty)"},
  {"name": "managed_account_money_manager", "type": "string", "nullable": true, "description": "money manager of a managed account (the SmartX marker)"},
  {"name": "managed_account_investment_strategy", "type": "string", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "bank_sweep_display_name", "type": "string", "nullable": true},
  {"name": "versmrkr_7", "type": "string", "nullable": true},
  {"name": "o_l", "type": "string", "nullable": true},
  {"name": "versmrkr_8", "type": "string", "nullable": true},
  {"name": "date_of_birth", "type": "date32[day]", "nullable": true, "pii": true},
  {"name": "coy_cd", "type": "string", "nullable": true},
  {"name": "st_cd", "type": "string", "nullable": true},
  {"name": "versmrkr_9", "type": "string", "nullable": true},
  {"name": "s_i", "type": "string", "nullable": true},
  {"name": "m_t", "type": "string", "nullable": true},
  {"name": "mobile_phone_number", "type": "string", "nullable": true, "pii": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08242234",
   "master_account_name_measured": "49 WEALTH MANAGEMENT LLC",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7555 ids measured length 10)",
   "last4_collisions_within_firm": 1798,
   "accounts_in_collisions": 4056,
   "denominator_accounts": 7555,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "SmartX"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7555 of 7555 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7386,
    "<empty>": 169
   },
   "money_manager_distinct": 2,
   "money_manager_smartx_rows": 7384,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "account",
  "account master",
  "registration",
  "account status",
  "money manager",
  "platform",
  "schwab",
  "49financial",
  "master 08242234"
 ],
 "common_queries": [
  "Which platform and money manager is account ...1234 on?",
  "Is account ...1234 open or closed, and when was it opened?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_resolve_account",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "SmartX",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "candidate account_refs with master, platform code, money manager, account type and status, from a NEW non-PII projection dim_account of fact_acc (projection law: select only); never title, taxpayer, address, contact, SSN/TIN or DOB",
   "answers": [
    "Which platform and money manager is account ...1234 on?",
    "Is account ...1234 open or closed, and when was it opened?",
    "Which accounts end in 1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "carries client PII columns (flagged pii:true); any tool must project them away (NFRA_OPLGTW forbidden_field_classes: raw_account_id, account_title, tax_identifier, mailing_address)"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 690 parts of schwab/08242234/silver/fact_acc/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08242234_fact_rld`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08242234_fact_rld",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08242234/silver/fact_rld/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rld",
 "source_feed": "RLD",
 "grain": "one row per realized lot closed on the business_date (daily; closing_date = business date on 08335338 2026-10-13)",
 "description": "Realized lots, daily: closing and opening events, quantity, proceeds, cost basis, gain/loss, holding term, order number. The PRIMARY realized-lot tax source (IRPT_DASHBD lot_source realized; legacy B_02).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08242234/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 940,
  "partitions": 940,
  "first_partition": "2023-01-17",
  "bytes": 146893002,
  "rows_all_partitions": 1058219,
  "rows_newest_partition": 6018,
  "row_count_rule": "event/append table: rows sum across partitions",
  "schema_variants": 1,
  "columns_union": 86,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "closing_date", "type": "date32[day]", "nullable": true, "description": "realized lot closing date"},
  {"name": "closing_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "proceeds", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "proceeds_per_share", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "orgpurch_date", "type": "date32[day]", "nullable": true},
  {"name": "original_purchase_price", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "adjusted_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adjusted_gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f_2", "type": "string", "nullable": true},
  {"name": "g_f", "type": "string", "nullable": true},
  {"name": "p_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "lot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adj_disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "publication_timestamp", "type": "string", "nullable": true},
  {"name": "cbm", "type": "string", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "federal_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "wh_st", "type": "string", "nullable": true},
  {"name": "ytd_amortization", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_i", "type": "string", "nullable": true},
  {"name": "settle_date", "type": "date32[day]", "nullable": true},
  {"name": "r_u", "type": "string", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "transaction_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_gain_loss_pct", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "employee_option_original_cost", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "employee_option_realized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "g_i", "type": "string", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "trancode_expanded", "type": "string", "nullable": true},
  {"name": "order_number", "type": "string", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "close_event_id", "type": "string", "nullable": true},
  {"name": "close_open_event_id", "type": "string", "nullable": true},
  {"name": "versmrkr_7", "type": "string", "nullable": true},
  {"name": "schwab_order_id", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08242234",
   "master_account_name_measured": "49 WEALTH MANAGEMENT LLC",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7555 ids measured length 10)",
   "last4_collisions_within_firm": 1798,
   "accounts_in_collisions": 4056,
   "denominator_accounts": 7555,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "SmartX"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7555 of 7555 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7386,
    "<empty>": 169
   },
   "money_manager_distinct": 2,
   "money_manager_smartx_rows": 7384,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "realized lots",
  "realized gains",
  "tax",
  "capital gains",
  "schwab",
  "49financial",
  "master 08242234"
 ],
 "common_queries": [
  "What realized gains did account ...1234 book on a date?",
  "What lots of CUSIP X were sold from account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_realized_lots",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "SmartX",
    "as_of": "YYYY-MM-DD or start..end",
    "period": "daily"
   },
   "returns": "realized lots (closing_date, cusip, ticker, closing_quantity, proceeds, cost_basis_unamortized, gain_loss_dollars, h_t) from a NEW projection dim_lot_realized over fact_rld",
   "answers": [
    "What realized gains did account ...1234 book on a date?",
    "What lots of CUSIP X were sold from account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "1 of 940 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 940 parts of schwab/08242234/silver/fact_rld/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08242234_fact_rlu`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08242234_fact_rlu",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08242234/silver/fact_rlu/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rlu",
 "source_feed": "RLU",
 "grain": "one row per realized lot, cumulative file; MEASURED cadence: quarterly (2023-03-03, 06-02, 09-01 ... 2026-06-05, 2026-09-04)",
 "description": "Realized lots, cumulative (unrealized-period file family per vendor naming); same layout family as fact_rld.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08242234/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-09-04",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 26,
  "cadence": "quarterly",
  "claim": "measured",
  "note": "judge against the cadence, not T-1: the newest file of a quarterly family is current until the next one is due"
 },
 "size": {
  "objects": 15,
  "partitions": 15,
  "first_partition": "2023-03-03",
  "bytes": 285993795,
  "rows_all_partitions": 2704973,
  "rows_newest_partition": 282721,
  "row_count_rule": "snapshot table: the table row count is the newest partition (282721 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 87,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "closing_date", "type": "date32[day]", "nullable": true, "description": "realized lot closing date"},
  {"name": "closing_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "proceeds", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "proceeds_per_share", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "orgpurch_date", "type": "date32[day]", "nullable": true},
  {"name": "original_purchase_price", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "adjusted_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adjusted_gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f_2", "type": "string", "nullable": true},
  {"name": "g_f", "type": "string", "nullable": true},
  {"name": "p_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "lot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adj_disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "publication_timestamp", "type": "string", "nullable": true},
  {"name": "cbm", "type": "string", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "federal_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "wh_st", "type": "string", "nullable": true},
  {"name": "ytd_amortization", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_i", "type": "string", "nullable": true},
  {"name": "settle_date", "type": "date32[day]", "nullable": true},
  {"name": "r_u", "type": "string", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "transaction_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_gain_loss_pct", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "employee_option_original_cost", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "employee_option_realized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "g_i", "type": "string", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "trancode_expanded", "type": "string", "nullable": true},
  {"name": "order_number", "type": "string", "nullable": true},
  {"name": "versmrkr_7", "type": "string", "nullable": true},
  {"name": "close_event_id", "type": "string", "nullable": true},
  {"name": "close_open_event_id", "type": "string", "nullable": true},
  {"name": "versmrkr_8", "type": "string", "nullable": true},
  {"name": "schwab_order_id", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08242234",
   "master_account_name_measured": "49 WEALTH MANAGEMENT LLC",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7555 ids measured length 10)",
   "last4_collisions_within_firm": 1798,
   "accounts_in_collisions": 4056,
   "denominator_accounts": 7555,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "SmartX"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7555 of 7555 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7386,
    "<empty>": 169
   },
   "money_manager_distinct": 2,
   "money_manager_smartx_rows": 7384,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "realized lots",
  "cumulative realized gains",
  "schwab",
  "49financial",
  "master 08242234"
 ],
 "common_queries": [
  "What are the cumulative realized gains of account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_realized_lots",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "SmartX",
    "as_of": "YYYY-MM-DD",
    "period": "cumulative"
   },
   "returns": "as fact_rld from the newest quarterly cumulative file at or before as_of",
   "answers": [
    "What are the cumulative realized gains of account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 15 parts of schwab/08242234/silver/fact_rlu/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08242234_fact_rlw`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08242234_fact_rlw",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08242234/silver/fact_rlw/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rlw",
 "source_feed": "RLW",
 "grain": "one row per realized lot, weekly file; MEASURED cadence: every Friday (2025-09-05 ... 2026-10-09); 08242234 only",
 "description": "Realized lots, weekly; presumed rld sibling at weekly cadence (data dictionary 2b-bis, presumption labeled).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08242234/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-09",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 2,
  "cadence": "weekly (Friday)",
  "claim": "measured",
  "note": "judge against the cadence, not T-1: the newest file of a weekly (Friday) family is current until the next one is due"
 },
 "size": {
  "objects": 52,
  "partitions": 52,
  "first_partition": "2025-09-05",
  "bytes": 1150208481,
  "rows_all_partitions": 11077930,
  "rows_newest_partition": 369371,
  "row_count_rule": "snapshot table: the table row count is the newest partition (369371 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 80,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "closing_date", "type": "date32[day]", "nullable": true, "description": "realized lot closing date"},
  {"name": "closing_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "proceeds", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "proceeds_per_share", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "orgpurch_date", "type": "date32[day]", "nullable": true},
  {"name": "original_purchase_price", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "adjusted_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adjusted_gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f_2", "type": "string", "nullable": true},
  {"name": "g_f", "type": "string", "nullable": true},
  {"name": "p_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "lot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adj_disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "publication_timestamp", "type": "string", "nullable": true},
  {"name": "cbm", "type": "string", "nullable": true},
  {"name": "federal_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "wh_st", "type": "string", "nullable": true},
  {"name": "ytd_amortization", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_i", "type": "string", "nullable": true},
  {"name": "settle_date", "type": "date32[day]", "nullable": true},
  {"name": "r_u", "type": "string", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "transaction_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_gain_loss_pct", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "employee_option_original_cost", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "employee_option_realized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "g_i", "type": "string", "nullable": true},
  {"name": "trancode_expanded", "type": "string", "nullable": true},
  {"name": "order_number", "type": "string", "nullable": true},
  {"name": "close_event_id", "type": "string", "nullable": true},
  {"name": "close_open_event_id", "type": "string", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "schwab_order_id", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08242234",
   "master_account_name_measured": "49 WEALTH MANAGEMENT LLC",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7555 ids measured length 10)",
   "last4_collisions_within_firm": 1798,
   "accounts_in_collisions": 4056,
   "denominator_accounts": 7555,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "SmartX"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7555 of 7555 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7386,
    "<empty>": 169
   },
   "money_manager_distinct": 2,
   "money_manager_smartx_rows": 7384,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "realized lots",
  "weekly realized gains",
  "schwab",
  "49financial",
  "master 08242234"
 ],
 "common_queries": [
  "What did account ...1234 realize this week?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_realized_lots",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "SmartX",
    "as_of": "YYYY-MM-DD",
    "period": "weekly"
   },
   "returns": "as fact_rld from the weekly file (08242234 only)",
   "answers": [
    "What did account ...1234 realize this week?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 52 parts of schwab/08242234/silver/fact_rlw/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08242234_fact_rly`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08242234_fact_rly",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08242234/silver/fact_rly/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rly",
 "source_feed": "RLY",
 "grain": "one row per realized lot, year-to-date file; MEASURED cadence: month-end (2023-01-31 ... 2026-09-30)",
 "description": "Realized lots, year-to-date (yearly file family).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08242234/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-09-30",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 9,
  "cadence": "month-end",
  "claim": "measured",
  "note": "judge against the cadence, not T-1: the newest file of a month-end family is current until the next one is due"
 },
 "size": {
  "objects": 45,
  "partitions": 45,
  "first_partition": "2023-01-31",
  "bytes": 647982863,
  "rows_all_partitions": 6129474,
  "rows_newest_partition": 324125,
  "row_count_rule": "snapshot table: the table row count is the newest partition (324125 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 87,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "closing_date", "type": "date32[day]", "nullable": true, "description": "realized lot closing date"},
  {"name": "closing_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "proceeds", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "proceeds_per_share", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "orgpurch_date", "type": "date32[day]", "nullable": true},
  {"name": "original_purchase_price", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "adjusted_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adjusted_gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f_2", "type": "string", "nullable": true},
  {"name": "g_f", "type": "string", "nullable": true},
  {"name": "p_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "lot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adj_disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "publication_timestamp", "type": "string", "nullable": true},
  {"name": "cbm", "type": "string", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "federal_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "wh_st", "type": "string", "nullable": true},
  {"name": "ytd_amortization", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_i", "type": "string", "nullable": true},
  {"name": "settle_date", "type": "date32[day]", "nullable": true},
  {"name": "r_u", "type": "string", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "transaction_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_gain_loss_pct", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "employee_option_original_cost", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "employee_option_realized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "g_i", "type": "string", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "trancode_expanded", "type": "string", "nullable": true},
  {"name": "order_number", "type": "string", "nullable": true},
  {"name": "versmrkr_7", "type": "string", "nullable": true},
  {"name": "close_event_id", "type": "string", "nullable": true},
  {"name": "close_open_event_id", "type": "string", "nullable": true},
  {"name": "versmrkr_8", "type": "string", "nullable": true},
  {"name": "schwab_order_id", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08242234",
   "master_account_name_measured": "49 WEALTH MANAGEMENT LLC",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7555 ids measured length 10)",
   "last4_collisions_within_firm": 1798,
   "accounts_in_collisions": 4056,
   "denominator_accounts": 7555,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "SmartX"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7555 of 7555 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7386,
    "<empty>": 169
   },
   "money_manager_distinct": 2,
   "money_manager_smartx_rows": 7384,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "realized lots",
  "year-to-date realized gains",
  "tax",
  "schwab",
  "49financial",
  "master 08242234"
 ],
 "common_queries": [
  "What are the year-to-date realized gains of account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_realized_lots",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "SmartX",
    "as_of": "YYYY-MM-DD",
    "period": "ytd"
   },
   "returns": "as fact_rld from the newest month-end year-to-date file at or before as_of",
   "answers": [
    "What are the year-to-date realized gains of account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 45 parts of schwab/08242234/silver/fact_rly/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08242234_fact_rps`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08242234_fact_rps",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08242234/silver/fact_rps/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rps",
 "source_feed": "RPS",
 "grain": "one row per account x security (cusip) x long/short side per business_date (daily full snapshot; 14 of 110,454 rows repeat account+cusip+l_s on 08335338 2026-10-13)",
 "description": "Positions, vendor-complete: quantities (settled, unsettled, cash, margin, short, when-issued), market value, closing price, factors.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08242234/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 599,
  "partitions": 599,
  "first_partition": "2024-05-24",
  "bytes": 996968069,
  "rows_all_partitions": 40942928,
  "rows_newest_partition": 106194,
  "row_count_rule": "snapshot table: the table row count is the newest partition (106194 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 63,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ly_st", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "rulst_sufid", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "security_description_line_1", "type": "string", "nullable": true},
  {"name": "security_description_line_2", "type": "string", "nullable": true},
  {"name": "security_description_line_3", "type": "string", "nullable": true},
  {"name": "scrtydes_line_4", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlying_industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "unrul_sufid", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "mnymk_code", "type": "string", "nullable": true},
  {"name": "d_r", "type": "string", "nullable": true},
  {"name": "c_g", "type": "string", "nullable": true},
  {"name": "closing_price", "type": "decimal128(16, 5)", "nullable": true, "description": "custodian per-share close (never additive)"},
  {"name": "secprice_lstupdte", "type": "date32[day]", "nullable": true},
  {"name": "quantity_settled_unsettled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "market_value_settled_unsettled", "type": "decimal128(17, 4)", "nullable": true, "description": "position market value (additive; short rows negative)"},
  {"name": "accounting_rule_code", "type": "string", "nullable": true},
  {"name": "quantity_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_unsettled_long", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_unsettled_short", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "tips_factor", "type": "decimal128(18, 9)", "nullable": true},
  {"name": "asset_backed_factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "closing_price_unfactored", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "factor_date", "type": "date32[day]", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "non_tradable_quantity", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "a_i", "type": "string", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "quantity_cash_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_margin_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_short_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_wheniss_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08242234",
   "master_account_name_measured": "49 WEALTH MANAGEMENT LLC",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7555 ids measured length 10)",
   "last4_collisions_within_firm": 1798,
   "accounts_in_collisions": 4056,
   "denominator_accounts": 7555,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "SmartX"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7555 of 7555 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7386,
    "<empty>": 169
   },
   "money_manager_distinct": 2,
   "money_manager_smartx_rows": 7384,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "positions",
  "holdings",
  "quantity",
  "market value",
  "schwab",
  "49financial",
  "master 08242234"
 ],
 "common_queries": [
  "What does account ...1234 hold today?",
  "What is the market value of CUSIP X in account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none (served only through its dim_ projection via schwab_query)",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 599 parts of schwab/08242234/silver/fact_rps/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08242234_fact_rps_s2`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08242234_fact_rps_s2",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08242234/silver/fact_rps_s2/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rps_s2",
 "source_feed": "RPS section 2",
 "grain": "one row per account per business_date (daily full snapshot)",
 "description": "Account balances (RPS section D2): long/short/net market value, net value plus cash, settled cash, margin, money-market funds, bank sweep, bank cash. Same object size as dim_balance at every partition (identity projection; content identity inferred).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08242234/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 599,
  "partitions": 599,
  "first_partition": "2024-05-24",
  "bytes": 249515573,
  "rows_all_partitions": 3352068,
  "rows_newest_partition": 7555,
  "row_count_rule": "snapshot table: the table row count is the newest partition (7555 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 39,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "account_title_line_1", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_2", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_3", "type": "string", "nullable": true, "pii": true},
  {"name": "acct_regis", "type": "string", "nullable": true},
  {"name": "acct_type", "type": "string", "nullable": true},
  {"name": "net_credit_debit", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "margin_balance", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "available_to_pay", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mrgn_buying_pwr", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "money_mkt_funds", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mtd_margin_int", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "daily_margin_int", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "eqty_excl_option", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "eqty_percentage", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mkt_value_long", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mkt_value_short", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "eqty_incl_option", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "option_rqrmnts", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mnth_end_div_pay", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "maintenance_call", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mvl_cash_ex_optn", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "net_mv_positions", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "net_mv_plus_cash", "type": "decimal128(15, 2)", "nullable": true, "description": "net market value of positions plus cash"},
  {"name": "cash_balance_settled_only", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "cash_margin_bal_settled", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "bank_sweep_ibf", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "bank_cash", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08242234",
   "master_account_name_measured": "49 WEALTH MANAGEMENT LLC",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7555 ids measured length 10)",
   "last4_collisions_within_firm": 1798,
   "accounts_in_collisions": 4056,
   "denominator_accounts": 7555,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "SmartX"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7555 of 7555 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7386,
    "<empty>": 169
   },
   "money_manager_distinct": 2,
   "money_manager_smartx_rows": 7384,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "balances",
  "cash",
  "account value",
  "margin",
  "schwab",
  "49financial",
  "master 08242234"
 ],
 "common_queries": [
  "What is the cash balance of account ...1234?",
  "What is the net market value plus cash of account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none (served only through its dim_ projection via schwab_query)",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "carries client PII columns (flagged pii:true); any tool must project them away (NFRA_OPLGTW forbidden_field_classes: raw_account_id, account_title, tax_identifier, mailing_address)",
  "same object size as dim_balance at every partition (249515573 bytes total both, measured); content identity inferred; one of the two is redundant storage"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 599 parts of schwab/08242234/silver/fact_rps_s2/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08242234_fact_rtu`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08242234_fact_rtu",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08242234/silver/fact_rtu/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rtu",
 "source_feed": "RTU",
 "grain": "one row per tax-lot detail row, cumulative file; MEASURED cadence: quarterly (same dates as fact_rlu)",
 "description": "Tax lot detail (DT section), cumulative.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08242234/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-09-04",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 26,
  "cadence": "quarterly",
  "claim": "measured",
  "note": "judge against the cadence, not T-1: the newest file of a quarterly family is current until the next one is due"
 },
 "size": {
  "objects": 15,
  "partitions": 15,
  "first_partition": "2023-03-03",
  "bytes": 124472049,
  "rows_all_partitions": 1150889,
  "rows_newest_partition": 111948,
  "row_count_rule": "snapshot table: the table row count is the newest partition (111948 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 75,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "closing_date", "type": "date32[day]", "nullable": true, "description": "realized lot closing date"},
  {"name": "closing_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "proceeds", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "proceeds_per_share", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "adjusted_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adjusted_gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_b", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "g_f", "type": "string", "nullable": true},
  {"name": "p_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "lot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adj_disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "publication_timestamp", "type": "string", "nullable": true},
  {"name": "cbm", "type": "string", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "federal_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "wh_st", "type": "string", "nullable": true},
  {"name": "ytd_amortization", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_i", "type": "string", "nullable": true},
  {"name": "settle_date", "type": "date32[day]", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "transaction_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_gain_loss_pct", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "trancode_expanded", "type": "string", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "close_event_id", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08242234",
   "master_account_name_measured": "49 WEALTH MANAGEMENT LLC",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7555 ids measured length 10)",
   "last4_collisions_within_firm": 1798,
   "accounts_in_collisions": 4056,
   "denominator_accounts": 7555,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "SmartX"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7555 of 7555 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7386,
    "<empty>": 169
   },
   "money_manager_distinct": 2,
   "money_manager_smartx_rows": 7384,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "tax lots",
  "tax lot detail",
  "schwab",
  "49financial",
  "master 08242234"
 ],
 "common_queries": [
  "What is the cumulative tax lot detail of account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_tax_lot_detail",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "SmartX",
    "as_of": "YYYY-MM-DD",
    "period": "cumulative"
   },
   "returns": "tax-lot detail rows of the newest quarterly file at or before as_of",
   "answers": [
    "What is the cumulative tax lot detail of account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 15 parts of schwab/08242234/silver/fact_rtu/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08242234_fact_rty`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08242234_fact_rty",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08242234/silver/fact_rty/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rty",
 "source_feed": "RTY",
 "grain": "one row per tax-lot detail row, year-to-date file; MEASURED cadence: month-end (same dates as fact_rly)",
 "description": "Tax lot detail (DT section), yearly.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08242234/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-09-30",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 9,
  "cadence": "month-end",
  "claim": "measured",
  "note": "judge against the cadence, not T-1: the newest file of a month-end family is current until the next one is due"
 },
 "size": {
  "objects": 45,
  "partitions": 45,
  "first_partition": "2023-01-31",
  "bytes": 270728318,
  "rows_all_partitions": 2486669,
  "rows_newest_partition": 113595,
  "row_count_rule": "snapshot table: the table row count is the newest partition (113595 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 75,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "closing_date", "type": "date32[day]", "nullable": true, "description": "realized lot closing date"},
  {"name": "closing_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "proceeds", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "proceeds_per_share", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "adjusted_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adjusted_gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_b", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "g_f", "type": "string", "nullable": true},
  {"name": "p_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "lot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adj_disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "publication_timestamp", "type": "string", "nullable": true},
  {"name": "cbm", "type": "string", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "federal_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "wh_st", "type": "string", "nullable": true},
  {"name": "ytd_amortization", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_i", "type": "string", "nullable": true},
  {"name": "settle_date", "type": "date32[day]", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "transaction_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_gain_loss_pct", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "trancode_expanded", "type": "string", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "close_event_id", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08242234",
   "master_account_name_measured": "49 WEALTH MANAGEMENT LLC",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7555 ids measured length 10)",
   "last4_collisions_within_firm": 1798,
   "accounts_in_collisions": 4056,
   "denominator_accounts": 7555,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "SmartX"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7555 of 7555 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7386,
    "<empty>": 169
   },
   "money_manager_distinct": 2,
   "money_manager_smartx_rows": 7384,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "tax lots",
  "tax lot detail",
  "year-to-date",
  "schwab",
  "49financial",
  "master 08242234"
 ],
 "common_queries": [
  "What is the year-to-date tax lot detail of account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_tax_lot_detail",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "SmartX",
    "as_of": "YYYY-MM-DD",
    "period": "ytd"
   },
   "returns": "tax-lot detail rows of the newest month-end file at or before as_of",
   "answers": [
    "What is the year-to-date tax lot detail of account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 45 parts of schwab/08242234/silver/fact_rty/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08242234_fact_sec`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08242234_fact_sec",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08242234/silver/fact_sec/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_sec",
 "source_feed": "SEC",
 "grain": "one row per security (cusip) per business_date (daily snapshot of the security master; 24 of 2,540 cusips repeat on 08335338 2026-10-13)",
 "description": "Security master: symbols, ISIN/SEDOL, description lines, product codes, prices, factors, rates, maturity, option fields, ratings.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08242234/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 690,
  "partitions": 690,
  "first_partition": "2024-01-16",
  "bytes": 183546254,
  "rows_all_partitions": 1583297,
  "rows_newest_partition": 2197,
  "row_count_rule": "snapshot table: the table row count is the newest partition (2197 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 74,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ly_st", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "reorg_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "rulst_sufid", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "security_description_line_1", "type": "string", "nullable": true},
  {"name": "security_description_line_2", "type": "string", "nullable": true},
  {"name": "security_description_line_3", "type": "string", "nullable": true},
  {"name": "scrtydes_line_4", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlying_industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "unrul_sufid", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "mnymk_code", "type": "string", "nullable": true},
  {"name": "last_update", "type": "date32[day]", "nullable": true},
  {"name": "s_f", "type": "string", "nullable": true},
  {"name": "closing_price", "type": "decimal128(16, 5)", "nullable": true, "description": "custodian per-share close (never additive)"},
  {"name": "secprice_lstupdte", "type": "date32[day]", "nullable": true},
  {"name": "security_valuation_unit", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "optnrt_symbol", "type": "string", "nullable": true},
  {"name": "opt_expr_date", "type": "string", "nullable": true},
  {"name": "c_p", "type": "string", "nullable": true},
  {"name": "strike_price", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "interest_rate", "type": "decimal128(7, 5)", "nullable": true},
  {"name": "maturity_date", "type": "date32[day]", "nullable": true},
  {"name": "tips_factor", "type": "decimal128(18, 9)", "nullable": true},
  {"name": "asset_backed_factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "face_value_amt", "type": "decimal128(13, 4)", "nullable": true},
  {"name": "st_cd", "type": "string", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "p_i", "type": "string", "nullable": true},
  {"name": "o_i", "type": "string", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "closing_price_unfactored", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "factor_date", "type": "date32[day]", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "call_date", "type": "date32[day]", "nullable": true},
  {"name": "call_price", "type": "decimal128(36, 18)", "nullable": true},
  {"name": "issue_date", "type": "date32[day]", "nullable": true},
  {"name": "1st_cpn_date", "type": "date32[day]", "nullable": true},
  {"name": "options_multiplier", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "dividend_interest_frequency", "type": "string", "nullable": true},
  {"name": "s_p_rating", "type": "string", "nullable": true},
  {"name": "moodys_rating", "type": "string", "nullable": true},
  {"name": "next_pay_date", "type": "date32[day]", "nullable": true},
  {"name": "next_put_date", "type": "date32[day]", "nullable": true},
  {"name": "next_put_price", "type": "decimal128(36, 18)", "nullable": true},
  {"name": "mkt_code", "type": "string", "nullable": true},
  {"name": "par_value", "type": "decimal128(36, 18)", "nullable": true},
  {"name": "is_cy", "type": "string", "nullable": true},
  {"name": "cy_is", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08242234",
   "master_account_name_measured": "49 WEALTH MANAGEMENT LLC",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "none (security grain)",
   "last4_derivation": "n/a",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "SmartX"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7555 of 7555 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7386,
    "<empty>": 169
   },
   "money_manager_distinct": 2,
   "money_manager_smartx_rows": 7384,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "security master",
  "cusip",
  "ticker",
  "description",
  "price",
  "schwab",
  "49financial",
  "master 08242234"
 ],
 "common_queries": [
  "What is the ticker and description of CUSIP X?",
  "What is the Schwab closing price of CUSIP X?"
 ],
 "existing_gateway_tool": {
  "name": "none (served only through its dim_ projection via schwab_query)",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 690 parts of schwab/08242234/silver/fact_sec/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08242234_fact_trn`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08242234_fact_trn",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08242234/silver/fact_trn/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_trn",
 "source_feed": "TRN",
 "grain": "one row per transaction line per business_date (daily APPEND, no row-unique key)",
 "description": "Transactions, vendor-complete: trade/settle dates, transaction codes (tr_cd, sb_cd, tran_srcde), quantity, price, gross and net amount, fees, withholding.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08242234/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 690,
  "partitions": 690,
  "first_partition": "2024-01-16",
  "bytes": 212504497,
  "rows_all_partitions": 3778943,
  "rows_newest_partition": 11827,
  "row_count_rule": "event/append table: rows sum across partitions",
  "schema_variants": 1,
  "columns_union": 140,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "account_title_line_1", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_2", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_3", "type": "string", "nullable": true, "pii": true},
  {"name": "acct_regis", "type": "string", "nullable": true},
  {"name": "acct_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ly_st", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "rulst_sufid", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlying_industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "unrul_sufid", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "mnymk_code", "type": "string", "nullable": true},
  {"name": "tr_cd", "type": "string", "nullable": true},
  {"name": "sb_cd", "type": "string", "nullable": true},
  {"name": "transaction_category", "type": "string", "nullable": true},
  {"name": "tran_srcde", "type": "string", "nullable": true},
  {"name": "transaction_source_code_description", "type": "string", "nullable": true},
  {"name": "transaction_detail_description", "type": "string", "nullable": true},
  {"name": "trade_typcd", "type": "string", "nullable": true},
  {"name": "t_c", "type": "string", "nullable": true},
  {"name": "trade_date", "type": "date32[day]", "nullable": true},
  {"name": "settlmnt_date", "type": "date32[day]", "nullable": true},
  {"name": "tran_date", "type": "date32[day]", "nullable": true},
  {"name": "exdivdnd_date", "type": "date32[day]", "nullable": true},
  {"name": "quantity", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "price", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "gross_amount", "type": "decimal128(15, 2)", "nullable": true, "description": "the money of a transaction (IRPT money law: never net_amount)"},
  {"name": "debit_credit", "type": "string", "nullable": true},
  {"name": "net_amount", "type": "decimal128(15, 2)", "nullable": true, "description": "net amount (reads 0.00 on cash rows; not the money)"},
  {"name": "commission", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "exchange_processing_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "broker_service_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "prime_broker_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "trade_away_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "redemption_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "other_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "federal_tefra_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "st_tx", "type": "string", "nullable": true},
  {"name": "accrued_interest", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "accounting_rule_code", "type": "string", "nullable": true},
  {"name": "ordr_srcd", "type": "string", "nullable": true},
  {"name": "order_number", "type": "string", "nullable": true},
  {"name": "trade_order_entry_tm_stmp", "type": "string", "nullable": true},
  {"name": "trade_order_exectn_tm_stmp", "type": "string", "nullable": true},
  {"name": "broker_code", "type": "string", "nullable": true},
  {"name": "broker_name", "type": "string", "nullable": true},
  {"name": "swb_from_account", "type": "string", "nullable": true},
  {"name": "swb_to_account", "type": "string", "nullable": true},
  {"name": "s1_check_number", "type": "string", "nullable": true},
  {"name": "s_i", "type": "string", "nullable": true},
  {"name": "stock_exchg", "type": "string", "nullable": true},
  {"name": "i_e", "type": "string", "nullable": true},
  {"name": "distribution_rate", "type": "decimal128(15, 8)", "nullable": true},
  {"name": "cash_in_lieu_share_quantity", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "dividend_interest_share_quantity", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "cash_in_lieu_rate", "type": "decimal128(15, 8)", "nullable": true},
  {"name": "asset_backed_factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "sr_sy", "type": "string", "nullable": true},
  {"name": "jn_tp", "type": "string", "nullable": true},
  {"name": "d_m", "type": "string", "nullable": true},
  {"name": "schwab_cashiering_unique_id", "type": "string", "nullable": true},
  {"name": "recipient_maker_name_line_1", "type": "string", "nullable": true},
  {"name": "recipient_maker_name_line_2", "type": "string", "nullable": true},
  {"name": "recipient_maker_name_line_3", "type": "string", "nullable": true},
  {"name": "frequency", "type": "string", "nullable": true},
  {"name": "disburse_check_number", "type": "string", "nullable": true},
  {"name": "federal_bank_reference_number", "type": "string", "nullable": true},
  {"name": "recipient_maker_acct_number", "type": "string", "nullable": true},
  {"name": "bank_act_typ", "type": "string", "nullable": true},
  {"name": "bank_name_part_1", "type": "string", "nullable": true},
  {"name": "bank_name_part_2", "type": "string", "nullable": true},
  {"name": "bank_aba", "type": "string", "nullable": true},
  {"name": "intermediary_name", "type": "string", "nullable": true},
  {"name": "transaction_check_memo_1", "type": "string", "nullable": true},
  {"name": "transaction_check_memo_2", "type": "string", "nullable": true},
  {"name": "retirement_fed_income_tax", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "retirement_state_income_tax", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "rt_tx", "type": "string", "nullable": true},
  {"name": "publication_time_stamp", "type": "string", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "tips_factor", "type": "decimal128(18, 9)", "nullable": true},
  {"name": "closing_price", "type": "decimal128(16, 5)", "nullable": true, "description": "custodian per-share close (never additive)"},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "transaction_memo", "type": "string", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "closing_price_unfactored", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "factor_date", "type": "date32[day]", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "step_in_fee", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "markupmarkdown", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "research_fee", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "exec_brok_comm", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "order_id", "type": "string", "nullable": true},
  {"name": "record_date", "type": "date32[day]", "nullable": true},
  {"name": "payable_date", "type": "date32[day]", "nullable": true},
  {"name": "accstart_date", "type": "string", "nullable": true},
  {"name": "accrend_date", "type": "string", "nullable": true},
  {"name": "d_f", "type": "string", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "yield_to_call", "type": "decimal128(8, 7)", "nullable": true},
  {"name": "yield_to_maturity", "type": "decimal128(8, 7)", "nullable": true},
  {"name": "trust_princ", "type": "decimal128(5, 2)", "nullable": true},
  {"name": "trust_income", "type": "decimal128(5, 2)", "nullable": true},
  {"name": "tax_cd", "type": "string", "nullable": true},
  {"name": "r_dc", "type": "string", "nullable": true},
  {"name": "r_cc", "type": "string", "nullable": true},
  {"name": "r_cy", "type": "string", "nullable": true},
  {"name": "cycle_id", "type": "string", "nullable": true},
  {"name": "tran_randm", "type": "decimal128(5, 0)", "nullable": true},
  {"name": "tranproc_date", "type": "date32[day]", "nullable": true},
  {"name": "cashiering_transaction_identifier", "type": "string", "nullable": true},
  {"name": "transaction_memo_or_wire_instructions", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08242234",
   "master_account_name_measured": "49 WEALTH MANAGEMENT LLC",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7555 ids measured length 10)",
   "last4_collisions_within_firm": 1798,
   "accounts_in_collisions": 4056,
   "denominator_accounts": 7555,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "SmartX"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7555 of 7555 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7386,
    "<empty>": 169
   },
   "money_manager_distinct": 2,
   "money_manager_smartx_rows": 7384,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "transactions",
  "trades",
  "flows",
  "deposits",
  "withdrawals",
  "fees",
  "schwab",
  "49financial",
  "master 08242234"
 ],
 "common_queries": [
  "What transactions did account ...1234 have on a date?",
  "What deposits and withdrawals did account ...1234 have this month?"
 ],
 "existing_gateway_tool": {
  "name": "none (served only through its dim_ projection via schwab_query)",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "carries client PII columns (flagged pii:true); any tool must project them away (NFRA_OPLGTW forbidden_field_classes: raw_account_id, account_title, tax_identifier, mailing_address)"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 690 parts of schwab/08242234/silver/fact_trn/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08242234_fact_uln`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08242234_fact_uln",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08242234/silver/fact_uln/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_uln",
 "source_feed": "ULN",
 "grain": "one row per account x open lot (event_id) per business_date (daily full snapshot; 0 duplicate account+event_id on 08335338 2026-10-13)",
 "description": "Unrealized lots, long and short (the non-taxable slice per the 49-schwab-conv skill): acquired date, quantity, cost basis, market value, unrealized gain, holding term. IRPT_DASHBD lot_source unrealized table.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08242234/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 691,
  "partitions": 691,
  "first_partition": "2024-01-12",
  "bytes": 6502529828,
  "rows_all_partitions": 97982104,
  "rows_newest_partition": 309551,
  "row_count_rule": "snapshot table: the table row count is the newest partition (309551 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 61,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "current_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "current_market_value", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "accrued_interest", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "orgpurch_date", "type": "date32[day]", "nullable": true},
  {"name": "org_purchase_price", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "yield_tomaturity", "type": "decimal128(11, 9)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "unrealized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "c_b", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "dflot_selct", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "g_i", "type": "string", "nullable": true},
  {"name": "original_cost_basis", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "adjusted_cost_incldg_unpd_amort", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "event_id", "type": "string", "nullable": true, "description": "lot id"},
  {"name": "c_v", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08242234",
   "master_account_name_measured": "49 WEALTH MANAGEMENT LLC",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7555 ids measured length 10)",
   "last4_collisions_within_firm": 1798,
   "accounts_in_collisions": 4056,
   "denominator_accounts": 7555,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "SmartX"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7555 of 7555 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7386,
    "<empty>": 169
   },
   "money_manager_distinct": 2,
   "money_manager_smartx_rows": 7384,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "unrealized lots",
  "cost basis",
  "unrealized gain",
  "tax lots",
  "schwab",
  "49financial",
  "master 08242234"
 ],
 "common_queries": [
  "What are the open lots and unrealized gain of account ...1234?",
  "What is the cost basis of CUSIP X in account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_unrealized_lots",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "SmartX",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "open lots (event_id, cusip, ticker, acquired_date, quantity, cost_basis_unamortized, current_market_value, unrealized_gain_loss, h_t) from a NEW projection dim_lot_unrealized over fact_uln + fact_ult with a slice column",
   "answers": [
    "What are the open lots and unrealized gain of account ...1234?",
    "What is the cost basis of CUSIP X in account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 691 parts of schwab/08242234/silver/fact_uln/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08242234_fact_ult`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08242234_fact_ult",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08242234/silver/fact_ult/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_ult",
 "source_feed": "ULT",
 "grain": "one row per account x open lot per business_date (daily full snapshot)",
 "description": "Unrealized lot detail, the TAXABLE (brokerage) slice; identical layout to fact_uln. IRPT_DASHBD lot_source unrealized table; the legacy B_02.canonical_lots input.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08242234/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 691,
  "partitions": 691,
  "first_partition": "2024-01-12",
  "bytes": 5716907756,
  "rows_all_partitions": 77641344,
  "rows_newest_partition": 219969,
  "row_count_rule": "snapshot table: the table row count is the newest partition (219969 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 61,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "current_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "current_market_value", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "accrued_interest", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "orgpurch_date", "type": "date32[day]", "nullable": true},
  {"name": "org_purchase_price", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "yield_tomaturity", "type": "decimal128(11, 9)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "unrealized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "c_b", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "dflot_selct", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "g_i", "type": "string", "nullable": true},
  {"name": "original_cost_basis", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "adjusted_cost_incldg_unpd_amort", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "event_id", "type": "string", "nullable": true, "description": "lot id"},
  {"name": "c_v", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08242234",
   "master_account_name_measured": "49 WEALTH MANAGEMENT LLC",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7555 ids measured length 10)",
   "last4_collisions_within_firm": 1798,
   "accounts_in_collisions": 4056,
   "denominator_accounts": 7555,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "SmartX"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7555 of 7555 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7386,
    "<empty>": 169
   },
   "money_manager_distinct": 2,
   "money_manager_smartx_rows": 7384,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "unrealized lots",
  "taxable lots",
  "cost basis",
  "unrealized gain",
  "schwab",
  "49financial",
  "master 08242234"
 ],
 "common_queries": [
  "What is the unrealized short-term vs long-term gain of account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_unrealized_lots",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "SmartX",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "as fact_uln (same tool, slice=taxable)",
   "answers": [
    "What is the unrealized short-term vs long-term gain of account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 691 parts of schwab/08242234/silver/fact_ult/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08242234_fact_upn`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08242234_fact_upn",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08242234/silver/fact_upn/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_upn",
 "source_feed": "UPN",
 "grain": "one row per account x position per business_date (DP section; semantics inferred from the dictionary: \"position (pending?)\")",
 "description": "Unrealized-position (DP section) file, non-taxable slice; meaning not vendor-confirmed (data dictionary 2a marks it with a question mark).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08242234/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 691,
  "partitions": 691,
  "first_partition": "2024-01-12",
  "bytes": 861144165,
  "rows_all_partitions": 27315315,
  "rows_newest_partition": 64995,
  "row_count_rule": "snapshot table: the table row count is the newest partition (64995 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 44,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "current_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "current_market_value", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "accrued_interest", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "unrealized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "c_b", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "dflot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "principal_paydown_factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08242234",
   "master_account_name_measured": "49 WEALTH MANAGEMENT LLC",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7555 ids measured length 10)",
   "last4_collisions_within_firm": 1798,
   "accounts_in_collisions": 4056,
   "denominator_accounts": 7555,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "SmartX"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7555 of 7555 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7386,
    "<empty>": 169
   },
   "money_manager_distinct": 2,
   "money_manager_smartx_rows": 7384,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "positions",
  "unrealized positions",
  "schwab",
  "49financial",
  "master 08242234"
 ],
 "common_queries": [
  "What unrealized position records does account ...1234 carry?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none",
  "note": "semantics not vendor-confirmed; no tool until the dictionary row binds"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 691 parts of schwab/08242234/silver/fact_upn/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08242234_fact_upt`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08242234_fact_upt",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08242234/silver/fact_upt/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_upt",
 "source_feed": "UPT",
 "grain": "one row per account x position per business_date (DP section; semantics inferred)",
 "description": "Unrealized-position (DP section) file, taxable slice; meaning not vendor-confirmed.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08242234/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 691,
  "partitions": 691,
  "first_partition": "2024-01-12",
  "bytes": 690656000,
  "rows_all_partitions": 17374902,
  "rows_newest_partition": 40291,
  "row_count_rule": "snapshot table: the table row count is the newest partition (40291 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 44,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "current_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "current_market_value", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "accrued_interest", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "unrealized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "c_b", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "dflot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "principal_paydown_factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08242234",
   "master_account_name_measured": "49 WEALTH MANAGEMENT LLC",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7555 ids measured length 10)",
   "last4_collisions_within_firm": 1798,
   "accounts_in_collisions": 4056,
   "denominator_accounts": 7555,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "SmartX"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7555 of 7555 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7386,
    "<empty>": 169
   },
   "money_manager_distinct": 2,
   "money_manager_smartx_rows": 7384,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "positions",
  "unrealized positions",
  "taxable",
  "schwab",
  "49financial",
  "master 08242234"
 ],
 "common_queries": [
  "What unrealized taxable position records does account ...1234 carry?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none",
  "note": "semantics not vendor-confirmed; no tool until the dictionary row binds"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 691 parts of schwab/08242234/silver/fact_upt/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_dim_asset`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_dim_asset",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/dim_asset/",
 "layer": "silver",
 "format": "parquet",
 "table": "dim_asset",
 "source_feed": "SEC projection",
 "grain": "one row per cusip per business_date (24-column projection of fact_sec)",
 "description": "Gateway-served security master projection (dataset dim_asset).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 571,
  "partitions": 571,
  "first_partition": "2024-07-08",
  "bytes": 102741623,
  "rows_all_partitions": 1337865,
  "rows_newest_partition": 2540,
  "row_count_rule": "snapshot table: the table row count is the newest partition (2540 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 29,
  "claim": "measured"
 },
 "columns": [
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "security_description_line_1", "type": "string", "nullable": true},
  {"name": "security_description_line_2", "type": "string", "nullable": true},
  {"name": "security_description_line_3", "type": "string", "nullable": true},
  {"name": "scrtydes_line_4", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "mnymk_code", "type": "string", "nullable": true},
  {"name": "closing_price", "type": "decimal128(16, 5)", "nullable": true, "description": "custodian per-share close (never additive)"},
  {"name": "closing_price_unfactored", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "par_value", "type": "decimal128(36, 18)", "nullable": true},
  {"name": "interest_rate", "type": "decimal128(7, 5)", "nullable": true},
  {"name": "maturity_date", "type": "date32[day]", "nullable": true},
  {"name": "strike_price", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "c_p", "type": "string", "nullable": true},
  {"name": "opt_expr_date", "type": "string", "nullable": true},
  {"name": "s_p_rating", "type": "string", "nullable": true},
  {"name": "moodys_rating", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "none (security grain)",
   "last4_derivation": "n/a",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "security master",
  "cusip",
  "ticker",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "What is the ticker and description of a Schwab security by cusip?"
 ],
 "existing_gateway_tool": {
  "name": "schwab_query (+ schwab_list_files, schwab_describe_dataset, schwab_get_access, schwab_prepare_download)",
  "verdict": "extend",
  "note": "keep the typed query; extend with last-4 resolution, history beyond the 30-day rolling window (DATA_CATALOG.yaml:2639 and :2654 mark PARTIAL), and the fork inputs"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_security",
   "inputs": {
    "firm": "49financial",
    "account_last4": "n/a (security grain)",
    "platform": "BlackDiamond",
    "as_of": "YYYY-MM-DD",
    "cusip_or_ticker": "<cusip|ticker>"
   },
   "returns": "one dim_asset row",
   "answers": [
    "What is the ticker and description of a Schwab security by cusip?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "silver_datasets.schwab_dim_asset",
  "present": true,
  "line": 2404
 },
 "prior_art": "org/standards/NFRA_OPLGTW_CONTRACT.json v1.4 (dataset dim_asset); data/assets/scripts/silver/schwab_projections.py PROJECTIONS; docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 571 parts of schwab/08335338/silver/dim_asset/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_dim_balance`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_dim_balance",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/dim_balance/",
 "layer": "silver",
 "format": "parquet",
 "table": "dim_balance",
 "source_feed": "RPS section 2 projection",
 "grain": "one row per account per business_date (identity projection of fact_rps_s2)",
 "description": "Gateway-served balances projection (dataset dim_balance).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 571,
  "partitions": 571,
  "first_partition": "2024-07-08",
  "bytes": 243753657,
  "rows_all_partitions": 3291921,
  "rows_newest_partition": 7646,
  "row_count_rule": "snapshot table: the table row count is the newest partition (7646 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 39,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "account_title_line_1", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_2", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_3", "type": "string", "nullable": true, "pii": true},
  {"name": "acct_regis", "type": "string", "nullable": true},
  {"name": "acct_type", "type": "string", "nullable": true},
  {"name": "net_credit_debit", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "margin_balance", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "available_to_pay", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mrgn_buying_pwr", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "money_mkt_funds", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mtd_margin_int", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "daily_margin_int", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "eqty_excl_option", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "eqty_percentage", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mkt_value_long", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mkt_value_short", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "eqty_incl_option", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "option_rqrmnts", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mnth_end_div_pay", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "maintenance_call", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mvl_cash_ex_optn", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "net_mv_positions", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "net_mv_plus_cash", "type": "decimal128(15, 2)", "nullable": true, "description": "net market value of positions plus cash"},
  {"name": "cash_balance_settled_only", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "cash_margin_bal_settled", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "bank_sweep_ibf", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "bank_cash", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7646 ids measured length 10)",
   "last4_collisions_within_firm": 1842,
   "accounts_in_collisions": 4156,
   "denominator_accounts": 7646,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "balances",
  "cash",
  "account value",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "What is the cash balance and net market value of account ...1234 on a date?"
 ],
 "existing_gateway_tool": {
  "name": "schwab_query (+ schwab_list_files, schwab_describe_dataset, schwab_get_access, schwab_prepare_download)",
  "verdict": "extend",
  "note": "keep the typed query; extend with last-4 resolution, history beyond the 30-day rolling window (DATA_CATALOG.yaml:2639 and :2654 mark PARTIAL), and the fork inputs"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_balances",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "BlackDiamond",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "one dim_balance row per resolved account_ref for as_of",
   "answers": [
    "What is the cash balance and net market value of account ...1234 on a date?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "silver_datasets.schwab_dim_balance",
  "present": true,
  "line": 2426
 },
 "prior_art": "org/standards/NFRA_OPLGTW_CONTRACT.json v1.4 (dataset dim_balance); data/assets/scripts/silver/schwab_projections.py PROJECTIONS; docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b; data/assets/scripts/gold/irpt_reporting/sources.json schwab_08335338 (IRPT_DASHBD contracts read this table) @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 571 parts of schwab/08335338/silver/dim_balance/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_dim_position`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_dim_position",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/dim_position/",
 "layer": "silver",
 "format": "parquet",
 "table": "dim_position",
 "source_feed": "RPS projection",
 "grain": "one row per account x cusip x l_s per business_date (25-column projection of fact_rps, row parity enforced)",
 "description": "Gateway-served positions projection (contract NFRA_OPLGTW v1.4 dataset dim_position).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 571,
  "partitions": 571,
  "first_partition": "2024-07-08",
  "bytes": 829274478,
  "rows_all_partitions": 39663401,
  "rows_newest_partition": 110454,
  "row_count_rule": "snapshot table: the table row count is the newest partition (110454 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 30,
  "claim": "measured"
 },
 "columns": [
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "accounting_rule_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "quantity_settled_unsettled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_unsettled_long", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_unsettled_short", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_cash_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_margin_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_short_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_wheniss_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "non_tradable_quantity", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "market_value_settled_unsettled", "type": "decimal128(17, 4)", "nullable": true, "description": "position market value (additive; short rows negative)"},
  {"name": "closing_price", "type": "decimal128(16, 5)", "nullable": true, "description": "custodian per-share close (never additive)"},
  {"name": "closing_price_unfactored", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "asset_backed_factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "secprice_lstupdte", "type": "date32[day]", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7646 ids measured length 10)",
   "last4_collisions_within_firm": 1842,
   "accounts_in_collisions": 4156,
   "denominator_accounts": 7646,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "positions",
  "holdings",
  "positions by account",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "What does account ...1234 hold today?",
  "What is the market value of a security in account ...1234 on a date?"
 ],
 "existing_gateway_tool": {
  "name": "schwab_query (+ schwab_list_files, schwab_describe_dataset, schwab_get_access, schwab_prepare_download)",
  "verdict": "extend",
  "note": "keep the typed query; extend with last-4 resolution, history beyond the 30-day rolling window (DATA_CATALOG.yaml:2639 and :2654 mark PARTIAL), and the fork inputs"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_positions",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "BlackDiamond",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "rows of dim_position for the resolved account_ref(s) on the business_date at or before as_of; a last-4 that matches several accounts returns the candidate list, never a merge",
   "answers": [
    "What does account ...1234 hold today?",
    "What is the market value of a security in account ...1234 on a date?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "silver_datasets.schwab_dim_position",
  "present": true,
  "line": 2450
 },
 "prior_art": "org/standards/NFRA_OPLGTW_CONTRACT.json v1.4 (dataset dim_position); data/assets/scripts/silver/schwab_projections.py PROJECTIONS; docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b; data/assets/scripts/gold/irpt_reporting/sources.json schwab_08335338 (IRPT_DASHBD contracts read this table) @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 571 parts of schwab/08335338/silver/dim_position/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_dim_transaction`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_dim_transaction",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/dim_transaction/",
 "layer": "silver",
 "format": "parquet",
 "table": "dim_transaction",
 "source_feed": "TRN projection",
 "grain": "one row per transaction line per business_date (39-column projection of fact_trn; append, no row-unique key)",
 "description": "Gateway-served transactions projection (dataset dim_transaction).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 571,
  "partitions": 571,
  "first_partition": "2024-07-08",
  "bytes": 71374312,
  "rows_all_partitions": 3339973,
  "rows_newest_partition": 11906,
  "row_count_rule": "event/append table: rows sum across partitions",
  "schema_variants": 1,
  "columns_union": 44,
  "claim": "measured"
 },
 "columns": [
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "trade_date", "type": "date32[day]", "nullable": true},
  {"name": "settlmnt_date", "type": "date32[day]", "nullable": true},
  {"name": "tran_date", "type": "date32[day]", "nullable": true},
  {"name": "tr_cd", "type": "string", "nullable": true},
  {"name": "sb_cd", "type": "string", "nullable": true},
  {"name": "transaction_category", "type": "string", "nullable": true},
  {"name": "tran_srcde", "type": "string", "nullable": true},
  {"name": "transaction_source_code_description", "type": "string", "nullable": true},
  {"name": "transaction_detail_description", "type": "string", "nullable": true},
  {"name": "debit_credit", "type": "string", "nullable": true},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "quantity", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "price", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "gross_amount", "type": "decimal128(15, 2)", "nullable": true, "description": "the money of a transaction (IRPT money law: never net_amount)"},
  {"name": "net_amount", "type": "decimal128(15, 2)", "nullable": true, "description": "net amount (reads 0.00 on cash rows; not the money)"},
  {"name": "accrued_interest", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "commission", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "prime_broker_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "trade_away_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "redemption_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "other_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "step_in_fee", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "research_fee", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "exec_brok_comm", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "broker_service_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "exchange_processing_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "federal_tefra_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "retirement_fed_income_tax", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "retirement_state_income_tax", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "closing_price", "type": "decimal128(16, 5)", "nullable": true, "description": "custodian per-share close (never additive)"},
  {"name": "factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7646 ids measured length 10)",
   "last4_collisions_within_firm": 1842,
   "accounts_in_collisions": 4156,
   "denominator_accounts": 7646,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "transactions",
  "trades",
  "flows",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "What transactions did account ...1234 have on a date?"
 ],
 "existing_gateway_tool": {
  "name": "schwab_query (+ schwab_list_files, schwab_describe_dataset, schwab_get_access, schwab_prepare_download)",
  "verdict": "extend",
  "note": "keep the typed query; extend with last-4 resolution, history beyond the 30-day rolling window (DATA_CATALOG.yaml:2639 and :2654 mark PARTIAL), and the fork inputs"
 },
 "proposed_tools": [
  {
   "name": "schwab_list_transactions",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "BlackDiamond",
    "as_of": "YYYY-MM-DD or start..end (<= 31 business dates)"
   },
   "returns": "dim_transaction rows by business_date for the resolved account_ref(s); row identity is (partition, row position)",
   "answers": [
    "What transactions did account ...1234 have on a date?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "silver_datasets.schwab_dim_transaction",
  "present": true,
  "line": 2474
 },
 "prior_art": "org/standards/NFRA_OPLGTW_CONTRACT.json v1.4 (dataset dim_transaction); data/assets/scripts/silver/schwab_projections.py PROJECTIONS; docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 571 parts of schwab/08335338/silver/dim_transaction/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_fact_acc`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_fact_acc",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/fact_acc/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_acc",
 "source_feed": "ACC",
 "grain": "one row per account per business_date (daily full snapshot of the master account file)",
 "description": "Account master: identity, registration, account type, status, open date, platform and money manager, and the client PII the vendor sends (title lines, taxpayer, address, contact, SSN/TIN, DOB).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 571,
  "partitions": 571,
  "first_partition": "2024-07-08",
  "bytes": 333904100,
  "rows_all_partitions": 3291738,
  "rows_newest_partition": 7646,
  "row_count_rule": "snapshot table: the table row count is the newest partition (7646 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 95,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "account_title_line_1", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_2", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_3", "type": "string", "nullable": true, "pii": true},
  {"name": "account_status", "type": "string", "nullable": true},
  {"name": "acct_regis", "type": "string", "nullable": true},
  {"name": "acct_type", "type": "string", "nullable": true},
  {"name": "txpyr_title", "type": "string", "nullable": true, "pii": true},
  {"name": "taxpayer_first_name", "type": "string", "nullable": true, "pii": true},
  {"name": "taxpayer_middle_name", "type": "string", "nullable": true, "pii": true},
  {"name": "taxpayer_last_name", "type": "string", "nullable": true, "pii": true},
  {"name": "txpyr_suff", "type": "string", "nullable": true, "pii": true},
  {"name": "wh_cd", "type": "string", "nullable": true},
  {"name": "primary_contact", "type": "string", "nullable": true, "pii": true},
  {"name": "alias_name", "type": "string", "nullable": true, "pii": true},
  {"name": "mailing_address_line_1", "type": "string", "nullable": true, "pii": true},
  {"name": "mailing_address_line_2", "type": "string", "nullable": true, "pii": true},
  {"name": "mailing_address_line_3", "type": "string", "nullable": true, "pii": true},
  {"name": "account_mailing_city", "type": "string", "nullable": true, "pii": true},
  {"name": "ac_st", "type": "string", "nullable": true},
  {"name": "acct_mail_zip", "type": "string", "nullable": true, "pii": true},
  {"name": "acct_mailing_ctry_code", "type": "string", "nullable": true, "pii": true},
  {"name": "email_address", "type": "string", "nullable": true, "pii": true},
  {"name": "phone_nbr", "type": "string", "nullable": true, "pii": true},
  {"name": "business_ph", "type": "string", "nullable": true, "pii": true},
  {"name": "date_opened", "type": "date32[day]", "nullable": true},
  {"name": "schwab_br_cd", "type": "string", "nullable": true},
  {"name": "s_s", "type": "string", "nullable": true},
  {"name": "ac_cs", "type": "string", "nullable": true},
  {"name": "ac_ma", "type": "string", "nullable": true},
  {"name": "m_a", "type": "string", "nullable": true},
  {"name": "a_r", "type": "string", "nullable": true},
  {"name": "a_m", "type": "string", "nullable": true},
  {"name": "nr_am", "type": "string", "nullable": true},
  {"name": "a_o", "type": "string", "nullable": true},
  {"name": "b_f", "type": "string", "nullable": true},
  {"name": "nr_bn", "type": "string", "nullable": true},
  {"name": "p_c", "type": "string", "nullable": true},
  {"name": "p_d", "type": "string", "nullable": true},
  {"name": "p_b", "type": "string", "nullable": true},
  {"name": "u_m", "type": "string", "nullable": true},
  {"name": "f_a", "type": "string", "nullable": true},
  {"name": "intbr_cd", "type": "string", "nullable": true},
  {"name": "intbr_mm_cd", "type": "string", "nullable": true},
  {"name": "intbearing_ticker_symbol", "type": "string", "nullable": true},
  {"name": "intbearing_feat_is_id", "type": "string", "nullable": true},
  {"name": "int_sf", "type": "string", "nullable": true},
  {"name": "p_v", "type": "string", "nullable": true},
  {"name": "p_m", "type": "string", "nullable": true},
  {"name": "statemnt_pref", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "dflt_ltsel", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "cbm_mf", "type": "string", "nullable": true},
  {"name": "cbm_nmf", "type": "string", "nullable": true},
  {"name": "cb_mthd_date", "type": "date32[day]", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "custtype_code", "type": "string", "nullable": true},
  {"name": "organization_primary_name", "type": "string", "nullable": true, "pii": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "rstr_rsn1", "type": "string", "nullable": true},
  {"name": "rstr_rsn2", "type": "string", "nullable": true},
  {"name": "rstr_rsn3", "type": "string", "nullable": true},
  {"name": "rstr_rsn4", "type": "string", "nullable": true},
  {"name": "rstr_rsn5", "type": "string", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "schwab_bank_ic_account", "type": "string", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "ssn_tin_number", "type": "string", "nullable": true, "pii": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "p_e", "type": "string", "nullable": true},
  {"name": "mngdacct_pltfrmcd", "type": "string", "nullable": true, "description": "managed-account platform code (measured values MAM or empty)"},
  {"name": "managed_account_money_manager", "type": "string", "nullable": true, "description": "money manager of a managed account (the SmartX marker)"},
  {"name": "managed_account_investment_strategy", "type": "string", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "bank_sweep_display_name", "type": "string", "nullable": true},
  {"name": "versmrkr_7", "type": "string", "nullable": true},
  {"name": "o_l", "type": "string", "nullable": true},
  {"name": "versmrkr_8", "type": "string", "nullable": true},
  {"name": "date_of_birth", "type": "date32[day]", "nullable": true, "pii": true},
  {"name": "coy_cd", "type": "string", "nullable": true},
  {"name": "st_cd", "type": "string", "nullable": true},
  {"name": "versmrkr_9", "type": "string", "nullable": true},
  {"name": "s_i", "type": "string", "nullable": true},
  {"name": "m_t", "type": "string", "nullable": true},
  {"name": "mobile_phone_number", "type": "string", "nullable": true, "pii": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7646 ids measured length 10)",
   "last4_collisions_within_firm": 1842,
   "accounts_in_collisions": 4156,
   "denominator_accounts": 7646,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "account",
  "account master",
  "registration",
  "account status",
  "money manager",
  "platform",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "Which platform and money manager is account ...1234 on?",
  "Is account ...1234 open or closed, and when was it opened?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_resolve_account",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "BlackDiamond",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "candidate account_refs with master, platform code, money manager, account type and status, from a NEW non-PII projection dim_account of fact_acc (projection law: select only); never title, taxpayer, address, contact, SSN/TIN or DOB",
   "answers": [
    "Which platform and money manager is account ...1234 on?",
    "Is account ...1234 open or closed, and when was it opened?",
    "Which accounts end in 1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b; org/standards/ADVI_BILLING_HOUSEHOLD_CROSSWALK_CONTRACT.json inputs.schwab_universe (newest fact_acc partition) @bc91e712ad",
 "open_items": [
  "carries client PII columns (flagged pii:true); any tool must project them away (NFRA_OPLGTW forbidden_field_classes: raw_account_id, account_title, tax_identifier, mailing_address)"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 571 parts of schwab/08335338/silver/fact_acc/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_fact_fam`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_fact_fam",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/fact_fam/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_fam",
 "source_feed": "FAM (CS identity file)",
 "grain": "one row per account x person (positional CSV, no trailer control)",
 "description": "CS identity file: 7-digit id, institution name, PERSON NAME, 8-digit account number, name/title, 9-digit id, in positional columns col_1..col_6 (naming blocked on the vendor spec). PII. 08335338 only.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-08-10",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 45,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 526,
  "partitions": 526,
  "first_partition": "2024-07-08",
  "bytes": 81024361,
  "rows_all_partitions": 2909996,
  "rows_newest_partition": 7202,
  "row_count_rule": "snapshot table: the table row count is the newest partition (7202 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 11,
  "claim": "measured"
 },
 "columns": [
  {"name": "col_1", "type": "string", "nullable": true, "pii": true},
  {"name": "col_2", "type": "string", "nullable": true, "pii": true},
  {"name": "col_3", "type": "string", "nullable": true, "pii": true},
  {"name": "col_4", "type": "string", "nullable": true, "pii": true},
  {"name": "col_5", "type": "string", "nullable": true, "pii": true},
  {"name": "col_6", "type": "string", "nullable": true, "pii": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "col_4 (positional, 8-digit account number per data dictionary 2b; inferred)",
   "last4_derivation": "absent (positional column, not measured)",
   "last4_collisions_within_firm": null,
   "claim": "inferred"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "account holders",
  "identity",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "Who are the named persons on account ...1234? (PII: not a gateway answer)"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none",
  "note": "PII identity file; no tool proposed"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "feed stopped: newest partition 2026-08-10 (45 trading days behind T-1) and bronze fam newest object 2026-08-11 while fact_slm continues to 2026-10-13; no surprise row filed by this part (write surface is the part file only)",
  "carries client PII columns (flagged pii:true); any tool must project them away (NFRA_OPLGTW forbidden_field_classes: raw_account_id, account_title, tax_identifier, mailing_address)"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 526 parts of schwab/08335338/silver/fact_fam/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_fact_rld`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_fact_rld",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/fact_rld/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rld",
 "source_feed": "RLD",
 "grain": "one row per realized lot closed on the business_date (daily; closing_date = business date on 08335338 2026-10-13)",
 "description": "Realized lots, daily: closing and opening events, quantity, proceeds, cost basis, gain/loss, holding term, order number. The PRIMARY realized-lot tax source (IRPT_DASHBD lot_source realized; legacy B_02).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 819,
  "partitions": 819,
  "first_partition": "2023-07-12",
  "bytes": 137391312,
  "rows_all_partitions": 999184,
  "rows_newest_partition": 6018,
  "row_count_rule": "event/append table: rows sum across partitions",
  "schema_variants": 1,
  "columns_union": 86,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "closing_date", "type": "date32[day]", "nullable": true, "description": "realized lot closing date"},
  {"name": "closing_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "proceeds", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "proceeds_per_share", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "orgpurch_date", "type": "date32[day]", "nullable": true},
  {"name": "original_purchase_price", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "adjusted_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adjusted_gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f_2", "type": "string", "nullable": true},
  {"name": "g_f", "type": "string", "nullable": true},
  {"name": "p_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "lot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adj_disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "publication_timestamp", "type": "string", "nullable": true},
  {"name": "cbm", "type": "string", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "federal_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "wh_st", "type": "string", "nullable": true},
  {"name": "ytd_amortization", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_i", "type": "string", "nullable": true},
  {"name": "settle_date", "type": "date32[day]", "nullable": true},
  {"name": "r_u", "type": "string", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "transaction_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_gain_loss_pct", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "employee_option_original_cost", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "employee_option_realized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "g_i", "type": "string", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "trancode_expanded", "type": "string", "nullable": true},
  {"name": "order_number", "type": "string", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "close_event_id", "type": "string", "nullable": true},
  {"name": "close_open_event_id", "type": "string", "nullable": true},
  {"name": "versmrkr_7", "type": "string", "nullable": true},
  {"name": "schwab_order_id", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7646 ids measured length 10)",
   "last4_collisions_within_firm": 1842,
   "accounts_in_collisions": 4156,
   "denominator_accounts": 7646,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "realized lots",
  "realized gains",
  "tax",
  "capital gains",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "What realized gains did account ...1234 book on a date?",
  "What lots of CUSIP X were sold from account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_realized_lots",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "BlackDiamond",
    "as_of": "YYYY-MM-DD or start..end",
    "period": "daily"
   },
   "returns": "realized lots (closing_date, cusip, ticker, closing_quantity, proceeds, cost_basis_unamortized, gain_loss_dollars, h_t) from a NEW projection dim_lot_realized over fact_rld",
   "answers": [
    "What realized gains did account ...1234 book on a date?",
    "What lots of CUSIP X were sold from account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b; data/assets/scripts/gold/irpt_reporting/sources.json schwab_08335338 (IRPT_DASHBD contracts read this table) @bc91e712ad",
 "open_items": [
  "1 of 819 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 819 parts of schwab/08335338/silver/fact_rld/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_fact_rlu`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_fact_rlu",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/fact_rlu/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rlu",
 "source_feed": "RLU",
 "grain": "one row per realized lot, cumulative file; MEASURED cadence: quarterly (2023-03-03, 06-02, 09-01 ... 2026-06-05, 2026-09-04)",
 "description": "Realized lots, cumulative (unrealized-period file family per vendor naming); same layout family as fact_rld.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-09-04",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 26,
  "cadence": "quarterly",
  "claim": "measured",
  "note": "judge against the cadence, not T-1: the newest file of a quarterly family is current until the next one is due"
 },
 "size": {
  "objects": 13,
  "partitions": 13,
  "first_partition": "2023-09-01",
  "bytes": 284928140,
  "rows_all_partitions": 2691004,
  "rows_newest_partition": 284476,
  "row_count_rule": "snapshot table: the table row count is the newest partition (284476 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 87,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "closing_date", "type": "date32[day]", "nullable": true, "description": "realized lot closing date"},
  {"name": "closing_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "proceeds", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "proceeds_per_share", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "orgpurch_date", "type": "date32[day]", "nullable": true},
  {"name": "original_purchase_price", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "adjusted_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adjusted_gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f_2", "type": "string", "nullable": true},
  {"name": "g_f", "type": "string", "nullable": true},
  {"name": "p_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "lot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adj_disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "publication_timestamp", "type": "string", "nullable": true},
  {"name": "cbm", "type": "string", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "federal_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "wh_st", "type": "string", "nullable": true},
  {"name": "ytd_amortization", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_i", "type": "string", "nullable": true},
  {"name": "settle_date", "type": "date32[day]", "nullable": true},
  {"name": "r_u", "type": "string", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "transaction_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_gain_loss_pct", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "employee_option_original_cost", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "employee_option_realized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "g_i", "type": "string", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "trancode_expanded", "type": "string", "nullable": true},
  {"name": "order_number", "type": "string", "nullable": true},
  {"name": "versmrkr_7", "type": "string", "nullable": true},
  {"name": "close_event_id", "type": "string", "nullable": true},
  {"name": "close_open_event_id", "type": "string", "nullable": true},
  {"name": "versmrkr_8", "type": "string", "nullable": true},
  {"name": "schwab_order_id", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7646 ids measured length 10)",
   "last4_collisions_within_firm": 1842,
   "accounts_in_collisions": 4156,
   "denominator_accounts": 7646,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "realized lots",
  "cumulative realized gains",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "What are the cumulative realized gains of account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_realized_lots",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "BlackDiamond",
    "as_of": "YYYY-MM-DD",
    "period": "cumulative"
   },
   "returns": "as fact_rld from the newest quarterly cumulative file at or before as_of",
   "answers": [
    "What are the cumulative realized gains of account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 13 parts of schwab/08335338/silver/fact_rlu/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_fact_rly`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_fact_rly",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/fact_rly/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rly",
 "source_feed": "RLY",
 "grain": "one row per realized lot, year-to-date file; MEASURED cadence: month-end (2023-01-31 ... 2026-09-30)",
 "description": "Realized lots, year-to-date (yearly file family).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-09-30",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 9,
  "cadence": "month-end",
  "claim": "measured",
  "note": "judge against the cadence, not T-1: the newest file of a month-end family is current until the next one is due"
 },
 "size": {
  "objects": 39,
  "partitions": 39,
  "first_partition": "2023-07-31",
  "bytes": 633502486,
  "rows_all_partitions": 5982768,
  "rows_newest_partition": 327621,
  "row_count_rule": "snapshot table: the table row count is the newest partition (327621 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 87,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "closing_date", "type": "date32[day]", "nullable": true, "description": "realized lot closing date"},
  {"name": "closing_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "proceeds", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "proceeds_per_share", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "orgpurch_date", "type": "date32[day]", "nullable": true},
  {"name": "original_purchase_price", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "adjusted_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adjusted_gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f_2", "type": "string", "nullable": true},
  {"name": "g_f", "type": "string", "nullable": true},
  {"name": "p_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "lot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adj_disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "publication_timestamp", "type": "string", "nullable": true},
  {"name": "cbm", "type": "string", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "federal_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "wh_st", "type": "string", "nullable": true},
  {"name": "ytd_amortization", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_i", "type": "string", "nullable": true},
  {"name": "settle_date", "type": "date32[day]", "nullable": true},
  {"name": "r_u", "type": "string", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "transaction_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_gain_loss_pct", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "employee_option_original_cost", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "employee_option_realized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "g_i", "type": "string", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "trancode_expanded", "type": "string", "nullable": true},
  {"name": "order_number", "type": "string", "nullable": true},
  {"name": "versmrkr_7", "type": "string", "nullable": true},
  {"name": "close_event_id", "type": "string", "nullable": true},
  {"name": "close_open_event_id", "type": "string", "nullable": true},
  {"name": "versmrkr_8", "type": "string", "nullable": true},
  {"name": "schwab_order_id", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7646 ids measured length 10)",
   "last4_collisions_within_firm": 1842,
   "accounts_in_collisions": 4156,
   "denominator_accounts": 7646,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "realized lots",
  "year-to-date realized gains",
  "tax",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "What are the year-to-date realized gains of account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_realized_lots",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "BlackDiamond",
    "as_of": "YYYY-MM-DD",
    "period": "ytd"
   },
   "returns": "as fact_rld from the newest month-end year-to-date file at or before as_of",
   "answers": [
    "What are the year-to-date realized gains of account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 39 parts of schwab/08335338/silver/fact_rly/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_fact_rps`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_fact_rps",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/fact_rps/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rps",
 "source_feed": "RPS",
 "grain": "one row per account x security (cusip) x long/short side per business_date (daily full snapshot; 14 of 110,454 rows repeat account+cusip+l_s on 08335338 2026-10-13)",
 "description": "Positions, vendor-complete: quantities (settled, unsettled, cash, margin, short, when-issued), market value, closing price, factors.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 571,
  "partitions": 571,
  "first_partition": "2024-07-08",
  "bytes": 981349093,
  "rows_all_partitions": 39663401,
  "rows_newest_partition": 110454,
  "row_count_rule": "snapshot table: the table row count is the newest partition (110454 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 63,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ly_st", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "rulst_sufid", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "security_description_line_1", "type": "string", "nullable": true},
  {"name": "security_description_line_2", "type": "string", "nullable": true},
  {"name": "security_description_line_3", "type": "string", "nullable": true},
  {"name": "scrtydes_line_4", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlying_industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "unrul_sufid", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "mnymk_code", "type": "string", "nullable": true},
  {"name": "d_r", "type": "string", "nullable": true},
  {"name": "c_g", "type": "string", "nullable": true},
  {"name": "closing_price", "type": "decimal128(16, 5)", "nullable": true, "description": "custodian per-share close (never additive)"},
  {"name": "secprice_lstupdte", "type": "date32[day]", "nullable": true},
  {"name": "quantity_settled_unsettled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "market_value_settled_unsettled", "type": "decimal128(17, 4)", "nullable": true, "description": "position market value (additive; short rows negative)"},
  {"name": "accounting_rule_code", "type": "string", "nullable": true},
  {"name": "quantity_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_unsettled_long", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_unsettled_short", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "tips_factor", "type": "decimal128(18, 9)", "nullable": true},
  {"name": "asset_backed_factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "closing_price_unfactored", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "factor_date", "type": "date32[day]", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "non_tradable_quantity", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "a_i", "type": "string", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "quantity_cash_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_margin_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_short_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_wheniss_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7646 ids measured length 10)",
   "last4_collisions_within_firm": 1842,
   "accounts_in_collisions": 4156,
   "denominator_accounts": 7646,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "positions",
  "holdings",
  "quantity",
  "market value",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "What does account ...1234 hold today?",
  "What is the market value of CUSIP X in account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none (served only through its dim_ projection via schwab_query)",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 571 parts of schwab/08335338/silver/fact_rps/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_fact_rps_s2`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_fact_rps_s2",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/fact_rps_s2/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rps_s2",
 "source_feed": "RPS section 2",
 "grain": "one row per account per business_date (daily full snapshot)",
 "description": "Account balances (RPS section D2): long/short/net market value, net value plus cash, settled cash, margin, money-market funds, bank sweep, bank cash. Same object size as dim_balance at every partition (identity projection; content identity inferred).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 571,
  "partitions": 571,
  "first_partition": "2024-07-08",
  "bytes": 243753657,
  "rows_all_partitions": 3291921,
  "rows_newest_partition": 7646,
  "row_count_rule": "snapshot table: the table row count is the newest partition (7646 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 39,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "account_title_line_1", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_2", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_3", "type": "string", "nullable": true, "pii": true},
  {"name": "acct_regis", "type": "string", "nullable": true},
  {"name": "acct_type", "type": "string", "nullable": true},
  {"name": "net_credit_debit", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "margin_balance", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "available_to_pay", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mrgn_buying_pwr", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "money_mkt_funds", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mtd_margin_int", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "daily_margin_int", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "eqty_excl_option", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "eqty_percentage", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mkt_value_long", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mkt_value_short", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "eqty_incl_option", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "option_rqrmnts", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mnth_end_div_pay", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "maintenance_call", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mvl_cash_ex_optn", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "net_mv_positions", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "net_mv_plus_cash", "type": "decimal128(15, 2)", "nullable": true, "description": "net market value of positions plus cash"},
  {"name": "cash_balance_settled_only", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "cash_margin_bal_settled", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "bank_sweep_ibf", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "bank_cash", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7646 ids measured length 10)",
   "last4_collisions_within_firm": 1842,
   "accounts_in_collisions": 4156,
   "denominator_accounts": 7646,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "balances",
  "cash",
  "account value",
  "margin",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "What is the cash balance of account ...1234?",
  "What is the net market value plus cash of account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none (served only through its dim_ projection via schwab_query)",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "carries client PII columns (flagged pii:true); any tool must project them away (NFRA_OPLGTW forbidden_field_classes: raw_account_id, account_title, tax_identifier, mailing_address)",
  "same object size as dim_balance at every partition (243753657 bytes total both, measured); content identity inferred; one of the two is redundant storage"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 571 parts of schwab/08335338/silver/fact_rps_s2/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_fact_rtu`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_fact_rtu",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/fact_rtu/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rtu",
 "source_feed": "RTU",
 "grain": "one row per tax-lot detail row, cumulative file; MEASURED cadence: quarterly (same dates as fact_rlu)",
 "description": "Tax lot detail (DT section), cumulative.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-09-04",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 26,
  "cadence": "quarterly",
  "claim": "measured",
  "note": "judge against the cadence, not T-1: the newest file of a quarterly family is current until the next one is due"
 },
 "size": {
  "objects": 13,
  "partitions": 13,
  "first_partition": "2023-09-01",
  "bytes": 124293750,
  "rows_all_partitions": 1149874,
  "rows_newest_partition": 112496,
  "row_count_rule": "snapshot table: the table row count is the newest partition (112496 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 75,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "closing_date", "type": "date32[day]", "nullable": true, "description": "realized lot closing date"},
  {"name": "closing_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "proceeds", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "proceeds_per_share", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "adjusted_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adjusted_gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_b", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "g_f", "type": "string", "nullable": true},
  {"name": "p_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "lot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adj_disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "publication_timestamp", "type": "string", "nullable": true},
  {"name": "cbm", "type": "string", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "federal_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "wh_st", "type": "string", "nullable": true},
  {"name": "ytd_amortization", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_i", "type": "string", "nullable": true},
  {"name": "settle_date", "type": "date32[day]", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "transaction_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_gain_loss_pct", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "trancode_expanded", "type": "string", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "close_event_id", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7646 ids measured length 10)",
   "last4_collisions_within_firm": 1842,
   "accounts_in_collisions": 4156,
   "denominator_accounts": 7646,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "tax lots",
  "tax lot detail",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "What is the cumulative tax lot detail of account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_tax_lot_detail",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "BlackDiamond",
    "as_of": "YYYY-MM-DD",
    "period": "cumulative"
   },
   "returns": "tax-lot detail rows of the newest quarterly file at or before as_of",
   "answers": [
    "What is the cumulative tax lot detail of account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 13 parts of schwab/08335338/silver/fact_rtu/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_fact_rty`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_fact_rty",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/fact_rty/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rty",
 "source_feed": "RTY",
 "grain": "one row per tax-lot detail row, year-to-date file; MEASURED cadence: month-end (same dates as fact_rly)",
 "description": "Tax lot detail (DT section), yearly.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-09-30",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 9,
  "cadence": "month-end",
  "claim": "measured",
  "note": "judge against the cadence, not T-1: the newest file of a month-end family is current until the next one is due"
 },
 "size": {
  "objects": 39,
  "partitions": 39,
  "first_partition": "2023-07-31",
  "bytes": 265160255,
  "rows_all_partitions": 2442615,
  "rows_newest_partition": 115936,
  "row_count_rule": "snapshot table: the table row count is the newest partition (115936 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 75,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "closing_date", "type": "date32[day]", "nullable": true, "description": "realized lot closing date"},
  {"name": "closing_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "proceeds", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "proceeds_per_share", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "adjusted_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adjusted_gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_b", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "g_f", "type": "string", "nullable": true},
  {"name": "p_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "lot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adj_disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "publication_timestamp", "type": "string", "nullable": true},
  {"name": "cbm", "type": "string", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "federal_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "wh_st", "type": "string", "nullable": true},
  {"name": "ytd_amortization", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_i", "type": "string", "nullable": true},
  {"name": "settle_date", "type": "date32[day]", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "transaction_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_gain_loss_pct", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "trancode_expanded", "type": "string", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "close_event_id", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7646 ids measured length 10)",
   "last4_collisions_within_firm": 1842,
   "accounts_in_collisions": 4156,
   "denominator_accounts": 7646,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "tax lots",
  "tax lot detail",
  "year-to-date",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "What is the year-to-date tax lot detail of account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_tax_lot_detail",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "BlackDiamond",
    "as_of": "YYYY-MM-DD",
    "period": "ytd"
   },
   "returns": "tax-lot detail rows of the newest month-end file at or before as_of",
   "answers": [
    "What is the year-to-date tax lot detail of account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 39 parts of schwab/08335338/silver/fact_rty/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_fact_sec`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_fact_sec",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/fact_sec/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_sec",
 "source_feed": "SEC",
 "grain": "one row per security (cusip) per business_date (daily snapshot of the security master; 24 of 2,540 cusips repeat on 08335338 2026-10-13)",
 "description": "Security master: symbols, ISIN/SEDOL, description lines, product codes, prices, factors, rates, maturity, option fields, ratings.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 571,
  "partitions": 571,
  "first_partition": "2024-07-08",
  "bytes": 155023690,
  "rows_all_partitions": 1337865,
  "rows_newest_partition": 2540,
  "row_count_rule": "snapshot table: the table row count is the newest partition (2540 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 74,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ly_st", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "reorg_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "rulst_sufid", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "security_description_line_1", "type": "string", "nullable": true},
  {"name": "security_description_line_2", "type": "string", "nullable": true},
  {"name": "security_description_line_3", "type": "string", "nullable": true},
  {"name": "scrtydes_line_4", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlying_industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "unrul_sufid", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "mnymk_code", "type": "string", "nullable": true},
  {"name": "last_update", "type": "date32[day]", "nullable": true},
  {"name": "s_f", "type": "string", "nullable": true},
  {"name": "closing_price", "type": "decimal128(16, 5)", "nullable": true, "description": "custodian per-share close (never additive)"},
  {"name": "secprice_lstupdte", "type": "date32[day]", "nullable": true},
  {"name": "security_valuation_unit", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "optnrt_symbol", "type": "string", "nullable": true},
  {"name": "opt_expr_date", "type": "string", "nullable": true},
  {"name": "c_p", "type": "string", "nullable": true},
  {"name": "strike_price", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "interest_rate", "type": "decimal128(7, 5)", "nullable": true},
  {"name": "maturity_date", "type": "date32[day]", "nullable": true},
  {"name": "tips_factor", "type": "decimal128(18, 9)", "nullable": true},
  {"name": "asset_backed_factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "face_value_amt", "type": "decimal128(13, 4)", "nullable": true},
  {"name": "st_cd", "type": "string", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "p_i", "type": "string", "nullable": true},
  {"name": "o_i", "type": "string", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "closing_price_unfactored", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "factor_date", "type": "date32[day]", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "call_date", "type": "date32[day]", "nullable": true},
  {"name": "call_price", "type": "decimal128(36, 18)", "nullable": true},
  {"name": "issue_date", "type": "date32[day]", "nullable": true},
  {"name": "1st_cpn_date", "type": "date32[day]", "nullable": true},
  {"name": "options_multiplier", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "dividend_interest_frequency", "type": "string", "nullable": true},
  {"name": "s_p_rating", "type": "string", "nullable": true},
  {"name": "moodys_rating", "type": "string", "nullable": true},
  {"name": "next_pay_date", "type": "date32[day]", "nullable": true},
  {"name": "next_put_date", "type": "date32[day]", "nullable": true},
  {"name": "next_put_price", "type": "decimal128(36, 18)", "nullable": true},
  {"name": "mkt_code", "type": "string", "nullable": true},
  {"name": "par_value", "type": "decimal128(36, 18)", "nullable": true},
  {"name": "is_cy", "type": "string", "nullable": true},
  {"name": "cy_is", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "none (security grain)",
   "last4_derivation": "n/a",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "security master",
  "cusip",
  "ticker",
  "description",
  "price",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "What is the ticker and description of CUSIP X?",
  "What is the Schwab closing price of CUSIP X?"
 ],
 "existing_gateway_tool": {
  "name": "none (served only through its dim_ projection via schwab_query)",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 571 parts of schwab/08335338/silver/fact_sec/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_fact_slm`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_fact_slm",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/fact_slm/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_slm",
 "source_feed": "SLM (CS identity file)",
 "grain": "one row per account x person (positional CSV, no trailer control)",
 "description": "CS identity file, same grammar as FAM. PII. 08335338 only.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 567,
  "partitions": 567,
  "first_partition": "2024-07-12",
  "bytes": 89730102,
  "rows_all_partitions": 3227655,
  "rows_newest_partition": 7593,
  "row_count_rule": "snapshot table: the table row count is the newest partition (7593 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 11,
  "claim": "measured"
 },
 "columns": [
  {"name": "col_1", "type": "string", "nullable": true, "pii": true},
  {"name": "col_2", "type": "string", "nullable": true, "pii": true},
  {"name": "col_3", "type": "string", "nullable": true, "pii": true},
  {"name": "col_4", "type": "string", "nullable": true, "pii": true},
  {"name": "col_5", "type": "string", "nullable": true, "pii": true},
  {"name": "col_6", "type": "string", "nullable": true, "pii": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "col_4 (positional, 8-digit account number per data dictionary 2b; inferred)",
   "last4_derivation": "absent (positional column, not measured)",
   "last4_collisions_within_firm": null,
   "claim": "inferred"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "account holders",
  "identity",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "Who are the named persons on account ...1234? (PII: not a gateway answer)"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none",
  "note": "PII identity file; no tool proposed"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "carries client PII columns (flagged pii:true); any tool must project them away (NFRA_OPLGTW forbidden_field_classes: raw_account_id, account_title, tax_identifier, mailing_address)"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 567 parts of schwab/08335338/silver/fact_slm/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_fact_trn`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_fact_trn",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/fact_trn/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_trn",
 "source_feed": "TRN",
 "grain": "one row per transaction line per business_date (daily APPEND, no row-unique key)",
 "description": "Transactions, vendor-complete: trade/settle dates, transaction codes (tr_cd, sb_cd, tran_srcde), quantity, price, gross and net amount, fees, withholding.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 571,
  "partitions": 571,
  "first_partition": "2024-07-08",
  "bytes": 186701992,
  "rows_all_partitions": 3339973,
  "rows_newest_partition": 11906,
  "row_count_rule": "event/append table: rows sum across partitions",
  "schema_variants": 1,
  "columns_union": 140,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "account_title_line_1", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_2", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_3", "type": "string", "nullable": true, "pii": true},
  {"name": "acct_regis", "type": "string", "nullable": true},
  {"name": "acct_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ly_st", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "rulst_sufid", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlying_industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "unrul_sufid", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "mnymk_code", "type": "string", "nullable": true},
  {"name": "tr_cd", "type": "string", "nullable": true},
  {"name": "sb_cd", "type": "string", "nullable": true},
  {"name": "transaction_category", "type": "string", "nullable": true},
  {"name": "tran_srcde", "type": "string", "nullable": true},
  {"name": "transaction_source_code_description", "type": "string", "nullable": true},
  {"name": "transaction_detail_description", "type": "string", "nullable": true},
  {"name": "trade_typcd", "type": "string", "nullable": true},
  {"name": "t_c", "type": "string", "nullable": true},
  {"name": "trade_date", "type": "date32[day]", "nullable": true},
  {"name": "settlmnt_date", "type": "date32[day]", "nullable": true},
  {"name": "tran_date", "type": "date32[day]", "nullable": true},
  {"name": "exdivdnd_date", "type": "date32[day]", "nullable": true},
  {"name": "quantity", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "price", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "gross_amount", "type": "decimal128(15, 2)", "nullable": true, "description": "the money of a transaction (IRPT money law: never net_amount)"},
  {"name": "debit_credit", "type": "string", "nullable": true},
  {"name": "net_amount", "type": "decimal128(15, 2)", "nullable": true, "description": "net amount (reads 0.00 on cash rows; not the money)"},
  {"name": "commission", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "exchange_processing_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "broker_service_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "prime_broker_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "trade_away_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "redemption_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "other_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "federal_tefra_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "st_tx", "type": "string", "nullable": true},
  {"name": "accrued_interest", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "accounting_rule_code", "type": "string", "nullable": true},
  {"name": "ordr_srcd", "type": "string", "nullable": true},
  {"name": "order_number", "type": "string", "nullable": true},
  {"name": "trade_order_entry_tm_stmp", "type": "string", "nullable": true},
  {"name": "trade_order_exectn_tm_stmp", "type": "string", "nullable": true},
  {"name": "broker_code", "type": "string", "nullable": true},
  {"name": "broker_name", "type": "string", "nullable": true},
  {"name": "swb_from_account", "type": "string", "nullable": true},
  {"name": "swb_to_account", "type": "string", "nullable": true},
  {"name": "s1_check_number", "type": "string", "nullable": true},
  {"name": "s_i", "type": "string", "nullable": true},
  {"name": "stock_exchg", "type": "string", "nullable": true},
  {"name": "i_e", "type": "string", "nullable": true},
  {"name": "distribution_rate", "type": "decimal128(15, 8)", "nullable": true},
  {"name": "cash_in_lieu_share_quantity", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "dividend_interest_share_quantity", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "cash_in_lieu_rate", "type": "decimal128(15, 8)", "nullable": true},
  {"name": "asset_backed_factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "sr_sy", "type": "string", "nullable": true},
  {"name": "jn_tp", "type": "string", "nullable": true},
  {"name": "d_m", "type": "string", "nullable": true},
  {"name": "schwab_cashiering_unique_id", "type": "string", "nullable": true},
  {"name": "recipient_maker_name_line_1", "type": "string", "nullable": true},
  {"name": "recipient_maker_name_line_2", "type": "string", "nullable": true},
  {"name": "recipient_maker_name_line_3", "type": "string", "nullable": true},
  {"name": "frequency", "type": "string", "nullable": true},
  {"name": "disburse_check_number", "type": "string", "nullable": true},
  {"name": "federal_bank_reference_number", "type": "string", "nullable": true},
  {"name": "recipient_maker_acct_number", "type": "string", "nullable": true},
  {"name": "bank_act_typ", "type": "string", "nullable": true},
  {"name": "bank_name_part_1", "type": "string", "nullable": true},
  {"name": "bank_name_part_2", "type": "string", "nullable": true},
  {"name": "bank_aba", "type": "string", "nullable": true},
  {"name": "intermediary_name", "type": "string", "nullable": true},
  {"name": "transaction_check_memo_1", "type": "string", "nullable": true},
  {"name": "transaction_check_memo_2", "type": "string", "nullable": true},
  {"name": "retirement_fed_income_tax", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "retirement_state_income_tax", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "rt_tx", "type": "string", "nullable": true},
  {"name": "publication_time_stamp", "type": "string", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "tips_factor", "type": "decimal128(18, 9)", "nullable": true},
  {"name": "closing_price", "type": "decimal128(16, 5)", "nullable": true, "description": "custodian per-share close (never additive)"},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "transaction_memo", "type": "string", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "closing_price_unfactored", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "factor_date", "type": "date32[day]", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "step_in_fee", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "markupmarkdown", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "research_fee", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "exec_brok_comm", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "order_id", "type": "string", "nullable": true},
  {"name": "record_date", "type": "date32[day]", "nullable": true},
  {"name": "payable_date", "type": "date32[day]", "nullable": true},
  {"name": "accstart_date", "type": "string", "nullable": true},
  {"name": "accrend_date", "type": "string", "nullable": true},
  {"name": "d_f", "type": "string", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "yield_to_call", "type": "decimal128(8, 7)", "nullable": true},
  {"name": "yield_to_maturity", "type": "decimal128(8, 7)", "nullable": true},
  {"name": "trust_princ", "type": "decimal128(5, 2)", "nullable": true},
  {"name": "trust_income", "type": "decimal128(5, 2)", "nullable": true},
  {"name": "tax_cd", "type": "string", "nullable": true},
  {"name": "r_dc", "type": "string", "nullable": true},
  {"name": "r_cc", "type": "string", "nullable": true},
  {"name": "r_cy", "type": "string", "nullable": true},
  {"name": "cycle_id", "type": "string", "nullable": true},
  {"name": "tran_randm", "type": "decimal128(5, 0)", "nullable": true},
  {"name": "tranproc_date", "type": "date32[day]", "nullable": true},
  {"name": "cashiering_transaction_identifier", "type": "string", "nullable": true},
  {"name": "transaction_memo_or_wire_instructions", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7646 ids measured length 10)",
   "last4_collisions_within_firm": 1842,
   "accounts_in_collisions": 4156,
   "denominator_accounts": 7646,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "transactions",
  "trades",
  "flows",
  "deposits",
  "withdrawals",
  "fees",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "What transactions did account ...1234 have on a date?",
  "What deposits and withdrawals did account ...1234 have this month?"
 ],
 "existing_gateway_tool": {
  "name": "none (served only through its dim_ projection via schwab_query)",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b; data/assets/scripts/gold/irpt_reporting/sources.json schwab_08335338 (IRPT_DASHBD contracts read this table) @bc91e712ad",
 "open_items": [
  "carries client PII columns (flagged pii:true); any tool must project them away (NFRA_OPLGTW forbidden_field_classes: raw_account_id, account_title, tax_identifier, mailing_address)"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 571 parts of schwab/08335338/silver/fact_trn/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_fact_uln`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_fact_uln",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/fact_uln/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_uln",
 "source_feed": "ULN",
 "grain": "one row per account x open lot (event_id) per business_date (daily full snapshot; 0 duplicate account+event_id on 08335338 2026-10-13)",
 "description": "Unrealized lots, long and short (the non-taxable slice per the 49-schwab-conv skill): acquired date, quantity, cost basis, market value, unrealized gain, holding term. IRPT_DASHBD lot_source unrealized table.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 571,
  "partitions": 571,
  "first_partition": "2024-07-08",
  "bytes": 6027465501,
  "rows_all_partitions": 91629238,
  "rows_newest_partition": 311174,
  "row_count_rule": "snapshot table: the table row count is the newest partition (311174 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 61,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "current_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "current_market_value", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "accrued_interest", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "orgpurch_date", "type": "date32[day]", "nullable": true},
  {"name": "org_purchase_price", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "yield_tomaturity", "type": "decimal128(11, 9)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "unrealized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "c_b", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "dflot_selct", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "g_i", "type": "string", "nullable": true},
  {"name": "original_cost_basis", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "adjusted_cost_incldg_unpd_amort", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "event_id", "type": "string", "nullable": true, "description": "lot id"},
  {"name": "c_v", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7646 ids measured length 10)",
   "last4_collisions_within_firm": 1842,
   "accounts_in_collisions": 4156,
   "denominator_accounts": 7646,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "unrealized lots",
  "cost basis",
  "unrealized gain",
  "tax lots",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "What are the open lots and unrealized gain of account ...1234?",
  "What is the cost basis of CUSIP X in account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_unrealized_lots",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "BlackDiamond",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "open lots (event_id, cusip, ticker, acquired_date, quantity, cost_basis_unamortized, current_market_value, unrealized_gain_loss, h_t) from a NEW projection dim_lot_unrealized over fact_uln + fact_ult with a slice column",
   "answers": [
    "What are the open lots and unrealized gain of account ...1234?",
    "What is the cost basis of CUSIP X in account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b; data/assets/scripts/gold/irpt_reporting/sources.json schwab_08335338 (IRPT_DASHBD contracts read this table) @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 571 parts of schwab/08335338/silver/fact_uln/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_fact_ult`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_fact_ult",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/fact_ult/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_ult",
 "source_feed": "ULT",
 "grain": "one row per account x open lot per business_date (daily full snapshot)",
 "description": "Unrealized lot detail, the TAXABLE (brokerage) slice; identical layout to fact_uln. IRPT_DASHBD lot_source unrealized table; the legacy B_02.canonical_lots input.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 571,
  "partitions": 571,
  "first_partition": "2024-07-08",
  "bytes": 5276267913,
  "rows_all_partitions": 71890341,
  "rows_newest_partition": 226234,
  "row_count_rule": "snapshot table: the table row count is the newest partition (226234 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 61,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "current_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "current_market_value", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "accrued_interest", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "orgpurch_date", "type": "date32[day]", "nullable": true},
  {"name": "org_purchase_price", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "yield_tomaturity", "type": "decimal128(11, 9)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "unrealized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "c_b", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "dflot_selct", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "g_i", "type": "string", "nullable": true},
  {"name": "original_cost_basis", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "adjusted_cost_incldg_unpd_amort", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "event_id", "type": "string", "nullable": true, "description": "lot id"},
  {"name": "c_v", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7646 ids measured length 10)",
   "last4_collisions_within_firm": 1842,
   "accounts_in_collisions": 4156,
   "denominator_accounts": 7646,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "unrealized lots",
  "taxable lots",
  "cost basis",
  "unrealized gain",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "What is the unrealized short-term vs long-term gain of account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_unrealized_lots",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "BlackDiamond",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "as fact_uln (same tool, slice=taxable)",
   "answers": [
    "What is the unrealized short-term vs long-term gain of account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b; data/assets/scripts/gold/irpt_reporting/sources.json schwab_08335338 (IRPT_DASHBD contracts read this table) @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 571 parts of schwab/08335338/silver/fact_ult/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_fact_upn`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_fact_upn",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/fact_upn/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_upn",
 "source_feed": "UPN",
 "grain": "one row per account x position per business_date (DP section; semantics inferred from the dictionary: \"position (pending?)\")",
 "description": "Unrealized-position (DP section) file, non-taxable slice; meaning not vendor-confirmed (data dictionary 2a marks it with a question mark).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 571,
  "partitions": 571,
  "first_partition": "2024-07-08",
  "bytes": 768119000,
  "rows_all_partitions": 23977480,
  "rows_newest_partition": 65294,
  "row_count_rule": "snapshot table: the table row count is the newest partition (65294 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 44,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "current_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "current_market_value", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "accrued_interest", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "unrealized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "c_b", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "dflot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "principal_paydown_factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7646 ids measured length 10)",
   "last4_collisions_within_firm": 1842,
   "accounts_in_collisions": 4156,
   "denominator_accounts": 7646,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "positions",
  "unrealized positions",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "What unrealized position records does account ...1234 carry?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none",
  "note": "semantics not vendor-confirmed; no tool until the dictionary row binds"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 571 parts of schwab/08335338/silver/fact_upn/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08335338_fact_upt`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08335338_fact_upt",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08335338/silver/fact_upt/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_upt",
 "source_feed": "UPT",
 "grain": "one row per account x position per business_date (DP section; semantics inferred)",
 "description": "Unrealized-position (DP section) file, taxable slice; meaning not vendor-confirmed.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08335338/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 571,
  "partitions": 571,
  "first_partition": "2024-07-08",
  "bytes": 624148806,
  "rows_all_partitions": 15546956,
  "rows_newest_partition": 44251,
  "row_count_rule": "snapshot table: the table row count is the newest partition (44251 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 44,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "current_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "current_market_value", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "accrued_interest", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "unrealized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "c_b", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "dflot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "principal_paydown_factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08335338",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "49financial (infra/logic/registry/scopes.json class MASTER)",
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 7646 ids measured length 10)",
   "last4_collisions_within_firm": 1842,
   "accounts_in_collisions": 4156,
   "denominator_accounts": 7646,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": false,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "BlackDiamond"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 7646 of 7646 fact_acc rows)",
   "platform_cd_measured": {
    "MAM": 7415,
    "<empty>": 231
   },
   "money_manager_distinct": 3,
   "money_manager_smartx_rows": 7401,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "positions",
  "unrealized positions",
  "taxable",
  "schwab",
  "49financial",
  "master 08335338"
 ],
 "common_queries": [
  "What unrealized taxable position records does account ...1234 carry?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none",
  "note": "semantics not vendor-confirmed; no tool until the dictionary row binds"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 571 parts of schwab/08335338/silver/fact_upt/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08403355_dim_asset`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08403355_dim_asset",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08403355/silver/dim_asset/",
 "layer": "silver",
 "format": "parquet",
 "table": "dim_asset",
 "source_feed": "SEC projection",
 "grain": "one row per cusip per business_date (24-column projection of fact_sec)",
 "description": "Gateway-served security master projection (dataset dim_asset).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08403355/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 513,
  "partitions": 513,
  "first_partition": "2024-09-27",
  "bytes": 7924128,
  "rows_all_partitions": 65716,
  "rows_newest_partition": 669,
  "row_count_rule": "snapshot table: the table row count is the newest partition (669 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 29,
  "claim": "measured"
 },
 "columns": [
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "security_description_line_1", "type": "string", "nullable": true},
  {"name": "security_description_line_2", "type": "string", "nullable": true},
  {"name": "security_description_line_3", "type": "string", "nullable": true},
  {"name": "scrtydes_line_4", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "mnymk_code", "type": "string", "nullable": true},
  {"name": "closing_price", "type": "decimal128(16, 5)", "nullable": true, "description": "custodian per-share close (never additive)"},
  {"name": "closing_price_unfactored", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "par_value", "type": "decimal128(36, 18)", "nullable": true},
  {"name": "interest_rate", "type": "decimal128(7, 5)", "nullable": true},
  {"name": "maturity_date", "type": "date32[day]", "nullable": true},
  {"name": "strike_price", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "c_p", "type": "string", "nullable": true},
  {"name": "opt_expr_date", "type": "string", "nullable": true},
  {"name": "s_p_rating", "type": "string", "nullable": true},
  {"name": "moodys_rating", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08403355",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "absent",
   "claim": "inferred"
  },
  "account": {
   "column": "none (security grain)",
   "last4_derivation": "n/a",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "absent"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 30 of 30 fact_acc rows)",
   "platform_cd_measured": {
    "<empty>": 18,
    "MAM": 12
   },
   "money_manager_distinct": 1,
   "money_manager_smartx_rows": 0,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "security master",
  "cusip",
  "ticker",
  "schwab",
  "49financial",
  "master 08403355"
 ],
 "common_queries": [
  "What is the ticker and description of a Schwab security by cusip?"
 ],
 "existing_gateway_tool": {
  "name": "schwab_query (+ schwab_list_files, schwab_describe_dataset, schwab_get_access, schwab_prepare_download)",
  "verdict": "extend",
  "note": "gateway IAM (infra/aws/terraform/opal-gateway/schwab_reader_iam.tf:72-75) already admits this prefix, but org/standards/NFRA_OPLGTW_CONTRACT.json v1.4 masters and data_prefixes name only 08242234 and 08335338, so the typed query cannot name this master"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_security",
   "inputs": {
    "firm": "49financial",
    "account_last4": "n/a (security grain)",
    "platform": "<label for 08403355: absent>",
    "as_of": "YYYY-MM-DD",
    "cusip_or_ticker": "<cusip|ticker>"
   },
   "returns": "one dim_asset row",
   "answers": [
    "What is the ticker and description of a Schwab security by cusip?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "silver_datasets.schwab_dim_asset",
  "present": true,
  "line": 2404,
  "note": "the catalog row describes \"the contract's two masters\"; 08403355 is not covered"
 },
 "prior_art": "org/standards/NFRA_OPLGTW_CONTRACT.json v1.4 (dataset dim_asset); data/assets/scripts/silver/schwab_projections.py PROJECTIONS; docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "330 of 513 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day",
  "08403355 has no row in infra/logic/registry/scopes.json (08242234 and 08335338 do) and no label in NFRA_OPLGTW_CONTRACT.json masters"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 513 parts of schwab/08403355/silver/dim_asset/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08403355/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08403355_dim_balance`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08403355_dim_balance",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08403355/silver/dim_balance/",
 "layer": "silver",
 "format": "parquet",
 "table": "dim_balance",
 "source_feed": "RPS section 2 projection",
 "grain": "one row per account per business_date (identity projection of fact_rps_s2)",
 "description": "Gateway-served balances projection (dataset dim_balance).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08403355/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 513,
  "partitions": 513,
  "first_partition": "2024-09-27",
  "bytes": 5069858,
  "rows_all_partitions": 2978,
  "rows_newest_partition": 30,
  "row_count_rule": "snapshot table: the table row count is the newest partition (30 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 39,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "account_title_line_1", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_2", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_3", "type": "string", "nullable": true, "pii": true},
  {"name": "acct_regis", "type": "string", "nullable": true},
  {"name": "acct_type", "type": "string", "nullable": true},
  {"name": "net_credit_debit", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "margin_balance", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "available_to_pay", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mrgn_buying_pwr", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "money_mkt_funds", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mtd_margin_int", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "daily_margin_int", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "eqty_excl_option", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "eqty_percentage", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mkt_value_long", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mkt_value_short", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "eqty_incl_option", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "option_rqrmnts", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mnth_end_div_pay", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "maintenance_call", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mvl_cash_ex_optn", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "net_mv_positions", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "net_mv_plus_cash", "type": "decimal128(15, 2)", "nullable": true, "description": "net market value of positions plus cash"},
  {"name": "cash_balance_settled_only", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "cash_margin_bal_settled", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "bank_sweep_ibf", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "bank_cash", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08403355",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "absent",
   "claim": "inferred"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 30 ids measured length 10)",
   "last4_collisions_within_firm": 0,
   "accounts_in_collisions": 0,
   "denominator_accounts": 30,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": true,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "absent"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 30 of 30 fact_acc rows)",
   "platform_cd_measured": {
    "<empty>": 18,
    "MAM": 12
   },
   "money_manager_distinct": 1,
   "money_manager_smartx_rows": 0,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "balances",
  "cash",
  "account value",
  "schwab",
  "49financial",
  "master 08403355"
 ],
 "common_queries": [
  "What is the cash balance and net market value of account ...1234 on a date?"
 ],
 "existing_gateway_tool": {
  "name": "schwab_query (+ schwab_list_files, schwab_describe_dataset, schwab_get_access, schwab_prepare_download)",
  "verdict": "extend",
  "note": "gateway IAM (infra/aws/terraform/opal-gateway/schwab_reader_iam.tf:72-75) already admits this prefix, but org/standards/NFRA_OPLGTW_CONTRACT.json v1.4 masters and data_prefixes name only 08242234 and 08335338, so the typed query cannot name this master"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_balances",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "<label for 08403355: absent>",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "one dim_balance row per resolved account_ref for as_of",
   "answers": [
    "What is the cash balance and net market value of account ...1234 on a date?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "silver_datasets.schwab_dim_balance",
  "present": true,
  "line": 2426,
  "note": "the catalog row describes \"the contract's two masters\"; 08403355 is not covered"
 },
 "prior_art": "org/standards/NFRA_OPLGTW_CONTRACT.json v1.4 (dataset dim_balance); data/assets/scripts/silver/schwab_projections.py PROJECTIONS; docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "304 of 513 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day",
  "08403355 has no row in infra/logic/registry/scopes.json (08242234 and 08335338 do) and no label in NFRA_OPLGTW_CONTRACT.json masters"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 513 parts of schwab/08403355/silver/dim_balance/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08403355/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08403355_dim_position`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08403355_dim_position",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08403355/silver/dim_position/",
 "layer": "silver",
 "format": "parquet",
 "table": "dim_position",
 "source_feed": "RPS projection",
 "grain": "one row per account x cusip x l_s per business_date (25-column projection of fact_rps, row parity enforced)",
 "description": "Gateway-served positions projection (contract NFRA_OPLGTW v1.4 dataset dim_position).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08403355/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 513,
  "partitions": 513,
  "first_partition": "2024-09-27",
  "bytes": 11572843,
  "rows_all_partitions": 191214,
  "rows_newest_partition": 3884,
  "row_count_rule": "snapshot table: the table row count is the newest partition (3884 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 30,
  "claim": "measured"
 },
 "columns": [
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "accounting_rule_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "quantity_settled_unsettled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_unsettled_long", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_unsettled_short", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_cash_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_margin_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_short_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_wheniss_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "non_tradable_quantity", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "market_value_settled_unsettled", "type": "decimal128(17, 4)", "nullable": true, "description": "position market value (additive; short rows negative)"},
  {"name": "closing_price", "type": "decimal128(16, 5)", "nullable": true, "description": "custodian per-share close (never additive)"},
  {"name": "closing_price_unfactored", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "asset_backed_factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "secprice_lstupdte", "type": "date32[day]", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08403355",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "absent",
   "claim": "inferred"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 30 ids measured length 10)",
   "last4_collisions_within_firm": 0,
   "accounts_in_collisions": 0,
   "denominator_accounts": 30,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": true,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "absent"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 30 of 30 fact_acc rows)",
   "platform_cd_measured": {
    "<empty>": 18,
    "MAM": 12
   },
   "money_manager_distinct": 1,
   "money_manager_smartx_rows": 0,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "positions",
  "holdings",
  "positions by account",
  "schwab",
  "49financial",
  "master 08403355"
 ],
 "common_queries": [
  "What does account ...1234 hold today?",
  "What is the market value of a security in account ...1234 on a date?"
 ],
 "existing_gateway_tool": {
  "name": "schwab_query (+ schwab_list_files, schwab_describe_dataset, schwab_get_access, schwab_prepare_download)",
  "verdict": "extend",
  "note": "gateway IAM (infra/aws/terraform/opal-gateway/schwab_reader_iam.tf:72-75) already admits this prefix, but org/standards/NFRA_OPLGTW_CONTRACT.json v1.4 masters and data_prefixes name only 08242234 and 08335338, so the typed query cannot name this master"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_positions",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "<label for 08403355: absent>",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "rows of dim_position for the resolved account_ref(s) on the business_date at or before as_of; a last-4 that matches several accounts returns the candidate list, never a merge",
   "answers": [
    "What does account ...1234 hold today?",
    "What is the market value of a security in account ...1234 on a date?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "silver_datasets.schwab_dim_position",
  "present": true,
  "line": 2450,
  "note": "the catalog row describes \"the contract's two masters\"; 08403355 is not covered"
 },
 "prior_art": "org/standards/NFRA_OPLGTW_CONTRACT.json v1.4 (dataset dim_position); data/assets/scripts/silver/schwab_projections.py PROJECTIONS; docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "310 of 513 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day",
  "08403355 has no row in infra/logic/registry/scopes.json (08242234 and 08335338 do) and no label in NFRA_OPLGTW_CONTRACT.json masters"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 513 parts of schwab/08403355/silver/dim_position/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08403355/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08403355_dim_transaction`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08403355_dim_transaction",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08403355/silver/dim_transaction/",
 "layer": "silver",
 "format": "parquet",
 "table": "dim_transaction",
 "source_feed": "TRN projection",
 "grain": "one row per transaction line per business_date (39-column projection of fact_trn; append, no row-unique key)",
 "description": "Gateway-served transactions projection (dataset dim_transaction).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08403355/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 513,
  "partitions": 513,
  "first_partition": "2024-09-27",
  "bytes": 5481017,
  "rows_all_partitions": 9393,
  "rows_newest_partition": 36,
  "row_count_rule": "event/append table: rows sum across partitions",
  "schema_variants": 1,
  "columns_union": 44,
  "claim": "measured"
 },
 "columns": [
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "trade_date", "type": "date32[day]", "nullable": true},
  {"name": "settlmnt_date", "type": "date32[day]", "nullable": true},
  {"name": "tran_date", "type": "date32[day]", "nullable": true},
  {"name": "tr_cd", "type": "string", "nullable": true},
  {"name": "sb_cd", "type": "string", "nullable": true},
  {"name": "transaction_category", "type": "string", "nullable": true},
  {"name": "tran_srcde", "type": "string", "nullable": true},
  {"name": "transaction_source_code_description", "type": "string", "nullable": true},
  {"name": "transaction_detail_description", "type": "string", "nullable": true},
  {"name": "debit_credit", "type": "string", "nullable": true},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "quantity", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "price", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "gross_amount", "type": "decimal128(15, 2)", "nullable": true, "description": "the money of a transaction (IRPT money law: never net_amount)"},
  {"name": "net_amount", "type": "decimal128(15, 2)", "nullable": true, "description": "net amount (reads 0.00 on cash rows; not the money)"},
  {"name": "accrued_interest", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "commission", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "prime_broker_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "trade_away_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "redemption_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "other_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "step_in_fee", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "research_fee", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "exec_brok_comm", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "broker_service_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "exchange_processing_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "federal_tefra_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "retirement_fed_income_tax", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "retirement_state_income_tax", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "closing_price", "type": "decimal128(16, 5)", "nullable": true, "description": "custodian per-share close (never additive)"},
  {"name": "factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08403355",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "absent",
   "claim": "inferred"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 30 ids measured length 10)",
   "last4_collisions_within_firm": 0,
   "accounts_in_collisions": 0,
   "denominator_accounts": 30,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": true,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "absent"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 30 of 30 fact_acc rows)",
   "platform_cd_measured": {
    "<empty>": 18,
    "MAM": 12
   },
   "money_manager_distinct": 1,
   "money_manager_smartx_rows": 0,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "transactions",
  "trades",
  "flows",
  "schwab",
  "49financial",
  "master 08403355"
 ],
 "common_queries": [
  "What transactions did account ...1234 have on a date?"
 ],
 "existing_gateway_tool": {
  "name": "schwab_query (+ schwab_list_files, schwab_describe_dataset, schwab_get_access, schwab_prepare_download)",
  "verdict": "extend",
  "note": "gateway IAM (infra/aws/terraform/opal-gateway/schwab_reader_iam.tf:72-75) already admits this prefix, but org/standards/NFRA_OPLGTW_CONTRACT.json v1.4 masters and data_prefixes name only 08242234 and 08335338, so the typed query cannot name this master"
 },
 "proposed_tools": [
  {
   "name": "schwab_list_transactions",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "<label for 08403355: absent>",
    "as_of": "YYYY-MM-DD or start..end (<= 31 business dates)"
   },
   "returns": "dim_transaction rows by business_date for the resolved account_ref(s); row identity is (partition, row position)",
   "answers": [
    "What transactions did account ...1234 have on a date?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "silver_datasets.schwab_dim_transaction",
  "present": true,
  "line": 2474,
  "note": "the catalog row describes \"the contract's two masters\"; 08403355 is not covered"
 },
 "prior_art": "org/standards/NFRA_OPLGTW_CONTRACT.json v1.4 (dataset dim_transaction); data/assets/scripts/silver/schwab_projections.py PROJECTIONS; docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "353 of 513 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day",
  "08403355 has no row in infra/logic/registry/scopes.json (08242234 and 08335338 do) and no label in NFRA_OPLGTW_CONTRACT.json masters"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 513 parts of schwab/08403355/silver/dim_transaction/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08403355/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08403355_fact_acc`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08403355_fact_acc",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08403355/silver/fact_acc/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_acc",
 "source_feed": "ACC",
 "grain": "one row per account per business_date (daily full snapshot of the master account file)",
 "description": "Account master: identity, registration, account type, status, open date, platform and money manager, and the client PII the vendor sends (title lines, taxpayer, address, contact, SSN/TIN, DOB).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08403355/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 512,
  "partitions": 512,
  "first_partition": "2024-09-30",
  "bytes": 10237580,
  "rows_all_partitions": 2976,
  "rows_newest_partition": 30,
  "row_count_rule": "snapshot table: the table row count is the newest partition (30 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 95,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "account_title_line_1", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_2", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_3", "type": "string", "nullable": true, "pii": true},
  {"name": "account_status", "type": "string", "nullable": true},
  {"name": "acct_regis", "type": "string", "nullable": true},
  {"name": "acct_type", "type": "string", "nullable": true},
  {"name": "txpyr_title", "type": "string", "nullable": true, "pii": true},
  {"name": "taxpayer_first_name", "type": "string", "nullable": true, "pii": true},
  {"name": "taxpayer_middle_name", "type": "string", "nullable": true, "pii": true},
  {"name": "taxpayer_last_name", "type": "string", "nullable": true, "pii": true},
  {"name": "txpyr_suff", "type": "string", "nullable": true, "pii": true},
  {"name": "wh_cd", "type": "string", "nullable": true},
  {"name": "primary_contact", "type": "string", "nullable": true, "pii": true},
  {"name": "alias_name", "type": "string", "nullable": true, "pii": true},
  {"name": "mailing_address_line_1", "type": "string", "nullable": true, "pii": true},
  {"name": "mailing_address_line_2", "type": "string", "nullable": true, "pii": true},
  {"name": "mailing_address_line_3", "type": "string", "nullable": true, "pii": true},
  {"name": "account_mailing_city", "type": "string", "nullable": true, "pii": true},
  {"name": "ac_st", "type": "string", "nullable": true},
  {"name": "acct_mail_zip", "type": "string", "nullable": true, "pii": true},
  {"name": "acct_mailing_ctry_code", "type": "string", "nullable": true, "pii": true},
  {"name": "email_address", "type": "string", "nullable": true, "pii": true},
  {"name": "phone_nbr", "type": "string", "nullable": true, "pii": true},
  {"name": "business_ph", "type": "string", "nullable": true, "pii": true},
  {"name": "date_opened", "type": "date32[day]", "nullable": true},
  {"name": "schwab_br_cd", "type": "string", "nullable": true},
  {"name": "s_s", "type": "string", "nullable": true},
  {"name": "ac_cs", "type": "string", "nullable": true},
  {"name": "ac_ma", "type": "string", "nullable": true},
  {"name": "m_a", "type": "string", "nullable": true},
  {"name": "a_r", "type": "string", "nullable": true},
  {"name": "a_m", "type": "string", "nullable": true},
  {"name": "nr_am", "type": "string", "nullable": true},
  {"name": "a_o", "type": "string", "nullable": true},
  {"name": "b_f", "type": "string", "nullable": true},
  {"name": "nr_bn", "type": "string", "nullable": true},
  {"name": "p_c", "type": "string", "nullable": true},
  {"name": "p_d", "type": "string", "nullable": true},
  {"name": "p_b", "type": "string", "nullable": true},
  {"name": "u_m", "type": "string", "nullable": true},
  {"name": "f_a", "type": "string", "nullable": true},
  {"name": "intbr_cd", "type": "string", "nullable": true},
  {"name": "intbr_mm_cd", "type": "string", "nullable": true},
  {"name": "intbearing_ticker_symbol", "type": "string", "nullable": true},
  {"name": "intbearing_feat_is_id", "type": "string", "nullable": true},
  {"name": "int_sf", "type": "string", "nullable": true},
  {"name": "p_v", "type": "string", "nullable": true},
  {"name": "p_m", "type": "string", "nullable": true},
  {"name": "statemnt_pref", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "dflt_ltsel", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "cbm_mf", "type": "string", "nullable": true},
  {"name": "cbm_nmf", "type": "string", "nullable": true},
  {"name": "cb_mthd_date", "type": "date32[day]", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "custtype_code", "type": "string", "nullable": true},
  {"name": "organization_primary_name", "type": "string", "nullable": true, "pii": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "rstr_rsn1", "type": "string", "nullable": true},
  {"name": "rstr_rsn2", "type": "string", "nullable": true},
  {"name": "rstr_rsn3", "type": "string", "nullable": true},
  {"name": "rstr_rsn4", "type": "string", "nullable": true},
  {"name": "rstr_rsn5", "type": "string", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "schwab_bank_ic_account", "type": "string", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "ssn_tin_number", "type": "string", "nullable": true, "pii": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "p_e", "type": "string", "nullable": true},
  {"name": "mngdacct_pltfrmcd", "type": "string", "nullable": true, "description": "managed-account platform code (measured values MAM or empty)"},
  {"name": "managed_account_money_manager", "type": "string", "nullable": true, "description": "money manager of a managed account (the SmartX marker)"},
  {"name": "managed_account_investment_strategy", "type": "string", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "bank_sweep_display_name", "type": "string", "nullable": true},
  {"name": "versmrkr_7", "type": "string", "nullable": true},
  {"name": "o_l", "type": "string", "nullable": true},
  {"name": "versmrkr_8", "type": "string", "nullable": true},
  {"name": "date_of_birth", "type": "date32[day]", "nullable": true, "pii": true},
  {"name": "coy_cd", "type": "string", "nullable": true},
  {"name": "st_cd", "type": "string", "nullable": true},
  {"name": "versmrkr_9", "type": "string", "nullable": true},
  {"name": "s_i", "type": "string", "nullable": true},
  {"name": "m_t", "type": "string", "nullable": true},
  {"name": "mobile_phone_number", "type": "string", "nullable": true, "pii": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08403355",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "absent",
   "claim": "inferred"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 30 ids measured length 10)",
   "last4_collisions_within_firm": 0,
   "accounts_in_collisions": 0,
   "denominator_accounts": 30,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": true,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "absent"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 30 of 30 fact_acc rows)",
   "platform_cd_measured": {
    "<empty>": 18,
    "MAM": 12
   },
   "money_manager_distinct": 1,
   "money_manager_smartx_rows": 0,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "account",
  "account master",
  "registration",
  "account status",
  "money manager",
  "platform",
  "schwab",
  "49financial",
  "master 08403355"
 ],
 "common_queries": [
  "Which platform and money manager is account ...1234 on?",
  "Is account ...1234 open or closed, and when was it opened?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_resolve_account",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "<label for 08403355: absent>",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "candidate account_refs with master, platform code, money manager, account type and status, from a NEW non-PII projection dim_account of fact_acc (projection law: select only); never title, taxpayer, address, contact, SSN/TIN or DOB",
   "answers": [
    "Which platform and money manager is account ...1234 on?",
    "Is account ...1234 open or closed, and when was it opened?",
    "Which accounts end in 1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "303 of 512 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day",
  "carries client PII columns (flagged pii:true); any tool must project them away (NFRA_OPLGTW forbidden_field_classes: raw_account_id, account_title, tax_identifier, mailing_address)",
  "08403355 has no row in infra/logic/registry/scopes.json (08242234 and 08335338 do) and no label in NFRA_OPLGTW_CONTRACT.json masters"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 512 parts of schwab/08403355/silver/fact_acc/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08403355/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08403355_fact_rld`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08403355_fact_rld",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08403355/silver/fact_rld/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rld",
 "source_feed": "RLD",
 "grain": "one row per realized lot closed on the business_date (daily; closing_date = business date on 08335338 2026-10-13)",
 "description": "Realized lots, daily: closing and opening events, quantity, proceeds, cost basis, gain/loss, holding term, order number. The PRIMARY realized-lot tax source (IRPT_DASHBD lot_source realized; legacy B_02).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08403355/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 761,
  "partitions": 761,
  "first_partition": "2023-10-03",
  "bytes": 11729854,
  "rows_all_partitions": 1894,
  "rows_newest_partition": 0,
  "row_count_rule": "event/append table: rows sum across partitions",
  "schema_variants": 1,
  "columns_union": 86,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "closing_date", "type": "date32[day]", "nullable": true, "description": "realized lot closing date"},
  {"name": "closing_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "proceeds", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "proceeds_per_share", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "orgpurch_date", "type": "date32[day]", "nullable": true},
  {"name": "original_purchase_price", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "adjusted_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adjusted_gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f_2", "type": "string", "nullable": true},
  {"name": "g_f", "type": "string", "nullable": true},
  {"name": "p_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "lot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adj_disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "publication_timestamp", "type": "string", "nullable": true},
  {"name": "cbm", "type": "string", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "federal_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "wh_st", "type": "string", "nullable": true},
  {"name": "ytd_amortization", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_i", "type": "string", "nullable": true},
  {"name": "settle_date", "type": "date32[day]", "nullable": true},
  {"name": "r_u", "type": "string", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "transaction_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_gain_loss_pct", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "employee_option_original_cost", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "employee_option_realized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "g_i", "type": "string", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "trancode_expanded", "type": "string", "nullable": true},
  {"name": "order_number", "type": "string", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "close_event_id", "type": "string", "nullable": true},
  {"name": "close_open_event_id", "type": "string", "nullable": true},
  {"name": "versmrkr_7", "type": "string", "nullable": true},
  {"name": "schwab_order_id", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08403355",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "absent",
   "claim": "inferred"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 30 ids measured length 10)",
   "last4_collisions_within_firm": 0,
   "accounts_in_collisions": 0,
   "denominator_accounts": 30,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": true,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "absent"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 30 of 30 fact_acc rows)",
   "platform_cd_measured": {
    "<empty>": 18,
    "MAM": 12
   },
   "money_manager_distinct": 1,
   "money_manager_smartx_rows": 0,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "realized lots",
  "realized gains",
  "tax",
  "capital gains",
  "schwab",
  "49financial",
  "master 08403355"
 ],
 "common_queries": [
  "What realized gains did account ...1234 book on a date?",
  "What lots of CUSIP X were sold from account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_realized_lots",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "<label for 08403355: absent>",
    "as_of": "YYYY-MM-DD or start..end",
    "period": "daily"
   },
   "returns": "realized lots (closing_date, cusip, ticker, closing_quantity, proceeds, cost_basis_unamortized, gain_loss_dollars, h_t) from a NEW projection dim_lot_realized over fact_rld",
   "answers": [
    "What realized gains did account ...1234 book on a date?",
    "What lots of CUSIP X were sold from account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "748 of 761 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day",
  "08403355 has no row in infra/logic/registry/scopes.json (08242234 and 08335338 do) and no label in NFRA_OPLGTW_CONTRACT.json masters"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 761 parts of schwab/08403355/silver/fact_rld/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08403355/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08403355_fact_rlu`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08403355_fact_rlu",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08403355/silver/fact_rlu/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rlu",
 "source_feed": "RLU",
 "grain": "one row per realized lot, cumulative file; MEASURED cadence: quarterly (2023-03-03, 06-02, 09-01 ... 2026-06-05, 2026-09-04)",
 "description": "Realized lots, cumulative (unrealized-period file family per vendor naming); same layout family as fact_rld.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08403355/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-09-04",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 26,
  "cadence": "quarterly",
  "claim": "measured",
  "note": "judge against the cadence, not T-1: the newest file of a quarterly family is current until the next one is due"
 },
 "size": {
  "objects": 12,
  "partitions": 12,
  "first_partition": "2024-01-19",
  "bytes": 222347,
  "rows_all_partitions": 36,
  "rows_newest_partition": 9,
  "row_count_rule": "snapshot table: the table row count is the newest partition (9 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 87,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "closing_date", "type": "date32[day]", "nullable": true, "description": "realized lot closing date"},
  {"name": "closing_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "proceeds", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "proceeds_per_share", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "orgpurch_date", "type": "date32[day]", "nullable": true},
  {"name": "original_purchase_price", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "adjusted_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adjusted_gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f_2", "type": "string", "nullable": true},
  {"name": "g_f", "type": "string", "nullable": true},
  {"name": "p_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "lot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adj_disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "publication_timestamp", "type": "string", "nullable": true},
  {"name": "cbm", "type": "string", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "federal_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "wh_st", "type": "string", "nullable": true},
  {"name": "ytd_amortization", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_i", "type": "string", "nullable": true},
  {"name": "settle_date", "type": "date32[day]", "nullable": true},
  {"name": "r_u", "type": "string", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "transaction_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_gain_loss_pct", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "employee_option_original_cost", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "employee_option_realized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "g_i", "type": "string", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "trancode_expanded", "type": "string", "nullable": true},
  {"name": "order_number", "type": "string", "nullable": true},
  {"name": "versmrkr_7", "type": "string", "nullable": true},
  {"name": "close_event_id", "type": "string", "nullable": true},
  {"name": "close_open_event_id", "type": "string", "nullable": true},
  {"name": "versmrkr_8", "type": "string", "nullable": true},
  {"name": "schwab_order_id", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08403355",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "absent",
   "claim": "inferred"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 30 ids measured length 10)",
   "last4_collisions_within_firm": 0,
   "accounts_in_collisions": 0,
   "denominator_accounts": 30,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": true,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "absent"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 30 of 30 fact_acc rows)",
   "platform_cd_measured": {
    "<empty>": 18,
    "MAM": 12
   },
   "money_manager_distinct": 1,
   "money_manager_smartx_rows": 0,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "realized lots",
  "cumulative realized gains",
  "schwab",
  "49financial",
  "master 08403355"
 ],
 "common_queries": [
  "What are the cumulative realized gains of account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_realized_lots",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "<label for 08403355: absent>",
    "as_of": "YYYY-MM-DD",
    "period": "cumulative"
   },
   "returns": "as fact_rld from the newest quarterly cumulative file at or before as_of",
   "answers": [
    "What are the cumulative realized gains of account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "8 of 12 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day",
  "08403355 has no row in infra/logic/registry/scopes.json (08242234 and 08335338 do) and no label in NFRA_OPLGTW_CONTRACT.json masters"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 12 parts of schwab/08403355/silver/fact_rlu/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08403355/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08403355_fact_rly`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08403355_fact_rly",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08403355/silver/fact_rly/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rly",
 "source_feed": "RLY",
 "grain": "one row per realized lot, year-to-date file; MEASURED cadence: month-end (2023-01-31 ... 2026-09-30)",
 "description": "Realized lots, year-to-date (yearly file family).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08403355/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-09-30",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 9,
  "cadence": "month-end",
  "claim": "measured",
  "note": "judge against the cadence, not T-1: the newest file of a month-end family is current until the next one is due"
 },
 "size": {
  "objects": 36,
  "partitions": 36,
  "first_partition": "2023-10-31",
  "bytes": 1578182,
  "rows_all_partitions": 5855,
  "rows_newest_partition": 1892,
  "row_count_rule": "snapshot table: the table row count is the newest partition (1892 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 87,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "closing_date", "type": "date32[day]", "nullable": true, "description": "realized lot closing date"},
  {"name": "closing_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "proceeds", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "proceeds_per_share", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "orgpurch_date", "type": "date32[day]", "nullable": true},
  {"name": "original_purchase_price", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "adjusted_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adjusted_gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f_2", "type": "string", "nullable": true},
  {"name": "g_f", "type": "string", "nullable": true},
  {"name": "p_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "lot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adj_disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "publication_timestamp", "type": "string", "nullable": true},
  {"name": "cbm", "type": "string", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "federal_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "wh_st", "type": "string", "nullable": true},
  {"name": "ytd_amortization", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_i", "type": "string", "nullable": true},
  {"name": "settle_date", "type": "date32[day]", "nullable": true},
  {"name": "r_u", "type": "string", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "transaction_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_gain_loss_pct", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "employee_option_original_cost", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "employee_option_realized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "g_i", "type": "string", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "trancode_expanded", "type": "string", "nullable": true},
  {"name": "order_number", "type": "string", "nullable": true},
  {"name": "versmrkr_7", "type": "string", "nullable": true},
  {"name": "close_event_id", "type": "string", "nullable": true},
  {"name": "close_open_event_id", "type": "string", "nullable": true},
  {"name": "versmrkr_8", "type": "string", "nullable": true},
  {"name": "schwab_order_id", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08403355",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "absent",
   "claim": "inferred"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 30 ids measured length 10)",
   "last4_collisions_within_firm": 0,
   "accounts_in_collisions": 0,
   "denominator_accounts": 30,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": true,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "absent"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 30 of 30 fact_acc rows)",
   "platform_cd_measured": {
    "<empty>": 18,
    "MAM": 12
   },
   "money_manager_distinct": 1,
   "money_manager_smartx_rows": 0,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "realized lots",
  "year-to-date realized gains",
  "tax",
  "schwab",
  "49financial",
  "master 08403355"
 ],
 "common_queries": [
  "What are the year-to-date realized gains of account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_realized_lots",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "<label for 08403355: absent>",
    "as_of": "YYYY-MM-DD",
    "period": "ytd"
   },
   "returns": "as fact_rld from the newest month-end year-to-date file at or before as_of",
   "answers": [
    "What are the year-to-date realized gains of account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "29 of 36 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day",
  "08403355 has no row in infra/logic/registry/scopes.json (08242234 and 08335338 do) and no label in NFRA_OPLGTW_CONTRACT.json masters"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 36 parts of schwab/08403355/silver/fact_rly/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08403355/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08403355_fact_rps`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08403355_fact_rps",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08403355/silver/fact_rps/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rps",
 "source_feed": "RPS",
 "grain": "one row per account x security (cusip) x long/short side per business_date (daily full snapshot; 14 of 110,454 rows repeat account+cusip+l_s on 08335338 2026-10-13)",
 "description": "Positions, vendor-complete: quantities (settled, unsettled, cash, margin, short, when-issued), market value, closing price, factors.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08403355/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 513,
  "partitions": 513,
  "first_partition": "2024-09-27",
  "bytes": 17924740,
  "rows_all_partitions": 191214,
  "rows_newest_partition": 3884,
  "row_count_rule": "snapshot table: the table row count is the newest partition (3884 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 63,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ly_st", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "rulst_sufid", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "security_description_line_1", "type": "string", "nullable": true},
  {"name": "security_description_line_2", "type": "string", "nullable": true},
  {"name": "security_description_line_3", "type": "string", "nullable": true},
  {"name": "scrtydes_line_4", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlying_industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "unrul_sufid", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "mnymk_code", "type": "string", "nullable": true},
  {"name": "d_r", "type": "string", "nullable": true},
  {"name": "c_g", "type": "string", "nullable": true},
  {"name": "closing_price", "type": "decimal128(16, 5)", "nullable": true, "description": "custodian per-share close (never additive)"},
  {"name": "secprice_lstupdte", "type": "date32[day]", "nullable": true},
  {"name": "quantity_settled_unsettled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "market_value_settled_unsettled", "type": "decimal128(17, 4)", "nullable": true, "description": "position market value (additive; short rows negative)"},
  {"name": "accounting_rule_code", "type": "string", "nullable": true},
  {"name": "quantity_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_unsettled_long", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_unsettled_short", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "tips_factor", "type": "decimal128(18, 9)", "nullable": true},
  {"name": "asset_backed_factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "closing_price_unfactored", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "factor_date", "type": "date32[day]", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "non_tradable_quantity", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "a_i", "type": "string", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "quantity_cash_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_margin_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_short_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "quantity_wheniss_settled", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08403355",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "absent",
   "claim": "inferred"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 30 ids measured length 10)",
   "last4_collisions_within_firm": 0,
   "accounts_in_collisions": 0,
   "denominator_accounts": 30,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": true,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "absent"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 30 of 30 fact_acc rows)",
   "platform_cd_measured": {
    "<empty>": 18,
    "MAM": 12
   },
   "money_manager_distinct": 1,
   "money_manager_smartx_rows": 0,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "positions",
  "holdings",
  "quantity",
  "market value",
  "schwab",
  "49financial",
  "master 08403355"
 ],
 "common_queries": [
  "What does account ...1234 hold today?",
  "What is the market value of CUSIP X in account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none (served only through its dim_ projection via schwab_query)",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "310 of 513 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day",
  "08403355 has no row in infra/logic/registry/scopes.json (08242234 and 08335338 do) and no label in NFRA_OPLGTW_CONTRACT.json masters"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 513 parts of schwab/08403355/silver/fact_rps/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08403355/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08403355_fact_rps_s2`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08403355_fact_rps_s2",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08403355/silver/fact_rps_s2/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rps_s2",
 "source_feed": "RPS section 2",
 "grain": "one row per account per business_date (daily full snapshot)",
 "description": "Account balances (RPS section D2): long/short/net market value, net value plus cash, settled cash, margin, money-market funds, bank sweep, bank cash. Same object size as dim_balance at every partition (identity projection; content identity inferred).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08403355/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 513,
  "partitions": 513,
  "first_partition": "2024-09-27",
  "bytes": 5069858,
  "rows_all_partitions": 2978,
  "rows_newest_partition": 30,
  "row_count_rule": "snapshot table: the table row count is the newest partition (30 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 39,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "account_title_line_1", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_2", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_3", "type": "string", "nullable": true, "pii": true},
  {"name": "acct_regis", "type": "string", "nullable": true},
  {"name": "acct_type", "type": "string", "nullable": true},
  {"name": "net_credit_debit", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "margin_balance", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "available_to_pay", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mrgn_buying_pwr", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "money_mkt_funds", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mtd_margin_int", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "daily_margin_int", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "eqty_excl_option", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "eqty_percentage", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mkt_value_long", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mkt_value_short", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "eqty_incl_option", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "option_rqrmnts", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mnth_end_div_pay", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "maintenance_call", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "mvl_cash_ex_optn", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "net_mv_positions", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "net_mv_plus_cash", "type": "decimal128(15, 2)", "nullable": true, "description": "net market value of positions plus cash"},
  {"name": "cash_balance_settled_only", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "cash_margin_bal_settled", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "bank_sweep_ibf", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "bank_cash", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08403355",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "absent",
   "claim": "inferred"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 30 ids measured length 10)",
   "last4_collisions_within_firm": 0,
   "accounts_in_collisions": 0,
   "denominator_accounts": 30,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": true,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "absent"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 30 of 30 fact_acc rows)",
   "platform_cd_measured": {
    "<empty>": 18,
    "MAM": 12
   },
   "money_manager_distinct": 1,
   "money_manager_smartx_rows": 0,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "balances",
  "cash",
  "account value",
  "margin",
  "schwab",
  "49financial",
  "master 08403355"
 ],
 "common_queries": [
  "What is the cash balance of account ...1234?",
  "What is the net market value plus cash of account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none (served only through its dim_ projection via schwab_query)",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "304 of 513 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day",
  "carries client PII columns (flagged pii:true); any tool must project them away (NFRA_OPLGTW forbidden_field_classes: raw_account_id, account_title, tax_identifier, mailing_address)",
  "same object size as dim_balance at every partition (5069858 bytes total both, measured); content identity inferred; one of the two is redundant storage",
  "08403355 has no row in infra/logic/registry/scopes.json (08242234 and 08335338 do) and no label in NFRA_OPLGTW_CONTRACT.json masters"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 513 parts of schwab/08403355/silver/fact_rps_s2/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08403355/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08403355_fact_rtu`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08403355_fact_rtu",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08403355/silver/fact_rtu/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rtu",
 "source_feed": "RTU",
 "grain": "one row per tax-lot detail row, cumulative file; MEASURED cadence: quarterly (same dates as fact_rlu)",
 "description": "Tax lot detail (DT section), cumulative.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08403355/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-09-04",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 26,
  "cadence": "quarterly",
  "claim": "measured",
  "note": "judge against the cadence, not T-1: the newest file of a quarterly family is current until the next one is due"
 },
 "size": {
  "objects": 12,
  "partitions": 12,
  "first_partition": "2024-01-19",
  "bytes": 190637,
  "rows_all_partitions": 36,
  "rows_newest_partition": 9,
  "row_count_rule": "snapshot table: the table row count is the newest partition (9 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 75,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "closing_date", "type": "date32[day]", "nullable": true, "description": "realized lot closing date"},
  {"name": "closing_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "proceeds", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "proceeds_per_share", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "adjusted_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adjusted_gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_b", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "g_f", "type": "string", "nullable": true},
  {"name": "p_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "lot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adj_disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "publication_timestamp", "type": "string", "nullable": true},
  {"name": "cbm", "type": "string", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "federal_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "wh_st", "type": "string", "nullable": true},
  {"name": "ytd_amortization", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_i", "type": "string", "nullable": true},
  {"name": "settle_date", "type": "date32[day]", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "transaction_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_gain_loss_pct", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "trancode_expanded", "type": "string", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "close_event_id", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08403355",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "absent",
   "claim": "inferred"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 30 ids measured length 10)",
   "last4_collisions_within_firm": 0,
   "accounts_in_collisions": 0,
   "denominator_accounts": 30,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": true,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "absent"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 30 of 30 fact_acc rows)",
   "platform_cd_measured": {
    "<empty>": 18,
    "MAM": 12
   },
   "money_manager_distinct": 1,
   "money_manager_smartx_rows": 0,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "tax lots",
  "tax lot detail",
  "schwab",
  "49financial",
  "master 08403355"
 ],
 "common_queries": [
  "What is the cumulative tax lot detail of account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_tax_lot_detail",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "<label for 08403355: absent>",
    "as_of": "YYYY-MM-DD",
    "period": "cumulative"
   },
   "returns": "tax-lot detail rows of the newest quarterly file at or before as_of",
   "answers": [
    "What is the cumulative tax lot detail of account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "8 of 12 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day",
  "08403355 has no row in infra/logic/registry/scopes.json (08242234 and 08335338 do) and no label in NFRA_OPLGTW_CONTRACT.json masters"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 12 parts of schwab/08403355/silver/fact_rtu/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08403355/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08403355_fact_rty`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08403355_fact_rty",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08403355/silver/fact_rty/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_rty",
 "source_feed": "RTY",
 "grain": "one row per tax-lot detail row, year-to-date file; MEASURED cadence: month-end (same dates as fact_rly)",
 "description": "Tax lot detail (DT section), yearly.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08403355/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-09-30",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 9,
  "cadence": "month-end",
  "claim": "measured",
  "note": "judge against the cadence, not T-1: the newest file of a month-end family is current until the next one is due"
 },
 "size": {
  "objects": 36,
  "partitions": 36,
  "first_partition": "2023-10-31",
  "bytes": 1304027,
  "rows_all_partitions": 5732,
  "rows_newest_partition": 1818,
  "row_count_rule": "snapshot table: the table row count is the newest partition (1818 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 75,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "closing_date", "type": "date32[day]", "nullable": true, "description": "realized lot closing date"},
  {"name": "closing_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "proceeds", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "proceeds_per_share", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "adjusted_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adjusted_gain_loss_percentage", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_b", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "g_f", "type": "string", "nullable": true},
  {"name": "p_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "lot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "adj_disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "publication_timestamp", "type": "string", "nullable": true},
  {"name": "cbm", "type": "string", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "federal_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "wh_st", "type": "string", "nullable": true},
  {"name": "ytd_amortization", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "c_i", "type": "string", "nullable": true},
  {"name": "settle_date", "type": "date32[day]", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "transaction_gain_loss_dollars", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_gain_loss_pct", "type": "decimal128(17, 12)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "trancode_expanded", "type": "string", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "close_event_id", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08403355",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "absent",
   "claim": "inferred"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 30 ids measured length 10)",
   "last4_collisions_within_firm": 0,
   "accounts_in_collisions": 0,
   "denominator_accounts": 30,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": true,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "absent"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 30 of 30 fact_acc rows)",
   "platform_cd_measured": {
    "<empty>": 18,
    "MAM": 12
   },
   "money_manager_distinct": 1,
   "money_manager_smartx_rows": 0,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "tax lots",
  "tax lot detail",
  "year-to-date",
  "schwab",
  "49financial",
  "master 08403355"
 ],
 "common_queries": [
  "What is the year-to-date tax lot detail of account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_tax_lot_detail",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "<label for 08403355: absent>",
    "as_of": "YYYY-MM-DD",
    "period": "ytd"
   },
   "returns": "tax-lot detail rows of the newest month-end file at or before as_of",
   "answers": [
    "What is the year-to-date tax lot detail of account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "29 of 36 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day",
  "08403355 has no row in infra/logic/registry/scopes.json (08242234 and 08335338 do) and no label in NFRA_OPLGTW_CONTRACT.json masters"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 36 parts of schwab/08403355/silver/fact_rty/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08403355/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08403355_fact_sec`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08403355_fact_sec",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08403355/silver/fact_sec/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_sec",
 "source_feed": "SEC",
 "grain": "one row per security (cusip) per business_date (daily snapshot of the security master; 24 of 2,540 cusips repeat on 08335338 2026-10-13)",
 "description": "Security master: symbols, ISIN/SEDOL, description lines, product codes, prices, factors, rates, maturity, option fields, ratings.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08403355/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 513,
  "partitions": 513,
  "first_partition": "2024-09-27",
  "bytes": 14548150,
  "rows_all_partitions": 65716,
  "rows_newest_partition": 669,
  "row_count_rule": "snapshot table: the table row count is the newest partition (669 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 74,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ly_st", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "reorg_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "rulst_sufid", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "security_description_line_1", "type": "string", "nullable": true},
  {"name": "security_description_line_2", "type": "string", "nullable": true},
  {"name": "security_description_line_3", "type": "string", "nullable": true},
  {"name": "scrtydes_line_4", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlying_industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "unrul_sufid", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "mnymk_code", "type": "string", "nullable": true},
  {"name": "last_update", "type": "date32[day]", "nullable": true},
  {"name": "s_f", "type": "string", "nullable": true},
  {"name": "closing_price", "type": "decimal128(16, 5)", "nullable": true, "description": "custodian per-share close (never additive)"},
  {"name": "secprice_lstupdte", "type": "date32[day]", "nullable": true},
  {"name": "security_valuation_unit", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "optnrt_symbol", "type": "string", "nullable": true},
  {"name": "opt_expr_date", "type": "string", "nullable": true},
  {"name": "c_p", "type": "string", "nullable": true},
  {"name": "strike_price", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "interest_rate", "type": "decimal128(7, 5)", "nullable": true},
  {"name": "maturity_date", "type": "date32[day]", "nullable": true},
  {"name": "tips_factor", "type": "decimal128(18, 9)", "nullable": true},
  {"name": "asset_backed_factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "face_value_amt", "type": "decimal128(13, 4)", "nullable": true},
  {"name": "st_cd", "type": "string", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "p_i", "type": "string", "nullable": true},
  {"name": "o_i", "type": "string", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "closing_price_unfactored", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "factor_date", "type": "date32[day]", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "call_date", "type": "date32[day]", "nullable": true},
  {"name": "call_price", "type": "decimal128(36, 18)", "nullable": true},
  {"name": "issue_date", "type": "date32[day]", "nullable": true},
  {"name": "1st_cpn_date", "type": "date32[day]", "nullable": true},
  {"name": "options_multiplier", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "dividend_interest_frequency", "type": "string", "nullable": true},
  {"name": "s_p_rating", "type": "string", "nullable": true},
  {"name": "moodys_rating", "type": "string", "nullable": true},
  {"name": "next_pay_date", "type": "date32[day]", "nullable": true},
  {"name": "next_put_date", "type": "date32[day]", "nullable": true},
  {"name": "next_put_price", "type": "decimal128(36, 18)", "nullable": true},
  {"name": "mkt_code", "type": "string", "nullable": true},
  {"name": "par_value", "type": "decimal128(36, 18)", "nullable": true},
  {"name": "is_cy", "type": "string", "nullable": true},
  {"name": "cy_is", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08403355",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "absent",
   "claim": "inferred"
  },
  "account": {
   "column": "none (security grain)",
   "last4_derivation": "n/a",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "absent"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 30 of 30 fact_acc rows)",
   "platform_cd_measured": {
    "<empty>": 18,
    "MAM": 12
   },
   "money_manager_distinct": 1,
   "money_manager_smartx_rows": 0,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "security master",
  "cusip",
  "ticker",
  "description",
  "price",
  "schwab",
  "49financial",
  "master 08403355"
 ],
 "common_queries": [
  "What is the ticker and description of CUSIP X?",
  "What is the Schwab closing price of CUSIP X?"
 ],
 "existing_gateway_tool": {
  "name": "none (served only through its dim_ projection via schwab_query)",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "330 of 513 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day",
  "08403355 has no row in infra/logic/registry/scopes.json (08242234 and 08335338 do) and no label in NFRA_OPLGTW_CONTRACT.json masters"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 513 parts of schwab/08403355/silver/fact_sec/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08403355/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08403355_fact_trn`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08403355_fact_trn",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08403355/silver/fact_trn/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_trn",
 "source_feed": "TRN",
 "grain": "one row per transaction line per business_date (daily APPEND, no row-unique key)",
 "description": "Transactions, vendor-complete: trade/settle dates, transaction codes (tr_cd, sb_cd, tran_srcde), quantity, price, gross and net amount, fees, withholding.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08403355/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 513,
  "partitions": 513,
  "first_partition": "2024-09-27",
  "bytes": 15609511,
  "rows_all_partitions": 9393,
  "rows_newest_partition": 36,
  "row_count_rule": "event/append table: rows sum across partitions",
  "schema_variants": 1,
  "columns_union": 140,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "account_title_line_1", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_2", "type": "string", "nullable": true, "pii": true},
  {"name": "account_title_line_3", "type": "string", "nullable": true, "pii": true},
  {"name": "acct_regis", "type": "string", "nullable": true},
  {"name": "acct_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ly_st", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "rulst_sufid", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlying_industry_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "unrul_sufid", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "mnymk_code", "type": "string", "nullable": true},
  {"name": "tr_cd", "type": "string", "nullable": true},
  {"name": "sb_cd", "type": "string", "nullable": true},
  {"name": "transaction_category", "type": "string", "nullable": true},
  {"name": "tran_srcde", "type": "string", "nullable": true},
  {"name": "transaction_source_code_description", "type": "string", "nullable": true},
  {"name": "transaction_detail_description", "type": "string", "nullable": true},
  {"name": "trade_typcd", "type": "string", "nullable": true},
  {"name": "t_c", "type": "string", "nullable": true},
  {"name": "trade_date", "type": "date32[day]", "nullable": true},
  {"name": "settlmnt_date", "type": "date32[day]", "nullable": true},
  {"name": "tran_date", "type": "date32[day]", "nullable": true},
  {"name": "exdivdnd_date", "type": "date32[day]", "nullable": true},
  {"name": "quantity", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "price", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "gross_amount", "type": "decimal128(15, 2)", "nullable": true, "description": "the money of a transaction (IRPT money law: never net_amount)"},
  {"name": "debit_credit", "type": "string", "nullable": true},
  {"name": "net_amount", "type": "decimal128(15, 2)", "nullable": true, "description": "net amount (reads 0.00 on cash rows; not the money)"},
  {"name": "commission", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "exchange_processing_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "broker_service_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "prime_broker_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "trade_away_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "redemption_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "other_fee", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "federal_tefra_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "state_tax_withholding", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "st_tx", "type": "string", "nullable": true},
  {"name": "accrued_interest", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "accounting_rule_code", "type": "string", "nullable": true},
  {"name": "ordr_srcd", "type": "string", "nullable": true},
  {"name": "order_number", "type": "string", "nullable": true},
  {"name": "trade_order_entry_tm_stmp", "type": "string", "nullable": true},
  {"name": "trade_order_exectn_tm_stmp", "type": "string", "nullable": true},
  {"name": "broker_code", "type": "string", "nullable": true},
  {"name": "broker_name", "type": "string", "nullable": true},
  {"name": "swb_from_account", "type": "string", "nullable": true},
  {"name": "swb_to_account", "type": "string", "nullable": true},
  {"name": "s1_check_number", "type": "string", "nullable": true},
  {"name": "s_i", "type": "string", "nullable": true},
  {"name": "stock_exchg", "type": "string", "nullable": true},
  {"name": "i_e", "type": "string", "nullable": true},
  {"name": "distribution_rate", "type": "decimal128(15, 8)", "nullable": true},
  {"name": "cash_in_lieu_share_quantity", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "dividend_interest_share_quantity", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "cash_in_lieu_rate", "type": "decimal128(15, 8)", "nullable": true},
  {"name": "asset_backed_factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "sr_sy", "type": "string", "nullable": true},
  {"name": "jn_tp", "type": "string", "nullable": true},
  {"name": "d_m", "type": "string", "nullable": true},
  {"name": "schwab_cashiering_unique_id", "type": "string", "nullable": true},
  {"name": "recipient_maker_name_line_1", "type": "string", "nullable": true},
  {"name": "recipient_maker_name_line_2", "type": "string", "nullable": true},
  {"name": "recipient_maker_name_line_3", "type": "string", "nullable": true},
  {"name": "frequency", "type": "string", "nullable": true},
  {"name": "disburse_check_number", "type": "string", "nullable": true},
  {"name": "federal_bank_reference_number", "type": "string", "nullable": true},
  {"name": "recipient_maker_acct_number", "type": "string", "nullable": true},
  {"name": "bank_act_typ", "type": "string", "nullable": true},
  {"name": "bank_name_part_1", "type": "string", "nullable": true},
  {"name": "bank_name_part_2", "type": "string", "nullable": true},
  {"name": "bank_aba", "type": "string", "nullable": true},
  {"name": "intermediary_name", "type": "string", "nullable": true},
  {"name": "transaction_check_memo_1", "type": "string", "nullable": true},
  {"name": "transaction_check_memo_2", "type": "string", "nullable": true},
  {"name": "retirement_fed_income_tax", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "retirement_state_income_tax", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "rt_tx", "type": "string", "nullable": true},
  {"name": "publication_time_stamp", "type": "string", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "tips_factor", "type": "decimal128(18, 9)", "nullable": true},
  {"name": "closing_price", "type": "decimal128(16, 5)", "nullable": true, "description": "custodian per-share close (never additive)"},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "transaction_memo", "type": "string", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "closing_price_unfactored", "type": "decimal128(16, 5)", "nullable": true},
  {"name": "factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "factor_date", "type": "date32[day]", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "step_in_fee", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "markupmarkdown", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "research_fee", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "exec_brok_comm", "type": "decimal128(18, 4)", "nullable": true},
  {"name": "versmrkr_5", "type": "string", "nullable": true},
  {"name": "order_id", "type": "string", "nullable": true},
  {"name": "record_date", "type": "date32[day]", "nullable": true},
  {"name": "payable_date", "type": "date32[day]", "nullable": true},
  {"name": "accstart_date", "type": "string", "nullable": true},
  {"name": "accrend_date", "type": "string", "nullable": true},
  {"name": "d_f", "type": "string", "nullable": true},
  {"name": "versmrkr_6", "type": "string", "nullable": true},
  {"name": "yield_to_call", "type": "decimal128(8, 7)", "nullable": true},
  {"name": "yield_to_maturity", "type": "decimal128(8, 7)", "nullable": true},
  {"name": "trust_princ", "type": "decimal128(5, 2)", "nullable": true},
  {"name": "trust_income", "type": "decimal128(5, 2)", "nullable": true},
  {"name": "tax_cd", "type": "string", "nullable": true},
  {"name": "r_dc", "type": "string", "nullable": true},
  {"name": "r_cc", "type": "string", "nullable": true},
  {"name": "r_cy", "type": "string", "nullable": true},
  {"name": "cycle_id", "type": "string", "nullable": true},
  {"name": "tran_randm", "type": "decimal128(5, 0)", "nullable": true},
  {"name": "tranproc_date", "type": "date32[day]", "nullable": true},
  {"name": "cashiering_transaction_identifier", "type": "string", "nullable": true},
  {"name": "transaction_memo_or_wire_instructions", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08403355",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "absent",
   "claim": "inferred"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 30 ids measured length 10)",
   "last4_collisions_within_firm": 0,
   "accounts_in_collisions": 0,
   "denominator_accounts": 30,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": true,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "absent"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 30 of 30 fact_acc rows)",
   "platform_cd_measured": {
    "<empty>": 18,
    "MAM": 12
   },
   "money_manager_distinct": 1,
   "money_manager_smartx_rows": 0,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "transactions",
  "trades",
  "flows",
  "deposits",
  "withdrawals",
  "fees",
  "schwab",
  "49financial",
  "master 08403355"
 ],
 "common_queries": [
  "What transactions did account ...1234 have on a date?",
  "What deposits and withdrawals did account ...1234 have this month?"
 ],
 "existing_gateway_tool": {
  "name": "none (served only through its dim_ projection via schwab_query)",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "353 of 513 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day",
  "carries client PII columns (flagged pii:true); any tool must project them away (NFRA_OPLGTW forbidden_field_classes: raw_account_id, account_title, tax_identifier, mailing_address)",
  "08403355 has no row in infra/logic/registry/scopes.json (08242234 and 08335338 do) and no label in NFRA_OPLGTW_CONTRACT.json masters"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 513 parts of schwab/08403355/silver/fact_trn/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08403355/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08403355_fact_uln`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08403355_fact_uln",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08403355/silver/fact_uln/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_uln",
 "source_feed": "ULN",
 "grain": "one row per account x open lot (event_id) per business_date (daily full snapshot; 0 duplicate account+event_id on 08335338 2026-10-13)",
 "description": "Unrealized lots, long and short (the non-taxable slice per the 49-schwab-conv skill): acquired date, quantity, cost basis, market value, unrealized gain, holding term. IRPT_DASHBD lot_source unrealized table.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08403355/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 513,
  "partitions": 513,
  "first_partition": "2024-09-27",
  "bytes": 5341869,
  "rows_all_partitions": 0,
  "rows_newest_partition": 0,
  "row_count_rule": "snapshot table: the table row count is the newest partition (0 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 61,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "current_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "current_market_value", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "accrued_interest", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "orgpurch_date", "type": "date32[day]", "nullable": true},
  {"name": "org_purchase_price", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "yield_tomaturity", "type": "decimal128(11, 9)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "unrealized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "c_b", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "dflot_selct", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "g_i", "type": "string", "nullable": true},
  {"name": "original_cost_basis", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "adjusted_cost_incldg_unpd_amort", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "event_id", "type": "string", "nullable": true, "description": "lot id"},
  {"name": "c_v", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08403355",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "absent",
   "claim": "inferred"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 30 ids measured length 10)",
   "last4_collisions_within_firm": 0,
   "accounts_in_collisions": 0,
   "denominator_accounts": 30,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": true,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "absent"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 30 of 30 fact_acc rows)",
   "platform_cd_measured": {
    "<empty>": 18,
    "MAM": 12
   },
   "money_manager_distinct": 1,
   "money_manager_smartx_rows": 0,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "unrealized lots",
  "cost basis",
  "unrealized gain",
  "tax lots",
  "schwab",
  "49financial",
  "master 08403355"
 ],
 "common_queries": [
  "What are the open lots and unrealized gain of account ...1234?",
  "What is the cost basis of CUSIP X in account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_unrealized_lots",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "<label for 08403355: absent>",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "open lots (event_id, cusip, ticker, acquired_date, quantity, cost_basis_unamortized, current_market_value, unrealized_gain_loss, h_t) from a NEW projection dim_lot_unrealized over fact_uln + fact_ult with a slice column",
   "answers": [
    "What are the open lots and unrealized gain of account ...1234?",
    "What is the cost basis of CUSIP X in account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "513 of 513 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day",
  "all 513 parts hold 0 rows: this master carries no non-taxable lot rows",
  "08403355 has no row in infra/logic/registry/scopes.json (08242234 and 08335338 do) and no label in NFRA_OPLGTW_CONTRACT.json masters"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 513 parts of schwab/08403355/silver/fact_uln/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08403355/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08403355_fact_ult`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08403355_fact_ult",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08403355/silver/fact_ult/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_ult",
 "source_feed": "ULT",
 "grain": "one row per account x open lot per business_date (daily full snapshot)",
 "description": "Unrealized lot detail, the TAXABLE (brokerage) slice; identical layout to fact_uln. IRPT_DASHBD lot_source unrealized table; the legacy B_02.canonical_lots input.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08403355/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 513,
  "partitions": 513,
  "first_partition": "2024-09-27",
  "bytes": 36423214,
  "rows_all_partitions": 331923,
  "rows_newest_partition": 5665,
  "row_count_rule": "snapshot table: the table row count is the newest partition (5665 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 61,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "current_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "trans_code", "type": "string", "nullable": true},
  {"name": "current_market_value", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "accrued_interest", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "acquired_date", "type": "date32[day]", "nullable": true},
  {"name": "orgpurch_date", "type": "date32[day]", "nullable": true},
  {"name": "org_purchase_price", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "yield_tomaturity", "type": "decimal128(11, 9)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "unrealized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "days_held", "type": "string", "nullable": true},
  {"name": "h_t", "type": "string", "nullable": true, "description": "holding term code (L long-term, S short-term)"},
  {"name": "c_b", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "dflot_selct", "type": "string", "nullable": true},
  {"name": "w_s", "type": "string", "nullable": true},
  {"name": "versmrkr_1", "type": "string", "nullable": true},
  {"name": "disallowed_loss_amount", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "transaction_cost", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "transaction_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "versmrkr_2", "type": "string", "nullable": true},
  {"name": "g_i", "type": "string", "nullable": true},
  {"name": "original_cost_basis", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_3", "type": "string", "nullable": true},
  {"name": "adjusted_cost_incldg_unpd_amort", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "versmrkr_4", "type": "string", "nullable": true},
  {"name": "event_id", "type": "string", "nullable": true, "description": "lot id"},
  {"name": "c_v", "type": "string", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08403355",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "absent",
   "claim": "inferred"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 30 ids measured length 10)",
   "last4_collisions_within_firm": 0,
   "accounts_in_collisions": 0,
   "denominator_accounts": 30,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": true,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "absent"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 30 of 30 fact_acc rows)",
   "platform_cd_measured": {
    "<empty>": 18,
    "MAM": 12
   },
   "money_manager_distinct": 1,
   "money_manager_smartx_rows": 0,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "unrealized lots",
  "taxable lots",
  "cost basis",
  "unrealized gain",
  "schwab",
  "49financial",
  "master 08403355"
 ],
 "common_queries": [
  "What is the unrealized short-term vs long-term gain of account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "schwab_get_unrealized_lots",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "<label for 08403355: absent>",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "as fact_uln (same tool, slice=taxable)",
   "answers": [
    "What is the unrealized short-term vs long-term gain of account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "332 of 513 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day",
  "08403355 has no row in infra/logic/registry/scopes.json (08242234 and 08335338 do) and no label in NFRA_OPLGTW_CONTRACT.json masters"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 513 parts of schwab/08403355/silver/fact_ult/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08403355/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08403355_fact_upn`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08403355_fact_upn",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08403355/silver/fact_upn/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_upn",
 "source_feed": "UPN",
 "grain": "one row per account x position per business_date (DP section; semantics inferred from the dictionary: \"position (pending?)\")",
 "description": "Unrealized-position (DP section) file, non-taxable slice; meaning not vendor-confirmed (data dictionary 2a marks it with a question mark).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08403355/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 513,
  "partitions": 513,
  "first_partition": "2024-09-27",
  "bytes": 3884436,
  "rows_all_partitions": 0,
  "rows_newest_partition": 0,
  "row_count_rule": "snapshot table: the table row count is the newest partition (0 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 44,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "current_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "current_market_value", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "accrued_interest", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "unrealized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "c_b", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "dflot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "principal_paydown_factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08403355",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "absent",
   "claim": "inferred"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 30 ids measured length 10)",
   "last4_collisions_within_firm": 0,
   "accounts_in_collisions": 0,
   "denominator_accounts": 30,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": true,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "absent"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 30 of 30 fact_acc rows)",
   "platform_cd_measured": {
    "<empty>": 18,
    "MAM": 12
   },
   "money_manager_distinct": 1,
   "money_manager_smartx_rows": 0,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "positions",
  "unrealized positions",
  "schwab",
  "49financial",
  "master 08403355"
 ],
 "common_queries": [
  "What unrealized position records does account ...1234 carry?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none",
  "note": "semantics not vendor-confirmed; no tool until the dictionary row binds"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "513 of 513 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day",
  "all 513 parts hold 0 rows: this master carries no non-taxable position rows",
  "08403355 has no row in infra/logic/registry/scopes.json (08242234 and 08335338 do) and no label in NFRA_OPLGTW_CONTRACT.json masters"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 513 parts of schwab/08403355/silver/fact_upn/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08403355/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/schwab_08403355_fact_upt`

```json
{
 "contract_id": "opal-data-assets/silver/schwab_08403355_fact_upt",
 "bucket": "opal-data-assets",
 "s3_prefix": "schwab/08403355/silver/fact_upt/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_upt",
 "source_feed": "UPT",
 "grain": "one row per account x position per business_date (DP section; semantics inferred)",
 "description": "Unrealized-position (DP section) file, taxable slice; meaning not vendor-confirmed.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet, one part per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-schwab (data/assets/scripts/silver/schwab_conversion.py + schwab_projections.py)",
  "schedule": "S3 ObjectCreated on schwab/08403355/bronze/ suffix .zip (bucket notification) + daily sweep rule opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *) ENABLED; bronze lands from the canonical-schwab-si2 daily pull",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "cadence": "daily",
  "claim": "measured"
 },
 "size": {
  "objects": 513,
  "partitions": 513,
  "first_partition": "2024-09-27",
  "bytes": 15420130,
  "rows_all_partitions": 190006,
  "rows_newest_partition": 3883,
  "row_count_rule": "snapshot table: the table row count is the newest partition (3883 rows); the all-partition sum counts row-days",
  "schema_variants": 1,
  "columns_union": 44,
  "claim": "measured"
 },
 "columns": [
  {"name": "custdian_id", "type": "string", "nullable": true},
  {"name": "mstracct_number", "type": "string", "nullable": true, "description": "the master number, 10-char padded", "example": "00<master>"},
  {"name": "master_account_name", "type": "string", "nullable": true, "description": "the master (advisor firm) name"},
  {"name": "business_date", "type": "date32[day]", "nullable": true, "description": "the vendor business date of the file (equals the date= partition)", "example": "2026-10-13"},
  {"name": "account_id", "type": "string", "nullable": true, "description": "Schwab account number, 10-char zero-padded string (never cast to int)", "example": "****1234"},
  {"name": "security_type", "type": "string", "nullable": true},
  {"name": "prod_code", "type": "string", "nullable": true},
  {"name": "prodcatg_code", "type": "string", "nullable": true},
  {"name": "tax_code", "type": "string", "nullable": true},
  {"name": "ticker_symbol", "type": "string", "nullable": true, "description": "ticker symbol (vendor empty string when none)"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "schwab_sec_nbr", "type": "string", "nullable": true},
  {"name": "item_issue_id", "type": "string", "nullable": true},
  {"name": "isin", "type": "string", "nullable": true},
  {"name": "sedol", "type": "string", "nullable": true},
  {"name": "options_display_symbol", "type": "string", "nullable": true},
  {"name": "underlying_ticker_symbol", "type": "string", "nullable": true},
  {"name": "underlyng_cusip", "type": "string", "nullable": true},
  {"name": "underly_schwab", "type": "string", "nullable": true},
  {"name": "underlying_itm_iss_id", "type": "string", "nullable": true},
  {"name": "underlying_isin", "type": "string", "nullable": true},
  {"name": "underly_sedol", "type": "string", "nullable": true},
  {"name": "current_quantity", "type": "decimal128(16, 6)", "nullable": true},
  {"name": "l_s", "type": "string", "nullable": true, "description": "long/short side code"},
  {"name": "current_market_value", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "accrued_interest", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "cost_basis_unamortized", "type": "decimal128(15, 2)", "nullable": true, "description": "lot cost basis"},
  {"name": "cost_per_share", "type": "decimal128(19, 8)", "nullable": true},
  {"name": "adjusted_cost_basis_amortized", "type": "decimal128(15, 2)", "nullable": true},
  {"name": "adjusted_cost_per_share", "type": "decimal128(23, 12)", "nullable": true},
  {"name": "unrealized_gain_loss", "type": "decimal128(17, 4)", "nullable": true},
  {"name": "c_b", "type": "string", "nullable": true},
  {"name": "c_t", "type": "string", "nullable": true},
  {"name": "a_t", "type": "string", "nullable": true},
  {"name": "c_f", "type": "string", "nullable": true},
  {"name": "original_face", "type": "decimal128(15, 5)", "nullable": true},
  {"name": "dflot_selct", "type": "string", "nullable": true},
  {"name": "c_m", "type": "string", "nullable": true},
  {"name": "principal_paydown_factor", "type": "decimal128(15, 12)", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_master_observed", "type": "string", "nullable": true, "description": "provenance: master read from the H1 header bytes (never the folder)"},
  {"name": "_section", "type": "string", "nullable": true, "description": "provenance: CRS section"},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment schwab/<master>/ (the master); master_account_name column on fact_acc",
   "values": [
    "49financial"
   ],
   "master": "08403355",
   "master_account_name_measured": "49 FINANCIAL",
   "registry": "absent",
   "claim": "inferred"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "last 4 characters of the 10-char zero-padded account_id string (all 30 ids measured length 10)",
   "last4_collisions_within_firm": 0,
   "accounts_in_collisions": 0,
   "denominator_accounts": 30,
   "basis": "measured on fact_acc date=2026-10-13 of this master (the master account universe); across the three 49financial masters the union is 7667 accounts with 1848 colliding last-4 values covering 4171 accounts",
   "unique": true,
   "claim": "measured"
  },
  "platform": {
   "column": "mngdacct_pltfrmcd + managed_account_money_manager (fact_acc); master label per NFRA_OPLGTW_CONTRACT masters",
   "values": [
    "absent"
   ],
   "custodian": "schwab (custdian_id = SCHWAB on 30 of 30 fact_acc rows)",
   "platform_cd_measured": {
    "<empty>": 18,
    "MAM": 12
   },
   "money_manager_distinct": 1,
   "money_manager_smartx_rows": 0,
   "claim": "measured"
  }
 },
 "nl_tags": [
  "positions",
  "unrealized positions",
  "taxable",
  "schwab",
  "49financial",
  "master 08403355"
 ],
 "common_queries": [
  "What unrealized taxable position records does account ...1234 carry?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none",
  "note": "semantics not vendor-confirmed; no tool until the dictionary row binds"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "docs/architecture/OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md v0.5 section 2a/2b @bc91e712ad",
 "open_items": [
  "332 of 513 parts hold 0 rows (measured); a 0-row partition is a landed empty file, not an absent day",
  "08403355 has no row in infra/logic/registry/scopes.json (08242234 and 08335338 do) and no label in NFRA_OPLGTW_CONTRACT.json masters"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=schwab/ (63 pages, 62,984 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 513 parts of schwab/08403355/silver/fact_upt/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "pyarrow read_table opal-data-assets/schwab/08403355/silver/fact_acc/date=2026-10-13/data.parquet columns account_id, master_account_name, mngdacct_pltfrmcd, managed_account_money_manager, custdian_id",
   "at": "2026-10-14T13:16Z"
  }
 ]
}
```

### `opal-data-assets/silver/commonwealth_cottonwood_account_day_value`

```json
{
 "contract_id": "opal-data-assets/silver/commonwealth_cottonwood_account_day_value",
 "bucket": "opal-data-assets",
 "s3_prefix": "commonwealth/cottonwood/silver/account_day_value/",
 "layer": "silver",
 "format": "parquet",
 "table": "account_day_value",
 "grain": "one row per account x date x cusip (plus a cash leg) over 2013-04-03..2026-06-22",
 "description": "Rebuilt daily valuation of every Commonwealth account: quantity, close, value, price source, blank reason.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "one delivery partition date=2026-06-23",
  "claim": "measured"
 },
 "producer": {
  "name": "data/assets/scripts/silver/commonwealth_daily_valuation.py / commonwealth_account_return_daily.py",
  "schedule": "none: a one-time historical delivery (bronze date=2026-06-23 only), converted by hand-run scripts 2026-10-06..10-09",
  "claim": "inferred"
 },
 "freshness": {
  "latest_partition": "2026-06-23",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 78,
  "note": "a closed historical delivery (the Commonwealth custody ended at the 2026-06-23 cut-over): lag is not staleness",
  "claim": "measured"
 },
 "size": {
  "objects": 1,
  "bytes": 54246028,
  "rows": 21102041,
  "schema_variants": 1,
  "columns_union": 10,
  "claim": "measured"
 },
 "columns": [
  {"name": "account", "type": "string", "nullable": true},
  {"name": "date", "type": "date32[day]", "nullable": true},
  {"name": "cusip", "type": "string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "quantity", "type": "double", "nullable": true},
  {"name": "close", "type": "double", "nullable": true},
  {"name": "value", "type": "double", "nullable": true},
  {"name": "price_source", "type": "string", "nullable": true},
  {"name": "blank_reason", "type": "string", "nullable": true},
  {"name": "cash_leg", "type": "string", "nullable": true},
  {"name": "run_commit", "type": "string", "nullable": true}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment commonwealth/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "account",
   "last4_derivation": "last 4 characters of the account string; ids are 7 to 17 characters long (measured), so last-4 is a weak key",
   "last4_collisions_within_firm": 352,
   "accounts_in_collisions": 731,
   "denominator_accounts": 1533,
   "basis": "measured on every transactions part (the delivery account universe); positions alone: 83 accounts, 0 collisions",
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment commonwealth/ (custodian and broker-dealer Commonwealth); Advisor_ID carries the rep code (4 advisor ids in transactions)",
   "values": [
    "commonwealth"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "account value",
  "daily valuation",
  "historical holdings",
  "commonwealth",
  "cottonwood",
  "legacy custodian",
  "pre-2026-06-23 history"
 ],
 "common_queries": [
  "What was account ...1234 worth on a past date before the custodian move?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "commonwealth_get_account_history",
   "inputs": {
    "firm": "cottonwood",
    "account_last4": "1234",
    "platform": "commonwealth",
    "as_of": "YYYY-MM-DD (<= 2026-06-23)"
   },
   "returns": "rows of this table for the resolved account(s); a last-4 matching several accounts returns the candidates",
   "answers": [
    "What was account ...1234 worth on a past date before the custodian move?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "data/assets/scripts/silver/commonwealth_*.py; data/assets/scripts/gold/irpt_reporting/sources.json key _commonwealth_delivery (empty object) @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=commonwealth/ (12 pages, 11,155 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 1 parquet parts of commonwealth/cottonwood/silver/account_day_value/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "projected read of Account_Number/AccountNumber/account columns",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

### `opal-data-assets/silver/commonwealth_cottonwood_account_links`

```json
{
 "contract_id": "opal-data-assets/silver/commonwealth_cottonwood_account_links",
 "bucket": "opal-data-assets",
 "s3_prefix": "commonwealth/cottonwood/silver/account_links/",
 "layer": "silver",
 "format": "parquet",
 "table": "account_links",
 "grain": "one row per old Commonwealth account (1,450 rows) with its linked new account",
 "description": "Old-to-new account linkage (LINKED 212, NOT_LINKED 1,238): advisor ids, first/last trade, score, evidence.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "one delivery partition date=2026-06-23",
  "claim": "measured"
 },
 "producer": {
  "name": "data/assets/scripts/silver/commonwealth_account_links.py",
  "schedule": "none: a one-time historical delivery (bronze date=2026-06-23 only), converted by hand-run scripts 2026-10-06..10-09",
  "claim": "inferred"
 },
 "freshness": {
  "latest_partition": "2026-06-23",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 78,
  "note": "a closed historical delivery (the Commonwealth custody ended at the 2026-06-23 cut-over): lag is not staleness",
  "claim": "measured"
 },
 "size": {
  "objects": 1,
  "bytes": 145773,
  "rows": 1450,
  "schema_variants": 1,
  "columns_union": 15,
  "claim": "measured"
 },
 "columns": [
  {"name": "old_account", "type": "string", "nullable": true},
  {"name": "advisor_id", "type": "string", "nullable": true},
  {"name": "first_trade", "type": "date32[day]", "nullable": true},
  {"name": "last_trade", "type": "date32[day]", "nullable": true},
  {"name": "end_positions", "type": "int64", "nullable": true},
  {"name": "status", "type": "string", "nullable": true},
  {"name": "new_account", "type": "string", "nullable": true},
  {"name": "new_advisor_id", "type": "string", "nullable": true},
  {"name": "score", "type": "double", "nullable": true},
  {"name": "matched", "type": "int64", "nullable": true},
  {"name": "reason", "type": "string", "nullable": true},
  {"name": "evidence", "type": "string", "nullable": true},
  {"name": "client_line", "type": "string", "nullable": true, "pii": true},
  {"name": "newest_account", "type": "string", "nullable": true},
  {"name": "newest_open", "type": "bool", "nullable": true}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment commonwealth/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "old_account (+ new_account, newest_account)",
   "last4_derivation": "last 4 characters of the account string; ids are 7 to 17 characters long (measured), so last-4 is a weak key",
   "last4_collisions_within_firm": 352,
   "accounts_in_collisions": 731,
   "denominator_accounts": 1533,
   "basis": "measured on every transactions part (the delivery account universe); positions alone: 83 accounts, 0 collisions",
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment commonwealth/ (custodian and broker-dealer Commonwealth); Advisor_ID carries the rep code (4 advisor ids in transactions)",
   "values": [
    "commonwealth"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "account link",
  "account migration",
  "commonwealth",
  "cottonwood",
  "legacy custodian",
  "pre-2026-06-23 history"
 ],
 "common_queries": [
  "Which new account did Commonwealth account ...1234 become?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "commonwealth_resolve_account",
   "inputs": {
    "firm": "cottonwood",
    "account_last4": "1234",
    "platform": "commonwealth",
    "as_of": "YYYY-MM-DD (<= 2026-06-23)"
   },
   "returns": "rows of this table for the resolved account(s); a last-4 matching several accounts returns the candidates",
   "answers": [
    "Which new account did Commonwealth account ...1234 become?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "data/assets/scripts/silver/commonwealth_*.py; data/assets/scripts/gold/irpt_reporting/sources.json key _commonwealth_delivery (empty object) @bc91e712ad",
 "open_items": [
  "carries a free-text client line (pii:true): project it away"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=commonwealth/ (12 pages, 11,155 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 1 parquet parts of commonwealth/cottonwood/silver/account_links/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "projected read of Account_Number/AccountNumber/account columns",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

### `opal-data-assets/silver/commonwealth_cottonwood_coverage`

```json
{
 "contract_id": "opal-data-assets/silver/commonwealth_cottonwood_coverage",
 "bucket": "opal-data-assets",
 "s3_prefix": "commonwealth/cottonwood/silver/coverage/",
 "layer": "silver",
 "format": "parquet",
 "table": "coverage",
 "grain": "one row per source record kind (5 rows)",
 "description": "Coverage census of the delivery: earliest/latest date, rows, distinct accounts per source file.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "one delivery partition date=2026-06-23",
  "claim": "measured"
 },
 "producer": {
  "name": "data/assets/scripts/silver/commonwealth_coverage.py",
  "schedule": "none: a one-time historical delivery (bronze date=2026-06-23 only), converted by hand-run scripts 2026-10-06..10-09",
  "claim": "inferred"
 },
 "freshness": {
  "latest_partition": "2026-06-23",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 78,
  "note": "a closed historical delivery (the Commonwealth custody ended at the 2026-06-23 cut-over): lag is not staleness",
  "claim": "measured"
 },
 "size": {
  "objects": 1,
  "bytes": 3315,
  "rows": 5,
  "schema_variants": 1,
  "columns_union": 8,
  "claim": "measured"
 },
 "columns": [
  {"name": "record_kind", "type": "string", "nullable": true},
  {"name": "source_file", "type": "string", "nullable": true},
  {"name": "date_column", "type": "string", "nullable": true},
  {"name": "earliest", "type": "date32[day]", "nullable": true},
  {"name": "latest", "type": "date32[day]", "nullable": true},
  {"name": "rows", "type": "int64", "nullable": true},
  {"name": "distinct_accounts", "type": "int64", "nullable": true},
  {"name": "note", "type": "string", "nullable": true}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment commonwealth/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "none",
   "last4_derivation": "n/a",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment commonwealth/ (custodian and broker-dealer Commonwealth); Advisor_ID carries the rep code (4 advisor ids in transactions)",
   "values": [
    "commonwealth"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "coverage",
  "delivery census",
  "commonwealth",
  "cottonwood",
  "legacy custodian",
  "pre-2026-06-23 history"
 ],
 "common_queries": [
  "What date range does the Commonwealth delivery cover?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "commonwealth_describe_delivery",
   "inputs": {
    "firm": "cottonwood",
    "account_last4": "1234",
    "platform": "commonwealth",
    "as_of": "YYYY-MM-DD (<= 2026-06-23)"
   },
   "returns": "rows of this table for the resolved account(s); a last-4 matching several accounts returns the candidates",
   "answers": [
    "What date range does the Commonwealth delivery cover?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "data/assets/scripts/silver/commonwealth_*.py; data/assets/scripts/gold/irpt_reporting/sources.json key _commonwealth_delivery (empty object) @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=commonwealth/ (12 pages, 11,155 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 1 parquet parts of commonwealth/cottonwood/silver/coverage/",
   "at": "2026-10-14T13:12Z..13:25Z"
  }
 ]
}
```

### `opal-data-assets/silver/commonwealth_cottonwood_crosswalk`

```json
{
 "contract_id": "opal-data-assets/silver/commonwealth_cottonwood_crosswalk",
 "bucket": "opal-data-assets",
 "s3_prefix": "commonwealth/cottonwood/silver/crosswalk/",
 "layer": "silver",
 "format": "parquet",
 "table": "crosswalk",
 "grain": "one row per Commonwealth account (1,533 rows)",
 "description": "Commonwealth account to current account crosswalk (MATCHED 471, NOT_MATCHED 1,062) with rule, score and evidence.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "one delivery partition date=2026-06-23",
  "claim": "measured"
 },
 "producer": {
  "name": "data/assets/scripts/silver/commonwealth_crosswalk.py",
  "schedule": "none: a one-time historical delivery (bronze date=2026-06-23 only), converted by hand-run scripts 2026-10-06..10-09",
  "claim": "inferred"
 },
 "freshness": {
  "latest_partition": "2026-06-23",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 78,
  "note": "a closed historical delivery (the Commonwealth custody ended at the 2026-06-23 cut-over): lag is not staleness",
  "claim": "measured"
 },
 "size": {
  "objects": 1,
  "bytes": 148093,
  "rows": 1533,
  "schema_variants": 1,
  "columns_union": 14,
  "claim": "measured"
 },
 "columns": [
  {"name": "commonwealth_account", "type": "string", "nullable": true},
  {"name": "normalized_account", "type": "string", "nullable": true},
  {"name": "status", "type": "string", "nullable": true},
  {"name": "rule", "type": "string", "nullable": true},
  {"name": "current_account", "type": "string", "nullable": true},
  {"name": "score", "type": "double", "nullable": true},
  {"name": "positions_compared", "type": "int64", "nullable": true},
  {"name": "positions_matched", "type": "int64", "nullable": true},
  {"name": "holdings_basis", "type": "string", "nullable": true},
  {"name": "last_activity", "type": "date32[day]", "nullable": true},
  {"name": "reason_code", "type": "string", "nullable": true},
  {"name": "reason", "type": "string", "nullable": true},
  {"name": "evidence", "type": "string", "nullable": true},
  {"name": "candidates", "type": "string", "nullable": true}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment commonwealth/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "commonwealth_account (+ current_account)",
   "last4_derivation": "last 4 characters of the account string; ids are 7 to 17 characters long (measured), so last-4 is a weak key",
   "last4_collisions_within_firm": 352,
   "accounts_in_collisions": 731,
   "denominator_accounts": 1533,
   "basis": "measured on every transactions part (the delivery account universe); positions alone: 83 accounts, 0 collisions",
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment commonwealth/ (custodian and broker-dealer Commonwealth); Advisor_ID carries the rep code (4 advisor ids in transactions)",
   "values": [
    "commonwealth"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "crosswalk",
  "account mapping",
  "commonwealth",
  "cottonwood",
  "legacy custodian",
  "pre-2026-06-23 history"
 ],
 "common_queries": [
  "What is the current account for Commonwealth account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "commonwealth_resolve_account",
   "inputs": {
    "firm": "cottonwood",
    "account_last4": "1234",
    "platform": "commonwealth",
    "as_of": "YYYY-MM-DD (<= 2026-06-23)"
   },
   "returns": "rows of this table for the resolved account(s); a last-4 matching several accounts returns the candidates",
   "answers": [
    "What is the current account for Commonwealth account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "data/assets/scripts/silver/commonwealth_*.py; data/assets/scripts/gold/irpt_reporting/sources.json key _commonwealth_delivery (empty object) @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=commonwealth/ (12 pages, 11,155 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 1 parquet parts of commonwealth/cottonwood/silver/crosswalk/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "projected read of Account_Number/AccountNumber/account columns",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

### `opal-data-assets/silver/commonwealth_cottonwood_daily_returns`

```json
{
 "contract_id": "opal-data-assets/silver/commonwealth_cottonwood_daily_returns",
 "bucket": "opal-data-assets",
 "s3_prefix": "commonwealth/cottonwood/silver/daily_returns/",
 "layer": "silver",
 "format": "parquet",
 "table": "daily_returns",
 "grain": "one row per account x date over 2013-04-03..2026-06-22",
 "description": "Daily value, flow and return per account rebuilt from the delivery.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "one delivery partition date=2026-06-23",
  "claim": "measured"
 },
 "producer": {
  "name": "data/assets/scripts/silver/commonwealth_daily_returns.py / commonwealth_account_return_daily.py",
  "schedule": "none: a one-time historical delivery (bronze date=2026-06-23 only), converted by hand-run scripts 2026-10-06..10-09",
  "claim": "inferred"
 },
 "freshness": {
  "latest_partition": "2026-06-23",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 78,
  "note": "a closed historical delivery (the Commonwealth custody ended at the 2026-06-23 cut-over): lag is not staleness",
  "claim": "measured"
 },
 "size": {
  "objects": 1,
  "bytes": 1651055,
  "rows": 1691729,
  "schema_variants": 1,
  "columns_union": 8,
  "claim": "measured"
 },
 "columns": [
  {"name": "account", "type": "string", "nullable": true},
  {"name": "date", "type": "date32[day]", "nullable": true},
  {"name": "value", "type": "double", "nullable": true},
  {"name": "flow", "type": "double", "nullable": true},
  {"name": "return", "type": "double", "nullable": true},
  {"name": "blank_reason", "type": "string", "nullable": true},
  {"name": "cash_leg", "type": "string", "nullable": true},
  {"name": "run_commit", "type": "string", "nullable": true}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment commonwealth/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "account",
   "last4_derivation": "last 4 characters of the account string; ids are 7 to 17 characters long (measured), so last-4 is a weak key",
   "last4_collisions_within_firm": 352,
   "accounts_in_collisions": 731,
   "denominator_accounts": 1533,
   "basis": "measured on every transactions part (the delivery account universe); positions alone: 83 accounts, 0 collisions",
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment commonwealth/ (custodian and broker-dealer Commonwealth); Advisor_ID carries the rep code (4 advisor ids in transactions)",
   "values": [
    "commonwealth"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "returns",
  "daily returns",
  "performance history",
  "commonwealth",
  "cottonwood",
  "legacy custodian",
  "pre-2026-06-23 history"
 ],
 "common_queries": [
  "What was the return of account ...1234 in 2019?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "commonwealth_get_account_history",
   "inputs": {
    "firm": "cottonwood",
    "account_last4": "1234",
    "platform": "commonwealth",
    "as_of": "YYYY-MM-DD (<= 2026-06-23)"
   },
   "returns": "rows of this table for the resolved account(s); a last-4 matching several accounts returns the candidates",
   "answers": [
    "What was the return of account ...1234 in 2019?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "data/assets/scripts/silver/commonwealth_*.py; data/assets/scripts/gold/irpt_reporting/sources.json key _commonwealth_delivery (empty object) @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=commonwealth/ (12 pages, 11,155 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 1 parquet parts of commonwealth/cottonwood/silver/daily_returns/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "projected read of Account_Number/AccountNumber/account columns",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

### `opal-data-assets/silver/commonwealth_cottonwood_document_index`

```json
{
 "contract_id": "opal-data-assets/silver/commonwealth_cottonwood_document_index",
 "bucket": "opal-data-assets",
 "s3_prefix": "commonwealth/cottonwood/silver/document_index/",
 "layer": "silver",
 "format": "parquet",
 "table": "document_index",
 "grain": "two objects: archives.parquet (one row per source archive, 3 rows) and document_index.parquet (one row per document)",
 "description": "Index of the delivered client documents: doc type, account, doc date, page count, rep codes, archive paths.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "one delivery partition date=2026-06-23",
  "claim": "measured"
 },
 "producer": {
  "name": "data/assets/scripts/silver/commonwealth_document_index.py",
  "schedule": "none: a one-time historical delivery (bronze date=2026-06-23 only), converted by hand-run scripts 2026-10-06..10-09",
  "claim": "inferred"
 },
 "freshness": {
  "latest_partition": "2026-06-23",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 78,
  "note": "a closed historical delivery (the Commonwealth custody ended at the 2026-06-23 cut-over): lag is not staleness",
  "claim": "measured"
 },
 "size": {
  "objects": 2,
  "bytes": 1433009,
  "rows": 11122,
  "schema_variants": 2,
  "columns_union": 21,
  "claim": "measured"
 },
 "columns": [
  {"name": "archive", "type": "string", "nullable": true},
  {"name": "source_zip_sha256", "type": "string", "nullable": true, "pii": true},
  {"name": "size_bytes", "type": "int64", "nullable": true},
  {"name": "pdfs", "type": "int64", "nullable": true},
  {"name": "listings", "type": "int64", "nullable": true},
  {"name": "listing_rows", "type": "int64", "nullable": true},
  {"name": "document_id", "type": "string", "nullable": true},
  {"name": "file_name", "type": "string", "nullable": true},
  {"name": "doc_type", "type": "string", "nullable": true},
  {"name": "account", "type": "string", "nullable": true},
  {"name": "doc_date", "type": "date32[day]", "nullable": true},
  {"name": "date_source", "type": "string", "nullable": true},
  {"name": "doc_name", "type": "string", "nullable": true},
  {"name": "page_count", "type": "int64", "nullable": true},
  {"name": "rep_codes", "type": "list<element: string>", "nullable": true},
  {"name": "archives", "type": "list<element: string>", "nullable": true},
  {"name": "paths", "type": "list<element: string>", "nullable": true},
  {"name": "listed", "type": "bool", "nullable": true},
  {"name": "present", "type": "bool", "nullable": true},
  {"name": "listing_files", "type": "list<element: string>", "nullable": true},
  {"name": "listing_fields", "type": "map<string, string ('listing_fields')>", "nullable": true}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment commonwealth/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "account",
   "last4_derivation": "last 4 characters of the account string; ids are 7 to 17 characters long (measured), so last-4 is a weak key",
   "last4_collisions_within_firm": 352,
   "accounts_in_collisions": 731,
   "denominator_accounts": 1533,
   "basis": "measured on every transactions part (the delivery account universe); positions alone: 83 accounts, 0 collisions",
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment commonwealth/ (custodian and broker-dealer Commonwealth); Advisor_ID carries the rep code (4 advisor ids in transactions)",
   "values": [
    "commonwealth"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "documents",
  "statements",
  "document index",
  "commonwealth",
  "cottonwood",
  "legacy custodian",
  "pre-2026-06-23 history"
 ],
 "common_queries": [
  "Which statements exist for account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "commonwealth_find_documents",
   "inputs": {
    "firm": "cottonwood",
    "account_last4": "1234",
    "platform": "commonwealth",
    "as_of": "YYYY-MM-DD (<= 2026-06-23)"
   },
   "returns": "rows of this table for the resolved account(s); a last-4 matching several accounts returns the candidates",
   "answers": [
    "Which statements exist for account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "data/assets/scripts/silver/commonwealth_*.py; data/assets/scripts/gold/irpt_reporting/sources.json key _commonwealth_delivery (empty object) @bc91e712ad",
 "open_items": [
  "the PDFs are client documents (11,120 objects, 1.80 GB under documents/); a tool returns metadata and a gateway-ticketed link, never bytes inline",
  "2 schema variants across the 2 objects (different tables in one prefix)"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=commonwealth/ (12 pages, 11,155 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 2 parquet parts of commonwealth/cottonwood/silver/document_index/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "projected read of Account_Number/AccountNumber/account columns",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

### `opal-data-assets/silver/commonwealth_cottonwood_documents`

```json
{
 "contract_id": "opal-data-assets/silver/commonwealth_cottonwood_documents",
 "bucket": "opal-data-assets",
 "s3_prefix": "commonwealth/cottonwood/silver/documents/",
 "layer": "silver",
 "format": "parquet",
 "table": "documents",
 "grain": "one row per extracted document (11,119 rows); the PDFs sit beside it under doc_type= partitions",
 "description": "Document landing manifest: document id, type, account, date, bytes, sha256, written key, status/refusal.",
 "partition": {
  "keys": [
   "date",
   "doc_type"
  ],
  "form": "one delivery partition date=2026-06-23",
  "claim": "measured"
 },
 "producer": {
  "name": "data/assets/scripts/silver/commonwealth_documents.py",
  "schedule": "none: a one-time historical delivery (bronze date=2026-06-23 only), converted by hand-run scripts 2026-10-06..10-09",
  "claim": "inferred"
 },
 "freshness": {
  "latest_partition": "2026-06-23",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 78,
  "note": "a closed historical delivery (the Commonwealth custody ended at the 2026-06-23 cut-over): lag is not staleness",
  "claim": "measured"
 },
 "size": {
  "objects": 1,
  "bytes": 1721245,
  "rows": 11119,
  "schema_variants": 1,
  "columns_union": 12,
  "claim": "measured"
 },
 "columns": [
  {"name": "document_id", "type": "string", "nullable": true},
  {"name": "doc_type", "type": "string", "nullable": true},
  {"name": "account", "type": "string", "nullable": true},
  {"name": "doc_date", "type": "date32[day]", "nullable": true},
  {"name": "source_path", "type": "string", "nullable": true},
  {"name": "bytes", "type": "int64", "nullable": true},
  {"name": "crc32", "type": "string", "nullable": true},
  {"name": "target_key", "type": "string", "nullable": true},
  {"name": "status", "type": "string", "nullable": true},
  {"name": "refusal", "type": "string", "nullable": true},
  {"name": "sha256", "type": "string", "nullable": true},
  {"name": "written_key", "type": "string", "nullable": true}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment commonwealth/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "account",
   "last4_derivation": "last 4 characters of the account string; ids are 7 to 17 characters long (measured), so last-4 is a weak key",
   "last4_collisions_within_firm": 352,
   "accounts_in_collisions": 731,
   "denominator_accounts": 1533,
   "basis": "measured on every transactions part (the delivery account universe); positions alone: 83 accounts, 0 collisions",
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment commonwealth/ (custodian and broker-dealer Commonwealth); Advisor_ID carries the rep code (4 advisor ids in transactions)",
   "values": [
    "commonwealth"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "documents",
  "pdf",
  "statements",
  "commonwealth",
  "cottonwood",
  "legacy custodian",
  "pre-2026-06-23 history"
 ],
 "common_queries": [
  "Where is the PDF of document X?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "commonwealth_find_documents",
   "inputs": {
    "firm": "cottonwood",
    "account_last4": "1234",
    "platform": "commonwealth",
    "as_of": "YYYY-MM-DD (<= 2026-06-23)"
   },
   "returns": "rows of this table for the resolved account(s); a last-4 matching several accounts returns the candidates",
   "answers": [
    "Where is the PDF of document X?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "data/assets/scripts/silver/commonwealth_*.py; data/assets/scripts/gold/irpt_reporting/sources.json key _commonwealth_delivery (empty object) @bc91e712ad",
 "open_items": [
  "the PDFs are client documents (11,120 objects, 1.80 GB under documents/); a tool returns metadata and a gateway-ticketed link, never bytes inline"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=commonwealth/ (12 pages, 11,155 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 1 parquet parts of commonwealth/cottonwood/silver/documents/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "projected read of Account_Number/AccountNumber/account columns",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

### `opal-data-assets/silver/commonwealth_cottonwood_month_grades`

```json
{
 "contract_id": "opal-data-assets/silver/commonwealth_cottonwood_month_grades",
 "bucket": "opal-data-assets",
 "s3_prefix": "commonwealth/cottonwood/silver/month_grades/",
 "layer": "silver",
 "format": "parquet",
 "table": "month_grades",
 "grain": "one row per account x month 2013-04..2026-06 (82,593 rows)",
 "description": "Computed vs reported monthly return grades (UNGRADABLE 78,622, MATCH 3,678, DIFF 288) with benchmark figures.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "one delivery partition date=2026-06-23",
  "claim": "measured"
 },
 "producer": {
  "name": "data/assets/scripts/silver/commonwealth_monthly_grade.py",
  "schedule": "none: a one-time historical delivery (bronze date=2026-06-23 only), converted by hand-run scripts 2026-10-06..10-09",
  "claim": "inferred"
 },
 "freshness": {
  "latest_partition": "2026-06-23",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 78,
  "note": "a closed historical delivery (the Commonwealth custody ended at the 2026-06-23 cut-over): lag is not staleness",
  "claim": "measured"
 },
 "size": {
  "objects": 1,
  "bytes": 421751,
  "rows": 82593,
  "schema_variants": 1,
  "columns_union": 21,
  "claim": "measured"
 },
 "columns": [
  {"name": "account", "type": "string", "nullable": true},
  {"name": "month", "type": "string", "nullable": true},
  {"name": "computed_pct", "type": "double", "nullable": true},
  {"name": "reported_month_pct", "type": "double", "nullable": true},
  {"name": "diff_pct", "type": "double", "nullable": true},
  {"name": "verdict", "type": "string", "nullable": true},
  {"name": "reason", "type": "string", "nullable": true},
  {"name": "reported_year_pct", "type": "double", "nullable": true},
  {"name": "reported_year_start", "type": "date32[day]", "nullable": true},
  {"name": "reported_year_end", "type": "date32[day]", "nullable": true},
  {"name": "reported_itd_pct", "type": "double", "nullable": true},
  {"name": "reported_itd_start", "type": "date32[day]", "nullable": true},
  {"name": "reported_itd_end", "type": "date32[day]", "nullable": true},
  {"name": "benchmark_month_pct", "type": "double", "nullable": true},
  {"name": "benchmark_year_pct", "type": "double", "nullable": true},
  {"name": "benchmark_itd_pct", "type": "double", "nullable": true},
  {"name": "benchmark_description", "type": "string", "nullable": true},
  {"name": "reported_note", "type": "string", "nullable": true},
  {"name": "list_version", "type": "string", "nullable": true},
  {"name": "cash_leg", "type": "string", "nullable": true},
  {"name": "run_commit", "type": "string", "nullable": true}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment commonwealth/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "account",
   "last4_derivation": "last 4 characters of the account string; ids are 7 to 17 characters long (measured), so last-4 is a weak key",
   "last4_collisions_within_firm": 352,
   "accounts_in_collisions": 731,
   "denominator_accounts": 1533,
   "basis": "measured on every transactions part (the delivery account universe); positions alone: 83 accounts, 0 collisions",
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment commonwealth/ (custodian and broker-dealer Commonwealth); Advisor_ID carries the rep code (4 advisor ids in transactions)",
   "values": [
    "commonwealth"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "monthly returns",
  "performance grading",
  "benchmark",
  "commonwealth",
  "cottonwood",
  "legacy custodian",
  "pre-2026-06-23 history"
 ],
 "common_queries": [
  "Does the rebuilt return of account ...1234 match the reported one for 2020-03?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "commonwealth_get_performance",
   "inputs": {
    "firm": "cottonwood",
    "account_last4": "1234",
    "platform": "commonwealth",
    "as_of": "YYYY-MM-DD (<= 2026-06-23)"
   },
   "returns": "rows of this table for the resolved account(s); a last-4 matching several accounts returns the candidates",
   "answers": [
    "Does the rebuilt return of account ...1234 match the reported one for 2020-03?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "data/assets/scripts/silver/commonwealth_*.py; data/assets/scripts/gold/irpt_reporting/sources.json key _commonwealth_delivery (empty object) @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=commonwealth/ (12 pages, 11,155 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 1 parquet parts of commonwealth/cottonwood/silver/month_grades/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "projected read of Account_Number/AccountNumber/account columns",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

### `opal-data-assets/silver/commonwealth_cottonwood_performance`

```json
{
 "contract_id": "opal-data-assets/silver/commonwealth_cottonwood_performance",
 "bucket": "opal-data-assets",
 "s3_prefix": "commonwealth/cottonwood/silver/performance/",
 "layer": "silver",
 "format": "parquet",
 "table": "performance",
 "grain": "one row per account x reporting period x perf type (Month 80,709, Year 6,425, InceptionToDate 1,520)",
 "description": "Vendor-reported performance (PerfNum, benchmark) partitioned by reporting_period.",
 "partition": {
  "keys": [
   "date",
   "reporting_period"
  ],
  "form": "one delivery partition date=2026-06-23",
  "claim": "measured"
 },
 "producer": {
  "name": "commonwealth bronze portfolio_accounting conversion",
  "schedule": "none: a one-time historical delivery (bronze date=2026-06-23 only), converted by hand-run scripts 2026-10-06..10-09",
  "claim": "inferred"
 },
 "freshness": {
  "latest_partition": "2026-06-23",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 78,
  "note": "a closed historical delivery (the Commonwealth custody ended at the 2026-06-23 cut-over): lag is not staleness",
  "claim": "measured"
 },
 "size": {
  "objects": 3,
  "bytes": 842764,
  "rows": 88654,
  "schema_variants": 1,
  "columns_union": 18,
  "claim": "measured"
 },
 "columns": [
  {"name": "Advisor_ID", "type": "string", "nullable": true},
  {"name": "Account_Number", "type": "string", "nullable": true},
  {"name": "ReportingPeriod", "type": "string", "nullable": true},
  {"name": "PerfType", "type": "string", "nullable": true},
  {"name": "NetGross", "type": "bool", "nullable": true},
  {"name": "Annualize", "type": "bool", "nullable": true},
  {"name": "StartDate", "type": "date32[day]", "nullable": true},
  {"name": "EndDate", "type": "date32[day]", "nullable": true},
  {"name": "PerfNum", "type": "double", "nullable": true},
  {"name": "BenchMark1Value", "type": "double", "nullable": true},
  {"name": "BenchMark1Description", "type": "string", "nullable": true},
  {"name": "Account_Status", "type": "string", "nullable": true},
  {"name": "AsOfDate", "type": "date32[day]", "nullable": true},
  {"name": "source_zip", "type": "string", "nullable": true, "pii": true},
  {"name": "source_zip_sha256", "type": "string", "nullable": true, "pii": true},
  {"name": "source_file", "type": "string", "nullable": true},
  {"name": "source_line", "type": "int64", "nullable": true},
  {"name": "source_record", "type": "int64", "nullable": true}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment commonwealth/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "Account_Number",
   "last4_derivation": "last 4 characters of the account string; ids are 7 to 17 characters long (measured), so last-4 is a weak key",
   "last4_collisions_within_firm": 352,
   "accounts_in_collisions": 731,
   "denominator_accounts": 1533,
   "basis": "measured on every transactions part (the delivery account universe); positions alone: 83 accounts, 0 collisions",
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment commonwealth/ (custodian and broker-dealer Commonwealth); Advisor_ID carries the rep code (4 advisor ids in transactions)",
   "values": [
    "commonwealth"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "performance",
  "reported returns",
  "benchmark",
  "commonwealth",
  "cottonwood",
  "legacy custodian",
  "pre-2026-06-23 history"
 ],
 "common_queries": [
  "What was the reported inception-to-date return of account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "commonwealth_get_performance",
   "inputs": {
    "firm": "cottonwood",
    "account_last4": "1234",
    "platform": "commonwealth",
    "as_of": "YYYY-MM-DD (<= 2026-06-23)"
   },
   "returns": "rows of this table for the resolved account(s); a last-4 matching several accounts returns the candidates",
   "answers": [
    "What was the reported inception-to-date return of account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "data/assets/scripts/silver/commonwealth_*.py; data/assets/scripts/gold/irpt_reporting/sources.json key _commonwealth_delivery (empty object) @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=commonwealth/ (12 pages, 11,155 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 3 parquet parts of commonwealth/cottonwood/silver/performance/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "projected read of Account_Number/AccountNumber/account columns",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

### `opal-data-assets/silver/commonwealth_cottonwood_positions`

```json
{
 "contract_id": "opal-data-assets/silver/commonwealth_cottonwood_positions",
 "bucket": "opal-data-assets",
 "s3_prefix": "commonwealth/cottonwood/silver/positions/",
 "layer": "silver",
 "format": "parquet",
 "table": "positions",
 "grain": "one row per account x security as of 2026-06-23 (469 rows, all Position_Type CASH, 83 accounts)",
 "description": "Final positions file of the delivery (only CASH rows remain).",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "one delivery partition date=2026-06-23",
  "claim": "measured"
 },
 "producer": {
  "name": "commonwealth bronze portfolio_accounting conversion",
  "schedule": "none: a one-time historical delivery (bronze date=2026-06-23 only), converted by hand-run scripts 2026-10-06..10-09",
  "claim": "inferred"
 },
 "freshness": {
  "latest_partition": "2026-06-23",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 78,
  "note": "a closed historical delivery (the Commonwealth custody ended at the 2026-06-23 cut-over): lag is not staleness",
  "claim": "measured"
 },
 "size": {
  "objects": 1,
  "bytes": 17152,
  "rows": 469,
  "schema_variants": 1,
  "columns_union": 16,
  "claim": "measured"
 },
 "columns": [
  {"name": "Advisor_ID", "type": "string", "nullable": true},
  {"name": "AccountNumber", "type": "string", "nullable": true},
  {"name": "Cusip", "type": "string", "nullable": true},
  {"name": "FundCode", "type": "string", "nullable": true},
  {"name": "Symbol", "type": "string", "nullable": true},
  {"name": "Security_Description", "type": "string", "nullable": true},
  {"name": "Quantity", "type": "double", "nullable": true},
  {"name": "LongShort_Indicator", "type": "string", "nullable": true},
  {"name": "Position_Type", "type": "string", "nullable": true},
  {"name": "AsOfDate", "type": "date32[day]", "nullable": true},
  {"name": "Account_Status", "type": "string", "nullable": true},
  {"name": "source_zip", "type": "string", "nullable": true, "pii": true},
  {"name": "source_zip_sha256", "type": "string", "nullable": true, "pii": true},
  {"name": "source_file", "type": "string", "nullable": true},
  {"name": "source_line", "type": "int64", "nullable": true},
  {"name": "source_record", "type": "int64", "nullable": true}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment commonwealth/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "AccountNumber",
   "last4_derivation": "last 4 characters of the account string; ids are 7 to 17 characters long (measured), so last-4 is a weak key",
   "last4_collisions_within_firm": 352,
   "accounts_in_collisions": 731,
   "denominator_accounts": 1533,
   "basis": "measured on every transactions part (the delivery account universe); positions alone: 83 accounts, 0 collisions",
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment commonwealth/ (custodian and broker-dealer Commonwealth); Advisor_ID carries the rep code (4 advisor ids in transactions)",
   "values": [
    "commonwealth"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "positions",
  "final holdings",
  "commonwealth",
  "cottonwood",
  "legacy custodian",
  "pre-2026-06-23 history"
 ],
 "common_queries": [
  "What cash did account ...1234 hold at the 2026-06-23 cut-over?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "commonwealth_get_account_history",
   "inputs": {
    "firm": "cottonwood",
    "account_last4": "1234",
    "platform": "commonwealth",
    "as_of": "YYYY-MM-DD (<= 2026-06-23)"
   },
   "returns": "rows of this table for the resolved account(s); a last-4 matching several accounts returns the candidates",
   "answers": [
    "What cash did account ...1234 hold at the 2026-06-23 cut-over?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "data/assets/scripts/silver/commonwealth_*.py; data/assets/scripts/gold/irpt_reporting/sources.json key _commonwealth_delivery (empty object) @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=commonwealth/ (12 pages, 11,155 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 1 parquet parts of commonwealth/cottonwood/silver/positions/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "projected read of Account_Number/AccountNumber/account columns",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

### `opal-data-assets/silver/commonwealth_cottonwood_price_evidence`

```json
{
 "contract_id": "opal-data-assets/silver/commonwealth_cottonwood_price_evidence",
 "bucket": "opal-data-assets",
 "s3_prefix": "commonwealth/cottonwood/silver/price_evidence/",
 "layer": "silver",
 "format": "parquet",
 "table": "price_evidence",
 "grain": "one row per cusip price evidence (2 rows), partition date=2022-10-12",
 "description": "Price/split evidence rows used by the valuation rebuild.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=2022-10-12 (evidence date)",
  "claim": "measured"
 },
 "producer": {
  "name": "data/assets/scripts/silver/commonwealth_split_level_probe.py",
  "schedule": "none: a one-time historical delivery (bronze date=2026-06-23 only), converted by hand-run scripts 2026-10-06..10-09",
  "claim": "inferred"
 },
 "freshness": {
  "latest_partition": "2022-10-12",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": null,
  "note": "a closed historical delivery (the Commonwealth custody ended at the 2026-06-23 cut-over): lag is not staleness",
  "claim": "measured"
 },
 "size": {
  "objects": 1,
  "bytes": 5940,
  "rows": 2,
  "schema_variants": 1,
  "columns_union": 9,
  "claim": "measured"
 },
 "columns": [
  {"name": "cusip", "type": "large_string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "symbol", "type": "large_string", "nullable": true},
  {"name": "symbol_source", "type": "large_string", "nullable": true},
  {"name": "close", "type": "double", "nullable": true},
  {"name": "splits", "type": "large_string", "nullable": true},
  {"name": "factor", "type": "double", "nullable": true},
  {"name": "as_traded", "type": "double", "nullable": true},
  {"name": "as_of", "type": "large_string", "nullable": true},
  {"name": "source", "type": "large_string", "nullable": true}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment commonwealth/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "none",
   "last4_derivation": "n/a",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment commonwealth/ (custodian and broker-dealer Commonwealth); Advisor_ID carries the rep code (4 advisor ids in transactions)",
   "values": [
    "commonwealth"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "price evidence",
  "splits",
  "commonwealth",
  "cottonwood",
  "legacy custodian",
  "pre-2026-06-23 history"
 ],
 "common_queries": [
  "What price evidence backs CUSIP X on 2022-10-12?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "commonwealth_describe_delivery",
   "inputs": {
    "firm": "cottonwood",
    "account_last4": "1234",
    "platform": "commonwealth",
    "as_of": "YYYY-MM-DD (<= 2026-06-23)"
   },
   "returns": "rows of this table for the resolved account(s); a last-4 matching several accounts returns the candidates",
   "answers": [
    "What price evidence backs CUSIP X on 2022-10-12?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "data/assets/scripts/silver/commonwealth_*.py; data/assets/scripts/gold/irpt_reporting/sources.json key _commonwealth_delivery (empty object) @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=commonwealth/ (12 pages, 11,155 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 1 parquet parts of commonwealth/cottonwood/silver/price_evidence/",
   "at": "2026-10-14T13:12Z..13:25Z"
  }
 ]
}
```

### `opal-data-assets/silver/commonwealth_cottonwood_transactions`

```json
{
 "contract_id": "opal-data-assets/silver/commonwealth_cottonwood_transactions",
 "bucket": "opal-data-assets",
 "s3_prefix": "commonwealth/cottonwood/silver/transactions/",
 "layer": "silver",
 "format": "parquet",
 "table": "transactions",
 "grain": "one row per transaction 2013-04-03..2026-06-22 (1,416,497 rows), partitioned by trade_year",
 "description": "Vendor transactions of the delivery: type, description, cusip, quantity, amount, dates, asset type, corporate-action id.",
 "partition": {
  "keys": [
   "date",
   "trade_year"
  ],
  "form": "one delivery partition date=2026-06-23",
  "claim": "measured"
 },
 "producer": {
  "name": "data/assets/scripts/silver/commonwealth_transactions.py",
  "schedule": "none: a one-time historical delivery (bronze date=2026-06-23 only), converted by hand-run scripts 2026-10-06..10-09",
  "claim": "inferred"
 },
 "freshness": {
  "latest_partition": "2026-06-23",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 78,
  "note": "a closed historical delivery (the Commonwealth custody ended at the 2026-06-23 cut-over): lag is not staleness",
  "claim": "measured"
 },
 "size": {
  "objects": 14,
  "bytes": 29395850,
  "rows": 1416497,
  "schema_variants": 1,
  "columns_union": 25,
  "claim": "measured"
 },
 "columns": [
  {"name": "Advisor_ID", "type": "string", "nullable": true},
  {"name": "Account_Number", "type": "string", "nullable": true},
  {"name": "Transaction_Type", "type": "string", "nullable": true},
  {"name": "Transaction_Description", "type": "string", "nullable": true},
  {"name": "Cusip", "type": "string", "nullable": true},
  {"name": "FundCode", "type": "string", "nullable": true},
  {"name": "Symbol", "type": "string", "nullable": true},
  {"name": "Quantity", "type": "double", "nullable": true},
  {"name": "Amount", "type": "double", "nullable": true},
  {"name": "AI", "type": "double", "nullable": true},
  {"name": "Trade_Date", "type": "date32[day]", "nullable": true},
  {"name": "Cost_Date", "type": "date32[day]", "nullable": true},
  {"name": "Settle_Date", "type": "date32[day]", "nullable": true},
  {"name": "Asset_Type", "type": "string", "nullable": true},
  {"name": "CA_Event_Id", "type": "string", "nullable": true},
  {"name": "LongShort_Indicator", "type": "string", "nullable": true},
  {"name": "Position_Type", "type": "string", "nullable": true},
  {"name": "Security_Description", "type": "string", "nullable": true},
  {"name": "Transaction_Note", "type": "string", "nullable": true},
  {"name": "AsOfDate", "type": "date32[day]", "nullable": true},
  {"name": "source_zip", "type": "string", "nullable": true, "pii": true},
  {"name": "source_zip_sha256", "type": "string", "nullable": true, "pii": true},
  {"name": "source_file", "type": "string", "nullable": true},
  {"name": "source_line", "type": "int64", "nullable": true},
  {"name": "source_record", "type": "int64", "nullable": true}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment commonwealth/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "Account_Number",
   "last4_derivation": "last 4 characters of the account string; ids are 7 to 17 characters long (measured), so last-4 is a weak key",
   "last4_collisions_within_firm": 352,
   "accounts_in_collisions": 731,
   "denominator_accounts": 1533,
   "basis": "measured on every transactions part (the delivery account universe); positions alone: 83 accounts, 0 collisions",
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment commonwealth/ (custodian and broker-dealer Commonwealth); Advisor_ID carries the rep code (4 advisor ids in transactions)",
   "values": [
    "commonwealth"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "transactions",
  "history",
  "flows",
  "commonwealth",
  "cottonwood",
  "legacy custodian",
  "pre-2026-06-23 history"
 ],
 "common_queries": [
  "What transactions did account ...1234 have in 2018?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "commonwealth_list_transactions",
   "inputs": {
    "firm": "cottonwood",
    "account_last4": "1234",
    "platform": "commonwealth",
    "as_of": "YYYY-MM-DD (<= 2026-06-23)"
   },
   "returns": "rows of this table for the resolved account(s); a last-4 matching several accounts returns the candidates",
   "answers": [
    "What transactions did account ...1234 have in 2018?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "data/assets/scripts/silver/commonwealth_*.py; data/assets/scripts/gold/irpt_reporting/sources.json key _commonwealth_delivery (empty object) @bc91e712ad",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=commonwealth/ (12 pages, 11,155 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 14 parquet parts of commonwealth/cottonwood/silver/transactions/",
   "at": "2026-10-14T13:12Z..13:25Z"
  },
  {
   "read": "projected read of Account_Number/AccountNumber/account columns",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

### `opal-data-assets/silver/gateway_global_taxsma_workbook`

```json
{
 "contract_id": "opal-data-assets/silver/gateway_global_taxsma_workbook",
 "bucket": "opal-data-assets",
 "s3_prefix": "gateway/global/silver/taxsma_workbook/",
 "layer": "silver",
 "format": "parquet",
 "table": "taxsma_workbook",
 "grain": "one row per worksheet row of ONE workbook snapshot (ACCOUNT_SLOT / BLANK / TOTAL / UNRECOGNIZED); each part is a FULL snapshot",
 "description": "Typed silver of the Tax SMA workbook read through GET /ms/taxsma-workbook: Index, Account Number, RIA, Strategy, AUM (Mn), Ready, Inception Date, Last Trade Date, Traded, each as a typed cell struct.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/<snapshot_id>-<response_sha256>.parquet, 1-4 parts per partition",
  "claim": "measured"
 },
 "producer": {
  "name": "MDPF_TAXSMA writer S19 (org/standards/MDPF_TAXSMA_DATA_CONTRACT.json v0.6.0 artifacts.workbook_silver); running inside mdpf-gold-lambda Tax prelude",
  "schedule": "daily, objects written ~13:58Z (measured LastModified); trigger inferred from the mdpf gold run",
  "claim": "inferred"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "claim": "measured"
 },
 "size": {
  "objects": 21,
  "partitions": 13,
  "rows_all_parts": 441,
  "rows_newest_part": 21,
  "row_count_rule": "snapshot per part: the newest partition holds 2 parts of 21 rows each (17 ACCOUNT_SLOT, 3 BLANK, 1 TOTAL), 0 duplicate accounts inside a part; the table row count is ONE part (21), never the sum",
  "schema_variants": 1,
  "claim": "measured"
 },
 "columns": [
  {"name": "row_number", "type": "int64", "nullable": true},
  {"name": "row_kind", "type": "string", "nullable": true},
  {"name": "other_business_cells_present", "type": "bool", "nullable": true},
  {"name": "Index", "type": "struct<kind: string, string_value: string, integer_value: int64, float_value: double, boolean_value: bool>", "nullable": true},
  {"name": "Account Number", "type": "struct<kind: string, string_value: string, integer_value: int64, float_value: double, boolean_value: bool>", "nullable": true},
  {"name": "RIA", "type": "struct<kind: string, string_value: string, integer_value: int64, float_value: double, boolean_value: bool>", "nullable": true},
  {"name": "Strategy", "type": "struct<kind: string, string_value: string, integer_value: int64, float_value: double, boolean_value: bool>", "nullable": true},
  {"name": "AUM (Mn)", "type": "struct<kind: string, string_value: string, integer_value: int64, float_value: double, boolean_value: bool>", "nullable": true},
  {"name": "Ready", "type": "struct<kind: string, string_value: string, integer_value: int64, float_value: double, boolean_value: bool>", "nullable": true},
  {"name": "Inception Date", "type": "struct<kind: string, string_value: string, integer_value: int64, float_value: double, boolean_value: bool>", "nullable": true},
  {"name": "Last Trade Date", "type": "struct<kind: string, string_value: string, integer_value: int64, float_value: double, boolean_value: bool>", "nullable": true},
  {"name": "Traded", "type": "struct<kind: string, string_value: string, integer_value: int64, float_value: double, boolean_value: bool>", "nullable": true}
 ],
 "enums": {
  "row_kind": [
   "ACCOUNT_SLOT",
   "BLANK",
   "TOTAL",
   "UNRECOGNIZED"
  ]
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "RIA cell (string_value); key scope is global because one sheet carries several firms",
   "values": [
    "49 Financial (14 rows)",
    "Cottonwood (3 rows)",
    "<empty> (4 rows)"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "Account Number (struct; string_value or integer_value)",
   "last4_derivation": "last 4 characters of the 9-digit number (all 15 measured length 9)",
   "last4_collisions_within_firm": 0,
   "denominator_accounts": 15,
   "claim": "measured"
  },
  "platform": {
   "column": "none; the Strategy cell names the strategy, the custodian is not carried",
   "values": [],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "tax sma",
  "tax sma workbook",
  "traded",
  "ready",
  "aum",
  "strategy",
  "mdpf"
 ],
 "common_queries": [
  "Is account ...1234 Ready and Traded on the Tax SMA sheet?",
  "What is the AUM and strategy of the Tax SMA accounts for 49 Financial?"
 ],
 "existing_gateway_tool": {
  "name": "none (GET /ms/taxsma-workbook is a route-only capability for the gold run, not an MCP tool)",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "taxsma_get_workbook_rows",
   "inputs": {
    "firm": "49financial|cottonwood (REQUIRED; filters the RIA cell)",
    "account_last4": "1234 (optional)",
    "platform": "n/a",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "the ACCOUNT_SLOT rows of the newest snapshot at or before as_of for that firm only; a row whose RIA is empty belongs to no firm and is never returned",
   "answers": [
    "Is account ...1234 Ready and Traded on the Tax SMA sheet?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "org/standards/MDPF_TAXSMA_DATA_CONTRACT.json v0.6.0; infra/aws/ec2/opal-gateway/app/taxsma_workbook.py @bc91e712ad",
 "open_items": [
  "multi-firm by construction (contract scope_note): the tool must take the firm and filter the RIA cell; 4 rows of 21 carry an empty RIA"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=gateway/ (1 page, 44 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of 21 parts; full read of the 2 parts of date=2026-10-13",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

### `opal-data-assets/silver/pathfinder_PFDE_fact_dailynav`

```json
{
 "contract_id": "opal-data-assets/silver/pathfinder_PFDE_fact_dailynav",
 "bucket": "opal-data-assets",
 "s3_prefix": "pathfinder/PFDE/silver/fact_dailynav/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_dailynav",
 "grain": "one row per fund per business date (1 row per partition)",
 "description": "Daily NAV file of the fund: net assets, shares outstanding, NAV and changes, market price, premium/discount, 30-day median spread.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-etf",
  "schedule": "S3 ObjectCreated on pathfinder/filepoint/bronze/ (bucket notification; .csv for pathfinder/filepoint, .html for trueshares) + rule opal-assets-silver-etf-sweep-daily cron(30 23 * * ? *) ENABLED",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "claim": "measured"
 },
 "size": {
  "objects": 91,
  "partitions": 91,
  "rows_all_partitions": 91,
  "rows_newest_partition": 1,
  "schema_variants": 1,
  "claim": "measured"
 },
 "columns": [
  {"name": "Fund Name", "type": "string", "nullable": true},
  {"name": "Fund Ticker", "type": "string", "nullable": true},
  {"name": "CUSIP", "type": "string", "nullable": true},
  {"name": "Net Assets", "type": "double", "nullable": true},
  {"name": "Shares Outstanding", "type": "double", "nullable": true},
  {"name": "NAV", "type": "double", "nullable": true},
  {"name": "NAV Change Dollars", "type": "double", "nullable": true},
  {"name": "NAV Change Percentage", "type": "double", "nullable": true},
  {"name": "Market Price", "type": "double", "nullable": true},
  {"name": "Market Price Change Dollars", "type": "double", "nullable": true},
  {"name": "Market Price Change Percentage", "type": "double", "nullable": true},
  {"name": "Premium/Discount Percentage", "type": "double", "nullable": true},
  {"name": "Rate Date", "type": "string", "nullable": true},
  {"name": "Median 30 Day Spread Percentage", "type": "double", "nullable": true},
  {"name": "rate_date_std", "type": "date32[day]", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_source", "type": "string", "nullable": true},
  {"name": "_feed", "type": "string", "nullable": true},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment pathfinder/PFDE/ (the fund ticker; Opal-issued fund, not a client firm)",
   "values": [
    "PFDE"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "none: fund data, no client account (the holdings Account column carries the fund ticker, measured PFDE on every row)",
   "last4_derivation": "n/a",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment names the fund administrator source (pathfinder)",
   "values": [
    "pathfinder"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "nav",
  "net assets",
  "premium discount",
  "fund price",
  "opal etf",
  "PFDE",
  "pathfinder"
 ],
 "common_queries": [
  "What was the NAV and net assets of PFDE on a date?"
 ],
 "existing_gateway_tool": {
  "name": "etfs_get_positioning (reads the portal-v2 positioning gold, DATA_CATALOG.yaml:1392)",
  "verdict": "keep"
 },
 "proposed_tools": [
  {
   "name": "etfs_get_fund_nav",
   "inputs": {
    "firm": "opal",
    "account_last4": "n/a",
    "platform": "pathfinder",
    "as_of": "YYYY-MM-DD",
    "fund_ticker": "PFDE"
   },
   "returns": "the rows of the newest partition at or before as_of",
   "answers": [
    "What was the NAV of PFDE on a date?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "channels row at DATA_CATALOG.yaml:395 names the four funds (served positioning, not this silver)",
  "present": false
 },
 "prior_art": "infra/aws/terraform/opal-assets/silver.tf silver_sweep_slots.etf @bc91e712ad",
 "open_items": [
  "G5 (opal-data-etfs) owns the ETF estate; these silver tables are the opal-data-assets landing of the same four funds: reconcile with G5 before cutting a tool"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=pathfinder/",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 91 parts; projected read of Account/date_std (holdings) or ticker/as-of (nav) on the newest part",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

### `opal-data-assets/silver/pathfinder_PFDE_fact_holdings`

```json
{
 "contract_id": "opal-data-assets/silver/pathfinder_PFDE_fact_holdings",
 "bucket": "opal-data-assets",
 "s3_prefix": "pathfinder/PFDE/silver/fact_holdings/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_holdings",
 "grain": "one row per fund holding per date (90 rows on 2026-10-13)",
 "description": "Daily ETF holdings file: ticker, cusip, name, shares, price, market value, weight, net assets, creation units.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-etf",
  "schedule": "S3 ObjectCreated on pathfinder/filepoint/bronze/ (bucket notification; .csv for pathfinder/filepoint, .html for trueshares) + rule opal-assets-silver-etf-sweep-daily cron(30 23 * * ? *) ENABLED",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "claim": "measured"
 },
 "size": {
  "objects": 91,
  "partitions": 91,
  "rows_all_partitions": 8099,
  "rows_newest_partition": 90,
  "schema_variants": 1,
  "claim": "measured"
 },
 "columns": [
  {"name": "Date", "type": "string", "nullable": true},
  {"name": "Account", "type": "string", "nullable": true},
  {"name": "StockTicker", "type": "string", "nullable": true},
  {"name": "CUSIP", "type": "string", "nullable": true},
  {"name": "SecurityName", "type": "string", "nullable": true},
  {"name": "Shares", "type": "double", "nullable": true},
  {"name": "Price", "type": "double", "nullable": true},
  {"name": "MarketValue", "type": "double", "nullable": true},
  {"name": "Weightings", "type": "string", "nullable": true},
  {"name": "NetAssets", "type": "double", "nullable": true},
  {"name": "SharesOutstanding", "type": "double", "nullable": true},
  {"name": "CreationUnits", "type": "double", "nullable": true},
  {"name": "MoneyMarketFlag", "type": "string", "nullable": true},
  {"name": "date_std", "type": "date32[day]", "nullable": true},
  {"name": "weightings_pct", "type": "double", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_source", "type": "string", "nullable": true},
  {"name": "_feed", "type": "string", "nullable": true},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment pathfinder/PFDE/ (the fund ticker; Opal-issued fund, not a client firm)",
   "values": [
    "PFDE"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "none: fund data, no client account (the holdings Account column carries the fund ticker, measured PFDE on every row)",
   "last4_derivation": "n/a",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment names the fund administrator source (pathfinder)",
   "values": [
    "pathfinder"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "etf holdings",
  "fund holdings",
  "weights",
  "opal etf",
  "PFDE",
  "pathfinder"
 ],
 "common_queries": [
  "What does PFDE hold today and at what weights?"
 ],
 "existing_gateway_tool": {
  "name": "etfs_get_positioning (reads the portal-v2 positioning gold, DATA_CATALOG.yaml:1392)",
  "verdict": "keep"
 },
 "proposed_tools": [
  {
   "name": "etfs_get_fund_holdings",
   "inputs": {
    "firm": "opal",
    "account_last4": "n/a",
    "platform": "pathfinder",
    "as_of": "YYYY-MM-DD",
    "fund_ticker": "PFDE"
   },
   "returns": "the rows of the newest partition at or before as_of",
   "answers": [
    "What does PFDE hold today?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "channels row at DATA_CATALOG.yaml:395 names the four funds (served positioning, not this silver)",
  "present": false
 },
 "prior_art": "infra/aws/terraform/opal-assets/silver.tf silver_sweep_slots.etf @bc91e712ad",
 "open_items": [
  "G5 (opal-data-etfs) owns the ETF estate; these silver tables are the opal-data-assets landing of the same four funds: reconcile with G5 before cutting a tool"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=pathfinder/",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 91 parts; projected read of Account/date_std (holdings) or ticker/as-of (nav) on the newest part",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

### `opal-data-assets/silver/pathfinder_PFOE_fact_dailynav`

```json
{
 "contract_id": "opal-data-assets/silver/pathfinder_PFOE_fact_dailynav",
 "bucket": "opal-data-assets",
 "s3_prefix": "pathfinder/PFOE/silver/fact_dailynav/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_dailynav",
 "grain": "one row per fund per business date",
 "description": "As PFDE fact_dailynav.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-etf",
  "schedule": "S3 ObjectCreated on pathfinder/filepoint/bronze/ (bucket notification; .csv for pathfinder/filepoint, .html for trueshares) + rule opal-assets-silver-etf-sweep-daily cron(30 23 * * ? *) ENABLED",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "claim": "measured"
 },
 "size": {
  "objects": 91,
  "partitions": 91,
  "rows_all_partitions": 91,
  "rows_newest_partition": 1,
  "schema_variants": 1,
  "claim": "measured"
 },
 "columns": [
  {"name": "Fund Name", "type": "string", "nullable": true},
  {"name": "Fund Ticker", "type": "string", "nullable": true},
  {"name": "CUSIP", "type": "string", "nullable": true},
  {"name": "Net Assets", "type": "double", "nullable": true},
  {"name": "Shares Outstanding", "type": "double", "nullable": true},
  {"name": "NAV", "type": "double", "nullable": true},
  {"name": "NAV Change Dollars", "type": "double", "nullable": true},
  {"name": "NAV Change Percentage", "type": "double", "nullable": true},
  {"name": "Market Price", "type": "double", "nullable": true},
  {"name": "Market Price Change Dollars", "type": "double", "nullable": true},
  {"name": "Market Price Change Percentage", "type": "double", "nullable": true},
  {"name": "Premium/Discount Percentage", "type": "double", "nullable": true},
  {"name": "Rate Date", "type": "string", "nullable": true},
  {"name": "Median 30 Day Spread Percentage", "type": "double", "nullable": true},
  {"name": "rate_date_std", "type": "date32[day]", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_source", "type": "string", "nullable": true},
  {"name": "_feed", "type": "string", "nullable": true},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment pathfinder/PFOE/ (the fund ticker; Opal-issued fund, not a client firm)",
   "values": [
    "PFOE"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "none: fund data, no client account (the holdings Account column carries the fund ticker, measured PFOE on every row)",
   "last4_derivation": "n/a",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment names the fund administrator source (pathfinder)",
   "values": [
    "pathfinder"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "nav",
  "net assets",
  "premium discount",
  "opal etf",
  "PFOE",
  "pathfinder"
 ],
 "common_queries": [
  "What was the NAV and net assets of PFOE on a date?"
 ],
 "existing_gateway_tool": {
  "name": "etfs_get_positioning (reads the portal-v2 positioning gold, DATA_CATALOG.yaml:1392)",
  "verdict": "keep"
 },
 "proposed_tools": [
  {
   "name": "etfs_get_fund_nav",
   "inputs": {
    "firm": "opal",
    "account_last4": "n/a",
    "platform": "pathfinder",
    "as_of": "YYYY-MM-DD",
    "fund_ticker": "PFOE"
   },
   "returns": "the rows of the newest partition at or before as_of",
   "answers": [
    "What was the NAV of PFOE on a date?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "channels row at DATA_CATALOG.yaml:395 names the four funds (served positioning, not this silver)",
  "present": false
 },
 "prior_art": "infra/aws/terraform/opal-assets/silver.tf silver_sweep_slots.etf @bc91e712ad",
 "open_items": [
  "G5 (opal-data-etfs) owns the ETF estate; these silver tables are the opal-data-assets landing of the same four funds: reconcile with G5 before cutting a tool"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=pathfinder/",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 91 parts; projected read of Account/date_std (holdings) or ticker/as-of (nav) on the newest part",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

### `opal-data-assets/silver/pathfinder_PFOE_fact_holdings`

```json
{
 "contract_id": "opal-data-assets/silver/pathfinder_PFOE_fact_holdings",
 "bucket": "opal-data-assets",
 "s3_prefix": "pathfinder/PFOE/silver/fact_holdings/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_holdings",
 "grain": "one row per fund holding per date (25 rows on 2026-10-13)",
 "description": "As PFDE fact_holdings.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-etf",
  "schedule": "S3 ObjectCreated on pathfinder/filepoint/bronze/ (bucket notification; .csv for pathfinder/filepoint, .html for trueshares) + rule opal-assets-silver-etf-sweep-daily cron(30 23 * * ? *) ENABLED",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "claim": "measured"
 },
 "size": {
  "objects": 91,
  "partitions": 91,
  "rows_all_partitions": 2211,
  "rows_newest_partition": 25,
  "schema_variants": 1,
  "claim": "measured"
 },
 "columns": [
  {"name": "Date", "type": "string", "nullable": true},
  {"name": "Account", "type": "string", "nullable": true},
  {"name": "StockTicker", "type": "string", "nullable": true},
  {"name": "CUSIP", "type": "string", "nullable": true},
  {"name": "SecurityName", "type": "string", "nullable": true},
  {"name": "Shares", "type": "double", "nullable": true},
  {"name": "Price", "type": "double", "nullable": true},
  {"name": "MarketValue", "type": "double", "nullable": true},
  {"name": "Weightings", "type": "string", "nullable": true},
  {"name": "NetAssets", "type": "double", "nullable": true},
  {"name": "SharesOutstanding", "type": "double", "nullable": true},
  {"name": "CreationUnits", "type": "double", "nullable": true},
  {"name": "MoneyMarketFlag", "type": "string", "nullable": true},
  {"name": "date_std", "type": "date32[day]", "nullable": true},
  {"name": "weightings_pct", "type": "double", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_source", "type": "string", "nullable": true},
  {"name": "_feed", "type": "string", "nullable": true},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment pathfinder/PFOE/ (the fund ticker; Opal-issued fund, not a client firm)",
   "values": [
    "PFOE"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "none: fund data, no client account (the holdings Account column carries the fund ticker, measured PFOE on every row)",
   "last4_derivation": "n/a",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment names the fund administrator source (pathfinder)",
   "values": [
    "pathfinder"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "etf holdings",
  "fund holdings",
  "opal etf",
  "PFOE",
  "pathfinder"
 ],
 "common_queries": [
  "What does PFOE hold today and at what weights?"
 ],
 "existing_gateway_tool": {
  "name": "etfs_get_positioning (reads the portal-v2 positioning gold, DATA_CATALOG.yaml:1392)",
  "verdict": "keep"
 },
 "proposed_tools": [
  {
   "name": "etfs_get_fund_holdings",
   "inputs": {
    "firm": "opal",
    "account_last4": "n/a",
    "platform": "pathfinder",
    "as_of": "YYYY-MM-DD",
    "fund_ticker": "PFOE"
   },
   "returns": "the rows of the newest partition at or before as_of",
   "answers": [
    "What does PFOE hold today?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "channels row at DATA_CATALOG.yaml:395 names the four funds (served positioning, not this silver)",
  "present": false
 },
 "prior_art": "infra/aws/terraform/opal-assets/silver.tf silver_sweep_slots.etf @bc91e712ad",
 "open_items": [
  "G5 (opal-data-etfs) owns the ETF estate; these silver tables are the opal-data-assets landing of the same four funds: reconcile with G5 before cutting a tool"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=pathfinder/",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 91 parts; projected read of Account/date_std (holdings) or ticker/as-of (nav) on the newest part",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

### `opal-data-assets/silver/trueshares_DIVZ_fact_holdings`

```json
{
 "contract_id": "opal-data-assets/silver/trueshares_DIVZ_fact_holdings",
 "bucket": "opal-data-assets",
 "s3_prefix": "trueshares/DIVZ/silver/fact_holdings/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_holdings",
 "grain": "one row per fund holding per date (30 rows on 2026-09-30)",
 "description": "Holdings CSV of the fund.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-etf",
  "schedule": "S3 ObjectCreated on trueshares/DIVZ/bronze/ (bucket notification; .csv for pathfinder/filepoint, .html for trueshares) + rule opal-assets-silver-etf-sweep-daily cron(30 23 * * ? *) ENABLED",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-09-30",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 9,
  "claim": "measured"
 },
 "size": {
  "objects": 38,
  "partitions": 38,
  "rows_all_partitions": 1104,
  "rows_newest_partition": 30,
  "schema_variants": 1,
  "claim": "measured"
 },
 "columns": [
  {"name": "Date", "type": "string", "nullable": true},
  {"name": "Account", "type": "string", "nullable": true},
  {"name": "Stock Ticker", "type": "string", "nullable": true},
  {"name": "CUSIP", "type": "string", "nullable": true},
  {"name": "Security Name", "type": "string", "nullable": true},
  {"name": "Shares", "type": "double", "nullable": true},
  {"name": "Price", "type": "double", "nullable": true},
  {"name": "Market Value", "type": "double", "nullable": true},
  {"name": "Weightings", "type": "double", "nullable": true},
  {"name": "Net Assets", "type": "double", "nullable": true},
  {"name": "date_std", "type": "date32[day]", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_source", "type": "string", "nullable": true},
  {"name": "_feed", "type": "string", "nullable": true},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment trueshares/DIVZ/ (the fund ticker; Opal-issued fund, not a client firm)",
   "values": [
    "DIVZ"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "none: fund data, no client account (the holdings Account column carries the fund ticker, measured DIVZ on every row)",
   "last4_derivation": "n/a",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment names the fund administrator source (trueshares)",
   "values": [
    "trueshares"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "etf holdings",
  "fund holdings",
  "opal etf",
  "DIVZ",
  "trueshares"
 ],
 "common_queries": [
  "What does DIVZ hold today and at what weights?"
 ],
 "existing_gateway_tool": {
  "name": "etfs_get_positioning (reads the portal-v2 positioning gold, DATA_CATALOG.yaml:1392)",
  "verdict": "keep"
 },
 "proposed_tools": [
  {
   "name": "etfs_get_fund_holdings",
   "inputs": {
    "firm": "opal",
    "account_last4": "n/a",
    "platform": "trueshares",
    "as_of": "YYYY-MM-DD",
    "fund_ticker": "DIVZ"
   },
   "returns": "the rows of the newest partition at or before as_of",
   "answers": [
    "What does DIVZ hold today?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "channels row at DATA_CATALOG.yaml:395 names the four funds (served positioning, not this silver)",
  "present": false
 },
 "prior_art": "infra/aws/terraform/opal-assets/silver.tf silver_sweep_slots.etf @bc91e712ad",
 "open_items": [
  "holdings stopped at 2026-09-30 (9 trading days behind T-1); bronze trueshares/DIVZ/bronze/holdings/ newest object is also 2026-09-30, so the vendor CSV stopped landing upstream of silver",
  "G5 (opal-data-etfs) owns the ETF estate; these silver tables are the opal-data-assets landing of the same four funds: reconcile with G5 before cutting a tool"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=trueshares/",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 38 parts; projected read of Account/date_std (holdings) or ticker/as-of (nav) on the newest part",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

### `opal-data-assets/silver/trueshares_DIVZ_fact_netassets_page`

```json
{
 "contract_id": "opal-data-assets/silver/trueshares_DIVZ_fact_netassets_page",
 "bucket": "opal-data-assets",
 "s3_prefix": "trueshares/DIVZ/silver/fact_netassets_page/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_netassets_page",
 "grain": "one row per fund per scrape date",
 "description": "Scraped fund page: NAV, market price, net assets, shares outstanding, each with its as-of.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-etf",
  "schedule": "S3 ObjectCreated on trueshares/DIVZ/bronze/ (bucket notification; .csv for pathfinder/filepoint, .html for trueshares) + rule opal-assets-silver-etf-sweep-daily cron(30 23 * * ? *) ENABLED",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "claim": "measured"
 },
 "size": {
  "objects": 91,
  "partitions": 91,
  "rows_all_partitions": 91,
  "rows_newest_partition": 1,
  "schema_variants": 1,
  "claim": "measured"
 },
 "columns": [
  {"name": "ticker", "type": "string", "nullable": true},
  {"name": "nav_raw", "type": "string", "nullable": true},
  {"name": "nav", "type": "double", "nullable": true},
  {"name": "nav_as_of_raw", "type": "string", "nullable": true},
  {"name": "nav_as_of", "type": "date32[day]", "nullable": true},
  {"name": "market_price_raw", "type": "string", "nullable": true},
  {"name": "market_price", "type": "double", "nullable": true},
  {"name": "market_price_as_of_raw", "type": "string", "nullable": true},
  {"name": "market_price_as_of", "type": "date32[day]", "nullable": true},
  {"name": "net_assets_raw", "type": "string", "nullable": true},
  {"name": "net_assets", "type": "double", "nullable": true},
  {"name": "net_assets_as_of_raw", "type": "string", "nullable": true},
  {"name": "net_assets_as_of", "type": "date32[day]", "nullable": true},
  {"name": "shares_outstanding_raw", "type": "string", "nullable": true},
  {"name": "shares_outstanding", "type": "double", "nullable": true},
  {"name": "shares_outstanding_as_of_raw", "type": "string", "nullable": true},
  {"name": "shares_outstanding_as_of", "type": "date32[day]", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_source", "type": "string", "nullable": true},
  {"name": "_feed", "type": "string", "nullable": true},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment trueshares/DIVZ/ (the fund ticker; Opal-issued fund, not a client firm)",
   "values": [
    "DIVZ"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "none: fund data, no client account (the holdings Account column carries the fund ticker, measured DIVZ on every row)",
   "last4_derivation": "n/a",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment names the fund administrator source (trueshares)",
   "values": [
    "trueshares"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "nav",
  "net assets",
  "fund page",
  "opal etf",
  "DIVZ",
  "trueshares"
 ],
 "common_queries": [
  "What was the NAV and net assets of DIVZ on a date?"
 ],
 "existing_gateway_tool": {
  "name": "etfs_get_positioning (reads the portal-v2 positioning gold, DATA_CATALOG.yaml:1392)",
  "verdict": "keep"
 },
 "proposed_tools": [
  {
   "name": "etfs_get_fund_nav",
   "inputs": {
    "firm": "opal",
    "account_last4": "n/a",
    "platform": "trueshares",
    "as_of": "YYYY-MM-DD",
    "fund_ticker": "DIVZ"
   },
   "returns": "the rows of the newest partition at or before as_of",
   "answers": [
    "What was the NAV of DIVZ on a date?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "channels row at DATA_CATALOG.yaml:395 names the four funds (served positioning, not this silver)",
  "present": false
 },
 "prior_art": "infra/aws/terraform/opal-assets/silver.tf silver_sweep_slots.etf @bc91e712ad",
 "open_items": [
  "MEASURED PARSE DEFECT on DIVZ date=2026-10-13: ticker reads the literal \"CUSIP\" and nav_as_of / net_assets_as_of read 2026-09-30 in the 2026-10-13 partition; the partition date is the scrape date, not the data date",
  "G5 (opal-data-etfs) owns the ETF estate; these silver tables are the opal-data-assets landing of the same four funds: reconcile with G5 before cutting a tool"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=trueshares/",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 91 parts; projected read of Account/date_std (holdings) or ticker/as-of (nav) on the newest part",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

### `opal-data-assets/silver/trueshares_IDVZ_fact_holdings`

```json
{
 "contract_id": "opal-data-assets/silver/trueshares_IDVZ_fact_holdings",
 "bucket": "opal-data-assets",
 "s3_prefix": "trueshares/IDVZ/silver/fact_holdings/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_holdings",
 "grain": "one row per fund holding per date (41 rows on 2026-09-30)",
 "description": "Holdings CSV of the fund.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-etf",
  "schedule": "S3 ObjectCreated on trueshares/IDVZ/bronze/ (bucket notification; .csv for pathfinder/filepoint, .html for trueshares) + rule opal-assets-silver-etf-sweep-daily cron(30 23 * * ? *) ENABLED",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-09-30",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 9,
  "claim": "measured"
 },
 "size": {
  "objects": 38,
  "partitions": 38,
  "rows_all_partitions": 1615,
  "rows_newest_partition": 41,
  "schema_variants": 1,
  "claim": "measured"
 },
 "columns": [
  {"name": "Date", "type": "string", "nullable": true},
  {"name": "Account", "type": "string", "nullable": true},
  {"name": "Stock Ticker", "type": "string", "nullable": true},
  {"name": "CUSIP", "type": "string", "nullable": true},
  {"name": "Security Name", "type": "string", "nullable": true},
  {"name": "Shares", "type": "double", "nullable": true},
  {"name": "Price", "type": "double", "nullable": true},
  {"name": "Market Value", "type": "double", "nullable": true},
  {"name": "Weightings", "type": "double", "nullable": true},
  {"name": "Net Assets", "type": "double", "nullable": true},
  {"name": "date_std", "type": "date32[day]", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_source", "type": "string", "nullable": true},
  {"name": "_feed", "type": "string", "nullable": true},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment trueshares/IDVZ/ (the fund ticker; Opal-issued fund, not a client firm)",
   "values": [
    "IDVZ"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "none: fund data, no client account (the holdings Account column carries the fund ticker, measured IDVZ on every row)",
   "last4_derivation": "n/a",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment names the fund administrator source (trueshares)",
   "values": [
    "trueshares"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "etf holdings",
  "fund holdings",
  "opal etf",
  "IDVZ",
  "trueshares"
 ],
 "common_queries": [
  "What does IDVZ hold today and at what weights?"
 ],
 "existing_gateway_tool": {
  "name": "etfs_get_positioning (reads the portal-v2 positioning gold, DATA_CATALOG.yaml:1392)",
  "verdict": "keep"
 },
 "proposed_tools": [
  {
   "name": "etfs_get_fund_holdings",
   "inputs": {
    "firm": "opal",
    "account_last4": "n/a",
    "platform": "trueshares",
    "as_of": "YYYY-MM-DD",
    "fund_ticker": "IDVZ"
   },
   "returns": "the rows of the newest partition at or before as_of",
   "answers": [
    "What does IDVZ hold today?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "channels row at DATA_CATALOG.yaml:395 names the four funds (served positioning, not this silver)",
  "present": false
 },
 "prior_art": "infra/aws/terraform/opal-assets/silver.tf silver_sweep_slots.etf @bc91e712ad",
 "open_items": [
  "holdings stopped at 2026-09-30 (9 trading days behind T-1); bronze trueshares/IDVZ/bronze/holdings/ newest object is also 2026-09-30, so the vendor CSV stopped landing upstream of silver",
  "G5 (opal-data-etfs) owns the ETF estate; these silver tables are the opal-data-assets landing of the same four funds: reconcile with G5 before cutting a tool"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=trueshares/",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 38 parts; projected read of Account/date_std (holdings) or ticker/as-of (nav) on the newest part",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

### `opal-data-assets/silver/trueshares_IDVZ_fact_netassets_page`

```json
{
 "contract_id": "opal-data-assets/silver/trueshares_IDVZ_fact_netassets_page",
 "bucket": "opal-data-assets",
 "s3_prefix": "trueshares/IDVZ/silver/fact_netassets_page/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_netassets_page",
 "grain": "one row per fund per scrape date",
 "description": "Scraped fund page.",
 "partition": {
  "keys": [
   "date"
  ],
  "form": "date=YYYY-MM-DD/data.parquet",
  "claim": "measured"
 },
 "producer": {
  "name": "Lambda opal-assets-silver-etf",
  "schedule": "S3 ObjectCreated on trueshares/IDVZ/bronze/ (bucket notification; .csv for pathfinder/filepoint, .html for trueshares) + rule opal-assets-silver-etf-sweep-daily cron(30 23 * * ? *) ENABLED",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "claim": "measured"
 },
 "size": {
  "objects": 91,
  "partitions": 91,
  "rows_all_partitions": 91,
  "rows_newest_partition": 1,
  "schema_variants": 1,
  "claim": "measured"
 },
 "columns": [
  {"name": "ticker", "type": "string", "nullable": true},
  {"name": "nav_raw", "type": "string", "nullable": true},
  {"name": "nav", "type": "double", "nullable": true},
  {"name": "nav_as_of_raw", "type": "string", "nullable": true},
  {"name": "nav_as_of", "type": "date32[day]", "nullable": true},
  {"name": "market_price_raw", "type": "string", "nullable": true},
  {"name": "market_price", "type": "double", "nullable": true},
  {"name": "market_price_as_of_raw", "type": "string", "nullable": true},
  {"name": "market_price_as_of", "type": "date32[day]", "nullable": true},
  {"name": "net_assets_raw", "type": "string", "nullable": true},
  {"name": "net_assets", "type": "double", "nullable": true},
  {"name": "net_assets_as_of_raw", "type": "string", "nullable": true},
  {"name": "net_assets_as_of", "type": "date32[day]", "nullable": true},
  {"name": "shares_outstanding_raw", "type": "string", "nullable": true},
  {"name": "shares_outstanding", "type": "double", "nullable": true},
  {"name": "shares_outstanding_as_of_raw", "type": "string", "nullable": true},
  {"name": "shares_outstanding_as_of", "type": "date32[day]", "nullable": true},
  {"name": "_source_file", "type": "string", "nullable": true, "description": "provenance: the bronze object the row came from"},
  {"name": "_source_as_of", "type": "string", "nullable": true, "description": "provenance: source as-of"},
  {"name": "_source", "type": "string", "nullable": true},
  {"name": "_feed", "type": "string", "nullable": true},
  {"name": "_schema_version", "type": "string", "nullable": true, "description": "provenance: pinned schema version"}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment trueshares/IDVZ/ (the fund ticker; Opal-issued fund, not a client firm)",
   "values": [
    "IDVZ"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "none: fund data, no client account (the holdings Account column carries the fund ticker, measured IDVZ on every row)",
   "last4_derivation": "n/a",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "none; key segment names the fund administrator source (trueshares)",
   "values": [
    "trueshares"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "nav",
  "net assets",
  "fund page",
  "opal etf",
  "IDVZ",
  "trueshares"
 ],
 "common_queries": [
  "What was the NAV and net assets of IDVZ on a date?"
 ],
 "existing_gateway_tool": {
  "name": "etfs_get_positioning (reads the portal-v2 positioning gold, DATA_CATALOG.yaml:1392)",
  "verdict": "keep"
 },
 "proposed_tools": [
  {
   "name": "etfs_get_fund_nav",
   "inputs": {
    "firm": "opal",
    "account_last4": "n/a",
    "platform": "trueshares",
    "as_of": "YYYY-MM-DD",
    "fund_ticker": "IDVZ"
   },
   "returns": "the rows of the newest partition at or before as_of",
   "answers": [
    "What was the NAV of IDVZ on a date?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "channels row at DATA_CATALOG.yaml:395 names the four funds (served positioning, not this silver)",
  "present": false
 },
 "prior_art": "infra/aws/terraform/opal-assets/silver.tf silver_sweep_slots.etf @bc91e712ad",
 "open_items": [
  "MEASURED PARSE DEFECT on DIVZ date=2026-10-13: ticker reads the literal \"CUSIP\" and nav_as_of / net_assets_as_of read 2026-09-30 in the 2026-10-13 partition; the partition date is the scrape date, not the data date",
  "G5 (opal-data-etfs) owns the ETF estate; these silver tables are the opal-data-assets landing of the same four funds: reconcile with G5 before cutting a tool"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=trueshares/",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of all 91 parts; projected read of Account/date_std (holdings) or ticker/as-of (nav) on the newest part",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

### `opal-data-assets/silver/yahoo_global_price_history`

```json
{
 "contract_id": "opal-data-assets/silver/yahoo_global_price_history",
 "bucket": "opal-data-assets",
 "s3_prefix": "yahoo/global/silver/price_history/",
 "layer": "silver",
 "format": "parquet",
 "table": "price_history",
 "grain": "per cusip=<CUSIP> partition: prices.parquet one row per trading day; dividends.parquet one row per dividend; splits.parquet one row per split; lock.json the pull lock; plus index/index.parquet one row per cusip (483)",
 "description": "Per-CUSIP Yahoo price store of MDPF_DEMQUE: served close, as-traded close, cash dividends, total-return series, split ratios, with claim/method/as_of in the index.",
 "partition": {
  "keys": [
   "cusip"
  ],
  "form": "cusip=<CUSIP>/{prices,dividends,splits}.parquet + lock.json; index/index.{parquet,csv}",
  "claim": "measured"
 },
 "producer": {
  "name": "data/mdpf/scripts/demque/price_store.py write()/write_index() driven by demand_queue.py draw (MDPF_DEMQUE)",
  "schedule": "daily on a box, ~02:30-03:50Z (measured from demand_ledger and index LastModified); no Lambda or EventBridge schedule found in 237 functions / 35 schedules scanned",
  "claim": "inferred"
 },
 "freshness": {
  "latest_partition": "index as_of max 2026-10-13",
  "basis": "trading-day-frontier",
  "t1": "2026-10-13",
  "trading_days_behind": 0,
  "per_cusip_newest_price_date": {
   "2026-06-22": 3,
   "2026-06-23": 14,
   "2026-10-09": 315,
   "2026-10-13": 151
  },
  "note": "of 483 cusips: 151 reach 2026-10-13 (0 behind), 315 stop at 2026-10-09 (2 behind), 17 stop at 2026-06-22/23 (the Commonwealth cut-over set)",
  "claim": "measured"
 },
 "size": {
  "objects": 1934,
  "parquet_parts": 1450,
  "cusips": 483,
  "price_rows": 478768,
  "rows_all_parquet": 535464,
  "zero_row_parts": 291,
  "schema_variants": 8,
  "claim": "measured"
 },
 "columns": [
  {"name": "date", "type": "timestamp[ms]|timestamp[ns]", "nullable": true},
  {"name": "amount", "type": "double", "nullable": true},
  {"name": "close_served", "type": "double", "nullable": true},
  {"name": "as_traded_close", "type": "double", "nullable": true},
  {"name": "cash", "type": "double", "nullable": true},
  {"name": "total_return", "type": "double", "nullable": true},
  {"name": "tr_source", "type": "large_string", "nullable": true},
  {"name": "flags", "type": "list<element: null>|list<element: string>", "nullable": true},
  {"name": "ratio", "type": "double", "nullable": true},
  {"name": "cusip", "type": "large_string", "nullable": true, "description": "security CUSIP", "example": "<9-char cusip>"},
  {"name": "yahoo_symbol", "type": "large_string", "nullable": true},
  {"name": "valid_from", "type": "large_string", "nullable": true},
  {"name": "valid_to", "type": "large_string", "nullable": true},
  {"name": "rows", "type": "int64", "nullable": true},
  {"name": "claim", "type": "large_string", "nullable": true},
  {"name": "method", "type": "large_string", "nullable": true},
  {"name": "as_of", "type": "large_string", "nullable": true},
  {"name": "run_id", "type": "large_string", "nullable": true}
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment yahoo/global/ (reference data, no firm)",
   "values": [
    "global"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "none: reference prices",
   "last4_derivation": "n/a",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "none (vendor yahoo)",
   "values": [
    "yahoo"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "price history",
  "total return",
  "dividends",
  "splits",
  "cusip",
  "yahoo"
 ],
 "common_queries": [
  "What was the close and total return of CUSIP X between two dates?",
  "What splits and dividends did CUSIP X have?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "prices_get_history",
   "inputs": {
    "firm": "n/a (global reference)",
    "account_last4": "n/a",
    "platform": "yahoo",
    "as_of": "start..end",
    "cusip_or_symbol": "<cusip|symbol>"
   },
   "returns": "daily close, as-traded close, total return, dividends and splits for one cusip, with the index row claim/method/as_of",
   "answers": [
    "What was the close and total return of CUSIP X between two dates?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "data/mdpf/scripts/demque/price_store.py (contract PRICE_STORE_CONTRACT.md named in its docstring) @bc91e712ad",
 "open_items": [
  "8 schema variants: date is timestamp[ms] in some parts and timestamp[ns] in others, flags list<null> vs list<string>; coerce before min/max",
  "291 of 1450 parquet parts hold 0 rows (empty dividends/splits files)"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 Prefix=yahoo/ (2 pages, 1,940 keys)",
   "at": "2026-10-14T12:53Z..12:57Z"
  },
  {
   "read": "pyarrow read_metadata of 1,450 parquet parts; projected date read of 483 prices.parquet; full read of index.parquet",
   "at": "2026-10-14T13:20Z..13:36Z"
  }
 ]
}
```

## 5. What could not be read, and why

- **Vendor meaning of UPN/UPT and of the FAM/SLM positional columns:** the data dictionary marks UPN/UPT "position (pending?)", and FAM/SLM naming is blocked on the vendor layout. These are inferred, not measured, and no tool is proposed.
- **Row-level uniqueness over history:** the grain checks read ONE date (08335338, 2026-10-13) per table. The 14-row `dim_position` and 24-row `dim_asset` repeats are measured on that date only.
- **08242234 and 08403355 grain checks** were not run (one master sampled). The schemas are identical across masters (measured), but row semantics are inferred to match.
- **Producer schedules of the non-Lambda writers** are inferred from LastModified times, not from a schedule object: the Yahoo price store (a box task) and the Tax SMA silver (`mdpf-gold-lambda` Tax prelude).
- **Commonwealth bronze** (`imaging` 3.17 GB zip, `portfolio_accounting` zip) was not opened. It is bronze, and only silver is contracted.
- **The PDFs under `commonwealth/cottonwood/silver/documents/`** (11,120 objects) were counted, not opened (client documents).
- **Gateway behaviour** (what `schwab_query` actually returns today) was not exercised. A tool call would be an act on a served surface outside this part's read-only list. Verdicts rest on the contract and the catalog.
- **Sibling prefixes** `blackdiamond/`, `orion/`, `eclipse/`, `smartx/` were counted only (2.1).

### Open items (for 4.0.0_SA_CRO~Z to route; this part writes no surprise row because its write surface is this file)

- **O-1** The `49-schwab-conv` skill points at a dead channel. `opal-data-bd/schwab/silver/` has been frozen since 2026-07-23 (57 trading days behind), and the live monolith silver differs in name and bucket. Anyone following the skill reads 57-day-old data. Owner: the skill's AE lane.
- **O-2** 08403355 is served by the gateway IAM but is absent from `NFRA_OPLGTW_CONTRACT.json` masters and data_prefixes, from `infra/logic/registry/scopes.json`, and from the `silver_datasets` wording. This is a contract/registry gap. Owner: NFRA_OPLGTW (CTO) and the LGIC registry.
- **O-3** The Schwab platform labels conflict: the contract says SmartX / BlackDiamond, the CTO ruling says Tax SMA, and the data reads MAM / SmartX. The `platform` tool input needs one ruled enum.
- **O-4** Last-4 collides on 54% of 49financial Schwab accounts and on 48% of Commonwealth accounts. Every last-4 tool needs a resolve step (`schwab_resolve_account`). A last-4 must never be treated as a key.
- **O-5** `fact_fam` (08335338) stopped at 2026-08-10, with bronze fam stopping too: 45 trading days behind.
- **O-6** `ADVI_BILLING_SMARTX_FEE_STATEMENT_CONTRACT.json` names a silver address in this bucket (`advi/49financial/silver/smartx_fee_statement/`) that holds 0 objects (no `advi/` prefix).
- **O-7** TrueShares: `fact_holdings` for DIVZ/IDVZ stopped at 2026-09-30 (9 behind; bronze holdings stopped too). `fact_netassets_page` on 2026-10-13 reads ticker "CUSIP" and as-of 2026-09-30: a parse defect. For G5 to reconcile.
- **O-8** `fact_rps_s2` and `dim_balance` have equal object sizes at 1,683 of 1,683 partition pairs (249.5 MB on 08242234 and 243.8 MB on 08335338), duplicate storage by design ("identity projection", "confirm-or-cut").
- **O-9** The Tax SMA workbook silver is multi-firm in one table (RIA cell; 4 of 21 rows with an empty RIA). Its tool must take the firm and filter it, or a cross-firm read follows.
- **O-10** `schwab/08335338/gold/canonical/` has been frozen since 2026-08-10 (44 behind). Who reads it is unmeasured here.


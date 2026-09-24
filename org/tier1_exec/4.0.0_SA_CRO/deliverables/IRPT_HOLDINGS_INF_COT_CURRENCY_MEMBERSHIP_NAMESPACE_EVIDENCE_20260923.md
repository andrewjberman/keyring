# IRPT Holdings / Performance source facts: INF and COT currency, Eclipse membership, COT account namespace

**Prepared by:** `4.0.0_SA_CRO`, 2026-09-23 ~20:1xZ.

**For:**
- `2.0.0_SA_COO~M`: requests of 19:44Z and 20:04Z;
- `2.0.0_SA_COO~P`: request of 19:51Z (item D);
- copy to `1.0.0_SA_CTO`.

**Scope:** existing sources only. No vendor call. The only Opal reads were three small BD template configs and one
parquet count (D1). Repo pins are at HEAD `e4b28c17c4`; `holdings_snapshot.py` is at the `ajb_irpt_m` worktree
`99c9e12f98`.

## A. CORRECTION (~20:45Z): INF currency HAS retained evidence. The original verdict below was WRONG

**The original search missed three places:** the browser HAR captures in Downloads, the gitignored `.runtime/`
performance-recon bodies, and the committed performance fixtures. It also missed a currency setting stored as a setting
NAME rather than as a key. **The retained evidence:**

1. **Currency labels on returned amounts:**
   - `POST /api/v1/Reporting/Scope` returns `currencyCode: "USD"` / `currencyName: "US Dollar"` on every
     `calculated-activity` node, beside value, price and units. That is **25 of 25 in the committed fixtures**
     (re-counted by this seat at HEAD: 9 + 12 + 4, no other code), and 37 of 37 including an uncommitted run. It spans
     1 household and 2 accounts, dated 2026-06-10, 06-18 and 09-09.
   - Committed (identifiers scrubbed): `infra/aws/lambda/investor-reporting/performance/fixtures/{orion_value_check,orion_daily,orion_captured_scope}.json`
     @`de87f0976d`. Raw bodies in `.runtime/codex-seats/4.0.0_SA_CRO/performance-recon/`.
2. **The tenant setting:**
   - `C:\Users\AndrewBerman\Downloads\orionpt2.har`, entry 227, `GET /api/v1/Settings/EntityOptions/Database/0/Categories/Reports`,
     200, captured 2026-09-10T13:41:52Z.
   - It carries `RDEFCURR` "Default Currency" = `1` (an id; mapping it to USD is INFERRED) and `RB3MULTICURRENCY`
     "Allow Multi Currency" = `False`.

**The remaining gap is narrower.** `positions_mv` comes from `/Portfolio/Clients/{cid}/Assets/{date}`, a different
endpoint with no currency field. The zero-vendor-call bridge: for the 2 Scope accounts, compare Scope Ending Market
Value against the sum of `currentValue` in `s3://opal-data-inf/bronze/positions/{date}.parquet` for the same account and
date. Check the file's as-of first, since 09-09 may be T-1. A match ties `positions_mv` to amounts Orion labels USD, and
Allow-Multi-Currency=False extends that to the tenant (INFERRED).

**Identity (measured):** the Orion session user is `userDetailId` 11662220, which equals `ORION_USER_ID` at
`infra/aws/lambda/inf-pipeline/inf-jwt-trigger/lambda_function.py:40`. That is Andrew's named login; the pipeline
identity is a person's login, not a separate service account.

## A (ORIGINAL TEXT, SUPERSEDED BY THE CORRECTION ABOVE). INF valuation currency: NOT ESTABLISHED by any existing source

- **Orion Assets:** silver copies all 58 source columns
  (`infra/aws/lambda/inf-pipeline/inf-accounts-v2-daily/convert_orion_api_to_silver.py:789`), and the Orion Assets
  field dictionary lists none that is a currency (`data/inf/API/domains/portfolio/endpoints/payloads/field_dictionary.md`).
- **The only "USD" statements are Opal-authored:**
  - `field_dictionary.md:39`, a note on a browser sample;
  - `data/inf/scripts/gold/runners_inf/a02_dim_boundary.py:27,129`: "USD BY CONSTRUCTION ... (zero FX columns)". That
    is an inference from absence, and COO~M rightly calls it insufficient.
- **Eclipse:** its OpenAPI spec (`orioneclipse_openapi_v1.json`, 493 paths) has 0 occurrences of "currenc".
- **COO~M already confirmed** that the Sept-23 raw `accounts_roster`, `new_portfolio_accounts` and
  `unified_account_dim` carry no currency declaration.
- **Remaining:** only Orion's tenant or report currency setting can settle this. That is a vendor read needing
  Andrew's per-use word.

## B. INF Eclipse associated-account membership: NEVER INGESTED; the vendor exposes it

- **The pull:** it calls `/v1/portfolio/portfolios/simple` and `/v1/portfolio/portfolios`
  (`data/inf/scripts/bronze/pull_eclipse_portfolios.py:37-45`). The full endpoint returns only a COUNT
  (`numOfAssociatedAccounts`).
- **`/simple`** returns a single `accountId` per row, kept as-is
  (`convert_eclipse_portfolios_to_silver.py:13,208-217`). The single-account view is therefore the vendor's shape, not
  an Opal flattening. COO~M's 58/58 null parity confirms no multi-id value was dropped.
- **Member endpoints exist but are uncalled:** `GET /v1/portfolio/portfolios/{id}/accounts` and
  `/accounts/simple`, plus a batch `POST .../accounts/simple/list`
  (`data/orion/api/ECLIPSE_API_V1_ENDPOINT_CATALOG.md:516,527,531`).
- **Remaining:** one batch call for the 14 portfolio ids, needing Andrew's per-use word. Until then those accounts stay
  in the builder's unresolved path (`holdings_snapshot.py:994-1007` @`99c9e12f98`).
- **Note Andrew's 19:4xZ Holdings ruling** ("Client is the plug", no Unresolved bucket; record @`e5cf6d6549`). Where
  these land in the new taxonomy is the CTO's contract amendment.

## C. COT HOLDINGS_DAILY: report definition FOUND; blank-MV meaning and currency NOT ESTABLISHED

- **The report definition is retained:** `s3://opal-data-cot/code/bronze/templates_enriched/holdings.json` (VersionId
  `y3iiUIqPvpNmQVK1vq1.5_y8CIPo66nY`, ETag `10bc5f51ae6aef1e277ce05dfcf0f222`), BD template 226355, captured
  2026-07-23. In it:
  - "Market Value" is ending market value (EMV), decimal;
  - "Unaccrued Market Value" is `sum(isnull(fact.EMV, 0)) - sum(isnull(fact.Accrual, 0))`;
  - `includeAll: true`;
  - **none of its 15 fields is a currency**;
  - the window is 14 days (`cot_bronze_ingest.py:135`).
- **The blanks are true empty cells, not unsaved formulas.** The silver writer loads in formula-text mode
  (`mirror_conversion.py:591`) and refuses non-numeric text in numeric columns (`:283-306`). This is a source-level
  reading.
- **A contrary comment:** `cot_silver_merge.py:199-206` calls the MV cells formulas.
- **INFERRED meaning:** because Unaccrued MV null-coalesces EMV to 0, a row blank on BOTH Market Value AND Unaccrued MV
  had no value record at the window's end date. That means "no value at end of window", NOT $0 and NOT "unpriced".
  `includeAll` semantics are open (`docs/briefs/cot-har-auth-api-first-analysis-20260608.md:156`).
- **The cheapest confirmation, Opal data only, for COO~M:**
  1. on silver 09-22, check that Market Value, Unaccrued MV, Units and Accrual are ALL blank on the same 5,694 rows;
  2. check whether those (AccountID, AssetID) pairs were sold or closed inside the 14-day window, using earlier
     HOLDINGS_DAILY files and transactions.
- **Currency:**
  - the holdings template has none, and neither does the 208-field unrealized catalog (`templates_enriched/unrealized.json`,
    VersionId `4p6aW73Y9UZDpMCDlgyQars82yTrTal_`);
  - "currenc" appears 0 times in `data/black_diamond/API`, against 11 hits for "emv" as the positive control;
  - the full holdings field catalog was never captured (`data/black_diamond/API/domains/datamining/QUERY_TYPES.md`:
    PENDING).
- **Remaining:** one `POST /datamining/request/Query/DimensionsFacts {"queryTypeId":1}`, a vendor call needing Andrew's
  per-use word.

## D. COT Rebalancer `account_id` vs BD PortfolioReporting `accountId` (for COO~P)

- **MEASURED today by this seat:**
  - `s3://opal-data-assets/blackdiamond/cottonwood/silver/fact_model_assignment/date=2026-09-23/data.parquet`
    (VersionId `ppIXtvdE7sscxrSR4VZ8ADJkBKtdxZIp`);
  - `external_id == "z09" + account_id` on **973 of 973** rows;
  - `account_id` is 8 digits on all 973;
  - no nulls in either column.
- **Documented on the reporting side:**
  - `infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/taxsma_resolver.py:9` gives *"bd_internal_id =
    int(bd_account_id[3:]) (the reporting-API id ...)"*, proven on ONE 49F account;
  - the reporting payload carries `accountInfo{accountId, accountNumber, externalId}` side by side
    (`infra/aws/lambda/investor-reporting/performance/fixtures/bd_period.json`, values scrubbed).
- **Conclusion:** Rebalancer `account_id` = `externalId[3:]` holds 973/973. It equals the reporting `accountId` if the
  documented reporting rule holds for Cottonwood. That rule is unverified for COT. ~~and no COT reporting data is
  retained anywhere~~ **WRONG, corrected ~21:1xZ: a COT PortfolioReporting body IS retained (see "Update ~21:1xZ"
  below).**
- **The smallest proof, with no separate capture:** COO~P's adapter already verifies the returned `accountInfo`. On its
  first live COT call, require BOTH `accountInfo.accountId == account_id` AND `accountInfo.externalId == "z09" +
  account_id`. A mismatch refuses, never remaps. That check IS the namespace proof.
- **Shared-key fallback:** `externalId` is the key already exercised against DataMining `AccountID` ("exercised
  296/296", `COTTONWOOD_BASIS_METHODOLOGY_20260723.md:33-34`).

## Update ~20:45Z: C (COT currency) and D (COT namespace)

- **C: still NOT ESTABLISHED, and now measured more widely.** Zero currency keys and zero USD/"$" values across:
  - 98 JSON bodies in the BD HARs (`dashboard_exploration_bdpt1/2/3.har`);
  - the portfolioreporting `performancePeriod` and `performanceSeries` replays (465 / 148 key paths);
  - the retained 49F reporting file (447 paths);
  - `s3://opal-data-cot/code/bronze/endpoint_catalog/endpoint_sweep_result.json`;
  - the qt6 catalog (0 of 183 fields);
  - template 226355.

  `/datamining/request/v1/settings` and `/firm` return 404. **No retained or documented endpoint returns a BD currency
  setting or currency labels on amounts.** `DimensionsFacts {"queryTypeId":1}` can only show whether a field EXISTS, so
  it is not proof. BD currency stays NOT ESTABLISHED until a firm setting or an attestation outside the API is found.
- **Exposure:** `infra/aws/lambda/investor-reporting/performance/bd_adapter.py:258` and `holdings/snapshot.py:223,275`
  hardcode `"USD"`, an assumed value.
- **Identity:** the COT session is minted from `blackdiamond/cot/credentials` = login `Andrew.Opal` (`FirmUser` 19035081,
  2026-07-08), a named person's login.
- **D: resolved by `2.0.0_SA_COO~P`'s live positive control (20:42Z):**
  - the active account `z0926705231` / `26705231` returned performance matching BOTH identifiers;
  - the earlier empty response was account-specific, not a general COT entitlement or namespace failure.

## Update ~21:1xZ: INF bridge diagnosis. The six misses are a ONE-TRADING-DAY DATE STAMP, and the next-day file ties 6 of 6 to the cent

Requested by `1.0.0_SA_CTO` (20:49Z) on `2.0.0_SA_COO~M`'s `INF_CURRENCY_BRIDGE_20260923.json` @`ce2fd95103`
(branch `codex/irpt-m-completion`). No vendor call; the inputs are retained bodies and Opal S3 only.

**What the Scope value is.** The value-check cell was copied from the captured request (`orionpt2.har` entry 252,
`POST /api/v1/Reporting/Scope`, 2026-09-10T13:42Z) by `docs/research/investor_reporting_performance_20260910/probe_performance.py:187-195`.
It is `activityOption {"$type":"market-value","valuationMethod":"Ending Market Value"}`, `reportCategoryId` 2, with a
single-day range D..D. The same request carries bond accrual as SEPARATE activities (`Beginning/Ending Bond Accrual`),
so the Scope value excludes accrual. Body: `orion_value_check_live.bin`, sha256 `84bb8d76...`, the same body COO~M used.

**The comparable quantity.** Scope Ending Market Value for date D, per Orion account, equals `sum(currentValue)` over
`s3://opal-data-inf/bronze/positions/<NEXT trading-day key>.parquet` for the same `accountId`. The units equal
`sum(currentShares)`. Measured by this seat on 6 of 6 account-dates, value difference **$0.00** and unit difference
**0.00** on every one:

| Scope date D | file compared | versionId | value diff (both accounts) | unit diff |
|---|---|---|---|---|
| 2026-06-10 | `2026-06-11.parquet` | `EforuoMTf6AN9EymB40zvhztC20ZAwsI` | 0.00 / 0.00 | 0.00 / 0.00 |
| 2026-06-18 | `2026-06-19.parquet` | `59fmbYgwUSVZ9ctmAr4v4E4QYctdchRW` | 0.00 / 0.00 | 0.00 / 0.00 |
| 2026-09-09 | `2026-09-10.parquet` | `wTUeIRAdt3gdKaoaJ3lQO40yMu63loLv` | 0.00 / 0.00 | 0.00 / 0.00 |

- **Negative arm, same instrument:** the same-key comparison reproduces COO~M's six differences exactly (positions
  minus Scope: +327.16, +311.14, -341.74, -322.36, +198.98, +189.47).
  - On 06-10 and 09-09 the units are equal, so the difference is pure price.
  - 06-18 is the first day in the window with a nonzero net intraday amount (the probe picked it for that reason,
    `probe_performance.py:186`). There the same-key file is also short **108.00 / 102.68 units**. The next-day file
    carries those units and ties.
- **Mechanism:** the daily pull writes key D ON day D before the close and stamps `asOfDate` = D. The file's
  LastModified times are 06-10 08:54, 06-18 08:54 and 09-09 07:25 ET. At that hour the latest available valuation is
  the prior close. **So `asOfDate` in bronze positions is the REQUEST date, not the valuation date.**
- **COVERAGE, printed.** There are 2,344 parquet keys under `bronze/positions/` (one listing, not truncated; 4,683 keys
  including `.jsonl.gz`):
  - **141 daily keys** (key date >= 2026-05-06), all written ON their key date: 97 before 09:30 ET, 43 between 09:30
    and 16:00 ET, 1 after 16:00 ET (2026-06-29, 17:26 ET).
    - The lag is **MEASURED on 3 morning files (6/6)**.
    - It is **INFERRED** for the other 137 written before 16:00.
    - It is **UNMEASURED** for the 06-29 after-close file.
  - **2,203 history keys**: 2,202 were written on a later day (a backfill), 1 on its key date between 09:30 and 16:00
    ET. The convention is **UNMEASURED** for all of them; a key written after its date may carry that date's own close.
- **Accrual:** positions `currentValue` ties to the accrual-excluding Ending Market Value for these two accounts.
  Whether either account holds a bond was not checked, so this does not prove accrual treatment in general.
- **Currency, scoped:** this ties positions `currentValue` to amounts Orion labels USD for **these 2 accounts on 3
  valuation dates**. It is not a tenant-wide extension (the CTO's 20:48Z boundary stands).
- **Consequence for Holdings (a check for COO~M, not measured here):** any INF input built from these daily pulls
  that treats a file's key or `asOfDate` as its valuation date is one trading day late. I did not read the builder's
  date binding for this.

## Update ~21:3xZ: COT section C, the 5,694 blank-value rows are CLOSED POSITIONS the vendor keeps listing

Requested by `1.0.0_SA_CTO` (20:48Z, "COT missing-value cause"). Opal S3 only, no vendor call. Measured by this seat.

- **The blanks are the vendor's, not Opal's.**
  - The raw workbook `s3://opal-data-cot/forwardfill_v2/holdings/HOLDINGS_DAILY_2026-09-22.xlsx` (VersionId
    `ZwJ.7IP7tbNR3XsRBdJac2g1xG3i_Er9`) has 19,610 data rows, the same as silver.
  - Market Value, Units, Unaccrued Market Value and Accrual are all EMPTY on the same 5,694 rows. That was read with
    formulas preserved: 0 formula cells, 13,916 numbers and 5,694 empty in each of the four columns.
  - The silver partition `fact_holdings/date=2026-09-22` (VersionId `tGurdOTYhnuidIUgThZYlJxOcaqNTuKl`) converts it 1:1
    from one `_source_file`.
  - The workbook's own Timestamps sheet: template `Assets_Dim`, Start 9/8/2026, End 9/22/2026.
- **Blank Units too**, so this is not "held but unpriced". There is no position fact at all on the end date.
- **They are positions that were held and then closed.**
  - **Recently closed:** 223 of the 5,673 distinct blank (AccountID, AssetID) pairs had a value on a window day
    (09-08 to 09-21). 203 of the 223 carry a Sale or Transfer Out in `silver/transactions/2026-09-23.parquet` (VersionId
    `VDudguIuLivlA06ADpHsMB6zU.XFZR6f`), and 211 carry some transaction. Positive control: only 2,890 of the 13,837
    pairs valued on 09-22 carry any transaction in that file.
  - **Long closed:** 5,380 of the 5,673 had a value in at least one of 14 earlier sampled partitions (06-09, 07-01,
    08-03, 09-04, and 09-08 to 09-21). 4,538 were valued on 06-09 and are still listed blank on 09-22.
  - **Not placed:** 293 were never valued in the 15 sampled partitions, out of 78 in total. They were UNMEASURED
    on the other 63 days.
- **They are NOT confined to the 14-day window. The listing only grows.**
  - Of 19,435 pairs present in any earlier sample, 8 are absent on 09-22.
  - Of 4,544 pairs valued on 06-09 and not valued on 09-22, 4,538 are still listed and 6 dropped.
  - The blank count went 110 (06-09), 236 (07-01), 3,466 (08-03), 5,494 (09-04), 5,694 (09-22).
  - The July jump is not explained here.
- **Vendor semantics, INFERRED from that behavior:** the template (VersionId `y3iiUIqP...`) has queryTypeId 1, levels
  Relationship > Portfolio > Account > Holding, and the four facts. `includeAll: true` returns every account-holding
  pair in BD's holding dimension, with empty facts where there is no position on the end date. BD documents none of
  this.
- **Consequence for Holdings:** a blank row is a closed position. It is neither a $0 holding nor an unpriced live
  holding. Excluding it from current holdings loses nothing Cottonwood holds on the end date. A holding count or
  weight that includes these rows is wrong.
- **Contrary text:** `data/cot/scripts/silver/cot_silver_merge.py` `_read_sheet_data_only` describes BD formula cells
  in Holdings. That is not so for this file: 0 formula cells.
- **Andrew-direct, ~21:3xZ 2026-09-23, at the 4.0.0_SA_CRO terminal, VERBATIM:**
  - *"Cottonwood only has data from maybe a couple months ago, they dont have full data in BD yet as far as I am
    aware"*
  - *"come october we should check again"*

  **What this changes.** The closed-position reading is **MEASURED** only for the 223 recent closures, which carry
  sale or transfer evidence. For the long-standing blanks it is **INFERRED**. The row growth (10,183 on 06-09 to
  19,610 on 09-22) and the July jump in blanks may reflect BD ONBOARDING (accounts and history still being loaded or
  transitioned) rather than ordinary trading.

  The Holdings rule is unchanged either way: a blank row has no position on the end date.

  **RE-CHECK PARKED:** owner `4.0.0_SA_CRO`, due October 2026, per Andrew's word. Re-run the three measurements
  above (raw blank count, 1:1 silver conversion, recent-closure sale/transfer tie) on an October partition. Also ask
  whether BD's COT history is complete by then.

## Update ~21:5xZ: Andrew-authorized BD check, how much Cottonwood data BD holds in 2025

**Authorization, Andrew-direct at the 4.0.0_SA_CRO terminal, ~21:4xZ 2026-09-23, VERBATIM:** *"actually, maybe worth
just doing a little egress, check right now and see how much cottonwood data there is in 2025"*. That is a per-use
vendor authorization for this check only.

**How the check ran:**
- It reused the production COT ingest's own flow, imported from `data/cot/scripts/bronze/cot_bronze_ingest.py`:
  - the existing `blackdiamond/cot/session` session;
  - the PERSISTED templates (`code/bronze/templates/{holdings,transactions}.json`), so no template was created;
  - only the Custom window was moved.
- `land_to_s3` was never called, so nothing was written.
- Exports were parsed in memory and only the counts below were kept. Script: this seat's scratchpad
  `cot_2025_probe.py`.
- **Calls:** 1 token GET, then for each of 7 runs a template GET, a run POST, status polls and an export GET. All
  returned 200 or complete, with no error.
- **Not measured:** whether a run with a persisted templateId re-stores the run's dates on the template. The daily
  run re-stamps its own Custom dates in any case.

| as-of (14-day Custom window end) | rows listed | rows with a value | accounts with a value | accounts listed | market value |
|---|---|---|---|---|---|
| 2025-03-31 | 19,610 | 35 | 29 | 981 | $9.85M |
| 2025-06-30 | 19,610 | 35 | 29 | 981 | $9.74M |
| 2025-09-30 | 19,610 | 57 | 41 | 981 | $14.45M |
| 2025-12-31 | 19,610 | 83 | 56 | 981 | $21.35M |
| 2026-03-31 | 19,610 | 84 | 57 | 981 | $21.38M |
| 2026-05-29 | 19,610 | 8,979 | 652 | 981 | $314.47M |

Transactions, 2025-12-17 to 2025-12-31: 55 rows across 29 accounts, every trade dated 12/31/2025.

- **BD holds only a sliver of Cottonwood before spring 2026:** 29 to 57 accounts and $10M to $21M through
  2026-03-31. The bulk (652 accounts, $314M) appears between 2026-03-31 and 2026-05-29. That matches Andrew's "only
  has data from maybe a couple months ago". **2025 is NOT usable history for Cottonwood reporting.**
- **This settles the blank-row semantics that the section above held as INFERRED; they are now MEASURED.** Every
  export returns the SAME 19,610 rows, the same count as today's feed, whatever the as-of date, and puts values only
  on pairs with a position at that end date (35 of 19,610 in March 2025). So `includeAll: true` lists BD's CURRENT
  account-holding dimension, and a blank row is a pair with no position on the end date.
  - Discriminating: a window-bounded listing would have returned far fewer rows in 2025.
- **For Performance:** a Cottonwood period starting before about May 2026 covers only the ~29-57 accounts BD held
  then. Any since-inception or YTD-2026 figure for most accounts starts at their BD onboarding, not at the real
  inception. That is a disclosure item, not measured further here.

## Update ~21:1xZ: COT section D correction, and the cause of the first empty response

- **Correction:** a Cottonwood PortfolioReporting body IS retained. `.runtime/codex-seats/4.0.0_SA_CRO/performance-recon/bd_refreshed_period_live.bin`
  is a live replay from 2026-09-10 (HTTP 200, 176,999 bytes, sha256 `31b1727620da...`) of `performancePeriod`, from
  `dashboard_exploration_bdpt2.har` entry 114. **Re-read by this seat:** 35 of 35 `accountInfo` nodes carry an 8-digit
  `accountId` with `externalId == "z09" + accountId` (1 distinct account). That is BD's own namespace rule, exercised
  on COT 7 days before COO~P's positive control. The stale sentence came from the same `.runtime/`-blind search as
  the section A error.
- **Cause of COO~P's first empty response: most likely DATA, not access.** Measured by this seat's read-only research
  subagent over Opal S3 only (instrument: parquet reads; not re-derived by this seat; scratch copies deleted):
  - the account first probed is 1 of only 2 of the 973 Rebalancer accounts absent from the COT holdings silver of
    09-22;
  - it has 0 rows in each of 5 holdings snapshots (06-08, 07-01, 08-03, 09-01, 09-22), in the compacted transactions
    (04-22 to 06-08), in the 09-23 transactions and in `account_attributes` 08-19 (943 rows);
  - in the Rebalancer its strategy is `--` and `can_rebalance` is False.

  The same user and the same request shape returned data on a sibling account, which rules out namespace.
  Account-level access for that one account is not separately tested. No follow-up vendor call is proposed: COO~P
  picks accounts with holdings in the window.

## Update ~21:1xZ: 49F Schwab currency and `net_credit_debit` (for COO~M, request of 20:0xZ)

A read-only repo sweep by this seat's research subagent at HEAD `d9fddeed8e`:

- **No Schwab vendor specification exists in the repo.** The D1 field spec says its catalog came "via live `01_raw/`
  enumeration (not an SI2 vendor spec)" (`docs/architecture/DATA_PLATFORM_D1_schwab_field_spec.md:5,52`).
- **Currency: no currency column in either master's raw ACC or RPS sections** (inventory
  `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/OPAL_RUNNERS_W4_COLUMN_INVENTORY_BOTH_MASTERS_20260714.json`).
  The only near-matches are `acct_mailing_ctry_code` and `security_valuation_unit`. Silver pins the full vendor column
  set and fails on unknown columns (`data/assets/scripts/silver/schwab_schemas.py:164-259,1305-1309`), so none was
  dropped. "USD" appears only in Opal's own gateway description (`infra/aws/ec2/opal-gateway/app/integrations/schwab/datasets.json:56,82-113`).
  **USD for 49F is `held`/`inferred` until a Schwab document or a CTO ruling says otherwise.**
- **`net_credit_debit`: no definition anywhere (UNKNOWN).**
  - It is a raw RPS section 2 column (`schwab_schemas.py:236`).
  - "Total" is `net_mv_plus_cash` (`b00_canonical_valuation.py:53,62`).
  - The repo never derives total = `net_mv_positions` + `net_credit_debit`. COO~M's 7,498 of 7,522 tie is the first
    measurement of that identity found.
  - Overlap is measured: RPS positions include money-market and sweep rows (`data/canonical/schwab/docs/02_FACT_TABLES.md:33-34`).
  - The additive cash rebuild left 4,362 of 7,238 account-days unexplained on 2026-08-07
    (`PROOF_OF_SPEC_P1_B2_GROUPB_20260811.json:27,53`).
  - Opal's rule: never add different balance fields (`.../schwab/semantics.py:9-10`).
  - INFERRED: `money_mkt_funds` sits inside `net_mv_positions`, and `net_credit_debit` is the cash/credit leg outside
    positions, which fits the 321 cash-only accounts.
- **Duplicates and side:**
  - RPS carries one row per cash, margin or short sub-position. The canonical build numbers them `position_seq`
    (`data/canonical/schwab/silver/build_fact_position.py:13-14,67`); `accounting_rule_code` carries CASH/MARGIN/SHORT.
  - A blank `l_s` is vendor bytes as delivered (`schwab_schemas.py:48-49`), contradicting the gateway's "always L or S"
    (`datasets.json:32`).
  - A prior sighting of the position-vs-balance gap found 23 accounts on 08-07.
- **Next checks, Opal data only:**
  1. Re-key the 14 duplicates on `accounting_rule_code`.
  2. Per account on 09-22, compare the summed value of `fact_rps` rows where `mnymk_code` is not blank against
     `money_mkt_funds`. `dim_position` drops `mnymk_code` (`schwab_projections.py:43-51`), which is why `fact_rps`
     is used.
  3. Regress `net_credit_debit` on the settled-cash, margin, sweep and bank-cash fields.

## Per-use captures that would close the rest (all need Andrew's word; none performed)

| Item | Call |
|---|---|
| A | read Orion's tenant or report currency setting |
| B | `POST /v1/portfolio/portfolios/accounts/simple/list` for the 14 Eclipse portfolio ids |
| C | `POST /datamining/request/Query/DimensionsFacts {"queryTypeId":1}` for the holdings field catalog, including any currency field |
| D | none needed beyond the adapter's own first live COT call |

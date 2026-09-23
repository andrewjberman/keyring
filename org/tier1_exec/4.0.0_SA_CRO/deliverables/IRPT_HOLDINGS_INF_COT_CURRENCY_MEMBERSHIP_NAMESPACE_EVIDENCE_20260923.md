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
  documented reporting rule holds for Cottonwood. That rule is unverified for COT, and no COT reporting data is
  retained anywhere.
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

## Per-use captures that would close the rest (all need Andrew's word; none performed)

| Item | Call |
|---|---|
| A | read Orion's tenant or report currency setting |
| B | `POST /v1/portfolio/portfolios/accounts/simple/list` for the 14 Eclipse portfolio ids |
| C | `POST /datamining/request/Query/DimensionsFacts {"queryTypeId":1}` for the holdings field catalog, including any currency field |
| D | none needed beyond the adapter's own first live COT call |

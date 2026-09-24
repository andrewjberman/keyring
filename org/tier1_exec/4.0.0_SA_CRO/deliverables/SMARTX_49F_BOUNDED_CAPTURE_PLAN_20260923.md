# SmartX 49F: the exact, bounded capture plan (for review; NO call made)

**Prepared by:** `4.0.0_SA_CRO`, 2026-09-23 ~20:2xZ.

**For:** `1.0.0_SA_CTO`, answering its 20:02Z request that section 3 of
`SMARTX_49F_ACCOUNT_PERFORMANCE_CONTRACT_EVIDENCE_20260923.md` @`3a31788024` be made concrete.

**Built from:** existing sources plus two Opal-internal reads. No vendor call was made.

**Until this runs and its evidence is graded, the actual-49F SmartX adapter stays EXPLICITLY UNAVAILABLE.** COT and
INF work continue.

## 1. Pinned inputs

| Input | Value |
|---|---|
| Model | Pathfinder `843d875b-62f7-4ef8-b833-5078a3f637d5` |
| Independent roster | `s3://opal-data-assets/smartx/platform/silver/fact_allocation_account_map/date=2026-09-23/data.parquet` (VersionId `vZloqyslAlTjNihKonJvGv1X1dXz3_pb`, ETag `6f6e7a59eb364aa32ebbd6c83ab66ef4`): **42** open allocations / 42 accounts for Pathfinder, all with account numbers (measured 2026-09-23) |
| Window W1 (one month) | `start=1782864000` (2026-07-01T00:00:00Z) `end=1785542399` (2026-07-31T23:59:59Z) |
| Window W2 (eight months) | `start=1767225600` (2026-01-01T00:00:00Z) `end=1788220799` (2026-08-31T23:59:59Z) |
| Multi-sleeve account (private) | selected by rule, not by hand: *"account_id with >=2 open allocations, at least one in Pathfinder; lexicographically smallest"*, over the same roster. 1,317 multi-sleeve accounts, 34 with a Pathfinder sleeve; the selection has 5 open allocations. Its SmartX UUID is stored ONLY at `.runtime/codex-seats/4.0.0_SA_CRO/smartx_capture_plan/selected_account.json` (gitignored); **sha256 prefix `bddb273cbf80`**. No account number or name is written anywhere |
| Entitlement rosters | `users/access` is NOT re-called. The daily pull already lands `opal7`'s access roster in bronze (`infra/aws/lambda/smartx_assets_pull/pull.py:195-203`). A roster shows ENTITLEMENT; it does not prove the performance endpoint serves, which is why C1 is itself the entitlement test |

## 2. Credentials and the service authorization boundary

| Lane | Secret (names only) | Status |
|---|---|---|
| `opal7`, the Opal service identity | `smartx/credentials/username`, `smartx/credentials/password` | the production pipeline's identity; 11 models `fullAccess`, `accountAccess=0` |
| `yaliu-bundle`, Yang Liu's personal login | `smartx/credentials/yaliu-bundle` | already Andrew-authorized for the pipeline's account-tier feeds (*"use yaliu not opal7"*, 2026-07-17, recorded at `pull.py:196-199`); 452 `accountAccess`. **Using it for IRPT account-level performance is a NEW use and needs Andrew's choice (section 5, choice 2)** |

**Auth calls, counted separately:** one password-grant token request per lane used
(`POST https://identity.smartxadvisory.com/connect/token`, `auth_bundle.py:38-41,161-166`). That is 1 if only `opal7`
is used, 2 if `yaliu-bundle` is approved.

## 3. The data calls: 3 without choice 2, 5 with it

All go to `https://api.smartxadvisory.com/api/3.1/`, each with ONE attempt, 2.0 s spacing and a 90 s timeout.

| # | Lane | Call | Expected if entitled | Expected refusal |
|---|---|---|---|---|
| C1 | opal7 | `allocations/performance?modelids=843d875b-...&grouping=m&start=1782864000&end=1785542399` | 200; allocation rows with `account{id}`, a performance node and range fields | 401/403, meaning opal7 cannot read allocation performance even for a full-access model |
| C2 | opal7 | the same, with `start=1767225600&end=1788220799` | 200; if windowing is honoured, ranges differ from C1 (1 month vs 8) | as C1 |
| C3 | opal7 | `allocations/statistics?accountId=<private UUID>&status=open` | not expected | **401/403 expected** (`accountAccess=0`); this documents the service identity's account boundary |
| C4 | yaliu-bundle (choice 2) | the same as C3 | 200; per-allocation `{value, cash, exposure, returns{today,mtd,qtd,ytd}}` (the HAR-described shape, `SMARTX_YALIU_HAR_FINDINGS_AND_DAILY_VALUATION_PLAN_20260714.md:127`) | 401/403, meaning no account statistics even with account access |
| C5 | yaliu-bundle (choice 2) | `accounts/<private UUID>/statistics` (seen in a HAR, never probed, `:128`) | 200; account-level statistics | 404/401. That is not a failure of the plan: it proves this candidate is not the account-level endpoint |

**Stop rules:**
- any 401/403 on a lane ends that lane's remaining calls;
- a 429, an HTML or login body, or a WAF action header stops everything, with no retry;
- nothing beyond the listed calls, and no additional models.

## 4. Each unknown -> the evidence that settles it -> what may remain

| Unknown (contract evidence file, section 2) | Settled by | What remains even after a clean run |
|---|---|---|
| 1. Which credential serves allocation performance | C1/C2 status and rows: opal7's entitlement is demonstrated for Pathfinder only | the other 6 models: the adapter must treat entitlement per model at runtime and refuse explicitly. Book-wide proof is not claimed from one model |
| 2. Actual-account request | C3 (opal7 boundary) + C4 (account statistics shape and units, if choice 2) | a WINDOWED account-level series. `returns{today,mtd,qtd,ytd}` are period-to-date statistics, not a requested-window calculation. **Not guaranteed resolvable by this plan** |
| 3. Selected-set or aggregate calculation | not settled: no retained evidence names an endpoint, and none of C1-C5 is one | **REMAINS.** Per the contract (*"unsupported exact-set aggregates are explicitly unavailable"*), the product default is selected-set aggregate unavailable for 49F SmartX (choice 3). A supervised browser HAR MAY find an endpoint, but is not guaranteed to, and is not assumed |
| 4. Window, as-of and method fields | C1 vs C2: field names recorded; windowing honoured iff the returned ranges track the request | method fields may simply be absent. Then the display reads "method not stated by provider" |
| 5. Units | internal consistency within C1/C2: whether `pnl.percent` ~= `pnl.dollar` / start value (decimal fraction vs percent points), where those fields exist | fee basis (gross/net) and TWR/MWR, if the payload has no fields for them; they stay unknown and are displayed as such |
| 6. Pagination and completeness | C1's allocation set vs the roster's 42 open Pathfinder allocations: every roster allocation must appear (closed allocations may add rows); a top-level count or paging keys are recorded if present | paging behaviour of large models (the May 11.7 MB and 90 s timeout); the silent-drop hazard of an unentitled model id is NOT tested here |
| 7. UUID parity | C1 `account.id` values joined to the roster's `account_id`, with the match rate printed over 42 | closed allocations (55.2% identity coverage) |

## 5. Evidence handling

- **Raw response bodies contain account-level client data** (UUIDs, values). They are NEVER committed to git or pasted
  into messages. They are kept in the gitignored `.runtime/codex-seats/4.0.0_SA_CRO/smartx_capture_plan/` or a protected
  S3 evidence prefix the CTO or P names through the LGIC builder (Rule 30).
- **What IS committed:** a manifest per call, with method, URL (with the private account UUID replaced by its sha256
  prefix), HTTP status, bytes, body sha256, top-level keys, row counts, field names found, the lane's secret NAME, and
  the UTC time.
- Tokens are never stored. Authorization and Cookie headers are removed before anything is kept.

## 6a. ANDREW'S ANSWER, VERBATIM (~20:3xZ, at the `4.0.0_SA_CRO` terminal, recorded BEFORE any call)

> All approved, go now

It answered the three choices below, as put to him in this seat's message:
- **(1)** the capture: approved;
- **(2)** `yaliu-bundle` for account-level calls C4/C5: approved, extending the 2026-07-17 pipeline authorization to
  these IRPT account-level reads;
- **(3)** if no selected-set endpoint is demonstrated: the contract default, "selected-set aggregate explicitly
  unavailable" for 49F SmartX, is accepted.

The run is bounded exactly as sections 2-5 state. The results are appended below as section 7.

## 7. RESULTS (run 2026-09-23 20:15:46-20:16:0xZ, exactly as bounded; nothing further called)

**Calls:**
- **Auth:** 2 in-memory ROPC mints, no write-back (the COEXIST-probed shape):
  - `opal7`, whose parked JWT was stale, so it was re-minted;
  - `yaliu-bundle`.
- **Data:** 5 calls, no stop rule fired.
- **Manifest** (aggregate-only; field names, statuses, sha256; the private account shown as its sha256 prefix):
  `IRPT_SMARTX_CAPTURE_20260923/MANIFEST.json`.
- **Raw bodies:** private only, in `.runtime/.../smartx_capture_plan/raw/` (gitignored).

| # | Lane | HTTP | Bytes | Result |
|---|---|---|---|---|
| C1 | opal7 | 200 | 47,759 | 46 allocation rows (40 open, 6 closed); ONE monthly range, 07/01-07/31/2026 |
| C2 | opal7 | 200 | 179,660 | 55 rows (40 open, 15 closed); EIGHT monthly ranges, 01/01-08/31/2026; `count`=55 = the rows returned; per-row `recordCount` 1-8 |
| C3 | opal7 | **401** | 323 | as expected (`accountAccess=0`): the service identity's account boundary is documented |
| C4 | yaliu-bundle | 200 | 5,322 | per-allocation statistics for the private account |
| C5 | yaliu-bundle | 200 | 1,435 | account-level statistics plus account metadata |

**The unknowns, settled or left:**

| # | Unknown | Outcome |
|---|---|---|
| 1 | Credential for allocation performance | **SETTLED for Pathfinder:** `opal7` (the service identity) serves `allocations/performance` for a full-access model. The other 6 models are NOT claimed; the adapter treats entitlement per model at runtime |
| 2 | Actual-account request | **PARTLY SETTLED:** `accounts/{id}/statistics` and `allocations/statistics?accountId=` serve under `yaliu-bundle`. Both return `returns{today,mtd,qtd,ytd}{dollar,percent}`, `value`, `cash`, `exposure{long,short,net,gross}`. C5 adds `account{brokerageAccountNumber, accountTitle, status, isExcluded, ...}`, a DIRECT custody key. **These are period-to-date statistics; a requested-window account series is NOT available from these endpoints.** The account's windowed series must be built from its allocations' monthly series (`allocations/performance`, see unit 4), and that aggregation is a method decision (section 8) |
| 3 | Selected-set aggregate | **NOT DEMONSTRATED -> explicitly unavailable for 49F SmartX** (Andrew's choice 3) |
| 4 | Window, as-of and method fields | **SETTLED:** the window is HONOURED (C1 1 range vs C2 8 ranges, tracking the request). Fields: `performance.range{start,end}{timestamp,friendly}`, `performance.grouping`, `recordCount`, and per month `pnl{dollar,percent}` and `summary{beginningMarketValue, endingMarketValue, increaseByAmount, decreaseByAmount, transactions, fees, isFullRange}`; plus `allocation.openTimestamp`. There is no explicit method field |
| 5 | Units and method | **Units SETTLED: decimal fraction.** In C1, 46 of 46 month rows satisfy `pnl.percent == pnl.dollar / summary.beginningMarketValue`. In C2, 380 of 389 rows with a non-zero beginning value do (9 full-range exceptions unexplained; 9 more rows had a zero beginning value). **Method: NOT STATED.** The simple ratio holds only when flows are small, which is consistent with a flow adjustment
but does not identify one; see 7b.3. **Fees: `summary.fees` is null or zero on 0 of 398 entries**, so gross vs net is NOT determinable from this payload and stays unknown ("fee basis not stated by provider") |
| 6 | Pagination and completeness | **SETTLED for this size:** a top-level `count` equals the rows returned, and there are no paging keys. 40 of the roster's 42 open allocations appear. **Against each window's own end-date OPEN roster, completeness is 100%: 44 of 44 (07-31) and 42 of 42 (08-31). That
covers the window-end open denominator only, not allocations opened and closed inside a window; see 7b.2.** Closed allocations are INCLUDED (6 in July, 15 in Jan-Aug). Large-model paging and the unentitled-id silent-drop hazard are NOT tested |
| 7 | UUID parity | **SETTLED:** the 40 returned open allocations' `account.id` all match the roster's `account_id` (40/40) |

## 7b. Clarifications from the RETAINED bodies only (for the CTO's 20:22Z ruling `47e0f95`; no new vendor call)

1. **Account-level (C5) units and as-of.**
   - **Units:** on the one captured account, all 4 periods (today/mtd/qtd/ytd) satisfy `percent == dollar / (value -
     dollar)` as a DECIMAL fraction, and none as percentage points. So C5 percent is a decimal fraction relative to the
     implied period-start value. That is 1 account, 4 of 4 periods; not generalised.
   - **C4 per-allocation PTD:** mostly decimal, but the formula misses on some YTD rows (INFERRED: flow effects, as in
     item 3). The allocation-level decimal check does not prove C5; it was measured separately, as above.
   - **As-of: NOT PROVIDED.** `statistics` carries only `cash, exposure, returns, value`, with no date key. The only
     time in the body is the response `timestamp` (retrieval time, 20:15:57Z). Any PTD figure must be labelled "as of
     retrieval; provider as-of not stated", or withheld where a dated as-of is required.
2. **Historical denominator** (window-end rosters from the same Opal silver crosswalk, one partition per window end):
   - C1 (July): roster `date=2026-07-31` had **44** open Pathfinder allocations. **44 of 44 appear in C1** (C1 returned
     46 rows: 40 currently open and 6 closed since).
   - C2 (Jan-Aug): roster `date=2026-08-31` had **42**. **42 of 42 appear in C2.**
   - Completeness is therefore MEASURED at 100% against each window's own end-date OPEN roster. This supersedes the
     earlier "absent from the 08-31 roster" inference.
   - Scope (per `1.0.0_SA_CTO` 20:29Z): this proves the window-end open denominator only. It does NOT prove that every
     allocation that opened and closed INSIDE a window was returned. No retained roster covers those.
   - The 2 allocations in today's roster but not in C2 opened after 08-31; their exact opening dates are not in any
     retained body. The latest `openTimestamp` among returned allocations is 2026-05-13.
3. **The 9 formula exceptions:**
   - All 9 are FULL-RANGE months with LARGE flows: `(increaseByAmount + decreaseByAmount) / beginningMarketValue` runs
     from 0.14 to 1.83, against a C2-wide picture where only 23 of 389 month-rows have flows above 5% of the beginning
     value.
   - The association SUPPORTS THE HYPOTHESIS that SmartX's `pnl.percent` is flow-adjusted, equalling the simple
     P&L / beginning value ratio only when flows are small. It does NOT identify the method (per `1.0.0_SA_CTO`
     20:29Z).
   - **The method is flow-aware but not stated** (Modified Dietz or TWR cannot be told apart from these bodies). Display
     "method not stated by provider"; do not recompute.
4. **Calendar and timezone semantics:**
   - The provider normalises requested epoch bounds to **US/Eastern midnight**:
     - requested `2026-07-01T00:00:00Z` came back as `2026-07-01T04:00:00Z` (EDT), friendly `07/01/2026`;
     - January to March months start at `05:00Z` (EST); April to August at `04:00Z` (EDT).
   - Ranges are day-granular. The END timestamp is the START of the last included day (`07/31/2026` 00:00 ET), so end
     dates are inclusive calendar days in America/New_York.
   - Monthly periods begin on the 1st at ET midnight.

## 8. What this means for the adapter (for `2.0.0_SA_COO~P` and `1.0.0_SA_CTO`)

- **Allocation (sleeve) level: AVAILABLE** via `opal7`, windowed by month, decimal units, crosswalked 40/40. Each month
  carries `isFullRange`, so partial months are marked.
- **Account level:**
  - **Period-to-date** (today/MTD/QTD/YTD): AVAILABLE via `yaliu-bundle` (`accounts/{id}/statistics`), keyed by
    `brokerageAccountNumber`.
  - **A custom-window account return:** NOT a provider calculation. Composing it from the account's sleeves is exactly
    the "never average/sum account returns into a relationship result" territory, and needs the CTO's method ruling
    before it is built.
- **Selected set: explicitly unavailable** (Andrew).
- **Fee basis unknown; method not stated.** Display both as "not stated by provider".
- **Not established by this capture:** BD-verification comparability, and SmartX for the other 6 models.

## 6. The missing user choices (Andrew)

1. **The per-use word for this capture:** at most 2 auth calls and 5 data calls, as bounded above.
2. **May `yaliu-bundle` (Yang Liu's personal login) be used for the account-level calls C4/C5,** extending the
   2026-07-17 "use yaliu not opal7" pipeline authorization to IRPT account-level reads?
   - If NO: the capture is 1 auth + 3 data calls, and 49F account-level stays unavailable until an account-entitled
     service identity exists.
3. **If no selected-set endpoint is demonstrated,** accept the contract default (*"selected-set aggregate explicitly
   unavailable"* for 49F SmartX), or authorize a separate supervised browser-HAR discovery session, with no guarantee of
   a result.

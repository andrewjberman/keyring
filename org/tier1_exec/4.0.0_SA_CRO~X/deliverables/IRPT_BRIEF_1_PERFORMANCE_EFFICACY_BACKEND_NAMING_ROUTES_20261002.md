# Brief 1 of 3 -- Investor Reporting PERFORMANCE (49 Financial): calculation efficacy, backend, naming, routes, status

**Author:** `4.0.0_SA_CRO~X`, 2026-10-02. **For:** `1.0.0_SA_CTO`, to fold into the Performance workstream
(`2.0.0_SA_COO~P`; the next-generation figure is IRPT_DASHBD workstream B, also issued by `2.0.0_SA_COO~P`).
**Source of the ask:** Andrew-direct 2026-10-02 ~14:5xZ, record
`org/tier1_exec/4.0.0_SA_CRO~X/deliverables/ANDREW_DIRECT_20261002_145xZ_IRPT_THREE_SURFACES_STATUS_AND_THREE_BRIEFS.md`
@fc46925968, points P1-P4. Siblings: brief 2 (Analysis), brief 3 (Holdings) in this folder.
**Claim words:** `measured` = read live this session; `held` = cited from a committed record, not re-run; `inferred` =
derived from code or records; `absent` = searched for and not found.

Andrew, verbatim (P1-P2): "For performance, I need to know the status on 49 Financial's calculations and modeling. The
last i heard, we had been able to put together holdings-based reporting that was precise on a net and gross basis to
3,000 accounts of which we had the ability to verify via Black Diamonds associated endpoints."

## 1. Calculation efficacy (P1, P2, first half of P4): PARTIALLY clear, and not on the claim as remembered

1.1 **Where "3,000 accounts" comes from** (held). The ADVI_BDPARITY P2-2 census of 2026-09-01
    (`org/tier2_senior/0.4.0_DS_ClientPlatform~Y/deliverables/ADVI_BDPARITY_P2-2_CENSUS_RESULT_20260901.md` @3637812fbc,
    table at `:90-96`) compared 49 Financial against Black Diamond's own Reporting PERFORMANCE endpoint, landed as
    bronze (5,309 accounts). On the 1-year period **3,003 of 5,156 accounts agreed EXACTLY (within 0.5 basis points)**;
    1,161 within 10 bp; 992 beyond. Over all three periods, 6,226 of 15,445 results were EXACT and 1,994 LARGE ones
    were never closed. No record states "net and gross to 3,000 accounts" (absent: `git log --grep` over
    3,000 / net and gross, since 2026-08-01).
1.2 **It was the NET figure only.** The census design kept the gross leg UNAVAILABLE
    (`org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ADVI_BDPARITY_BP1-4_CENSUS_DESIGN_20260830.md:72`); no later
    record compares gross at population (held).
1.3 **It measured an engine the page no longer uses.** The census graded the flow-based engine (`canonical/twr_daily`).
    On 2026-09-28 Andrew ruled holdings-based performance for every firm; the page switched to the holdings gold on
    2026-09-29 (IB-pr-201) (held).
1.4 **What serves today** (measured): Opal's holdings-based PRICE return,
    `s3://opal-data-49financial/irpt/49financial/gold/holdings_performance_daily/`, 561 daily partitions
    2024-07-09..2026-10-01 (latest written 2026-10-02T11:30Z, current to the prior trading day); on 2026-10-01, 7,570
    accounts, 6,678 computable. Per day it is the value-weighted return of the prior day's holdings with cash earning
    zero; no fees, no income, no external flows. Its only population check against Black Diamond (2026-09-29,
    @8798bc4c4a, held): 3,994 of 4,098 fully covered accounts (97.5%) within 5 PERCENTAGE POINTS over one year, median
    gap 1.64 points with Opal below Black Diamond, as two different bases should be. That bounds the figure; it is not
    precision.
1.5 **The label is wrong.** The served adapter stamps `fee_basis = "NET"` on that no-fee price return
    (`infra/aws/lambda/investor-reporting/performance/holdings_gold.py:270`, measured). The IRPT_DASHBD PRD names the
    same defect; no surprise row tracks it on IRPT_BCKEND (inferred).
1.6 **Net vs gross is already ruled.** Andrew, 2026-09-30, verbatim: "Yes gross of fees is correct, we're not dealing
    with these fuckers fees because we don' tknow their fee methodology", plus a fee "rail" for later
    (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260930_06xxZ_REPORTING_DASHBOARD_TWO_BRIEFS_SCOPE_ANSWERS.md:35-44`).
    Today's "net and gross" wording is therefore an open question for Andrew (section 7, call 1), not a ruling.
1.7 **The replacement he asked for is not served.** The GIPS total return of 2026-09-30 (end-of-day flows, income on
    cash receipt, gross of fees, fee rail unused) is IRPT_DASHBD's `account_return_daily`: built for 6 accounts, its
    read route not served, "The thread is NOT live" (CTO round-1 analysis); its Black Diamond tie-out had 0 like-day
    pairs, and PRD v0.6 (@aabc054e89) grades agreement only on like day sets (held).
1.8 **A wrong figure is still served elsewhere.** The D2-held perfrp leaf
    `s3://opal-data-portal-v2/platinum/advi/49financial/perfrp_performance_account.json` serves Since-inception figures
    inflated by the 2025-01-10 cash-flow defect (account 0093614544: +69.80% against +8.47%), row W100-S2, parked until
    Andrew lifts the D2 hold (held).

**Verdict (1).** Precision against Black Diamond was proven only for the retired engine's NET figure. The served
figure and the planned one have no tight population check. "Clear on efficacy" needs one population tie-out of the
figure the page will serve, against Black Diamond's performance endpoint, on like day sets, with the band stated
before the run.

## 2. The backend data structure, and why the tab is slow (P3)

Andrew, verbatim (P3): "I also want to know the exact backend data structure, because all of that has to be designed in
a manner that it is precomputed. There cannot be any lags in this functionn, currently it is very very slow and not
functional as a result."

2.1 **Two Performance backends are live, and the page uses both** (measured):
    - **PATH A, compute on request (IRPT_BCKEND).** `GET /api/scoped/investor-reporting/performance/{accountSetId}?start&end`
      -> Lambda `irpt-performance-adapter`. Only the DAILY return is stored. Every window figure (YTD, 1Y, since
      inception) is computed per request: list all 561 date partitions, read one firm-wide parquet per trading day in the
      window (YTD ~185 files, since inception 561), filter to ONE account, chain
      (`infra/aws/lambda/investor-reporting/performance/holdings_gold.py:202-260`). One account, one window per request.
    - **PATH B, precomputed (IRPT_DASHBD).** Gold `account_return_daily` -> publisher writes per-account
      `series.json.gz` + `manifest.json` -> `GET /api/scoped/investor-reporting/reporting/{account_id}/{manifest|series}`
      -> Lambda `irpt-49f-reporting-read-lambda`, which streams stored bytes and recomputes nothing. This is the design
      Andrew ordered on 2026-09-30 (`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260930_052xZ_PRECOMPUTED_GZIP_JSON_REPORTING_UNDER_2S_AND_PUSH_MANAGED.md`).
      It covers SIX 49 Financial accounts, by design: "six accounts stay six; widening the population is a deliberate
      act" (`infra/aws/lambda/investor-reporting/reporting-gold/handler.py:18-19`, measured).
    - The page tries PATH B first and falls back to PATH A for every account without a published manifest, i.e. all
      49 Financial accounts but six (held, `STATUS~D.md` item 1, portal `39b7a0fc`).
2.2 **The stores** (measured; every address is `lib/opal_naming.py address()` output):

| Store | Address | Grain | Coverage |
|---|---|---|---|
| holdings-basis gold | `s3://opal-data-49financial/irpt/49financial/gold/holdings_performance_daily/date=YYYY-MM-DD/data.parquet` | account x day, one firm-wide file per day, 19 columns (daily_return, account_value, status, excluded/included counts and values, cash_value, ...) | 561 days, 7,570 accounts on 10-01 |
| reporting gold | `s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/date=YYYY-MM-DD/data.parquet` | account x day, 19 columns (market_value_eod, external_flow, income_received, total_return_daily, return_basis, fee_amount, day_quality, guard_state, method_version, ...), contract `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` 0.2.0 | 562 days, 6 accounts |
| platinum | `s3://opal-data-49financial/irpt/49financial/platinum/reporting/account=<id>/series.json.gz` + `manifest.json` | one gzip JSON per account, columnar per-day arrays, contract `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` 0.1.0 | 6 accounts, 2.3-17.8 KB each |

    Producers (schedules ENABLED, measured): `irpt-holdings-performance-lambda` (daily; served code 363dc1fda4,
    emission 1.1); `irpt-49f-reporting-gold-lambda` `cron(41 7 ? * MON-FRI *)`; `irpt-49f-reporting-publish-lambda`
    `cron(15 8 ? * MON-FRI *)`.
2.3 **Why it is slow** (measured):
    - **Fan-out.** `portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx:614-640` loops over EVERY account
      in the client's list and fires one PATH A request per account for the picker's YTD figure, again on every window
      change. A client with N accounts costs N request-time computations.
    - **Each computation is heavy.** One firm-wide 305 KB parquet per trading day to extract one account: YTD ~56 MB,
      since inception ~170 MB read per request (inferred from measured object sizes).
    - **CloudWatch, 2026-09-25..10-02, `irpt-performance-adapter`:** 1,218 invocations, p50 0.87 s, p95 12.0 s, p99
      24.2 s, max 30.2 s; 27 of 82 invocations today were cold starts. Timeout 120 s, 1,536 MB.
    - **The 29 s gateway cap** (`infra/aws/terraform/investor-reporting/api/integrations.tf:58`
      `timeout_milliseconds = 29000`) turns the slow tail into hard failures (503 to the browser) while the Lambda runs on.
    - **PATH B for comparison:** read Lambda p50 1.9 ms warm; the signed-in FWD-1 run measured tab press to painted chart
      5.3 s (manifest 2.9 s, then series 1.7 s, sequential) and 0 requests on window changes (held,
      `FWD1_REAL_RUN_20261002.md` @74df2f62dd). Andrew's 09-30 target is under 2 s.

## 3. Routes and the pattern (P4)

All IRPT routes sit on one HTTP API under `/api/scoped/investor-reporting/`, one custom authorizer, one AWS_PROXY
integration per Lambda, one shared boundary `_authz/served.py` (measured, `aws apigatewayv2 get-routes`):

| Surface | Route | Lambda | Model |
|---|---|---|---|
| Performance A | GET `/performance/{accountSetId}` | irpt-performance-adapter | compute on request, selection id |
| Performance B | GET `/reporting/{account_id}/{manifest\|series}` | irpt-49f-reporting-read-lambda | stream precomputed bytes, account id |
| Holdings | GET `/holdings/{accountSetId}` | irpt-holdings | thin projection over a scheduled publication, selection id |
| Analysis | POST `/analysis`, `/analysis/inputs`; GET `/analysis/comparisons`, `/analysis/requests[/{id}]`, `/analysis/{jobId}/sections`, `/status[/{jobId}]` | irpt-ycharts-generate, irpt-status | async job + poll |
| Shared | `/directory/*`, `/selections`, `/export/*`, `/narrative/{reportId}` | irpt-directory-search, irpt-export-render, irpt-narrative | sync / async |

**Pattern verdict.** The prefix and auth pattern is uniform. The data pattern is clear for Holdings (scheduled
publication, thin read) and Performance B (scheduled publication, byte stream); **Performance A is the outlier** (the only
route that computes on request) and Performance alone has two routes in two id spaces. `comp-routes api-routes` does not
model this API (22 routes, none IRPT): a tool gap, noted.

## 4. LGIC naming (P4)

Doctrine `infra/logic/02_DOCTRINE.md`; builder `lib/opal_naming.py` `address()` / `name()` / `grade()` (measured):
4.1 **Conformant:** every Performance S3 address and bucket `opal-data-49financial`; the data-plane Lambdas
    `irpt-holdings-performance-lambda`, `irpt-49f-reporting-gold-lambda`, `irpt-49f-reporting-publish-lambda`,
    `irpt-49f-reporting-read-lambda`, `irpt-holdings-refresh-lambda`; role `irpt-performance-adapter-role`.
4.2 **Out of pattern** (missing the `-lambda` kind slot): the nine request-path Lambdas `irpt-performance-adapter`,
    `irpt-holdings`, `irpt-ycharts-generate`, `irpt-directory-search`, `irpt-export-render`, `irpt-status`,
    `irpt-narrative`, `irpt-directory-refresh`, `irpt-intake-poller`; policy `irpt-performance-adapter-logs` (missing
    `-policy`). The adapter's environment still maps firms to LEGACY buckets (`IRPT_DIRECTORY_BUCKET_MAP`: 49financial ->
    `opal-data-bd`, which grades as an ALIAS).
4.3 **No exception is registered.** `infra/logic/06_CONFORMANCE_LEDGER.md` has one IRPT entry (X10, axis A2); none
    covers these names. Rule 30 binds new pipelines; existing ones conform through an R19 migration project. Whether IRPT's
    route Lambdas (built 09-11..09-24) count as existing is recorded nowhere (absent) -- the CTO's ruling.

## 5. Development status (P4)

- **IRPT_BCKEND~P** (PRD v0.24; FULL mode, `/canonical-drive` 10m): adapter served at `cdbFZDJA..` (10-01 08:20Z) on
  the holdings gold; producer 363dc1fda4 served; emission 1.2, linked rows and the Inflection root are on CLOUD, not
  built. Next: the Inflection serving packet (DRAFT @9893683dc3), waiting on Andrew's word to delete nine stale gap-day
  objects; then the mirror release packet (held, `STATUS~P.md`).
- **IRPT_DASHBD** (PRD v0.6): FWD-1, one 49 Financial account end to end, RAN signed in on the real backend 2026-10-02
  06:26Z and 08:13Z; ACCEPT is Andrew's, the grade the CVO's. Open: TO-DB-b-10 (one Black Diamond pull over Opal's
  accounts), DB-b-2/DB-b-4 on worker `0.9.0_WK_IRPT_DASHBD~1` (held).
- **Not started:** widening PATH B past six accounts; any Inflection or Cottonwood reporting gold; the picker reading
  precomputed figures; PATH A's retirement.

## 6. Outcomes for the fold-in (each is something a person can do)

- **P-1** An advisor opens the Performance tab for any 49 Financial client and sees the account picker and the chart
  painted in under 2 s; changing the window computes nothing on the backend.
- **P-2** Every 49 Financial account in the holdings population has a published manifest and series (not six);
  Inflection and Cottonwood follow, each when its gold is served.
- **P-3** The picker's per-account figures come from one precomputed read per client (a manifest summary), not one
  request per account.
- **P-4** The figure says what it is: gross of fees, the 09-30 total-return method; no "NET" label on a no-fee figure.
- **P-5** A reader can see one population tie-out of the served figure against Black Diamond's performance endpoint, on
  like day sets, per period, with the agreement band stated before the run.
- **P-6** When a firm is fully served by PATH B, PATH A for that firm is retired in the same window (no two paths).
- **P-7** Each out-of-pattern name in 4.2 is either renamed to builder output under a migration or listed as an R20
  departure Andrew acknowledges.

## 7. Calls for Andrew (each with a recommendation)

**RULED 2026-10-02 ~18:1xZ** (record addendum 3): call 1 = gross for now, net-fee operations assessed per
custodian/vendor firm by firm (Orion for Inflection, possibly raw custodial data from Cottonwood, Black Diamond
otherwise); call 2 = APPROVED, widen to every 49 Financial account now, then each firm. Call 3 (naming) was not put to
Andrew: it is the CTO's unless the exception route is chosen.

1. **Net as well as gross?** The 09-30 word is gross only, with a fee rail for later. Recommendation: keep gross; label it;
   build the fee rail when a fee field exists.
2. **Widen the precomputed path to the whole population.** Today's "has to be designed in a manner that it is
   precomputed" reads as that order; the CTO confirms it as the deliberate act `handler.py:18-19` waits for.
   Recommendation: all 49 Financial accounts first, then each firm as its gold serves.
3. **Naming:** rename under migration or register the exception. Recommendation: rename at the same move that retires
   PATH A, so no Lambda is renamed twice.

## 8. What this brief does not claim

- No Black Diamond call and no tie-out run were made; section 1's figures are held from committed records.
- The 56 MB / 170 MB per-request read volumes are inferred from object sizes, not logged per request.
- PATH B's 5.3 s is one signed-in run; it is not a distribution.

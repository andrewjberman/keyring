# DATA_PLATFORM D2b -- Black Diamond REST Endpoint + Payload Catalog

**Status:** v0.2 DRAFT -- the sweep RAN (off-box, no EC2 needed -- see sec.2 correction). **DECISIVE FINDING: Billing is a separate BD app/API (`billing.bdreporting.com`), NOT a DataMining query type.** Its Accounts-Receivable fee-charge endpoints are enumerated (sec.6) but return 403/405/500 under the current session -- role/shape unresolved, not "doesn't exist". CTO arch-gate + CVO reconcile pending.
**TO:** `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/DATA_PLATFORM.D2b.bd-rest-endpoint-catalog.md`
**Author:** 0.4.0_DS_ClientPlatform (Andrew-direct 2026-07-08). **Consult:** 0.7.0_AE_CloudOps (on-box). **Verify:** 3.0.0_SA_CVO.
**Sibling of:** `DATA_PLATFORM_D2_BLACK_DIAMOND_ARCH_SPEC.md` (the DataMining model) + `DATA_PLATFORM_D4_smartx_endpoint_sweep.md` (the endpoint-sweep pattern this applies to BD).
**Tool:** `data/cot/scripts/bronze/bd_endpoint_sweep.py` (the a-la-carte query harness + sweep engine).

> **Purpose (Andrew-direct 2026-07-08):** a **dedicated catalog of every BD REST endpoint + its payload**, so we can query the BD database **a-la-carte, purpose-based, outside the scheduled ETL** -- instead of relying only on the 5 fixed view-pulls. D2 documented the DataMining *flow* for the 5 query types cot ingests; it never swept the full surface. This is the "D4-for-BD" catalog.

---

## 1. Origin

Christa Bass (Financial Advisor, Cottonwood) emailed Andrew 2026-07-08: *"Mgmt fees hit Black Diamond today!"* A DS probe (COO GO, Andrew-direct) ground-truthed the cot bronze: the management-fee **CHARGES are absent** from every partition. cot ingests only qt1-5 (holdings/transactions/realized/unrealized/allocations); **none is a billing query type.** The billing fields we *do* carry (allocations/realized/unrealized) are billing **CONFIG** (fee-schedule rates, discount %, billing-config names) -- the *rate a client would be billed*, not the fee *charged*. Transactions' only fee-shaped rows are custodian ADR/expense/debit-card items (`Transaction Fee`/`Account Fee` = 0). So the mgmt-fee charges post into a BD **Billing** surface we do not query -- which is exactly why the Cottonwood Books tab renders `fee_earning_aua` / `implied_revenue` / `distribution` = 0. Closing that gap **starts** with cataloging the surface (this doc) -> finding the billing query type -> wiring it in (a follow-on build TO).

## 2. Auth model (grounded -- D2 sec.3, CORRECTED 2026-07-08)

**CORRECTION (Andrew directly challenged + DS tested live, 2026-07-08): "IP-bound, off-box replay fails" is DISPROVEN for querying an established session.** D2 sec.3 asserted this as "the hard infra constraint," traced to a single 2026-06-09 incident that memory honestly called "suspected own-goal" (never confirmed) and that was confounded with the separately-real short-TTL fact below. Live test from a non-EC2 machine, same cached `blackdiamond/cot/session` secret: `auth/token` mint (200, valid token, `x-session-expires-in:1199`), a full enriched-template GET (200, 23.8KB), and the full template-list GET (200, 44.7KB) all succeeded off-box, back to back, zero blocking. **Querying an established session needs no EC2/SSM.** Residual, still untested: the interactive LOGIN (Playwright, new session) has real bot-detection (`EC2_EXPORTER.md`) and may still benefit from the EC2's IP/browser reputation -- that's a different mechanism, not retested here (real risk of tripping a live-vendor lockout). Session REFRESH stays on-box until that's deliberately tested; QUERYING does not.

Two-credential split. Effective session TTL ~30-60 min (cf_bm + idsrv idle, confirmed) -> a fresh `opal-cot-bd-session-fetch` still precedes any multi-hour campaign, regardless of origin.

| Step | Endpoint | Auth | Yields |
|---|---|---|---|
| mint bearer | `GET /datamining/auth/token` | Cookie (`.bd.identity` jar) | `{access_token}` -- opaque, short-lived |
| catalog/template ops + run | (Bearer) | `Authorization: Bearer` | template GETs, run POST |
| binary export | `GET /Api/DataMining/ExportResults/{guid}` | Cookie | xlsx bytes |

## 3. KNOWN endpoints (grounded in `cot_bronze_ingest.py` -- the 5-table ETL flow)

| Method | Path | Auth | Payload / role |
|---|---|---|---|
| GET | `/datamining/auth/token` | Cookie | `{access_token}` bearer mint |
| POST | `/datamining/request/v1/template/` | Bearer | create a template (body = enriched query) -> `{templateId}` |
| GET | `/datamining/request/v1/template/{id}` | Bearer | the FULL enriched template body (levels/dimensions/facts) -- the server-side persisted selection |
| POST | `/datamining/request/v1/run` | Bearer | `{template, asOfDate}` -> `{templateId(runId), resultGuid}` (async materialize) |
| GET | `/datamining/request/v1/run/{runId}/status` | Bearer | `{statusMessage, isComplete}` -- poll; error-while-incomplete bail |
| GET | `/Api/DataMining/ExportResults/{guid}` | Cookie | xlsx bytes (`Sheet1`=data, `Timestamps`=as-of meta) |

### 3.1 Query types (the table families) -- CONFIRMED CLOSED: there is no Billing query type

**The real roster endpoint is `GET /datamining/request/v1/template` (list, no params)** -- NOT a numeric `/querytype/{id}` catalog (that guess 404s everywhere). It returns every template ever persisted on the account. Grounded 2026-07-08 against the FULL roster (hundreds of templates, Andrew's live BD session, HAR-captured + live-replayed): the only `queryType` values that have EVER existed on this Cottonwood account are:

`Transactions, Allocation, Snapshot, RealizedGainLoss, UnrealizedGainLoss, NotAQueryType` (the last = abandoned/misconfigured template attempts, not a real type).

| queryTypeId | queryType name | Table | Ingested? | Leaf grain | Key measures |
|---|---|---|---|---|---|
| 1 | Snapshot | holdings | YES | Account x Holding (snapshot) | Market Value, Accrual, Units, Unaccrued Market Value |
| 2 | Transactions | transactions | YES | Transaction | Units, MV, Transaction Fee, Income, Account Fee |
| 3 | RealizedGainLoss | realized | YES | Tax Lot (closed) | Units, Cost Basis, Proceeds, ST/LT G/L, Total Gain Loss, Disallowed Loss |
| 4 | UnrealizedGainLoss | unrealized | YES | Tax Lot (open) | Units, Cost Basis, Amortization, MV, ST/LT G/L, Accrual |
| 5 | Allocation | allocations | YES | Account (allocation rollup) | Market Value (Child Facts) |
| -- | (none) | **BILLING** | **N/A -- no such query type exists** | -- | -- |

**CLOSED, not pending:** Andrew independently confirmed this live (2026-07-08) by building a "Billing Snapshot" template himself in the BD UI (`queryTypeId:1`, i.e. Snapshot) and selecting every billing-labeled dimension available (`Portfolio - Billing Configuration Name`, `Fee Schedule Rate/Type/Level`, `Basis Points`, `Flat Fee`, `Billing Discount Percentage`, etc. -- 8 Portfolio-level + 28 Account-level fields). **The Snapshot query type's ENTIRE fact/measure catalog is `{Market Value, Accrual, Units, Unaccrued Market Value}` -- zero billing/fee-charge measures exist for Snapshot, structurally.** Same for the other 4 (their facts are gain/loss/MV only -- see table above). **There is no fact anywhere in DataMining that carries a posted fee charge.** Everything billing-shaped in DataMining is Portfolio/Account-level CONFIGURATION (rate/schedule/discount), never a charge. This closes the "hunt within DataMining" thread definitively -- see sec.6 for where the charges actually live.

## 4. A-la-carte querying (the tool)

`data/cot/scripts/bronze/bd_endpoint_sweep.py` -- run ON-BOX (cot-exporter, fresh session):

```
python3 bd_endpoint_sweep.py                    # full catalog pass (spec-hunt + querytypes + sweep + billing)
python3 bd_endpoint_sweep.py --billing          # find + dump the billing query-type catalog (no run)
python3 bd_endpoint_sweep.py --probe /datamining/request/v1/querytype   # GET any endpoint, dump the payload
```

Output -> `s3://opal-data-cot/code/bronze/endpoint_catalog/` (`endpoint_sweep_result.json`, `querytype_catalog.json`, `billing_catalog.json`, `probe/{path}.json`). The `--probe` primitive is the athletic ad-hoc query: hit any BD path, capture the payload -- no template, no ETL.

## 5. Completeness basis + PENDING (the on-box sweep) -- D4 method

Per the D4 discipline (basis (a) spec-proven vs basis (b) observed/probed): the BD REST surface has **no known published spec** (a swagger/openapi spec-hunt is the first sweep step). So the catalog is **basis (b) -- observed + actively probed**; a 404 in the sweep = *as-of-date absent*, NOT *provably-cannot-exist*. The PENDING live sweep (AE, on-box, fresh session) fills:

- **spec-hunt** -- swagger/openapi/OIDC-discovery candidates (is any part spec-published?).
- **query-type enumeration** -- ids 1..25 -> name + dim/fact counts -> **surfaces BILLING + every unused query type**.
- **endpoint exhaustion sweep** -- candidate DataMining + billing paths -> per-path status/bytes/ctype/sample.
- **billing focus** -- the billing dimension/fact catalog + a small billing pull -> the mgmt-fee CHARGE fields/accounts/magnitude (answers the Christa/COO delta, Rule 22-grounded on the live response).

**On completion:** fill sec.3.1 (the full query-type roster) + a per-endpoint payload table + the billing-charge finding; then CTO arch-gate + CVO reconcile -> v1.0. Fold in the still-un-run D2 sec.7 enriched-template dump (same on-box window, if session-refresh still needs the EC2 -- see sec.2 correction).

## 6. WHERE THE BILLING CHARGES ACTUALLY LIVE -- a separate federated app (`billing.bdreporting.com`), not DataMining

Found via a static-analysis technique (grep the SPA's own JS bundle for embedded route/host strings -- the same discovery method D4 used for SmartX): `bd3.bdreporting.com`'s federated-header bundle (`bd-federated-header/main.*.js`) carries a module-name map with distinct keys `Billing:"billing"`, `BillingManagement:"billing_management"`, `BD3Billing:"bd3_billing"` -- separate federated modules from Data Mining. A CSP/config literal in the DataMining page repeats `billing.bdreporting.com` 11x; Pendo's agent config additionally confirms `billing.dev.bdreporting.local` / `billing.staging.bdreporting.local` (dev/staging siblings) -> production is **`billing.bdreporting.com`**.

**Confirmed live, 2026-07-08 (read-only GETs, off-box):**
- `GET https://billing.bdreporting.com/` -> **200**, a completely separate Angular/React SPA, `<title>Billing</title>`. The SAME `.bdreporting.com`-scoped session cookies (`.bd.identity`, `__cf_bm` -- both domain=`.bdreporting.com`) authenticate here with zero extra login -- confirms it's a sibling federated app under the same OIDC realm, not a separate credential.
- The app has its **own bearer-mint endpoint**, same pattern as DataMining: `GET https://billing.bdreporting.com/auth/token` (Cookie-authorized) -> **200, valid `access_token`**.
- Its JS bundle (`/dist/web.module.js`) contains a rich REST surface under `/api/*` -- the real Billing/Accounts-Receivable API. Selected routes (full list in the bundle, this is the fee-relevant subset):

| Path | Likely role |
|---|---|
| `GET/POST /api/accountsreceivable/dashboard/fees/overview` | fee dashboard summary -- **the Christa-relevant surface** |
| `GET/POST /api/accountsreceivable/dashboard/fees/outstanding` | outstanding (unpaid) fee charges |
| `/api/accountsreceivable/fees/active` | active fee charges (405 on GET -- likely POST-only, search-style like DataMining `v1/run`) |
| `/api/accountsreceivable/txns/active` | active AR transactions -- probably the actual posted CHARGE rows |
| `/api/accountsreceivable/summary/account/unreconciled/`, `.../portfolios/unreconciled/` | unreconciled fee summaries |
| `/api/accountsreceivable/reconcile/manual/*` | **WRITE/mutating -- reconcile actions. DO NOT CALL (out of read-only scope).** |
| `/api/feeSchedule`, `/api/feeSchedule/countstats` | fee-schedule config (the CONFIG side, mirrors what DataMining already exposes) |
| `/api/dashboard/revenue` | firm-level revenue dashboard |
| `/api/expenseCredit/*` | fee credits/adjustments |
| `/api/exportRequest/feeschedules`, `/api/exportRequest/feesplits` | export jobs for fee schedules/splits |

**Current state (read-only GETs against 3 of these, 2026-07-08):** `fees/overview` -> 403, `fees/outstanding` -> 403, `dashboard/revenue` -> 500 (real BD error envelope: `{title,status,detail,traceId}` -- confirms the route exists and is being hit, not a 404 ghost). **403 most likely means the current session's role (Andrew.Opal, provisioned for DataMining/reporting) lacks Billing-module permission** -- a plausible, ordinary permission boundary, not a technical dead-end. 405 on a couple of routes confirms they're real but want a different HTTP verb (POST with a body, same pattern as DataMining's `v1/run`).

**This is the closing answer to "what is Christa talking about":** Black Diamond's management-fee CHARGES live in this separate Accounts-Receivable module, entirely outside the DataMining API cot's ETL (or any DataMining a-la-carte query) can reach. Closing the loop needs EITHER (a) a Billing-module role grant for the session identity, then a correct request shape (POST body, matching the DataMining `v1/run` pattern) against `fees/overview`/`txns/active`, OR (b) Andrew capturing a HAR of himself actually clicking into the live Billing UI (which will show the exact authorized request shape a real client sends -- the fastest path to a working a-la-carte call). Once either lands, the follow-on D2c build TO (wiring a Billing puller into cot's ETL, or standing up an a-la-carte Billing probe) has a real, confirmed contract to build against.

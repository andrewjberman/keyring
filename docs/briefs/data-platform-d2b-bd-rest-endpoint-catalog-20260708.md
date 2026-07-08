# DATA_PLATFORM D2b -- Black Diamond REST Endpoint + Payload Catalog

**Status:** v0.3 -- **RESOLVED with real numbers.** DataMining DOES carry a genuine fee-CHARGE query type: **queryTypeId 6, "BI Billing"** (Andrew discovered it live 2026-07-08; it never showed up in the historical template roster because it had simply never been used on this account before, correcting v0.2's premature "no billing query type exists" verdict -- see sec.3.2). Built + ran a probe query selecting its `Fees` measure: **$1,006,622.12 total fees, 618 of 806 accounts, posted for period-end 07/31/2026** -- the concrete answer to Christa's "mgmt fees hit BD today." The separate `billing.bdreporting.com` Accounts-Receivable app (sec.6) still exists and is real, but is NOT needed for this -- DataMining qt6 already answers it. CTO arch-gate + CVO reconcile pending.
**TO:** `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/DATA_PLATFORM.D2b.bd-rest-endpoint-catalog.md`
**Author:** 0.4.0_DS_ClientPlatform (Andrew-direct 2026-07-08). **Consult:** 0.7.0_AE_CloudOps (on-box). **Verify:** 3.0.0_SA_CVO.
**Sibling of:** `DATA_PLATFORM_D2_BLACK_DIAMOND_ARCH_SPEC.md` (the DataMining model) + `DATA_PLATFORM_D4_smartx_endpoint_sweep.md` (the endpoint-sweep pattern this applies to BD).
**Tool:** `data/black_diamond/API/tools/bd_endpoint_sweep.py` (the a-la-carte query harness + sweep engine; relocated 2026-07-08 to the shared vendor-neutral catalog, see `data/black_diamond/API/README.md`).

> **Purpose (Andrew-direct 2026-07-08):** a **dedicated catalog of every BD REST endpoint + its payload**, so we can query the BD database **a-la-carte, purpose-based, outside the scheduled ETL** -- instead of relying only on the 5 fixed view-pulls. D2 documented the DataMining *flow* for the 5 query types cot ingests; it never swept the full surface. This is the "D4-for-BD" catalog.

---

## 1. Origin

Christa Bass (Financial Advisor, Cottonwood) emailed Andrew 2026-07-08: *"Mgmt fees hit Black Diamond today!"* A DS probe (COO GO, Andrew-direct) ground-truthed the cot bronze: the management-fee **CHARGES are absent** from every partition. cot ingests only qt1-5 (holdings/transactions/realized/unrealized/allocations); none of the 5 carries a fee-charge fact -- only CONFIG (fee-schedule rates, discount %, billing-config names, the *rate a client would be billed*, not the fee *charged*). Transactions' only fee-shaped rows are custodian ADR/expense/debit-card items (`Transaction Fee`/`Account Fee` = 0). **RESOLVED (sec.3):** BD DOES have a 6th query type, `BI Billing` (queryTypeId 6), carrying a genuine `Fees` measure -- it simply had never been used/persisted on this account before, so it was invisible to a template-history-based roster (sec.3.2). A probe query against it (sec.3.3) confirms **$1,006,622.12 in fees posted across 618 accounts for the period ending 07/31/2026** -- the concrete, grounded answer to Christa's email. This is exactly why the Cottonwood Books tab renders `fee_earning_aua`/`implied_revenue`/`distribution` = 0: cot's ETL simply never configured qt6 as a 6th ingested table. Closing that gap is a follow-on D2c build TO (wire qt6 into `cot_bronze_ingest.py` as a 6th table).

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

### 3.1 Query types (the table families) -- 6 confirmed, incl. the real billing type

**The real roster endpoint is `GET /datamining/request/v1/template` (list, no params)** -- NOT a numeric `/querytype/{id}` catalog (that guess 404s everywhere). It returns every template ever PERSISTED on the account -- a HISTORY, not the full catalog of query types BD offers. That distinction matters (see 3.2): a query type with zero prior usage is invisible to this endpoint until someone builds one.

| queryTypeId | queryType name | Table | Ingested? | Leaf grain | Key measures |
|---|---|---|---|---|---|
| 1 | Snapshot | holdings | YES | Account x Holding (snapshot) | Market Value, Accrual, Units, Unaccrued Market Value |
| 2 | Transactions | transactions | YES | Transaction | Units, MV, Transaction Fee, Income, Account Fee |
| 3 | RealizedGainLoss | realized | YES | Tax Lot (closed) | Units, Cost Basis, Proceeds, ST/LT G/L, Total Gain Loss, Disallowed Loss |
| 4 | UnrealizedGainLoss | unrealized | YES | Tax Lot (open) | Units, Cost Basis, Amortization, MV, ST/LT G/L, Accrual |
| 5 | Allocation | allocations | YES | Account (allocation rollup) | Market Value (Child Facts) |
| **6** | **BI Billing** | -- | **NO (the gap)** | **Account x Month** | **BMV, EMV, Additions, Withdrawals, Net Additions/Flows incl/excl Fees, Contributions, Withdrawals, `Fees`, Net Gain, Income, New Accounts** |

Query types 1-5 (Snapshot/Transactions/Realized/Unrealized/Allocation) carry billing-labeled DIMENSIONS only (fee-schedule rate, discount %, config names) -- descriptive config, never a charge (confirmed by Andrew building a "Billing Snapshot" template on qt1 selecting every billing-labeled field available; qt1's entire fact catalog is `{Market Value, Accrual, Units, Unaccrued Market Value}`, zero fee-charge measures -- same story for qt2-5, see the table above). **qt6 "BI Billing" is different: it has a genuine `Fees` measure (id 55, `mappedColumn: biFees`, `sourceColumn: fees`)** at Account x Month grain, alongside flow-reconciliation measures (Net Additions incl/excl Fees, Net Flows incl/excl Fees) -- this is the real fee-CHARGE surface, and it lives inside DataMining after all.

### 3.2 Why the first-pass "no billing query type exists" verdict was wrong

The v0.2 draft of this doc concluded the DataMining hunt was closed based on the template-roster HISTORY showing only 5 query types ever used. That was a real methodological gap, not a re-guess: **qt6 had never been used on this account before Andrew built it live on 2026-07-08**, so it was invisible to a roster built from PAST templates. The roster endpoint answers "what has been queried," not "what query types exist" -- those are different questions, and conflating them produced a false-negative. Lesson for future sweeps: a template-history roster is a floor on the real catalog, never a ceiling; a query type with zero historical usage requires either a UI walkthrough (as Andrew did) or a true catalog/spec endpoint (BD has none published, sec.5) to discover.

### 3.3 CONFIRMED: the real charge magnitude (grounded on a live query + export, 2026-07-08)

Built a probe template (queryTypeId=6, `Custom` dateRangeType 05/09/2026-07/08/2026, dims: Return Date/Month/Year/Account Number/AccountID/Account Name, fact: `Fees`), created it (`templateId 242684`), ran it (`runId 242685`, completed), and downloaded the export (`Api/DataMining/ExportResults`, 87,676 bytes, 2,188 rows) -- all off-box, from Andrew's local machine, using the existing session (per the sec.2 correction).

| Return Date (period-end) | Account-months | Nonzero-fee rows | Fee total |
|---|---|---|---|
| 05/29/2026 | 596 | 0 | $0.00 |
| 06/30/2026 | 789 | 60 | $2,293.34 |
| **07/31/2026** | 803 | **558** | **$1,004,328.78** |
| **TOTAL** | 2,188 | 618 | **$1,006,622.12** |

**This is the concrete answer to Christa's "Mgmt fees hit Black Diamond today":** a quarterly fee-billing run posted for the period ending 07/31/2026, hitting 558 of 806 distinct accounts (a small June-only subset of 60 accounts is on a different/monthly cycle), totaling **$1,006,622.12**. BD dates the charge to the period-END (07/31/2026) even though it posted today (07-08) -- consistent with a forward-dated quarterly accrual/billing convention, not a data anomaly. Sample rows (account/date/amount) are in the commit history of this doc's authoring session; the full 2,188-row export was not persisted (ephemeral local probe, per the read-only-probe scope) -- re-running the same template (`templateId 242684`, left persisted on the BD account, same as Andrew's own test templates) reproduces it exactly.

## 4. A-la-carte querying (the tool)

`data/black_diamond/API/tools/bd_endpoint_sweep.py` -- run from anywhere with a valid session (off-box OK, see sec.2 correction):

```
python3 bd_endpoint_sweep.py                    # full catalog pass (spec-hunt + querytypes + sweep + billing)
python3 bd_endpoint_sweep.py --billing          # find + dump the billing query-type catalog (no run)
python3 bd_endpoint_sweep.py --probe /datamining/request/v1/querytype   # GET any endpoint, dump the payload
```

Output -> `s3://opal-data-cot/code/bronze/endpoint_catalog/` (`endpoint_sweep_result.json`, `querytype_catalog.json`, `billing_catalog.json`, `probe/{path}.json`). The `--probe` primitive is the athletic ad-hoc query: hit any BD path, capture the payload -- no template, no ETL.

## 5. Completeness basis -- D4 method, and where it actually landed

Per the D4 discipline (basis (a) spec-proven vs basis (b) observed/probed): the BD REST surface has **no known published spec** (a swagger/openapi spec-hunt confirms this -- only OIDC discovery is published, auth-only). So this catalog is **basis (b) -- observed + actively probed**, same as D4's SmartX catalog. The numeric-id sweep tool (`bd_endpoint_sweep.py`, sec.4) tests this basis mechanically but has a real blind spot the resolution (sec.3.2) exposed: a query type's DIMENSIONS/FACTS only surface once something has actually queried it, so a pure catalog sweep of ids 1..25 undercounts -- it found nothing at qt6 because nothing in the tool's guessed URL patterns matched BD's real `Query/DimensionsFacts` (POST, body `{queryTypeId}`) shape. **The reliable discovery path turned out to be the live BD UI itself** (Andrew building test templates + a HAR capture of the resulting network calls), not blind endpoint guessing -- worth folding into the tool as a documented limitation, not a tool rewrite (sec.4's `--probe` primitive already covers the "hit one endpoint, dump payload" case; it just needs the right path, which the UI/HAR method supplies).

**Still open, lower priority now that the billing question is answered:** the D2 sec.7 qt1/holdings enriched-template dump (never run) -- fold into a future on-box or off-box pass if useful; not gating anything.

## 6. A SECOND, SEPARATE billing surface exists too (`billing.bdreporting.com`) -- real, but NOT needed for the Christa answer

**Superseded by sec.3.3:** this section documents a genuinely separate BD federated app that is real and worth knowing about, but qt6 "BI Billing" (found afterward, sec.3.2/3.3) already answers the fee-charge question directly through DataMining -- no role grant or second app needed. Keeping this section because the AR/Accounts-Receivable surface below may still be useful for reconciliation/outstanding-invoice use cases DataMining's qt6 doesn't cover (qt6 gives posted fee amounts; AR's `unreconciled`/`outstanding` endpoints likely cover collection status, a different question).

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

**Status:** parked, not blocking. If a future need requires collection/reconciliation status (vs. the posted-charge amount qt6 already gives), revisit closing AR access (role grant or a HAR of the live Billing UI) then.

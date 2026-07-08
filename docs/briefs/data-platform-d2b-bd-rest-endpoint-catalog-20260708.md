# DATA_PLATFORM D2b -- Black Diamond REST Endpoint + Payload Catalog

**Status:** v0.1 DRAFT (skeleton) -- KNOWN endpoints grounded; the full surface is **PENDING the on-box exhaustion sweep** (see sec.5). CTO arch-gate + CVO reconcile pending the sweep result.
**TO:** `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/DATA_PLATFORM.D2b.bd-rest-endpoint-catalog.md`
**Author:** 0.4.0_DS_ClientPlatform (Andrew-direct 2026-07-08). **Consult:** 0.7.0_AE_CloudOps (on-box). **Verify:** 3.0.0_SA_CVO.
**Sibling of:** `DATA_PLATFORM_D2_BLACK_DIAMOND_ARCH_SPEC.md` (the DataMining model) + `DATA_PLATFORM_D4_smartx_endpoint_sweep.md` (the endpoint-sweep pattern this applies to BD).
**Tool:** `data/cot/scripts/bronze/bd_endpoint_sweep.py` (the a-la-carte query harness + sweep engine).

> **Purpose (Andrew-direct 2026-07-08):** a **dedicated catalog of every BD REST endpoint + its payload**, so we can query the BD database **a-la-carte, purpose-based, outside the scheduled ETL** -- instead of relying only on the 5 fixed view-pulls. D2 documented the DataMining *flow* for the 5 query types cot ingests; it never swept the full surface. This is the "D4-for-BD" catalog.

---

## 1. Origin

Christa Bass (Financial Advisor, Cottonwood) emailed Andrew 2026-07-08: *"Mgmt fees hit Black Diamond today!"* A DS probe (COO GO, Andrew-direct) ground-truthed the cot bronze: the management-fee **CHARGES are absent** from every partition. cot ingests only qt1-5 (holdings/transactions/realized/unrealized/allocations); **none is a billing query type.** The billing fields we *do* carry (allocations/realized/unrealized) are billing **CONFIG** (fee-schedule rates, discount %, billing-config names) -- the *rate a client would be billed*, not the fee *charged*. Transactions' only fee-shaped rows are custodian ADR/expense/debit-card items (`Transaction Fee`/`Account Fee` = 0). So the mgmt-fee charges post into a BD **Billing** surface we do not query -- which is exactly why the Cottonwood Books tab renders `fee_earning_aua` / `implied_revenue` / `distribution` = 0. Closing that gap **starts** with cataloging the surface (this doc) -> finding the billing query type -> wiring it in (a follow-on build TO).

## 2. Auth model (grounded -- D2 sec.3)

Two-credential split; the BD session is **IP-bound to the cot-exporter EC2** (`i-0643a5bee8a8feabf`) -- every live read runs on-box via SSM. Effective session TTL ~30-60 min -> a fresh `opal-cot-bd-session-fetch` precedes any sweep.

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

### 3.1 Query types (the table families) -- KNOWN qt1-5; the rest PENDING the sweep

| queryTypeId | Table | Ingested? | Leaf grain | Key measures |
|---|---|---|---|---|
| 1 | holdings | YES | Account x Holding (snapshot) | Market Value, Units |
| 2 | transactions | YES | Transaction | Units, MV, Transaction Fee, Income, Account Fee |
| 3 | realized | YES | Tax Lot (closed) | Cost Basis, Proceeds, ST/LT G/L |
| 4 | unrealized | YES | Tax Lot (open) | Cost Basis, MV, ST/LT G/L |
| 5 | allocations | YES | Account (allocation rollup) | Market Value |
| **6..N** | **PENDING** -- incl. the expected **BILLING** (mgmt-fee charges) | **NO** | -- | **the sweep enumerates these** |

> **The billing gap in one line:** BD DataMining almost certainly exposes a **Billing** query type (qt >= 6) carrying the actual fee *charges* -- but it is not one of our 5 configured tables, so it never enters cot bronze. The sweep (sec.5) confirms its id + catalog; a follow-on build TO wires it in.

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

**On completion:** fill sec.3.1 (the full query-type roster) + a per-endpoint payload table + the billing-charge finding; then CTO arch-gate + CVO reconcile -> v1.0. Fold in the still-un-run D2 sec.7 enriched-template dump (same on-box window).

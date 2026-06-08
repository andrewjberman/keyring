# COT (Cottonwood) — 49F BD Table ↔ DataMining Endpoint Cross-Reference (interim)

**Author:** 0.4.0_DS_ClientPlatform · **Date:** 2026-06-08 · **Project:** ADVI_COTETL
**Status:** COMPLETE — all 5 BD query types empirically confirmed. qt=2 from HAR-1; qt=1/3/4/5 from HAR-2 (`bd3.bdreporting.com2.har`, Andrew-captured 2026-06-08, incl. his `CW_Allocation` template build).
**Companions:** Brief 1 (DataMining API contract), Brief 3 (medallion port).

---

## 0. The reframe (Andrew, 2026-06-08)

API access means **we define the tables** — COT bronze is not bound to the field selection in the `CW_Transactions_Rich` CSV. Every 49F BD-sourced table is reproducible by issuing the right DataMining query (queryTypeId + dimension/fact selection) against the **same** endpoint contract (Brief 1): `auth/token → POST v1/run{template} → poll status → ExportResults/{resultGuid}`. **Only the `queryTypeId` and the selected dimensions/facts change per table.**

---

## 1. What 49F actually secures from BD (the source-of-truth list)

From the bronze/silver scripts, 49F lands exactly **5 BD-sourced tables** via the `forwardfill_v2/*` prefix (each a BD DataMining export → silver):

| 49F BD table | Source prefix | Silver | DataMining query type | Identifying signature |
|---|---|---|---|---|
| **Transactions** | `forwardfill_v2/transactions` | `silver/transactions` | **qt = 2** (Transactions) | 63-dim Transactions/Rel/Portfolio/Account/Holding template (HAR-1) |
| **Allocations / AUA** | `forwardfill_v2/allocations` | `silver/allocations` | **qt = 5** (Allocation) | **Andrew's `CW_Allocation` template #225472** — Market Value snapshot, CurrentDay; allocation hierarchy (Portfolio Group → Relationship → Portfolio → Account → …) |
| **Realized Gain/Loss** | `forwardfill_v2/realized` | `silver/realized` | **qt = 3** (Realized G/L) | **Tax Lot** level + measures **Proceeds, Short/Long-Term Gain, Disallowed Loss** (closed lots) |
| **Unrealized Gain/Loss** | `forwardfill_v2/unrealized` | `silver/unrealized` | **qt = 4** (Unrealized G/L) | **Tax Lot** level + measures **Unaccrued Market Value, Unaccrued Short/Long-Term Gain, Cost Basis** (open lots) |
| **Assets / Securities dim** | `forwardfill_v2/assets` | `silver/bd_assets_dim` | **Holding-level projection** (no separate query type) | Asset attributes (name/ticker/CUSIP/SEC asset type/coupon/expense ratio/etc.) are the **Holding** level dimensions present in qt=1/2/4; extract from the Holdings (qt=1) query |
| _(bonus)_ **Holdings/Positions** | — | (positions snapshot) | **qt = 1** (Holdings) | Team/Rel/Portfolio Group/Portfolio/Account/Classification/Holding + measures **Market Value, Accrual, Units, Unaccrued MV** |

**NOT from BD (do not need a DataMining query):**
- `silver/prices`, `silver/historical_prices`, `silver/interpolated_prices` — public market data (yfinance/yahoo).
- `silver/rps`, `silver/uln`, `silver/trn`, `silver/acc` — **Schwab custodian** data (OneDrive sync, `convert_schwab_*`). COT is 98.8% Fidelity IWS → **COT almost certainly needs none of the Schwab path** (confirm, but likely drop).

## 2. How each BD table feeds the gold layer (why we need all 5)

| BD table | Gold consumption |
|---|---|
| Transactions (qt=2) | A_00 accounts_dim (primary), A_03 positions cube (units + flows), C_01 NNA (inflow/outflow classification) |
| Allocations (qt=1) | A_00 enrichment (account_type/registration), AUA market-value snapshot + cross-validation of positions×prices |
| Unrealized (qt=?) | `gold/canonical/lots_unrealized` → B_* holdings/lots, C_05 tax liability (unrealized gain/loss) |
| Realized (qt=?) | `silver/realized` → `gold/canonical/account_gains` (B_03), C_05 tax liability (realized gains) |
| Assets (qt=?) | `silver/bd_assets_dim` → B_01b security classification, asset attributes (CUSIP/ticker/asset-type/coupon/etc.) |

So the full 49F gold pipeline needs **all 5** BD tables. The COT bronze must reproduce all 5 query types — not just transactions+allocations as Brief 3 §5 initially scoped (correction folded here).

## 3. What's confirmed vs. what the fresh HAR pins

**All confirmed (HAR-1 + HAR-2):**
- The **endpoint contract is identical for all query types** (Brief 1) — `v1/run` takes a template with any `queryTypeId` + dimension/fact selection; results export the same way.
- **qt=1 Holdings · qt=2 Transactions · qt=3 Realized G/L · qt=4 Unrealized G/L · qt=5 Allocation** — all pinned via DimensionsFacts measure signatures (HAR-2 carries qt=1/3/4/5 catalogs; qt=2 from HAR-1's template).
- **Assets/Securities** is the **Holding-level dimension set** (asset attributes), not a distinct query type — extract from the Holdings (qt=1) query's Holding level.
- The `GET /datamining/request/v1/build/querytype` catalog body is still empty in both HARs, but it's **no longer needed** — the per-domain DimensionsFacts probes pinned every ID + its full field catalog directly.

## 4. Capture guidance for the fresh HAR (maximally useful)

To pin the remaining 3 (and lock the whole catalog), capture a BD DataMining session that does any of these (in priority order):

1. **Best single call:** open `GET /datamining/request/v1/build/querytype` with a populated response body — this is the full `queryTypeId → name` catalog (Transactions, Holdings, Realized G/L, Unrealized G/L, Assets, Performance, Income, …).
2. **Per-domain DimensionsFacts:** in the "new query/template" UI, select each query type — **Realized Gain/Loss, Unrealized Gain/Loss, Holdings/Allocation, and Assets/Securities**. Each selection fires `POST /datamining/request/Query/DimensionsFacts {"queryTypeId":N}` whose response is that domain's full dimension+fact catalog. Capturing those 3–4 calls pins the IDs **and** the selectable fields in one pass.
3. **(Optional, gold-plated) build + export one tiny template per domain** (a few rows, narrow date window) — gives the exact `v1/run` body shape + a sample export per table to validate the parser against, same as `CW_Transactions_Rich` did for Transactions.

Any of 1–2 is sufficient to complete this cross-reference; (3) additionally de-risks the bronze parser per table.

## 5. Bottom line

**Fully mapped.** 49F secures 5 BD tables via one DataMining endpoint, distinguished only by `queryTypeId` + field selection: **Transactions (qt=2), Allocation (qt=5), Realized G/L (qt=3), Unrealized G/L (qt=4)**, with **Holdings (qt=1)** as the positions/AUA snapshot and the **Assets/Securities** dimension as a Holding-level projection. Andrew's HAR-2 capture (incl. his `CW_Allocation` qt=5 template) pinned every remaining ID. COT bronze can now reproduce all 5 tables — each is one `v1/run` template (queryTypeId + dimension/fact selection) → `ExportResults`. Next: select the dimension/fact set per table to match each 49F silver schema (the per-table template bodies — straightforward from these catalogs), wired behind the P0 auth infra. Schwab custodian tables are not BD and are N/A for COT (98.8% Fidelity).

# Brief: Inflection — SILVER layer (end-to-end audit)

**Author:** 3.0.0_SA_CVO (Andrew-direct, ADVI_BREAKS unified-flow audit) | **Date:** 2026-06-30
**Scope:** Inflection silver only. Bronze = `inflection-bronze`; Gold+portal = `inflection-gold`.
**Rule 17:** silver = dedup + dtype standardization ONLY (no field slimming, no business fillna/dropna/filter). Compliance noted in §4.

---

## 1. The silver step set the daily chain actually runs (`CHAIN_FULL`)

| Chain step | Script | → output |
|---|---|---|
| INF_API_SILVER_REPS | `convert_orion_api_to_silver.py --dim representatives` | `silver/api_dims/representatives/snapshot_date={date}/data.parquet` |
| INF_API_SILVER_HHREP | `convert_orion_api_to_silver.py --dim household_rep_mapping` | `silver/api_dims/household_rep_mapping/snapshot_date={date}/` |
| INF_API_SILVER_ACCOUNTS_V2 | `convert_orion_api_to_silver.py --dim accounts_v2` | `silver/api_dims/accounts_v2/snapshot_date={date}/` |
| INF_API_SILVER_POSITIONS_MV | `convert_orion_api_to_silver.py --dim positions_mv` | `silver/api_dims/positions_mv/snapshot_date={date}/data.parquet` ◄ AUA source |
| INF_API_SILVER_ASSETS_V2 | **`convert_assets_v2_to_silver.py`** (own) | `silver/assets_v2/{date}.parquet` |
| INF_API_SILVER_TXN | **`convert_transactions_to_silver.py`** (own) | `silver/transactions/{date}.parquet` |
| INF_API_SILVER_PERF | **`convert_performance_to_silver.py`** (own) | `silver/performance/{date}.parquet` |
| INF_S_00 | `INF_build_canonical_prices.py` | `silver/prices/canonical_prices.parquet` |

`tax` + `billing` silver: built by `build_tax_dim.py` / `build_billing_dim.py` (separate builders), not in the chain's silver block — gold reads them / they run out-of-band.

## 2. Layout variance (3 patterns, same disease as bronze)

```
 PATTERN A — partitioned (canonical):  silver/api_dims/{dim}/snapshot_date={date}/data.parquet
   household, performance*, activity, billing*, representatives, household_rep_mapping,
   accounts_v2, positions_mv        (the convert_orion_api_to_silver DIM_BUILDERS set)
 PATTERN B — flat own-prefix:          silver/{dim}/{date}.parquet
   assets_v2, transactions, performance     (the standalone converters the chain uses)
 PATTERN C — single-file:              silver/prices/canonical_prices.parquet  (prices)
```
Note the **positions_mv flip**: it is NON-standard in bronze (`bronze/positions/{date}.parquet`) but **canonical in silver** (`silver/api_dims/positions_mv/snapshot_date={date}/`). `assets` is non-standard in BOTH (`bronze/assets` + `silver/assets_v2`).

## 3. Converter divergence (worse than bronze — duplicate converters)

`convert_orion_api_to_silver.py` is a **unified** converter (DIM_BUILDERS registry, line 936): `household, performance, activity, billing, representatives, household_rep_mapping, positions_mv, transactions`. BUT the daily chain does NOT use it for `transactions` or `performance` — it uses standalone scripts instead:

| Dim | Unified converter has a builder? | Standalone script? | Chain uses |
|---|---|---|---|
| transactions | YES (`build_transactions`, L945/992) | YES (`convert_transactions_to_silver.py`, 1 of 2) | **standalone** |
| performance | YES (`build_performance`) | YES (`convert_performance_to_silver.py`) | **standalone** |
| assets_v2 | (no — assets handled separately) | YES (`convert_assets_v2_to_silver.py`) | standalone |
| reps/hhrep/accounts_v2/positions_mv | YES | — | **unified** |

Plus `convert_orion_to_silver.py` (a THIRD, older converter — likely legacy/dead, confirm) and 3 `build_{assets,billing,tax}_dim.py` builders. So a single dim (`transactions`, `performance`) has **two live converter implementations**, mirroring the bronze `_v2/_dim` ↔ `_rest` pull-script fork.

## 4. Rule 17 compliance (good — keep on the rewrite)

`convert_transactions_to_silver.py` documents Rule 17 explicitly (header L3–72): dedup + dtype standardization + mechanical provenance only; no field slimming; no business derivations; no business-default fillna/dropna. One permitted metadata addition: `.fillna("Unknown")` on a `trans_type_desc` dict-miss (declared as a label join, not a business default). The standalone converters are Rule-17-aware — a unification rewrite must preserve this (the failure Rule 17 prevents: ADVI_DWSPLT, Andrew 2026-05-13).

## 5. Silver variance inventory (what the unified flow must eliminate)

| Axis | Today | Unified target |
|---|---|---|
| **Output layout** | A: `api_dims/{dim}/snapshot_date={date}/` ; B: flat `silver/{dim}/{date}.parquet` ; C: single-file prices | 1 partitioned pattern `silver/api_dims/{dim}/snapshot_date={date}/data.parquet` for ALL dims |
| **Converter per dim** | unified converter for 4 dims; standalone for 3 (assets_v2/txn/perf); `transactions`+`performance` have BOTH; legacy `convert_orion_to_silver.py`; 3 `build_*_dim` builders | 1 converter path per dim (fold standalone into the unified DIM_BUILDERS or vice-versa; retire the duplicates + legacy) |
| **positions_mv** | special in bronze, canonical in silver (inconsistent across layers) | uniform end-to-end |
| **Rule 17** | compliant (preserve) | preserve dedup+dtype-only contract |

## 6. Tie to the unified flow

Silver shows the **same structural variance as bronze**, one layer deeper: a unified converter that was meant to own all dims, but with `transactions`/`performance`/`assets_v2` forked off into standalone scripts and a flat output layout, plus duplicate + legacy converters. The unified-flow rewrite collapses this to: **one converter dispatch (DIM_BUILDERS-style) → one partitioned `silver/api_dims/{dim}/snapshot_date={date}/` layout for every dim → Rule-17-preserved**. positions_mv is already at the canonical silver layout, so it is the template; assets_v2/transactions/performance are the ones to normalize.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| grep/read on data/inf/scripts/silver + orion-gold-dispatch.sh | converter-per-dim, output layout, DIM_BUILDERS, Rule-17 headers | PASS (rail-checked) |
| (live S3 silver freshness) | covered in inflection-bronze §3 baseline | — |

— 3.0.0_SA_CVO

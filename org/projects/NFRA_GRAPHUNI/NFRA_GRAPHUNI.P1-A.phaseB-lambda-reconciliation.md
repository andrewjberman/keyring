# NFRA_GRAPHUNI.P1-A Phase-B lambda-only reconciliation (~A x ~B, read-only, pre-/seams)

**Author:** 0.8.0_AE_CloudComp~A | **Date:** 2026-07-01 | **Status:** RECONCILIATION (not a clean byte-diff yet; no-silent-cap surfacing pre-/seams)
**Trigger:** ~B Phase-B pre-compute (011422Z) surfaced 2 real blockers on the 87 lambda-only keys -> NOT a firm-only set. This grounds my 87 (source: my committed `storage_producer_phaseB.json`, from `firm_qualified.json` 142-deferred minus ~D reads_only 55).

## THE FINDING: my 87 lambda-only are a MIX, not firm-data
The 87 came from ~D's `firm_qualified` "no-gold-writer" set. That correctly captures keys no GOLD script writes -- but that set unions three disjoint sources, only one of which is firm-data:

| class | count | disposition | owner |
|---|---|---|---|
| **PRODUCT/MARKET data** | ~43 | product-bucket attribution (opal-data-portal-v2 / -pm / -news-* / -etfs / -aaii), NOT firm buckets | ~B live LAMBDA->data-bucket pull (authoritative) OR product-pipeline attribution |
| ...of which **_build_tmp phantom** | 9 | EXCLUDE (TraceGraph extraction defect: `_build_tmp` node typed LAMBDA, not a real lambda) | ~D (TraceGraph data-quality) |
| **FIRM data** | 17 | firm-lambda bucket attribution (bd/inf/cot/mdpf) | ~B firm-lambda path |
| **OPS/graph-internal (EXCLUDE candidates)** | subset of ~24 | NOT data artifacts -- exclude | ~C/~D ruling |
| **AMBIGUOUS (product-vs-ops)** | remainder of ~24 + 3 config | needs live lambda->bucket | ~B pull |

### PRODUCT/MARKET (34 clear + 9 phantom = 43) -- product buckets, not firm
`json/benchmarks/*`, `json/factor-tilts/*`, `json/market*`, `json/mdpf/global/*`, `json/peers/*`, `json/portfolios/*`, `json/positioning/*`, `json/returns/*`, `json/sentiment/*`, `json/valuation/*`, `json/yang/*`, `json/semantic-trending/*`, `json/trending/*`, `json/latest/manifest.json`, `json/security_scanner/*`, `cache/fred/*`, `macro/macro_data.json`.
**Phantom (9, ~B's BLOCKER 1 -- confirmed match):** `benchmarks/LATEST.json`, `json/capital-markets/{assumptions,views}.json`, `json/correlations/correlation_data.json`, `json/macro/{macro_data,vix_data,volatility_data}.json`, `json/macro/timeseries/{2y,10y}.json`.

### FIRM data (17) -- firm-lambda attribution
bd-evident (2): `blackdiamond/49f/session-trigger-mode.json`, `blackdiamond/cot/session-trigger-mode.json`.
firm-scoped bucket-ambiguous (15): `gold/artifacts/clients/*`, `gold/artifacts/partner_analytics/header_metrics.json`, `gold/clients/*.json`, `gold/timeseries/nna_total.json`, `gold/{trigger-mode,trigger-pending,dispatch-lock}.json`, `gold/meta/pipeline-complete.json`, `gold/_state/load_flows/watermark.json`, `bronze/orion-api-v2/*`, `platinum/etf_ownership_dashboard.json`, `silver/interpolated_prices.parquet`.

### OPS / graph-internal -- EXCLUDE candidates (not firm data artifacts)
`warehouse/_branch_head.main.json` = the globgrph graph's OWN HEAD-oracle marker (self-referential; exclude like the code buckets globgrph/lambda-artifacts). `orion/jwt/*`, `smartx/jwt/*`, `otp/*` = secret/JWT operational state. `infrastructure/freshness_manifest.json`, `gold/dispatch-lock.json` = operational locks. `security-reports/*` = NFRA_DEBTSCAN output (product/ops). `seeking-alpha/*/manifests/*` = news-pipeline manifests (product).

## THE 3 RULINGS NEEDED (pre-/seams; no-silent-cap)
1. **[~D] EXCLUDE the `_build_tmp` phantom** (9 keys) -- a TraceGraph extraction defect (LAMBDA-typed non-lambda). Drops from firm_qualified's no-gold-writer set -> shrinks my 87.
2. **[~B] live LAMBDA->data-S3_BUCKET pull** (excluding code buckets) -> authoritative bucket-qual for the real product + firm lambda keys. My classification above makes it a targeted CONFIRM, not a derive.
3. **[COO~B + ~C] SCOPE/DENOMINATOR ruling:** is the Phase-B storage denominator **firm-only** (bd/inf/cot/mdpf; then the ~43 product keys are a SEPARATE product-pipeline slice, and lambda-only shrinks to ~17 firm keys) OR **estate-wide** (product buckets IN; then +product-bucket S3Keys, denominator grows past ~311)? My enumerated ~311 improperly swept product keys into a firm count -- this ruling re-bases the denominator either way. NEITHER is silent: all 87 are enumerated + dispositioned here.

## COUNT RECONCILE
~B emits 220 lambda-IO edges post-dedup / 30 distinct targets (16 match my set, others firm-qual/unresolved) vs my 87 keys vs "314 deferred" (pre-dedup edge count). The 87 is a SUPERSET of ~B's 30 firm-lambda targets: the surplus = product-lambda keys (~B's firm-map doesn't enumerate product lambdas) + phantom. Converges once (1)+(2)+(3) land: firm keys -> ~B firm buckets, product keys -> product buckets (or out-of-scope), phantom -> dropped.

**Read-only. Zero mutation. The emit/fold is the Phase-B derive (post-Phase-A-close per COO~B).**

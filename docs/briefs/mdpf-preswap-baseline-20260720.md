# MDPF pre-swap BASELINE — the fixed parity target (comprehensive current-numbers capture)

**Author:** 1.0.0_SA_CTO · **Date:** 2026-07-20 · **Andrew-direct:** "before swapping… actually spot check the numbers from what is in there currently… we have to be very very comprehensive."

**Provenance:** the CURRENT served artifacts (`opal-data-portal-v2/json/…`), generated **2026-07-20 ~11:30Z** off data period **2026-07-18**, still fed by the **LEGACY** feed (`opal-data-mdpf/mdpf/feeds/model_aua_positions/{firm}/2026-07-18.parquet`) + the mdpf gold + the DDB `opal-assets-daily-aua`. This is the number set the revamp's gold `dim_*` projections must reproduce (parity streak N=3) BEFORE any re-point. Nothing sampled — every model, every level.

---

## 1. DAILY START / END POINTS (the timeseries range) — identical across all firms

| | value |
|---|---|
| as_of_first / dates[0] | **2024-11-01** |
| as_of_last / dates[-1] | **2026-07-18** |
| n_dates | **429** |
| non_model_assets time_series | len 455, 2024-11-01 → 2026-07-18 |

(as_of 2026-07-18 on a 2026-07-20 generation = within the T-1 trading frontier; not stale.)

## 2. LATEST AGGREGATE + BY-MODEL RADIAL (per firm, as-of 2026-07-18)

### GLOBAL
- **model_aua $1,534,471,753.80** · non_model_aua **$312,170,328.70** · opal_aggregate_aua **$1,782,163,983.16**
- by_model (9): UST $45.66M/180 · ST $112.39M/716 · INT $368.00M/1807 · **LTC(disp "Long Term") $765.47M/3295** · **LTA(disp "Ultra-Long Term") $204.09M/1419** · div_sma(sma) $18.84M/40 · growth_sma(sma) $4.62M/45 · blend_5050_int_ltc $31.59M/158 · blend_5050_st_int $7.28M/24 → **sum $1,557.94M** (= model_aua + SMAs $23.46M)

### 49 FINANCIAL
- **model_aua $1,397,301,724.98** (= the SCHWAB-RPS 5-core, exact) · non_model_aua **$247,692,229.36** · partner_custody_total **$1,644,993,954.34**
- by_model (7): UST $44.74M/170 · ST $106.74M/691 · INT $292.20M/1599 · LTC $751.80M/3205 · LTA $201.83M/1388 · div_sma $18.84M/40 · growth_sma $4.62M/45 → **sum $1,420.77M** (= 5-core $1,397.30M + SMAs $23.46M)

### INFLECTION
- **model_aua $137,170,028.82** · non_model_aua **$64,478,099.34** · partner_custody_total **$201,648,128.16**
- by_model (7): INT $75.80M/208 · blend_5050_int_ltc $31.59M/158 · LTC $13.67M/90 · blend_5050_st_int $7.28M/24 · ST $5.65M/25 · LTA $2.26M/31 · UST $0.92M/10 → **sum $137.17M** (= model_aua; no SMAs; carries the 2 blend cohorts)

## 3. ACCOUNT DISTRIBUTIONS + COUNTS (per firm, period 2026-07-18)

| firm | total acct_count | total_aum | mean | median | p10 | p25 | p50 | p75 | p90 | min | max | std |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **global** | **7553** | $1,534,450,951 | $203,158 | $70,213 | $7,907 | $23,111 | $70,213 | $192,128 | $445,903 | $1,002 | $33,731,055 | $644,122 |
| **49financial** | **7019** | $1,397,281,888 | $199,071 | $67,794 | $7,454 | $22,160 | $67,794 | $186,980 | $427,553 | $1,002 | $33,731,055 | $658,890 |
| **inflection** | **534** | $137,169,063 | $256,871 | $106,938 | $15,914 | $39,240 | $106,938 | $282,998 | $703,705 | $1,110 | $3,125,361 | $398,985 |

Each firm's histogram = 20 bins; by_model account_count sums TIE the total (global 7553, 49F 7019, inflection 534).

**Per-model distribution counts (account_count):**
- **global** (7): UST 178 · ST 712 · INT 1798 · LTC 3267 · LTA 1419 · blend_int_ltc 155 · blend_st_int 24
- **49financial** (5): UST 168 · ST 687 · INT 1598 · LT 3178 · ULT 1388
- **inflection** (7): UST 10 · ST 25 · INT 200 · LT 89 · ULT 31 · blend_int_ltc 155 · blend_st_int 24

## 4. GLOBAL HEADER KPI (aum-metrics.json) + NON-MODEL (non_model_assets.json)
- aum-metrics: period 2026-07-18, **total aum $1,782,163,983 / account_count 7587**; quarter-ends q0 2026-06-30, q1 2026-03-31, q2 2025-12-31, q3 2025-09-30; by_model(7) UST 180 · ST 716 · INT 1800 · LTC 3293 · LTA 1419 · blend_int_ltc 155 · blend_st_int 24.
- non_model_assets latest 2026-07-18: enterprise_total $1,782,163,983 · model_aum $1,534,471,754 · **non_model_aum $247,692,229** · non_model_pct 13.90%.

## 5. INTERNAL CONSISTENCY — all PASS
- Global model_aua $1,534.47M = 49F $1,397.30M + Inflection $137.17M ✓ (exact)
- 49F 5-core $1,397.30M = the DDB `49f_smartx_platform` + the monolith silver roster 5-core (verified this session) ✓
- non_model_aua = custody − model per firm: 49F $247.69M = $1,644.99M − $1,397.30M ✓ · Inflection $64.48M = $201.65M − $137.17M ✓
- Global timeseries non_model_aua $312.17M = 49F $247.69M + Inflection $64.48M ✓ (firm-summed)
- by_model sums = model totals per firm ✓

## 6. PARITY TRAPS — the gold projection MUST reproduce these distinctions (do NOT normalize away)

1. **TWO account-count denominators.** aum-metrics global = **7587**; account-distribution global = **7553** (Δ34). The distribution counts FUNDED accounts (excludes unfunded); aum-metrics includes unfunded. The FE renders both + an unfunded footer. Preserve both denominators.
2. **TWO non-model numbers, both served.** A5 spine `non_model_aua` global = **$312.17M** (firm-summed custody−model); A4 `non_model_assets` global = **$247.69M** (enterprise_total − model, a DIFFERENT enterprise basis). They differ by ~$64.5M (= the inflection non_model). BOTH are served and must be reproduced distinctly — this is the CVO-flagged F3, now grounded. Never substitute one for the other.
3. **model_aua EXCLUDES SMAs; non_model INCLUDES them.** model_aua = the models only; the 2 SMAs (div $18.84M + growth $4.62M = $23.46M) fold into non_model. The platinum-daily shape keeps `sma_aua` distinct (F8) — don't cross shapes.
4. **Display-name divergence (the crosswalk):** served display "Long Term" = LTC = `opal_long_term_conservative`; "Ultra-Long Term" = LTA. Key by `model_id`, never the display string (F5).
5. **The current numbers come from the LEGACY feed** (`model_aua_positions`). The ~$4.1M roster-vs-legacy 5-core delta (F2: monolith roster $1,395–1,401M vs served $1,397.30M) is the named parity delta to ground at authoring.

## 7. THE PARITY BAR (per firm, at swap)
The new gold projection ties this baseline within tolerance for N=3 consecutive cycles; every named delta explained (the F2 ~$4.1M; any vintage move); the two count denominators + the two non-model numbers reproduced distinctly; then never-widen co-sign → re-point. Raw per-day dumps in the CTO scratchpad; this doc is the fixed reference.

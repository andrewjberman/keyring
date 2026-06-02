# MDPF account-distribution (donut) consistency check — DS 0.4.0_DS_ClientPlatform, 2026-06-02
COO optional interim item (the out-of-scope artifact I flagged): is the 6/01 donut stale vs the now-6/02 timeseries? within-MDPF FE consistency? Read-only.

## What it is
`json/mdpf/{firm}/account-distribution.json` = the FE donut/distribution artifact: a current-period account-SIZE histogram + percentiles + per-model (by_model) breakdown. SEPARATE producer from the rollup (`compute_per_firm_account_distribution.py`, SmartX/Eclipse source). Snapshot, NOT a timeseries. Scope = MODEL accounts (cohort 1a) — source is smartx_allocations (model only) / eclipse model_portfolio_accounts.

## Findings (both firms)
| firm | donut period / gen | donut total_aum | by_model sum==total | TS 1a latest (6/02) | donut-vs-TS-1a |
|---|---|---|---|---|---|
| 49financial | 202605 (May monthly) / 6/01 20:38Z | $1,379,701,688.62 | YES (to-the-cent) | $1,382,865,276.17 | −$3.16M (−0.23%) |
| inflection | 2026-05-29 (Eclipse daily) / 6/01 20:38Z | $96,601,199.67 | YES (to-the-cent) | $96,695,664.13 | −$94K (−0.10%) |

1. **INTERNALLY CONSISTENT** — by_model sum == total.total_aum to-the-cent, both firms.
2. **CROSS-CONSISTENT with the timeseries 1a** — donut total ≈ timeseries model_aua within <0.25%. The small deltas are the EXPECTED grain difference (donut = monthly[49f]/2026-05-29[inflection] snapshot; timeseries = daily through 6/02). Model AUA drifted ~$3.16M (49f, over the May→6/02 gap) / ~$94K (inflection, 3 days) — ordinary market movement, NOT a defect. Donut + trend chart tell a consistent FE story.
3. **FRESHNESS — not a stale-defect.** The donut is a MONTHLY (49f period 202605) / snapshot (inflection 2026-05-29) artifact by design; 6/01-generated is the current monthly snapshot (next: 202606 at June month-end / when June SmartX lands). It is NOT daily, so "6/01 vs 6/02 timeseries" is expected, not stale.

## Verdict
**CLEAN — no defect, no fix needed in my lane.** Donut data is correct (model-1a scope, internally consistent, matches timeseries 1a within grain tolerance). 
OBSERVATIONS (non-defect, for awareness, NOT my lane):
- The donut is MODEL(1a)-scoped; if any FE surface places the donut total next to the full headline AUA (1a+1b+1c+2a), label it as model-accounts to avoid an apparent mismatch (FE/RD presentation, not a data issue).
- A tighter producer cadence (June/daily donut) would shrink the <0.25% donut-vs-trend-endpoint gap, but that's a SmartX/Eclipse producer-cadence preference, not an MDPF-rollup correctness issue (separate lane).
Audit script `.runtmp/` (inline check). CC CTO + RD~B (FE-label observation).

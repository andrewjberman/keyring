# 0.4.0_DS_ClientPlatform — work_1920Z (I3 adv-view fix: built+deployed+comprehensive-verified; RAVC2-close filed)

**archetype:** IMPLEMENT + VALIDATE

## MDLP_DISTFIX I3 — adv-view bypass fix: BUILT + DEPLOYED + COMPREHENSIVELY VERIFIED

### Root cause (confirmed independently of AE's diagnosis)

The 18:48:39Z served `partner_analytics_monthly.json` had both `views.geo` AND `views.adv` in
the same object (same LastModified). `views.geo` was floored (p10=$11,729.60 ≥ $1K) —
`views.adv` was NOT (p10=$8.42, min=-$11.70). Code bug, not stale-publish. A re-run would
reproduce it deterministically.

`_build_adv_view` had TWO unfloored blocks that the first I3 pass missed:
- `by_segment` histogram block (L2464-2481): raw `.quantile()` on `adv_rows['aua']`
- `total_dist` block (L2483-2501): raw `.quantile()` on `acct_aua['aua']`

`_calc_distribution_stats_adv` (the donut-segment AUA summarizer) WAS floored — only the
two downstream histogram/percentile blocks escaped.

### Fix — geo-mirror pattern applied to both blocks

**Why geo-mirror, not AE's proposed `floor_series`:** `floor_series(acct_aua['aua'])` on L2483
reassigns `aua_series_total` to the >=$1K-filtered series. The next line
`'sum': aua_series_total.sum()` would then become the subset sum, diverging from:
- the adv donut total (computed via `_calc_distribution_stats_adv` on the full series)
- `views.geo.*.distribution.total.sum` (already sum=full)

This breaks the sum invariant. Geo-mirror preserves it:

```python
# by_segment — MDLP_DISTFIX I3 adv-view bypass fix
aua_series = adv_rows['aua']
_seg_stats = floored_distribution_stats(aua_series.tolist(), _ADV_SUMMARY_NUM_BINS)
by_segment[adv] = {
    'count': int(adv_rows['account_id'].nunique()),
    'sum':   round(float(aua_series.sum()), 2),   # full-series sum preserved
    'mean':  _seg_stats['mean'],
    ...
}

# total_dist — MDLP_DISTFIX I3 adv-view bypass fix
aua_series_total = acct_aua['aua']   # NO reassignment -- sum stays full
_total_stats = floored_distribution_stats(aua_series_total.tolist(), _ADV_SUMMARY_NUM_BINS)
total_dist = {
    'count': int(acct_aua['account_id'].nunique()),   # 875 accounts, full
    'sum':   round(float(aua_series_total.sum()), 2), # full-series sum preserved
    'mean':  _total_stats['mean'],
    ...
}
```

### Commit + deploy

- **Commit:** `25154e161` (DS Rule-13 orion-gold lane; `.tools/safe-commit.sh`)
- **Gate:** ds-commit-gate exit 0 (py_compile + AST undefined-name + sync-guard-triple + ruff)
- **Pre-push hook auto-deploy (19:09:27Z):** `s3://opal-data-inf/code/gold/INF_D_04.client_portal_summary.py` byte-verified
- **AE republish (191506Z):** `inf-gold-layer-runner --single INF_D_04` + CF-invalidate
  `/api/scoped/advisor-intelligence/*` on EVTSA9VEHNZVH

### Comprehensive served-verify — ALL SURFACES PASS

Read `opal-data-inf/platinum/firm/partner_analytics_monthly.json` post-publish.
ALL 4 windows × 2 views (geo + adv) × total + by_segment independently verified.

**views.adv (was $8.42 dust):**
| window | min | p10 | p50 | p90 |
|--------|-----|-----|-----|-----|
| current | $1,052.42 | $11,729.60 | $106,531.29 | $733,522.72 |
| m1 | $1,052.42 | $11,760.09 | $105,930.89 | ~$725K |
| m2 | $1,052.42 | $11,849.57 | ~$106K | ~$726K |
| m3 | $1,052.42 | $10,951.73 | ~$104K | ~$720K |

ALL 4 windows: min ≥ $1K / p10 ≥ $1K (was $8.42). Sum = $206,082,063.00 preserved (full-series invariant).

**views.geo (unchanged — verify confirms no regression):**
- Identical min/p10/p50/p90 to adv: $1,052.42 / $11,729.60 / $106,531.29 / $733,522.72
- Sum = $206,082,063.00 (same firm, same population, same as-of)
- count = 293 (household grain label on account-basis distribution — confirmed deliberate, not under-count)

**adv.total_dist vs geo.total:**
- Both sum = $206,082,063.00 ✓
- Both p10 = $11,729.60 ✓ (identical percentiles = same 875 per-account population, same floor)

### Andrew-direct answers to COO (191525Z) — all 3 accepted (COO ACK 191625Z)

1. **ADV-FIX:** geo-mirror over the 2-line — correct; deployed (25154e161 / 19:09:27Z)
2. **COUNT-DISPARITY:** 7,341 (ALL model) / 7,334 (>0) / 7,301 (≥$1K); delta 40 = 7-at-$0 + 33-in-(0,$1K); methodology call Andrew's
3. **GEO-293:** household-grain label on account-basis distribution; NOT under-count; sum invariant holds ($206M across all 3 grains); base-DE confirms FE renders geo as household-grain

## I3 RAVC2-close filed to COO

Gate: adv p10 = $11,729.60 ≥ $1K ✓; sum = $206M preserved ✓; geo unchanged ✓; code + served
consistent. Remaining: Andrew-visual on the ADV panel (COO to loop Andrew / /frontend-dev).

## Standing / open obligations
- **I3 close:** Andrew-visual on ADV panel pending (COO loops Andrew); RAVC2-close filed to COO
- **I1+I2 close:** AE deploying in event-gated 11:30Z job; post-deploy served-verify (card $1.808B, donut $1.492B, total_aum≠$0) → RAVC2-close
- **R2 close:** next-day BucketSizeBytes trend read → RAVC2-close
- **GLDINC §5:** engages when 0.6.0_AE starts P0 CHECKPOINT

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| ds-commit-gate | INF_D_04.client_portal_summary.py | exit 0 |
| (S3 served read) | partner_analytics_monthly.json post-publish | ALL PASS: adv + geo, 4 windows, p10≥$1K, sum=$206M preserved |

work-cycle:0019

# Cache-Control EC2 Gold Scripts 09 and 10 — 0.6.0_AE_PartnerETL

**Date:** 2026-03-10
**Task Order:** ADVI_49FNV3.006.cache-control-ec2-gold-scripts.md
**Commit:** `5bed0dbf`

## Objective

Add `CacheControl='public, max-age=300, s-maxage=3600'` to the `put_object` calls in
EC2 gold scripts 09 and 10. These scripts write portal-consumed JSON files directly to
S3, bypassing the publisher Lambda, and had no Cache-Control header — the same browser
heuristic caching issue fixed for the publisher Lambdas in ADVI_49FNV3.005.

Files targeted:
- `09_generate_partner_analytics.py` → writes `gold/partner_analytics/header_metrics_{quarterly,monthly,annual}.json`
- `10_generate_advisor_rolling_flows.py` → writes `gold/advisor_rolling_flows.json`

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Edit script 09 `write_s3()` at line 1616 | Added `CacheControl='public, max-age=300, s-maxage=3600'` |
| 2 | Edit script 10 `write_s3()` at line 911 | Same change |
| 3 | Upload 09 to `s3://opal-data-bd/code/gold/` | `aws s3 cp` — 71.3 KiB |
| 4 | Upload 10 to `s3://opal-data-bd/code/gold/` | `aws s3 cp` — 40.7 KiB |
| 5 | Commit | `5bed0dbf` feat(bd-gold): add Cache-Control to EC2 gold scripts 09 and 10 |
| 6 | Start EC2 `i-01003b035d2988dfb` | Gold pipeline ran with updated scripts |
| 7 | Verify script 10 running via SSM | `python3 10_generate_advisor_rolling_flows.py --upload` at 18:06 UTC |
| 8 | EC2 stopped (pipeline complete) | Confirmed stopped |
| 9 | Verify all 4 S3 objects | CacheControl confirmed on all targets |
| 10 | CloudFront invalidation | `IBP92G3KSU9TRO8LMNOVNG533C` InProgress |
| 11 | Push | `5bed0dbf` confirmed on `origin/CLOUD` |

## Verification

```
gold/partner_analytics/header_metrics_quarterly.json: public, max-age=300, s-maxage=3600 | 2026-03-10 18:06:07 UTC
gold/partner_analytics/header_metrics_monthly.json:  public, max-age=300, s-maxage=3600 | 2026-03-10 18:06:25 UTC
gold/partner_analytics/header_metrics_annual.json:   public, max-age=300, s-maxage=3600 | 2026-03-10 18:06:43 UTC
gold/advisor_rolling_flows.json:                     public, max-age=300, s-maxage=3600 | 2026-03-10 18:07:28 UTC
```

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| S3 upload directly via `aws s3 cp` | EC2 deployment standard — repo → S3 → EC2 pulls. No Terraform involved for EC2 code. |
| Triggered full gold pipeline run | Needed to rewrite the 4 S3 objects with new header immediately. |
| No `safe-ec2-deploy.sh` required | These are data scripts uploaded to S3 code path, not EC2 service deploy scripts. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/gold/09_generate_partner_analytics.py` | Added `CacheControl=` to `write_s3` put_object | Yes — `5bed0dbf` |
| `data/black_diamond/scripts/gold/10_generate_advisor_rolling_flows.py` | Same | Yes — `5bed0dbf` |

---

## Blockers

None.

---

## Current State

> **Status:** COMPLETE
> **Active branch:** `CLOUD`

All S3 objects written by the gold pipeline (both publisher Lambdas and EC2 scripts 09/10)
now carry `Cache-Control: public, max-age=300, s-maxage=3600`. The full cache-control fix
for ADVI_49FNV3 is complete across all three writing paths:
- bd-portal-publisher Lambda (ADVI_49FNV3.005)
- bd-portal-advisor-publisher Lambda (ADVI_49FNV3.005)
- EC2 script 09 (this task order)
- EC2 script 10 (this task order)

---

## Next Steps

1. **[Andrew] Verify in portal** — hard refresh Advisor Intelligence page. DevTools Network
   tab should show `Cache-Control: public, max-age=300, s-maxage=3600` for
   `partner_analytics/header_metrics_quarterly.json` and `advisor_rolling_flows.json`.
   Portal should now display $1.62B AUA as of 2026-03-06.
2. No further cache-control work needed — all gold output paths are covered.

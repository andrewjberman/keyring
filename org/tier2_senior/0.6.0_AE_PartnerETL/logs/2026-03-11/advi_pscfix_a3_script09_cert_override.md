# ADVI_PSCFIX A3 — Script 09 Cert Override Deploy — 0.6.0_AE_PartnerETL

**Date:** 2026-03-11
**Start Time:** 23:45
**End Time:** 23:58

## Objective

Add `_load_aua_certification()` helper and current-period donut total override to
`09_generate_partner_analytics.py` per task order ADVI_PSCFIX.A3. When
`gold/aua_certification/{today}.json` exists, overrides `views.aua/geo/adv[current].donut.total`
with `certified_aua` in all three granularity JSONs (`header_metrics_quarterly/monthly/annual.json`).

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read task order, read 09 script (period loop ~line 1538) | Structure confirmed |
| 2 | Add `_load_aua_certification()` after `load_data()` (line 309) | Helper function inserted |
| 3 | Add `_s3 + cert = _load_aua_certification(...)` in `generate_header_metrics()` after `data_as_of` | Cert loaded once per granularity run |
| 4 | Add `is_current_period` flag + override block after adv view, before NNA view | Override wired in loop |
| 5 | Commit source | `f6fef305` feat(bd-pipeline): script 09 cert override |
| 6 | safe-ec2-deploy.sh bd-gold-layer-runner | 09 uploaded to s3://opal-data-bd/code/gold/ |
| 7 | EC2_MANIFEST.json updated | Manifest commit `cc798d4d` |
| 8 | Mark task order complete | ADVI_PSCFIX.A3 status=complete |

## Verification

S3 upload confirmed:
```
s3://opal-data-bd/code/gold/09_generate_partner_analytics.py  (73 KiB)
```

To spot-check current-period donut total after next pipeline run:
```bash
aws s3 cp s3://opal-data-bd/gold/partner_analytics/header_metrics_quarterly.json - \
  | python -c "import sys,json; d=json.load(sys.stdin); print(d['views']['aua']['current']['donut']['total'])"
# Expected: ~1599225407.0 (certified_aua) vs prior ~1604943633.0 (gold_aua)
```

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| `is_current_period = (ts == ref_date)` | `ref_date = client_perf['date'].max()` is the last perf snapshot — exactly the current in-progress period end date. Simplest and most direct flag. |
| Cert loaded once per `generate_header_metrics()` call | Function is called once per granularity (quarterly/monthly/annual). Cert is date-level so one load suffices for all periods in the call. |
| New `_s3` client created in `generate_header_metrics()` | `load_data()` has its own private s3 client; not accessible here. Cheap to create a second one for the cert fetch. |
| Override placed after adv view, before NNA view | Exact position specified in task order. NNA/CLA don't have a `donut.total` — only aua/geo/adv need the override. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/gold/09_generate_partner_analytics.py` | Added `_load_aua_certification()` + cert load + current-period override | Yes — `f6fef305` |
| `infra/aws/ec2/EC2_MANIFEST.json` | Deploy recorded by safe-ec2-deploy.sh | Yes — `cc798d4d` |
| `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_PSCFIX.A3.script09-cert-override.md` | status=complete | Yes (this commit) |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

`09_generate_partner_analytics.py` is live in S3 with the cert override. On the next nightly
gold run: 05d writes `gold/aua_certification/{date}.json`; then 09 loads it and applies
`certified_aua` (~1.599B) to all three granularity JSONs' current-period aua/geo/adv donut totals.
Historical period donut totals are untouched. Override is non-blocking — if no cert JSON exists,
09 falls back to gold-derived totals silently.

ADVI_PSCFIX Track A (pipeline) is now structurally complete:
- A1: 05d writes cert JSON daily (COMPLETE)
- A3: 09 overrides current-period donuts (COMPLETE)
- Pending: publisher Lambda override (DS + DT track, separate task orders)

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Confirm publisher Lambda cert override** — PRD Deliverables 2 & 3
   (bd-portal-publisher: timeseries NMNC/NMEC scaling + snapshot total_aua override).

2. **[0.6.0_AE_PartnerETL] Complete ADVI_49FNV3.008** — write 05c_validate_aua_vs_silver.py
   (still pending; wired in run_gold_layer.sh with file-existence guard).

3. **Verify on next pipeline run** — check quarterly donut total:
   ```bash
   aws s3 cp s3://opal-data-bd/gold/partner_analytics/header_metrics_quarterly.json - \
     | python -c "import sys,json; d=json.load(sys.stdin); print(d['views']['aua']['current']['donut']['total'])"
   ```

**Do NOT:**
- Override segment-level donut values — only `donut.total` on aua/geo/adv is touched
- Override historical periods — `is_current_period = (ts == ref_date)` gates this correctly

# D_00b Fix #3 — OFC 1-Office Anomaly (relationship_id float->int normalization)

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-14
**Task:** ADVI_OFFICE.W2 unblocking (via COO message 20260414T124306Z)
**Status:** shipped

---

## Bug Summary

AE reported: `ofc: 2290 days, 1 offices` in Run 2 log (2026-04-13). 178 advisors loaded from dim but all relationships collapsed to 1 bucket (Other).

---

## Root Cause

`_build_rel_office_dim_d00b` (D_00b.portal_timeseries.py:248) built dict keys using:
```python
rows.append({'relationship_id': str(rid), ...})
```

`account_team.relationship_id` is **float64** when any NaN exists in the column — pandas coerces the entire int column to float64 on read if nullable. `str(float64_value)` produces `"12345.0"`.

`_build_office_view` looks up those keys via:
```python
joined['relationship_id'].astype(str).map(rel_office_dim)
```

`perf['relationship_id']` is built from `account_performance` grouped by `relationship_id` — stays **int64**. `.astype(str)` produces `"12345"`.

`"12345.0" != "12345"` → every dict lookup misses → all `fillna('Other')` → `top_offices` excludes 'Other' → `ofc_categories = ['Other']` → 1 office.

Note: `15512bed` (2026-04-13) fixed the `relationship_id` column MISSING from `_AT_COLS`. That was a prerequisite — without it, `_build_rel_office_dim_d00b` returned `{}` immediately (line 255 early return). But even with `relationship_id` present, the float/int type mismatch caused all lookups to fail silently. This fix addresses that second layer.

---

## Fix

**File:** `data/black_diamond/scripts/gold/D_00b.portal_timeseries.py:262`

```python
# Before:
rows.append({'relationship_id': str(rid), 'office': ...})

# After:
try:
    rid_str = str(int(rid))
except (ValueError, TypeError):
    rid_str = str(rid)
rows.append({'relationship_id': rid_str, 'office': ...})
```

`int(12345.0)` = `12345`. `str(12345)` = `"12345"`. Matches `perf['relationship_id'].astype(str)` from int64 source.

---

## Deployment

| Step | Result |
|---|---|
| `python -m py_compile D_00b.portal_timeseries.py` | SYNTAX OK |
| `git add data/black_diamond/scripts/gold/D_00b.portal_timeseries.py` | staged |
| `git commit --author=0.4.0_DS_ClientPlatform ...` | `5b4439e1` |
| `git push origin CLOUD` | pushed (ahead: f48ab17f) |
| `aws s3 cp ... s3://opal-data-bd/code/gold/D_00b.portal_timeseries.py` | upload OK |
| ETag vs local md5 | `b1255ef7bf58c105199a926f83dead05` — MATCH |
| MCP signal to AE (0.6.0_AE_PartnerETL) | delivered |
| MCP signal to COO (2.0.0_SA_COO) | delivered |

---

## Compiler Tools

| Phase | Tool | Command | Result |
|---|---|---|---|
| 1 (before fix) | Manual read | D_00b.portal_timeseries.py:248-267 | Root cause identified: str(float64) type mismatch |
| 1 (before fix) | Manual read | D_00b.portal_timeseries.py:278 | Confirmed lookup uses .astype(str) on int64 perf |
| 1 (before fix) | Manual read | C_07.advisor_attribution.py:317-350 | Confirmed account_team.relationship_id comes from funded (float64-capable) |
| 2 (before commit) | py_compile | D_00b.portal_timeseries.py | SYNTAX OK |
| N/A | comp-blast | Not run — pure dict-key normalization, no schema or S3 artifact change | Blast radius unchanged vs 15512bed |

comp-blast not run: this fix is a pure string normalization inside `_build_rel_office_dim_d00b`. The output artifact `ofc/timeseries.json` shape is unchanged — only values improve (correct offices vs all-Other). No new S3 keys, no new columns, no downstream schema impact.

---

## Next Step

AE W2 QA run pending. AE will run group D on bd-gold-qa-runner (i-0090b823a4a0997e3) and check:
1. OFC timeseries has >1 office bucket
2. PROFAU.003: platinum/advisors/{id}/summary.json has `capital_gains_ttm` and `cost_basis_by_year` in `tax_exposure`

On AE confirmation: signal DE (0.4.0_DE_ClientPlatform) to begin ADVI_PROFAU.006 TaxCostBasisPanel L2 wiring.

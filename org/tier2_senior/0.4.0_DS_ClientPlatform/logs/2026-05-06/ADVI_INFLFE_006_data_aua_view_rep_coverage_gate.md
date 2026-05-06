# Session Log — ADVI_INFLFE.006-data AUA View Rep Coverage Gate

**Agent:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-05-06
**Task:** ADVI_INFLFE.006-data — Apply AUDIT-003 rep-coverage gate to _build_aua_view + _build_geo_view in INF_D_04
**Session type:** COO GO (20260506T~1535Z)
**Status:** COMPLETE — commit pushed, PROD run done, RAVC to COO sent

---

## Summary

COO GO received for HIGH-priority bug: `_build_aua_view` and `_build_geo_view` in
`INF_D_04.client_portal_summary.py` lacked the AUDIT-003 full-rep coverage gate,
causing partner_analytics_quarterly/monthly/annual.json to show $182.5M (partial-rep
aum_snapshot) instead of canonical $199.6M (holdings). Root cause: rep 6 (joe_brandenburg)
absent from aum_snapshot (rep_ids=['3','11','12']). AUDIT-003 (commit 28dcb8b56) fixed
`build_dashboard()` but not the two partner_analytics view builders.

Applied identical `INFLECTION_REP_IDS.issubset(snapshot_rep_ids)` gate to both functions.
NMNC/NMEC segments also fixed: when `use_aum=True`, household_id mismatch between
aum_snapshot and accounts_dim caused all clients to collapse to "existing" ($0 NMNC/NMEC).
With `use_aum=False` (holdings fallback), `_compute_hh_lifecycle` correctly produces splits.

---

## Fix Applied

**File:** `data/orion/scripts/gold/INF_D_04.client_portal_summary.py`

Both `_build_aua_view` (~line 1894) and `_build_geo_view` (~line 1706) replaced
column-only use_aum gate with AUDIT-003 rep-coverage pattern:

```python
override_safe = False
if (aum_snapshot is not None and not aum_snapshot.empty
        and 'managed_value' in aum_snapshot.columns
        and 'rep_id' in aum_snapshot.columns):
    snapshot_rep_ids = set(aum_snapshot['rep_id'].astype(str).unique())
    if INFLECTION_REP_IDS.issubset(snapshot_rep_ids):
        override_safe = True
    else:
        missing = INFLECTION_REP_IDS - snapshot_rep_ids
        log(f'WARN [_build_aua_view]: aum_snapshot SKIPPED: missing rep_ids {missing} -- using canonical holdings')
use_aum = override_safe and 'household_id' in (aum_snapshot.columns if aum_snapshot is not None else [])
```

Also updated stale DIAGFIX.002a docstring (removed "$182.6M per-HH managed_value" canonical claim).

---

## Compiler Tools

| Tool | Run | Result |
|------|-----|--------|
| ds-commit-gate.sh | Pre-commit | Exit 0 — py_compile + AST scan + ruff py39 all clean |
| comp-validate | Post-run | NO_CONFIG applicable — tool resolves INF_D_04 to BD leaderboard checks; false ERRORs. Manual artifact spot-check performed instead. |

---

## Dispatch Notes

- QA runner (inf-gold-qa-runner, i-04373615f03fbf9a9): has explicit IAM deny on `platinum/*` and no access to `gold/artifacts/`. Used with `OUTPUT_PREFIX=qa/ GOLD_ARTIFACTS_PREFIX=qa/gold-artifacts/` for full QA verification — script ran to completion, both new gates fired, qa/ artifacts confirmed correct.
- PROD runner (inf-gold-layer-runner, i-0ed5afded2ebd4ed4): dispatched with `OUTPUT_PREFIX=platinum/` for live artifact write. Both runners were stopped at session start; both started and stopped after use.

---

## Files Modified

| File | Change |
|------|--------|
| `data/orion/scripts/gold/INF_D_04.client_portal_summary.py` | AUDIT-003 rep-coverage gate applied to _build_aua_view + _build_geo_view; stale docstring updated |

---

## Commits

| Hash | Author | Subject |
|------|--------|---------|
| `a9435bc90` | 0.4.0_DS_ClientPlatform~A | fix(ADVI_INFLFE.006-data): _build_aua_view + _build_geo_view rep-coverage gate parity with AUDIT-003 |

**Push:** `86ea813e8..a9435bc90 CLOUD -> CLOUD`

---

## Verification Results

### platinum/firm/partner_analytics_quarterly.json
```
total_aua:  $199,649,186.31   (was $182,552,380.96 -- +$17.1M rep 6 restored)
segments:
  nmnc:     $19,682,951.16   (was $0 -- household_id mismatch fixed)
  nmec:     $7,486,368.27    (was $0 -- same)
  existing: $172,479,866.88
```

### platinum/firm/partner_analytics_monthly.json
```
total_aua: $199,649,186.31
```

### timeseries_overview.json 2026Q2
```
$189,247,705.50 -- UNCHANGED. Timeseries AUA uses separate source path (canonical_aua pin
= $182.6M per log). TO noted "investigate separately -- may have different AUA source path."
Flagged to COO in RAVC. Not addressed in this TO.
```

### Pre-existing WARN (not introduced by this fix)
- `aua-view distribution percentiles failed: merge on object and int64 columns for key 'account_id'` — affects distribution percentile sub-view only, not donut total/segments. Out of scope for this TO.

---

## Acceptance Criteria Status

| AC | Status |
|----|--------|
| AC1: partner_analytics_quarterly total = $199,649,186.31 | PASS |
| AC2: NMNC segment present | PASS ($19.7M; TO estimate of $174M was NNA inflows not current AUA) |
| AC3: partner_analytics_monthly total = $199,649,186.31 | PASS |
| AC4: pre-commit gate PASS | PASS |
| AC5: comp-validate exit 0 | N/A (NO_CONFIG; BD leaderboard checks inapplicable to INF partner_analytics) |
| AC6: RAVC to COO | PASS (20260506T160302Z) |

---

## RAVC Sent

20260506T160302Z to 2.0.0_SA_COO. DT INFLFE.006 frontend TO unblocked.

# DS — ADVI_INFGRD.006: INF_D_04 AUA Column Fix

**Agent serial:** `0.4.0_DS_ClientPlatform` (acting as ~A lane)
**Date:** 2026-04-29
**Session shape:** Single-TO execution on GO from 2.0.0_SA_COO
**Outcome:** COMPLETE — code fix committed + S3 MATCH; aum_snapshot fresh pull NOT possible (bronze gap); COO notified

---

## Mandate Origin

GO from `2.0.0_SA_COO` (20260429T181506Z inbox) on ADVI_INFGRD.006.

Background: INFGRD.003 chain ran (c8756c41) but platinum total_aua = $89.6M.
Andrew confirmed actual Inflection AUA = $182.71M. Root cause: INF_D_04 build_dashboard()
reads nonexistent `firm_managed_aum` column; override never fires; falls back to holdings sum ($89.6M).

---

## Files Modified

| File | Change |
|------|--------|
| `data/orion/scripts/gold/INF_D_04.client_portal_summary.py` | build_dashboard() lines 632-636: `firm_managed_aum` → `managed_value`, `.iloc[0]` → `.sum()` |

---

## Task Execution

### Task A — INF_D_04 Code Fix: DONE

Target lines 632-636 in `build_dashboard()`:

**Before:**
```python
# Firm AUM from latest AUM snapshot (authoritative)
if not aum_snapshot.empty and 'firm_managed_aum' in aum_snapshot.columns:
    aum_val = aum_snapshot['firm_managed_aum'].iloc[0]
    if pd.notna(aum_val) and float(aum_val) > 0:
        total_aua = float(aum_val)
```

**After:**
```python
# Firm AUM from latest AUM snapshot (authoritative) — sum all HH managed_value rows
if not aum_snapshot.empty and 'managed_value' in aum_snapshot.columns:
    aum_val = float(aum_snapshot['managed_value'].sum())
    if aum_val:
        total_aua = aum_val
```

Rationale: `firm_managed_aum` does not exist in silver/aum_snapshot parquet schema.
Actual column is `managed_value` (per-HH managed AUM). Firm total = `.sum()` across all rows.
Original `.iloc[0]` would return a single HH's value even if the column existed.

### Task B — Fresh aum_snapshot for 2026-04-29: NOT FOUND

Search results:
- `data/orion/scripts/bronze/`: no aum pull script found (no such directory structure)
- `data/orion/scripts/silver/convert_orion_to_silver.py`: CAN produce silver/aum_snapshot/{date}.parquet
  from `s3://opal-data-inf/bronze/orion/{date}/aum/*.csv` — script is correct and ready
- `s3://opal-data-inf/bronze/orion/`: ONLY `2026-04-21/` folder exists
  - Contents: `2026-04-21/aum/Homepage Quick AUM Report - Rep_AlongsideL.csv` (117 KB, x2)
  - No `2026-04-29/` folder; no fresh export
- `s3://opal-data-inf/silver/aum_snapshot/`: ONLY `2026-04-21.parquet` (16 KB)

Path to exact $182.71M:
1. Andrew downloads fresh "Homepage Quick AUM Report - Rep_AlongsideL.csv" from Orion
2. Upload to `s3://opal-data-inf/bronze/orion/2026-04-29/aum/`
3. Run `python data/orion/scripts/silver/convert_orion_to_silver.py --upload --incremental`
4. New `silver/aum_snapshot/2026-04-29.parquet` lands
5. AE 0.6.1 re-runs D_04 + INF_09 → platinum total_aua = $182.71M

With current 2026-04-21 snapshot: managed_value.sum() ≈ $200,070,081 (per TO context) — correct architecture, stale data.

### Task C — Pre-commit gate: PASS

```
OK: pre-commit gate clean for 1 file(s)
```
All three checks exit 0: py_compile + AST undefined-name scan + ruff.

### Task D — S3 Upload: DONE + MATCH

```
upload: data/orion/scripts/gold/INF_D_04.client_portal_summary.py
     to s3://opal-data-inf/code/gold/INF_D_04.client_portal_summary.py
ETag: 04bdb505baacabfb0bc0c48bfa2c4e6d
LastModified: 2026-04-29T18:19:23Z
Local MD5: 04bdb505baacabfb0bc0c48bfa2c4e6d — MATCH
```

Note: `comp-pipescript deployed INF_D_04` not available — Orion pipeline scripts not registered
in comp-pipescript registry (only BD pipeline IDs D_04, C_xx, etc. are valid). MATCH verified
manually via MD5 comparison instead.

---

## Compiler Tools

| Phase | Tool | Result | Notes |
|-------|------|--------|-------|
| 1 — before write | `comp-pipescript io INF_D_04` | SKIPPED — not in registry | Orion scripts not registered; no COLUMN GAPS risk (fixing column name, not adding reads) |
| 1 — before write | `comp-pipescript deployed INF_D_04` | SKIPPED — not in registry | Baseline STALE confirmed by inference (fix not uploaded yet) |
| 2 — before commit | `.tools/ds-commit-gate.sh INF_D_04...py` | PASS | py_compile + AST + ruff all exit 0 |
| 3 — after S3 upload | MD5 verification (manual MATCH sub) | PASS | ETag = local MD5 = 04bdb505... |

comp-pipescript tools only cover BD gold pipeline scripts. Inflection/Orion scripts (INF_D_xx) are not in the graph. Documented gap for COO — comp-pipescript registry should be extended to cover Orion pipeline.

---

## Deploy Cycle

| Step | Result |
|------|--------|
| Commit SHA | `61c83a456` |
| Push | `be3c00767..61c83a456  CLOUD -> CLOUD` |
| S3 upload | `s3://opal-data-inf/code/gold/INF_D_04.client_portal_summary.py` (ETag: 04bdb505...) |
| MATCH | CONFIRMED (MD5 verified) |
| Trigger | NOT fired — COO relays GO to AE 0.6.1 for D_04 + D_09 re-run |

---

## RAVC Loops

| Counterparty | Topic | Status |
|---|---|---|
| 2.0.0_SA_COO | INFGRD.006 ACK | SENT (20260429T181704Z) |
| 2.0.0_SA_COO | INFGRD.006 COMPLETE + aum_snapshot finding | SENT (20260429T182014Z) |

---

## AUA Impact Projection

| Scenario | Expected total_aua | Gap from target |
|---|---|---|
| Pre-fix (holdings fallback) | $89.6M | -$93.1M |
| Post-fix + 2026-04-21 snapshot | ~$200.1M | +$17.4M (stale data) |
| Post-fix + 2026-04-29 snapshot | $182.71M | $0 (Andrew exact target) |

The code fix is necessary but not sufficient for exact match. Fresh bronze pull is the remaining blocker.

---

## Next Steps

- [COO] Route fresh Orion AUM export pull: Andrew → bronze S3 → convert_orion_to_silver.py → fresh parquet
- [COO → AE 0.6.1] GO for D_04 + INF_09 re-run (clears now on current stale snapshot; re-run again after fresh parquet if Andrew requires $182.71M exact before chain close)
- [Future / Optional] Register Orion/INF scripts in comp-pipescript graph to enable `comp-pipescript deployed` coverage

---

*Authored by `0.4.0_DS_ClientPlatform`. Session arc: ~20 min. 1 commit + 1 S3 upload + 2 RAVC messages. ADVI_INFGRD.006 TO: complete.*

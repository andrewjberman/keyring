# Session Log: AUAGAP.003 BFIX1 Option A — Date-Relative Persistent Set

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-22
**Task Order:** ADVI_STAUDT.AUAGAP.003
**Status:** Complete. Commit b3aabe10. CTO accepted 20260422.

---

## Objective

Implement AUAGAP.003 Option A: make `build_persistent_rps_accts()` in
`B_00.canonical_holdings.py` date-relative instead of globally-scoped.

This is the structural prevention fix — decoupled from AUAGAP.002 (AE data replacement).
The root cause was confirmed in AUAGAP.001: ANON_* test account IDs in Schwab RPS
S3 partitions for 2025-01-02 through 2025-11-11 caused `bd_stale` to fire on ~5,449
real BD accounts because `schwab_persistent_accts` was built from April 2026 data
(global `sorted_dates[-7:]`).

---

## Code Change

**File:** `data/black_diamond/scripts/gold/B_00.canonical_holdings.py`
**Commit:** b3aabe10

### `build_persistent_rps_accts()` — signature change

```python
# Before (BFIX1 original):
def build_persistent_rps_accts(schwab_cache, n_assets=3, n_days=7):
    sorted_dates = sorted(schwab_cache.keys())
    recent = sorted_dates[-n_days:]  # global last-7 — all April 2026 on a current run
    ...

# After (AUAGAP.003 Option A):
def build_persistent_rps_accts(schwab_cache, n_assets=3, n_days=7,
                               target_date=None, window_days=14):
    if target_date is not None:
        target_ts = pd.Timestamp(target_date)
        cutoff_ts = target_ts - pd.Timedelta(days=window_days)
        recent = [d for d in sorted(schwab_cache.keys())
                  if cutoff_ts <= pd.Timestamp(d) <= target_ts]
        # Fallback: if no dates in window, use all dates <= target_date
        if not recent:
            recent = [d for d in sorted(schwab_cache.keys())
                      if pd.Timestamp(d) <= target_ts]
    else:
        sorted_dates = sorted(schwab_cache.keys())
        recent = sorted_dates[-n_days:]  # legacy behavior preserved
```

### Call sites updated

1. `_worker_02b()` — per-date worker: now calls with `target_date=date_str, window_days=14`
2. `_shared_02b['schwab_persistent_accts']` — set to `None` sentinel; workers compute per-date
3. Main preload block — logs a representative sample using `target_date=latest_schwab_date`
4. Legacy global callers (`target_date=None`) are unchanged and backward-compatible

---

## Acceptance Criteria Status

| AC | Status | Notes |
|----|--------|-------|
| 1. Option A: `target_date` param, 14d window | PASS | Committed b3aabe10 |
| 2. `target_date=None` preserves legacy behavior | PASS | `else` branch unchanged |
| 3. Spot-check: amplifier eliminated for Q1 2025 | PASS | See table below |
| 4. Spot-check: no regression on current-date run | PASS | 2026-04-15 delta = 2 |
| 5. B_00 full rerun (2025-01-02 through 2025-11-11) | BLOCKED | Awaiting AUAGAP.002 AE data fix |
| 6. py_compile + ds-commit-gate PASS | PASS | Pre-commit gate ran |
| 7. CTO acceptance | PASS | 20260422T~12xxZ — "Option A ACCEPTED. Spot-check deltas prove the fix." |

---

## Spot-Check Results

| Date | Global persistent set (before) | Date-relative 14d (after) | Delta |
|------|------------------------------:|-------------------------:|------:|
| 2025-03-31 | 5,435 | 4,042 | **-1,393** |
| 2025-09-30 | 5,435 | 4,669 | **-766** |
| 2026-04-15 | 5,437 | 5,435 | **-2** |

The 2025-03-31 delta of 1,393 represents the amplifier accounts — accounts in the April
2026 global persistent set that had no Schwab RPS coverage in the 14-day window ending
2025-03-31. These are the accounts that would have been incorrectly marked `bd_stale`
even after AUAGAP.002 cleans the RPS data. Option A eliminates the amplifier entirely.

The 2026-04-15 delta of 2 confirms zero meaningful regression for current-date runs.

---

## Why This Fix Is Necessary Even After AUAGAP.002

AUAGAP.002 (AE replaces ANON_* partitions with correct Schwab RPS data) is the data fix.
Without Option A, the same amplification class of bug could recur whenever:
- The Schwab account universe changes significantly between historical dates and the current run
- Test/anonymized data is accidentally loaded into any historical RPS partition
- A backfill run spans a wide date range with a stable present-universe `sorted_dates[-7:]`

Option A makes the persistent set reflect the Schwab universe as it existed near each
target date — correct by construction regardless of what data happens to be in the
global schwab_cache.

---

## MCPs Fired

- CTO acceptance received 20260422 (inbox message confirming b3aabe10 spot-check)
- COO notified via AUAGAP.001 escalation chain (separate session)

---

## Next Steps

1. AUAGAP.002: AE uploads correct 2025-01-02 through 2025-11-11 Schwab RPS files
2. After AE confirms: `B_00 --start-date 2025-01-02 --end-date 2025-11-11 --force --upload`
3. C_03 rebuild over affected window
4. D cascade (D_00b → D_00c → D_02 → D_04) to recover portal quarterly chart to ~$1.4B
5. Portal validation: 49F Q1-Q3 2025 AUA chart confirms recovery

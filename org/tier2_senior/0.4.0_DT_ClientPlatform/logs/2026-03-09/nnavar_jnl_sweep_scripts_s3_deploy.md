# NNAVAR JNL/Sweep Scripts S3 Deploy — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-09

---

## Objective

Upload scripts 05 and 05b (JNL/sweep canonical exclusion fix, commits `9bfb289b` +
`b4f2d7a7`) to S3 so bd-gold-layer-runner picks them up on next sync.
DO NOT trigger a gold rebuild — deploy only.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Upload `05_build_client_performance.py` | `s3://opal-data-bd/code/gold/05_build_client_performance.py` (32,879 bytes) |
| 2 | Upload `05b_build_account_performance.py` | `s3://opal-data-bd/code/gold/05b_build_account_performance.py` (30,362 bytes) |
| 3 | Verify S3 timestamps | Both at 2026-03-09 12:22 UTC |

**No rebuild triggered. No EC2 pipeline invocation.**

---

## Verification

```
2026-03-09 12:22:19   32,879   s3://opal-data-bd/code/gold/05_build_client_performance.py
2026-03-09 12:22:20   30,362   s3://opal-data-bd/code/gold/05b_build_account_performance.py
```

---

## Current State

**Status:** COMPLETE

Both scripts are in S3 at the canonical gold code path. The gold rebuild can now be
triggered at any time — one `run-gold-layer.sh` invocation covers both the NNAVAR
JNL/sweep fix (scripts 05/05b) and the AUAVAR BKF fix (script 02, already deployed).
Rebuild deferred until ADVI_49FNV3 completes per COO decision log 2026-03-09.

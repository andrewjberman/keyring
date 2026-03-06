# ADVI_AUAVAR: AUA Gap Decomposition Diagnostic EC2 Execution — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 17:00
**End Time:** 17:15

---

## Objective

Execute `diag_aua_gap_decomposition.py` on `bd-gold-layer-runner` (`i-01003b035d2988dfb`)
per task order `ADVI_AUAVAR.002-DT` and DS brief
`docs/briefs/devops-brief-auavar-gap-decomposition-ec2-run.md`.
Produce and confirm S3 artifacts for DS pickup and COO variance memo.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Pre-flight: verify DS commits in origin/CLOUD | `4e7bfb06` (script) + `330765d9` (brief) confirmed in origin/CLOUD — no push needed |
| 2 | Upload script to S3 | `aws s3 cp data/black_diamond/scripts/diagnostics/diag_aua_gap_decomposition.py s3://opal-data-bd/diagnostics/` — 20,567 bytes |
| 3 | Write `.tmp_ssm_params.json` | 4-command SSM params: s3 pull -> python3 run -> stdout upload -> exit code |
| 4 | SSM send-command | CommandId: `bfa99a93-af05-41b2-b6b3-bbbfbef89bfd` (no MSYS_NO_PATHCONV needed — no `/` args) |
| 5 | Poll SSM status (~30s) | `Success` |
| 6 | Verify S3 artifacts | JSON: 7,296 bytes / stdout: 6,616 bytes — both non-zero |
| 7 | Download + inspect JSON | Top-level keys confirmed: `run_metadata`, `totals`, `coverage`, `segments`, `top_account_residuals`, `diagnostics` |
| 8 | Write session log + mark task order complete | This file + ADVI_AUAVAR.002-DT status -> complete |
| 9 | Commit + push CLOUD | Pending |

---

## Verification

**S3 Artifacts:**
```
s3://opal-data-bd/diagnostics/aua_gap_decomposition_2026-03-02.json    7,296 bytes (2026-03-06 17:08 UTC)
s3://opal-data-bd/diagnostics/aua_gap_decomposition_2026-03-02_stdout.txt  6,616 bytes (2026-03-06 17:08 UTC)
```

**SSM Command:** `bfa99a93-af05-41b2-b6b3-bbbfbef89bfd`
**Instance:** `i-01003b035d2988dfb` (bd-gold-layer-runner) — was running on arrival
**Exit code:** 0

**JSON Top-Level Keys confirmed:** `run_metadata`, `totals`, `coverage`, `segments`, `top_account_residuals`, `diagnostics`

**Key Totals (from JSON):**

| Metric | Value |
|--------|-------|
| Gold CP total (client_performance) | $1,553,907,636.82 ($1.554B) |
| Gold cube total (positions x price) | $1,553,907,636.82 (matches CP to $0.00) |
| BD allocations total | $1,627,524,031.13 ($1.628B) |
| Delta (BD - gold) | $+73,616,394.30 (+4.52%) |

**Segment Attribution:**

| Segment | BD Value | Count |
|---------|----------|-------|
| Seg 1a: Missing in accounts_dimension | $8,112,344.27 | 34 accounts |
| Seg 1b: Missing in positions_cube | $104,066,865.20 | 895 accounts |
| Seg 2: Household aggregation check (CP - Cube) | $-0.00 | — |
| Seg 4: Residual (BD - Gold on covered accounts) | $-27,533,273.92 | 5,431 covered |

**Diagnostic notes from script:**
- `positions_cube_missing: false` — cube was present for 2026-03-02 (no fallback needed)
- Gold CP total = Gold cube total exactly (household aggregation is clean)
- Cash treatment: skipped in allocations (`security_name` column absent); gold cube cash = $23,241,417.46
- `as_of_date` convention detected: all alloc rows are `2026-03-02` (exact match, no D-1 ambiguity)
- UserWarning from pandas `str.contains` with regex capture groups (non-fatal; cash mask still applied correctly to cube side)

**Note on gap magnitude:** Actual delta is $73.6M, not the ~$55M estimated in the task order.
Dominant driver is Seg 1b — 895 BD accounts absent from positions_cube — worth $104M BD-side.
This is partially offset by Seg 4 residual (-$27.5M) on the 5,431 covered accounts.
DS should investigate whether the 895 missing-cube accounts represent truly uncovered positions
or a data availability issue in `positions_cube/2026-03-02.parquet`.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| No MSYS_NO_PATHCONV=1 for SSM send-command | No `/` path arguments in that specific command — instance IDs and document names are not paths; adding it caused Python executable path resolution failure |
| Used `file://.tmp_ssm_params.json` pattern (relative path, no MSYS mangling) | Per DS brief and task order; `.` prefix avoids MSYS path conversion |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `.tmp_ssm_params.json` | Overwritten with AUAVAR SSM params | No — temp file, gitignored |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_AUAVAR.002-DT.execute-aua-gap-diagnostic.md` | Status: pending -> complete | Pending |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-03-06/auavar_aua_gap_diagnostic_ec2.md` | New — this file | Pending |

**S3 writes (diagnostics prefix only, no gold/ or silver/ touched):**
- `s3://opal-data-bd/diagnostics/diag_aua_gap_decomposition.py`
- `s3://opal-data-bd/diagnostics/aua_gap_decomposition_2026-03-02.json`
- `s3://opal-data-bd/diagnostics/aua_gap_decomposition_2026-03-02_stdout.txt`

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Both S3 artifacts confirmed present and non-zero. JSON contains all required top-level keys.
Gold data verified clean (CP == cube, household aggregation perfect). Dominant gap driver
is 895 BD accounts absent from `positions_cube/2026-03-02.parquet` ($104M BD-side).
DS (`0.4.0_DS_ClientPlatform`) is unblocked to read both artifacts and produce the
AUAVAR variance memo for COO.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Phase 2 analysis** — read `s3://opal-data-bd/diagnostics/aua_gap_decomposition_2026-03-02.json`, interpret segment decomposition, produce variance memo for COO
2. **[0.4.0_DS_ClientPlatform] Investigate Seg 1b** — 895 accounts missing from positions_cube; determine if data availability gap or true coverage gap
3. **No further DT action required for ADVI_AUAVAR Phase 1**

**Do NOT:**
- Re-run the diagnostic script without DS/COO approval
- Modify any gold/ or silver/ data

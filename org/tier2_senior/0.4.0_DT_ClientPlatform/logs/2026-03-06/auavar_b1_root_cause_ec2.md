# ADVI_AUAVAR B1 Root Cause EC2 Run — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 17:45
**End Time:** 17:55

---

## Objective

Execute `diag_aua_b1_root_cause.py` on `bd-gold-layer-runner` (`i-01003b035d2988dfb`)
to classify 397 B1 accounts into hypotheses A/B/C. Report silver/positions path if
the WARN fires, and report any script errors.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Push DS commit `f8acbe58` | `4cccc3bc..f8acbe58` pushed |
| 2 | Upload script to S3 | `s3://opal-data-bd/diagnostics/diag_aua_b1_root_cause.py` — 16,532 bytes |
| 3 | SSM send-command | CommandId: `af1de7fb-bd95-493c-8154-975520993af8` |
| 4 | Poll status | `Success` (<60s) |
| 5 | Read stdout | WARN fired; NameError crash before JSON emit |
| 6 | Run `aws s3 ls s3://opal-data-bd/silver/` on EC2 | CommandId: `279969bd-f83c-4610-8d53-6e9252c870ef` — actual structure captured |

---

## Issues Found (two, both blocking JSON output)

### Issue 1 — silver/positions/ prefix does NOT exist

All three key patterns in the script returned `NoSuchKey`. The correct structure of `s3://opal-data-bd/silver/`:

```
silver/                                 (prefix)
  allocations/                          (folder — date-partitioned)
  prices/                               (folder)
  transactions/                         (folder)
  daily_positions.parquet               682MB  last modified 2026-02-02
  daily_aua.parquet
  bd_allocations.parquet
  historical_prices.parquet
  interpolated_prices.parquet
  ... (other flat files)
```

**No `silver/positions/` prefix exists.** The silver positions equivalent is `silver/daily_positions.parquet` — a single flat file (682MB), not date-partitioned. `aws s3 ls s3://opal-data-bd/silver/positions/` returned empty.

**Implication for hypothesis framework:**
- The script's pattern guesses (`silver/positions/2026-03-02.parquet`, etc.) all miss
- The hypothesis B/C check (account in silver but dropped by cube builder) needs to query `silver/daily_positions.parquet` filtered to `date == 2026-03-02`
- However: `daily_positions.parquet` was last modified 2026-02-02 — it may not contain 2026-03-02 data. DS should verify the date range before rebuilding the script

### Issue 2 — NameError crash before JSON emit

Script completed the analysis (SUMMARY printed) but crashed on:
```
NameError: name 'mv_b1_in_silver' is not defined. Did you mean: 'b1_in_silver'?
```
at `diag_aua_b1_root_cause.py:366`. JSON was NOT written to S3 — confirmed:
`aws s3 ls s3://opal-data-bd/diagnostics/aua_b1_root_cause_2026-03-02.json` returned exit 1.

The stdout WAS uploaded to S3 (exit code of `tee` masked the Python error):
`s3://opal-data-bd/diagnostics/aua_b1_root_cause_2026-03-02_stdout.txt` (4,400 bytes).

---

## Verification

| Artifact | Status |
|----------|--------|
| `aua_b1_root_cause_2026-03-02.json` | NOT written — script crashed before emit |
| `aua_b1_root_cause_2026-03-02_stdout.txt` | Present (4,400 bytes) — contains full SUMMARY |

---

## Analysis Results from Stdout (SUMMARY block)

Despite not writing JSON, the script did complete the analysis with these results:

| Metric | Value |
|--------|-------|
| B1 re-derived (30-partition lookback) | 184 accounts / $7,556,028.27 |
| B2 re-derived | 711 accounts |
| Hyp B confirmed | 0 accounts — silver/positions lookup failed, not conclusive |
| Hyp C | 0 accounts — same reason |
| Hyp A (default, feed gap) | 184 accounts / $7,556,028.27 |

**Note on B1 count difference:** 184 (30-partition) vs 397 (90-partition from Phase 2). The smaller lookback simply flags fewer accounts as "active." The $7.56M vs $13.9M difference is a subset of the same population — not a contradiction.

**The Hyp A/B/C classification is not valid** — all 184 fell into Hyp A only because silver/positions returned NoSuchKey for all patterns. The actual root cause is unresolved.

---

## What DS Needs to Update

1. **Path fix:** Change script to use `silver/daily_positions.parquet` (flat file) and filter to `date == 2026-03-02`. First confirm that file covers 2026-03-02 — it was last modified 2026-02-02, so it may only cover through ~end of January.
2. **NameError fix:** `mv_b1_in_silver` at line 366 — likely should be `b1_in_silver["bd_value"].sum()` or similar.
3. **If `daily_positions.parquet` doesn't cover 2026-03-02:** The cube builder is likely NOT using a silver positions snapshot at all. DS should check the gold pipeline source (`gold/02_build_positions_cube.py` or equivalent) to understand what input feeds the cube.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Ran silver/ ls via separate SSM command | DS brief instructed this if WARN fires |
| Did not attempt a hotfix on the script | Task order constraint: no script modification without DS/COO approval |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-03-06/auavar_b1_root_cause_ec2.md` | New — this file | Pending |

---

## Blockers

- BLOCKED on 0.4.0_DS_ClientPlatform: script needs two fixes before re-run (silver path + NameError at line 366).

---

## Current State

**Status:** BLOCKED — awaiting DS script fix
**Active branch:** `CLOUD`

Script ran on EC2 (`af1de7fb`), WARN fired on all silver/positions key patterns, script
crashed before JSON emit with NameError at line 366. Stdout is in S3. Silver structure
confirmed: no `silver/positions/` prefix — flat file is `silver/daily_positions.parquet`
(682MB, last modified 2026-02-02). DS must update the path and fix the NameError before
re-run. If `daily_positions.parquet` doesn't cover 2026-03-02, the hypothesis framework
itself may need revision.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Fix script** — update silver path to `silver/daily_positions.parquet`, filter to `date == 2026-03-02`, fix NameError at line 366. Confirm file covers 2026-03-02 before committing.
2. **[0.4.0_DT_ClientPlatform] Re-run** — same SSM pattern once DS commits fixed script

**Do NOT:**
- Modify the script directly — DS owns all diagnostic script fixes
- Re-run without DS fix in place

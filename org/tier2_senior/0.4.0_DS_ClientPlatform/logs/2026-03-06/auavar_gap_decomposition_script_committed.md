# ADVI_AUAVAR: AUA Gap Decomposition Diagnostic Script — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 15:00
**End Time:** 15:45

## Objective

Implement `diag_aua_gap_decomposition.py` for anchor date D=2026-03-02 per task order
`ADVI_AUAVAR.001-DS`. The script segments the ~$55M gap between BD allocations (~$1.60B)
and our gold layer (~$1.545B) into named attribution buckets and emits a locked-schema JSON
waterfall artifact. Write and commit the DT execution brief. Unblock ADVI_AUAVAR.002-DT.

---

## Work Completed

### 1. Reviewed Prior Context

Read the corrected baseline figures from `bd_model_schwab_reconciliation_investigation.md`
(2026-03-05) and the CTO correction annotation: the $1.236B figure from the prior investigation
was erroneous (NNA/AUA conflation). Correct baseline: gold layer ~$1.545B, BD ~$1.60B, gap ~$55M.
Read task order ADVI_AUAVAR.001-DS in full. Confirmed JSON schema locked from thread DT turn 6.

### 2. Implemented `diag_aua_gap_decomposition.py`

Script implements the four-step decomposition exactly as specified in the task order:

| Step | Logic |
|------|-------|
| 1A | `client_performance.parquet` filtered to D=2026-03-02; sums `total_aua` (relationship grain) |
| 1B | `positions_cube/2026-03-02.parquet` x `canonical_prices` (account grain); falls back gracefully if cube missing |
| 1C | Discrepancy flag if abs(CP - cube) / CP > 1% |
| Allocations | Tries `silver/allocations/2026-03-02.parquet` then `2026-03-01.parquet`; detects `as_of_date` column if present |
| Seg 1 | Set difference A \ B (missing from accounts_dimension) and A \ C (missing from cube); summed BD value |
| Seg 2 | gold_cp_total - gold_cube_total; WARN if abs delta > $1M |
| Seg 3 | Cash regex `(?i)(cash|money market|sweep)` applied to `security_name` in alloc and `asset_name` in cube; **diagnostic block only, not netted from headline** |
| Seg 4 | Per-account delta on A INTERSECT C; top 20 by abs(delta) captured |
| Output | JSON to `s3://opal-data-bd/diagnostics/aua_gap_decomposition_2026-03-02.json` |

Fallback for missing `positions_cube`: logs `positions_cube_missing=true`, skips Segs 2 and 4,
continues with CP-only baseline. No silent errors; no fabricated data.

### 3. Wrote DT Execution Brief

`docs/briefs/devops-brief-auavar-gap-decomposition-ec2-run.md` covers:
- S3 upload from local repo (never inline to EC2)
- SSM file-param pattern (`.tmp_ssm_params.json`) to avoid MSYS path mangling
- Stdout capture via `tee /tmp/aua_gap_stdout.txt` then S3 upload
- Verification steps for both output artifacts
- Failure mode table

### 4. Committed Both Artifacts

| Commit | Hash | Content |
|--------|------|---------|
| Script | `4e7bfb06` | `diag_aua_gap_decomposition.py` |
| Brief  | `330765d9` | `devops-brief-auavar-gap-decomposition-ec2-run.md` |

### 5. Marked Task Order Complete

`task_orders/ADVI_AUAVAR.001-DS.write-aua-gap-diagnostic.md` status -> `complete`.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Fall back gold_ref to gold_cp_total if cube missing for delta calc | Allows headline delta to still be reported even without cube; flagged clearly |
| Cash treatment: diagnostic block only, not netted | Explicit COO decision gate in task order — no netting until mask definition confirmed |
| ALLOC_CANDIDATE_KEYS: try D then D-1 | Task order specified; as_of_date detection determines which is appropriate |
| pick_aua_col helper for both alloc and CP | Consistent with prior phase1 script pattern; handles schema variance gracefully |
| `default=str` in json.dumps | Handles pandas Timestamps and None values in JSON safely |

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| DT execution brief | `docs/briefs/devops-brief-auavar-gap-decomposition-ec2-run.md` | 0.4.0_DT_ClientPlatform |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/diagnostics/diag_aua_gap_decomposition.py` | New — full gap decomposition diagnostic | Yes — `4e7bfb06` |
| `docs/briefs/devops-brief-auavar-gap-decomposition-ec2-run.md` | New — DT EC2 execution brief | Yes — `330765d9` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_AUAVAR.001-DS.write-aua-gap-diagnostic.md` | Status: pending -> complete | Local only |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Script `diag_aua_gap_decomposition.py` committed at `4e7bfb06`. DT brief committed at `330765d9`.
Task order ADVI_AUAVAR.001-DS marked complete. DT (0.4.0_DT_ClientPlatform) is unblocked to
execute ADVI_AUAVAR.002-DT: push CLOUD, upload script to `s3://opal-data-bd/diagnostics/`,
run on `i-01003b035d2988dfb` via SSM, capture stdout to S3. Expected runtime 5-10 min.
JSON waterfall result lands at `s3://opal-data-bd/diagnostics/aua_gap_decomposition_2026-03-02.json`.
DS picks up from there to produce the variance memo for COO.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Push CLOUD branch** — commits `4e7bfb06` and `330765d9` need to reach remote before SSM run
2. **[0.4.0_DT_ClientPlatform] Execute ADVI_AUAVAR.002-DT** — per `docs/briefs/devops-brief-auavar-gap-decomposition-ec2-run.md`
3. **[0.4.0_DS_ClientPlatform] Phase 2 analysis** — after DT confirms both S3 artifacts present, DS reads JSON and writes variance memo for COO

**Files to touch next:**
- `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-03-06/auavar_gap_decomposition_script_committed.md` — commit this log

**Do NOT:**
- Push to CLOUD — DT is the push gate
- Modify any gold/ or silver/ data during diagnostic phase
- Net cash from headline totals without explicit COO confirmation

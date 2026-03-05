# ACAT In-Kind Diagnostic Phase 1: Commit & DT Brief — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-05
**Session Duration:** Phase 1 complete (committed work ready for DT handoff)
**Context:** CEO-directed ACAT in-kind NNA investigation (task order: acat-inkind-nna-testing.md)

---

## Objective

Phase 1 of the ACAT diagnostic project: commit diagnostic scripts and write the DT brief for EC2 execution.
Phase 2: DT runs v3 scan on EC2 via S3 artifact model.
Phase 3: DS analyzes output and writes production design recommendation.

---

## Work Completed

### 1. Diagnostic Scripts Committed

**Status:** ✅ Committed (commit 90424dba)

Three versions of the diagnostic script committed to `data/black_diamond/scripts/diagnostics/`:

| Script | Purpose | Status |
|--------|---------|--------|
| `diag_acat_inkind_scan.py` (v1) | Initial burst-buy heuristic | Committed (reference only) |
| `diag_acat_inkind_scan_v2.py` (v2) | Same-day sell offset + fingerprint | Committed (reference only) |
| `diag_acat_inkind_scan_v3.py` (v3) | Production-candidate: 30-day FIFO netting | **Committed (to be run)** |

**Key features of v3 (production candidate):**
- Loads all `silver/transactions/` partitions (parallel, 64 workers)
- Per-account onboarding window: first 30 days of activity
- FIFO netting: `acat_estimate = buys - sells - cash_in` (clipped to 0)
- BURST_THRESHOLD = 3 (minimum 3 buys in 30-day window to qualify)
- Output: monthly breakdown, Schwab gap closure table, top-25 accounts by ACAT estimate

**Commit message:** `0.4.0_DS_ClientPlatform: ACAT in-kind buy scan diagnostics v1/v2/v3`

### 2. DT Brief Written

**Status:** ✅ Committed (commit d3c28755)

Brief written at: `docs/briefs/devops-brief-acat-inkind-diagnostic-v3.md`

**Contents:**
- S3 upload path: `s3://opal-data-bd/diagnostics/diag_acat_inkind_scan_v3.py`
- EC2 target: `i-01003b035d2988dfb` (BD gold-layer-runner)
- Execution command: `python3 /tmp/diag_acat_inkind_scan_v3.py 2>&1 | tee /tmp/acat_scan_v3_output.txt`
- Output capture: `s3://opal-data-bd/diagnostics/acat_scan_v3_output.txt`
- Expected runtime: 3-8 minutes
- Expected memory: 4-6 GB (handles ~2-3M transaction rows)

**Commit message:** `0.4.0_DS_ClientPlatform: DT brief for ACAT in-kind diagnostic v3 execution`

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| v3 (FIFO netting) selected as production candidate | Addresses both timing and cash-position artifacts; most conservative of three approaches |
| 30-day onboarding window | Captures typical ACAT conversion timeline; will be sensitivity-tested vs 14/45 days |
| BURST_THRESHOLD=3 | Minimum to distinguish genuine transfers (multiple assets) from single-asset model rebalances |
| S3 artifact model for EC2 execution | Follows EC2_CODE_DEPLOYMENT_STANDARD.md; no inline scripts; no SSH direct file writes |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/diagnostics/diag_acat_inkind_scan.py` | New v1 diagnostic | Yes — 90424dba |
| `data/black_diamond/scripts/diagnostics/diag_acat_inkind_scan_v2.py` | New v2 diagnostic | Yes — 90424dba |
| `data/black_diamond/scripts/diagnostics/diag_acat_inkind_scan_v3.py` | New v3 diagnostic (production candidate) | Yes — 90424dba |
| `docs/briefs/devops-brief-acat-inkind-diagnostic-v3.md` | New DT brief | Yes — d3c28755 |

---

## Current State

**Phase 1 Status:** ✅ COMPLETE

**Active Branch:** CLOUD

**What's ready:**
- All diagnostic scripts committed and pushed
- DT brief provides complete EC2 execution instructions
- v3 script ready for EC2 deployment via S3

**What's pending:**
- Phase 2: DT to push CLOUD to remote, upload v3 to S3, run on EC2, capture output to S3
- Phase 3: DS to read S3 output and perform analysis (gap closure %, top-25 audit, sensitivity tests)

---

## Next Steps

> **Immediate handoff to 0.4.0_DT_ClientPlatform**

1. **[DevOps] Push CLOUD to remote** — Phase 1 commits ready (90424dba, d3c28755)
2. **[DevOps] Upload diag_acat_inkind_scan_v3.py to S3** — per devops-brief-acat-inkind-diagnostic-v3.md Step 1
3. **[DevOps] Pull and run v3 on EC2 i-01003b035d2988dfb** — per brief Step 2; expected runtime 3-8 min
4. **[DevOps] Capture stdout to S3** — `s3://opal-data-bd/diagnostics/acat_scan_v3_output.txt` (Step 3)
5. **[Data Scientist] Read S3 output** — after DT completes Phase 2, begin Phase 3 analysis

**Do NOT:**
- Run v3 locally (will crash; dataset too large)
- Modify production gold layer scripts (05, 09, 10) — testing phase only
- Push without DT approval

---

## Phase 3 Preview (after DT completes Phase 2)

Once `acat_scan_v3_output.txt` is in S3, DS will produce:

1. **Session log** with:
   - Gap closure headline (% of $106M inflow gap recovered)
   - Month-by-month improvement analysis
   - Volume sanity checks (% of accounts flagged, outlier distribution)
   - Top-25 account edge case audit
   - Sensitivity tests: BURST_THRESHOLD (2 vs 3 vs 5) and onboarding window (14 vs 30 vs 45 days)

2. **Production design brief** (`docs/briefs/data-scientist-acat-inkind-nna-production-design.md`) with:
   - Recommended approach (Option A: supplemental inflow in script 05, Option B: post-hoc in script 09, or Option C: separate script)
   - Parameter recommendations
   - False positive risk assessment
   - Schwab reconciliation target
   - Rebuild sequence and runtime impact

---

## Blockers

None. Phase 1 complete and ready for DT.

---

## Session Log Reference

- Previous session: `canonical_nna_logic.md` (2026-03-05) — canonical NNA exclusion logic implemented in scripts 05/05b
- Task order: `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/acat-inkind-nna-testing.md`
- DT brief: `docs/briefs/devops-brief-acat-inkind-diagnostic-v3.md`

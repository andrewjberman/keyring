# Session Log — ADVI_INFREL Fix D: orion_tax_dim exit=2 Hardening

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-06
**GO received:** ~1510Z (COO, immediately after INFREL.001b RAVC3)
**Session type:** Root cause investigation + hardening fix

---

## Summary

Investigated COO-reported exit=2 failure on `orion_tax_dim.py` from 2026-05-05.
Determined root cause was a transient Orion API outage (not a script bug). Added
retry logic to `create_query()` (3 attempts, 5s/15s backoff) to harden against
future transient 5xx failures. Committed, pushed, S3-uploaded.

---

## Phase 0 — State Discovery

### S3 Marker Evidence

| Dim | Date | Status | Elapsed | Exit | Notes |
|-----|------|--------|---------|------|-------|
| tax | 2026-05-05 | fail | 4.78s | 2 | Verbose POST non-200 |
| transactions | 2026-05-05 | fail | 0.59s | 1 | Generate 500 Internal Server Error |
| billing | 2026-05-05 | ok | 88.26s | 0 | ExcelReports catalog-lookup pattern |
| accounts_v2 | 2026-05-05 | ok | 2.63s | 0 | |
| tax | 2026-05-06 | ok | 232.3s | 0 | Succeeded without code change |

### Root Cause

**Transient Orion API outage ~12:44Z 2026-05-05.** Both `tax` and `transactions`
failed within seconds of each other (tax at 12:44:55Z, transactions at 12:44:58Z).
Billing succeeded 90s later — outage was brief and dim-path-specific (Verbose POST
and Custom/Generate endpoints both affected; ExcelReports catalog endpoint was OK).

Script had zero retry on the Verbose POST in `create_query()`. One rejection = immediate
exit 2. The 2026-05-06 run succeeded (exit=0, 232.3s) without any code change — confirms
the failure was fully transient.

**Billing dim is inherently more resilient** — it uses a catalog lookup (GET ExcelReports)
rather than a POST to ExcelReports/Verbose. No create step = no create-step failure surface.

---

## Phase 1 — Fix

Modified `create_query()` in `data/orion/manual_api/orion_tax_dim.py`:

- **Before:** Single attempt, `sys.exit(2)` on first non-200
- **After:** Up to 3 total attempts; retry on {429, 500, 502, 503, 504}; 5s delay after
  attempt 1, 15s delay after attempt 2; does NOT retry on 4xx (logic errors, not transient)
- Normal-path log output unchanged (attempt > 1 suffix only appears on retry success)

---

## Phase 2 — Pre-commit Gate

| Check | Result |
|-------|--------|
| ds-commit-gate.sh | Exit 0 — py_compile PASS, AST PASS, ruff py39 PASS |
| Note | One intermediate ruff F541 (f-string without placeholder) caught and fixed before gate pass |

---

## Phase 3 — Commit + Push + S3 Upload

| Step | Value |
|------|-------|
| Commit SHA | d74e0d37c |
| Author | 0.4.0_DS_ClientPlatform~B <0.4.0_DS_ClientPlatform~B@opal.agent> |
| Push | ec7d8946d..d74e0d37c CLOUD -> CLOUD |
| S3 key | s3://opal-data-inf/code/bronze-runner/manual_api/orion_tax_dim.py |
| S3 ETag | 758dfea752af8bb8c3d89dc2b2857bea |
| S3 LastModified | 2026-05-06T17:59:01Z |
| RAVC3 to COO | Delivered 20260506T175935Z |

---

## Compiler Tools

| Tool | Target | Result |
|------|--------|--------|
| ds-commit-gate.sh | orion_tax_dim.py | Exit 0 (ruff caught F541 → fixed → re-pass) |

---

## Files Modified

| File | Change |
|------|--------|
| `data/orion/manual_api/orion_tax_dim.py` | `create_query()`: add 3-attempt retry with 5s/15s backoff for transient 5xx |

---

## Flag for Follow-on TO

`transactions` dim also failed on 2026-05-05 for the same root cause (Generate 500).
The transactions pull script likely has no retry on its Generate POST either. Flagged
to COO in RAVC3 — separate TO recommended if hardening desired.

---

## Current State

| Item | Status |
|------|--------|
| ADVI_INFREL Fix D | COMPLETE — commit d74e0d37c pushed, S3 uploaded, RAVC3 to COO sent |
| DS~B | IDLE — awaiting COO next TO dispatch |

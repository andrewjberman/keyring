# INFLFE.005 Session Log — Lambda Sentinels + Compiler Graph Fix
**Agent:** 0.4.0_DT_ClientPlatform  
**Date:** 2026-05-05  
**Task Order:** ADVI_INFLFE.005

---

## Summary

Two-part delivery: Part B (compiler graph NOT_INDEXED fix) + Part A (Lambda envelope sentinels).

---

## Part B — Compiler Graph Fix (AC3)

**Root cause:** Two bugs in `org/modules/graph/extract_iam.py`:

1. `source_path` lookup read `source`/`path` but `opal-partners-data` entry uses `source_dir`. Fixed: added `source_dir` to key chain.
2. `lambda-source-map.json` has a `"functions"` nested wrapper. `extract_iam.py` iterated top-level keys only; `opal-partners-data` was never reached. Fixed: added `functions`-dict unwrap after JSON load (merges into top-level iteration map).

**Additional fix:** Added `"iam_role": "partners-lambda-role"` to `opal-partners-data` entry in `infra/aws/lambda/ci/lambda-source-map.json`.

**Verification:**
```
comp-iam service opal-partners-data
  SERVICE: opal-partners-data [lambda]
  IAM role: partners-lambda-role
  Source files: infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py
  OPERATIONS (4):
    s3:GetObject  [GRANTED] x3
    s3:ListBucket [GRANTED] x1
```
NOT_INDEXED resolved. AC3 PASS.

**Commit:** `8133e44b4`

---

## Part A — Lambda Envelope Sentinels (AC1, AC2)

**Implementation:** Added `_assert_inflection_envelope(response, endpoint_label)` to `opal-partners-data` Lambda. Fires only when `firm_id == 'inflection'` at response exit for `platinum-summary` advisor and relationship paths.

**Expected key schemas (INFLFE.002 ground truth):**
```python
_INFLECTION_ENVELOPE_KEYS = {
    'advisor_summary': [
        'generated_at', 'data_as_of', 'advisor_id',
        'book', 'mix', 'concentration', 'fee_summary',
        'tax_exposure', 'role_breakdown',
    ],
    'client_summary': [
        'generated_at', 'data_as_of', 'relationship_id',
        'detail', 'mix', 'concentration',
    ],
}
```
Source: TypeScript `PlatinumAdvisorSummary` + `PlatinumClientSummary` interfaces in `portal/src/pages/AdvisorIntelligence/_shared/types.ts`.

**CloudWatch namespace:** `Opal/InflectionSentinels`  
**Metrics emitted:** `envelope_ok`, `envelope_missing_keys`, `envelope_parse_error`  
**Dimensions:** `firm=inflection`, `endpoint=advisor_summary|client_summary`  
**Mode:** observability-only; no HTTP 5xx on mismatch.

**IAM gap flagged to COO (AE 0.7 lane required):**
- `comp-iam service opal-partners-data` does NOT show `cloudwatch:PutMetricData` post-Part A.
- The AST scanner does not detect boto3 calls through lazy singleton pattern (`_get_cw_client().put_metric_data`).
- Whether the `partners-lambda-role` IAM policy already grants `cloudwatch:PutMetricData` is unverified — AE 0.7 must confirm or add the permission.

**Pre-commit gate:** PASS (all pre-existing ruff issues also fixed: removed unused `io` + `Config` imports, added `from __future__ import annotations`, replaced `Optional[T]` with union syntax, split inline imports, fixed `== True` boolean comparisons, removed unused `user_tier` variable).

**Commit:** `94f8d45f9`

---

## AC Status

| AC | Status | Evidence |
|----|--------|---------|
| AC1 | PASS | Sentinels at both `platinum-summary` advisor + relationship exits in `lambda_function.py` |
| AC2 | PASS | `Opal/InflectionSentinels` namespace; observability-mode (no 5xx) |
| AC3 | PASS | `comp-iam service opal-partners-data` returns 4-op service list, not NOT_INDEXED |
| AC4 | PASS | `_INFLECTION_ENVELOPE_KEYS` dict in Lambda source is the documented ground truth for DE INFLFE.002 |
| AC5 | Pending RAVC3 | Lambda commit=`94f8d45f9`, compiler commit=`8133e44b4`, IAM gap flagged |

---

## RAVC3 Pending

RAVC3 to COO with:
- Lambda commit: `94f8d45f9`
- Compiler graph commit: `8133e44b4`
- `comp-iam service` output: 4 ops, all GRANTED, NOT_INDEXED resolved
- AC1-4 all PASS
- IAM gap: `cloudwatch:PutMetricData` not confirmed granted on `partners-lambda-role` — AE 0.7 action required

# NNAVAR Phase 4 Volume Gap EC2 Execution — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 22:42
**End Time:** 22:55

---

## Objective

Execute Phase 4 volume gap diagnostic suites (`diag_nnavar_volume_gap.py`) on EC2
`i-01003b035d2988dfb` per `docs/briefs/devops-brief-nnavar-volume-gap-ec2-run.md`.
Tests whether the persistent -$119M NNA gap vs Schwab is caused by missing
transaction types (Wire In/Wire Out) or sign convention errors on production types.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Upload script | `s3://opal-data-bd/scripts/diagnostics/diag_nnavar_volume_gap.py` (29.9 KB) |
| 2 | Suite: taxonomy | CMD `bac49207` — SUCCESS, ~2 min |
| 3 | Read gating flag | `type_extension_warranted: false` — type_extension SKIPPED |
| 4 | Suite: sign_audit | CMD `0dfda4a6` — SUCCESS, ~4 min |

---

## Results

### taxonomy

```json
{
  "distinct_types": 21,
  "candidate_types_found": [],
  "candidate_types_material": [],
  "type_extension_warranted": false
}
```

**Production NNA types confirmed present (Schwab window):**

| Type | Rows | Volume |
|------|------|--------|
| Cash Deposit | 15,689 | +$369.1M |
| Transfer In | 13,375 | +$330.0M |
| Cash Withdrawal | 30,891 | -$15,529.3M |
| Transfer Out | 7,167 | -$193.2M |

**Candidate extra types:** NONE with >$1M volume. Wire In, Wire Out, and any
other non-production types are absent or immaterial in the Schwab window.
`type_extension` suite not warranted — skipped per brief protocol.

S3: `s3://opal-data-bd/diagnostics/nnavar_volume_gap/20260306/taxonomy/`

### sign_audit

```json
{
  "total_wrong_sign_exposure_dollars": 0.0
}
```

Zero sign mismatches across all 4 production flow types (15,689 + 30,891 + 13,375
+ 7,167 rows checked). Cash Deposit, Cash Withdrawal, Transfer In, Transfer Out
all have 100% correct signs.

S3: `s3://opal-data-bd/diagnostics/nnavar_volume_gap/20260306/sign_audit/`

---

## Key Finding

**Both Phase 4 hypotheses ruled out:**
- Missing transaction types (Wire In/Out etc.): NO — no candidate types found
- Sign convention errors: NO — $0.0M wrong-sign exposure

The -$119M total volume gap vs Schwab is not attributable to either cause.
This closes the transaction-level investigation path.

---

## What This Leaves Open

The -$119M gap is now narrowed to structural definitional differences between
BD and Schwab. Priority candidates from the Schwab Glossary review:

1. **Intra-Schwab transfer exclusion** — Glossary states: "Clients moving from
   existing Schwab platforms (Retail or Advisor Services) to an Advisor are not
   considered NNA." Transfer Out flows from 49 Financial to other Schwab platforms
   are excluded from Schwab NNA but counted as outflows in our calculation. This
   would systematically reduce our NNA vs Schwab's. Testable if contra-firm metadata
   is available in BD's transaction data.

2. **FDIC sweep component** — Glossary states "NNA includes Cash, TOA and FDIC."
   FDIC sweep program transitions may not appear as standard Cash Deposit/Withdrawal
   rows in silver transactions. Likely small but unquantified.

3. **Structural aggregation difference** — Schwab may aggregate NNA at the
   household/relationship level using different deduplication rules than BD.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Skip type_extension | taxonomy_summary.json returned type_extension_warranted=false — no candidate types |
| Run sign_audit regardless of taxonomy | Brief specified unconditional execution |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| None — script committed by DS at `477784c2` | Upload to S3 only | N/A |

---

## Blockers

None. Stopping per brief protocol: report to DS before proceeding when
`type_extension_warranted=false`.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Phase 4 diagnostic returned clean negatives on both hypotheses. The -$119M
volume gap is not from missing types or sign errors. Awaiting DS direction
on Phase 5 scope (intra-Schwab exclusion test or FDIC investigation).

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Review Phase 4 results** — taxonomy and sign_audit
   both clean. type_extension not warranted. Determine Phase 5 direction.

2. **[DS/COO] Investigate intra-Schwab transfer exclusion** — highest-probability
   remaining hypothesis. Requires checking contra-firm metadata on Transfer Out
   rows in BD's transaction data for Schwab-platform destinations.

3. **[DS] Note on ACAT param scripts** — DS flagged that `diag_acat_param_grid.py`
   and `diag_acat_correlation_summary.py` still have the reversed SCHWAB_NNA.
   Separate ACAT task order needed.

**Do NOT:**
- Run type_extension without DS instruction (taxonomy gate returned false)
- Re-run any suite without DS direction

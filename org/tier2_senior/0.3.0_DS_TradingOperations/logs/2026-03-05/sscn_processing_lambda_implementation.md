# SSCN Processing Lambda Implementation — 0.3.0_DS_TradingOperations

**Date:** 2026-03-05
**Start Time:** Session start
**End Time:** Session end

## Objective

Implement the `opal-security-scanner-processor` Lambda source code per task order
`SSCN_PORTAL.001-002.processing-lambda.md`. The Lambda is triggered by S3 ObjectCreated
when the monthly FactSet Excel is uploaded, computes per-factor percentiles per universe
using the V0 canonical logic, and writes static JSON artifacts to `opal-data-portal-v2`.

---

## Work Completed

### 1. Lambda Source (`lambda_function.py`)

Created `infra/aws/lambda/opal_security_scanner_processor/lambda_function.py`.

Key implementation decisions:
- `factor_metadata_registry.json` bundled as package constant (loaded once at cold start via `os.path.dirname(__file__)`)
- `NON_SCORING_COLS` frozenset hardcoded from `source_headers_20251028.json` (identity + universe + admin columns)
- Scoring columns identified dynamically: any column in `df.columns` not in `NON_SCORING_COLS`
- `_compute_percentiles()` creates ONE copy of the universe DataFrame and adds all `{code}_pctl` columns to it (not one copy per factor)
- `_to_json_value()` helper handles numpy scalars, pd.NA, pd.NaT, float NaN/Inf — all become Python None before json.dumps
- No gzip (Phase 0)
- S3 writes: both `{asOf}/` and `latest/` paths for all outputs (factor_metadata, universe_data, scanner_data per universe)
- `country` always emitted as string (per SSCN_DATA_CONTRACT.md Section 10.4 recommendation; UI conditionally hides column)
- Error handling: invalid key pattern raises ValueError (fail fast); missing universe column logs WARN and skips (no full-run failure)

### 2. Requirements File

Created `infra/aws/lambda/opal_security_scanner_processor/requirements.txt`:
- `pandas`
- `openpyxl`
- boto3 NOT listed (provided by Lambda runtime)

### 3. Factor Metadata Registry

Created `infra/aws/lambda/opal_security_scanner_processor/factor_metadata_registry.json`
Copied canonical copy to `docs/architecture/security-scanner-source/factor_metadata_registry.json`

Registry covers all 284 scoring factor codes from `source_headers_20251028.json`.
11 categories: size, activity, growth, capital_allocation, profitability, quality, leverage, valuation, analyst, ownership, technicals.

**PHASE 0 LIMITATION:** `name`, `ic`, `coveragePct`, `autocorrelationPct`, `systematic` fields are
placeholders. `relationship` assignments (Positive/Inverse) are domain-knowledge-based, not sourced
from XLSM Tab 3. Must be updated from XLSM "3-Factor Data" sheet before production use.

The XLSM file (`Factor_Scanning_Model.xlsm`) was not in the repo during this session.
The XLSM audit (`SECURITY_SCANNER_XLSM_AUDIT.md`, 35,899 lines) contains Tab 3 structure
but not extracted cell values. The gap is documented here; registry must be validated when
the XLSM is accessible.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Bundle registry as package constant (not S3) | Small enough (~284 entries), simpler deployment, no runtime S3 call needed |
| Single `df_universe.copy()` in `_compute_percentiles` | Avoid N copies; one copy accumulates all pctl columns |
| Hardcode NON_SCORING_COLS | From confirmed source_headers_20251028.json; stable set; no runtime file needed |
| Always emit `country` as string (never null) | Per SSCN_DATA_CONTRACT.md Section 10.4 recommendation; UI hides column for US universes |
| `relationship` defaults to "Positive" for unknown codes | Defensively correct for most factors; logged as Phase 0 gap |
| AE deploys via Terraform | Per CLAUDE.md Rule 1 and task order constraints |

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| None required | Task order had full spec; AE task order already issued | N/A |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/opal_security_scanner_processor/lambda_function.py` | Created — SSCN processing Lambda | No — local only |
| `infra/aws/lambda/opal_security_scanner_processor/requirements.txt` | Created — pandas + openpyxl | No — local only |
| `infra/aws/lambda/opal_security_scanner_processor/factor_metadata_registry.json` | Created — 284-factor registry (Phase 0) | No — local only |
| `docs/architecture/security-scanner-source/factor_metadata_registry.json` | Created — canonical copy of registry | No — local only |

---

## Blockers

- AMBIGUOUS dependency: `0.5.0_AE_OpalETL` has no log folder at this time.
  SSCN_PORTAL.001-002.terraform-infra.md is in their task_orders but no log confirms status.
  AE deploys after DS delivers source code — DS delivery is now complete.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Lambda source, requirements, and factor metadata registry are written and ready for DT commit.
The three files at `infra/aws/lambda/opal_security_scanner_processor/` implement the full
SSCN_PORTAL-001 processing contract. Registry Phase 0 gap is documented: relationship
assignments are domain-knowledge-based and must be validated against XLSM Tab 3 before
production. DT must commit and AE must deploy via Terraform per `SSCN_PORTAL.001-002.terraform-infra.md`.

---

## Next Steps

1. **[0.3.0_DT_TradingOperations] Commit and push** `infra/aws/lambda/opal_security_scanner_processor/` to CLOUD branch, then signal `0.5.0_AE_OpalETL` that source is ready for Terraform deploy
2. **[0.5.0_AE_OpalETL] Deploy via Terraform** per `SSCN_PORTAL.001-002.terraform-infra.md` — Lambda source is now delivered
3. **[Future DS session] Populate registry from XLSM Tab 3** — when `Factor_Scanning_Model.xlsm` is accessible, extract `factor_metadata_registry.json` fields: name, category, relationship (authoritative), ic, coveragePct, autocorrelationPct, systematic. Update both `docs/architecture/security-scanner-source/factor_metadata_registry.json` and the Lambda package copy.

**Files to touch next:**
- `org/tier2_senior/0.3.0_DS_TradingOperations/task_orders/SSCN_PORTAL.001-002.processing-lambda.md` — mark status=complete

**Do NOT:**
- Deploy Lambda directly via `aws lambda update-function-code` — Terraform only (CLAUDE.md Rule 1)
- Add boto3 to requirements.txt — provided by Lambda runtime

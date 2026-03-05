# SSCN Processing Lambda Implementation — 0.3.0_DS_TradingOperations

**Date:** 2026-03-05
**Start Time:** Session start
**End Time:** Session end

## Objective

Implement the `opal-security-scanner-processor` Lambda source code per task order
`SSCN_PORTAL.001-002.processing-lambda.md`. Three rounds of work: initial implementation,
registry category correction from XLSM Tab 3, and sentinel-42 + country casing patch
discovered from DS file analysis of the actual FactSet upload.

---

## Work Completed

### 1. Initial Lambda Implementation — commit `3879941c`

Created `infra/aws/lambda/opal_security_scanner_processor/lambda_function.py`.

**Design decisions:**
- `factor_metadata_registry.json` bundled as a package constant loaded at cold start via `os.path.dirname(__file__)`
- `NON_SCORING_COLS` frozenset derived from `source_headers_20251028.json` (identity + universe + admin); scoring columns identified dynamically as all `df.columns` not in this set
- `_compute_percentiles()` does one `df_universe.copy()` then adds all `{code}_pctl` columns in a single loop — no per-factor copies
- `_to_json_value()` helper: handles numpy scalars, `pd.NA`, `pd.NaT`, `float` NaN/Inf → all become `None` before `json.dumps`
- V0 canonical percentile logic: `pd.to_numeric(errors='coerce')` → negate if `relationship == 'Inverse'` → `rank(pct=True, method='average') * 100`
- S3 writes: both `{asOf}/` and `latest/` paths for factor_metadata, universe_data, scanner_data (6 universes × 3 files = 18 write paths + 2 for factor_metadata = 20 S3 puts per run)
- Error handling: invalid key pattern → `ValueError` (fail fast); missing universe column → WARN + skip (no full-run failure)
- No gzip, no CloudFront invalidation (Phase 0)
- `country` always emitted as raw string (per SSCN_DATA_CONTRACT.md Section 10.4; UI hides column for US universes)

Created `requirements.txt`: `pandas`, `openpyxl` only. boto3 omitted (Lambda runtime).

Created initial `factor_metadata_registry.json` (284 factors, domain-knowledge category names, domain-knowledge relationship assignments).

---

### 2. Registry Category Correction from XLSM Tab 3 — commit `001fb7d6`

DE code review of `3879941c` flagged category name mismatch: DS used domain-derived names
instead of the contracted 11-category V0 taxonomy from `V0_SYSTEM_REFERENCE.md`.

**Source accessed:** `C:\Users\AndrewBerman\Desktop\Factor_Scanner.V0\Factor_Scanning_Model.xlsm`
Tab 3 "3-Factor Data" — 288 rows, 287 after cleanup, 284 matching the scoring factor list.

**Extraction method:** `pd.read_excel(xlsm, sheet_name='3-Factor Data', header=3, engine='openpyxl')`.
Skipped the "Filter" row at row 5; columns positionally indexed (col_0=Category, col_1=FactorName, col_2=FactorCode, col_3=Relationship, col_4=IC, col_10=Coverage(%), col_11=Autocorrelation(%)).

**Tab 3 actual categories (18):** efficiency, size, technical, short, crowding, momentum, value, management, profitability, insider, governance, quality, growth, solvency, analyst, beta, volatility, liquidity.

**Mapping to V0 contracted 11 categories:**

| XLSM Tab 3 | V0 contracted |
|---|---|
| efficiency | efficiency |
| size | size |
| technical, short, momentum, beta, volatility, liquidity | systematic |
| crowding, insider | institutional |
| governance | management |
| management | management |
| profitability | profitability |
| quality | quality |
| growth | growth |
| solvency | quality |
| analyst | sentiment |
| value (yield-form: ey/dy/fcfy/sp/ebitdaev/etc.) | yield |
| value (multiple-form: bp/tbp/peg/pegy) | value |

**Relationship corrections confirmed from XLSM Tab 3 data:**
- `bv`, `midcap`, `assets`: Positive → **Inverse** (size factors in V0 are inverse: smaller = better)
- `capex_depr`: Positive → **Inverse**
- `passive_pctout`: Positive → **Inverse**

**IC/coveragePct/autocorrelationPct:** Populated from Tab 3 for all 282 covered factors. 2 factors not in Tab 3 (`upbeta_252d`, `downbeta_252d`) inferred from their 63D counterparts (beta category, same relationship direction).

**Final category distribution:** efficiency(22), size(6), growth(25), management(22), profitability(21), quality(43), yield(20), value(6), sentiment(12), systematic(72), institutional(35) = **284**.

---

### 3. FactSet Sentinel-42 Patch + Country Casing — commit `82463f79`

DS analysis of the actual FactSet upload file confirmed two additional issues:

**Sentinel 42:** FactSet uses `42` as the N/A sentinel across ALL numeric columns — both scoring factor columns (`short_pct: 42`, `days_to_cover: 42`) and universe weight columns (`wt_ivv: 42` = not-in-universe). Without replacement, rows with `wt_{etf}=42` incorrectly satisfy `df[universe_col] > 0` and are included as universe members. Factor values of 42 are also emitted as `42.0` instead of null.

Fix: `df = df.replace(42, float("nan"))` immediately after `pd.read_excel()`, before the universe membership filter.

**Country casing:** `country_name` in the FactSet export is UPPERCASE (`UNITED STATES`, `GERMANY`). Applied `.title()` in `_build_universe_rows()` and `_build_scanner_rows()` for readable display (`United States`, `Germany`). Decision logged in SSCN_DATA_CONTRACT.md Section 10.6.

Both findings documented in task order POST-COMPLETE ADDENDUM and SSCN_DATA_CONTRACT.md Sections 7, 8, 10.5, 10.6.

---

### 4. Downstream Check

`0.3.0_DT_TradingOperations` received the Lambda source and committed the portal pointer advance + task order updates in `7a341fc6`. DT is unblocked.

`0.5.0_AE_OpalETL` terraform-infra task order is in their `task_orders/` folder; no log folder exists yet — status AMBIGUOUS.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Bundle registry as package constant | 284 entries × ~200 bytes = ~56 KB; fits in Lambda package; no runtime S3 call |
| Single `df_universe.copy()` in `_compute_percentiles` | One copy per universe, all pctl columns added in-place |
| Hardcode NON_SCORING_COLS | Stable set from confirmed source_headers_20251028.json |
| `df.replace(42, float("nan"))` before universe filter | FactSet sentinel must be cleared before membership test or non-members are incorrectly included |
| `.title()` on country_name | UPPERCASE country names in FactSet export are unreadable; DE/RD confirmed title-case preferred |
| XLSM Tab 3 as authoritative category source | V0_SYSTEM_REFERENCE.md gives contracted taxonomy names; Tab 3 gives per-factor assignments |
| solvency → quality | Debt/coverage ratios = financial health quality per V0 logic |
| governance → management | Board composition = management quality per V0 logic |
| liquidity (XLSM) → systematic | Trading liquidity metrics (lix, bid_ask_spread, atvr) are systematic market factors |

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| None required | Task order had full spec; DE data contract updates handled by DE | N/A |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/opal_security_scanner_processor/lambda_function.py` | Created + patched (sentinel-42, country.title()) | Yes — `3879941c`, `82463f79` |
| `infra/aws/lambda/opal_security_scanner_processor/requirements.txt` | Created — pandas + openpyxl | Yes — `3879941c` |
| `infra/aws/lambda/opal_security_scanner_processor/factor_metadata_registry.json` | Created (Phase 0) → replaced with XLSM Tab 3 data | Yes — `3879941c`, `001fb7d6` |
| `docs/architecture/security-scanner-source/factor_metadata_registry.json` | Created (Phase 0) → replaced with XLSM Tab 3 data | Yes — `3879941c`, `001fb7d6` |
| `org/tier2_senior/0.3.0_DS_TradingOperations/task_orders/SSCN_PORTAL.001-002.processing-lambda.md` | Marked status=complete + POST-COMPLETE ADDENDUM | Yes — `3879941c` (status), task order modified locally after |
| `org/daily_log/2026-03-05.md` | Added DS session entries (initial + follow-up) | Yes — via `4f6b5a5a` housekeeping |

---

## Blockers

- AMBIGUOUS: `0.5.0_AE_OpalETL` has no log folder. Their terraform-infra task order is present; no evidence of work started or blocked. DS source is delivered; AE is unblocked from DS side.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Three commits on CLOUD from this session: `3879941c` (initial), `001fb7d6` (registry fix), `82463f79` (sentinel patch). Lambda source, requirements, and registry are production-ready pending AE Terraform deploy. SSCN_DATA_CONTRACT.md Sections 10.5 and 10.6 updated by DE with file-analysis findings. DT (`7a341fc6`) has pushed CLOUD and advanced portal pointer. AE is the last gate before the Lambda is live.

---

## Next Steps

1. **[0.5.0_AE_OpalETL] Deploy via Terraform** per `SSCN_PORTAL.001-002.terraform-infra.md` — Lambda source is delivered and committed
2. **[0.3.0_DE_TradingOperations] Wire portal proxy routes** per `SSCN_PORTAL.001-002.shared-utils-extraction-proxy-routes.md`
3. **[0.3.4_RD_SecurityScanner] Implement page** per design contract and `SSCN_PORTAL.001-002.page-implementation.md`

**Files to touch next (if DS is called back):**
- `infra/aws/lambda/opal_security_scanner_processor/lambda_function.py` — any further contract changes from AE/DE testing
- `docs/architecture/security-scanner-source/factor_metadata_registry.json` — if Tab 3 `systematic` field needs populating per Section 10.3

**Do NOT:**
- Deploy Lambda via `aws lambda update-function-code` — Terraform only (CLAUDE.md Rule 1)
- Add boto3 to requirements.txt — provided by Lambda runtime
- Add gzip or CloudFront invalidation — Phase 0 exclusion, locked in SSCN_DATA_CONTRACT.md Section 9

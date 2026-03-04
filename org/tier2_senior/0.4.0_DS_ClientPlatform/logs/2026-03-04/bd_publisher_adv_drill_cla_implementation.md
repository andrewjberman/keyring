# ADVI-004 A1+A2 + ADVI-005 A3 Implementation — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-04
**Start Time:** session start
**End Time:** in progress

## Objective

Work through the A-roll task orders in sequence: ADVI-004 (adv_drill + cla in bd-portal-publisher
Lambda) and ADVI-005 (stacked_bar + rolling_1y in gold script 10). Also assessed DC task order
on startup. A4 (script 09 bell curve verification) and A5 (opal-users-v2 investigation) remain.

---

## Work Completed

### 1. DC Task Order — Startup Assessment

Read `data_contract.md` task order. Status was already `complete` (issued 2026-03-02; baseline
contract creation). data_contract.xml at `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/`
was adequate to begin A1+A2: timeseries_chart.json Source 2 block existed but had no adv_drill
or cla entries. Those are added by A1+A2's own DC.1 requirement, not the DC task order.

### 2. ADVI-004 A2.0 Pre-Check: primary_city Confirmed in Script 04

Read `data/black_diamond/scripts/gold/04_build_client_dimension.py`.
- `primary_city` is defined in the schema comment at line 17.
- Written to output at lines 267-268 via `modal_value(grp['_city'])`.
- The Lambda's `load_all()` did NOT include `primary_city` in its cdim column prune.
- Conclusion: `cla.geo_city_drill` is a Lambda-only change — no gold-layer enhancement needed.
  This validates the CTO scope correction in the ADVI-004 task order.

### 3. ADVI-004 A1: adv_drill in bd-portal-publisher

Modified `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py`.

Changes:
- Added constants `TOP_N_CLIENTS_PER_ARCH = 8` and `MAX_CLA_CITIES = 9`.
- Added `primary_city` to cdim column prune in `load_all()`.
- Expanded `perf_cohort` merge in `build_timeseries_chart()` to pull
  `relationship_name, primary_architect, primary_state, primary_city` from cdim
  (one merge serves all new views — no second parquet load).
- Added `adv_drill` computation block: iterates `adv_categories` (excl "Other");
  for each architect finds top 8 clients by latest-day AUA from `perf_cohort`;
  category key = `"{relationship_name} ({relationship_id})"` (collision-safe per contract).
- adv_drill keys match `adv.categories` strings exactly (portal drillParent lookup requirement).
- `adv_drill` added to result conditionally (omit if empty).

Contract ref: ADVI-004 Pattern 0 thread receipt, DS turn 7 (converge).

### 4. ADVI-004 A2: cla in bd-portal-publisher

Added `cla` dict to `build_timeseries_chart()` in same file.

Sub-views:
- `cla.total`: firm-wide NMNC/NMEC AUA; reuses `perf_cohort.cohort` already computed.
- `cla.geo_drill[state]`: per-state NMNC/NMEC AUA; keys match `geo.categories` exactly.
- `cla.adv_drill[arch]`: per-architect NMNC/NMEC AUA; keys match `adv.categories` exactly.
- `cla.geo_city_drill[state][city]`: NMNC/NMEC AUA per city using `cdim.primary_city`;
  top 9 cities per state by latest-day AUA. Optional — omitted if no city data.

NMNC/NMEC rule: trailing-12-month vintage (`months_since_first <= 12`), same formula
as the existing `aua` view in `build_timeseries_chart()`. No new classification introduced.

Helper `_cla_view(df_subset)` added to DRY the groupby/unstack pattern across all 4 sub-views.

Contract ref: ADVI-004 Pattern 0 thread receipt + CTO task order A2.0-A2.3.

### 5. ADVI-004 DC.1: data_contract.xml Updated

Added `adv_drill` and `cla` key definitions to the timeseries_chart.json Source 2 block in
`data_contract.xml`. Documented: structures, category key format, TOP_N_CLIENTS_PER_ARCH,
NMNC/NMEC rule with exact formula, sign conventions, source parquet references, primary_city
derivation with script 04 line citations, geo_city_drill feasibility basis.
Also updated `<date>` to 2026-03-04 and added source_note about the 2026-03-04 extensions.

Syntax verified: `ast.parse()` clean. Committed at `5f60d30e`.

### 6. DT Brief Written for Stream B1

Wrote `docs/briefs/devops-brief-advi-004-adv-drill-cla.md` for `0.4.0_DT_ClientPlatform`.
Covers: what changed, build-and-upload.sh command, terraform plan/apply sequence,
verification steps, next tag `bd-v2.15.0`. Committed at `f2e3c675`.

### 7. ADVI-005 A3.0 Pre-Check: Data History Confirmed

Could not query S3 directly (AWS CLI hanging in Git Bash on Windows). Resolved via session
log archaeology:
- `logs/sessions/2026-02-27/data_scientist/partner_analytics_09_script_implementation.md`:
  "client_performance has exact daily data back to 2020-06-30"
- `logs/sessions/2026-02-26/data_scientist/partner_analytics_new_script_design_task_order.md`:
  "for every day back to 2020-06-30"
- `nna_aua_by_advisor.parquet` is derived from same positions cube — same inception date.

Findings documented:
- Data inception: **2020-06-30**. Data range: ~5.5 years.
- First valid 1Y rolling point: ~2021-07-01 (after 1Y warmup).
- 3Y and Max stacked_bar coverage: **complete** — data exceeds required 4Y lookback.
- No history caveat needed; all 5 stacked_bar periods fully supported.

### 8. ADVI-005 A3.1: stacked_bar in script 10

Modified `data/black_diamond/scripts/gold/10_generate_advisor_rolling_flows.py`.

Added:
- `STACKED_BAR_PERIODS = ('qtd', 'ytd', '1y', '3y', 'max')` constant.
- `compute_stacked_bar()` function:
  - Computes period boundaries: qtd/ytd via `_get_period_boundaries()`;
    1y/3y via trailing Timedelta(365/1095 days); max via parquet inception date.
  - Calls existing `_compute_nna_for_range()` per period — no new data logic.
  - Returns `{period: [AdvisorBarEntry]}` for a single role.
  - `AdvisorBarEntry`: `{advisor_name, advisor_id, inflows, outflows, nna_net}`.
  - `outflows` positive magnitude. `nna_net` signed.
- Assembled into period-outer / role-inner structure per CTO task order A3.1 correction:
  `stacked_bar = { period: { 'architects': [...], 'implementors': [...] } }`
  Note: this differs from thread receipt (role-outer); task order is the binding spec.

### 9. ADVI-005 A3.2: rolling_1y in script 10

Added `rolling_1y` dict extracted from existing `compute_rolling_series()` 1Y window output.
- `rolling_1y.architects`: list of `{advisor_name, advisor_id, series: [{date, nna, inflows, outflows}]}`
- `rolling_1y.implementors`: same shape.
- Full history emitted; frontend slices x-axis by period toggle.
- No new rolling computation — reuses series['1Y'] already produced.
- Point fields `{date, nna, inflows, outflows}` match `Rolling1YDataPoint` contract exactly.

### 10. ADVI-005 A3.3: Backward Compatibility

All legacy keys (`generated_at`, `data_as_of`, `firm_id`, `summary`, `architects`,
`implementors` with 30d/90d/1Y windows) are unchanged. `stacked_bar` and `rolling_1y`
are additive top-level keys. Dry-run preview block updated to show both new keys.

### 11. ADVI-005 DC.1: data_contract.xml Updated

Replaced the thin Source 5 (advisor_rolling_flows) entry with a full documented block:
- Script source (EC2 gold script, not Lambda).
- Data history block: 2020-06-30 inception, 5.5Y range, first 1Y point ~2021-07-01, 3Y/Max complete.
- Legacy key schema for summary/architects/implementors.
- stacked_bar: full structure, AdvisorBarEntry fields, period boundary definitions, sign convention.
- rolling_1y: AdvisorRolling1YSeries structure, daily cadence, all 3 fields, rolling method.

Syntax verified. Committed at `c9b3ab76`.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Expand perf_cohort merge (not a separate join) | One merge serves A1 + all CLA sub-views; no extra parquet load |
| _cla_view() helper | 4 CLA sub-views share identical groupby/unstack/fill pattern |
| Iterate adv_categories (not top_architects) for adv_drill | adv_categories is the portal's drillParent key source — must match exactly |
| adv_drill and geo_city_drill both conditional | Omit if empty, consistent with existing geo_drill pattern |
| Period-outer/role-inner for stacked_bar | CTO task order A3.1 explicitly overrides thread receipt (role-outer) |
| rolling_1y reuses series['1Y'] directly | No new rolling math needed; existing output matches contract exactly |
| Data history via session log archaeology (not live S3 query) | AWS CLI hanging in Git Bash on Windows; session logs have confirmed the 2020-06-30 date |
| A4: no patch needed — signed percentiles are intentional | `calculate_nna_distribution_stats()` docstring and bin design confirm signed distribution is correct; abs() is present where it matters (materiality filter, bin construction) |
| A4.2 deferred — code verification sufficient | S3 live check is data sanity only; no patch warranted by code analysis; remain blocked by AWS CLI until that is resolved |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py` | TOP_N_CLIENTS_PER_ARCH + MAX_CLA_CITIES; primary_city to cdim; expanded perf_cohort merge; adv_drill + cla blocks; adv_drill/cla added to result | Yes — `5f60d30e` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/data_contract.xml` | adv_drill + cla doc in timeseries_chart.json Source 2; adv_rolling_flows Source 5 fully documented with A3 shapes | Yes — `5f60d30e`, `c9b3ab76` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI-004-adv_drill_cla.md` | Status: pending -> complete | Yes — `5f60d30e` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI-005-rolling_flows_data.md` | Status: pending -> complete | Yes — `c9b3ab76` |
| `data/black_diamond/scripts/gold/10_generate_advisor_rolling_flows.py` | STACKED_BAR_PERIODS constant; compute_stacked_bar(); rolling_1y extraction; both added to return dict; dry-run preview extended | Yes — `c9b3ab76` |
| `docs/briefs/devops-brief-advi-004-adv-drill-cla.md` | New — DT Stream B1 deploy instructions | Yes — `f2e3c675` |
| `docs/briefs/devops-brief-advi-005-rolling-flows.md` | New — DT Stream B2 EC2 deploy instructions | Yes — `75b3b83f` |

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| DT deploy — bd-portal-publisher (Stream B1) | `docs/briefs/devops-brief-advi-004-adv-drill-cla.md` | 0.4.0_DT_ClientPlatform |
| DT deploy — script 10 EC2 (Stream B2) | `docs/briefs/devops-brief-advi-005-rolling-flows.md` | 0.4.0_DT_ClientPlatform |

---

### 12. ADVI A4.1: Script 09 Bell Curve Code Verification

Read `data/black_diamond/scripts/gold/09_generate_partner_analytics.py`.

Note: the task order referenced `09_build_distribution_stats.py` — the actual filename is
`09_generate_partner_analytics.py`. The file contains the full partner analytics script
including distribution stats functions.

**A4.1 — Function located:**
- `calculate_nna_distribution_stats(nna_values: pd.Series)` — line 320
- This is the bell curve / distribution stats function for per-relationship period NNA

**abs() handling verified present:**

| Location | Line | Code | Purpose |
|----------|------|------|---------|
| Materiality filter | 332 | `vals = vals[vals.abs() >= NNA_MATERIALITY_THRESHOLD]` | Excludes sub-$1K NNA accounts (fees, dividends, rounding noise) |
| Bin max | 348 | `abs_max = float(vals.abs().max())` | Log-spaced bin upper bound from largest magnitude (pos or neg) |
| Bin min | 349 | `abs_min = max(float(vals.abs().min()), 1_000)` | Log-spaced bin lower bound floored at $1K |
| Symmetric bins | 353-357 | `neg_edges = -pos_edges[::-1]` mirrored around zero | Both inflows (positive) and outflows (negative) visible in histogram |

**Percentile design:** Percentiles at lines 374-380 are SIGNED (not abs()). This is
intentional — the function docstring states "signed, symmetric log bins." For a mixed
distribution: p10 reflects the 10th-percentile NNA value (could be large negative for
outflow-heavy segments); p90 reflects the 90th-percentile (typically positive inflow).
Signed percentiles correctly convey the shape of a bimodal inflow/outflow distribution.

**Commit attribution:** The abs() handling landed across two commits after 8247c6d0:
- `792b4e05`: Added `calculate_nna_distribution_stats()` with symmetric log bins + abs() for bin construction
- `9216c922` (2026-03-03): Added `NNA_MATERIALITY_THRESHOLD = 1_000` and abs() materiality filter

All three commits predating the A4 task order (2026-03-03). The fix is present in current CLOUD HEAD.

**A4.2 — S3 verification: BLOCKED**
Cannot read `s3://opal-data-bd/gold/partner_analytics/header_metrics.json` — AWS CLI
non-functional in Git Bash on Windows (hangs with "File association not found for extension .py").
Actual P10/P25/Median/P75/P90 threshold values not confirmed from live data.

**A4.3 — Assessment:** Code analysis confirms the abs() fix landed. No patch needed.
A4.2 remains open pending AWS CLI resolution.

---

### 13. Stream B2 DT Brief Written

Wrote `docs/briefs/devops-brief-advi-005-rolling-flows.md` for `0.4.0_DT_ClientPlatform`.
Covers: what changed (script 10 only, no infra changes), safe-ec2-deploy.sh command,
EC2 start command for incremental run, verification via S3 JSON key check, next tag `bd-v2.15.1`.
Notes: run_gold_layer.sh incremental mode runs 02-10 sequentially — only script 10 output changes.
Does NOT trigger pipeline-complete to re-run on its own; EC2 boot triggers the run automatically.
Committed at `75b3b83f`.

---

## Blockers

- AWS CLI non-functional in Git Bash on Windows (hangs with "File association not found for
  extension .py"). Affects:
  - A4.2: cannot read header_metrics.json from S3 to confirm live distribution threshold values
  - A5: opal-users-v2 DynamoDB investigation requires live AWS CLI reads
  Must resolve before either can be fully closed.

---

## Current State

**Status:** IN PROGRESS (A1+A2+A3 complete; A4 code-verified/S3-blocked; B2 brief complete; A5 blocked)
**Active branch:** `CLOUD`

Three task orders complete this session: ADVI-004 (A1+A2) at `5f60d30e` and ADVI-005 (A3)
at `c9b3ab76`. Both commits local on CLOUD. data_contract.xml updated in both — DT deploy
gates satisfied. DT briefs written for both streams:
- Stream B1 (bd-portal-publisher Lambda): `docs/briefs/devops-brief-advi-004-adv-drill-cla.md` (commit `f2e3c675`)
- Stream B2 (script 10 EC2): `docs/briefs/devops-brief-advi-005-rolling-flows.md` (commit `75b3b83f`)
A4 code-verified: abs() fix confirmed present in `calculate_nna_distribution_stats()` at line 320.
A4.2 (S3 live-data check) and A5 blocked by AWS CLI issue.

---

## Next Steps

> Ordered by priority.

1. **[0.4.0_DT_ClientPlatform] Deploy Stream B1 — bd-portal-publisher** (commit `5f60d30e`)
   Full instructions: `docs/briefs/devops-brief-advi-004-adv-drill-cla.md`.
   Next tag: `bd-v2.15.0`.

2. **[0.4.0_DT_ClientPlatform] Deploy Stream B2 — script 10 EC2** (commit `c9b3ab76`)
   Full instructions: `docs/briefs/devops-brief-advi-005-rolling-flows.md`.
   Next tag: `bd-v2.15.1`.

3. **[0.4.0_DS] A4.2 — Script 09 S3 live data verification** (BLOCKED by AWS CLI)
   Once AWS CLI functional: read `s3://opal-data-bd/gold/partner_analytics/header_metrics.json`.
   Inspect `views.nna.current.distribution.total.percentiles` and `views.nna.current.distribution.by_segment`.
   Confirm P10/P25/Median/P75/P90 are non-degenerate (non-zero, non-symmetric, reflect real data).
   No patch expected — code analysis confirms correct. This is a data sanity check only.

4. **[0.4.0_DS] A5 — opal-users-v2 DynamoDB investigation** (BLOCKED by AWS CLI)
   Requires working AWS CLI. Fix AWS CLI in Git Bash first (try aws.cmd or Python invoke).
   Inspect table schema and sample records. Determine JWT->advisor mapping scenario (a/b/c).

**Files to touch next:**
- None on DS side pending AWS CLI resolution.

**Do NOT:**
- Re-enable `build_partner_analytics()` in bd-portal-publisher lambda_handler (DISABLED intentionally).
- Change stacked_bar nesting to role-outer/period-inner (thread receipt shape) — CTO task order is binding.
- Modify existing aua/nna/geo/adv/geo_drill keys in timeseries_chart.json.
- Run `02_build_positions_cube.py --start-date` (known to corrupt data; full rebuild only if needed).

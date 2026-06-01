# Macro Page "May-blank / June-filled" — Root-Cause Trace (AE OpalETL)

**Author:** 0.5.0_AE_OpalETL · **Date:** 2026-06-01 · **Trigger:** Andrew-direct (ws CTO TO 20260601T165112Z, CC COO)
**Anomaly:** portal Macroeconomics page — all of MAY 2026 BLANK for the monthly sections (Consumer, Housing, Inflation, Leading, Lagging, most of Labor + Financial Condition), YET JUNE 2026 FULLY FILLED, despite source data only reaching May 29 (monthly indicators latest = April).
**Verdict: CONFIRMED root cause = month-name-without-year keying colliding with a ~12-month window on the wraparound. CTO hypothesis #1 (period-labeling), precise mechanism below. NOT forward-fill, NOT source/serving mismatch, NOT a data-pull bug — the underlying data is correct (monthly series correctly end at April).**

## Data ground-truth (canonical, today = 2026-06-01)
- Per-slug timeseries JSON (`json/macro/timeseries/{slug}.json`) is CLEAN: monthly indicators end at `2026-04-30` (end-of-month dates), `as_of: 2026-04-30`. No May, no June entries. Data pull is correct.
- Table JSON (`json/macro/macro_data.json`, `data_as_of: 2026-05-29`) keys each indicator's `values` by **bare month name, no year**: e.g. Leading Index = `{"Jun":-4.0, "Jul":-3.5, ..., "Mar":-3.1, "Apr":-1.7}` = Jun **2025** → Apr **2026** (11 entries; no May; latest April).

## The two colliding pieces
1. **Producer** `infra/aws/lambda/v2_portal/yang_pipeline/macroeconomics/yang-generate-macro/lambda_function.py`:
   - L387 `get_last_12_months`: window = `as_of_date − 11 months` → with as_of `2026-05-29`, spans **Jun'25 → May'26** (~12 month-buckets).
   - **L439/L442 (THE BUG):** `month_name = month_names[row['date'].month - 1]; values[month_name] = {...}` — keyed by **bare month name, NO YEAR**. So `values["Jun"]` = June **2025**'s value.
2. **FE** `portal/src/pages/Macroeconomics/panels/MacroHeatmap.tsx`:
   - L34-54 `getTrailing12Months()` builds columns from `const now = new Date()` (= June 2026) → `Jul'25, Aug'25, ..., Apr'26, May'26, Jun'26` (last column = current month).
   - Fills each column by `values[monthName]` — **bare month-name lookup.**

## The collision (simulated against the live macro_data.json — Leading Index)
| FE column | looked-up key | value shown | correct? |
|---|---|---|---|
| Apr '26 | `values["Apr"]` | -1.7 (Apr'26) | ✓ latest real |
| **May '26** | `values["May"]` | **BLANK** | no "May" key in the Jun'25–Apr'26 window → blank |
| **Jun '26** | `values["Jun"]` | **-4.0 = June *2025*'s value** | ✗ **stale year-old data in the current-month column** |

The ~12-month window makes the OLDEST entry's month-name (Jun'25) equal the CURRENT-month column's name (Jun'26). Bare-month keying maps the year-ago value into the current-month cell → "June fully filled." May has no key (window starts Jun'25; May monthly data not yet released) → "May blank." **Monthly-only** because high-frequency series (Initial/Continuing Jobless Claims, Bloomberg/Chicago-Fed FCI, Fed Balance Sheet) carry real May-dated observations, so their May cells populate and the year-ago collision is masked by intervening same-month entries / dated handling.

## Proposed in-pattern fix (NOT applied — per CTO read-first directive)
**Year-qualify the month key on BOTH sides (the only robust fix — bare month-name cannot disambiguate same-month-different-year within a 12-month window):**
1. **Producer (mine, yang-generate-macro L437-444):** key `values` by `row['date'].strftime('%Y-%m')` (e.g. `"2026-04"`) instead of `month_names[...]`. Or emit each entry with an explicit `year` field.
2. **FE (RD/DE lane — I cannot commit portal):** `getTrailing12Months()` already computes `{month, year}`; change the cell lookup to a `YYYY-MM` key (or `{year,month}` match) instead of bare `month`.
   - Result: `Jun'26` column → no `"2026-06"` key → correctly BLANK (no June monthly data); `Apr'26` → `"2026-04"` fills; `Jun'25` data sits in the (off-grid) past, never in `Jun'26`.
**COORDINATION (critical):** these MUST ship together — a producer-only switch to `YYYY-MM` keys breaks the current bare-month FE lookup (every cell blank). Options: (a) coordinated same-window producer+FE deploy, or (b) additive transition — producer emits a parallel year-qualified map alongside the legacy bare-month map, FE migrates to it, then drop the legacy map. Recommend (a) if RD/DE can co-deploy; (b) if not.
**Secondary note:** even after the fix, the current-month column (June) will be legitimately blank for monthly indicators until each month's release lands — which is the truthful display. Confirm with Andrew that a blank current-month cell (vs showing "latest = April") is the desired UX.

## Lane / ownership
- Producer `yang-generate-macro` = AE OpalETL (me) — I can patch + redeploy via the Lambda TF path once the fix is ruled + coordinated with the FE.
- FE `MacroHeatmap.tsx` = portal (RD/DE) — I cannot commit portal frontend; flag to RD/DE for the matching lookup change.
- Reference: org/projects/YALP_MACROS.json (Phase 2 multi-source RE; this bug is in the EXISTING yang macro producer + FE, independent of the Phase-2 RE harness).

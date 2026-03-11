# ADVI_PSCFIX A2: Publisher Restructure — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-11
**Start Time:** session start
**End Time:** session end

## Objective

Implement task order ADVI_PSCFIX.A2: restructure `bd-portal-publisher` Lambda to (1) replace
rolling-12M NMNC/NMEC classification with static period-bound definition, (2) output
pre-aggregated quarterly/monthly/annually AUA data instead of a daily rolling series, and
(3) apply certified_aua overrides to all `total_aua` fields when certification JSON is present.

---

## Work Completed

### 1. New Helpers Added

**`_load_aua_certification(today_str)`**
- Loads `gold/aua_certification/{today}.json` from S3
- Non-blocking: returns None on any exception (NoSuchKey, network, etc.)
- Logs: loaded with certified_aua/gold_aua/gap_pct, or "absent -- using gold totals"

**`_build_static_aua_periods(perf, cdim)`**
- Computes static period-bound NMNC/NMEC for quarterly, monthly, annually
- For each period P: NMNC = clients whose `first_seen_date` in [period_start, period_end];
  NMEC = all others active at the period_end snapshot
- Period_end for in-progress period = `perf.date.max()`; for completed periods = last calendar
  day of the period
- Snapshot date: last available perf date <= period_end (handles missing dates gracefully)
- Rolling/gradient NMNC definition preserved as code comment — not wired to any output
- NMNC + NMEC == total_aua at period_end for every period (float precision guarantee)
- Output shape: `{quarterly: {categories, data}, monthly: {categories, data}, annually: {categories, data}}`
- Each data entry: `{period, label, end_date, NMNC, NMEC}`

### 2. `build_timeseries_chart` Restructured

- Added `cert: dict = None` parameter
- Replaced old daily rolling `aua_data` array with call to `_build_static_aua_periods()`
- Rolling cohort classification (`months_since_first <= 12`) kept active for `cla` sub-views
  (ADVI-004 A2); annotated clearly as the rolling definition, not used for aua view
- `aua` key in result is now `aua_periods` dict (quarterly/monthly/annually sub-keys)
- Old flat `aua.data` and `aua.categories` top-level keys are gone
- Cert override: when cert present, scale last entry in each granularity so NMNC+NMEC == certified_aua

### 3. `build_header_metrics` Updated

- Added `cert: dict = None` parameter
- When cert present: `total['aua'] = cert['certified_aua']` (NNA fields untouched — flow metrics)
- Print statement logs both display AUA and gold AUA for audit trail

### 4. `build_snapshots` Updated

- Added `cert: dict = None` parameter
- `total_aua` for architect, tax_status, state, region responses:
  - When cert present: `total_aua = cert['certified_aua']` (replacement, not scaling)
  - Segment-level `aua` values unchanged
  - `aua_pct` per segment recomputed against certified total (denominator change)
- State snapshot `total_aua` now uses certified value (previously used `state_total` — top-N sum)

### 5. `lambda_handler` Updated

- Cert loaded once after parquets: `cert = _load_aua_certification(today.strftime('%Y-%m-%d'))`
- Passed as `cert=cert` to `build_timeseries_chart`, `build_header_metrics`, `build_snapshots`
- `results['aua_certification']` = 'applied' or 'absent (gold totals)' for CloudWatch visibility
- Return body uses `display_aua` (certified when available)

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Keep rolling cohort code active for `cla` | `cla` sub-views use rolling NMNC; removing it would break them. Comment documents the two-definition system. |
| Pass cert to builders as optional kwarg | Non-breaking: existing callers still work. Fallback is gold totals when None. |
| State snapshot `total_aua`: use certified, not state_total | Task order says all 4 snapshots use certified_aua as top-level total. State segment pcts use state_total denominator internally (segment-level AUA unchanged). |
| No changes to `cla`, `adv`, `geo`, `nna`, `growth_decomposition` | Requirement 4 explicitly preserves these. |
| Script 09 cert override is out of scope | Scope lists only publisher lambda. PRD notes script 09 also needs cert override for donut totals — flagged in handler comment as pending separate deliverable. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py` | Static NMNC/NMEC + certified_aua override | Yes — `ea832f51` |

---

## Briefs Written

None. DE is implementing the portal side in parallel (already has the schema from the PRD).
No additional data contract brief needed — output shape is fully specified in the PRD and task order.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Publisher commit `ea832f51` on CLOUD implements all three A2 requirements: static period-bound
NMNC/NMEC at quarterly/monthly/annually granularities in `timeseries_chart.json aua`; certified_aua
override on `summary/header_metrics.json total.aua` and all four `snapshots/aua_by_{dim}.json
total_aua`; non-blocking cert load. Dependency A1 (script `05d`, AE) not yet deployed — publisher
will fall back to gold totals until cert JSONs appear. Task order marked complete.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Deploy publisher Lambda** — commit `ea832f51` is ready for deploy.
   No new Lambda Layer needed. Standard bd-pipeline deployment via `build-and-upload.sh` then
   `terraform apply`. Reference: `docs/briefs/` if DT needs a deploy brief (can be written on request).

2. **[0.6.0_AE_PartnerETL] Deploy script 05d** — produces `gold/aua_certification/{date}.json`
   which activates the cert override in the publisher.

3. **Script 09 cert override** — `09_generate_partner_analytics.py` also needs
   `views.aua/geo/adv.current.donut.total = cert['certified_aua']` per PRD Deliverable 3.
   This was out of scope for A2 (publisher only). Needs a separate task order to DS or AE.

**Files to touch next:**
- None for this agent. Work is complete.

**Do NOT:**
- Modify `cla` sub-views — they correctly use rolling NMNC for their purpose
- Apply cert override to NNA fields in header_metrics (`nna_ytd`, `nna_qtd`, etc.) — those are flow metrics
- Attempt to deploy the Lambda — that is DT's responsibility

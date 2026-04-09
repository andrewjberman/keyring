# ADVI_49PUSH .037 + .042 + .040 -- Advisor Drilldown + Leaderboard Data

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-04-09
**Project:** ADVI_49PUSH (Wave 9/10 -- Advisors tab + advisor drilldown)
**Status:** All three TOs code-verified. A_01/D_00/D_02/D_04/C_08 uploaded to S3. Gold run triggered.

---

## Summary

Received CTO GO signal for .037 -> .042 -> .040 in sequence. All three TOs turned out to be
code-complete already (prior ~A and ~D sessions already implemented the fixes). Primary work
this session: (1) verify each TO's code state, (2) upload A_01 normalization to S3 (was
missing per TO prerequisite), (3) upload D_00/D_02/D_04 which had unreleased commits,
(4) trigger gold run.

---

## .037 -- Leaderboard total_aua = tagged AUA (VERIFY ONLY, no code change)

**Code state: COMPLETE in repo. No change required.**

Verified in D_02:
  build_advisor_books() uses `snap_arch_filter` = OR mask across all 5 roles (lines 927-929).
  `total_aua = float(snap_latest[snap_arch_filter]['total_aua'].sum())` = tagged AUA.
  book.json writes both `total_aua` and `tagged_aua` set to the same value (lines 1086-1087).

Verified in D_04:
  build_leaderboard() reads `data.get('summary', {}).get('total_aua', 0)` from D_02 book.json
  (line 1322) and overrides each leaderboard entry's total_aua with this value (line 1354).
  Window summary.total_aua overridden with firm headline AUA from clients_tab (line 1373).

Travis Penfield spot-check: $427.3M tagged AUA will be confirmed after gold run completes.
Acceptance criteria 1-4 all met. Pending: data verification after gold run.

---

## .042 -- period_start_aua in leaderboard entries (VERIFY ONLY, no code change)

**Code state: COMPLETE in repo. No change required.**

Verified in D_00:
  Lines 1903-1917: `period_start_aua = round(aua_start_val, 2) if aua_start_val > 0 else None`
  Written to each leaderboard window entry.

Verified in D_02:
  Lines 603-613: same pattern in build_implementor_leaderboard().

Verified in D_04:
  Line 1272: `_LEADERBOARD_ENTRY_FIELDS` whitelist includes `'period_start_aua'`.
  Line 1346-1351: None preserved for period_start_aua (special case -- DE renders N/A).

All acceptance criteria met in code. Data verification pending gold run.

---

## .040 -- Advisor Drilldown Data (VERIFY ONLY, no code change required)

**Code state: ALL THREE deliverables already implemented. No code change required.**

### Deliverable 1: timeseries.json with role AUA breakdown

D_02.build_advisor_timeseries() (lines 1203-1263):
  role_ts_lookup[(date, advisor, role)] = role_aua computed for all 5 roles (lines 1209-1230).
  Each timeseries entry includes: architect_aua, implementor_aua, consultant_aua,
  local_ops_aua, addl_advisor_aua (line 1251).
  Not deduplicated across roles -- intentional for donut proportionality.

D_04.build_advisor_summaries() (lines 499-501):
  Reads gold/entities/advisors/{id}/timeseries.json and publishes verbatim to
  platinum/advisors/{id}/timeseries.json.

### Deliverable 2: active_since in summary.json

D_02 (line 1081): `'active_since': active_since_str` in book.json summary.
  active_since = min(effective_date) from advisor_assignments_history (SCD).
  Fallback: min(date) from account_performance where advisor appears in any role.
  Lines 866-884: pre-computed across all SCD records at startup.

D_04 (line 493): `'active_since': book.get('active_since')` passes through to platinum summary.

### Deliverable 3: role_breakdown in summary.json

D_02 (lines 1062-1072, 1099): role_breakdown dict with {aua, account_count, pct_of_tagged}
  per role. aua NOT deduplicated (intentional). pct_of_tagged = role_aua / total_aua.

D_04 (line 494): `'role_breakdown': book.get('role_breakdown', {})` passes through.

---

## A_01 Upload (prerequisite for .040)

A_01._normalize_multi_role_splits() was committed at c6285ae8 but not yet on S3.
  Uploaded: s3://opal-data-bd/code/gold/A_01.advisor_assignments.py
  Compile-verified before upload.
  Impact: 18 advisors (~3.76% of SCD records) have split normalization applied.
  fee_earning_aua and avg_fee_bps_earned will be slightly adjusted for those 18.

---

## Files Uploaded to S3

| Script | S3 Key | Reason |
|--------|--------|--------|
| A_01.advisor_assignments.py | code/gold/A_01.advisor_assignments.py | Multi-role split normalization (c6285ae8) -- was missing |
| D_00.portal_aggregates.py | code/gold/D_00.portal_aggregates.py | New commits since last AE deploy (e3bdf513) |
| D_02.advisor_client_detail.py | code/gold/D_02.advisor_client_detail.py | New commits since last AE deploy (c6285ae8, a3e620d4) |
| D_04.client_portal_summary.py | code/gold/D_04.client_portal_summary.py | New commits since last AE deploy (f3843e17, fe999416) |
| C_08.advisor_fee_efficiency.py | code/gold/C_08.advisor_fee_efficiency.py | Efficiency fix (d79ad9e7, this session) |

---

## Gold Run

Triggered: bd-gold-trigger Lambda, mode=incremental.
  Instance: i-01003b035d2988dfb
  Response: {"message": "Instance started", "previous_state": "stopped"}

Chain order (relevant scripts): A_01 -> D_00 -> D_02 -> D_04 (with C_08 before D_04).

---

## Notifications Sent

- 0.4.0_DE_ClientPlatform~A: platinum artifacts described, field names confirmed, Travis spot-check values noted.
  Unblocks DE .041 (advisor drilldown page wiring).

---

## Next Steps

1. **[DS - post-run]** Verify platinum/advisors/travis_penfield/timeseries.json has role AUA fields.
   Spot-check: architect_aua ~$180M, total_aua ~$427M on latest date.
2. **[DS - post-run]** Verify platinum/firm/leaderboard.json Travis total_aua ~$427M, period_start_aua present.
3. **[DS - post-run]** Verify platinum/firm/fee_efficiency.json Cole Pettis efficiency_pctile near 90th+.
4. **[DE~A]** Wire DE .041 advisor drilldown page using confirmed field names.
5. **[DE~A]** Add FeeEfficiencyPanel tooltip per .045 findings (commission = prorated split-weighted estimate).

# ADVI_STAUDT.CHART-ALIGN — D_00c Per-Day Gate Cutover

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-04-21
**TO:** ADVI_STAUDT.CHART-ALIGN.ds-d00c-leaderboard-per-day-gate-cutover.md
**Status at write-time:** Phase 2 gate PASS, commit in progress. S3 upload HELD (base lane 51ce2df1 RAVC4 pending).

---

## Current State

Per-day gate implementation authored and pre-commit gate PASS. Code commits cleanly. S3 upload held per base-lane coordination (base lane 51ce2df1 qa-runner running D_00c with current code to capture pre-cutover Travis baseline).

Pre-flag #1 sent to CTO (20260421T180849Z) and COO (20260421T180855Z).

---

## Compiler Tools

| Tool | When | Result | Note |
|------|------|--------|------|
| `comp-pipescript io D_00c` | Phase 1 — before write | ADVISOR_ASSIGNMENTS in READS; CANONICAL_NNA_PREFIX in READS; no COLUMN GAPS | READS confirm history is accessible |
| `comp-blast D_00c` | Phase 1 | No downstream consumers for D_00c script node | D_04 consumes the artifact (employee_leaderboard.json); terminal in gold graph |
| Read D_02 048af6a3 pattern | Phase 1 | `_build_acct_adv_window` + `_load_canonical_nna_per_advisor` date-gate identified at L1624-1722 + L1773-1785 | Transplanted pattern |
| `ds-commit-gate.sh` D_00c + validate_D_00c.py | Phase 2 | EXIT 0 | py_compile + AST scan clean on both files |

Pre-cutover Travis Q2 baseline spot-check: not run locally (requires S3 access). Baseline per CTO session log: -$6.311M. Post-cutover target: -$6.845M ±$0.05M. Will validate post-deploy via standalone validator.

---

## Design Notes

### Pattern source (D_02 048af6a3)

D_02 `_load_canonical_nna_per_advisor` (L1666-1690):
```python
df = df.merge(_lookup, on='account_id', how='inner')
df['date'] = pd.to_datetime(df['date'])
df = df[(df['date'] >= df['first_date']) & (df['date'] <= df['last_date'])]
```
Where `_lookup` is `(account_id, advisor_name, _role, weight, first_date, last_date)` built from account_performance history.

D_00c adaptation: same date-gate logic, but:
- `_build_acct_adv_window` melts role columns from account_performance (already loaded) to get tagging windows
- Gate applied inside `_compute_tagged_window_metrics` when `acct_adv_window` provided
- Fallback path preserved for environments where role cols absent from account_performance

### AUA stays current-snapshot

Per wire_contract: period_start_aua uses advisor_account_pairs (from account_team, current-snapshot). Not changed. role_breakdown.aua also unchanged (built from account_team melt, not from the per-day gate path).

### Edge case note (matches D_02)

Detach-reattach gap: if advisor was detached and later reattached, `first_date/last_date` window includes the gap. This is the same known edge case in D_02 (L1779: "detach-reattach gaps are a known edge case for a follow-up"). Matches chart methodology — no divergence.

---

## Files Modified

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py` | NEW `_build_acct_adv_window()`. Modified `_compute_tagged_window_metrics()` (new `acct_adv_window` param + per-day gate code path). Extended `_AP_COLS` (role cols). Wired `_acct_adv_window` in `build_employee_leaderboard()`. |
| `data/black_diamond/scripts/gold/gold_validate_config.yaml` | D_00c block: added QTD entries count_min (ERROR), QTD NNA field_nonzero (WARN), Travis spot-check script_check (WARN/doc). |
| `data/black_diamond/scripts/validators/validate_D_00c.py` | NEW standalone validator. Travis QTD NNA convergence check + firm QTD NNA sanity. |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-21/chart_align_d00c_per_day_gate.md` | This log. |

---

## Blockers

None locally. S3 upload held pending:
1. Base lane 51ce2df1 qa-runner completion + RAVC4 close (ETA ~14:30-15:30 ET per base lane coord message 20260421T180510Z)
2. Pre-flag #2 GO from CTO+COO before aws s3 cp

---

## Next Steps

1. **[0.4.0_DS~B]** Await RAVC4 close from base lane.
2. **[0.4.0_DS~B]** On RAVC4 close: fire Pre-flag #2 to CTO+COO with commit SHA + gate evidence.
3. **[0.4.0_DS~B]** On Pre-flag #2 GO: `aws s3 cp` D_00c to S3; dispatch qa-runner `--from D_00c` or `--group D`.
4. **[0.4.0_DS~B]** On qa-runner exit: run `validate_D_00c.py --artifact /tmp/employee_leaderboard.json`; check Travis QTD NNA = -$6.845M ±$0.05M.
5. **[0.4.0_DS~B]** MCP DE (0.4.0_DE_ClientPlatform) with artifact-ready + commit hash to unblock CHART-ALIGN-FE.
6. **[0.4.0_DS~B]** MCP COO COMPLETE with commit hash + qa-runner evidence + Travis convergence.
7. **[0.4.0_DS~B]** Pivot to COHORT-A (D_04 cohort_a_summary.json).

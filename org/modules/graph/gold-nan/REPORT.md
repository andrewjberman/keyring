# gold-nan NaN-Compliance Audit Report

**Generated:** 2026-05-14 (ADHC_COMPIL_V4.029b)
**Lane:** `data/inf/scripts/gold/` (top-level scripts only; lib/ and tests/ excluded)

## Summary

| Classification | Count | % of emit-boundary scripts |
|---|---|---|
| PASS    | 2  | 5% |
| INLINE  | 0  | 0% |
| NEITHER | 40 | 95% |
| N/A (no JSON emit) | 37 | — |
| **Total** | **79** | |

## PASS (compliant — safe_json_dumps from shared lib)

- `INF_D_00c.portal_leaderboard` (`data/inf/scripts/gold/INF_D_00c.portal_leaderboard.py`)
- `INF_D_04.client_portal_summary` (`data/inf/scripts/gold/INF_D_04.client_portal_summary.py`)

## INLINE (opportunistic-refactor candidates)

(none — no inline _strip_nan defs or allow_nan=False found)

## NEITHER (silent-drift risk — follow-up TOs needed)

- `09.generate_partner_analytics` (`data/inf/scripts/gold/09.generate_partner_analytics.py`)
- `B_01b.classify_new_securities` (`data/inf/scripts/gold/B_01b.classify_new_securities.py`)
- `C_05.client_tax_liability` (`data/inf/scripts/gold/C_05.client_tax_liability.py`)
- `C_06.client_mix_timeseries` (`data/inf/scripts/gold/C_06.client_mix_timeseries.py`)
- `C_08.advisor_fee_efficiency` (`data/inf/scripts/gold/C_08.advisor_fee_efficiency.py`)
- `D_00c.portal_leaderboard` (`data/inf/scripts/gold/D_00c.portal_leaderboard.py`)
- `D_02.advisor_client_detail` (`data/inf/scripts/gold/D_02.advisor_client_detail.py`)
- `D_04.client_portal_summary` (`data/inf/scripts/gold/D_04.client_portal_summary.py`)
- `I_D00.portal_aggregates` (`data/inf/scripts/gold/I_D00.portal_aggregates.py`)
- `I_D00b.portal_timeseries` (`data/inf/scripts/gold/I_D00b.portal_timeseries.py`)
- `I_D03.composition_artifacts` (`data/inf/scripts/gold/I_D03.composition_artifacts.py`)
- `INF_09.generate_partner_analytics` (`data/inf/scripts/gold/INF_09.generate_partner_analytics.py`)
- `INF_A_-1.materialize_txn_cache` (`data/inf/scripts/gold/INF_A_-1.materialize_txn_cache.py`)
- `INF_B_00.canonical_holdings` (`data/inf/scripts/gold/INF_B_00.canonical_holdings.py`)
- `INF_B_01b.classify_new_securities` (`data/inf/scripts/gold/INF_B_01b.classify_new_securities.py`)
- `INF_C_05.client_tax_liability` (`data/inf/scripts/gold/INF_C_05.client_tax_liability.py`)
- `INF_C_06.client_mix_timeseries` (`data/inf/scripts/gold/INF_C_06.client_mix_timeseries.py`)
- `INF_C_08.advisor_fee_efficiency` (`data/inf/scripts/gold/INF_C_08.advisor_fee_efficiency.py`)
- `INF_D_00.portal_aggregates` (`data/inf/scripts/gold/INF_D_00.portal_aggregates.py`)
- `INF_D_00b.portal_timeseries` (`data/inf/scripts/gold/INF_D_00b.portal_timeseries.py`)
- `INF_D_00d.cumulative_chart` (`data/inf/scripts/gold/INF_D_00d.cumulative_chart.py`)
- `INF_D_00e.fresh_header_supplement` (`data/inf/scripts/gold/INF_D_00e.fresh_header_supplement.py`)
- `INF_D_00f.advisor_nna_canonical` (`data/inf/scripts/gold/INF_D_00f.advisor_nna_canonical.py`)
- `INF_D_02.advisor_client_detail` (`data/inf/scripts/gold/INF_D_02.advisor_client_detail.py`)
- `INF_D_02b.top_holdings` (`data/inf/scripts/gold/INF_D_02b.top_holdings.py`)
- `INF_D_02c.client_directory` (`data/inf/scripts/gold/INF_D_02c.client_directory.py`)
- `INF_D_02d.firm_mix_summary` (`data/inf/scripts/gold/INF_D_02d.firm_mix_summary.py`)
- `INF_D_03.composition_artifacts` (`data/inf/scripts/gold/INF_D_03.composition_artifacts.py`)
- `INF_D_04b.client_publishers` (`data/inf/scripts/gold/INF_D_04b.client_publishers.py`)
- `INF_D_05.activity_scan` (`data/inf/scripts/gold/INF_D_05.activity_scan.py`)
- `INF_D_05.client_top_holdings` (`data/inf/scripts/gold/INF_D_05.client_top_holdings.py`)
- `INF_D_06.cash_drag` (`data/inf/scripts/gold/INF_D_06.cash_drag.py`)
- `INF_D_06.client_timeseries` (`data/inf/scripts/gold/INF_D_06.client_timeseries.py`)
- `INF_D_07.concentration_risk` (`data/inf/scripts/gold/INF_D_07.concentration_risk.py`)
- `INF_D_07a.firm_concentrations` (`data/inf/scripts/gold/INF_D_07a.firm_concentrations.py`)
- `INF_D_08.nmec_nmnc_nna` (`data/inf/scripts/gold/INF_D_08.nmec_nmnc_nna.py`)
- `INF_D_09.account_timeseries` (`data/inf/scripts/gold/INF_D_09.account_timeseries.py`)
- `INF_E_00.eclipse_model_portfolios` (`data/inf/scripts/gold/INF_E_00.eclipse_model_portfolios.py`)
- `valgate_baseline` (`data/inf/scripts/gold/valgate_baseline.py`)
- `valgate_gate` (`data/inf/scripts/gold/valgate_gate.py`)

## N/A (no JSON-emit boundary — parquet/CSV-only scripts)

- `A_00.accounts_dimension`
- `A_01.advisor_assignments`
- `A_02.fee_rate_history`
- `A_03.positions_cube`
- `A_04.client_dimension`
- `B_00.canonical_holdings`
- `B_01.holdings_lots`
- `B_02.canonical_lots`
- `B_03.account_gains`
- `build_canonical_prices`
- `C_00.canonical_performance`
- `C_01.canonical_nna`
- `C_01b.role_aua_backfill`
- `C_02.client_performance`
- `C_03.account_performance`
- `C_04.validate_aua`
- `C_07.advisor_attribution`
- `INF_A_00.accounts_dimension`
- `INF_A_01.advisor_assignments`
- `INF_A_02.fee_rate_history`
- `INF_A_03.positions_cube`
- `INF_A_04.client_dimension`
- `INF_B_01.holdings_lots`
- `INF_B_02.canonical_lots`
- `INF_B_03.account_gains`
- `INF_build_canonical_prices`
- `INF_C_00.canonical_performance`
- `INF_C_01.canonical_nna`
- `INF_C_01b.role_aua_backfill`
- `INF_C_02.client_performance`
- `INF_C_03.account_performance`
- `INF_C_04.validate_aua`
- `INF_C_07.advisor_attribution`
- `INF_C_09.fee_status_audit`
- `INF_run_c_chain`
- `run_c_chain`
- `valgate_gate_fixtures`

## Upgrade Path

For all NEITHER-class scripts, migrate each S3-emit `json.dumps` to `safe_json_dumps`:

```python
from safe_json_serialize import safe_json_dumps  # noqa: E402
# before: body = json.dumps(obj, default=str, separators=(",", ":"))
# after:  body = safe_json_dumps(obj, default=str, separators=(",", ":"))
```

Shared lib: `data/inf/scripts/gold/lib/safe_json_serialize.py`
S3 mirror: `s3://opal-data-inf/code/gold/lib/safe_json_serialize.py`

## Ruling

**AC2:** This enumeration is NOT a forced migration. NEITHER-class scripts are flagged
for opportunistic follow-up TOs (DS lanes). No immediate data reprocess required.
Priority order for follow-up: INF_D portal-emit scripts first (user-facing JSON);
C/B-chain parquet-adjacent scripts second.

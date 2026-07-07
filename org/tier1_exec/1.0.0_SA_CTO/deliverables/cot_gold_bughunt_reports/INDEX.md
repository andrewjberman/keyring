# cot gold-runner code-review -- per-agent report index

Raw per-agent outputs from workflow `wf_61db2e92-8e9`. 39 review + 28 verify = 67 agents, one file each in this folder. NOT triaged/aggregated -- these are the granular agent reports for the per-report drive phase.

## Review agents (one per script)
| file | verdict | findings (C/H/M/L) | runs_in_incremental |
|---|---|---|---|
| review_A_00.accounts_dimension.py.md | issues-found | 1/1/1/2 | True |
| review_A_01.advisor_assignments.py.md | issues-found | 0/0/1/2 | False |
| review_A_02.fee_rate_history.py.md | issues-found | 0/2/0/1 | False |
| review_A_03.positions_cube.py.md | issues-found | 0/0/2/3 | False |
| review_A_04.client_dimension.py.md | issues-found | 0/0/3/0 | False |
| review_B_00.canonical_holdings.py.md | issues-found | 0/2/3/0 | False |
| review_B_01.holdings_lots.py.md | issues-found | 1/1/1/1 | False |
| review_B_01b.classify_new_securities.py.md | issues-found | 1/1/1/0 | False |
| review_B_02.canonical_lots.py.md | issues-found | 1/0/3/1 | False |
| review_B_03.account_gains.py.md | issues-found | 0/1/2/1 | False |
| review_C_01.canonical_nna.py.md | issues-found | 0/0/3/1 | False |
| review_C_01b.role_aua_backfill.py.md | issues-found | 0/1/1/1 | False |
| review_C_01c.role_aua_flow_join.py.md | issues-found | 0/0/1/2 | False |
| review_C_03.account_performance.py.md | issues-found | 0/1/1/1 | False |
| review_C_04.validate_aua.py.md | issues-found | 1/1/1/1 | False |
| review_C_05.client_tax_liability.py.md | issues-found | 0/0/2/2 | False |
| review_C_06.client_mix_timeseries.py.md | issues-found | 0/2/1/1 | True |
| review_C_07.advisor_attribution.py.md | issues-found | 1/0/1/1 | False |
| review_C_08.advisor_fee_efficiency.py.md | issues-found | 0/0/1/3 | False |
| review_D_00.portal_aggregates.py.md | issues-found | 0/0/2/2 | False |
| review_D_00b.portal_timeseries.py.md | issues-found | 0/0/1/2 | False |
| review_D_00c.portal_leaderboard.py.md | issues-found | 0/0/2/2 | False |
| review_D_01.partner_analytics.py.md | issues-found | 1/1/2/1 | False |
| review_D_02.advisor_client_detail.py.md | issues-found | 0/1/0/2 | False |
| review_D_03.composition_artifacts.py.md | issues-found | 0/0/1/3 | True |
| review_D_04.client_portal_summary.py.md | issues-found | 0/0/2/2 | False |
| review_E_00.decompose_aua_gap.py.md | issues-found | 0/0/1/1 | False |
| review_E_01.account_quality_tiers.py.md | issues-found | 0/0/2/3 | False |
| review_E_18.detect_new_securities.py.md | issues-found | 0/0/0/2 | False |
| review_E_20.cross_script_validation.py.md | issues-found | 0/0/4/2 | False |
| review_E_21.generate_reconciliation_reference.py.md | issues-found | 0/1/1/4 | False |
| review_E_22.diagnose_unassigned_accounts.py.md | issues-found | 0/0/0/2 | False |
| review_E_23.diagnose_fee_splits.py.md | issues-found | 0/0/1/3 | False |
| review_E_24.rebuild_fee_scorecard.py.md | issues-found | 0/1/1/1 | False |
| review_build_canonical_prices_v2.py.md | issues-found | 0/1/2/1 | False |
| review_diag_gold_silver_recon.py.md | issues-found | 0/2/2/1 | False |
| review_gldinc_p1_shadow.py.md | issues-found | 0/0/1/1 | False |
| review_validate_platinum_consistency.py.md | issues-found | 0/0/2/1 | False |
| review_validate_sl_nightly_gate.py.md | issues-found | 0/1/1/2 | False |

## Verify agents (one per adversarial check of a material finding)
| file | target | is_real | confidence | corrected_sev |
|---|---|---|---|---|
| verify_01_A_02.fee_rate_history.md | A_02.fee_rate_history.py | False | refuted | low |
| verify_02_build_canonical_prices_v2.md | build_canonical_prices_v2.py | True | confirmed | medium |
| verify_03_A_02.fee_rate_history.md | A_02.fee_rate_history.py | False | refuted | low |
| verify_04_B_00.canonical_holdings.md | B_00.canonical_holdings.py | True | confirmed | high |
| verify_05_A_00.accounts_dimension.md | A_00.accounts_dimension.py | False | refuted | low |
| verify_06_B_01b.classify_new_securities.md | B_01b.classify_new_securities.py | True | confirmed | high |
| verify_07_B_00.canonical_holdings.md | B_00.canonical_holdings.py | True | confirmed | high |
| verify_08_s3_layout.md | s3_layout.py | True | confirmed | high |
| verify_09_A_00.accounts_dimension.md | A_00.accounts_dimension.py | True | confirmed | critical |
| verify_10_unknown.md | unknown | False | refuted | low |
| verify_11_nna_flows.md | nna_flows.py | False | refuted | low |
| verify_12_B_02.canonical_lots.md | B_02.canonical_lots.py | True | confirmed | high |
| verify_13_cot_silver_merge.md | cot_silver_merge.py | False | refuted | low |
| verify_14_unknown.md | unknown | False | refuted | low |
| verify_15_C_04.validate_aua.md | C_04.validate_aua.py | False | refuted | low |
| verify_16_C_04.validate_aua.md | C_04.validate_aua.py | False | refuted | low |
| verify_17_build_transactions_silver.md | build_transactions_silver.py | True | confirmed | critical |
| verify_18_D_03.composition_artifacts.md | D_03.composition_artifacts.py | False | refuted | low |
| verify_19_C_07.advisor_attribution.md | C_07.advisor_attribution.py | True | confirmed | critical |
| verify_20_unknown.md | unknown | True | confirmed | high |
| verify_21_D_01.partner_analytics.md | D_01.partner_analytics.py | True | confirmed | high |
| verify_22_gold_utils.md | gold_utils.py | False | refuted | low |
| verify_23_unknown.md | unknown | True | plausible | medium |
| verify_24_s3_layout.md | s3_layout.py | True | confirmed | high |
| verify_25_C_08.advisor_fee_efficiency.md | C_08.advisor_fee_efficiency.py | True | confirmed | medium |
| verify_26_unknown.md | unknown | True | confirmed | medium |
| verify_27_unknown.md | unknown | True | confirmed | medium |
| verify_28_validate_sl_nightly_gate.md | validate_sl_nightly_gate.py | True | confirmed | low |
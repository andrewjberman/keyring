# Session Log — GLDOPS.004 Script Rename + Canonical NNA + Portal Audit
**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-07
**Project:** ADVI_GLDOPS

---

## Summary

Major refactoring session covering five areas: (1) canonical NNA now includes transaction-classified flows, (2) 08c fee efficiency rewritten to use canonical sources, (3) all gold scripts renamed to 5-group taxonomy (A-E), (4) complete portal artifact audit and redundancy mapping, (5) C_06 portal writes extracted to D_03.

---

## Part 1: Canonical NNA (C_01, formerly 04b)

04b previously wrote only the accounting residual (`aua_residual`). Now also loads BD transaction flows via `nna_flows.load_flows_from_transactions()` once at startup, joins `daily_inflow`, `daily_outflow`, `nna_txn` onto every partition.

Canonical NNA output schema: `date, account_id, relationship_id, architect, client_state, tax_status, aua_residual, growth, aua_current, components, nna_clean, daily_inflow, daily_outflow, nna_txn`

This makes C_01 the single source of truth for NNA. Downstream scripts never call `nna_flows` independently.

---

## Part 2: Fee Efficiency Rewrite (C_08, formerly 08c)

Full rewrite:
- Reads canonical NNA (C_01) for real NNA (`nna_txn`), not the accounting residual
- Uses `account_team.parquet` (C_07/08b) for resolved advisor names
- Keeps SCD PIT for split percentages and fee rates (01's table)
- Bulk vectorized: single concat, single merge pass, single groupby, parallel write
- Removed ProcessPoolExecutor/fork pattern, per-date SCD lookup, `nna_implied` references

---

## Part 3: Portal Publisher Fixes (D_00, D_01, D_02)

### D_00 (11a) — Account-level NNA
- New `_load_canonical_nna()`: bulk-loads all C_01 partitions (account-level)
- New `_build_account_nna_by_geo()` and `_build_account_nna_by_advisor()`: aggregate NNA at account grain
- Firm NNA chart, nna_geo, nna_adv drills use account-level canonical NNA
- `_build_geo_view`, `_build_advisor_view`, `_build_geo_city_view` now carry `daily_inflow`/`daily_outflow` through aggregations
- All paths fall back to relationship-level if C_01 hasn't been re-run

### D_01 (09) — Account-level NNA for period views
- Loads canonical NNA + account_team in `load_data()`
- `build_nna_geo_view` and `build_nna_adv_view` use account-level canonical NNA for period NNA
- Per-relationship NNA distributions use canonical NNA summed to relationship level

### D_02 (11b) — Account-team architect resolution
- Loads `account_team` (C_07) and overrides architect/implementor in account_performance
- All downstream per-entity JSONs use 08b's resolved names

---

## Part 4: Script Rename (5-Group Taxonomy)

All 41+ gold scripts renamed from old numbering (00, 01b, 02b, ...) to rigid 5-group scheme:

| Group | Name | Count | Purpose |
|-------|------|-------|---------|
| A | Foundation | 5 | Dimensions, SCD history |
| B | Holdings | 4 | Canonical positions, lots, gains |
| C | Activity | 9 | Performance, NNA, tax, attribution |
| D | Portal | 4 | JSON artifact publishers |
| E | Diagnostics | 20 | Ad-hoc validation/audit |

3 absorbed scripts deleted: 07 (geo), 08 (advisor), 10 (rolling flows) — all absorbed into D_00.

### gold_dispatch.sh — Complete rewrite
Three modes via flags: `--single C_07`, `--group B`, `--chain full`
Modifiers: `--bg`, `--incremental`, `--dry-run`
Preset chains: full, canonical, downstream, foundation, rebuild
Script catalog is a single block at the top — one line per script.

### Dependency fix found during audit
C_06 depends on C_07 (rel_architect_lookup) for advisor-level mix grouping. Reordered downstream chain: `C_03 -> C_05 -> C_07 -> C_06 -> C_08 -> D_00 -> D_01 -> D_02 -> D_03`

### Legacy cleanup
- `run_canonical_chain.sh`, `run_downstream_chain.sh` deleted (superseded)
- `run_gold_layer.sh` replaced with thin wrapper delegating to `gold_dispatch.sh`
- EC2 SSM chain intact: `ssm-run-gold.sh` -> `run_gold_layer.sh` -> `gold_dispatch.sh`

---

## Part 5: Portal Artifact Audit

### New docs
- `docs/architecture/gold-artifact-mapping.md` — complete artifact map (every S3 key, who writes, who reads, portal route)
- `data/black_diamond/scripts/gold/REGISTRY.md` — script registry with groups, chains, inputs/outputs, canonical source-of-truth docs

### Key findings
- 13 of 39 artifacts redundantly produced by both Lambda publishers and EC2 scripts
- 5 dead routes in opal-partners-data (no producer, no frontend consumer) — marked DEPRECATED
- 3 Lambda hot-path parquet reads (50-350MB per request) — replaceable by pre-computed JSONs
- 2 opal-partners-data routes read OLD S3 keys — fixed to new paths

### opal-partners-data Lambda fixes
- `clients-tab`: `gold/clients_tab.json` -> `gold/artifacts/clients_tab.json`
- `client detail`: `gold/clients/{id}.json` -> `gold/entities/clients/{id}/detail.json`
- 5 dead routes marked DEPRECATED in docstrings

### C_06 -> D_03 portal write extraction
- New `lib/mix_views.py`: shared `compute_period_views()`, `advisor_id()`, `MIX_ASSET_CLASSES`
- C_06 no longer writes firm/advisor portal JSONs. Writes intermediate `gold/views/mix_daily_summary.json`
- D_03 reads summary, publishes firm_mix_views, firm_mix_views_daily, per-advisor mix/mix_daily/mix_timeseries
- All portal-facing JSONs now produced exclusively by D-group scripts

---

## Files Modified

| File | Change |
|------|--------|
| C_01.canonical_nna.py (04b) | Added transaction flow loading, daily_inflow/daily_outflow/nna_txn columns |
| C_08.advisor_fee_efficiency.py (08c) | Full rewrite: canonical NNA + account_team + bulk vectorize |
| D_00.portal_aggregates.py (11a) | Account-level NNA loading + geo/adv views carry flow columns |
| D_01.partner_analytics.py (09) | Account-level NNA for period views |
| D_02.advisor_client_detail.py (11b) | Account-team architect resolution |
| C_06.client_mix_timeseries.py | Removed portal JSON writes, writes mix_daily_summary.json instead |
| D_03.composition_artifacts.py | Added Step 8: publish firm/advisor mix views from C_06 summary |
| lib/mix_views.py | NEW: shared compute_period_views, advisor_id, MIX_ASSET_CLASSES |
| lib/s3_layout.py | Added MIX_DAILY_SUMMARY key |
| gold_dispatch.sh | Full rewrite: 3-mode launcher with catalog, chains, groups |
| run_gold_layer.sh | Replaced with thin wrapper delegating to gold_dispatch.sh |
| opal-partners-data/lambda_function.py | Fixed 2 old-key reads, marked 5 dead routes DEPRECATED |
| docs/architecture/gold-artifact-mapping.md | NEW: complete artifact mapping + redundancy analysis |
| REGISTRY.md | NEW: script registry with groups, chains, portal coverage map |
| All 22 A-D scripts | Renamed + docstring/banner updates |
| All 20 E scripts | Renamed |
| 3 absorbed scripts | Deleted (07, 08, 10) |
| 2 legacy shell scripts | Deleted (run_canonical_chain.sh, run_downstream_chain.sh) |

---

## Next Steps

- [AE] Execute full pipeline run on bd-gold-layer-runner. Report per-step timings.
- [DT] Deploy opal-partners-data Lambda (2 route fixes + 5 deprecated routes)
- [DT] Disable bd-portal-publisher + bd-portal-advisor-publisher Lambda triggers (Phase 1 of redundancy cleanup)
- [DS] After timing report: evaluate GLDOPS.005 (bulk vectorize remaining scripts)
- [DS] Future: add per-account timeseries JSON to D_02 (eliminates Lambda hot-path E2)

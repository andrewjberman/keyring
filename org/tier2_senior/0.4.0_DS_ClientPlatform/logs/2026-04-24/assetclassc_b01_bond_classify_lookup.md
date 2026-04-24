# ADVI_ROLLUP.ASSETCLASSc — Bond Classify Lookup Chain
# 0.4.0_DS_ClientPlatform — 2026-04-24
# Commit: 090d11f6 (CLOUD, pushed)
# Status: COMPLETE

## Compiler Tools

| Step | Command | Observed | Pass? |
|------|---------|----------|-------|
| P1.1 | comp-pipescript io B_01 | READS: ACCOUNTS_DIMENSION + silver/bd_assets_dim.parquet. bd_assets_dim already a B_01 read (CP-DS1 CUSIP enrichment). No column gaps. | PASS |
| P1.2 | comp-blast B_01 | No downstream consumers (terminal writes — holdings_lots timeseries). Pre-change and post-change identical. | PASS (baseline) |
| P1.3 | bd_assets_dim coverage check | 10,937 rows. opal_asset_class: equity 6,294 / fixed_income 2,731 / alternatives 1,833 / other 49 / cash 30. 0 nulls. cusip non-null 9,901; ticker non-null 7,744. | INFO |
| P2.1 | python -m py_compile B_01 | Exit 0 | PASS |
| P2.2 | .tools/ds-commit-gate.sh B_01 | Exit 0 after ruff auto-fix (7 issues) + manual F841 prefix fix (3 vars) + E702 split | PASS |
| P3.1 | comp-pipescript deployed B_01 | MATCH | PASS |
| P3.2 | comp-blast B_01 (post-change) | Same terminal consumer set — no new downstream nodes | PASS |

## Summary

Replaced `cost_per_unit <= 2.0` bond detection heuristic in `_apply_rps_price_override`
with deterministic lookup chain from bd_assets_dim (opal_asset_class == 'fixed_income').

**Implementation:**
- `_build_rps_context`: loads bd_assets_dim, builds `is_bond_by_cusip` (9,901 entries)
  and `is_bond_by_ticker` (7,744 entries) dicts from opal_asset_class == 'fixed_income'.
  Adds both to rps_context dict. Graceful fallback if dim load fails (heuristic for all).
- `_apply_rps_price_override`: vectorized pandas lookup (no loop).
  Priority: cusip dim → ticker dim → cost_per_unit <= 2.0 heuristic with WARN log.
  Logs: n_dim_cusip / n_dim_ticker / n_heuristic + heuristic % per run.

**Scope note:** ticker_lookup.json (TO reference) does not exist as a local file.
The bd_assets_dim ticker lookup serves as the effective second path. No local curated
JSON exists; ETFClassifier (DynamoDB bd-securities) is the separate classification
system used by C_06/D_03/D_04 and is not in scope for this RPS pricing function.

**Side effect:** `from __future__ import annotations` added (DSFLOW.004 Rule 15 mandate).
Pre-existing ruff issues also cleaned (F401/F541/E702/F841) — constitutes B_01 backfill
sweep so DSFLOW.004 backfill pass can treat B_01 as already clean.

## ACs Status

| AC | Status |
|----|--------|
| AC#1 B_01 classification replaced per lookup chain | DONE 090d11f6 |
| AC#2 Heuristic-fallback-ratio (to be measured on first nightly run) | PENDING nightly |
| AC#3 Spot-check 20 rows | DEFERRED — requires live BD runner invocation |
| AC#4 No regression on downstream consumers (comp-blast same consumer set) | DONE |
| AC#5 py_compile + ds-commit-gate exit 0 | DONE |
| AC#6 comp-pipescript deployed MATCH | DONE |
| AC#7 Session log Compiler Tools | THIS FILE |
| AC#8 MCP COMPLETE to COO | DONE (see COO reply in session) |

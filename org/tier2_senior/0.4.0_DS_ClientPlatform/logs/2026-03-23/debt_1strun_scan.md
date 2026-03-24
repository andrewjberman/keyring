# DEBT_1STRUN Scan -- 0.4.0_DS_ClientPlatform

**Date:** 2026-03-23
**Scope:** data/black_diamond/scripts/gold/, data/black_diamond/scripts/silver/, data/black_diamond/scripts/classification/
**Task Order:** DEBT_1STRUN.001.scan
**Status:** Complete

---

## Findings

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 1 | gold/archive/ (31 files) | all | C1 Dead | High | Entire archive/ directory is dead code. `run_gold_layer.sh:71` excludes it from S3 sync (`--exclude "archive/*"`). No active script imports from archive. ~5,000+ lines of unreachable code across 31 files. |
| 2 | silver/build_interpolated_prices.py | 1-236 | C1 Dead | High | Entire script orphaned. `build_interpolated_prices()` never called by any orchestrator. Output `interpolated_prices.parquet` has zero downstream consumers. |
| 3 | silver/merge-daily-allocation-incremental.py | 1-338 | C1 Dead | High | Docstring line 17 states "DEPRECATED. The unified merge-daily-incremental.py with --allocations flag is the preferred path." Not called by any orchestrator. Maintains orphaned manifest `silver/allocation_incremental_manifest.json`. |
| 4 | silver/fetch_historical_prices_yfinance.py | 1-594 | C1 Dead | High | Not invoked by any orchestrator or Lambda. Docstring references `historical-prices-scheduler Lambda` that does not exist. OpenAI discovery path (lines 130-208) never runs in production. |
| 5 | silver/security_ticker_mapping_final.py | 12-132 | C1 Dead | High | Static dict `FINAL_BATCH_MAPPINGS` (150+ entries) superseded by `config/ticker_lookup.json` in S3. Only consumer is `build_interpolated_prices.py` (itself dead). Imports from `security_ticker_mapping_complete` which lives only in archive/. |
| 6 | gold/08_build_nna_aua_by_advisor.py | 255-261 | C1 Dead | Low | `save_rel_lookup()` is a no-op stub. Comment: "rel_architect_lookup.parquet is now written by 08b". |
| 7 | gold/01_build_advisor_assignments_history.py | 329 | C1 Dead | Low | Emoji character in print statement. Violates CLAUDE.md rule 13 (no emojis -- breaks CloudWatch on Windows). |
| 8 | gold/04_build_client_dimension.py | 368 | C1 Dead | Low | Emoji character in print statement. Same violation. |
| 9 | gold/06_build_client_tax_liability.py | 284 | C1 Dead | Low | Emoji character in print statement. Same violation. |
| 10 | gold/07_build_nna_aua_by_geography.py | 337 | C1 Dead | Low | Emoji/Unicode character in print statement. Same violation. |
| 11 | gold/01_build_advisor_assignments_history.py | 69, 86 | C2 Deprecated | Medium | Comments reference stale `silver/bd_transactions.parquet` that is "no longer maintained." Outdated documentation artifact. |
| 12 | gold/04_build_client_dimension.py | 81-86 | C2 Deprecated | Medium | `load_transactions_summary()` has comment about stale `bd_transactions.parquet`. Documentation warning is outdated since the new pattern is established. |
| 13 | gold/05_build_client_performance.py | 126-150 | C2 Deprecated | Medium | "AUA Overrides" section loads `aua_overrides.json` for RC6 ghost account exclusions. Comment states RC1/RC2 mispriced assets are now fixed at source. Transitional workaround that may be fully removable. |
| 14 | gold/06b_build_client_mix_timeseries.py | 122 | C2 Deprecated | Medium | Comment references `.tmp_insurance_ap_gate.py` that does not exist. Stale documentation for a dead helper script. |
| 15 | silver/security_ticker_mapping_final.py | 12-132 | C2 Deprecated | High | Hardcoded mapping dict superseded by dynamic `config/ticker_lookup.json` in S3 and `_OPAL_ETF_OVERRIDES` dicts in active price scripts. |
| 16 | silver/fetch_historical_prices_yfinance.py | 130-208 | C2 Deprecated | Medium | OpenAI API integration with `gpt-4o-mini` (line 178) for security discovery. Never runs in production. `price_discovery` secret referenced but not documented. |
| 17 | classification/classify_bd_securities.py | 93 | C2 Deprecated | Medium | `model='gpt-4o-mini'` hardcoded with no version pinning. Model deprecation risk. |
| 18 | gold/05_build_client_performance.py + 05b_build_account_performance.py | 88-106 / 92-100 | C3 Duplication | High | Identical `INFLOW_TYPES` and `OUTFLOW_TYPES` frozensets defined in both scripts. NNA classification rules duplicated -- divergence if either changes independently. |
| 19 | gold/05_build_client_performance.py + 05b_build_account_performance.py | 203-361 / 253-378 | C3 Duplication | High | `load_flows_from_transactions()` nearly identical across both scripts. Composite dedup, exclusion rules, flow capping all copy-pasted. Bug fixes require coordinated edits. |
| 20 | gold/07_build_nna_aua_by_geography.py + 08_build_nna_aua_by_advisor.py | 74-86 / 85-96 | C3 Duplication | Medium | Identical `modal_str()` helper and `_MODAL_NULLS` frozenset duplicated in both aggregation scripts. |
| 21 | gold/05c_validate_aua_vs_silver.py + 05d_write_aua_certification.py | 60-62 / 60-67 | C3 Duplication | Medium | Identical `s3_object_exists()` helper function in both scripts. |
| 22 | silver/build_canonical_prices_v2.py (69-84) + bd_price_update.py (128-136) | see desc | C3 Duplication | Medium | `_OPAL_ETF_OVERRIDES` dict duplicated in both files. Comment in bd_price_update says "Keep this dict in sync" -- manual sync is a maintenance hazard. |
| 23 | silver/merge-daily-incremental.py + merge-daily-allocation-incremental.py | multiple | C3 Duplication | Medium | 6+ functions duplicated: `to_snake_case()`, `load_manifest()`/`save_manifest()`, `run_cmd()`, date extraction, parquet upload patterns. |
| 24 | All gold scripts (00-12) | line ~57 each | C4 Hardcoded | Medium | S3 bucket name `'opal-data-bd'` hardcoded as module-level constant in every script. Prevents environment-specific deployments. |
| 25 | gold/05_build_client_performance.py | 344, 117-118 | C4 Hardcoded | High | `FLOW_CAP = 50_000_000` and `VELOCITY_WINDOW_DAYS = 90`, `VELOCITY_THRESHOLD = 1.0` are business rules baked into code. Should be configurable. |
| 26 | gold/09_generate_partner_analytics.py | 81-98 | C4 Hardcoded | Medium | Color palettes (`GEO_COLORS`, `NNA_BLUE_SHADES`, `CLA_NMNC_COLOR`) hardcoded in Python backend. Presentation constants belong in config or CSS. |
| 27 | silver/merge-daily-incremental.py | 49 | C4 Hardcoded | Medium | `CORRECT_COL_COUNT = 71` magic number for schema validation. Schema changes break this silently. |
| 28 | silver/build_canonical_prices_v2.py | 49 | C4 Hardcoded | Medium | `MAX_WORKERS = 64` hardcoded thread pool size. Not tunable per instance type. |
| 29 | silver/bd_price_update.py | 56, 59-65 | C4 Hardcoded | Medium | `MAX_UNIT_PRICE = 100_000` price ceiling and `SOURCE_RANK` dict hardcoded. New sources require code changes. |
| 30 | classification/classify_bd_securities.py | 17-20 | C4 Hardcoded | Medium | `REGION = 'us-east-1'`, S3 bucket, DynamoDB table names all hardcoded. |
| 31 | classification/seed_bd_securities.py | 21-22, 27-36 | C4 Hardcoded | Medium | Table names, region, and `OPAL_ALIASES` dict all hardcoded. Aliases should be a config file. |
| 32 | classification/classify_bd_securities.py | 159 | C4 Hardcoded | Low | Secret ID `'openai-api-key'` hardcoded. |
| 33 | silver/build_interpolated_prices.py | 198, 217 | C5 Orphaned | High | Writes `interpolated_prices.parquet` and `interpolated_prices_summary.json` to S3. No downstream reader found in any script. Dead output accumulating in S3. |
| 34 | silver/merge-daily-allocation-incremental.py | 44-45 | C5 Orphaned | Medium | Maintains separate `silver/allocation_incremental_manifest.json` in S3. Never read by any script (unified script has its own manifest). |
| 35 | gold/05c_validate_aua_vs_silver.py | all | C5 Orphaned | Medium | Writes `gold/validation/aua_validation_{date}.json` to S3. No downstream consumer verified. Monitoring-only output with no pipeline integration. |
| 36 | gold/05c_validate_aua_vs_silver.py | 285-291 | C6 Stale | High | Main try-except catches all exceptions and calls `sys.exit(0)`. Validation failures are invisible. Downstream tasks assume validation passed. |
| 37 | gold/05d_write_aua_certification.py | 169-176 | C6 Stale | High | Main try-except catches all exceptions and calls `sys.exit(0)`. DynamoDB/S3 write failures exit silently. Pipeline continues unaware certification JSON was never written. |
| 38 | gold/00_build_accounts_dimension.py | 174-176 | C6 Stale | Medium | `except Exception as e:` returns `(None, None)` for any error. Cannot distinguish S3 permission errors from expected key-not-found. |
| 39 | gold/03_build_holdings_lots.py | 224-226 | C6 Stale | Medium | `except Exception as e:` in `load_allocations()` silently returns `None`. Parquet corruption indistinguishable from missing file. |
| 40 | gold/detect_new_securities.py | 59-62 | C6 Stale | Medium | `s3_object_exists()` catches both `ClientError` and `Exception`, returning `False` for both. 403 (permission denied) indistinguishable from 404 (not found). |
| 41 | gold/lib/etf_classifier.py | 59-62 | C6 Stale | Medium | DynamoDB scan `except Exception as e:` falls back to empty maps silently. Auth errors, service errors, and network errors all produce same result. Heuristic fallback hides real failures. |
| 42 | gold/05c_validate_aua_vs_silver.py | 51-53 | C6 Stale | Low | Custom `log()` function manually prefixes timestamps instead of using `logging` module. Not compatible with CloudWatch structured logging. |
| 43 | gold/05d_write_aua_certification.py | 55-57 | C6 Stale | Low | Custom `log()` same issue as #42. |
| 44 | silver/build_canonical_prices_v2.py | 231-236 | C6 Stale | Medium | Outlier capping uses hardcoded 50x threshold. Outliers silently replaced with asset median -- no structured logging of which assets were affected. |
| 45 | classification/classify_bd_securities.py | 104-111, 181-182 | C6 Stale | High | OpenAI call retry does not distinguish rate-limit (should backoff) from schema error (should skip) from network failure (should retry). Failed batches silently skipped with `continue`. |
| 46 | silver/merge-daily-incremental.py | 206-208, 160-162 | C6 Stale | Medium | Generic "Error processing" message on exception. Column count validation silently skips bad files without logging which columns were present. |
| 47 | silver/bd_price_update.py | 362-381 | C6 Stale | Medium | `invoke_price_update()` broad try-except. If status != 202, warning printed but execution continues with potentially stale prices. |

---

## Summary

- **Total findings:** 47
- **By category:** C1: 10, C2: 7, C3: 6, C4: 9, C5: 3, C6: 12
- **High severity:** 13
- **Medium severity:** 24
- **Low severity:** 10

### Recommended Priority Fixes (Top 3 by Impact)

1. **Delete gold/archive/ directory (Finding #1)** -- 31 files, ~5,000+ lines of dead code. Already excluded from S3 sync. No active references. Largest single reduction in maintenance surface area. Remove from repo or move to `docs/historical/` if compliance requires retention.

2. **Consolidate NNA flow classification logic (Findings #18, #19)** -- `INFLOW_TYPES`/`OUTFLOW_TYPES` frozensets and `load_flows_from_transactions()` are copy-pasted between `05_build_client_performance.py` and `05b_build_account_performance.py`. This is the highest-risk duplication: business rules for NNA classification will silently diverge if either script is edited independently. Extract to `gold/lib/nna_flows.py`.

3. **Fix silent `sys.exit(0)` in validation scripts (Findings #36, #37)** -- `05c_validate_aua_vs_silver.py` and `05d_write_aua_certification.py` swallow ALL exceptions and exit with code 0. Pipeline sees "success" even when validation fails or certification JSON is never written. This masks data quality issues and S3/DynamoDB failures. Change to `sys.exit(1)` on error, or propagate exceptions to the orchestrator.

---

**Report delivered to:** 0.4.0_DE_ClientPlatform for aggregation.

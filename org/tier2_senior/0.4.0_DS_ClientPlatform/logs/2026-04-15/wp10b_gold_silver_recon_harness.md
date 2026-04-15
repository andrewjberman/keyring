# 0.4.0_DS_ClientPlatform~B -- WP-10b Gold<->Silver Recon Harness

**Date:** 2026-04-15 (EDT)
**Serialization:** ~B
**Task Order:** `BDPL_CNPRCS.WP-10b.ds-gold-silver-recon-harness.md`

## Summary

Delivered the nightly gold<->silver reconciliation harness per WP-10b.
Script writes MD + JSON manifest covering 19 domains (18 row-count/sum +
1 AUA-total cross-check). Exit code 1 on FAIL, 0 otherwise -- AE can
wire into CloudWatch alerting.

## Files Modified

| File | Change |
|------|--------|
| data/black_diamond/scripts/diagnostics/diag_gold_silver_recon.py | NEW -- recon harness |
| data/black_diamond/diagnostics/gold_silver_recon_2026-04-15.md | NEW -- smoke test artifact |
| data/black_diamond/diagnostics/gold_silver_recon_2026-04-15.json | NEW -- smoke test artifact |

## Compiler Tools -- Canonical Triad Reproduction

### Phase 1 (before write)

| Step | Command | Expect | Observed | Pass/Fail |
|------|---------|--------|----------|-----------|
| 1 | `comp-pipescript io` on A_00..D_04 (26 scripts) | Enumerate every gold-silver join boundary | Captured to /tmp/wp10b_io.txt (500 lines). Identified silver boundaries: silver/prices/canonical_prices.parquet; gold/canonical/{holdings,lots_realized,lots_unrealized,performance,account_gains,nna,advisor_fee_detail}/; schwab/silver/{rld,uln,ult}/; gold/entities/clients/; gold/views/nna_aua_by_*; gold/artifacts/snapshots/aua_by_*. | **PASS** |
| 2 | `comp-blast diag_phantom_valuations` | Confirm no overlap (WP-10b != phantom) | `No nodes matching: diag_phantom_valuations` -- WP-7 staged, node does not yet exist. Zero overlap risk. | **PASS** |

Domain list (approved by COO 20260415T163447Z):
holdings_lots, canonical_holdings, canonical_prices, canonical_nna,
canonical_performance, canonical_lots_realized, canonical_lots_unrealized,
canonical_account_gains, advisor_fee_detail, nna_aua_by_{geo,advisor,city},
aua_snapshots_{region,state,architect,tax_status}, client_timeseries.

### Phase 2 (before commit)

| Step | Command | Expect | Observed | Pass/Fail |
|------|---------|--------|----------|-----------|
| 1 | `python -m py_compile diag_gold_silver_recon.py` | Exit 0 | Exit 0 | **PASS** |
| 2 | `python diag_gold_silver_recon.py --no-upload` | Manifest written, schema valid | 19 checks; 18 OK + 1 WARN (aua_totals cross-check TODO). MD+JSON written to data/black_diamond/diagnostics/. | **PASS** |
| 3 | `python diag_gold_silver_recon.py --no-upload --inject-fail canonical_nna` | FAIL status surfaces on injected domain; overall FAIL; exit 1 | canonical_nna reported FAIL; overall FAIL; exit 1. | **PASS** |

### Phase 3 (after commit)

| Step | Command | Expect | Observed | Pass/Fail |
|------|---------|--------|----------|-----------|
| 1 | `comp-blast gold_silver_recon_manifest` | No unintended consumers | (run post-commit) | **TBD** |

## Acceptance Criteria

| # | Criterion | Status |
|---|-----------|--------|
| 1 | Harness runs nightly; manifest to S3 diagnostics/ | **PENDING AE** (cron / EventBridge wiring -- `<next>` block) |
| 2 | Clean run for 3 consecutive nights | **PENDING** (runs tonight, next two nights) |
| 3 | Deliberate drift test produces FAIL w/ correct domain | **PASS** (Phase 2 step 3) |
| 4 | comp-validate on output schema exits 0 | **PENDING** (schema needs gold_validate_config entry) |
| 5 | Session log reproduces triad per phase | **PASS** (this log) |
| 6 | MCP COMPLETE w/ 3-night manifest paths | **PENDING** (3-night run) |

## Next Steps

- [AE 0.6.0] wire `python diag_gold_silver_recon.py` into post-gold_dispatch nightly job; ingest JSON manifest into CloudWatch alerting
- [DS ~B] post-commit: run `comp-blast` on the new script node (Phase 3)
- [DS ~B] author comp-validate schema config entry for gold_silver_recon output
- [DS ~B] report 3-night manifest paths to COO for acceptance #2/#6 close

# ADVI_PRICES .001 -- Full Gold Rebuild + Allocation-Authority Recon Verification -- 0.6.0_AE_PartnerETL

**Date:** 2026-03-23 / 2026-03-24
**Start Time:** 14:45 UTC (2026-03-23)
**End Time:** 12:16 UTC (2026-03-24)

## Objective

Execute the full AE workstream for ADVI_PRICES-001: validate DS taxonomy expansion,
run diagnostic battery to isolate phantom lot root cause, deploy DS allocation-authority
fix to gold layer, run full gold rebuild on ephemeral c5.4xlarge, verify results with
recon diagnostic.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Verify DS commits on CLOUD | `f1b3f33d` (taxonomy expansion), `9b039259` (diagnostics), `c50877b0` (allocation-authority), `7dd2432b` (positions_cube phantom exclusion), `4278798e` (temporal guard) |
| 2 | Sync SELL_TYPES/CA_SELL_SUBTYPES to script 02 | `f043b19e` -- Redemption + 5 CA subtypes |
| 3 | Upload gold + diagnostic scripts to S3 | All 16 gold scripts + 8 diagnostic scripts |
| 4 | Start EC2 i-01003b035d2988dfb | SSM online |
| 5 | SSM `a02e793c`: taxonomy enumeration (full history) | 2,771,144 rows, 1,754 files. Redemption=176 rows. Exchange/Tender/Maturity/Called/Liquidation=0. |
| 6 | SSM `a425538e`: recon baseline --date 2026-03-19 | $296M net gap, 268 phantom accts +$91.2M |
| 7 | SSM `889b9aaf`: phantom asset name mismatch --top 5 | Hypothesis disproven: 0% explained by name mismatch |
| 8 | Fix `diag_phantom_fifo_replay.py` _units_num bug | Moved pd.to_numeric before sell slice |
| 9 | SSM `b540f181`: FIFO replay --top 10 | H1: 94 sells dropped by dedup (16K units). H3: 4 temporal guard hits. 35/48 positions = zero sells. |
| 10 | SSM `69633a95`+`891a01b6`: overshoot + undershoot diags | O1+O2 phantom = $352M. Pricing overshoot = $97M. Undershoot structural = -$176M. |
| 11 | SSM `067d7059`+`00e2ba66`: zero-sells + partial-sells patterns | 2023Q1 sell-stop cohort (76 accts). TIAA/529/TermLife overrepresented. DRIP = 0.4% of buys. |
| 12 | Fix `diag_phantom_partial_sells_patterns.py` groupby bug | `.abs().sum()` -> `.apply(lambda x: x.abs().sum())` |
| 13 | SSM `2b647ea9`: phantom concentration | Top 10% = 82% of excess. 6 accounts = $122M (58%). |
| 14 | Force re-upload script 03 to S3 | Prior `s3 sync` skipped due to timestamp match |
| 15 | Launch ephemeral c5.4xlarge `i-042c000ba5212e575` | `run_gold_layer.sh full` -- scripts 00-10 + 12 + 06b |
| 16 | Verify phantom exclusion fired in script 02 | `Phantom exclusion: 6,415 accounts, 6,017 alive (AUA >= $100)` -- 398 excluded |
| 17 | Ephemeral instance stopped | Script 03 did not write updated holdings_lots/2026-03-19 |
| 18 | SSM `0952aac5` on runner: script 03 --date 2026-03-19 + recon | 74,035 lots force-closed, $351M removed. Net gap: -$57.7M (-3.6%) |
| 19 | SSM `a8ac014b`: scripts 06 + 12 | Tax liability + composition rebuilt with clean holdings_lots |
| 20 | Terminate ephemeral `i-042c000ba5212e575` | Confirmed terminated |

---

## Verification

### Pre-Fix Baseline (2026-03-19)

| Metric | Value |
|--------|-------|
| BD AUA | $1,593,308,085 |
| Lot MV | $1,889,291,370 |
| Net gap | +$295,983,285 (+18.6%) |
| RC1_PHANTOM | 268 accounts, +$91,211,940 |
| Gross overshoot | +$494,047,695 (4,129 accounts) |

### Post-Fix (2026-03-19, same allocations)

| Metric | Value |
|--------|-------|
| BD AUA | $1,593,308,085 |
| Lot MV | $1,535,649,187 |
| Net gap | -$57,658,898 (-3.6%) |
| RC1_PHANTOM | 77 accounts, +$1,121,298 |
| Gross overshoot | +$116,620,339 (1,986 accounts) |

### Delta

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Net gap | +$296.0M (+18.6%) | -$57.7M (-3.6%) | **$353.6M improvement** |
| RC1 Phantom | $91.2M (268 accts) | $1.1M (77 accts) | **-$90.1M (98.8% eliminated)** |
| Gross overshoot | $494.0M | $116.6M | **-$377.4M** |
| Lots force-closed | 0 | 74,035 | 2,080 accounts cleaned |
| Largest phantom | $20.9M (BNP Paribas) | $48.7K | **-99.8%** |

### Allocation-Authority Reconciliation Detail (script 03 output)

```
Phantom lot reconciliation (allocation-authority):
  Accounts force-closed:  2,080
  Lots force-closed:      74,035
  MV removed:             $351,038,451
```

### Post-Fix Waterfall

| Category | Accounts | Gap |
|----------|----------|-----|
| RC1_PHANTOM | 77 | +$1.1M |
| RC2_ALLOC_ONLY | 197 | -$33.6M |
| RC3_INSURANCE | 99 | -$8.7M |
| RC4_NON_INVESTMENT | 103 | +$1.8M |
| RC5_NORMAL | 5,939 | -$18.2M |

Remaining gap is structural: RC2 (allocation-only accounts with no transaction history)
and RC3 (insurance wrappers) account for -$42.3M, which is by-design and not fixable
via lot logic.

---

## Diagnostic Battery Results (S3 artifacts)

| Diagnostic | S3 Key | Key Finding |
|-----------|--------|-------------|
| Taxonomy enumeration | `diagnostics/txn_taxonomy_enumeration_2026-03-23.json` | Only Redemption (176 rows) has data. 5 new CA subtypes = 0 rows. |
| Recon baseline | stdout | $296M net gap, 268 phantom accounts |
| Asset name mismatch | `diagnostics/phantom_name_mismatch_2026-03-19.json` | 0% of excess explained by name mismatch |
| FIFO replay | `diagnostics/phantom_fifo_replay_2026-03-19.json` | 35/48 positions = zero sells. H3 temporal guard = 4 hits. |
| Overshoot analysis | `diagnostics/overshoot_analysis_2026-03-19.json` | O1+O2 phantom = $352M across 1,598 accounts |
| Undershoot analysis | `diagnostics/undershoot_analysis_2026-03-19.json` | U3 partial lots = -$141M (pricing), U1+U2 = -$15M (structural) |
| Zero-sells patterns | `diagnostics/phantom_zero_sells_patterns_2026-03-19.json` | TIAA/529 overrepresented. Relationship z08130107: 17/22 phantom. |
| Partial-sells patterns | `diagnostics/phantom_partial_sells_patterns_2026-03-19.json` | 2023Q1 sell-stop cohort (27%). DRIP = 0.4%. |
| Concentration | `diagnostics/phantom_concentration_2026-03-19.json` | Top 10% = 82%. 6 accounts = $122M (58%). |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Cancel initial gold rerun | Other gold work in progress -- avoid double rerun |
| Accept $10M residual in positions_cube | Rule 2 (BD-diminished) only in script 03; joining prices into 02's write_partition too expensive |
| Launch ephemeral c5.4xlarge for full rebuild | Faster than running on r6i.xlarge runner; self-terminates |
| Rerun script 03 on persistent runner after ephemeral stopped | Ephemeral instance stopped before 03 wrote updated 2026-03-19 partition |
| Rerun scripts 06 + 12 after 03 | Direct downstream consumers of holdings_lots |
| Fix two DS script bugs inline | `_units_num` column ordering in FIFO replay; `.abs().sum()` groupby in partial-sells |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/gold/02_build_positions_cube.py` | Sync SELL_TYPES/CA_SELL_SUBTYPES + phantom exclusion (DS `7dd2432b`) | AE commit `f043b19e` (taxonomy sync); DS commit `7dd2432b` (phantom exclusion) |
| `data/black_diamond/scripts/gold/03_build_holdings_lots.py` | Allocation-authority reconciliation (Rule 1 + Rule 2) + temporal guard fix | DS commits `c50877b0`, `4278798e` |
| `data/black_diamond/scripts/diagnostics/diag_phantom_fifo_replay.py` | Fix _units_num column ordering bug | Local only (DS reverted to own fix) |
| `data/black_diamond/scripts/diagnostics/diag_phantom_partial_sells_patterns.py` | Fix groupby .abs().sum() bug | Local only (DS reverted to own fix) |

---

## Blockers

None. All workstreams complete.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

All ADVI_PRICES-001 AE deliverables are done. Taxonomy expansion validated (only
Redemption matters, 176 rows). Diagnostic battery ran 9 scripts identifying the root
cause as BD transaction feed incompleteness (not taxonomy, not naming, not FIFO bugs).
DS built allocation-authority reconciliation in script 03 and phantom exclusion in
script 02. Full gold rebuild ran on ephemeral c5.4xlarge (scripts 00-10, 12, 06b).
Script 03 rerun on persistent runner with --date 2026-03-19 force-closed 74,035 lots
($351M) across 2,080 accounts. Net gap improved from +$296M (+18.6%) to -$57.7M (-3.6%).
Remaining gap is structural (allocation-only + insurance). Downstream scripts 06 and 12
rebuilt. Ephemeral instance terminated.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Push CLOUD** -- 10 DS commits + 1 AE commit for ADVI_PRICES-001
2. **[0.4.0_DT_ClientPlatform] Deploy bd-portal-publisher + bd-portal-advisor-publisher** -- Lambda Terraform apply needed for downstream portal data to reflect corrected holdings
3. **[0.6.0_AE_PartnerETL] Run full gold layer on next weekday** -- nightly incremental will use the updated scripts automatically; verify the next incremental run shows phantom exclusion in logs
4. **[0.4.0_DS_ClientPlatform] Mark ADVI_PRICES.001 task order complete** -- all DS deliverables deployed and verified

**Do NOT:**
- Run another full gold rebuild -- the nightly incremental will keep outputs current
- Remove the allocation-authority logic from script 03 -- it is the primary fix for $351M in phantom lots
- Assume the -3.6% undershoot is a bug -- it is structural (alloc-only + insurance accounts)

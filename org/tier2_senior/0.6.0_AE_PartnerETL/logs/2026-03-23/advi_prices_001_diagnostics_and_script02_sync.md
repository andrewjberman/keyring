# ADVI_PRICES .001 -- Taxonomy Sync, Enumeration, Recon Baseline, Phantom Root Cause -- 0.6.0_AE_PartnerETL

**Date:** 2026-03-23
**Start Time:** 14:45 UTC
**End Time:** 15:25 UTC

## Objective

Execute AE workstreams for ADVI_PRICES-001 after DS delivered taxonomy expansion
(commit `f1b3f33d`) and diagnostic scripts (commit `9b039259`). Sync allowlist
changes to script 02, run taxonomy enumeration against full history, run baseline
recon diagnostic, and run phantom asset name mismatch hypothesis test.

Gold layer rerun (WS2) deferred -- other gold work in progress, will combine into
a single rerun.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Verify DS commits on CLOUD | `f1b3f33d` (script 03 taxonomy) + `9b039259` (recon + enum scripts) confirmed |
| 2 | Sync SELL_TYPES/CA_SELL_SUBTYPES to script 02 | `f043b19e` feat(gold): sync expansion to script 02 |
| 3 | Upload gold scripts to S3 | `aws s3 sync` -- 5 files uploaded (02, 03, 06b, 12, detect_new_securities) |
| 4 | Upload diagnostic scripts to S3 | recon_lots_vs_allocations.py, diag_txn_taxonomy_enumeration.py, diag_phantom_asset_name_mismatch.py |
| 5 | Start EC2 i-01003b035d2988dfb | Was stopped, started to pending->running, SSM online |
| 6 | SSM `a02e793c`: taxonomy enumeration (full history) | Success -- 2,771,144 rows, 1,754 files |
| 7 | SSM `a425538e`: recon baseline --date 2026-03-19 | Success -- waterfall + top 20 phantom drill-down |
| 8 | SSM `889b9aaf`: phantom asset name mismatch --top 5 | Success -- hypothesis largely disproven |
| -- | SSM `677ae436`: full gold layer rerun | **Cancelled** -- other gold work in progress |

---

## Verification

### WS1: Taxonomy Enumeration (full history)

Enumeration output saved to `s3://opal-data-bd/diagnostics/txn_taxonomy_enumeration_2026-03-23.json`.

Newly added types from DS expansion and their actual frequency:

| Type | SubType | Rows | Accounts | Net Units |
|------|---------|------|----------|-----------|
| Sale | Redemption | **176** | 81 | 7,805,107 |
| Corporate Action | Exchange | **0** | 0 | 0 |
| Corporate Action | Tender | **0** | 0 | 0 |
| Corporate Action | Maturity | **0** | 0 | 0 |
| Corporate Action | Called | **0** | 0 | 0 |
| Corporate Action | Liquidation | **0** | 0 | 0 |

Zero unrecognized exit-like types (no negative-unit types outside allowlists).
Conclusion: Redemption (176 rows, 81 accounts) is the only expansion with real data impact.
The 5 CA subtypes are insurance against future data.

### WS3 Baseline: Recon 2026-03-19 (pre-rerun)

| Metric | Value |
|--------|-------|
| BD AUA total | $1,593,308,085 (6,219 accounts) |
| Lot MV total | $1,889,291,370 (7,773 accounts) |
| Net gap | +$295,983,285 (+18.6%) |
| Gross overshoot | +$494,047,695 (4,129 accounts) |
| Gross undershoot | -$198,064,410 (4,008 accounts) |

Waterfall:

| Category | Accounts | Gap | Notes |
|----------|----------|-----|-------|
| RC1_PHANTOM | 268 | +$91,211,940 | Stale lots, BD near-zero AUA |
| RC2_ALLOC_ONLY | 108 | -$25,592,607 | BD has AUA, we have $0 lots |
| RC3_INSURANCE | 99 | -$8,735,755 | Opaque wrappers |
| RC4_NON_INVESTMENT | 103 | +$2,049,373 | Bank/Savings/Loan noise |
| RC5_NORMAL | 7,632 | +$237,050,333 | Pricing + partial exit residuals |

NOTE: This baseline uses the **old** holdings_lots (pre-taxonomy-expansion gold rerun).
The net gap here is $296M vs COO's original $68M because this is same-date recon on
2026-03-19, but the lot MV includes all accounts (not just those in allocations).
After gold rerun with expanded taxonomy, RC1 may decrease modestly (Redemption covers
81 accounts) but the bulk of phantom excess is not taxonomy-driven.

### Phantom Asset Name Mismatch Hypothesis

Output saved to `s3://opal-data-bd/diagnostics/phantom_name_mismatch_2026-03-19.json`.

| Metric | Value |
|--------|-------|
| Accounts analyzed | 5 (top phantom by excess) |
| Total phantom excess (top 5) | $52,763,695 |
| Accounts with orphan sell groups | 3 |
| Accounts with fuzzy name matches | 1 (false positive) |
| Excess explained by name mismatch | $0 (the 1 match was Vanguard Growth vs Value -- different funds) |

**Hypothesis disproven.** The dominant pattern is partial exits -- buys and sells exist
under the same asset name, but sells only deplete 30-70% of bought units. BD's
allocation drops the account to near-zero while our FIFO still holds the remaining
units as open lots. The transaction feed never sent the final exit events.

Root cause is inconsistency between BD's allocation feed (position-level snapshot) and
transaction feed (event stream). Allocations reflect closures/transfers that never
appeared as sell transactions.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Sync script 02 allowlists before gold rerun | 02 and 03 must agree; DS comment in 03 says "02 defines these identically" |
| Cancel gold rerun | Other gold work in progress -- will combine into single rerun to avoid running twice |
| Fix non-ASCII arrows in script 02 | CLAUDE.md rule 13 -- replaced arrow chars with ASCII dashes |
| Run phantom name mismatch on top 5 only | DS requested top 5; sufficient to validate/invalidate hypothesis |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/gold/02_build_positions_cube.py` | Sync SELL_TYPES + CA_SELL_SUBTYPES expansion from script 03; fix non-ASCII arrows | Yes -- `f043b19e` |

---

## Blockers

- Gold layer rerun (WS2) deferred until other gold work completes. Scripts are uploaded to S3 and ready; just need SSM `run_gold_layer.sh full`.

---

## Current State

**Status:** IN PROGRESS (WS1 complete, WS2 deferred, WS3 baseline captured)
**Active branch:** `CLOUD`

Script 02 taxonomy sync committed (`f043b19e`). All gold scripts and diagnostics
uploaded to S3. Three diagnostics run on EC2: taxonomy enumeration confirms only
Redemption (176 rows) has data; recon baseline captures the $296M gross gap; phantom
name mismatch hypothesis disproven (0% of excess explained). DS is continuing to
investigate the true root cause -- likely an allocation-authority reconciliation layer
rather than taxonomy or name normalization. Gold rerun deferred pending completion of
other gold work. EC2 i-01003b035d2988dfb is running.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Continue phantom root cause investigation** -- DS designing the reconciliation layer (allocation-authority lot closure vs taxonomy/name-norm)
2. **[0.6.0_AE_PartnerETL] Run full gold layer rerun** -- when other gold work completes, SSM `run_gold_layer.sh full` on i-01003b035d2988dfb. Scripts already on S3.
3. **[0.6.0_AE_PartnerETL] Post-rerun recon** -- run `recon_lots_vs_allocations.py --date {new_date}` and compare to 2026-03-19 baseline to quantify Redemption impact
4. **[0.4.0_DT_ClientPlatform] Push commit `f043b19e`** -- script 02 sync needs to reach remote

**Do NOT:**
- Run gold rerun until other gold work is complete (would need to run twice)
- Assume taxonomy expansion will significantly reduce phantom excess (only 176 Redemption rows in full history)
- Stop EC2 instance if gold rerun is imminent -- save the startup cycle

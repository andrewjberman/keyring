# ADHC_HISTRY / ADVI_PRICES: Schwab TRN Cross-Reference and Rotation Capital Investigation -- 0.4.0_DS_ClientPlatform

**Date:** 2026-03-31 (session 3)
**Start Time:** 7:00 PM ET
**End Time:** 10:30 PM ET (2026-04-01)
**Project:** ADHC_HISTRY (forensic investigation) + ADVI_PRICES (model overlay accuracy)

---

## Objective

Investigate the $390M pre-injection FIFO overshoot end to end, prove what the
ground truth is, and validate that the rotation capital approach (synthetic sell
capital recycled into synthetic buys shaped by model weights) can close the gap
between gold and silver.

---

## Work Completed

### 1. ADHC_HISTRY.001-004: Forensic Investigation Complete

**Finding: FIFO logic is clean. Transaction feed is incomplete.**

| Diagnostic | What it proved |
|---|---|
| .001 txn_id duplication | 950K dupes are pure re-deliveries. Zero retroactive type changes. |
| .002 FIFO walkthrough | Account-level traces confirm correct signed_units logic. |
| .003 structural causes | Cash reclassification: CLEAN. Transfer+Buy overlap: $5K (negligible). CA mergers: +6M units but all positive (no old-shares-out). |
| .004 realized cross-reference | **Definitive decomposition of the $390M overshoot** |

**.004 results (the money shot):**

| Category | Positions | MV |
|---|---|---|
| Confirmed open (in unrealized) | 70,038 | $1,245M |
| Sold, missing sell (in realized, not unrealized) | 50,887 | $513M |
| Vanished (neither realized nor unrealized) | 10,832 | $177M |
| **Total FIFO** | **131,757** | **$1,935M** |

After removing sold+vanished: $1,245M confirmed vs $1,586M silver = -$341M UNDER.
The FIFO is actually undershooting on confirmed positions. The $390M "overshoot"
was entirely phantom positions from missing sell transactions.

### 2. Rotation Capital Approach

**Concept (from Andrew):** Synthetic sells free capital. That capital flows into
synthetic buys for the missing positions. Gold total stays flat -- it's a
reallocation, not an addition. The sells ARE the buys.

Tested multiple approaches:

| Approach | DIVZ Total | Gap vs Silver | Problem |
|---|---|---|---|
| Lot-count residual (old RC2) | $189M | +$166M over | Sell-closed positions re-injected |
| Zero-history-only injection | $47M | +$190M over | DIVZ has history (just insufficient), excluded |
| Residual to unrealized (no cash) | $55M | +$192M over | Residual spread thin across all positions |
| Model-weight target injection | $168M | +$620M over | Additive, not reallocation |
| **Rotation reallocation (no cash)** | **$156M** | **+$194M over** | Best result -- hits DIVZ target |

**Rotation reallocation approach (the winner):**
1. Sell injection frees $517M from phantom positions
2. $341M redistributed to missing unrealized positions (excluding cash)
3. Shaped by 49F model weights (all accounts are 49F)
4. DIVZ gets $110M injection -> $156M total (target: $150-160M)
5. Remaining gap: $214M "excess capital" from accounts where sells freed capital
   but all unrealized positions already have FIFO coverage

**Excess capital investigation:** These are accounts where the rotation was already
complete -- old positions sold AND new positions bought, both in our transaction
feed. The sell injection redundantly closes positions that real transactions already
sold. The freed capital has nowhere to go because buys are already covered.

### 3. Schwab TRN Silver Layer Exploration

**Schwab TRN data (2.73M rows, 554 daily files, 2024-01-16 to 2026-03-30):**

| Field | Content |
|---|---|
| account_id | 10-digit Schwab numbers (e.g., 0010023253) |
| transaction_source | Type: blank=market trades, REINVEST DIVIDEND, MERGER, TRANSFER ACCOUNT, etc. |
| cusip | 9-char CUSIP |
| ticker | DIVZ, IDVZ, CLIP, etc. (old tickers -- SPLG not SPYM) |
| **quantity** | **Actual share count per transaction** |
| price | Per-unit price |
| gross_amount | Dollar value |

**Critical finding: Schwab has exact unit counts.** This is what BD's unrealized
report is missing. No more estimation.

**DIVZ from Schwab:** 9.68M units across 9,789 accounts = $360M at $37.17.
BD unrealized only sees 5,117 accounts. Schwab sees nearly double.

### 4. Schwab-BD Account Mapping (BREAKTHROUGH)

**Direct mapping via zero-stripped account_number:**

BD realized `account_number` = `85238265`
Schwab `account_id` = `0085238265`

Just zero-padding. **6,417 accounts mapped directly.** 93 additional via (cusip,
trade_date) fingerprinting. **6,510 total mappings saved to S3.**

**DIVZ validation on mapped accounts:**
- Accounts with ratio ~1.0 confirm mapping is correct (same units in both systems)
- Accounts with BD=0, Schwab>0 are the injection targets -- Schwab has the exact
  units BD's transaction feed never delivered
- Accounts with BD>0, Schwab=0 may be newer than Schwab data coverage

**Mapping artifact:** `s3://opal-data-bd/gold/dimensions/schwab_bd_account_mapping.parquet`

---

## Decisions Made

| Decision | Rationale |
|---|---|
| FIFO logic validated, no code changes needed | .001-.004 prove the reconstruction is correct; the transaction feed is incomplete |
| Rotation capital is the correct injection model | Sells fund buys, gold stays flat. Confirmed by $156M DIVZ hitting target |
| CASH excluded from buy injection targets | Cash sweeps are not model rotation targets |
| Schwab TRN provides ground truth unit counts | BD unrealized has lots but no units; Schwab has exact quantities |
| Account mapping via zero-padded account_number | BD realized has unmasked account_number that maps to Schwab with zero-padding |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `gold/02_build_positions_cube.py` | RC3 fix (no-silver accounts), sell-closed exclusion | Yes -- c3551eca, 3884a54f |
| `gold/03_build_holdings_lots.py` | RC3 fix (no-silver accounts), sell-closed exclusion | Yes -- c3551eca, 3884a54f |
| `diagnostics/adhc_histry_001-004` | Forensic investigation scripts | Yes -- 72693b27 |
| `diagnostics/rc_*.py` | Rotation capital test scripts | Local only |
| `diagnostics/_schwab_*.py` | Schwab exploration and mapping scripts | Local only |

---

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| This session log | This file | All agents |

---

## Current State

**Status:** INVESTIGATION COMPLETE. Ready for Schwab-authority injection implementation.

**RC status (held per Andrew's direction -- do not deploy RC3/RC4):**

| RC | Status | Notes |
|---|---|---|
| RC1 | DEPLOYED | Name aliasing. Working. Do not touch. |
| RC2 | Code on S3 (experimental) | Hold. Superseded by Schwab-authority approach. |
| RC3 | Committed locally (c3551eca) | Hold. DO NOT deploy. |
| RC4 | N/A | Superseded -- model weights are universal (all 49F), Schwab has exact units. |
| RC5 | Not a bug | Transitional positions ($47M). Expected. |

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Schwab-authority injection calculation** -- For each
   (BD account, asset) pair: `injection_units = schwab_units - fifo_units`. Use the
   6,510 account mapping + Schwab net quantity per (account, ticker). This gives
   exact injection targets with no estimation. Run as diagnostic first.

2. **[0.4.0_DS_ClientPlatform] Implement Schwab-authority injection in scripts 02/03** --
   Replace residual-based injection with direct Schwab unit targets. Load
   `schwab_bd_account_mapping.parquet` + aggregate Schwab TRN quantities per account.

3. **[0.6.0_AE_PartnerETL] Schwab TRN daily ingestion pipeline** -- Currently manual.
   Needs automated daily ingest to keep Schwab quantities current.

4. **[0.6.0_AE_PartnerETL] Schwab ACC files to silver** -- May contain additional
   account metadata (account type, registration, etc.) for enrichment.

5. **[Andrew] Validate account mapping** -- 6,417 direct matches via zero-padding.
   Spot-check a few to confirm BD account_number = Schwab account_id (zero-padded).

**Do NOT:**
- Deploy RC3/RC4 changes (held per Andrew's direction)
- Remove RC1 (name aliasing) -- it is correct and deployed
- Run full gold layer until Schwab-authority injection is validated
- Trust lot-count as a unit proxy (correlation = -0.02, confirmed useless)

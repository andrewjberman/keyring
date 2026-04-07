# GLDOPS.004 — AUA Reconciliation Discovery: FIFO Ghosts and the Model Rotation

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-06
**Project:** ADVI_GLDOPS
**Task Order:** ADVI_GLDOPS.004

---

## Discovery Timeline

### Starting point: $1.875B canonical vs $1.632B silver allocations (+14.9%)

02b's initial dry run produced $1.875B canonical AUA — $243M above BD's silver allocations. Investigation began to find the source of inflation.

### Step 1: Decomposed by source category

```
bd (BD-only):           $435M  — non-Schwab accounts
reconciled:             $685M  — both agree
schwab_override:        $562M  — both present, Schwab units used (higher than BD)
schwab (gap-fill):      $176M  — Schwab has position, BD cube does not
```

The $176M schwab gap-fill was the primary inflation driver.

### Step 2: Investigated the gap-fill positions

The top gap-fill assets were all Opal model portfolio holdings:
- DIVZ (POLEN DIVIDEND INCOME ETF): $102M across 3,299 accounts
- SPYM (S&P 500 ETF): $33M across 1,685 accounts
- IEFA: $13M, IEMG: $8M, etc.

All 3,599 accounts with gap-fill positions were in BD's accounts_dimension, had cube positions for other assets, and were in silver allocations. BD knew about these accounts — the cube just didn't have certain positions.

### Step 3: Andrew identified the root cause

Andrew pointed out we might be double-counting. Investigation confirmed: BD's silver allocations already values these accounts correctly (reads BD's position valuation directly, not FIFO replay). The Schwab gap-fill was adding AUA on top of what silver already counted.

### Step 4: First fix — BD units as AUA authority

Changed 02b to use BD units for the canonical `units` column. Schwab gap-fill positions excluded (units=0). Result: $1.655B canonical, +1.5% vs silver. No more double-counting.

But $174M in gap-fill positions were dropped entirely — losing diagnostic intelligence about where the cube has gaps.

### Step 5: Colleague validation — discovered the model rotation

Validation session traced the gap-fill positions to a specific event: **April 24-30, 2024 model portfolio rotation**. ~879 accounts sold old model (ACWI, DFAS, REET, BNDW) and bought new model (DIVZ, PDBC, COWZ, IQLT, VTV, QUAL).

BD's transaction ingestion captured the sells (old positions disappeared from cube) but NOT the buys (new positions never appeared). Schwab RPS captured both sides day-by-day.

The cube was carrying stale "ghost" positions of the old model for Schwab-covered accounts where the custodian confirmed those positions no longer exist.

### Step 6: Introduced `bd_stale` source classification

For any BD-only position where the account has Schwab coverage but Schwab doesn't report that position: **the position is a FIFO ghost**. Schwab is the custodian — if they don't see it, it's not there.

```python
schwab_covered = set(schwab_df['account_id'].unique())
# BD-only + account is Schwab-covered + Schwab doesn't have this position = stale
source[has_bd & ~has_schwab & is_schwab_covered] = 'bd_stale'
merged.loc[merged['source'] == 'bd_stale', 'units'] = 0
```

For Schwab-covered accounts, Schwab units are now authoritative (reconciled, override, and gap-fill all use Schwab units). For non-Schwab accounts, BD units remain the only source.

### Step 7: Final result

```
$1.604B canonical AUA (-1.7% vs silver allocations $1.632B)

Source distribution:
  reconciled        44,647  (52.2%)  — BD + Schwab agree
  schwab_override   27,925  (32.6%)  — Schwab corrects BD units
  schwab             8,630  (10.1%)  — real positions cube missed
  bd                 4,344  ( 5.1%)  — non-Schwab accounts

Gaps diagnostic:     8,382 bd_stale positions (FIFO ghosts, zeroed)
```

The -1.7% delta (canonical below silver) is canonical_prices vs BD's own pricing — same magnitude as before, just in the other direction now that Schwab units are authoritative for Schwab-covered accounts.

---

## Three Guards Implemented

### 1. Self-heal `isdigit()` guard
Text-format account_numbers like "403506 UNIVERSITY OF REDLANDS" were being zero-padded into false Schwab IDs. Added `acct_num.isdigit()` check. Reduced self-heal from +1,534 to +1,254.

### 2. False-positive mapping filter
`filter_false_mappings()` — removes mapping pairs where Schwab AUA / silver AUA > 5x. Catches 158 v3 fingerprint matcher errors ($60M excess). Institutional/retirement accounts incorrectly matched to unrelated Schwab brokerage accounts.

### 3. `bd_stale` detection
BD-only positions in Schwab-covered accounts are FIFO ghosts — zeroed in canonical, preserved in `gold/canonical/holdings_gaps/{date}.parquet` for audit.

---

## AUA Progression Through Fixes

| Fix | Canonical AUA | vs Silver ($1.632B) |
|-----|--------------|-------------------|
| Original (Schwab wins all) | $1.875B | +14.9% |
| BD units as authority | $1.655B | +1.5% |
| + bd_stale zeroing + Schwab authoritative for covered accounts | $1.604B | -1.7% |

The final -1.7% is a clean pricing methodology delta, not structural inflation.

---

## Related Briefs

- `briefs/2026-04-06_account_mapping_gap_brief.md` — 335 unmapped accounts (resolved by self-healing)
- `briefs/2026-04-06_canonical_stack_session_brief.md` — full session summary
- Model rotation ghost positions brief (from validation session) — identified the April 2024 rotation as root cause

---

## Key Insight

The positions_cube (script 02) is a FIFO reconstruction from transaction history. When transactions are missing (buy-side of a rotation not ingested), the cube carries ghosts of old positions and misses new ones. Silver allocations reads BD's current position valuation directly and is correct. Schwab RPS is the custodial source of truth for Schwab-covered accounts.

Canonical holdings now uses three tiers of authority:
1. **Schwab-covered accounts**: Schwab units are authoritative (custodian of record)
2. **Non-Schwab accounts**: BD units are the only source
3. **FIFO ghosts**: detected by Schwab coverage gap, zeroed with audit trail

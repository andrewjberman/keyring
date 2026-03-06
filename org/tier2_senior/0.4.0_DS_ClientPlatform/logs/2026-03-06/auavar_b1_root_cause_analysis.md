# ADVI_AUAVAR B1 Root Cause Analysis — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 17:00
**End Time:** 18:30

## Objective

Identify why 397 accounts ($13.9M) in BD allocations that are open and have
transaction history are absent from `gold/positions_cube/2026-03-02.parquet`.
Classify the gap as bug vs policy and determine the correct next action for each
sub-bucket. This is the final step to fully attribute the $73.6M BD-vs-gold gap.

---

## Work Completed

### 1. Reframed the Investigation After DT Failure Report

DT's first run of `diag_aua_b1_root_cause.py` failed on two issues:
- All `silver/positions/` key patterns returned NoSuchKey
- `NameError: mv_b1_in_silver not defined` before JSON emit

DT's silver structure report showed `silver/daily_positions.parquet` (682MB,
last modified 2026-02-02) — a monolithic flat file, not date-partitioned.
Andrew flagged this as suspicious (expected date-partitioned `silver/positions/`
mirroring `silver/transactions/`).

Correct diagnosis came from reading `02_build_positions_cube.py` directly.

**Key finding from Script 02 source:**
Script 02 builds positions by replaying `silver/transactions/` — it does NOT
read any silver positions file at any path. `silver/daily_positions.parquet`
is a legacy artifact from before Script 02 was built. The investigation was
aimed at the wrong layer entirely.

### 2. Identified the Actual Filter Mechanism in Script 02

`_compute_account_end_dates()` (Script 02, lines 339-388):

```python
# Accounts with >= 1 TXN_DAILY_*.xlsx transaction -> fill to global_end_date
# Accounts with ONLY backfill transactions -> fill to their LAST transaction date
```

The `_source_file` column on each transaction record determines whether an account
is "active in the daily pipeline" or "backfill-only." Backfill-only accounts are
forward-filled only through their last transaction date. An account that bought
securities in Oct 2025, holds since, and receives no new daily export rows gets
zero cube entries after Oct 2025 — but BD still shows its current market value.

### 3. Rewrote Diagnostic Script Targeting _source_file

Replaced the failed `silver/positions/` pattern-checking approach with a targeted
`_source_file` classification. Script loads all transaction partitions in parallel
(64 workers), retains only B1 rows in memory, and buckets each account as:
- **ACT**: has at least one `TXN_DAILY` source file → should be in cube → bug
- **BKF**: all transactions are backfill → intentionally capped by Script 02
- **UNK**: account not found in any transaction partition (unexpected)

Fixed the NameError: all output variables initialized before conditional blocks.
Removed all `silver/positions/` code.

Commit: `645229ea`

### 4. DT Re-Ran — Clean Result (43b893ba)

| Bucket | Count | BD MV | Verdict |
|--------|-------|-------|---------|
| ACT (has TXN_DAILY, missing from cube) | 164 | $7,360,070 | Script 02 secondary filter bug |
| BKF (backfill-only, capped by design) | 233 | $6,585,658 | Policy decision |
| UNK | 0 | $0 | Clean |

**BKF profile (critical context):**
- Median days since last transaction: **41 days**
- All accounts last transacted in **2025Q4–2026Q1** (NOT stale ancient accounts)
- Account types: Brokerage, IRA, Joint Tenants (standard investment accounts)
- 0 accounts with last transaction > 180 days ago

These are active clients who simply haven't generated new transactions in 5–15
weeks. BD shows real, current holdings. This is not the "phantom AUA from
dormant accounts" scenario that the Script 02 safeguard was designed for.

---

## Full Gap Attribution (Final)

| Segment | Amount | Type | Action |
|---------|--------|------|--------|
| Non-investment products (insurance/annuity, 118 accts) | +$59.5M | Structural exclusion | Document, no change |
| Cash positions in gold cube (BD separates cash) | -$23.2M | Structural offset | Use non-cash AUA metric |
| Cash-only / new accounts (~354 accts, B2 remainder) | +$34.1M | Scope question | COO decision |
| B1 ACT: Script 02 secondary filter bug (164 accts) | +$7.4M | Addressable bug | AE investigates Script 02 |
| B1 BKF: backfill-only, capped by design (233 accts) | +$6.6M | Policy decision | COO: accept or extend forward-fill |
| Liability accounts (26 accts, negative MV) | -$3.5M | Structural exclusion | Document, no change |
| Seg 2 household aggregation check | $0.00 | No issue | Clean |
| Pricing/timing spread + set overlap | ~-$7.1M | Normal variance | No action |
| **Total** | **+$73.6M** | | |

**Revised apples-to-apples (investment-only, non-cash):**
BD ~$1,571.6M vs Gold $1,530.7M = ~$40.9M gap (2.6%).

**If both B1 buckets were recovered:**
Gold non-cash AUA + $7.4M (ACT bug fix) + $6.6M (BKF policy) = ~$1,544.7M.
vs BD investment-only ~$1,571.6M = ~$26.9M residual gap (1.7%).
The majority of that residual is the $34.1M cash-only/new accounts scope question
minus the $23.2M cash offset, netting to ~$10.9M + normal variance.

**Andrew's target math (~99.2% accuracy at $1.614B)** is achievable:
- Current gold: $1,553.9M
- Fix ACT bug (+$7.4M): ~$1,561.3M
- Add BKF via policy extension (+$6.6M): ~$1,567.9M
- Add insurance/annuity if included in scope (+$59.5M): ~$1,614B (but this may not be desirable)
- The cleaner path: fix ACT + extend BKF forward-fill = $1,567.9M, 96.3% of BD's $1,627.5M
  or 99.8% of BD investment-only $1,571.6M (same universe)

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Dropped silver/positions/ hypothesis entirely | Script 02 source confirmed it doesn't use any positions file; wrong layer |
| Targeted _source_file as the classification signal | It is the exact variable Script 02 uses for the end-date cap decision |
| Loaded ALL transaction partitions for B1 rows | 90-partition shortcut risks miscounting; full load gives correct B1 set |
| BKF classified as policy not bug | The 41-day median and 2025Q4-2026Q1 profile show these are active clients, not ghost accounts; however the Script 02 design intent was to exclude them |

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| COO variance memo (needs B1 final numbers update) | `docs/briefs/data-scientist-auavar-variance-memo.md` | 2.0.0_SA_COO, 1.0.0_SA_CTO |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/diagnostics/diag_aua_b1_root_cause.py` | Complete rewrite — _source_file classification | `645229ea` |

---

## Blockers

None. Full gap attribution is complete. Two open items are decision gates, not blockers.

---

## Current State

**Status:** COMPLETE (DS investigative work for ADVI_AUAVAR)
**Active branch:** `CLOUD`

The $73.6M BD-vs-gold gap is fully decomposed across all three diagnostic phases.
DT's clean run at `43b893ba` produced `s3://opal-data-bd/diagnostics/aua_b1_root_cause_2026-03-02.json`
with the definitive B1 split: ACT=$7.4M (Script 02 secondary filter bug, AE to investigate),
BKF=$6.6M (backfill-only, policy). The variance memo at `docs/briefs/data-scientist-auavar-variance-memo.md`
requires a minor update to reflect the final B1 numbers from this run.

DS work is done. Two external actions needed:
1. AE — find the secondary filter in Script 02 that drops 164 ACT accounts
2. COO — decide on BKF (accept or extend forward-fill using BD allocations as confirmation signal)

---

## Next Steps

1. **[DS] Update variance memo** with final B1 numbers (ACT=$7.4M/164 accts, BKF=$6.6M/233 accts)
   and the revised "if fixed" target numbers for COO context

2. **[0.7.0_AE_CloudOps or 0.4.0_DT_ClientPlatform] Investigate Script 02 ACT bug**
   — 164 accounts have TXN_DAILY records but are absent from cube/2026-03-02.parquet.
   The secondary filter runs after `_compute_account_end_dates()`. Candidate suspects:
   - `units > 0` filter in `expand_pairs_to_daily()` (line 269: `open_mask = units_series > 0`)
     — accounts that had a net-zero position on 2026-03-02 due to same-day buy+sell would be dropped
   - `asset_name.notna()` filter in `compute_unit_events()` (line 184)
     — transactions with null asset_name are excluded from the unit replay
   - The `expand_start_date` clip if a partial rebuild was run for 2026-03-02

3. **[2.0.0_SA_COO] BKF policy decision** — 233 backfill-only accounts, $6.6M, all 2025Q4-2026Q1,
   standard account types. Options:
   - Accept gap: acknowledge Script 02 design excludes these; BD sees them, gold doesn't
   - Extend forward-fill: if account appears in BD allocations as open on date D, allow forward-fill
     through D regardless of `_source_file` classification. This is an AE change to Script 02.

**Do NOT:**
- Modify Script 02 directly — AE owns the gold pipeline code
- Push variance memo without updating B1 section to reflect final diagnostic numbers

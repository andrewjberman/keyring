# A_03 — positions_cube — DATA_ANALYTICS layer briefing  ★ the crux of the rebuild thesis

**Script:** `data/black_diamond/scripts/gold/A_03.positions_cube.py` (1,928 lines — by far the largest Group-A script)
**Output:** `gold/positions_cube/YYYY-MM-DD.parquet` — one file/day, every (account_id, asset_name, units>0). 2,361 partitions (2020-01-01..present).
**Layer / order:** Group A; catalog line 82. The positions FACT table → B_00 canonical_holdings → all B/C/D → portal AUA/holdings.
**Essential status:** ESSENTIAL (the foundational fact; everything downstream values it).
**Briefing by:** 0.4.0_DS_ClientPlatform, 2026-06-24 (Andrew-direct A1 layer-walk). Source-grounded + deployed-verified.

---

## 1. What it does
FIFO-reconstructs daily holdings PURELY from `silver/transactions/`: classify each txn as buy/sell/corporate-action/passthrough → signed units → cumulative units per (account, asset) → forward-fill to a continuous daily timeline → keep units>0 → one parquet per day. Memory-bounded (sorted by first-txn, flush-safe-partitions, category dtypes, process-pool expansion).

## 2. Recompute posture — FULL nightly, and INHERENTLY so (NOT a quick flip like A_01)
- Catalog = `--upload` (no `--incremental`); runs a full rebuild (~563s) nightly.
- A_03's `--incremental` is NOT a narrowing — it's a whole-run **input-fingerprint SKIP-GATE** (L1740-1797): skip the entire build only if NO input changed since the last run (then outputs are byte-identical). It CANNOT narrow per-date because the latest-snapshot reconciliation (phantom sells, RPS ground-truth, back-dated txns) **legitimately rewrites historical partitions every data-night** (L1742-1750).
- **The gate would not help:** gate-evidence scorecards = `INPUTS-CHANGED` EVERY night (06-20..06-24; 13 scorecards) — new daily txn/alloc/RPS files land nightly, so even with `--incremental` it runs full. **So A_03 is NOT routed for a flip** (the flip is ~zero-value here, unlike A_01's real 1,815→14-day narrowing).
- **The real fix is ARCHITECTURAL, not a flag:** the full nightly recompute + the entire injection machinery exist ONLY because positions are FIFO-reconstructed from an INCOMPLETE transaction feed. **Snapshot-native positions (the cot model — custodian-direct holdings snapshot) eliminate the FIFO, the nightly history-rewrite, AND all ~500 lines of injection.** A_03 is the single biggest argument for the DATA_ANALYTICS clean rebuild.

## 3. Bullshit / overfit — the WORST in Group A (the 49F-overfit mess to kill)
This script is dense with BD-feed-repair band-aids + hardcoded overfit:
- **~500 lines of synthetic injection** (L359-866) repairing BD's incomplete feed:
  - `_load_realized_sell_events` — synth sells to close phantom positions BD never sent the sell for (the 4/30/2024 Opal onboarding rotation).
  - `_load_rps_injection_events` — Schwab RPS `quantity_settled` as two-sided ground truth (buy/sell gaps) + the CUSIP bridge to close ~$177M of "vanished" positions (in FIFO, absent from BD reports).
  - `_load_synthetic_buy_events` — back-solve buy events for unrealized-open positions with zero txn history (lot-weighted residual / RC3 lot×price).
  - **ALL of this vanishes under snapshot-native positions.**
- **Hardcoded `NAME_ALIASES`** (L278-282): `OPAL DIVIDEND INCOME ETF`→`POLEN`, `EVENTIDE HIGH DIVIDEND ETF`→`POLEN` — security remap baked in the gold transform → belongs in a silver security-master/alias table.
- **Hardcoded `_CASH_PATTERNS` + `_PAR_VALUED_PATTERNS`** (L286-307): `SHIELD`/`BUFFER`/`DELPHI`/`CAP 20% PROTECTION` force $1/unit — overfit to specific 49F holdings (Allianz Shield, AQR Delphi) → belongs in a security-classification table.
- **`_MATURITY_YEAR_RE`** (L77, L1244-1252): regex-parse the maturity YEAR from the asset NAME to drop matured bonds — a fragile string hack for a missing-redemption-txn problem.
- **Sentinel-date band-aids:** `MIN_OUTPUT_DATE`=2020 clip + `_MIN_TXN_DATE` clamp (1901 sentinels→2020, L903-912) to avoid 43,500 empty partitions from BD's garbage dates.

## 4. Tech debt
- **DEAD CODE** (L254-262): an unreachable fragment AFTER `_load_phantom_exclusion_set`'s `return` (L251) — leftover "ghost suppression" referencing `alloc_agg`/`ghost_ids` from a deleted function. Never executes.
- **3 overlapping allocation loaders:** `_load_open_account_ids` (L138), `_load_allocation_signals` (L167), `_load_phantom_exclusion_set` (L205) — redundant (all load silver/allocations + extract account sets); `_load_allocation_signals` was added to "avoid reading twice" but the others remain.
- **LEGACY dual-write** in 3 places (L1222-1224 partition, L1490-1496 synth-index, L1726-1728 single-date) — migration leftover.
- `stats['rows_written'] += 1` (L1317) counts PARTITIONS not rows ("actual row count lost", L1317 comment) — misleading stat.

## 5. What's GOOD (keep)
- The **fingerprint-gate + gate-evidence shadow** (L1740-1860) is correct engineering for an inherently-full fact-table: it proves "fingerprint unchanged ⇒ served outputs unchanged" before ever skipping. Sound design — just rarely applicable here.
- Memory strategy (flush-safe-partitions, category dtypes, fork process-pool) is thoughtful for 300M-row scale.
- Deterministic compute (sorted groupby cumsum); the transaction taxonomy (buy/sell/CA-subtype/passthrough) is carefully maintained.

## 6. Actions
| When | Action | Owner |
|---|---|---|
| A2 | DELETE dead code (L254-262); consolidate the 3 allocation loaders → 1; drop the 3 legacy dual-writes; fix the rows/partitions stat | DS |
| A2 | Move NAME_ALIASES + _CASH/_PAR patterns + maturity logic to a silver security-master/classification table (out of gold) | DS (+ silver/AE) |
| **A3 (the big one)** | **Snapshot-native positions** (custodian-direct, the cot model) → eliminates FIFO reconstruction + ALL ~500 lines of injection + the nightly history-rewrite + the sentinel-date band-aids. A_03 is the prime case for the rebuild. | DS authors / AE deploys |
| — | Recompute: NO flag-flip (the gate won't help — inputs change nightly). The fix is the A3 architecture. | — |

## 7. Status
- **Essential** (the positions fact). **THE poster child for the DATA_ANALYTICS clean rebuild:** ~500 lines of injection band-aids + inherent nightly full-recompute, all because positions are FIFO-reconstructed from an incomplete feed. Snapshot-native positions collapse this script to a fraction of its size and kill the full-recompute. Distinct from A_01 (no quick flip-win here — the answer is architecture, not a flag).

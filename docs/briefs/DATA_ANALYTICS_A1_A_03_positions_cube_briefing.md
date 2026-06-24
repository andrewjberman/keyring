# A_03 — positions_cube — DATA_ANALYTICS layer briefing  ★ the crux of the rebuild thesis

**Script:** `data/black_diamond/scripts/gold/A_03.positions_cube.py` (1,928 lines — by far the largest Group-A script)
**Output:** `gold/positions_cube/YYYY-MM-DD.parquet` — one file/day, every (account_id, asset_name, units>0). 2,361 partitions (2020-01-01..present).
**Layer / order:** Group A; catalog line 82. The positions FACT table → B_00 canonical_holdings → all B/C/D → portal AUA/holdings.
**Essential status:** ESSENTIAL (the foundational fact; everything downstream values it).
**Briefing by:** 0.4.0_DS_ClientPlatform, 2026-06-24 (Andrew-direct A1 layer-walk). Source-grounded + deployed-verified.

---

## 1. What it does
FIFO-reconstructs daily holdings PURELY from `silver/transactions/`: classify each txn as buy/sell/corporate-action/passthrough → signed units → cumulative units per (account, asset) → forward-fill to a continuous daily timeline → keep units>0 → one parquet per day. Memory-bounded (sorted by first-txn, flush-safe-partitions, category dtypes, process-pool expansion).

## 2. Recompute posture — FULL nightly, and it is NOT justified (CORRECTED 2026-06-24, Andrew-challenged)
- Catalog = `--upload` (no `--incremental`); runs a full 2020→present rebuild (~563s, all 2,361 partitions) nightly. The build also **writes every partition unconditionally** (build_full → flush_all_partitions), even byte-identical ones.
- A_03's `--incremental` is only a whole-run **input-fingerprint SKIP-GATE** (L1740-1797), not a narrowing; gate-evidence = `INPUTS-CHANGED` every night, so it'd run full anyway. So flipping it is ~zero-value (correct) — BUT that does NOT mean A_03 can't be incremental. It CAN; the gate is just the wrong incremental.
- **CORRECTION (I over-claimed "inherently full"; Andrew was right):** the author's comment "historical partitions change every data-night" (L1742-1750) is FALSE for the deep past. GROUNDED via the synthetic index (79,026 events): **2024 = 78,692 (99.6%, the 4/30/2024 rotation); pre-2024 = 13 events (0.0%).** So **2020-2023 (the majority of partitions) is provably stable** and rebuilt nightly for nothing. The author conflated "the 2024 injection window rewrites" with "all history rewrites" and punted to a coarse whole-run gate.
- **The RIGHT incremental (Andrew's model): first run FULL; daily = a ~7-14 day revision window (back-dated/restated rows) + FREEZE the stable deep history.** That covers the genuine churn without a 2020→present rebuild.
- **The one real wrinkle to fix:** the injection (RPS/unrealized/realized) is **re-derived from TODAY's snapshot every night but pinned to historical dates** (mostly 2024-04-30), so it rewrites 2024→present nightly. That's a bug-shaped artifact — a position on 2024-05-15 should not change because today's RPS moved; the 4/30 rotation is a FIXED historical correction that should be **computed once and frozen**, not re-derived nightly. Freeze it and the windowed-incremental holds.
- **Two fixes, both valid:** (A) windowed-incremental in the CURRENT design (freeze deep history + revision window + freeze the one-time injection) = a real win now; (B) **snapshot-native positions (cot model)** = the clean end-state that deletes the FIFO + injection entirely → true 1-partition-a-day incremental. A_03 remains the biggest argument for (B), but (A) is available without the rebuild.

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
| **A2/A3 — windowed-incremental (CORRECTED: a real win NOW, current design)** | first-full-then-window: freeze deep history (pre-2024 provably stable, 0.0% injection) + recompute a ~7-14 day revision window + **freeze the one-time 2024 injection (compute once, stop re-deriving from today's snapshot)**. Stops the nightly 2020→present rebuild without the full architecture change. | DS authors / AE deploys |
| **A3 (the clean end-state)** | **Snapshot-native positions** (custodian-direct, the cot model) → eliminates FIFO + ALL ~500 lines of injection + sentinel band-aids → true 1-partition-a-day incremental. | DS authors / AE deploys |

## 7. Status
- **Essential** (the positions fact). **Recompute CORRECTED (Andrew-challenged 2026-06-24):** the full 2020→present nightly rebuild is NOT justified — grounded, pre-2024 = 0.0% of injections, deep history is stable. It CAN be windowed-incremental (first-full → ~7-14 day revision window + freeze deep history + freeze the one-time injection) in the current design; the author's "history rewrites nightly" was an over-claim (conflated the 2024 injection window with all history). Snapshot-native (the cot model) is still the cleaner end-state (deletes the FIFO + injection), but a real incremental win exists WITHOUT the rebuild. Also THE poster child for why snapshot-native is better (~500 injection lines).

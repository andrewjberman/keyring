# GLDINC P2 — A_03.positions_cube Reconcile-Correctness Design (draft)

**Author:** 0.4.0_DS_ClientPlatform (§5 reconcile-correctness co-owner)
**Date:** 2026-06-08
**Status:** DRAFT for COO/AE/CTO review — pre-staged parallel to AE's P0 validation; NO prod touch (C1)
**Pairs with:** ADHC_GLDINC_PRD §5/§5a (v0.2.1, refinement #5), §4 dual-run, §4a carve-out, §4b scorecard
**Build-lead:** 0.6.0_AE (compute/DAG/state mechanics). This doc = the reconcile-correctness half.

---

## 1. What A_03 actually is (scoping the reconcile)

A_03 produces `gold/positions_cube/{date}.parquet` = `(account_id, asset_name, units)` for every
open position (units>0) per calendar day. It is the **units cube**, NOT cost-basis FIFO lots (those
are Stage-3 `03_build_holdings_lots`). So A_03's reconcile is about **cumulative UNIT correctness per
(account,asset) over time**, plus a date-anchored **injection layer**. Two computation stages:

- **cum_units** (`compute_unit_events`): signed-unit events (buy=+, sell=−, passthrough=as-is, CA by
  sub-type) → `groupby(account,asset,date).sum()` → `cumsum` per (account,asset). A pure prefix-sum.
- **expand** (`expand_pairs_to_daily`): forward-fills each pair's cum_units across every day from
  first-txn to its end date (global_end_date for active accounts; capped last-txn for backfill-only),
  keeping units>0. **This full pair×day cross-product (~300M rows) is the 76 GB memory floor = the P2
  prize.** Per-partition filters (matured-bond by name-year, phantom-exclusion by alloc AUA≥$100) are
  applied at write time, derived from the target-date allocation snapshot — they are NOT state.

## 2. The incremental state model (the per-pair cum-unit store)

**Key realization:** the "stateful per-pair cum-unit store" the PRD calls for can BE the **prior-day
open-position set** carried forward. Today's partition = `forward_fill(yesterday_open_positions) ⊕
today_signed_deltas`, with the two per-partition filters reapplied — NOT a re-expansion of all history.
A buy-and-hold pair with no txn today simply carries yesterday's units (the forward-fill). This drops
the working set from ~300M pair×day rows to ~the current open set (hundreds of K) + today's delta.

**Persisted state (the seed, §4 FLAG 3):**
| Artifact | Content | Source today |
|---|---|---|
| `gold/positions_cube/_state/cum_units@{wm}.parquet` | per-(account,asset): latest `cum_units` + last-event `trade_date` (POST-injection) | `_latest_cum_units(unit_events)` after all injections |
| `gold/positions_cube/_state/account_end_dates@{wm}.parquet` | per-account forward-fill end date (active→global; backfill-only→capped) | `_compute_account_end_dates()` |
| `gold/synthetic_positions_index` (EXISTS) | all injection events `{account,asset,trade_date,signed_units}` | already written by build_full Step 2a |
| `gold/positions_cube/_state/watermark.json` | max processed date + per-input LastModified/checksum (see §4) | new |

The injection contributions are already recoverable from the persisted synthetic index, so the seed =
`compute_unit_events(real txns) ⊕ synthetic_index`, rebuilt once. **One-time state-seed step:** run the
current full build once, emit the four state artifacts, freeze the watermark. Gated complete before any
parity accrual (§4 FLAG 3). This is the only full-history pass P2 needs.

## 3. Normal-day dirty-set (no restatement)

1. Detector confirms no historical input changed (§4) → carry-forward path.
2. Load today's new `silver/transactions/{today}.parquet` (+ any dates in `(wm, today]`).
3. Apply signed deltas to the cum-unit store for the **touched pairs only**; new pairs append.
4. Build today's partition = open positions (units>0) = carry-forward of all live pairs to `today`
   (active accounts; capped accounts stop at their end date) ⊕ touched-pair updates.
5. Reapply matured-bond + phantom-exclusion filters from `silver/allocations/{today}`.
6. Write `{today}.parquet`; advance watermark.

Dirty-set = touched pairs ∪ (carry-forward of all still-open pairs). The carry-forward is O(open-set),
not O(history). No `expand_pairs_to_daily` cross-product.

## 4. Reconcile triggers (the hard part — Gate 3) + invalidation scope

Three restatement classes. All detected via the §5a unifying primitive (per-input LastModified /
content-checksum vs the stored watermark). Each invalidates a **scope**, then re-derives only that scope.

### 4.1 Historical transaction restatement (§5a primitive, dated partitions)
- **Detect:** any `silver/transactions/{date ≤ wm}.parquet` whose `LastModified` advanced.
- **Scope:** pairs with an event on `date` → cum_units is a prefix-sum, so a changed historical event
  invalidates that pair's cum_units **from `date` forward** → every subsequent day-partition for those
  pairs is stale.
- **Re-derive:** recompute cum_units for the affected pairs only, re-emit partitions `[date, today]`
  for those pairs (scoped re-expand — cheap; pairs, not whole-book).

### 4.2 Injection-snapshot restatement (reconcile-on-injection — the A_03-specific core)
The injection layer (`_load_realized_sell_events`, `_load_rps_injection_events`,
`_load_synthetic_buy_events`) depends on NON-transaction inputs: `schwab/silver/rps/{latest}`,
`silver/unrealized/`, `silver/realized/bd_realized_agg`, `gold/dimensions/schwab_bd_account_mapping`,
and `silver/prices/canonical_prices` (§4.3). Injection events are stamped at **2024-04-30** (RPS/sell)
or unrealized `open_date` (buy).
- **Detect:** LastModified/checksum advance on ANY injection input vs watermark.
- **Scope:** re-run the affected injection back-solve → the resulting `signed_units` at the injection
  date(s) change → affected pairs' cum_units change **from the injection date forward**.
- **Re-derive:** re-run injection for affected pairs, rebuild cum_units (`_rebuild_unit_events`), re-emit
  partitions from the injection date forward for those pairs; rewrite `synthetic_positions_index`.
- **This is why §4a matters:** the highest-risk path (the 2024-04-30 injection-date re-FIFO) is NEVER
  hit by a forward N-night window. The §4a **scoped single-date carve-out target = 2024-04-30** — re-run
  that one injection date through oracle (full) vs incremental (reconcile-triggered) + value-for-value
  diff = the P2 reconcile-parity evidence. (One date, small box, cost-logged — per §4a conditions.)

### 4.3 canonical_prices restatement (refinement #5 wiring — the monolithic input)
`canonical_prices.parquet` is **monolithic** (no dated partitions), so the §5a partition-LastModified
detector doesn't scope it — this is the gap refinement #5 closes. **A_03-specific narrowing:** A_03
uses canonical_prices ONLY in the buy-injection back-solve, and ONLY the **latest price per asset**
(`drop_duplicates('asset_name', keep='last')`, L679) → `units = injectable_mv / latest_price`.
- **Detect (refinement #5):** on a `canonical_prices` LastModified advance, group by date, hash each
  date's rows, diff vs the stored per-date checksum manifest → `changed_dates` + `changed_assets`.
- **A_03 narrowing:** A_03's injected units change **iff the LATEST price for an injection-target asset
  changed** (a strictly-historical price restatement that doesn't move the per-asset latest does NOT
  change A_03 output — but the full per-date manifest is still emitted for the downstream Stage-3
  `valued_positions` valuation, which IS per-date price-sensitive). So A_03's trigger condition =
  `changed_assets ∩ injection_target_assets` has a member whose per-asset latest-price row moved.
- **Scope/re-derive:** re-run buy-injection for affected assets/accounts → §4.2 re-derive path.
- **Future opt (non-required, noted in #5):** if `build_canonical_prices_v2.py` emits a
  `changed_dates.json`, A_03 reads it directly (skip the re-hash). Not needed for P2.

### 4.4 Dirty-set cascade completeness (§5a refinements 1/4 applied to A_03)
- A reassignment (§5a #1) is an advisor-assignment concern (Stage 07-10), not A_03 — A_03 keys are
  (account,asset), reassignment-invariant. NOT an A_03 trigger. (Flag so we don't over-scope.)
- No freeze-baseline in A_03 (§5a #4 is P5/D_00b) — A_03 has no frozen-period cascade.
- A_03's only cascade is the prefix-sum-forward one (4.1/4.2): any change at date D invalidates [D, today]
  for the touched pairs. The invalidation MUST reach `today`, never stop at D.

## 5. Parity benchmark hooks (§4b scorecard, per A_03)
Emit `gold/_parity/P2/{run_date}/scorecard.json` diffing incremental vs oracle `positions_cube/{date}`:
- `key_set_symmetric_diff` on (account_id,asset_name) per partition — TARGET 0.
- `row_count_delta` per partition — TARGET 0.
- `exact_match_rate` on units (float) within FROZEN epsilon; `max_abs_diff` (units are float cum-sums →
  tiny order-of-ops epsilon expected; freeze at the known-correct dual-run value, never widen).
- `headline_metric_diffs`: per-partition open-position COUNT + total units per top asset — TARGET 0.
- The **2024-04-30 injection-date scorecard** (via §4a) is the P2 gold-standard gate, not just N
  steady-state nights.

## 6. Open constraints / risks to resolve with AE at P2 kickoff
1. **`build_single_date()` omits the injection layer** — it's a raw txn snapshot, NOT injection-
   consistent with `build_full`. The incremental day-builder CANNOT reuse it as-is; it must carry
   forward from the POST-injection seed state (§2). Flagging as the first build-mechanics item for AE.
2. **Dormant-pair forward-fill** is the correctness subtlety: a pair that hasn't traded in 2 years is
   still in today's partition (forward-filled) until it sells to zero or its account caps. The carry-
   forward state must retain ALL open pairs, not just recently-active ones — else dormant buy-and-hold
   positions silently vanish (the exact bug the `--start-date` full-history-cum_units note guards).
3. **Per-partition filters are date-derived, not state** — matured-bond (name-year vs partition-year)
   and phantom-exclusion (alloc AUA≥$100) must be reapplied each incremental day from that day's
   allocation snapshot; they are correctly NOT carried in the cum-unit store.
4. **Account end-date drift:** an account flipping active↔backfill-only (or newly alloc-confirmed-open)
   changes its forward-fill horizon → its dormant pairs start/stop appearing. Treat an
   `account_end_dates` change as a reconcile trigger for that account's pairs.

## 7. Summary
A_03's reconcile reduces to: a per-pair cum-unit carry-forward store (seeded once, §3) + three
restatement detectors (txn-partition LastModified §4.1; injection-snapshot change §4.2; canonical_prices
refinement-#5 per-date checksum §4.3) each invalidating `[trigger_date, today]` for the affected pairs
only. The 2024-04-30 injection-date is the §4a scoped-carve-out parity target (the path no forward
window hits). Reassignment/freeze-baseline cascades are NOT A_03 (correctly out of scope). Ready to
co-develop with 0.6.0_AE the moment P1 lands + CTO GOs.

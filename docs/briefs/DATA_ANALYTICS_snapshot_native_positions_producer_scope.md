# Snapshot-native positions producer — scope (Phase 1: Schwab book)

Scopes the real A_03 fix: replace FIFO-reconstruction with the daily custodial holdings snapshot (the cot model) for the Schwab-custodied 49F book. DS-authored, AE deploy-lane, shadow-proven vs the FIFO cube before cutover. Origin: Andrew-direct A_03 deep-dive + the feasibility test (DATA_ANALYTICS_A_03_snapshot_native_feasibility_test.md). COO-endorsed scope.

## Goal
A daily (account_id, asset_id)-keyed holdings snapshot for Schwab-custodied accounts, sourced directly from Schwab RPS — no FIFO, no synthetic injection. Non-Schwab accounts stay on FIFO (A_03) interim; union downstream.

## Inputs (all already retained daily)
- `schwab/silver/rps/date={YYYYMMDD}/` — quantity_settled + market_value + closing_price + cusip/ticker, per (schwab_account, security). Back to 2024-01-12.
- `gold/dimensions/schwab_bd_account_mapping.parquet` — schwab_account_id → bd_account_id.
- CUSIP→asset_name/asset_id bridge (existing: from unrealized + realized) — for the asset key + name.

## Output
(account_id, asset_id)-keyed daily holdings: account_id (bd), asset_id, asset_name, ticker, cusip, units (quantity_settled), market_value, source='schwab_snapshot'. Matches the cot canonical_holdings contract so B_00/downstream consume it unchanged.

## KEY ARCHITECTURAL FINDING — CONFIRMED (source-traced 2026-06-24)
**A_03's RPS injection is REDUNDANT with B_00's RPS reconciliation on the canonical-holdings path.** Traced B_00.reconcile_date (L502-559): full-outer-join cube vs RPS, then for any Schwab-covered account B_00 **uses Schwab/RPS units in EVERY case** — `schwab` (cube missed it), `reconciled` (agree), `schwab_override` (disagree) all take Schwab units; `bd_stale` zeroes FIFO ghosts. The cube's (FIFO + A_03-injected) units survive **only** for cash, unresolvable-CUSIP assets, and non-Schwab accounts. So A_03 injects RPS into the cube → **B_00 throws those units away and uses raw RPS** for exactly the Schwab-covered positions the injection targets (and the injection already excludes cash). **The RPS injection's effect on served holdings is discarded.**

Consequences:
- **The Schwab book is ALREADY effectively snapshot-native at B_00** (B_00 overwrites FIFO with RPS). A_03's FIFO + RPS-injection for Schwab accounts is wasted compute B_00 discards.
- **Immediate cleanup (independent of the full rebuild):** remove A_03's `_load_rps_injection_events` (a big chunk of the ~500 lines) — B_00 is already the RPS reconciliation point. The synthetic sell/buy injection is more nuanced (may still aid NON-Schwab accounts where B_00 keeps 'bd' units) — trace separately.
- **CAVEAT before removal (Rule-22):** B_00 is the primary cube consumer, but trace OTHER raw-`positions_cube` consumers (B_01 holdings_lots, C_* etc.) to confirm none depend on the injected units. Full consumer census before deleting the injection.

## Build plan (additive + shadow-proven, the A_01/A_02 lifecycle)
1. **Confirm the B_00-redundancy** (above) — determines whether the fix is "remove A_03 injection + let B_00 reconcile" (simplest) vs "new snapshot producer."
2. **Build the snapshot producer** (additive; full A_03 FIFO stays default+authoritative): RPS → (account,asset) holdings w/ units+MV, CUSIP-bridged, account-mapped, cash/par handled.
3. **Shadow-parity** vs the served FIFO cube (per-account, per-asset units + MV within tolerance; account-coverage diff = the expected non-Schwab tail). Prove over clean nights.
4. **Cutover the Schwab book** when shadow-PASS; non-Schwab stays FIFO interim (union at B_00).
5. Retire A_03's injection block for the Schwab majority.

## Coverage / phasing
- Phase 1 (this scope): Schwab book (~5,521 accts / $1.55B / ~80%). Snapshot-native.
- Phase 2: non-Schwab tail (~1,376 accts / ~20%) via custodian-direct feeds (DATA_PLATFORM obtainable-per-client lever). Until then: FIFO interim for the tail only.
- Net: kills FIFO + the ~500-line injection for ~80% of accounts now; the whole cube once Phase 2 feeds land.

## Risks / discipline
- Positions fact = downstream AUA depends on it → shadow-prove byte/tolerance-identical before ANY cutover (never an ad-hoc gold run; validate on the scheduled nightly's shadow).
- The non-Schwab union boundary (which accounts are Schwab vs not) must be deterministic (the mapping) — a misclassified account drops or double-counts. Guard + reconcile.
- DS-authored (A_03 is DS-lane); AE deploy-lane for the dispatch/EC2 side.

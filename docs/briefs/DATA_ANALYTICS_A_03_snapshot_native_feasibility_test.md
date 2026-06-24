# A_03 snapshot-native positions — feasibility test (Andrew-direct, 2026-06-24)

Test of replacing A_03's FIFO-reconstruction with a daily account/holdings snapshot (the cot model), keyed (account_id, asset_id). Read-only exploration (no served writes); grounded on 2026-06-18 data.

## The cot model (what we use for Cottonwood today)
`opal-data-cot silver/holdings/{date}.parquet` IS an (account_id, asset_id)-keyed daily holdings snapshot with full asset detail (units, market_value, asset_id, asset_name, ticker, cusip, expense_ratio, cash_equivalent; ~15/account). cot's B_00 reads it directly — no FIFO, no injection. 49F has NO `silver/holdings/` → B_00 "falls through to the positions-FIFO path" (A_03).

## The 49F equivalent, built from the snapshot data we already retain
Daily snapshot sources retained for the 49F book:
- **Schwab RPS** (`schwab/silver/rps/date=YYYYMMDD/`): daily, back to **2024-01-12**, (account, security) grain with **quantity_settled + market_value + closing_price + ticker/cusip**. A complete custodial holdings snapshot for the Schwab book.
- **BD Unrealized** (`silver/unrealized/{date}`): daily back to 2026-03-27, lot-level — but **NO quantity, NO market_value** (raw confirmed: 14 cols = lot identity + open_date + unit_cost only; NOT a silver-slimming bug — BD's "unrealized" is a lot-OPENINGS feed). So BD-direct cannot give current units without FIFO.
- BD Allocations (`silver/allocations/{date}`): daily, but **account-level AUA only** (~1 row/account), no per-holding detail.

### Built (account_id, asset_id)-keyed 49F holdings from RPS, 2026-06-18:
```
86,043 holdings | 5,521 bd-accounts | ~15.6/acct | total MV $1.55B
columns: account_id, asset_id(cusip), ticker, quantity, market_value   <- units + MV INLINE
sample z0820277481: 14 holdings, $34.4M (IEFA $5.94M / DIVZ $5.23M / IDVZ $4.37M / ...)
```
- **Cleaner than A_03**: RPS carries units AND market_value; A_03's cube is units-only and needs the separate canonical_prices join + the pricing chain. Snapshot-native simplifies pricing too.
- **No FIFO, no ~500-line injection** — matches the cot model.

### Coverage vs A_03 reconstruction (2026-06-18)
| | accounts | positions | units | MV |
|---|---|---|---|---|
| A_03 cube (FIFO) | 6,877 | 104,398 | yes | no (priced later) |
| RPS snapshot | 5,521 | 86,043 | yes | **yes inline** |
- Overlap: 5,501 accounts. RPS-only: 20. **cube-only: 1,376** = the NON-Schwab-custodied accounts.

## The one gap + how it closes
The **~1,376 non-Schwab accounts (~20%)** have NO direct units snapshot: RPS is Schwab-only, and BD unrealized is lot-openings (no quantity). These accounts are custodied **elsewhere (Fidelity et al.)** — which ties directly to the DATA_PLATFORM strategic reframe: **custodian-direct feeds are low-friction per-client-obtainable** (Andrew, LD-era). So the non-Schwab snapshot = the same custodian-direct-feed acquisition lever.

## Verdict + path
Snapshot-native is **feasible and cleaner**, validated end-to-end on the Schwab book.
- **Phase 1 (ready now):** snapshot-native positions for the Schwab-custodied 49F book (~80% accts, $1.55B) directly from RPS — generalizes the cot model to 49F; deletes FIFO + injection for these accounts.
- **Phase 2:** acquire custodian-direct feeds for the non-Schwab tail (the obtainable per-client grants) → snapshot-native everything.
- **Interim:** keep FIFO for ONLY the non-Schwab ~20% tail (vs all 6,877 accounts today) — already a major simplification + kills the injection for the Schwab majority.
- Build = a snapshot-native positions producer (RPS + cot-style), shadow-proven vs the FIFO cube before cutover (the A_01/A_02 lifecycle). DS-authored, AE deploy-lane.

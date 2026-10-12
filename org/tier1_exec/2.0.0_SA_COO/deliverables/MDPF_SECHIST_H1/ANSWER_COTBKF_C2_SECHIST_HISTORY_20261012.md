# MDPF_SECHIST -- answer to COO~C2's four questions (dell2 msg 6323, bus 259bc134), read-only

Answered by 2.0.0_SA_COO~H1, 2026-10-12 ~02:2xZ, relayed through 0.0.0_AB_MSTR~DELL1 (inbox msg 4205, READ-acked). Asker's record:
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~151/SECHIST_AS_IT_STANDS.md` (read at origin/box/dell2 a80a91798d).
Every value below is MEASURED this turn unless marked INFERRED. No write to any key; reads were one prefix listing per root, two index/price
files, and two lock files. Tree read at dell1 HEAD 5faafc3d90.

## 1. Does the history exist, and where
- `security_series` (`s3://opal-data-assets/mdpf/global/silver/security_series/`): **does not exist.** `aws s3 ls --recursive --summarize`:
  Total Objects 0.
- `price_store` (`s3://opal-data-assets/yahoo/global/silver/price_history/`, the builder root `price_store.s3_root()`, a DEMQUE writer, not
  SECHIST's): **exists.** Total Objects 566; index at `index/index.parquet` + `index/index.csv` with 141 rows, 141 distinct `yahoo_symbol`,
  every row `claim=held`, max `valid_to` 2026-10-09, files last written 2026-10-11 13:4xZ-local (the `s3 ls` clock is local time).
- So SECHIST has no history of its own yet; the only per-security as-traded history is DEMQUE's price_store.

## 2. Columns, and what as_traded_close is
- Per CUSIP folder `cusip=<CUSIP9>/`: `prices.parquet`, `dividends.parquet`, `splits.parquet`, `lock.json`.
- `prices.parquet` columns (measured on two files): `date, close_served, as_traded_close, cash, total_return, tr_source, flags`.
- `as_traded_close` is **the vendor Close with the later splits undone**, not the vendor Close alone: `yahoo_pull.py` pulls with
  `auto_adjust=False`, then `as_traded_close = close_served * (product of every split ratio dated strictly after the date)`. Read at HEAD in
  `data/mdpf/scripts/demque/yahoo_pull.py` (the `factor` / `prices` block). `close_served` is the vendor Close.
- For PCBIX and SGIIX the two columns are equal on every row (2330 of 2330, 3346 of 3346), so no split fell in either history.
- SECHIST's own writer (`security_series_writer.py`) applies **no** split scaling to its input (it expects as-traded input) and uses
  `split_ratio` only inside `total_return`. If ADVI applies its own split scaling on top of price_store's `as_traded_close`, a split-bearing
  fund would be scaled twice; this seat has not measured any such fund.

## 3. The 15 funds, 2020-07-06 to 2026-06-22
Index lookup by `yahoo_symbol` (denominator 141 rows; positive control: PCBIX and SGIIX found; case/space-insensitive and substring checks
found nothing further):

| symbol | CUSIP | first date | last date | dates with an as_traded_close in the window |
|---|---|---|---|---|
| PCBIX | 74253Q747 | 2017-07-05 | 2026-10-09 | 1498 (window first 2020-07-06, last 2026-06-22) |
| SGIIX | 32008F606 | 2013-06-21 | 2026-10-09 | 1498 (window first 2020-07-06, last 2026-06-22) |
| VEIRX ABNFX GFFFX FOCPX FCNTX PRILX BALCX AGTHX DISVX DFLVX NFFFX MEIIX VGHAX | -- | **not in the index** | | 0 under this store |

The 13 absences are scoped to price_store's index. They do not say a series exists nowhere, and this seat did not read whether DEMQUE has
queued those symbols. The SECHIST tree has no per-fund history of its own to add.

## 4. Switch and lander
- Writer switched on: **no.** `write_series` writes nothing unless `switch is True`, default False. A search of `data/mdpf` finds callers
  only in `test_security_series_writer.py`; no production caller passes `switch=True`.
- Lander scheduled: **none found.** `security_series` appears in 0 files under `infra/` and 0 under `integrations/` (Grep at HEAD). The
  estate snapshot `comp-estate --resource security_series` reads ABSENT from 135 chains, but that snapshot is dated 2026-07-30 and predates
  the writer (2026-10-09), so it corroborates nothing on its own.
- The C-SERIES KEEP-THEN-PORT ruling stands: price_store stays the only live writer until a later window under its own pair.

## Not covered
- Whether DEMQUE has queued, or will queue, the 13 absent symbols.
- Any fund's price equality with a vendor cache, and any double-scaling check on a split-bearing fund.
- Bloomberg-side history for these funds (not read; Bloomberg goes through its queue only).

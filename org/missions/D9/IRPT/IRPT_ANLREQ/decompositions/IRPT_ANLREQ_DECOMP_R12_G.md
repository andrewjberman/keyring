# IRPT_ANLREQ round 12, workstream ~G (ENGINE) -- decomposition: the four price adapters behind the one total-return helper

Issuer `2.0.0_SA_COO~G2`, 2026-10-15.

**Input:** the price-adapter facts read `AR-g-69` (merged `d1de2f0cd6`; record `deliverables/0.9.0_WK_IRPT_ANLREQ~176/r9/PRICE_ADAPTER_FACTS.json`, `q2` the formula per source, `q4` the four adapter shapes), the helper `AR-g-80` (merged `f089142e91`, `ycharts/research/tr_level.py`), the chain core `AR-g-51` / `AR-g-70` (`price_source.py`: `resolve_prices(symbols, start, end, readers, as_of)`, a reader is `reader(symbol, start, end)`), CTO msg 8377, PRD v0.15 FWD-7.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **Seams.** The facts record named `partitions` and `index_frame` as DataFrames. Pandas is not on the host and not in the tests, so the seams are plain rows: BBG `partitions=[(day, [dict])]`; DEMQUE `index_rows=[dict]` and `price_rows={cusip: [dict]}`; yfinance `fetch(symbol) -> [dict]`. The default (production) read of each source goes through the injected client and a lazily imported `pyarrow` or `yfinance`; its test skips when the library is absent. The checks fix the seams; the worker builds to them.
- **Yahoo serves split-adjusted data.** `yahoo_pull.py` lines 141-147 and `tr_compare.as_traded_dividends` undo every split dated STRICTLY AFTER a row to get the as-traded Close and the as-traded dividend. The AR-g-69 formula `(P_t + D_t) / (P_(t-1) / s_t) - 1` is on those as-traded values. Cell `AR-g-83` therefore undoes the later splits on both Close and Dividends before the formula; the check has a case for each (a served 2-for-1 split, and a served dividend dated before a later split).
- **YCharts basis is unproven.** The record marks the YCharts level as INFERRED total return (no tracked line says the served `fund_data` level is dividend-inclusive). The adapter is built to the level contract; its use as total return in production waits on that verification and on the CTO ruling about the secret grant (below). The chain order puts it last.
- **Typed refusals.** An unset source is `ValueError("BBG_SOURCE")` / `ValueError("DEMQUE_SOURCE")`; a client error propagates and the chain types it (`price_source.py` `PRICE_READERS`). No adapter catches, stores or logs an error text.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-81` | `ycharts/research/price_adapter_bbg.py` (NEW) and `tests/test_price_adapter_bbg.py` | those two files + the worker's folder | WORLD (floor of an infrastructure path; source and tests only) |
| `AR-g-82` | `ycharts/research/price_adapter_demque.py` (NEW) and `tests/test_price_adapter_demque.py` | those two files + the worker's folder | WORLD |
| `AR-g-83` | `ycharts/research/price_adapter_yfinance.py` (NEW) and `tests/test_price_adapter_yfinance.py` | those two files + the worker's folder | WORLD |
| `AR-g-84` | `ycharts/research/price_adapter_ycharts.py` (NEW) and `tests/test_price_adapter_ycharts.py` | those two files + the worker's folder | WORLD |

## Edges and chains

- FOUR independent chains. Each cell owns one file pair; none imports another; all import the merged `tr_level`. No hookup in a shared file belongs to any cell: the wiring of the four readers into `resolve_prices` is the later compose cell (`opal_producer.py`).

## Host and grant facts these cells do NOT move (carried, not decided here)

- **pandas, pyarrow, yfinance** are not in any tracked requirement of the resident host: a CloudOps act under a pair in the release cell (r32). The adapters build and test without them.
- **DEMQUE:** the resident runner role has no read grant on the store's bucket (an estate-wide shared read): CTO ruling. Until then the estate tier is the Bloomberg history only.
- **YCharts:** the CRO's measured route uses the secret `ycharts/credentials`, which the runner does not hold; the resident's own session secret is `ycharts/session/current`. The adapter takes a transport argument and reads no secret.
- **`lib/trading_calendar.py`** is not in the resident tarball: the T-1 date reaches the producer from the caller, or the module joins the package member list in the release cell.

## Four-postulate record

(i) Domain: the four sources of the price chain (FWD-7), one cell each. (ii) Same grain: a reader function per source. (iii) One intent: yield a base-100 total-return level series. (iv) What this cut does NOT move: any deployed byte, any host dependency, any grant, the chain core, the compose into the producer.

fanout: 4 of 4 chains, cap 8, reason: four disjoint file pairs, each a pure module over one shared merged helper; slots 181 to 184 (178 and 179 are drained and removed).

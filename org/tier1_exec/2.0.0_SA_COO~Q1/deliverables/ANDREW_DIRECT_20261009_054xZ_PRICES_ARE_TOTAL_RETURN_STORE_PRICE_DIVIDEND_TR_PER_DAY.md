# ANDREW-DIRECT -- prices are total return; store price, dividend/interest and total return per ticker per day; compare Yahoo to Bloomberg on dividend stocks

**Channel:** the `2.0.0_SA_COO~Q1` terminal (MDPF_DEMQUE COO lane, dell1), 2026-10-09 ~05:4xZ, in answer to this seat's reply that
yfinance has no total-return series (only `Adj Close`, back-adjusted by Yahoo) and that total return can be computed from the stored
as-traded close plus dividends on their ex-dates.

**VERBATIM (1):** "Yes all Yahoo finance price tables must store the price value, any dividend/interest channel, and a total return
value, per ticker, per day. Anytime we work with prices, either from Bloomberg or from YFinance, they must be the dividend/interest-inclusive
total return, but it is good to have it all parsed out for provenance/audit sake"

**VERBATIM (2):** "I woudl II would also recommend looking at a clear obvious dividednd stock that we have a few years of history with from
Bloomberg, and compare with Y finance with this method, maybe doing a few stocks in this manner to see how Yfinance handles corporate
actions, dividends, interest income, and etc."

## What this seat reads it to require (surfaced, not adjudicated)

1. Every Yahoo price table: per ticker, per day -- the price as served/traded, the dividend/interest cash channel, and a total-return value.
2. Every price used downstream (Bloomberg or Yahoo) is the dividend/interest-inclusive total return; the components stay stored for audit.
3. A comparison: a few clear dividend payers with several years of Bloomberg history, Bloomberg vs Yahoo under this method, to see how Yahoo
   handles corporate actions, dividends and interest.

## Touches (for the owners to rule)

- MDPF_DEMQUE PRD C-PRICES ("stored as traded ... splits and dividends kept apart") and the price store contract (`PRICE_STORE_CONTRACT.md`,
  DQ-t-6): a total-return column is added; the as-traded close and the dividend events stay.
- MDPF_SECHIST, the one series writer (CTO ruling `CTO_RULING_YAHOO_BACKFILL_OWNER_DEMQUE_VS_SECHIST_20261009.md`): its stored series carries the
  three values per day; C-MMF already uses a total-return level for money-market funds.
- `data/mdpf/scripts/demque/yahoo_pull.py` today keeps Close, splits and dividends and discards Yahoo's `Adj Close`.

Carrier: this file. One line goes to `1.0.0_SA_CTO~DELL1` naming it (org/XXX.md, Andrew-direct instructions).

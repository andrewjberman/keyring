# MDPF_SECCLASS round 7 intake -- FWD-9 and FWD-10 (addendum v0.3): what was measured, and five questions before the cut

**Author:** `2.0.0_SA_COO~M` (L5 owner), 2026-10-05 06:xxZ. **For:** `1.0.0_SA_CTO`. The questions are contract-level (key namespace,
history home and producer, classification source, domain), so they are ruled at L4 before any cell is cut, not inside one.
**Basis:** PRD v0.3 @ffb329af49 (ADMITTED, CTO msg 105182), addendum v0.3 (C-BACKFILL; the input is ETFS_RIVALS' served artifact).

## 1. The FWD-9 universe, measured (read-only, 2026-10-05 05:5x-06:0xZ)

- **Input:** `s3://opal-data-etfs/rivalfunds/etfs/gold/canonical_shape/date=<d>/holdings-<rev>.parquet`.
  - 504 daily partitions, 2024-09-30 to 2026-10-02 (about 2 years, not 3); the newest revision of each day was read.
  - 13 funds: BASG, BIDD, CGIC, ETFT, GQGU, IDVZ, INEQ, PCLG, PFOE, SCHY, TSEL, TXUE, WCMG.
  - 300,030 position rows.
- **Securities:** non-cash rows by `security_bloomberg` give 822 distinct securities, by exchange code:
  - US 178;
  - JP 134, LN 56, GR 40, CN 35, HK 35, FP 34, SS 27, AU 22, SM 19, SW 18, KS 17, IN 17, NA 16, and others;
  - `Index` 17: equity index futures such as `MESZ24 Index`. They are not stocks.
- **Keys available:**
  - US: 178 listings, of which 27 carry a CUSIP.
  - Non-US: 516 listings. **0 carry an ISIN** and none a CUSIP. The only stable key is `security_bloomberg` (for example
    `REL LN Equity`), and bare tickers collide across markets (`1` HK, `005930` KS).
- **Against `etf-classifications`:**
  - US tickers: 177 distinct; 139 have a row, 38 have none.
  - Non-US: none is keyed today. Measured by bare first token, 323 of 907 tickers have a row. Those are mostly US matches,
    plus possible wrong-market hits.
- **Class signals in the input:**
  - `asset_class` Equity / Cash, all RESOLVED;
  - `sub_asset_class` and `gics_*` come from Bloomberg GICS via the G4 `security_market` enrichment. On the newest day
    191 of 217 rows are UNRESOLVED;
  - `provider_security_type` is Equity / Index / Curncy.

## 2. Where FWD-9's "history" is (C-BACKFILL: "the series a holding's modal reads")

Read-only code search (Explore agent, 2026-10-05). Paths are file:line.
- **Portal:** no Holdings, Investor Reporting, Portfolio Management or Security Analysis modal reads a per-holding price
  series.
  - `SecurityDetailModal` takes its data as a prop (`portal/src/pages/PortfolioManagement/components/SecurityDetailModal.tsx:13-17`).
  - `EtfModal` reads fund-level figures (`portal/src/components/EtfModal.tsx:83-89`).
  - `IndexPerformanceModal` covers market indices only (`portal/src/api/endpoints/market.ts:595-615`).
- **The one holding dialog with a history is Rival Funds'** (`data/etfs/scripts/rivalfunds/render.py:1321-1368`).
  - It reads G4 `security_market` (`px_close`, `total_return_index`) at
    `opal-data-etfs/rivalfunds/etfs/gold/security_market/date=<D>/market-<rev>.parquet`.
  - The writer is `data/etfs/scripts/rivalfunds/enrichment_bloomberg.py:35-40, :347` (Bloomberg PX_LAST and
    DAY_TO_DAY_TOT_RETURN_GROSS_DVDS). It has a `backfill` mode (`:595-597`) with a 730-day default window (`:82`).
  - That is ETFS_RIVALS' producer at site Z, on the Bloomberg budget.
- **Other tools:**
  - `integrations/bloomberg/pipeline/backfill_extra_securities_history.py` takes a ticker list and writes
    `opal-data-etfs/bbg-testpull/tickers/{T}/history.csv` (Bloomberg).
  - `data/black_diamond/scripts/silver/fetch_historical_prices_yfinance.py` uses yfinance.

## 3. FWD-10's inputs and the routine it can reuse

- **Opal ETFs:** `s3://opal-data-etfs/silver/holdings/{run_date}.parquet`, with `holding_ticker`, `cusip` and
  `security_name`. Written by `infra/aws/lambda/etfs-pipeline/etfs-netassets-daily/lambda_function.py:1501-1508`, on
  `cron(0 22 * * ? *)`.
- **Rival ETFs:** the canonical_shape above, refreshed Monday to Friday at about 07:10 ET.
- **The FWD-7 pattern:** `E_18.detect_new_securities.py` plans with `etf_classification_scheduled.py`.
  - The write is a conditional put, `attribute_not_exists(ticker)` (`:506`), with `classified_by scheduled`.
  - It calls no LLM (`:30-31`).
  - Wired today only to `bd-securities` (`E_18:289-293`), so `instrument_kind` (fund / single_security) is never filled
    through it (`:405-420`).

## 4. Questions for the CTO, each with this seat's REC

| # | the question | REC |
|---|---|---|
| Q1 | **Key namespace.** How are 516 non-US stocks keyed, given no ISIN or CUSIP? | A third namespace, mirroring the `CUSIP:` rows: key `BBG:<ticker> <exch>` (from `security_bloomberg`, `Equity` dropped), `identifier_namespace: BLOOMBERG`. US listings keep the bare-ticker key. Readers keyed by ticker are unaffected; a reader census (the SC-e-15 pattern) runs before the write. |
| Q2 | **History: which series and whose producer.** | The series is G4 `security_market`, the Rival Funds dialog's own. Extending it to 3 years is ETFS_RIVALS' `enrichment_bloomberg` backfill at site Z, on the Bloomberg budget. Route it as an INPUT dependency, not a laptop cell. This project's cell READS coverage per security (back to `min(3y, first trading day)`) and names every gap as a row. A second source would need Andrew's word. |
| Q3 | **Classification source.** | Derive from the input's own served fields: class `equity` from `asset_class` Equity; sub-class from Bloomberg GICS where RESOLVED, mapped to the table's ratified vocabulary; `instrument_kind single_security`; `classified_by scheduled` and `updated_by rivalfunds-backfill`. Where GICS is UNRESOLVED, write no sub-class and mark it unresolved (`low_confidence`). No new vendor and no model. |
| Q4 | **Domain.** | "Stock" means `provider_security_type` Equity and non-cash. The 17 `Index` futures are out. The window is the input's own (about 2 years today); the 3-year cap binds history, not membership. |
| Q5 | **FWD-10's shape and home.** | A scheduled producer, not a monitor: an E_18-style detector over the Opal ETF silver holdings and the rival canonical_shape, through the same planner and writer and Q1's keys. It runs after both land (daily, after the 07:10 ET refresh) and starts history through Q2's owner. Its runtime and lane, and the read grant on `opal-data-etfs/rivalfunds/etfs/gold/` (the CTO's "laptop cell"), are named at the cut. |

## 5. The cut, once ruled (sketch; nothing issued yet)

| cell | what |
|---|---|
| R7-1 | Reader census for the `BBG:` namespace (if Q1). Then the FWD-9 row writer over the measured universe: about 38 US plus 516 non-US rows, dry run first, under its own never-widen half. |
| R7-2 | FWD-9 history coverage read against G4 `security_market` per security, back to `min(3y, first trading day)`. Gaps go to rows routed to ETFS_RIVALS. |
| R7-3 | FWD-10 producer: detector, writer, schedule, and the read grant cell. |

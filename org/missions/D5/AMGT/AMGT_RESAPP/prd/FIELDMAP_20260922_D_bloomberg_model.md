# D -- BLOOMBERG TERMINAL CHANNELS AND THE MODEL TAB: field-level map

Scope: every Bloomberg (Terminal DAPI) channel feeding AMGT_RESAPP -- model block (refdata / histdata / bestdata),
histdata_daily_px, identity (add-security -> crosswalk/v1), exec_officers (management fallback), and the price axis
(DynamoDB TRENDING_PRICE / BREAKOUT_PRICE). Read-only. No Terminal pull was run. S3 reads were through `.tools/aws`, with
at most 3 to 4 sample objects per prefix. Measured 2026-09-22 against the working tree on branch SITEZ @78106b9cea, and
the portal submodule @f22e369c (= origin/DEV).

Prior inventories were relied on and verified, not re-derived:
- `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/RESAPP_DATA_SHAPE_INVENTORY_20260918.md` s.2 (bronze skeletons; the
  top-level key is the SPACED Bloomberg id; DynamoDB item attribute presence out of 284 items, :344-360).
- `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/PLAN_AMGT_HARVEST_CHANNEL_FORMATS_20260921.md` s.5.1 (:158-198; bestdata,
  identity, exec_officers and pull_log shapes; proposed silver tables).
  Both documents still name the OLD landing `raw/bloomberg/<key>/<stamp>/<request>.json`. That landing has since been moved
  (AMGT-rk-90 M1, `lib/research/harvest/bloomberg.py:331-435`). The live keys are below.

Every Bloomberg call is box-side: the DAPI listens only on loopback 127.0.0.1:8194 on the Terminal machine. Every call goes
through `integrations/bloomberg/mcp/blp_client.py` (`model_block_pull.py:257-266`, `price_axis_pull.py:1-16`).

---

## 0. LIVE STORAGE CENSUS (opal-data-harvest, `s3 ls --recursive | wc -l`, 2026-09-22)

| prefix | objects | distinct securities | notes |
|---|---|---|---|
| `bloomberg/harvest/bronze/refdata/security_key=<k>/<stamp>.json` | 48 | 37 | 30 from one batch on 2026-09-16; 3 x 3 on 2026-09-19 (CAT, CSL, 6861); 2 each for BA and BABA (09-10/09-16); 3 for SAP; 2 for NVDA (09-11) |
| `.../bronze/histdata/...` | 48 | 37 | paired 1:1 with refdata stamps |
| `.../bronze/bestdata/...` | 6 | **3** (CAT US, CSL AU, 6861 JP) | forecasts exist for 3 names only |
| `.../bronze/identity/...` | 3 | 3 (CAT, CSL, 6861) | only names registered through add_security |
| `.../bronze/exec_officers/...` | 4 | 2 (CSL, 6861) | 09-19 + 09-21 each |
| `.../bronze/histdata_daily_px/...` | 1 | 1 (BABA US) | 162 KB, one daily PX_LAST series |
| `bloomberg/harvest/silver/` | **0** | -- | silver `model_block` is built but NOT wired |
| `amgt/harvest/state/pull_log/security_key=<k>/<stamp>.json` | 9 | 3 | only the 09-19 pulls; older stamps have no pull log |
| `derived/model_block/<key>/<stamp>/model_block.json` | 122 | 37 (38 first segments: `BP/` and `NG/` split on the slash) | SERVED JSON the Model tab reads |
| `derived/model_block_fye/...` | 3 | 3 | the FYE-fixed variant; no production reader (CRO plan :165) |
| `crosswalk/v1/<date>.json` | 2 | -- | `2026-09-15.json`, `2026-09-19.json` (newest served) |

Bronze object metadata, read on `refdata/security_key=CAT_US_Equity/20260919T152117Z.json`:
`{schema-version: "1", received-form: "bbg-client-json", document-sha256: <hex>}`. The body is the client's parsed dict,
pretty-printed. The M1 mover copied the old bytes unchanged (`bloomberg.py:367-371`), so the body is not the canonical
`client_json` form that a fresh `bronze_write` would produce.

---

## 1. CHANNEL: BLOOMBERG MODEL BLOCK (refdata + histdata + bestdata) -- primary feed of the Model tab

### 1.1 Channel
- Vendor: Bloomberg Terminal DAPI (blpapi). Mechanism: one `ReferenceDataRequest` (header), one `HistoricalDataRequest`
  (YEARLY) and three `ReferenceDataRequest`s with overrides (forecasts) per security.
- Entry point: `integrations/bloomberg/research/model_block_pull.py`. `stage_pull` is at :432-505 and `stage_derive` at
  :965-1104. The CLI is `pull|derive --securities` (:1173-1183), capped at 3 securities per call (:1179-1180).
- Trigger and cadence today: MANUAL, a hand run on the Terminal box. The backfill proposal names it "manual, 3 names per
  call -> weekly" (`BACKFILL_SCOPE_PROPOSAL_20260922.md:50`). There is no schedule. The PRD reserves the cadence to Andrew
  (`AMGT_RESAPP_PRD.md:1024,1030-1031`).
- An on-demand path also exists: the API's pull-request route enqueues to SQS, and `integrations/bloomberg/research/
  pull_consumer.py` consumes the queue on the box (CRO inventory row 21).

### 1.2 Every mnemonic requested (the complete list)

**A. refdata -- `HEADER_FIELDS` (17), `model_block_pull.py:89-107`, one ReferenceDataRequest, current snapshot.**
Units are from the unit map (`field_map.json`, where one exists) and the basis text is from `FIELD_BASIS` (`:196-254`).

| # | mnemonic | meaning | type / unit |
|---|---|---|---|
| 1 | NAME | Bloomberg issuer short/legal name | str |
| 2 | CRNCY | ISO currency of the trading/reporting line (can be `GBp` = pence) | str |
| 3 | CNTRY_OF_DOMICILE | ISO country of domicile | str |
| 4 | GICS_SECTOR_NAME | GICS sector name | str |
| 5 | PX_LAST | last/closing price, trading currency | float, PRICE |
| 6 | CUR_MKT_CAP | market cap, FULL currency units | float, ABSOLUTE |
| 7 | NET_DEBT | total debt minus cash, MILLIONS, reporting currency; negative = net cash | float, MILLIONS |
| 8 | CURR_ENTP_VAL | enterprise value, MILLIONS | float, MILLIONS |
| 9 | VOLUME_AVG_30D | 30-trading-day average volume, shares | float, ABSOLUTE share count |
| 10 | EQY_SH_OUT_REAL | real-time shares outstanding, absolute | float |
| 11 | EQY_FREE_FLOAT_PCT | free float % of shares outstanding | float, PERCENT |
| 12 | EQY_BETA | Bloomberg beta (default window) | float, RATIO |
| 13 | EQY_DVD_YLD_IND | indicated dividend yield % | float, PERCENT |
| 14 | SHORT_INT_RATIO | short interest days-to-cover | float, RATIO. **Empty for non-US names** (SAP GY, 6861 JP measured) |
| 15 | SI_PERCENT_EQUITY_FLOAT | short interest % of float | float, PERCENT. **Empty for non-US names** |
| 16 | CIE_DES | company description, long text | str |
| 17 | CIE_DES_BULK | company description as a BULK field | list[{"Company Description": str}] in the raw form; joined to one string at derive (`:116-130`) |

`FISCAL_YEAR_END` was probed and is BAD_FLD/INVALID_FIELD, so it is not requested (`:83-84`, `fye_join.py:14-17`).

**B. histdata -- `HIST_FIELDS` (23), `:141-165`, HistoricalDataRequest, `periodicity=YEARLY`,
`start=HIST_START="2016-01-01"` (`:167`), end = today UTC (`_rolling_end_date`, `:317-320`).**

| # | mnemonic | meaning (Bloomberg's own definition, adopted as-is) | unit |
|---|---|---|---|
| 1 | PX_LAST | year-end price (calendar year-end trading day) | PRICE |
| 2 | SALES_REV_TURN | total revenue | MILLIONS |
| 3 | IS_OPER_INC | operating income | MILLIONS |
| 4 | OPER_MARGIN | operating margin | PERCENT |
| 5 | EBITDA | reported (unadjusted) EBITDA | MILLIONS |
| 6 | EBITDA_ADJUSTED | Bloomberg-adjusted EBITDA | MILLIONS |
| 7 | EBITDA_MARGIN | EBITDA margin | PERCENT |
| 8 | IS_EPS | Bloomberg's reported EPS | PER SHARE |
| 9 | BOOK_VAL_PER_SH | book value per share | PER SHARE |
| 10 | IS_SH_FOR_DILUTED_EPS | weighted diluted share count | MILLIONS (shares) |
| 11 | CAPITAL_EXPEND | capex, reported NEGATIVE (cash outflow) | MILLIONS |
| 12 | CF_FREE_CASH_FLOW | free cash flow | MILLIONS |
| 13 | IS_DIV_PER_SHR | dividend per share | PER SHARE |
| 14 | RETURN_ON_ASSET | ROA | PERCENT |
| 15 | RETURN_COM_EQY | ROE | PERCENT |
| 16 | PE_RATIO | P/E at the price-row date | RATIO |
| 17 | CURRENT_EV_TO_T12M_EBITDA | EV / trailing-12-month EBITDA | RATIO |
| 18 | PX_TO_BOOK_RATIO | P/B | RATIO |
| 19 | EQY_DVD_YLD_IND | dividend yield (also in the header) | PERCENT |
| 20 | REVENUE_PER_SH | revenue per share (the sheet's Revenue/Sh row; rk-37) | unit map has NO entry |
| 21 | FREE_CASH_FLOW_YIELD | FCF yield % (FCF yield row; rk-37) | unit map has NO entry |
| 22 | FREE_CASH_FLOW_MARGIN | FCF margin % (FCF margin row; rk-37) | unit map has NO entry |
| 23 | PROF_MARGIN | net profit margin % (Earnings margin row; rk-37) | unit map has NO entry |

RoTA was probed and refused (`RETURN_ON_TOT_ASSETS` and `RETURN_ON_TOTAL_ASSETS` are both INVALID_FIELD). It stays ABSENT
(`:136-140`).

**C. bestdata -- `FORECAST_FIELDS` (5) + `BEST_PERIOD_END_DATE`, `:175-186`. Three ReferenceDataRequests, each with the
override `BEST_FPERIOD_OVERRIDE` = `1FY` / `2FY` / `3FY` (`:470-484`).**

| mnemonic | meaning | unit |
|---|---|---|
| BEST_EPS | consensus EPS for the overridden fiscal year | PER SHARE (the map has no entry on any name) |
| BEST_SALES | consensus revenue | MILLIONS |
| BEST_EBITDA | consensus EBITDA | MILLIONS |
| BEST_PE_RATIO | consensus forward P/E | RATIO |
| BEST_DPS | consensus DPS | PER SHARE |
| BEST_PERIOD_END_DATE | the period end date of the overridden FY. It names the column; it is not itself a figure | "YYYY-MM-DD" |

Without the override, a BEST_ field returns the next QUARTER (`:44-46`, PRD :1018-1019). A guard refuses the whole forecast
set when the three dates are not at least 300 days apart (`:185-186`, `:694-720`).

**Periods:** history is annual fiscal years from 2016 to the latest CLOSED fiscal year. A year counts as closed when
`SALES_REV_TURN` or `IS_EPS` is non-null (`:188-191`, `:981-985`). Forecasts cover FY1 to FY3.
**Currency:** native. No FX conversion is applied anywhere. Statement fields are in the REPORTING currency and PX_LAST is in
the TRADING currency (see 1.6).

### 1.3 Bronze field dictionary (as received: Bloomberg client JSON; `received-form: bbg-client-json`)

**refdata** (sample `refdata/security_key=CAT_US_Equity/20260919T152117Z.json`, 1,363 B):
```
{ "<SPACED Bloomberg id, e.g. 'CAT US Equity'>": {
    NAME: str, CRNCY: str, CNTRY_OF_DOMICILE: str, GICS_SECTOR_NAME: str,
    PX_LAST: float, CUR_MKT_CAP: float, NET_DEBT: float, CURR_ENTP_VAL: float,
    VOLUME_AVG_30D: float, EQY_SH_OUT_REAL: float, EQY_FREE_FLOAT_PCT: float, EQY_BETA: float,
    EQY_DVD_YLD_IND: float, SHORT_INT_RATIO: float?, SI_PERCENT_EQUITY_FLOAT: float?,
    CIE_DES: str?, CIE_DES_BULK: list[{"Company Description": str}]?,
    __field_errors__?: {<MNEMONIC>: {category, code:int, message, subcategory}} } }
```
A field with no value is simply ABSENT from the dict. It is not a null. The 2026-09-16 batch (e.g. `SAP_GY_Equity/
20260916T201948Z.json`, 450 B) carries only 13 keys: no CIE_DES and no CIE_DES_BULK, and the short-interest pair is empty.
That batch predates rk-37.

**histdata** (sample `histdata/security_key=CAT_US_Equity/20260919T152117Z.json`; 6861 JP 20260919T152125Z):
```
{ "<spaced id>": [ { date: "YYYY-MM-DD", <any subset of the 23 HIST_FIELDS>: float }, ... ] }
```
Bloomberg SPLITS each year into two sub-rows:
- A PRICE/RATIO row dated at the calendar year-end trading day (e.g. `2016-12-30`), carrying PX_LAST, PE_RATIO,
  CURRENT_EV_TO_T12M_EBITDA, PX_TO_BOOK_RATIO, EQY_DVD_YLD_IND and FREE_CASH_FLOW_YIELD.
- A FUNDAMENTALS row dated at the issuer's TRUE fiscal period end, carrying the other 17 fields.
When both fall on 12-31 they come back merged (CAT 2018+). For 6861 JP (Keyence, fiscal year ends 03-20) the rows run
`2016-03-20` (fundamentals, 17 fields) / `2016-12-30` (ratios, 6 fields) / ... through `2026-03-20`: 21 rows for 11 fiscal
years.

**bestdata** (sample `bestdata/security_key=CAT_US_Equity/20260919T152117Z.json`, 1,883 B): the producer's own wrapper.
```
{ requests: list[3] of {type:"ReferenceDataRequest", security:str, fields:list[6], overrides:{BEST_FPERIOD_OVERRIDE:"1FY"|"2FY"|"3FY"}, at:"YYYYMMDDTHHMMSSZ"},
  "1FY": {"<spaced id>": {BEST_EPS:float, BEST_SALES:float, BEST_EBITDA:float, BEST_PE_RATIO:float, BEST_DPS:float, BEST_PERIOD_END_DATE:"2026-12-31"}},
  "2FY": {...}, "3FY": {...} }
```

**pull_log** (STATE, not bronze; `amgt/harvest/state/pull_log/security_key=CAT_US_Equity/20260919T152117Z.json`):
`{securities:[str], requests:[{type, security, fields:[..], start_date?, end_date?, periodicity?, overrides?, at}]}`.
`history_window.end_requested` is read back from this log (`:415-429`).

### 1.4 Silver field dictionary: `model_block` (DESIGNED, NOT WIRED -- 0 objects live)
Writer: `lib/research/harvest/bloomberg.py:215-305`. `write_model_block_silver` has zero production callers (`:12-14`).
Target: `bloomberg/harvest/silver/model_block/date=<d>/part-<stamp>.parquet` (CRO plan :178). Record key
`(security_key, fiscal_year, mnemonic)` (`:300-303`). It is a LOSSLESS re-serialisation of the served JSON, ONE ROW PER
FIGURE:

| column | type | meaning |
|---|---|---|
| security_key | str | the doc's `security_key` (else `security` with spaces -> `_`) |
| fiscal_year | str (history) / int (forecast) / null (header) | copied from the figure |
| mnemonic | str | Bloomberg mnemonic |
| scope | str | `header` / `fiscal_year_line_item` / `forecast` |
| unit, sign, source, vintage | str | copied from the figure |
| value_number | float? | numeric value (exactly one of number/text is set) |
| value_text | str? | string value (NAME, CRNCY, CIE_DES ...) |
| basis_json | str | canonical JSON of `basis` |
| figure_json | str | canonical JSON of the WHOLE figure (the round-trip source) |
| figure_index | int | original order |
| doc_json | str | canonical JSON of the document minus `figures` (history_window, unresolved, cases, forecast_fallback) |
| bronze_key | str | the source key |
| fetched_at | str | the fetch time |

Hazard: forecast figures carry `fiscal_year` as an INT (`2027`) while history carries a STRING (`"2025"`). One parquet
column would then hold mixed types.

### 1.5 SERVED JSON field dictionary: `derived/model_block/<security_key>/<derived_stamp>/model_block.json`
Sample read: `derived/model_block/CAT_US_Equity/20260919T152153Z/model_block.json` (126,936 B; 262 figures = 17 header +
230 FY + 15 forecast, 0 unresolved). Also read: `6861_JP_Equity/20260919T152154Z` (277 figures, 2 unresolved) and
`SAP_GY_Equity/20260919T075337Z` (203 figures, NO forecast, raw stamp 20260916). Built at `model_block_pull.py:1077-1093`.
The Model tab renders this, shaped into Adam's Model sheet.

**Top level**

| field | type | example shape | meaning |
|---|---|---|---|
| security | str | `"CAT US Equity"` | spaced Bloomberg id with the yellow key |
| security_key | str | `"CAT_US_Equity"` | spaces -> `_` (`:309-310`). **A slash survives**: `"BP/_LN_Equity"` |
| raw_stamp_used | str | `"20260919T152117Z"` | the bronze stamp derived from (latest refdata+histdata pair) |
| fiscal_years | list[str] | `["2016",...,"2025"]` | CLOSED fiscal years only |
| fiscal_year_row_count | int | `10` | len(fiscal_years) |
| orphan_price_rows | int | `0` | always 0 by construction |
| history_window | obj | `{start:"2016-01-01", end_requested:"2026-09-19", latest_closed_fiscal_year:"2025", rule:str}` | the rolling window; `end_requested` is read from the pull_log, null when there is no log |
| figures | list[obj] | see below | every value |
| unresolved | list[obj] | `{scope, mnemonic, fiscal_year?, fiscal_period?, reason, fallback_status?}` | every requested cell without a value, with its reason. Count in = count out |
| forecast_fallback | obj | `{sa_symbol_candidates:list, sa_symbol:str?, entity_test, classification, gaps_before:int, filled_by_sa:int, sa_raw_key:str?, reason:str, sa_field_map:obj}` | the Seeking Alpha fallback record (`sa_forecast_fallback.py`) |
| cases | obj | `{base:{status:"SERVED", value:float, formula:"consensus EPS (FY1) x trailing-median P/E", inputs:{consensus_eps:{value, mnemonic:"BEST_EPS", fiscal_period:"FY1", fiscal_year:int, period_end_date, source}, trailing_median_pe:{value, mnemonic:"PE_RATIO", window:[str], n:int, source}}, px_last:{value, mnemonic, vintage}?}, upside:{status:"ABSENT", reason}, downside:{status:"ABSENT", reason}}` | Base case, computed once at derive (`:892-962`). Upside/Downside are ruled ABSENT |

`forecast_fallback` and `cases` exist only on blocks derived after rk-36/37. SAP's newest block lacks both
(`_model_cases` then serves "no cases on the landed block", `scoped_amgt.py:2824-2834`).

**`figures[]`, header and fiscal-year scopes** (10 keys):

| field | type | example | meaning |
|---|---|---|---|
| scope | str | `"header"` / `"fiscal_year_line_item"` | which request it came from |
| fiscal_year | null / str | `null` / `"2024"` | calendar year of the row's `date[:4]` (see hazard H1) |
| mnemonic | str | `"IS_EPS"` | Bloomberg field |
| value | float / str | `10.85` / `"CATERPILLAR INC"` | raw Bloomberg value, native currency |
| unit | str | `"MILLIONS"`, `"PER SHARE (local trading/reporting currency)"`, `"PERCENT"`, `"RATIO (dimensionless multiple)"`, `"ABSOLUTE (full currency units)"`, `"PRICE (local trading currency, per share/unit)"`, `"TEXT (string field)"`, `"UNRESOLVED-ON-<sec>: <reason>"`, `"SEE field_map.json (... not yet built)"` | measured unit from the unit map |
| sign | str | `"POSITIVE"`, `"NEGATIVE (Bloomberg cash-outflow convention, ...)"`, `"NEGATIVE (net-cash position)"`, `"N/A (non-numeric field)"`, `"UNRESOLVED-ON-..."` | measured sign convention |
| basis | obj | `{mnemonic, definition:str}` | Bloomberg definition text (C-BLOOMBERG-BASIS) |
| vintage | str | `"2026-09-19T15:21:53Z"` | DERIVE time (not the pull time) |
| source | str | `"bloomberg-dapi"` | constant |
| currency_caveat | str / null | the PE cross-check finding text | set on currency-sensitive fields of 15 flagged names (see 1.6) |

**`figures[]`, forecast scope** (13 keys): `scope:"forecast"`, `fiscal_period:"FY1"|"FY2"|"FY3"`,
`override:"1FY"|..`, `period_end_date:"2026-12-31"`, `fiscal_year:int` (the END year of the period), `mnemonic`, `value`,
`unit`, `sign`, `basis`, `vintage`, `source:"BBG"|"SA_FALLBACK"`, `estimate_basis:"consensus"`. An SA fill adds
`sa_field`, `sa_symbol` and `sa_raw_key` (`:854-875`). Forecast figures carry NO `currency_caveat` key.

**API-side additions (not in the stored JSON).** `read_model_block` applies a "corrected fiscal-price overlay" that can
rewrite fiscal PX_LAST `value` and add `observation_date`, `derivation_key` and `corrected_overlay_status`
(`scoped_amgt.py:957-1010`, `:1087-1102`). The overlay root is `AMGT_MODEL_BLOCK_ROOT`, which defaults to `""`
(`:160-161`), so in the deployed Lambda it is inactive (see H1).

### 1.6 Transformations bronze -> served
1. **Header:** each of the 17 header mnemonics becomes one figure, or one `unresolved` entry carrying the
   `__field_errors__` reason or "empty/no value returned" (`:991-1020`). CIE_DES_BULK rows are joined with single spaces.
2. **History:** `merge_by_fiscal_year` groups rows by `date[:4]`, the CALENDAR year (`:508-525`). A later key overwrites
   an earlier one within a group. Only CLOSED years are emitted. Non-closed years go to `unresolved` (`:1022-1054`).
3. **Forecast:** read back from bestdata. The quarter-trap guard runs first. Empty cells go to the Seeking Alpha fallback
   (`sa_forecast_fallback.run_fallback`), whose fills are tagged `SA_FALLBACK` (`:732-889`). No model/LLM call.
4. **Unit and sign** are looked up per (mnemonic, security) in `integrations/bloomberg/research/field_map.json`
   (`:552-586`). When a security has no entry at all, `build_unit_map.py` builds one at derive (`:619-663`) and writes the
   REPO file. That is a repo write from a producer run, which means the Terminal box's working tree is the unit map's real
   home.
5. **currency_caveat:** attached when `field_map.cross_security_findings` names the security (`:595-616`).
6. **cases.base** = FY1 `BEST_EPS` x median(`PE_RATIO` over all closed FYs) (`:892-962`). There is no FX; it is in native
   units.
7. Dropped: nothing from the raw form except the `date` strings, and the row split noted in 1.3.

**Unit map (`field_map.json`, rk-34 builder `build_unit_map.py`):** `{securities:[36 spaced ids], fields:[32 entries of
{mnemonic, unit:{<sec>:label}, unit_status, sign:{<sec>:label}, sign_status, basis, finding, measured_on,
per_security_detail}], cross_security_findings:[15]}`. Last commit fcbac1c95e (2026-09-19 11:03Z).
Classification is by MAGNITUDE BAND per field family (`build_unit_map.py:146-193`): PERCENT if |v| >= 0.3, else DECIMAL;
ABSOLUTE if > 1e9, MILLIONS if 1 to 1e7; PER SHARE if 0 to 2000; and so on.
- **11 of the 43 requested mnemonics have NO map entry**: CIE_DES, CIE_DES_BULK, REVENUE_PER_SH, FREE_CASH_FLOW_YIELD,
  FREE_CASH_FLOW_MARGIN, PROF_MARGIN and the 5 BEST_ fields. The map covers 32; 17 + 23 + 5 minus 2 overlaps = 43. On the
  CAT and 6861 served blocks these carry `unit: "SEE field_map.json (... not yet built)"`, which the Thesis check face
  classifies REFUSE_NOT_YET_BUILT (`build_unit_map.py:111-117`). The builder only runs for a security with no entry
  (`model_block_pull.py:633-634`), so new mnemonics on already-mapped names never get measured.
- NVDA US Equity is not in `securities`, so every NVDA figure is "not yet built".
- Band failures on non-US names: 6861 JP `BOOK_VAL_PER_SH` (14,313 JPY/sh > 2000 band) and `CURR_ENTP_VAL` are
  `UNRESOLVED-ON-6861 JP Equity`. JPY-scale per-share values and KRW/IDR-scale magnitudes will keep failing these bands.

**Currency and units for non-US names (measured in `cross_security_findings`):** the builder compares a naive PX_LAST /
IS_EPS against Bloomberg's own PE_RATIO. Flagged: all 7 `LN` names quote in `GBp` (pence). Their ratio is about 52 to 100,
so price is in pence and statements are in GBP. Also flagged: `BABA US` (ADR in USD, statements in CNY; ratio 0.169),
`992 HK` (7.78), CHF names NOVN/ROG/ZURN (0.64 to 0.79), `CSL AU` (1.50, AUD price vs USD-reporting), and `HAL`/`VLO`.
Nothing converts. The caveat is text only.

### 1.7 Component map
Route: `/thesis` returns `read_thesis_bundle` (`scoped_amgt.py:1984-2067`), which carries `header_figures`,
`fiscal_year_figures`, `check_face`, `model_status`, `fiscal_years`, `model_cases`, and the whole `read_model()` return
(`:2846-2916`: `fiscal_year_figures`, `forecast_figures`, `forecast_periods`, `forecast_source_counts`, `forecast_reason`,
`cases`). `/overlay` returns `header_figures` (`:1936-1951`).

| component | fields read | server | client |
|---|---|---|---|
| **Model** | all `fiscal_year_line_item` figures (value, unit, sign, basis, vintage, fiscal_year), `fiscal_years`, `cases`, `scores` | `scoped_amgt.py:2846-2916`, `:2017-2029` | `portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx:104-172` -> `modelSheet.ts:38-59,89-161`. Named rows: EPS=IS_EPS, BVPS=BOOK_VAL_PER_SH, Diluted shares=IS_SH_FOR_DILUTED_EPS, DPS=IS_DIV_PER_SHR, Dividend yield=EQY_DVD_YLD_IND, P/E=PE_RATIO, P/B=PX_TO_BOOK_RATIO, ROA=RETURN_ON_ASSET, ROE=RETURN_COM_EQY; EBITDA / EBITDA_ADJUSTED / EBITDA_MARGIN; everything else goes to "Other lines" by subtraction |
| Model: forecasts FY1-FY3 | `forecast_figures`, `forecast_periods` | served (`:2864-2912`) | **NONE.** No portal file at origin/DEV references `forecast_figures` or `forecast_periods`. Only the Base case (derived from BEST_EPS) reaches the page |
| Model: scores | Robustness reads `NET_DEBT`, `EBITDA`, `CF_FREE_CASH_FLOW`, `SALES_REV_TURN` from the block (`lib/research/scores/robustness.py:354-375`). Peers V and Divergence want `BEST_CUR_EV_TO_EBITDA`, `TRAIL_12M_EPS`, `CRNCY_ADJ_MKT_CAP`, `BEST_EPS_STANDARD_DEV` and others (`scores/peers_v.py:75-81`, `scores/divergence.py:49-51`) | `scores/v1/` | ModelTab `ScoresSection` (`:81-105`). **None of those Peers V / Divergence mnemonics is in any current pull** |
| **Lead Panel** (security overlay) | ALL header figures (17 mnemonics, provenance line each) | `scoped_amgt.py:1939` | `components/SecurityOverlay.tsx:110-118` (mounted from `LeadPanel.tsx:358`) |
| Lead Panel: one-line description | header CIE_DES, else CIE_DES_BULK | `scoped_amgt.py:2919-2966` | `components/HeaderBrief.tsx` |
| **Thesis** | header + FY + forecast figures feed `check_face` only; the tab text is D-1 drafting | `scoped_amgt.py:2012-2016` | ThesisTab (check face); `postureCites.ts:217-218` looks up a figure by mnemonic/year for cites |
| **Peers** | header `GICS_SECTOR_NAME`, `CUR_MKT_CAP`, `CNTRY_OF_DOMICILE`, `CRNCY` only: candidate-universe classification and cap for covered names (`lib/research/peers/universe.py:137-143,472-555`). The peer COMPARISON ratios come from the security-scanner universe (`opal-data-portal-v2`, `universe.py:64-69,412-459`), NOT from Bloomberg model_block | peers/v1 | PeersTab (CSC table) |
| **Exec Mgmt** | none from the model block | -- | -- |

### 1.8 Gaps and hazards
- **H1 -- calendar-year join on non-December filers (live in served data).** `merge_by_fiscal_year` groups by `date[:4]`.
  For 6861 JP (FYE 03-20) the served FY "2025" pairs 2025-03-20 fundamentals (IS_EPS 1643.77) with the 2025-12-31
  PX_LAST 56680 and PE_RATIO 34.48, which belong to the fiscal year ending 2026-03. FY "2026" has fundamentals but no
  price/ratios (checked in `mb_6861.json`). So P/E, P/B, EV/EBITDA, dividend yield and FCF yield are about 9 months off on
  every non-December filer, and the Base case's trailing-median P/E inherits that shift. The fix exists
  (`fye_join.py:83-129`, `derive_fye_fixed.py`, the `derived/model_block_fye/` engine, 3 objects). But `model_block_pull`
  still calls the old join, and the adapter's overlay is keyed to a LOCAL dir (`AMGT_MODEL_BLOCK_ROOT`, default `""`), so
  the fix is inactive in Lambda. `fye_join` also drops the ratio fields entirely: it pairs only PX_LAST (`fye_join.py:
  107-128`).
- **H2 -- population lag.** Only CAT, CSL and 6861 have bestdata, CIE_DES and the rk-37 rows. The other 34 served blocks
  come from the 2026-09-16 batch (13 to 15 header scalars, 19 history fields, no forecasts, no `cases`). The portal Model
  sheet still maps Revenue/Sh, FCF yield, FCF margin and Earnings margin to `null`, so it shows them ABSENT even where
  REVENUE_PER_SH etc. exist. Those land in "Other lines" instead (`modelSheet.ts:38-59`, same at origin/DEV).
- **H3 -- forecasts served but not rendered** (see 1.7). The PRD wants FY1-FY3 columns labelled CONSENSUS
  (PRD :1015-1024).
- **H4 -- unit map gaps**: 11 mnemonics are unmapped (1.6), so their cells are REFUSED at the check face.
- **H5 -- keying.** The served key is `security.replace(" ", "_")`, which is ticker-derived. `BP/ LN` gives
  `BP/_LN_Equity` and the served path `derived/model_block/BP/_LN_Equity/...`, splitting on the slash. The bronze partition
  is slash-safe (`BP-SLASH-_LN_Equity`); the served path is not. `WALMEX*_MM_Equity` carries a `*`. A ticker change or
  re-listing mints a new key, and nothing in the block carries a FIGI or ISIN (section 6).
- **H6 -- no FX anywhere.** GBp pence and ADR currency mismatches are flagged in text only (1.6).
- **H7 -- `vintage` is derive time**, not pull time. A re-derive restamps unchanged Bloomberg values.
- **H8 --** pull_log exists only for the 9 stamps from 09-19, so `history_window.end_requested` is null on older blocks.
- **H9 --** the PRD states BEST_ coverage as 33/33/33 (PRD :1019-1020), but live bronze holds bestdata for 3 names. That
  PRD figure came from a probe, not from landed data.

---

## 2. CHANNEL: BLOOMBERG DAILY PRICE HISTORY (histdata_daily_px)
- Entry: `integrations/bloomberg/research/pull_baba_daily_px.py`. HistoricalDataRequest, `PX_LAST` only, DAILY, fixed
  window `2016-01-01..2025-12-31` (`:34-40`). One-off for BABA. Manual.
- Bronze: `bloomberg/harvest/bronze/histdata_daily_px/security_key=BABA_US_Equity/20260911T073221Z.json` (1 object):
  `{ "BABA US Equity": [ {date:"2016-01-04", PX_LAST: float}, ... ] }`.
- Silver: none (proposed `security_price_daily`, CRO plan :173). Consumer: `derive_fye_fixed.py:107-115` ->
  `derived/model_block_fye/` (no production reader).
- Components: NONE directly. It would feed Model P/E pairing once H1 is fixed.

## 3. CHANNEL: PRICE AXIS (Lead Panel ranking) -- DynamoDB TRENDING_PRICE / BREAKOUT_PRICE
- Entry: `integrations/bloomberg/research/price_axis_pull.py`. HistoricalDataRequest `["PX_LAST"]` DAILY over a 30-day
  window ending at `trading_calendar.prev_trading_day` (T-1), in chunks of 20 tickers (`:264-286`). The universe is the
  MEASURED `bloomberg_ticker` values in a worker-deliverable `universe.json` (`:142-163`). Manual. **No schedule exists**
  (backfill proposal row 9, `:58`). **No bronze is kept**: the raw series is discarded after scoring. It violates
  C-RAW-BEFORE-DERIVED.
- Transform: score = 30-day simple return (TRENDING), and % jump of the last observation vs the trailing mean (BREAKOUT).
  Ranked server-side (`lib/research/price/generation.py:235-335`).
- Storage: DynamoDB `opal-harvest-security-metrics`, HASH `axis_date` = `TRENDING_PRICE#<date>[#<generation_id>]`,
  RANGE `ticker`, GSI `axis-rank-index` (CRO inventory :344-360, :610-629).

| attribute | type | meaning |
|---|---|---|
| axis_date | S | `<AXIS>#<as_of>` or `<AXIS>#<as_of>#<generation_id>` (two grammars live, H-16) |
| ticker | S | Bloomberg form WITHOUT yellow key, e.g. `"CAT US"` |
| security_key | S? | crosswalk key when resolved (present on 146 of 284 items) |
| identity_status | S | MEASURED / UNRESOLVED |
| axis, movement, subject, movement_basis, movement_measure, min_absolute_jump_basis | S | movement-gate provenance |
| as_of_date, computed_at | S | T-1 date, compute time |
| rank | N, rank_sort | S | server rank |
| score | N | % return or % jump |
| window_days | N | 30 |
| px_start_date, px_start, px_end_date, px_end | S/N | first/last PX_LAST in the window (native currency) |
| trading_days_observed | N | count |
| baseline_mean, pct_jump | N | BREAKOUT only |
| source | S | `"bloomberg-dapi"` |
| generation_id, payload_hash, state, run_id, coverage_vintage, record_type, row_count, written_at | S | generation/pointer rows |

- Components: **Lead Panel** ranked list and chart (`components/RankedList.tsx:113-117,230` reads `score`, `rank`,
  `px_start_date`, `px_end_date`; `RankedChart.tsx:83`), and the per-name price rank in the overlay
  (`SecurityOverlay.tsx:137-138`, from `scoped_amgt.py:1913-1948`, which keys the point read by `identity.bloomberg`, the
  ticker form). No other component reads it.
- Hazards: keyed by TICKER, not security_key (138 of 284 items have no security_key). There is no bronze, so there is no
  replay or backfill. The universe file is a worker deliverable, not the crosswalk.

## 4. CHANNEL: IDENTITY (add-security) -> crosswalk/v1
- Entry: `lib/research/identity/add_security.py`. ONE ReferenceDataRequest per new security (`:357-360`) with
  `IDENTITY_FIELDS` = `NAME`, `EXCH_CODE`, `LEGAL_ENTITY_IDENTIFIER`, `CENTRAL_INDEX_KEY_NUMBER` (`:54-59`). Manual, once
  per security. `--write-pool` requires `--as-of` = today (`:305-316`).
- Bronze (`identity/security_key=CAT_US_Equity/20260919T011821Z.json`, 183 B):
  `{"CAT US Equity": {CENTRAL_INDEX_KEY_NUMBER:"0000018230", EXCH_CODE:"US", LEGAL_ENTITY_IDENTIFIER:str(20), NAME:str}}`.
  For a non-SEC filer (6861 JP): CIK is absent and there is a `__field_errors__.CENTRAL_INDEX_KEY_NUMBER` entry
  `{category:"BAD_FLD", code:9, message:"Field not applicable to security", subcategory:"NOT_APPLICABLE_TO_REF_DATA"}`.
- Transform: `security_key = "<ROOT>_<EXCH>_Equity"` built from the INPUT id, not from Bloomberg (`:342`). EXCH_CODE is
  compared with the id token (`:376-381`). The CIK is split into int `cik` and 10-char `sec_id`. The result is appended to
  `lib/research/identity/registrations.json` (REPO config), and then `crosswalk.build_crosswalk` rebuilds the pool document.
- **Served crosswalk `crosswalk/v1/2026-09-19.json` (202,505 B).** Top level: `schema_version:int`, `as_of:str`,
  `coverage_source:str` (a worker `universe.json` path), `registrations_source:str`,
  `coverage_vintage:{corpus_root_mtime, read_started_at, read_finished_at, denominator_folders:int,
  ticker_status_partition:{MEASURED, UNRESOLVED}}`, `key_conventions:list[6]`, `denominators:{input_names:89, records:96,
  MEASURED:36, UNRESOLVED:60, with_association_keys:96, association_conventions:list[6], registered:7}`, `records:list[96]`.
- **Record fields (full list):**

| field | type | meaning |
|---|---|---|
| security_key | str? | canonical `<ROOT>_<CC>_Equity`; null when UNRESOLVED |
| bloomberg | str? | `"<ROOT> <CC>"`, no yellow key |
| display_ticker | str? | same as bloomberg |
| model_key | str? | = security_key |
| association_keys | list[str] | every legacy key form (pack key, model key, `security-<hash16>`) |
| exchange | str? | second token of the id |
| share_class | str? | a `/`-separated class marker, else null |
| source_row | obj | `{coverage_source, folder:str?, one_pager_files:list[str], bloomberg_ticker:{value, status, evidence, resolved_at}}` |
| provenance | obj | one prose string per derived field (source_row, raw_identifier, association_keys, security_key, bloomberg, display_ticker, model_key, exchange, share_class, resolution). **Stale: still names `raw/bloomberg/...` keys** |
| resolution | str | MEASURED / UNRESOLVED |
| raw_identifier | str? | id as read |
| identity | obj (only on registered records, 3 of 96) | `{bloomberg_security, name, exchange (Bloomberg EXCH_CODE), lei, cik:int?, sec_id:str?, source (raw key), registered_at, field_errors}` |

- **The 6 keying conventions (`key_conventions[]`, each `{convention, form, measured_on}`):**
  1. `bare-root-pilot-key`: `<ROOT>` (publication-links/v1 pilots)
  2. `security-hash-key`: `security-<first 16 hex of SHA256(source folder)>` (opal_data_harvest)
  3. `pack-key`: `<ROOT>_<CC>` (packs/, SA raw)
  4. `model-key`: `<ROOT>_<CC>_Equity` (derived/model_block, Bloomberg bronze) -- THE canonical security_key
  5. `bloomberg-identifier`: `<ROOT> <CC>` (ONE PAGER bloomberg_ticker cell)
  6. `bloomberg-identifier-with-equity-suffix`: `<ROOT> <CC> EQUITY` (ONE PAGER Identifier cell, stripped)
- Components: every component resolves identity through the crosswalk (`scoped_amgt.py:1704-1865`). The Lead Panel shows
  `display_ticker`. None of the Bloomberg identity values (LEI, CIK) is rendered as a page field. CIK drives the SEC
  filings route (another agent's scope).
- Hazards: 60 of 96 records UNRESOLVED (no ONE PAGER). Only 3 names went through a Bloomberg call. Every other MEASURED
  key comes from a spreadsheet ticker cell, not from Bloomberg. Keys are ticker-derived.

## 5. CHANNEL: BLOOMBERG EXEC OFFICERS (management fallback)
- Entry: `lib/research/management/bloomberg_fallback.py:129-198`. ReferenceDataRequest `["NAME",
  "COMPANY_EXEC_OFFICERS"]`, called by `enrich.apply_bloomberg_fallback` (`enrich.py:589-632`) ONLY when the filing roster
  is not RESOLVED. It runs as a weekly task, which is disabled (backfill proposal row 8).
- Bronze (`exec_officers/security_key=CSL_AU_Equity/20260921T162530Z.json`, 1,487 B). The producer's wrapper, written with
  `indent=2` rather than `client_json`:
  `{security:str, pulled_at:"YYYY-MM-DDTHH:MM:SSZ", response:{NAME:str, COMPANY_EXEC_OFFICERS:list[{"Executive
  Officers": "<name>,  <title>"}], __field_errors__?:obj}}`. CSL has 14 entries; 6861 has 1. Values are redacted here.
- Transform: split on the first `",  "` into `{name, title}`, ASCII-folded (`:117-126`). Each becomes an M-1 officer with
  `{name, role (title or "Officer (Bloomberg, no title returned)"), role_start:null, role_start_basis:"absent",
  tenure_years:null, profile_url:null, lusha_title:null, source:"bloomberg", confirmed:true, enrichment:"NOT-ATTEMPTED",
  age:null}`. The doc also gets `roster_source:"BLOOMBERG_FALLBACK"` and a `fallback` block `{security, field, status
  OK|EMPTY|FAILED, entries_returned, officers_parsed, raw_key, pulled_at, reason, label}` (`enrich.py:605-632`). This is
  folded into served `management/v1/<key>/<date>.json`. Silver `executive_officer` is not built.
- Component: **Exec Mgmt** (`scoped_amgt.py:2577-2627` serves `officers`, `roster_source`, `source_item`, `source_key`, and
  `pool_read NOT_READ` because Bloomberg carries no role start; `ExecManagementTab.tsx:170-171,228` labels the fallback).
- Hazards: no tenure or role start, and the name/title split relies on a two-space separator.

## 6. COMPOSITE FIGI / ISIN / SEDOL -- which Bloomberg fields, and whether any current pull asks
- **No current AMGT production pull requests any of them.** The complete requested sets are HEADER_FIELDS, HIST_FIELDS,
  FORECAST_FIELDS + BEST_PERIOD_END_DATE, IDENTITY_FIELDS (NAME, EXCH_CODE, LEI, CIK), exec officers (NAME,
  COMPANY_EXEC_OFFICERS) and the price axis/daily px (PX_LAST). Searched `lib/**/*.py` and `integrations/**/*.py`: 0
  requests of `ID_BB_GLOBAL`, `COMPOSITE_ID_BB_GLOBAL`, `ID_ISIN` or `ID_SEDOL1`.
- Fields that would carry them: `COMPOSITE_ID_BB_GLOBAL` (composite FIGI), `ID_BB_GLOBAL` (exchange-level FIGI),
  `ID_BB_GLOBAL_SHARE_CLASS_LEVEL` (share-class FIGI), `ID_ISIN`, `ID_SEDOL1`, and also `ID_BB_UNIQUE`, `ID_BB_COMPANY` and
  `TICKER`. The CRO keying research lists all of these for one 12-field identifier request
  (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/RESEARCH_AMGT_KEYING_STRUCTURE_IEFA_20260922.md:14-20,77-79,108,153-154`).
- Measured servability: `ID_BB_GLOBAL` WAS returned on this Terminal by a one-off CRO research pull on 2026-09-15 (values
  like `BBG000...` in `org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_TAB_SCORE_REVIEW_20260915_W/pool_1FY.json:76`;
  request list at `measure.py:129,223`). `COMPOSITE_ID_BB_GLOBAL`, `ID_ISIN` and `ID_SEDOL1` entitlement on this Terminal
  is UNKNOWN: no landed response found.
- Natural home: `add_security.IDENTITY_FIELDS` (`add_security.py:54-59`) -> bronze `identity` -> crosswalk
  `identity.{...}`. That is one extra field per call, no new request.
- Adjacent non-AMGT source: DynamoDB `trade-security-identifiers` (92 rows, `{isin, figi, sedol}` keyed `"<ROOT> US
  EQUITY"`), read by `lib/research/identity/positioning_chain.py:283-309`. It is US-only. Whether its `figi` is composite or
  exchange-level is UNKNOWN.

---

## SUMMARY
1. The Bloomberg Model channel requests 45 mnemonics: 17 header refdata (`model_block_pull.py:89-107`), 23 annual
   history fields 2016-to-today (`:141-165`), and 5 BEST_ consensus fields plus BEST_PERIOD_END_DATE with an explicit
   1FY/2FY/3FY override (`:175-186`). Units are native currency with no FX.
2. Live bronze: refdata 48 / histdata 48 (37 names), bestdata 6 (3 names), identity 3, exec_officers 4, daily_px 1. Silver
   `model_block` has 0 objects; it is designed (`lib/research/harvest/bloomberg.py:215-305`) but not wired.
3. The served `derived/model_block/<key>/<stamp>/model_block.json` (122 objects) is what the Model tab renders. Each figure
   carries {scope, fiscal_year, mnemonic, value, unit, sign, basis, vintage, source, currency_caveat}, and the block adds
   history_window, unresolved, forecast_fallback and cases.base.
4. Only CAT, CSL and 6861 carry forecasts, descriptions and the 4 new rows. The other 34 names are from the 2026-09-16
   batch.
5. Hazard (served data): the calendar-year join puts P/E, P/B, EV/EBITDA and yields about 9 months off on non-December
   filers (6861 FY2025 measured). The FYE fix exists but is not wired.
6. The unit map lacks entries for 11 mnemonics (all BEST_, CIE_DES*, REVENUE_PER_SH, FCF yield/margin, PROF_MARGIN), and
   the check face refuses those cells. There is no FX conversion: 7 LN names quote in pence, and ADR/CHF/AUD mismatches are
   flagged in text only.
7. Portal (DEV f22e369c): the Model tab renders fiscal figures and the Base case but NOT the FY1-FY3 forecasts. The Lead
   Panel overlay shows all header scalars and the price rank. Peers uses only sector, cap, country and currency from the
   header (peer ratios come from the scanner). Exec Mgmt uses the COMPANY_EXEC_OFFICERS fallback.
8. The price axis writes DynamoDB TRENDING/BREAKOUT_PRICE rows keyed by ticker. It keeps no bronze and has no schedule.
9. Crosswalk/v1 records have 11 base fields plus `identity` on 3 registered names, and 6 key conventions. The canonical
   key is ticker-derived `<ROOT>_<CC>_Equity`, and a slash survives in served paths (`BP/_LN_Equity`).
10. No production pull requests composite FIGI, ISIN or SEDOL. `ID_BB_GLOBAL` is proven servable (CRO 09-15 probe);
    `COMPOSITE_ID_BB_GLOBAL` entitlement is UNKNOWN. The natural home is `add_security.IDENTITY_FIELDS`.

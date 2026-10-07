# MDPF_SECHIST round 2 -- intake measurements (FWD-2, FWD-3, FWD-4/5; C-SERIES, C-DEPTH, C-GAP, C-IDENTITY)

Measured 2026-10-07T19:09Z by a read-only intake for 2.0.0_SA_COO~H1; nothing written elsewhere, no vendor call.
Host DESKTOP-HK1UU7N (dell1), IAM user cloudops-dell1-agent-user. S3/DynamoDB reads via boto3, default profile.

## 1. FWD-2 / C-SERIES -- where the one series per security lives today

Readers (code at HEAD):
- Gold `data/etfs/scripts/gold/etf_positioning_gold.py`: `load_history` :731 lists `bbg/<date>/` prefixes, keeps
  partitions within HISTORY_LOOKBACK_DAYS=400 (:320), reads `bbg/<date>/history_topup.parquet` (:763), then appends
  `_load_backfill_history` :675/:783. Keyed by `_strip_bbg_security` :670 (first token of label) at :791.
  De-dup: populated beats NaN, scheduled beats backfill as tiebreak (comment :780-800).
- `_load_backfill_history` selects every key ending `/history.csv` under `bbg-testpull/tickers/` (:694) and takes the
  ticker from path segment 2 (:705). CONSEQUENCE: it ALSO reads `tickers/<T>/gap_*/history.csv`.
- Pull `integrations/bloomberg/pipeline/etf_daily_pull.py` `earliest_held_dates` :285 reads the same partitions plus
  only `tickers/<T>/history.csv` (len(parts)==4, :327) -- it does NOT see gap_* files. Gold and pull disagree on
  what the frozen store holds (gap files counted by gold, not by the depth planner).
- Round-1 depth lands in the SAME `history_topup` artifact, "no new address" (pull :538-539).

Stores in s3://opal-data-etfs (listed in full, paginated):

| store | objects | securities | rows | date range | columns |
|---|---|---|---|---|---|
| `bbg/<date>/history_topup.parquet` (+ .csv twin) | 33 parquet + 33 csv, 33 date prefixes 2026-08-20..2026-10-06 | 186 distinct labels | 5,390 | 2026-08-20..2026-10-06 | date, PX_LAST, DAY_TO_DAY_TOT_RETURN_GROSS_DVDS, security (33 of 33 identical) |
| `bbg-testpull/tickers/<T>/history.csv` | 173 (176 ticker dirs; 357 objects under bbg-testpull/) | 173 | 168,341 | first date: 2020-12-31 x101, 2025-07-21 x62, other x10; last date: 2026-08-20 x109, 2026-08-24 x62, 2026-09-11 x2 | date, price, return (173 of 173) |
| `bbg-testpull/tickers/<T>/gap_20261001_20261005/history.csv` | 57 | 57 | 171 | 2026-10-01..2026-10-05 (all 57) | date, price, return |

Other bbg-testpull objects: 109 `tickers/<T>/characteristics.csv`, 4 `fund_daily.csv`, `combined/` 9, `code/` 4, README 1.
bbg-testpull LastModified 2026-08-21..2026-10-06 (the gap folder is the 2026-10-06 write).
Per-day history_topup row counts: 171 typical; 113 on 2026-10-01/02/05; 170-173 elsewhere.
No partition has a date before 2026-08-20: round-1 depth (`history_backfill`) has not landed -- 0 of 33 top-level
run_manifest.json carry a `history_backfill` key.

Key form today: first token of the Bloomberg label, upper-case (gold :670, :705; pull `_ticker_of` :235). Labels
measured: 185 `<T> US Equity`, 1 `<T> B US Equity`; first-token collisions 1 (`QXO` <- `QXO US Equity`, `QXO B US
Equity`). The frozen store is keyed by directory name = bare ticker only.
C-IDENTITY would need: the series keyed by the `etf-classifications` hash key verbatim (bare / `CUSIP:` / `BBG:<tkr>:<exch>`;
live scan 3,786 rows = 2,735 bare, 626 BBG:, 425 CUSIP:; describe-table ItemCount 3,508 is approximate), carried as
a column, not derived from a label token or a path segment.

Rule 30: any new address/name is builder output, `lib/opal_naming.py` `address()` :1849, `name()` :2033; a frozen
store is read via `legacy_address()`. Builder exposes (printed): address, name, key, lookup, legacy_address,
reporting_destination, preview_reporting_destination, reporting_policy, validate, grade, generate, census*,
load_registry, registry_hash, load_schema, build_vectors, targets_report, fence_patterns, plus constants (BLOCKS, VIEWS,
REGISTRY_FILES, TARGET_REGISTRY_KEYS, ...). No address is proposed here.

## 2. COTBKF price-need file (@50a35d3ada)

`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~27/PRICE_NEED_FOR_SECHIST.csv`: 4,545 rows,
4,545 distinct security_id, columns security_id, asset_class, source, first_date_needed, last_date_needed, days_needed.
Companion JSON: end 2026-06-23, fetched 0, sums_ok true; never_priced 2,914 securities / 6,259,410 days, gap_only
1,631 / 1,831,900. Days = every NYSE trading day from first Trade_Date, an UPPER BOUND (JSON `basis`).

| source | asset_class | securities | security-days | earliest first_date_needed |
|---|---|---|---|---|
| YAHOO | Equity | 1,784 | 3,173,008 | 2013-04-08 |
| YAHOO | Mutual Fund | 975 | 1,855,921 | 2013-04-08 |
| YAHOO | ETF | 311 | 351,504 | 2013-04-08 |
| YAHOO | Mutual Fund (Closed End) | 98 | 224,422 | 2013-04-08 |
| YAHOO | Unit Investment Trust | 58 | 168,921 | 2013-04-08 |
| YAHOO total | | 3,226 | 5,773,776 | 2013-04-08 |
| BLOOMBERG_SITE_Z | Fixed Income | 778 | 1,747,877 | 2013-04-08 |
| BLOOMBERG_SITE_Z | Cash Equivalent | 487 | 476,076 | 2013-04-09 |
| BLOOMBERG_SITE_Z | Annuity | 29 | 60,198 | 2013-04-30 |
| BLOOMBERG_SITE_Z | Alternative Investment | 22 | 25,294 | 2013-04-10 |
| BLOOMBERG_SITE_Z | Cash | 3 | 8,089 | 2013-04-03 |
| BLOOMBERG_SITE_Z total | | 1,319 | 2,317,534 | 2013-04-03 |

last_date_needed max 2026-06-23 both sources. Pre-2010 first_date_needed: 0 rows (trading_calendar safe).
security_id shape: 4,544 of 4,545 are 9-char [0-9A-Z]; 1 other (`CFNCASH`, BLOOMBERG_SITE_Z). Of the 4,544, CUSIP
check digit valid 4,523 (YAHOO 3,216 of 3,226; BBG 1,307 of 1,318); 21 fail the check digit (YAHOO 10, BBG 11).

yfinance 1.7.0 (`...\Python314\Lib\site-packages\yfinance\`), source read only: the string "cusip" occurs 0 times in
the package. `base.py:102-112` accepts an ISIN as the ticker (`utils.is_isin` :225, `^[A-Z]{2}[A-Z0-9]{9}[0-9]$`) and
resolves it by `utils.get_ticker_by_isin` :254 -> `Search(query=isin)` (`utils.py:236`) -- a Yahoo network call per
security. So: NOT keyable by CUSIP. Options: (a) US+CUSIP+check digit = ISIN (deterministic, no map) then one Yahoo
Search per ISIN (extra vendor calls, unmeasured hit rate); (b) a CUSIP->symbol map, then `Ticker(symbol)`.

Maps found in the repo/estate:
- cot's OWN data: Commonwealth silver transactions (`opal-data-assets/commonwealth/cottonwood/silver/transactions/
  date=2026-06-23/`, 14 parquet, via `address()` in `data/assets/scripts/analysis/commonwealth_price_census.py:307`)
  carries Cusip+Symbol; the census already matches "CUSIP first, else Symbol" (`:717`, `read_universe` :336).
  Measured: YAHOO 3,101 of 3,226 have a non-blank Symbol (3,086 alphabetic <=5 chars, 15 other); 210 of the 3,101
  carry a Symbol claimed by more than one CUSIP (census does not credit those). BBG_SITE_Z: 67 of 1,319.
  Symbols are as-traded and may be retired (e.g. CTL, CHK); Yahoo coverage of retired symbols NOT MEASURED.
- `etf-classifications` (hash `ticker`): no attribute holds both a CUSIP and a ticker (attribute census over 3,786).
- `bd-securities` (hash `ticker`, 10,965 rows scanned): no cusip-named attribute; not a map. (49f-firm table.)
- `lib/research/identity/crosswalk.py` resolve(): CUSIP/ISIN/SEDOL/ticker -> `<ROOT>_<CC>_Equity`, research-coverage
  universe; its coverage of these 3,226 CUSIPs NOT MEASURED. Rival `gold_canonical_shape.py:117` uses it.
- 49f Schwab fact_uln/fact_rps carry cusip+ticker_symbol+isin, but are another firm's data: NOT usable for cot.

## 3. First appearance by firm (C-DEPTH client point). One object read per store; firms side by side, never joined.

Note: per `lib/opal_naming.lookup()`, `bd` and `49f` are ONE firm (key 49financial): bd = its Black Diamond tree,
49f = its Schwab masters 08242234 / 08335338.

| firm / store | producer path:line | object read | first-date col: min .. max | distinct securities |
|---|---|---|---|---|
| bd (49financial via BD) `s3://opal-data-bd/gold/timeseries/holdings_lots/` (101 objects) | `data/black_diamond/scripts/gold/B_01.holdings_lots.py:22` (doc), :1078 (set) | `2026-10-02.parquet`, 1,294,122 lots | acquisition_date 1996-02-07 .. 2026-10-02, null 0 | cusip 10,204; ticker 4,064 |
| inf `s3://opal-data-inf/gold/lots/` (145 objects) | `data/inf/scripts/gold/INF_B_02.canonical_lots.py:275` (buy_date=trade_date), out :62 | `lots_latest.parquet`, 68,399 lots | buy_date 2020-01-01 .. 2026-10-06, null 0 | ticker 247 (no cusip column) |
| 49f Schwab 08335338 `opal-data-assets/schwab/08335338/silver/fact_uln/` (566) | schema `data/assets/scripts/silver/schwab_schemas.py:499-500` | `date=2026-10-06/data.parquet`, 330,110 | acquired_date 2001-09-19 .. 2026-10-06 (null 0); orgpurch_date same range (null 3) | cusip 805; ticker 743 |
| 49f Schwab 08242234 `.../08242234/silver/fact_uln/` (686) | same | `date=2026-10-06/data.parquet`, 328,473 | acquired_date 2001-09-19 .. 2026-10-06 | cusip 786; ticker 724 |
| cot `opal-data-cot/gold/timeseries/holdings_lots/` | `data/cot/scripts/gold/B_01.holdings_lots.py` exists (bucket default `opal-data-cot` :152) | ABSENT: 0 objects; `gold/timeseries/` holds only positions_cube/ | -- | -- |
| cot current `opal-data-assets/blackdiamond/cottonwood/silver/fact_holdings/` (88) | `data/cot/scripts/gold/E_18.detect_new_securities.py:88` | `date=2026-10-06`, 21,081 rows | no acquisition column (26 columns read) | -- |
| cot history (ADVI_COTBKF) Commonwealth silver transactions | `commonwealth_price_census.py:307` | 14 parquet, 1,416,497 rows | Trade_Date 2013-04-03 .. 2026-06-22; per-CUSIP first trade median 2018-03-14 | Cusip 4,634 |

Caveats measured: bd first appearance per CUSIP median 2023-08-18, pre-2010 3 CUSIPs; bd lots with
acquisition_date == snapshot_date 24,689 (synthetic lots, :1330) -- those are not true first appearances.
fact_rps (both masters) has NO acquired_date/orgpurch_date column (brief PART IV.4 lists it; only fact_uln has them).
49f fact_uln per-CUSIP median first 2024-01-03 / 2024-02-05; pre-2010 17 CUSIPs each; the two masters share 4,069
accounts (of 4,086 / 4,082) -- largely the same book, union not double-count. inf: 45 of 247 tickers first at exactly
2020-01-01, consistent with an opening-balance floor, not a purchase date. Pre-2010 dates exist for bd and 49f:
calendar counts there must not use lib/trading_calendar.

## 4. Gap record (enrichment 1; FWD-4/5, C-GAP)

What the pull records: `vendor_observations` = {label minus " US Equity": rows Bloomberg returned in the run's window}
(`etf_daily_pull.py:508-516`, built from the response; universe members with no rows recorded as 0), written in
`bbg/<date>/run_manifest.json` (:682) with `vendor_observations_note` (:683). It is a COUNT per run window, not a list
of dates. 30 of 33 top-level manifests carry it (3 do not; not named); recent ones hold 171-172 keys with 1 zero
(114 on 2026-10-01/02/05). Readers: comp-find `vendor_observations` = 14 hits / 61,316 files; SURFACED 4, none a
reader (the producer's two lines, a docstring mention in `lib/research/price/axis.py:13`, a HUD log line). No reader
exists. Gold explicitly does not detect an interior gap (`etf_positioning_gold.py` compute_returns docstring, ~:870-890).

Interior missing weekday over the last 20 history_topup partitions (2026-09-09 .. 2026-10-06), union de-duped on
(security, date): 186 securities; 58 have >= 1 interior missing weekday; 174 missing security-weekdays, all on
2026-10-01, 2026-10-02, 2026-10-05 (58 each). Within any single partition: 0 of 3,240 (security, partition) pairs.
57 of the 58 have a `gap_20261001_20261005/history.csv` in bbg-testpull (gold reads it, :694; pull's depth planner
does not, :327); the 58th is `QXO B US Equity`, which the ticker-keyed frozen store cannot hold (its gap folder `QXO`
would key to `QXO US Equity`). Weekday counting over-counts exchange holidays (none fell in this window by weekday
count; NOT checked against the calendar) and non-US trading calendars.

## NOT MEASURED

- `s3://opal-data-cottonwood/` -- ListBucket AccessDenied (explicit deny in bucket policy) for cloudops-dell1-agent-user.
- Yahoo coverage/hit rate for the 3,226 CUSIPs or their Commonwealth Symbols (would need a vendor call; not made).
- Coverage of `lib/research/identity/crosswalk.py` over the COTBKF CUSIPs; content of `ticker_resolution.parquet`
  (bd gold dimension, read by B_01) as a CUSIP->ticker source.
- The 3 run_manifests lacking vendor_observations were not individually named; earlier-than-20 partitions not gap-scanned.
- bd holdings_lots: only the newest of 101 objects read (closed-before-snapshot lots not visible, per brief PART IV.4).
- inf/49f/bd per-security first appearance intersected with any ingestion point or with the ETF universe.
- Exchange-holiday correction of the weekday gap count.

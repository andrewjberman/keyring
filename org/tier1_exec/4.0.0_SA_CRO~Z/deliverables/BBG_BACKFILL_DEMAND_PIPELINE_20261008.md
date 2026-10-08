# Bloomberg backfill demand: every planned, pending and per-onboarding pull, sized in cells

**From:** 4.0.0_SA_CRO~Z. **For:** Andrew, on his question about demand for Rival Funds, the Positioning performance views,
and ADVI / IRPT onboarding backfills ("we may need to start being more clever with how we script these ingestions ... and
developing our reserves").
**Read:** 2026-10-08 ~18:4xZ-20:xxZ. Sources were records, code, S3 listings and small S3 reads. No Bloomberg call was made,
nothing was pulled, and no code, config, schedule or S3 object was changed.
**Unit:** a cell is one value. For history it is securities x fields x dates; for reference data, securities x fields; for
a BQL query through Excel, rows x columns returned (16 per rivalfunds holdings row). **M** = measured in this read or in
the cited record's own count. **E** = estimated, with the arithmetic shown.

## Summary table

| # | Backfill | Surface it feeds | Securities x fields x dates | Cells | Request type | Kind | Status | Paced by |
|---|---|---|---|---|---|---|---|---|
| 1 | Rival Funds D13: ACWI + IWM holdings history | Rival Funds page, benchmark rankings and trend | ~4,233 rows per date (M, probes) x 189 dates (M) x 16 columns | **~12.8M (E)**; plus ~67,700 a day once ACWI and IWM join the daily queue (E) | BQL holdings via Excel | one-time, then recurring | PENDING; stopped at the 2026-10-05 block | `check_backfill` (rows) |
| 2 | MDPF_SECHIST card A: Cottonwood client securities' price history (Bloomberg part) | Investor Reporting / Advisor Intelligence: a client security's performance since it was first held | 1,319 securities (M), 2,317,534 security-days (M) x 1-2 fields | **2.32M-4.64M (E)** | historical data, keyed by CUSIP | one-time, per onboarding firm | APPROVED, no code, held | ledger intended; no code yet |
| 3 | Rival Funds FWD-24: a year of closes for every security held in the last 365 days | Rival Funds security dialog, price curve and trade markers | 742 securities (M) x 1 field (PX_LAST) x 251 trading days (M); 184,600 owed (M) | **184,600 (M owed) one-time**; then ~300-900 a day (E) | historical data | one-time catch-up, then daily | APPROVED 2026-10-08; switch not set | `check_points` + cap 20,000 a run |
| 4 | AMGT_CORPUS daily refresh of the 96 model blocks | AMGT Model tab | 96 names (M) x 25 header + 83 history fields (~15 rows) | **74,255 a day (M, 10-08 fire)** | reference + historical data | recurring daily, and per new research name | RUNNING since 2026-10-03 | **none: not on the ledger** |
| 5 | AMGT price axis, rolling 30-day PX_LAST | AMGT price ranking (30/90/365 days) | 94 names (M) x 1 field x ~22 days | **~2,089 a day (M)** | historical data | recurring daily | RUNNING | none |
| 6 | Positioning: one-year depth fill for each new Opal ETF holding (SECHIST SH-t-1) | Positioning > ETFS > Holdings Breakdown, Performance toggle (1D..1Y) | 15 securities on its first run (M); ~265 days x 2 fields each | **5,858 on its first run (M)**; ~530 per new holding (E); ~800 a day asked for 3 securities Bloomberg cannot price (E) | historical data | per new holding (automatic) | RUNNING inside the daily pull | ledger (`etf_daily_pull.py:560-609`) |
| 7 | Positioning daily top-up and characteristics | same page | 172 securities (M) x 2 history fields x 1 day; 172 x 14 reference fields | **~2,770 a day (M rows x fields)** | historical + reference | recurring daily (production) | RUNNING | none (production) |
| 8 | Other client firms' securities (BD, 49 Financial, Inflection) | same as #2 | BD 10,204 CUSIPs, 49F 811 + 786, INF 248 (M counts); history need not computed | **not sized** (rule of thumb below) | historical data | per onboarding | NO PLAN, NO RECORD | n/a |
| 9 | IRPT_YCDGEN FWD-14: daily sector and country spread of the funds clients hold | IRPT report sector and country pages, as of past dates | not specified | **not sized** | not specified | recurring daily | APPROVED, not started ("Bloomberg quota") | n/a |
| 10 | Security classification on onboarding (MDPF_SECCLASS) | ETFClassifier table, every classed surface | n/a | **0 Bloomberg cells (M by code read)** | none (AI classifier, reused rivalfunds GICS) | per new security | RUNNING | n/a |
| -- | Already done, for scale | | | Positioning 2026-08 backfills 296,814 + 34,152; GLD/VXX 5,716; gap fill 342; AMGT year pull 26,081; D12 IDVZ/PFOE 12,820 rows = 205,120 (all M) | | | DONE | |

**Biggest:** #1, the ACWI + IWM holdings history, at about 12.8 million BQL cells. It is also the only one that draws on BQL,
the meter that blocked the Terminal on 2026-10-05. **Biggest that is not BQL:** #2, Cottonwood, 2.3M-4.6M history cells.
**Biggest recurring and unguarded:** #4, about 74,000 cells a day, of which about 72,000 are bytes identical to the day
before.

## 1. Rival Funds D13: ACWI and IWM holdings history (ETFS_RIVALS)

- **Purpose and surface.** ACWI is the index control for IDVZ's peer group and IWM for PFOE's (PRD v0.8,
  `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md:635-638`; RFW-D13 at `:872`: "ACWI and IWM appear as benchmarks
  with their own rankings and trend"). The pull gives the Rival Funds page those two benchmarks' holdings back to 2026-01-02.
- **Size.**
  - Rows per date: ACWI 2,280-2,283 and IWM 1,953-1,957 (M, probes of 2026-01-02 and 2026-01-16, rows Z-S21/Z-S22). That is
    about 4,233 rows per date.
  - Dates: 2026-01-02 to 2026-10-02, **189 trading days** (M, `lib/trading_calendar`). Through 2026-10-07 it is 192.
  - Columns: 16 per row (M, `BBG_CELL_TRACKING_RECONSTRUCTION_20261005_BLOCK_20261008.md` section 3).
  - Total: 4,233 x 189 = **~800,000 rows = ~12.8M cells (E)**.
- **What 2026-10-05 already spent on it and kept.** 76,859 + 84,655 rows plus about 8,500 probe rows (M, row evidence), about
  2.7M cells. **Nothing from those chunks was kept.** `C:\bbg_backfill\acwi_iwm\` holds 20 capture files, and all 20 are the
  07:06Z blocked chunk with 0 rows (M, file count this read). So the full 189 dates are still owed.
- **Request type.** BQL `holdings()` through Excel (`data/etfs/scripts/rivalfunds/collector_bloomberg.py:386` `excel_fetch`),
  `--mode backfill`.
- **Kind.** One-time. Once the D13 gate flips, ACWI and IWM also join the **daily** queue (PRD `:663-666`). That adds
  ~4,233 rows, or ~67,700 cells, every day (E). Today's daily holdings capture is 748 rows (M, ledger 2026-10-08), so the
  flip would multiply the daily BQL draw about 6.7 times.
- **Pacing.** `bbg_budget.check_backfill` (`collector_bloomberg.py:615-616`) prices it at `est_rows_per_fund_date` ACWI
  2,198 + IWM 1,979 = 4,177 rows per date (`bbg_budget.json`). Against the 120,000-row backfill allowance that is about 28
  dates a day, or 7 days. But the Terminal's BQL capacity blocked at about 183,000 rows (M floor, 2026-10-05), and that
  limit is not the ledger's. The run stays stopped until it can be paced "in smaller daily slices" (row Z-S24,
  `surprise-channel/investigations/INVESTIGATION_v1.Z.md:3344`).
- **Authority.** Andrew-direct 2026-10-01 ~18:2xZ (PRD v0.8, record @19c5277a57; "Use Russel 2000 for PFOE, ACWI for
  IDVZ"); CTO~Z budget ruling msg 29445 (1M rows, per date, stop on first failure); the 3-year lookback ceiling
  `org/tier1_exec/2.0.0_SA_COO/deliverables/cooRV_ANDREW_DIRECT_20261005_03xxZ_RIVALFUNDS_LOOKBACK_CAP_3Y.md`; the plan
  `deliverables/2.0.0_SA_COO~RV/round8/BACKFILL_D12_PLAN.md:33-34`. The D12 sibling (IDVZ + PFOE, 12,820 rows, 205,120
  cells) is done (M).

## 2. MDPF_SECHIST card A: Cottonwood client securities (ADVI / IRPT onboarding)

- **Purpose and surface.** FWD-2: "A client's security shows performance for the whole time the client has held it"
  (`org/missions/D8/MDPF/MDPF_SECHIST/prd/MDPF_SECHIST_PRD.md:37-41`). The reader is Investor Reporting; ADVI_COTBKF's
  C-SCOPE-OUT leaves which product reads it open.
- **Size (M, record).** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~27/PRICE_NEED_FOR_SECHIST.json`:
  - Universe 4,634 CUSIPs; 4,545 need prices, over 8,091,310 security-days (every trading day from the CUSIP's first trade
    date to 2026-06-23; the file calls it an upper bound).
  - Routing by PRD v0.4 Addendum 2: Yahoo for equities, ETFs and funds (3,226 securities, 5,773,776 days); **Bloomberg for
    the rest: 1,319 securities, 2,317,534 security-days** (fixed income 778 / 1,747,877; cash equivalents 487 / 476,076;
    annuities 29; alternatives 22; cash 3). That is about 1,757 days per security, back to 2013.
  - Fields are not chosen; the estate's patterns are PX_LAST alone or PX_LAST + DAY_TO_DAY_TOT_RETURN_GROSS_DVDS.
  - **Cells: 2.32M at one field, 4.64M at two (E).**
  - Only 67 of the 1,319 carry a ticker, so requests are CUSIP-keyed.
- **Kind.** One-time for Cottonwood; the same pull recurs for each new firm (section 8).
- **Code and pacing.** None yet: cell SH-t-5 is "HELD, not cut" (`MDPF_SECHIST_DECOMP_R2.md:13`). The approval binds it to
  the ledger. At the full 120,000 a day it takes about 20 days. At the ~48,900 a day left after AMGT and the daily legs
  (pacer statement, msg 31560) it takes about 48 days (E).
- **Authority.** `org/tier1_exec/2.0.0_SA_COO~H1/ANDREW_DIRECT_20261007_185xZ_SECHIST_NEXT_CALLS_ALL_RECS_APPROVED.md` CALL 1,
  on card `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/ANDREW_CARD_SECHIST_COTTONWOOD_PRICE_HISTORY_VENDOR_PULLS_20261007.md`
  part A. The Yahoo part B is a separate yes. **If B were refused and Bloomberg took all of it, the Cottonwood need is 8.09M
  security-days, 8.1M-16.2M cells (E).**

## 3. Rival Funds FWD-24: a year of closes per held security (ETFS_RIVALS)

- **Purpose and surface.** The price curve in the Rival Funds security dialog. "A security a fund bought this week has a
  full year's curve in its modal" (PRD `:453-480`, Addendum G `:1204-1259`).
- **Size.**
  - Population, from the latest universe object
    `s3://opal-data-etfs/rivalfunds/etfs/gold/security_universe/date=2026-10-07/universe-20261008T130817Z-c0506f7d71fa.parquet`
    (M this read): 1,051 rows, 787 security_ids, **742** with a Bloomberg key and last seen on or after 2025-10-08 (the
    `history_owed.py:46-49` filter). ACWI and IWM holdings are not in it: the 13 funds listed are the rivals only.
  - Window 2025-10-08 to 2026-10-07: **251 trading days** (M). 742 x 251 = 186,242.
  - Owed: **184,600 points over 251 dates** (M, RIV-ho-1's live read 2026-10-08, `STATUS.md:17`). Stored closes cover only
    6 dates today (9 objects, M).
  - Field: PX_LAST only (`enrichment_bloomberg.py:720`). Plus one CRNCY reference lookup for securities with no stored
    currency, at most 742 cells (E).
  - **Cells: ~184,600 one-time (M), ~185,300 with the currency lookups (E).**
  - After the catch-up: about 355 new (fund, security) entries a year at 251 closes each, plus the widened daily list (742
    held within 365 days against 581 priced today, M). That is ~300-900 cells a day (E).
- **Code and pacing.** `enrichment_bloomberg.py:928-1004` (`_history_owed`), switched by `RIVALFUNDS_HISTORY_OWED` (unset on
  this box). Every request is checked against `bbg_budget` (`check_points`, `:815-862`) and recorded as points requested.
  The per-run cap is `HISTORY_OWED_CAP`: 5,000 in code (`:901`), 20,000 after round 28 (commit 8d50ab6e32). At 20,000 a
  morning the catch-up takes about 10 mornings.
- **Authority.** Andrew-direct 2026-10-08 ~17:1xZ card 5, "Yes I like this strategy"
  (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_171xZ_OPEN_CALLS_SIX_ANSWERED_AND_CELL_TRACKING_ASK.md:21`).
  It runs after three writer fixes (currency, trading date, window end). The earlier ad hoc one-time backfill (RIV-bk-1,
  planned 863 x 252 = 217,476) is the same owed set (Addendum G.3 `:1245-1246`). It is **not counted twice** here.
- **Not this.** Funds still short of a year of holdings history: WCMG 95 of 252 dates (first 2026-04-23), ETFT 210, PCLG
  230 (CRO analysis 2026-10-07). No backfill is planned or authorized for them, and their launch dates were not read. At
  ~45-150 rows per fund-date (E) they are small (under 0.5M cells together, E).

## 4. AMGT_CORPUS: the daily model-block refresh (and new research names)

- **Purpose and surface.** The AMGT Model tab: header figures, fiscal-year history and forecasts for every covered name
  (FWD-22, `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md:622-639`).
- **Size (M, this read)** on the 2026-10-08 13:14Z fire, under `s3://opal-data-harvest/bloomberg/harvest/bronze/`:
  - `histdata/`: 96 objects, 1,499 fiscal-year rows, 71,988 values;
  - `refdata/`: 96 objects, 2,267 values;
  - **74,255 cells a day**, about 773 per name. Field list: header 25, history 83, forecast 12
    (`deliverables/2.0.0_SA_COO~X/C3_PLANNED_POPULATION_FIRE_20261008.md:40`).
- **Repetition (M).** 95 of 96 `histdata` objects of 2026-10-08 are byte-identical to 2026-10-07; 0 of 96 `refdata` are.
  The fiscal-year history (~72,000 cells) is re-pulled unchanged every day. Only the ~2,300 reference cells move.
- **Per new research name.** A new research-library folder adds a name to the population
  (`C3_PLANNED_POPULATION_FIRE_20261008.md:18-20`): about 773 cells a day for every day it stays (E from the mean).
- **Code and pacing.** Scheduled task `amgt-induction-daily`, 13:00Z (`integrations/bloomberg/research/model_block_pull.py`
  `refresh`). **Not on the budget ledger** (pacer note `MDPF_SECHIST_PACER_20261007.md` section 2, claim 2). Its 2026-10-05
  fire was refused 96 of 96 for capacity.
- **Authority.** PRD FWD-22, Andrew-direct 2026-10-01 03:4xZ ("so they update automatically"). The PRD's WAIT line asks for
  Andrew's standing word. **That record was not located by this read**, though FWD-22 was graded REALIZED on the scheduled
  fires (commits 04ff86b965, 0990e8d201).
- **Done, for scale (M).** One-time year of PX_LAST, `price_history_px_last/date=2026-10-02/year_pull.json`: 95 names, 26,081
  values. Segments (88 objects) and officers (93 objects) pulled 2026-10-07 (`research_pulls.py`).

## 5. AMGT price axis: rolling 30-day PX_LAST

- **Surface.** AMGT price ranking, 30/90/365-day trending and breakout (`integrations/bloomberg/research/price_axis_pull.py`;
  90/365 from stored history through `price_series_persist.py`).
- **Size (M).** `price_history_px_last/date=2026-10-07/daily_30d.json`: 94 names, 2,089 points (2026-09-07 to 10-07).
  About 94 of those are new each day; the other ~1,995 are re-asked (E).
- **Pacing.** None; not on the ledger. **Authority:** AMGT_RESAPP FWD-36 (cited in `price_history_pull.py:1-9`).

## 6. Positioning: depth fill for new Opal ETF holdings (MDPF_SECHIST SH-t-1)

- **What "Positioning performance" is.** The Performance toggle on Positioning > ETFS > Holdings Breakdown: 1D, WTD, MTD,
  1M, QTD, 1Q, YTD, 1Y per holding. `data/etfs/scripts/gold/etf_positioning_gold.py` compounds
  DAY_TO_DAY_TOT_RETURN_GROSS_DVDS (`compute_returns` :855) over `bbg/{date}/history_topup.parquet` plus
  `bbg-testpull/tickers/{T}/**/history.csv` (`load_history` :731, `_load_backfill_history` :675). The IRPT
  holdings-performance producer and the `irpt-performance-*` deploys read custody data and make **no** Bloomberg request.
- **Size.**
  - The first run (2026-10-07 data, ad hoc 2026-10-08 12:09Z) planned 15 of 172 securities and recorded 2,929 rows (M,
    ledger line `etf_history_backfill_2026-10-07`) = **5,858 cells**.
  - Each future new holding: ~265 weekdays x 2 fields, about **530 cells** (E; `DEPTH_START_DAYS` 372,
    `etf_daily_pull.py:59-62`). New securities across Opal and rival ETFs ran 39 (10-06), 50 (10-07) and 0 (10-08) a day
    (M, `opal-data-etfs/mdpf/etfs/gold/new_securities/`); not all are Positioning holdings.
  - Waste: 3 securities (2602335D, PFDE, PFOE) return 0 rows and are planned again on every run. That is ~398 rows, ~800
    cells a day (E).
- **Pacing.** The only Positioning pull on the ledger: estimate before any request, record after (`etf_daily_pull.py:560-609`).
  Cap 50 securities a run (`:62`).
- **Authority.** `MDPF_SECHIST_PRD.md:28-35` (FWD-1); `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_160xZ_NEW_SECURITY_LIFECYCLE_AND_HISTORY_BACKFILL.md`;
  deploy ledger `org/critical_paths/.open_deploys/mdpf-sechist-sh-t1-sitez-etf-daily-pull-20261007.json` (L3 open).
- **Done (M), from the ETF history store.**
  - 2026-08-21: 109 tickers, 148,407 rows = 296,814 cells. No authorizing record found; the 08-21 record treats it as done.
  - 2026-08-25: 62 tickers, 17,076 rows = 34,152 cells. No authorizing record found.
  - GLD/VXX 2026-09-15: 2,858 rows = 5,716 cells (`backfill_extra_securities_history.py`; record
    `ANDREW_DIRECT_20260915_030xZ_BBG_ETF_PULL_RETURN_FIELDS_VENDOR_CHANGE_APPROVED.md`).
  - Gap fill 2026-10-06: 57 tickers x 3 days = 342 cells.
  - None of these ran under a budget guard.

## 7. Positioning daily pull (production, for context)

`etf_daily_pull.py` (task OPAL_BBGTML_daily_pull). 2026-10-07 manifest: 172 securities (M). Its draw per day:

- history top-up, 2 fields x 172 = 344 cells;
- characteristics, 14 fields x 172 = 2,408 cells;
- fund daily, 5 fields x 4 = 20 cells.

That is **~2,770 cells a day**. Production spend is neither checked nor recorded on the ledger.

## 8. Other client onboardings (BD, 49 Financial, Inflection)

- **Securities they bring (M unless noted).**
  - Cottonwood: 1,522 CUSIPs held now (`opal-data-assets/blackdiamond/cottonwood/silver/fact_holdings/date=2026-10-07/`);
    4,634 in its transaction history.
  - Inflection: 248 tickers (`opal-data-inf/gold/lots/lots_latest.parquet`).
  - 49 Financial: 811 CUSIPs in account 08335338 (`opal-data-assets/schwab/08335338/silver/fact_uln/date=2026-10-07/`) and
    786 in 08242234 (record).
  - BD: 10,204 CUSIPs and 4,064 tickers (record, `MDPF_SECHIST_R2_INTAKE.md:99`). BD and 49F are the same firm.
- **What is pulled per new client security today.** Classification: nothing from Bloomberg (section 10). History: nothing
  yet. The rule is "from first appearance in the account" (SECHIST C-DEPTH). Equities and funds route to Yahoo; fixed
  income, cash equivalents, annuities and alternatives route to Bloomberg (COTBKF PRD v0.4 Addendum 2).
- **Cells per new security (E).**
  - Bloomberg-routed: ~1,757 days x 1-2 fields = 1,757-3,514. The day count follows each firm's first-trade dates: 49F
    median first appearance 2024, BD 2023-08, so it will not carry over evenly.
  - Yahoo-routed: 0 Bloomberg cells.
- **Per typical onboarding (E).** On Cottonwood's mix (29% of securities Bloomberg-routed), Bloomberg cells are about
  0.29 x new CUSIPs x ~1,757 x fields. For BD's 10,204 CUSIPs that would be ~5.2M-10.4M cells **if** the mix and depth
  matched Cottonwood's. It is unmeasured; BD already holds Yahoo prices in `silver/historical_prices.parquet`.
- **Authority.** No plan and no authorizing record for any firm but Cottonwood.

## 9. IRPT_YCDGEN FWD-14: daily sector and country spread of client-held funds

`org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md:143-148`: "Opal records each day, from Bloomberg, how the funds its
clients hold are spread across sectors and countries". The SOURCE line reads "Andrew's card 2 (approved, not started:
Bloomberg quota)"; the card record itself was not located. **Not sized: no fund list, field or request type is written.**
If it is built as a BQL `holdings()` look-through, each broad index fund costs about what ACWI does (~2,280 rows x 16 = ~36,000
cells per fund-day, E). If it uses fund-level breakdown reference fields, it costs tens of cells per fund-day. **The design
choice decides whether this is a small or a large BQL claimant.**

## 10. Classification on onboarding (MDPF_SECCLASS): no Bloomberg cells

- `data/cot/scripts/gold/E_18.detect_new_securities.py:21-29` (and the BD copy) writes rows and calls no vendor.
- Blanks are filled by an AI classifier (`org/critical_paths/.open_deploys/secclass-e32-ai-leg-i-20261007.json`, 2,291 keys).
- The daily new-security producer (`infra/aws/lambda/mdpf-secclass/new-security-classifier/lambda_function.py`) reuses GICS
  the rivalfunds G4 pull already fetched.
- ETFS_RIVALS PRD v0.16 (`:930-931`) routes "every Rival Funds stock backfilled into the ETFClassifier canonical table" to
  SECCLASS. That is also a classification act with no Bloomberg pull of its own.

## Overlap: the same data pulled more than once

Measured on Bloomberg keys normalized to "TICKER EXCH". Sources: rivalfunds universe (743 keys in window), Positioning
`bbg/2026-10-07/history_topup.parquet` (171), AMGT `year_pull.json` (95).

| Pair | Shared securities (M) | What is pulled twice | Duplicated cells (E) |
|---|---|---|---|
| Positioning and Rival Funds | **81** (e.g. AAPL, AMD, AMZN, ASML, AVGO US) | PX_LAST every day in both daily pulls. FWD-24 will ask a year of PX_LAST for all 81, though Positioning already stores a year or more of PX_LAST and total return for them | ~20,300 one-time (81 x 251); ~81 a day; plus GICS for 81 a day in both reference pulls (~240 a day) |
| AMGT and Rival Funds | **74** | AMGT's year pull already holds 2025-08-28 to 2026-10-02 PX_LAST for them; FWD-24's owed set asks those days again | ~18,600 one-time (74 x ~251); ~74 a day |
| AMGT and Positioning | **24** (V, MA, UNH, LLY, TSM US...) | daily PX_LAST in both | ~24-48 a day; ~6,000 one-time already paid twice |
| All three | 22 | | |
| Overall | 1,009 security-pulls cover **852** distinct securities (M) | 157 securities (16%) are pulled by two or three projects | |

- **Into three separate stores.** The same close lands in rivalfunds `gold/security_market`, Positioning
  `bbg/*/history_topup` + `bbg-testpull/tickers`, and AMGT `harvest/bronze/price_history_px_last`. None reads another's.
  MDPF_SECHIST FWD-3 already describes the single registry ("each place it entered ... the deepest requirement wins",
  `MDPF_SECHIST_PRD.md:43-47`), but FWD-24 and SH-t-1 each keep their own store.
- **Re-asking the same days.** These are the largest avoidable draws found, and none of them is cross-project:
  - AMGT model blocks: ~72,000 unchanged cells a day (95 of 96 objects identical);
  - AMGT 30-day window: ~1,995 of 2,089 points a day re-asked;
  - Positioning: ~800 cells a day for 3 securities Bloomberg cannot price.
  - Together that is about 75,000 cells a day, roughly what one D13 benchmark date costs in BQL.
- **Cottonwood against the others:** not measured. The list is mostly CUSIP-keyed fixed income, so overlap with the equity
  price pulls is likely small.

## What the ledger can and cannot see

The ledger (`%LOCALAPPDATA%\opal_bbg_budget\`, 150,000 ceiling, 30,000 reserve) records rivalfunds holdings (rows
returned), rivalfunds names, rivalfunds market-range / history-owed (points requested), and the Positioning depth fill (rows
returned). It does **not** see:

- AMGT_CORPUS (~74,000 cells a day);
- the AMGT price axis;
- the Positioning production pull;
- the OPAL_BBGTML notebooks.

It counts rows or points, not cells, and BQL capacity is a different Terminal limit from reference and history. One ledger
row is 16 cells for a holdings row, 2 for a Positioning history row, and 1 for a rivalfunds close.

## Not measured

- Bloomberg's actual daily capacity per service, and its unit. Only the BQL floor (~183,000 rows on 2026-10-05) is known.
- The 06:37Z 2026-10-05 D13 draw.
- Launch dates of WCMG, ETFT and PCLG (young fund or hole).
- Price-history need for BD, 49F and Inflection (no census like Cottonwood's exists).
- IRPT_YCDGEN FWD-14's design, fund list and fields.
- The OPAL_BBGTML notebook pulls (model portfolio exposure dashboard).
- Whether ACWI/IWM holdings would ever enter `security_universe`. If they did, FWD-24's owed set would grow by about 4,000
  securities x 251 days, ~1.0M PX_LAST cells (E). The universe code has no benchmark rule either way.
- Cottonwood's overlap with the other three price stores.
- The AMGT_CORPUS standing-word record for the daily re-pull, and the Andrew record for the two 2026-08 Positioning
  backfills.

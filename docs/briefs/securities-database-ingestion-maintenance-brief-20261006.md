# BRIEF -- Opal's internal securities database: ingestion and maintenance

Author 4.0.0_SA_CRO~P, 2026-10-06. Mode: NEW (no project owns this whole).
Order: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_160xZ_NEW_SECURITY_LIFECYCLE_AND_HISTORY_BACKFILL.md`
(verbatim ruling: "this is really how Opal builds its internal securities database and the associated ingestion and
maintenance logic"). Grounding analysis: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_SECURITY_LIFECYCLE_ANALYSIS_20261006.md`.

## PART I -- THE OUTCOME TERRITORY

### CANDIDATE THREAD
One security newly bought by one Opal ETF (DIVZ), on the Positioning page's ETFS view: the morning after the
holding first lands, an Opal analyst opens Holdings Breakdown, sees the security with its class, sector and clean
name, flips to Performance, and reads every window its 1Y history supports -- with no hand-run pull by anyone.
(CSCO and BX, added ~2026-09-18 and still blank past WTD, are the live negative case.)

### O1 -- A new ETF holding is complete the next morning
An Opal analyst reads a newly bought ETF holding on the Positioning page with its classification and all eight
return windows populated from one year of history, without anyone requesting a pull.

### O2 -- A client's security has history for the whole time the client held it
An Investor Reporting reader sees performance for a security in a client account covering the period from its
first appearance in that account forward -- not from the day Opal happened to start tracking it.

### O3 -- Every ingestion point declares how deep history must go
An operator can read, for any security, which ingestion points brought it in (Positioning ETF holdings, a client
account by firm, rival funds, Advisor Intelligence where it pipes through the table) and the history depth each one
requires; the deepest requirement governs. Andrew's two rules are the first entries: Positioning = 1Y; client
account = from first appearance in that account.

### O4 -- An operator can see whether each security's history is complete
For any security an operator reads its stored range, the range its ingestion points require, and any gap, without
re-pulling from Bloomberg.

### O5 -- A gap fills itself and never shows as a wrong number
When a security drops out of the daily pull for some days (as DIVZ/IDVZ constituents did 2026-10-01..05), the next
run fills the missing days; until then a reader sees a blank window, never a return compounded across the gap.

### O6 -- Any held instrument gets exactly one row and one series
A preferred share, a numeric Bloomberg ticker or a CUSIP-only holding (QXO B is the live case) is one security with
one classification row and one history series, and never borrows another security's row or prices.

### O7 -- Daily Bloomberg cost follows what is missing, inside one budget
An operator reads the day's Bloomberg spend for this system against the shared budget: a backfill is paid once per
security, the daily cost is one row per tracked security plus any gap, and a backfill never starves the production
pulls.

### O8 -- Every screen reads one answer for a security
A security's class, sector, clean name and return for a given window are the same on Positioning, Investor
Reporting and Advisor Intelligence, because each reads the same table row and the same stored series.

### O9 -- A vendor null has a declared treatment
A reader sees performance for a money-market fund such as SALXX under one ruled method, instead of the window
silently blanking whenever Bloomberg returns no daily return (it does so on the first trading day of each week).

## PART II -- WHERE THE BOUNDARY SITS

**Owns:** the security lifecycle (detect on ingestion -> fill the row -> backfill to the governing depth ->
day-over-day incremental with gap fill); the depth policy per ingestion point; the one stored history series and its
coverage record; the daily pull plan that asks each security only for what is missing.

**Relies on, does not own:**
- **MDPF_SECCLASS** -- owns the `etf-classifications` table, its schema and classification rules, the FWD-10
  new-security detector for ETF and rival-fund holdings, FWD-7 (rows for securities new in any firm's holdings),
  FWD-12 (sector and industry group onto the table and served to the ETF view), FWD-14 (clean names). This brief
  extends those; it does not re-own them. Whether this becomes an MDPF_SECCLASS extension or its own project is the
  CTO's call at L3.
- **ETFS_POSITIONING** gold and publisher -- consumers of the series and row.
- **Investor Reporting (IRPT_*) and Advisor Intelligence (bd/cot gold, `etf_classifier.py`)** -- consumers.
- **Per-firm holdings producers (bd, cot, inf, 49f)** -- supply the first-appearance evidence; not changed here
  beyond exposing it.
- **ETFS_RIVALS** -- owns `bbg_budget.py` (the quota ledger) and `gold_security_universe` (3-year first/last-seen);
  both reused, not rebuilt.
- **Bloomberg terminal at site Z (0.0.3_BG_BBGTerminal)** -- runs every pull; a new pull leg lands in its daily vehicle.

## PART III -- THE QUALITATIVE BAR

- Nobody runs a hand pull to make a newly held security show performance; today every deep history in the estate
  came from a one-off run.
- A reader never sees a return that silently skipped days; a blank is acceptable, a wrong number is not.
- A held instrument that is not a plain 1-5 letter ticker is a first-class security, not a skipped row.
- The daily Bloomberg spend for history is small enough that it is never the reason a production pull fails.
- One table answers "what is this security" for every screen; `bd-securities` stops being a second answer.

## PART IV -- THE SUBSTRATE (findings, measured 2026-10-06)

1. **Table:** DynamoDB `etf-classifications`, hash key `ticker` (bare, `CUSIP:`, `BBG:<tkr>:<exch>`), 3,507 rows;
   no first-seen, ingestion-point or sector/industry-group field (attribute census over all rows).
2. **ETF/rival detector (live):** `infra/aws/lambda/mdpf-secclass/new-security-classifier/`, 10:00 ET Mon-Fri,
   diffs today vs yesterday, writes rows only, "calls NO vendor" (`lambda_function.py:22`); admits only
   `^[A-Z]{1,5}$` tickers (`:79`), so QXO B never gets a row. 2026-10-06 run: 39 new, 8 written.
3. **Client detectors (not effective):** bd `data/black_diamond/scripts/gold/E_18.detect_new_securities.py` runs
   daily but diffs against `bd-securities`, which `B_01b` fills first (OpenAI), so it finds 0; rows written by it in
   the table: 0 of 3,507. cot has the script, not scheduled, role read-only (`cot-pipeline/iam.tf:366-369`). 49f and
   inf have none; inf `classify_assets.py` writes `bd-securities`.
4. **First appearance is derivable, not recorded:** bd `gold/holdings_lots` `acquisition_date` (back to 1996);
   inf `gold/lots` `buy_date` (from 2019); 49f Schwab `fact_uln/fact_rps` `acquired_date`/`orgpurch_date`
   (back to 2001); cot `fact_holdings` has no acquisition column (10-year backfill ADVI_COTBKF in flight). Lots fully
   closed before the earliest snapshot are not visible.
5. **History today:** ETF pull `integrations/bloomberg/pipeline/etf_daily_pull.py` uses ONE window for all
   securities (`:240-257`); deep history only in frozen `s3://opal-data-etfs/bbg-testpull/tickers/` (3 hand-run
   batches, last 2026-09-14). Client side holds PRICES, not total returns: bd `silver/historical_prices.parquet`
   (yfinance, 3,628 tickers, 2020-), firm `canonical_prices` (cot frozen at 2026-06-09), 49f Schwab closing prices.
   No Investor Reporting code found reading them.
6. **Identity defect:** gold keys Bloomberg rows by the first token of the label (`etf_positioning_gold.py:670`);
   `QXO B US Equity` and `QXO US Equity` both key to `QXO`.
7. **Gap blindness:** gold compounds observations present and does not detect an interior missing day
   (`etf_positioning_gold.py:884-889`); the pull records `vendor_observations` per security but nothing reads it.
8. **Quota:** `data/etfs/scripts/rivalfunds/bbg_budget.py` (150k rows/day, 30k production reserve) is the only
   budget; the ETF pull, price legs and backfills do not use it.
9. **Advisor Intelligence:** reads the table via `data/black_diamond/scripts/gold/lib/etf_classifier.py:87-89`
   (never writes); `opal-partners-data` still reads `bd-securities` (`etf_classifier.py:36`).
10. **Canonical pattern:** the lifecycle fits the estate's medallion shape -- raw vendor rows in bronze, one series
    per security in silver, returns in gold -- and new names must come from `lib/opal_naming.py` (CLAUDE.md rule 30).

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- A ruling on which ingestion points exist and their depth (Andrew gave Positioning and client accounts; rival
  funds' 3-year rule lives in MDPF_SECCLASS FWD-9; Advisor Intelligence pipes through bd/cot).
- A key that holds non-ticker instruments end to end (detector, pull label, gold join).
- A per-security first-appearance date from each firm's holdings (cot depends on ADVI_COTBKF).
- The ETF pull (or a sibling leg) able to request per-security windows; site Z vehicle changes are deploys.
- The budget ledger extended to the ETF and history legs.
- Money-market vendor nulls (SALXX): RULED by Andrew 2026-10-06 ~18:1xZ ("both recs approved") -- derive the
  day's return from Bloomberg's total-return index level; show the window blank until that exists. Unverified:
  whether Bloomberg fills the index level on the days the daily return is null.
- Retirement path for `bd-securities` as a second answer (MDPF_SECCLASS FWD-5).

## PART VI -- STATUS (NOT OUTCOME-BEARING; measured 2026-10-06 ~15:00-17:00Z)

- DIVZ/IDVZ scrape outage 2026-10-01..05 fixed and deployed (@32b8a2717d, 6c7d8b29d6; origin CLOUD 66b1b42a71).
- DIVZ/IDVZ-only constituents have no history rows for 2026-10-01, 10-02, 10-05; from the 2026-10-07 gold run their
  MTD/QTD read as one-day returns unless that gap is pulled (decision pending with Andrew).
- CSCO, BX: 9 history rows each from 2026-09-18, no backfill. SALXX: 6 of 28 daily rows NaN. QXO B: no row, no
  series.

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- Did not measure Bloomberg's cost per historical row against the 150k budget's unit; the budget's unit is rows as
  `bbg_budget.py` counts them.
- Did not verify the inf `classify_assets` schedule, or any cot transaction history.
- Did not check whether Bloomberg returns total return for every client-held instrument type (mutual funds, CDs,
  options, private holdings); some may need a price-only or no-history rule.
- Did not decide whether client-account history should be per security (one series) or per position (holding
  period); Andrew's rule reads as one series starting at the earliest first appearance across accounts -- the PRD
  should confirm.
- The first-appearance date misses lots closed before each firm's earliest snapshot.

## REFS

```
  BRIEF PATH        docs/briefs/securities-database-ingestion-maintenance-brief-20261006.md
  PROJECT           NONE-YET (candidate: MDPF_SECCLASS extension; CTO's call at L3)
  EXISTING PRD      org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md (v0.11; FWD-5, 7, 9, 10, 12, 14 adjacent)
  SIBLING PROJECTS  MDPF_SECCLASS, ETFS_POSITIONING, ETFS_RIVALS, IRPT_*, ADVI_COTBKF
  PRIOR ART         etf-classifications; mdpf-secclass new-security-classifier; bd/cot E_18; etf_daily_pull.py;
                    bbg-testpull backfill; backfill_extra_securities_history.py; bbg_budget.py;
                    gold_security_universe.py; firm lots tables (bd/inf/49f)
  MEASURED AT       2026-10-06 15:00-17:00Z
```

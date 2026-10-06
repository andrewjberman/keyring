# ETF holdings: new-security lifecycle and return history -- analysis and proposed pattern

Author 4.0.0_SA_CRO~P, 2026-10-06. Order: `ANDREW_DIRECT_20261006_160xZ_NEW_SECURITY_LIFECYCLE_AND_HISTORY_BACKFILL.md`
(this folder). Read-only analysis; measured on live S3, DynamoDB and the repo at HEAD 66b1b42a71.

## 1. Conclusion

No component manages a security's lifecycle. Three pieces exist and are not joined:

1. the canonical classification table (DynamoDB `etf-classifications`, 3,507 rows) and a live new-security detector
   that writes rows to it (MDPF_SECCLASS FWD-10);
2. a Bloomberg daily pull whose history leg uses ONE date window for every security;
3. a frozen one-off history backfill (`bbg-testpull/tickers/`, 173 tickers, last written 2026-09-14).

So a security added after the backfill gets forward-only history, and the Positioning ETF view classifies from
Bloomberg's daily file instead of the table. Every symptom in the screenshots follows from that.

## 2. The four symptoms, measured

| Row | Cause | Evidence |
|---|---|---|
| CSCO, BX: 1D/WTD only | Added to holdings ~2026-09-18; not in the backfill; daily pull gives each security only the run's window. Gold blanks a window whose start predates the first observation. | history rows CSCO 9 / BX 9, first 2026-09-18; `bbg-testpull/tickers/{CSCO,BX}/` 0 objects; `etf_positioning_gold.py:911` |
| SALXX: blank past short windows | Bloomberg returns `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` = NaN on the first trading day of each week for this money-market fund (6 of 28 rows: 08-24, 08-31, 09-08, 09-14, 09-21, 09-28). Gold refuses any window containing a NaN. | history_topup census; `etf_positioning_gold.py:915` |
| QXO B: no data, odd name | Key collision. The pull labels it `QXO B US Equity`; gold keys every Bloomberg row by the FIRST TOKEN (`_strip_bbg_security`, `:670`), so it becomes `QXO`, colliding with QXO common, and the holding `QXO B` never matches. The name is the issuer's raw description (gold prefers it, `:1245`). The FWD-10 detector admits only `^[A-Z]{1,5}$` tickers, so `QXO B` never gets a table row either. | history securities under key QXO: `QXO B US Equity`, `QXO US Equity`; detector `:79,:194-201` |
| DIVZ/IDVZ all "Other" (fixed today) | TrueShares scrape broke 10-01; the pull's universe came from the day's file only. Fixed and deployed @32b8a2717d / 6c7d8b29d6. | earlier record, same folder |

**Open hazard from the outage:** DIVZ/IDVZ-only names (VZ, MO, NEE ...) have no history for 2026-10-01, 10-02, 10-05.
Tomorrow's pull window is 10-06 only (`etf_daily_pull.py:240-257`), and gold compounds whatever days exist without
detecting an interior gap (`:884-889`). From 2026-10-07 those rows would show MTD and QTD equal to a one-day return,
and YTD / 1Y short three days -- wrong numbers, not blanks -- until the gap is filled.

## 3. What exists (reuse, do not rebuild)

| Asset | Where | State |
|---|---|---|
| Canonical table | DynamoDB `etf-classifications`, hash key `ticker` (bare, `CUSIP:`, `BBG:<tkr>:<exch>`); client `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` | live; no sector / industry-group field yet (FWD-12 open) |
| New-security detector | `infra/aws/lambda/mdpf-secclass/new-security-classifier/` ; schedule `mdpf-secclass-new-security-daily` 10:00 ET Mon-Fri | live; diffs today vs yesterday holdings; writes rows only; calls no vendor; history explicitly out of scope (`:22`) |
| ETF daily pull | `integrations/bloomberg/pipeline/etf_daily_pull.py`, site Z 07:00 ET | one global top-up window; records `vendor_observations` per security but nothing acts on it |
| Frozen backfill | `s3://opal-data-etfs/bbg-testpull/tickers/{T}/history.csv` | 3 hand-run batches (08-21, 08-25, 09-14); no committed script for the 08-25 batch |
| One-off backfill script | `integrations/bloomberg/pipeline/backfill_extra_securities_history.py` | hand-run, named tickers, refuses overwrite |
| Price axis store | `research/price_axis_pull.py` -> `opal-data-harvest/bloomberg/harvest/bronze/price_history_px_last/` | live; 30-day rolling PX_LAST, a year pull once; separate universe |
| 3-year security universe | `data/etfs/scripts/rivalfunds/gold_security_universe.py` | live; first/last-seen per security -- a ready new-security signal nobody reads for backfill |
| Bloomberg budget | `data/etfs/scripts/rivalfunds/bbg_budget.py` + `bbg_budget.json` (150k rows/day, 30k reserve) | live for rival funds only; the ETF pull and backfills do not use it |
| PRD | `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.11 | FWD-10 history half, FWD-12 (sector to ETF view), FWD-14 (clean names) open |

## 4. Proposed pattern: one security lifecycle, one history store

**Lifecycle per security, keyed by the canonical table's key (not by ticker first-token):**
`DETECTED -> CLASSIFIED -> BACKFILLED -> INCREMENTAL`, with `GAP` as a re-entry state.

1. **Detect** -- the existing FWD-10 detector, widened to admit any held identifier (CUSIP / Bloomberg id), so
   `QXO B`, preferreds and numeric tickers get rows. Output: the day's new keys (already written to
   `mdpf/etfs/gold/new_securities/`).
2. **Classify** -- the row is filled from Bloomberg reference data (sector, industry group, clean name, instrument
   kind) -- FWD-12 / FWD-14. The Positioning gold reads class, sector and name FROM THE TABLE; the Bloomberg daily
   file becomes an input to the table, not to the page.
3. **Backfill** -- a new key with no history gets ONE 1Y pull (`PX_LAST` + total return), charged to the existing
   `bbg_budget` ledger, written once to the history store.
4. **Incremental** -- the daily pull asks each security for `last_observed + 1 .. as_of` instead of one global
   window. A security that dropped out for N days (today's outage) is gap-filled automatically; a current one costs
   one row. Quota is proportional to what is missing.
5. **Recalculate from the store** -- gold computes returns from the stored series only; no re-pull.

**One history store** replaces the frozen `bbg-testpull` CSVs plus 32 daily partitions: per-security series
(`date, PX_LAST, total_return, source, pulled_at`) with a coverage row per security (`first_obs, last_obs,
vendor_count, gaps`). The pull's `vendor_observations` already gives the count Bloomberg returned; storing it makes
an interior gap visible as data rather than invisible arithmetic.

**Three rule fixes the pattern needs:**
- **Identity:** key Bloomberg rows by the query identifier, never the first token of the label (fixes QXO B and
  the QXO / QXO B collision).
- **NaN returns:** where `total_return` is NaN and `PX_LAST` is present on both days, derive the return from price;
  otherwise mark the day `vendor_null` in coverage. Needs a ruling for money-market funds (SALXX price is flat; its
  return is the dividend accrual).
- **Interior gap:** gold blanks a window that contains a recorded gap, instead of compounding across it.

**Cost to state:** the 1Y backfill for today's ~170 constituents is about 170 x 252 = ~43k rows once; daily
incremental is ~170 rows. Both fit inside the existing 150k/day budget beside rival funds.

## 5. Decisions for Andrew

1. **The 10-01..10-05 gap:** run a one-off site-Z gap pull for the DIVZ/IDVZ-only constituents before 09:00 ET
   2026-10-07, or accept wrong MTD / QTD / YTD / 1Y on those rows until the lifecycle work lands.
2. **Home:** extend MDPF_SECCLASS (FWD-10 history half, FWD-12, FWD-14 already cover most of it) or open a separate
   project. Recommendation: extend MDPF_SECCLASS; it owns the table and the detector.
3. **Money-market returns:** the SALXX rule (derive from price, treat as accrual, or show blank).

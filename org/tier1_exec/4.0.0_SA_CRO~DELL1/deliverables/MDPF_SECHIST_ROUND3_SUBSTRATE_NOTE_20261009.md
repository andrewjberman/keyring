# MDPF_SECHIST round 3 -- substrate note on FWD-2, FWD-5, FWD-6 and FWD-9 (CRO, read-only)

- **Author:** `4.0.0_SA_CRO~DELL1`, 2026-10-09 ~04:0x-04:2xZ. **For:** `1.0.0_SA_CTO~DELL1`, as input to the round-2 analysis.
- **Why:** move 3 of unblock proposal `UB-20261009T035455Z-cbf8` (COO `2.0.0_SA_COO~H1`). This note is research. It adds no cell,
  no order and no ruling, and the round-2 decomposition is untouched (CLAUDE.md rule 27).
- **Cost:** zero Bloomberg calls. Reads only: git, S3 `opal-data-etfs`, DynamoDB `etf-classifications` (one full scan).
- **PRD:** `org/missions/D8/MDPF/MDPF_SECHIST/prd/MDPF_SECHIST_PRD.md` (v0.2). Every PRD line cited below was printed from the
  file at this seat's HEAD (box/dell1), not grepped for a quote.

## 0. Findings that change the shape of round 3 (read these first)

1. **The money-market null is a same-day artefact, and a later request returns the value.** In the scheduled daily
   top-ups, SALXX's daily return is null on the first trading day of each week and populated on the other days sampled.
   Requested again later, the same Monday carries a value. If confirmed, ONE mechanism (re-request a day held as null)
   serves both C-GAP (FWD-5) and C-MMF (FWD-9), and the C-MMF level computation may not be needed. C-MMF is ratified text,
   so whether to keep it is the CTO's and Andrew's call, not this note's (section 2).
2. **The top-up window never re-requests a held-null day.** It starts the day after the prior manifest's window end
   (`integrations/bloomberg/pipeline/etf_daily_pull.py:425-441`). A missed run is re-covered; a day returned null is not.
3. **The table carries a key form C-IDENTITY does not list.** `NAME::<label>` is the largest key form today, 5,673 of
   11,361 rows (section 3).
4. **Cottonwood's price-need file and the table use different key forms.** 234 of 4,545 price-need ids match a
   `CUSIP:<id>` table key (section 4). This blocks FWD-2's join for Cottonwood regardless of ADVI_COTBKF's progress.

## 1. C-GAP / FWD-5 -- gaps are blank, never compounded

**Contract.** PRD `:97`: "A window spanning a missing day reads blank; the next run requests the missing days; the gap
record is read before any return is computed." FWD-5 at `:56` ("Missing days fill themselves, and a gap never shows as a
wrong number"). Enrichment item 1 at `:118`. Surface S03 at `:135` ("build", "blank over a gap").

**What exists today (code read 2026-10-09 ~04:1xZ):**
- `compute_returns` (`data/etfs/scripts/gold/etf_positioning_gold.py:855-921`) compounds the observations present and checks
  two endpoints only: an observation on as-of (frontier) and a series start at or before the window start. Its docstring
  states the design: a missing interior day is "deliberately no longer" caught there, and the check "moves to ingest".
- A present-but-null reading disqualifies the whole window (`:913-915`, `sel.isna().any()`). So a null reads blank, which
  is C-GAP-correct. An ABSENT interior day is compounded across, which is the gap C-GAP forbids.
- The pull records `vendor_observations` (rows Bloomberg returned per security) in each run manifest
  (`etf_daily_pull.py:697`). Readers of that field: 0 outside the pull itself (search of `data/`, `integrations/`,
  `infra/`; 1 file holds the name, the writer).
- The history de-dup prefers a populated row over a null one across partitions
  (`etf_positioning_gold.py:819-823`). A later partition that carries a value for a held-null day therefore repairs gold
  with no gold change.
- Prior art for a hand gap fill: `s3://opal-data-etfs/bbg-testpull/tickers/SALXX/gap_20261001_20261005/history.csv`
  (written 2026-10-06 15:25Z, 3 rows, the DIVZ/IDVZ outage days).

**Served artefact (S3, read 2026-10-09 04:07Z):** newest partition `bbg/2026-10-07/` (written 2026-10-08 08:09Z,
`run_class` `adhoc`, `history_window_start`=`end`=2026-10-07). `vendor_observations` holds 172 securities.
`history_topup.csv` holds 3,100 rows over 171 securities, 2025-09-30..2026-10-07, 1 null return (`QXO B US Equity`).

**The gap.** Nothing compares `vendor_observations` with the stored series, and nothing re-requests a missing or null day.
C-GAP has three parts: a gap record, blank over a gap, and next-run re-request. Of these, only "blank over a NULL" exists.

**Candidate cell shape (coarse; the hop, not the decomposition):**
- hop A, ingest: the pull writes a per-security gap record (expected days from the vendor's own count against the stored
  days, plus held-null days) and widens its next request to cover the listed days.
- hop B, gold: `compute_returns` reads the gap record and blanks any window that contains a listed day.
The two hops share the gap record as their only data edge.

**Not measured:** how many securities have an interior absent day today (it needs the stored series per security against
the vendor counts across partitions; this note read four partitions in full and the manifest of one). Whether widening the
request changes the Bloomberg row draw against `bbg_budget.py` (C-BUDGET; the unit question is site Z ruling 31311).

## 2. C-MMF / FWD-9 -- money-market funds

**Contract.** PRD `:96`: "A money-market fund's daily return is computed from its total-return level, not the vendor's
daily-return field (empty on the first trading day of each week, brief O9); a day with neither is blank, never estimated."
FWD-9 at `:83`, DONE WHEN "SALXX read across a week that includes a Monday". Surface S07 at `:139`.

**What exists today:** the pull asks for two history fields only, `PX_LAST` and `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS`
(`etf_daily_pull.py:472`). No total-return level field is requested, so the C-MMF computation has no input today.

**Measured (S3, 2026-10-09 ~04:1xZ), SALXX in the scheduled top-ups, one row per partition:**

| partition | weekday | first trading day of its week | SALXX daily return |
|---|---|---|---|
| 2026-09-08 | Tue | yes (Labor Day Monday) | null |
| 2026-09-14 | Mon | yes | null |
| 2026-09-15 | Tue | no | 0.0093 |
| 2026-09-21 | Mon | yes | null |
| 2026-09-22 | Tue | no | 0.0097 |
| 2026-09-28 | Mon | yes | null |
| 2026-09-29 | Tue | no | 0.0097 |
| 2026-09-30 | Wed | no | 0.0097 |
| 2026-10-06 | Tue | no | 0.0097 |

Denominator: 9 partitions sampled, 4 first-trading-day partitions, 4 of 4 null; 5 other partitions, 0 of 5 null.

**Re-request evidence:** the same days requested later carry values. `bbg-testpull/tickers/SALXX/history.csv` (written
2026-08-25 00:52Z, 273 rows, 2025-07-21..2026-08-24) has 0 null returns, including 58 first-trading-day rows. The 10-06
gap pull returns Monday 2026-10-05 as 0.0097. The gold de-dup comment records 2026-08-24 (a Monday) as null in the
scheduled top-up and 0.0092 in the later test pull (`etf_positioning_gold.py:797-799`).

**The gap.** The served SALXX windows that span a first trading day read blank (null disqualifies the window), which is the
"silently blank" FWD-9 forbids. Under the current window rule (section 0.2), no later run re-requests those days.

**Candidate cell shape:** two admissible routes, both one hop at ingest.
- (a) as ratified: add a total-return level field to the existing history request and compute the money-market daily
  return from it in gold.
- (b) if the CTO and Andrew prefer it: C-GAP's re-request (section 1 hop A) treats a held-null day as missing, and the
  value arrives the next day. FWD-9's "one stated rule" becomes "a null is re-requested next run; until then the window is
  blank". This changes ratified text, so it is a PRD addendum on Andrew's word, not a default.
Either way, the FWD-9 read needs a week with a Monday after the change lands.

**Not measured:** whether the populated-later pattern holds for money-market funds other than SALXX (FXFXX is named in gold
as a control but was not read here). Whether Bloomberg's total-return level field is populated on Mondays for SALXX (it
was never requested, and this note spent no calls). Whether null-then-filled also occurs for non-money-market securities
(the 2 nulls per Monday partition were not attributed beyond SALXX).

## 3. C-IDENTITY / FWD-6 -- one key per instrument

**Contract.** PRD `:98`: "The table's key forms (bare ticker, `CUSIP:`, `BBG:<tkr>:<exch>`) reach the detector, the pull label
and the join; no instrument is keyed by the first token of its label." FWD-6 at `:63` (QXO B the live case). S05 at `:137`
("wire", "MDPF_SECCLASS owns the key"). Enrichment item 3 at `:120`.

**What exists today:**
- Gold still keys Bloomberg rows by the label's first token: `_strip_bbg_security` (`etf_positioning_gold.py:668-672`,
  `str(s).split(" ")[0]`), used for the history join at `:791`. `QXO B US Equity` and `QXO US Equity` both key to `QXO`.
- The ETF/rival detector still admits only `^[A-Z]{1,5}$` (`infra/aws/lambda/mdpf-secclass/new-security-classifier/lambda_function.py:79`,
  last commit 2026-10-07).
- The 2026-10-07 top-up carries `QXO B US Equity` with a null return (the only null in that file).

**Table census (DynamoDB `etf-classifications`, full scan 2026-10-09 04:12Z, 11,361 items, no further page):**

| key form | rows |
|---|---|
| `NAME::<label>` | 5,673 |
| bare `A-Z`, 1-5 characters | 4,463 |
| `BBG:` | 626 |
| `CUSIP:` | 552 |
| other (mixed alphanumerics, underscores) | 31 |
| numeric | 9 |
| share class (`BRK.B`, `BF-B`) | 7 |

The brief measured 3,507 rows on 2026-10-06. QXO has three keys: `QXO`, `NAME::QXO INC COM NEW`,
`NAME::QXO INC 5 50 DEP PFD`. The table has no `cusip` attribute on any row; the CUSIP lives only in the key form.

**The gap.** The contract lists three key forms; the table carries those plus `NAME::` (its largest), numeric and
share-class keys. The detector admits only one form; gold collapses share classes. FWD-6's "own row" is met for QXO's
preferred in the table (`NAME::QXO INC 5 50 DEP PFD`), but no hop carries that key to the pull label or the join.

**Candidate cell shape:** S05 is "wire". hop A: gold's history join keys on the pull's full label (or the table key it
resolves to), never the first token. hop B: the detector admits the table's key forms. The question of which forms are
canonical, and whether `NAME::` is one, belongs to MDPF_SECCLASS (the key's owner) and should be asked before the cell is
cut, because the contract text names three forms.

**Not measured:** which writer mints `NAME::` keys (tests in `data/black_diamond/scripts/classification/tests/` and
`infra/aws/lambda/v2_portal/_shared/tests/` exercise the form). How many held instruments today resolve only to a
`NAME::` key. Whether Bloomberg resolves QXO B's preferred by any identifier in the table.

## 4. S04 / FWD-2 -- first appearance per security per firm

**Contract.** FWD-2 at `:37` ("from the day it first appeared in the client's account"). C-DEPTH at `:94`: client account,
by firm, "from the security's first appearance in that firm's holdings". C-SERIES at `:95`: one series per security from its
earliest first appearance. S04 at `:136` ("build", "cot after ADVI_COTBKF"). Enrichment item 2 at `:119`. The v0.2
addendum (`:161-168`) admits Yahoo for the Yahoo share of ADVI_COTBKF's price-need file and binds C-SERIES and C-GAP to
those rows.

**What exists today:**
- No first-appearance field in the table: 0 of 16 attribute names across 11,361 items mention first, seen, appear, ingest or
  point.
- Derivable sources per firm, as the brief found (IV.4): bd `holdings_lots.acquisition_date`, inf `lots.buy_date`, 49f
  `fact_uln`/`fact_rps` acquired dates. Cottonwood has none until ADVI_COTBKF.
- Nearest built prior art: bd `data/black_diamond/scripts/silver/build_bd_assets_dim.py:127`
  (`first_seen_trade_date`, the minimum trade date per asset, firm-wide, from transactions) and rival funds
  `data/etfs/scripts/rivalfunds/gold_security_universe.py` (`first_seen` per security).
- Cottonwood's need is already a file:
  `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~27/PRICE_NEED_FOR_SECHIST.csv`. Read here: 4,545
  rows, keyed `security_id` (4,544 of them 9-character CUSIP-shaped), sources YAHOO 3,226 and BLOOMBERG_SITE_Z 1,319,
  first dates 2013-04-03..2026-06-10. The 1,319 Bloomberg rows are card A, held by Andrew's named hold (call deae).
- ADVI_COTBKF: `status` active, `dep_stage` EXECUTING, placement DELL2; last change 2026-10-08 (`0699d36bfe`).

**The gap.** First appearance is derivable at three firms and recorded nowhere. Cottonwood's dates exist in the price-need
file, but its ids meet the table in only 234 of 4,545 cases as `CUSIP:<id>`, so the series cannot be joined to the
security row for most of it (C-IDENTITY, section 3).

**Candidate cell shape:** hop A: one first-appearance record per security per firm, derived from each firm's lot or
transaction source, bd reusing `build_bd_assets_dim` logic. hop B: the depth record (S02, C-DEPTH) reads it. Cottonwood
enters hop A from the price-need file once its ids map to table keys. The Yahoo load (v0.2) needs no Andrew word beyond
the addendum's; the Bloomberg 1,319 stay under the hold.

**Not measured:** first-appearance coverage at bd, inf and 49f (no source was read, only cited from the brief). How the
other 4,311 Cottonwood ids map to table keys (a `NAME::` or bare-ticker join was not tried). Whether ADVI_COTBKF's
round-27 file is its final word.

## 5. For the CTO's round-2 analysis, in one place

- **FWD-5 and FWD-9 may be one cell, not two,** if the re-request route (2b) is taken. That needs Andrew's word because
  C-MMF is ratified text. Under route 2a they stay two cells, and the pull gains a field.
- **FWD-6 needs a key ruling from MDPF_SECCLASS before cutting:** whether `NAME::` is a canonical key form.
- **FWD-2's Cottonwood leg is gated twice:** card A's hold (Bloomberg share) and the id join (all shares). The join is
  workable now, read-only, and is not under the hold.
- None of the above depends on round 2's FWD-1 read except the order in which rounds enrich the thread (rule 27).

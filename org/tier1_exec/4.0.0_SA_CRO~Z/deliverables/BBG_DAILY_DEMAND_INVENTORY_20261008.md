# Daily Bloomberg demand on site Z, in cells, by job, with what each feeds

**From:** 4.0.0_SA_CRO~Z. **For:** Andrew, and the backfill demand queue brief
(`docs/briefs/bbg-backfill-demand-queue-brief-20261008.md`).
**Unit (Andrew, 2026-10-08):** a cell is one row x one field. Reference data: securities x fields. History: securities x
fields x dates returned. BQL through Excel: rows x columns returned (the holdings query returns 16).
**Measured:** 2026-10-08, read-only, by a research subagent of this seat (from the job code, the stored outputs on S3 and
the PKL files, the run logs under `C:\Users\Opal Bloomberg\opal_bbg_logs\` and the budget ledger), then spot-checked by
this seat (the schedules below, read from Windows Task Scheduler at ~20:2xZ). No Bloomberg call was made.

## 1. The answer

**About 957,000 cells on a normal day. Two jobs are about 98% of it, and both re-request history that did not change
since the day before.**

| Job | Schedule (box time, ET) | Type | Cells per day | What reads the output | Fields nobody reads (candidates) |
|---|---|---|---|---|---|
| Models PKL notebooks (Yang's `tplus1` notebooks, the first leg of `scheduled_daily_pull.cmd`) | 07:00 daily, task `OPAL_BBGTML_daily_pull` | history 801,704 + reference 558 | **~802,262** (measured from the PKLs) | portal performance, correlation, valuation, macro, positioning and factor pages | `BEST_EPS`, `TRAIL_12M_EPS`, `BEST_LTG_EPS`, `RSI_30D` (~117,000 cells) |
| AMGT_CORPUS induction | 09:00 daily, seven days a week, task `amgt-induction-daily` | history 124,417 + reference 7,296 | **~131,713** (measured from S3) | the research API, scores and dossiers (Security Analysis page) | not checked |
| Rival funds holdings (`collector_bloomberg.py`) | 07:00 leg | BQL via Excel | **11,984** (749 rows x 16 columns) | Rival Funds page | 3 of the 16 columns are dropped before use |
| Rival funds enrichment (`enrichment_bloomberg.py`) | 07:00 leg | reference 6,417, plus up to 5,810 history requested | ~6,400 to 12,300 | Rival Funds gold scripts | none confirmed |
| ETF leg (`etf_daily_pull.py`) | 07:00 leg | reference 2,408 + history 362 | ~2,770, plus top-ups (5,858 on 2026-10-07) | ETF Positioning page | 656 cells: fund-only fields asked of 164 holdings that cannot answer them |
| Price leg | 07:00 leg | history | ~2,000 | AMGT Lead Panel | none |
| Constituents leg (`etf_constituents_pull.py`) | 07:00 leg | reference, including bulk | 164 | **no reader found** | all of this leg's Bloomberg output |
| Connection check | 07:00 leg | reference | 1 | pass or fail only | - |

By request type, roughly: **history ~930,000; reference ~17,000; BQL ~12,000** a day.

## 2. What drives the volume

1. **The models notebooks re-pull full history on every run.** The monthly series reaches back to 1989 and the daily
   series to 2020, every day. An incremental pull would be about 2,000 cells (an estimate). These are Yang's notebooks;
   any change is the owner's call.
2. **AMGT induction re-fetches yearly history since 2016 for 96 names, seven days a week.** 95 of the 96 history objects
   were identical between 2026-10-07 and 2026-10-08. Pulling that history weekly, or only around earnings dates, would
   remove about 124,000 cells a day.
3. **The rest is small.** The ETF leg asks fund-only fields of individual holdings (656 cells a day); the constituents
   leg writes tables nothing reads.

## 3. The channel question

The 2026-10-05 block hit the BQL/Excel channel after about 2.92 million cells
(`BBG_CELL_TRACKING_RECONSTRUCTION_20261005_BLOCK_20261008.md`). The two big daily jobs use the API's reference and history
requests, which kept working through that block. **No limit is documented for either channel**, so the daily ~957,000
cells cannot yet be read against a ceiling. They can be read against each other: the daily BQL draw (~12,000) is about
0.4% of what the BQL channel took before it blocked.

## 4. Today's run

The 07:00 ET run on 2026-10-08 exited 50 (Task Scheduler, measured) and never reached Bloomberg (connection down, per the
run log). The data dated 2026-10-07 on S3 came from manual runs at 12:07Z and 12:09Z. So today's measured volumes come
from stored outputs of earlier runs.

## 5. Not measured

- Whether the models notebooks call Bloomberg on weekends (the trigger fires daily; the data notebook skips its calls
  when the day's PKL already exists).
- Which induction fields anyone reads.
- How many history points the enrichment request actually returned (the ledger records points requested).
- Which script wrote the hourly `probe-capacity` ledger rows of 2026-10-05 and 10-06.
- Other boxes (the laptop, DELL1, DELL2): not covered.

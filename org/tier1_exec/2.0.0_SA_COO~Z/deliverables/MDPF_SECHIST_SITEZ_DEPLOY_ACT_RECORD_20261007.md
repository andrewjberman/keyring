# MDPF_SECHIST SH-t-1 at site Z -- the ledger owner's ACT RECORD (`2.0.0_SA_COO~Z`, 2026-10-07)

Ledger: slug `mdpf-sechist-sh-t1-sitez-etf-daily-pull-20261007`, OPEN, legs L1 L2 L3, opened @e4e17dd7bc on CTO ruling msg 30730.
This file is the owner's durable record beside the ledger entry, because the entry's `.md` is a rendering of its sentinel and a
later `close-leg` may re-render it. **State at this writing (~11:3xZ): NOT MERGED. Nothing run.**

## 1. The condition of the CTO half, measured 2026-10-07 ~09:0xZ (copied from the entry as opened)

`bbg_budget.ledger_dir()` is EQUAL for the ETF leg and the rival-funds collector:
`C:\Users\Opal Bloomberg\AppData\Local\opal_bbg_budget` under the launcher's line 247 environment and under its line 431
environment (one launcher, one cmd process, user `Opal Bloomberg`; `RIVALFUNDS_BBG_BUDGET_DIR` unset at Machine and User scope).
Negative control: with the variable set to `C:\negctl` the function returns `C:\negctl`. Branch (a): the deploy lands, no variable
to set. Limit: measured from this seat's session as the same Windows user, not inside the Task Scheduler's process; the 2026-10-06
scheduled run's collector batch `batch-20261006T110635Z` is a line in that directory's ledger file.

## 2. The ad-hoc QA run dell1 asks for (relay msg 30833; ruling 167, read at `git show 4b1da8e663:org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_MDPF_SECHIST_FWD1_ADHOC_QA_RUN_20261007.md`)

Today's scheduled ETF leg ran on the OLD script and landed at 11:08:13-14Z (this seat's listing, below). So if the merge lands
after it, the ruling asks for ONE ad-hoc run of the leg the same day; the next scheduled pull is the acceptance either way.

**What a hand-run of the leg does, read from the signed bytes (`git show 20a69d5a62:integrations/bloomberg/pipeline/etf_daily_pull.py`):**
- The as-of is `BDay(-1)` of today: `2026-10-06`. It lands under `bbg/2026-10-06/`, the SAME keys the scheduled leg wrote this
  morning. There is no key override and no dry mode that fetches; `plan_only()` is the one read-only entry.
- It re-pulls and OVERWRITES seven objects: `characteristics.{csv,parquet}`, `history_topup.{csv,parquet}`,
  `fund_daily.{csv,parquet}`, `run_manifest.json`. The `constituents/` objects belong to another script and are not touched.
- `RUN_CLASS` defaults to `adhoc` unless `ETF_RUN_CLASS` is set. A hand-run therefore rewrites the day's manifest from
  `run_class: scheduled` (read on the landed manifest today) to `run_class: adhoc`. This seat does NOT set the variable to
  `scheduled` on a hand-run: that would give a manual run production provenance, which the script's own comment (lines 38-45)
  exists to prevent. Readers of the bronze manifest's `run_class`: none found in the three scripts that name the token (the
  Positioning gold and publisher carry their OWN `run_class`, classified from their own event; `home_producer.py` names it as
  a field of another record).
- **`opal-data-etfs` versioning is NOT enabled** (`get-bucket-versioning` returns empty, read 11:2xZ; the COO half says the same).
  An overwrite there keeps no prior bytes.

**The base, listed 11:2xZ (`list-objects-v2`, prefix `bbg/2026-10-06/`, 16 objects, 7 of them this leg's):**

| key | bytes | LastModified |
|---|---|---|
| `characteristics.csv` / `.parquet` | 24,055 / 20,438 | 11:08:13Z / 11:08:14Z |
| `fund_daily.csv` / `.parquet` | 366 / 5,037 | 11:08:14Z |
| `history_topup.csv` / `.parquet` | 6,909 / 6,927 | 11:08:14Z |
| `run_manifest.json` | 4,187 | 11:08:14Z; `run_class scheduled`, window 2026-10-06..2026-10-06, no `history_backfill*` fields |

**Conditions this seat sets on itself for the run (they add to the pair, they change none of it):**
1. **A local byte copy of the seven objects first**, with each object's size and ETag printed. On an unversioned bucket that copy
   is the only rollback source for the scheduled landing. Rollback is a re-put of those bytes at the same keys, never a delete.
2. After the run, `characteristics` and `fund_daily` are compared to the copy (rows and values). They are the same as-of pulled a
   few hours apart and are expected equal; a difference is reported, and the scheduled bytes are restored for those two files
   unless the CTO says the newer pull stands.
3. `history_topup` is expected to GROW (the backfill rows). Its production-window rows are compared to the copy.
4. The budget check is read from the run's own log BEFORE any fetch line, and the day's ledger file is read after for a
   `backfill` line. A refusal is branch B and is reported as such.
5. One run. Not between 10:30Z and 12:00Z. Not while the vehicle or the 07:30 ET check is running.
6. The halt gate: the deploy presents this seat's serial (`org/mcp/sessions/<session>.serial` is written).

**What the run is NOT:** acceptance. FWD-1's acceptance stays the next scheduled pull. Because the hand-run writes the production
keys, the next Positioning gold run WILL read its rows; that is the served move the pair signed ("the first run after the deploy").

## 3. Order of acts once the merge hash arrives

L1 close (the merge commit) -> L2 (working-tree blob reads `0e399c9523f60511107b8491b9894c892a6aeb60`, `py_compile` rc 0) ->
`plan_only()` at site Z (read-only; the plan and the budget inputs) -> the local copy -> the ONE ad-hoc run -> the comparisons ->
report to `0.0.0_AB_MSTR~Z` for dell1 with the entry path. L3 stays OPEN for tomorrow's scheduled run.

---

# 4. THE MERGE LANDED (13:45Z); L1 and L2 CLOSED; NO hand run today (ruled); L3 waits for tomorrow's scheduled pull

Sections 2 and 3 above were written before the ruling below. Their "ONE ad-hoc run" did NOT happen and will not: this section
supersedes them.

## The ruling on the ad-hoc run

This seat put the overwrite to `1.0.0_SA_CTO~Z` before running anything (msg 30967). **Ruling msg 30968: (b), no hand run of the
leg today.** Reasons as ruled: it overwrites today's seven scheduled `bbg/2026-10-06/` objects on an unversioned bucket and turns
`run_class` to adhoc, on keys that feed Positioning and the ETF view under Andrew's no-modify order, and no pair covers that
overwrite; the backfill is paid once per security, so a hand run would spend what tomorrow's acceptance run is meant to exercise;
a local byte copy is a rollback only this seat's process can vouch for. `1.0.0_SA_CTO~DELL1` ACCEPTED (relay msg 30975): its
ruling 167 is superseded for the site-Z act, and MDPF_SECHIST FWD-1 is re-dated to tomorrow's scheduled 07:00 ET pull.

## L1 -- the merge (CLOSED)

`fad25b1527` (parents `b1a8bc190f`, `45899bfc6c`), by `0.0.0_AB_MSTR~Z` at 2026-10-07T13:45:36Z on Andrew's word (@b72e8ae904),
after the 10:30Z-12:00Z exclusion. Read by this seat at 13:52Z: a commit; an ancestor of HEAD; `20a69d5a62` an ancestor of HEAD;
no `.git/MERGE_HEAD`. Pushed: origin CLOUD reads `fad25b1527` by MSTR~Z's ls-remote (msg 30998); its pre-push gate uploaded
nothing.

## L2 -- the working-tree bytes (CLOSED)

| read | value |
|---|---|
| `git hash-object integrations/bloomberg/pipeline/etf_daily_pull.py` (the site-Z working tree) | `0e399c9523f60511107b8491b9894c892a6aeb60` |
| `git rev-parse HEAD:<file>` | the same |
| `git rev-parse 20a69d5a62:<file>` (the signed bytes) | the same |
| `py_compile` under Python 3.11 | rc 0 |

**The deploy is live from 13:45Z:** the scheduled task runs the working tree, so the next run of the leg is the new code.

## `plan_only()` at site Z, read-only (13:52Z, the merged bytes, no fetch, nothing written)

`asof 2026-10-06`, `universe_count 172` (166 constituents + 4 funds + 2 extra securities), `needing_count 15`, `capped []`,
`written []`. The 15: 2602335D, BBY, BE, BX, CSCO, DG, ED, EXPD, GEV, LNVGY, META, MRNA, PFDE, PFOE, PWR, each from 2025-09-29 to
the day before its earliest held row (CSCO and BX to 2026-09-17). That is the same 15 the COO half read on dell1.

Budget inputs at 13:53Z: `daily_ceiling_rows 150000`, `production_reserve_rows 30000`, `spent()` today 755 rows,
`ledger_dir()` `C:\Users\Opal Bloomberg\AppData\Local\opal_bbg_budget`. The request's own bound for the first run is about
15 x 250 = 3,750 rows, far under the 120,000 a backfill may spend. The figure tomorrow is tomorrow's ledger, which starts empty
(one file per UTC day).

## L3 -- OPEN, tomorrow

The first scheduled `OPAL_BBGTML_daily_pull` after the merge: 2026-10-08 07:00 America/New_York (11:00Z).
- **Owed BEFORE it (the CTO half's condition, restated by dell1 in relay 30975):** `ledger_dir()` for the leg and the collector
  re-measured against the MERGED tree and printed here.
- **Owed AFTER it:** the manifest at `bbg/2026-10-07/run_manifest.json` (as-of 2026-10-07): the planned securities with rows
  returned, `history_backfill_error` null, `history_backfill_budget {estimate, limit, spent_before, recorded}`, the leg's exit 0
  in the vehicle log, and a `backfill` line in that day's ledger file. Then L3 closes, or the rollback of the COO half runs.

## A note on the ledger entry's `.md`

`close-leg` re-rendered the entry from its sentinel, and the "PRE-MERGE MEASUREMENT" section this seat appended at the open is no
longer in the file (0 matches at 13:54Z). It stands in section 1 of this record and in git at e4e17dd7bc. The tool said so
itself ("The .md is a RENDERING of the sentinel -- never hand-edit it"); the measurement belongs here, not there.

# 5. L3, THE READ OWED BEFORE THE PULL: `ledger_dir()` RE-MEASURED ON THE MERGED TREE (2026-10-08 ~05:4xZ)

Measured by `2.0.0_SA_COO~Z` in the shared tree at CLOUD HEAD `d99155c49a`, before the 2026-10-08 11:00Z scheduled pull.
`data/etfs/scripts/rivalfunds/bbg_budget.py` was last changed by `3a941ae6c6` (2026-10-07).

- `bbg_budget.ledger_dir()` under the default interpreter (3.14.7) and under the vehicle's interpreter (Python 3.11.9), with
  `RIVALFUNDS_BBG_BUDGET_DIR` unset in the process: `C:\Users\Opal Bloomberg\AppData\Local\opal_bbg_budget` both times. The
  ETF leg and the rival-funds collector import the same module and run as one user under one launcher, so they resolve the same
  directory.
- Negative control: with the variable set to `C:\negctl` the function returns `C:\negctl` (both interpreters).
- The variable at Machine scope and at User scope: empty, both.
- Launchers that set it: 0 occurrences of the name across 0 `.cmd`, `.bat`, `.ps1`, `.sh` and `.xml` files of the repo (one
  content search); the hits of the name read in `.py` files were tests and check scripts.
- That directory today: three ledger files (10-05, 10-06, 10-07). The 10-07 file holds yesterday's scheduled run, written by
  the collector: `{"at": "2026-10-07T11:09:16Z", "mode": "daily", "rows": 749, "batch_id": "batch-20261007T110832Z"}` and a
  `names` line of 6 rows. So the scheduled task's process wrote where this seat's session reads.

**The condition holds on the merged tree: branch (a), no variable to set.** Limit, as in section 1: measured from this seat's
session as the same Windows user, not inside the Task Scheduler's process; yesterday's line is the evidence for that process.

Owed AFTER the pull, unchanged: the manifest at `bbg/2026-10-07/run_manifest.json`, the leg's exit in the vehicle log, and a
`backfill` line in the 2026-10-08 ledger file. Then L3 closes, or the rollback of the COO half runs.

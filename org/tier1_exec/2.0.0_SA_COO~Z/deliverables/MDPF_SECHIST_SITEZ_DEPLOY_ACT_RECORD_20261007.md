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

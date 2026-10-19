# Line-115 prune fix -- dry-run evidence, and the models-leg backfill answer

**author:** 0.0.3_BG_BBGTerminal | **on:** 1.0.0_SA_CTO~Z msg 35953 | **row:** Z-S17 (shape ruled by Z-S20)
**archetype:** VALIDATE
**date:** 2026-10-19 | **deadline the fix is for:** 2026-10-20 11:00Z scheduled run

File under test: `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd`
[file:///C:/Users/Opal%20Bloomberg/Desktop/ajb_workspace/integrations/bloomberg/pipeline/scheduled_daily_pull.cmd](file:///C:/Users/Opal%20Bloomberg/Desktop/ajb_workspace/integrations/bloomberg/pipeline/scheduled_daily_pull.cmd)

## 1. What the fix changes (two executable lines, nothing else)

| line | was | is |
|---|---|---|
| 145 (`:precond_down`, rc 50) | `goto :prune` | `goto :etf_leg` |
| 195 (pull-failed, DAPI UNVERIFIED) | `goto :prune` | `goto :etf_leg` |

Plus `set "PY_AWS=..."` HOISTED to line 49, above the precondition. That hoist is load-bearing and is
not cosmetic: the rc 50 path now enters the landing legs ABOVE the old definition site (line ~164), and
the etf/cons/price legs dereference `%PY_AWS%` with NO guard of their own (lines 289, 340, 401 -- only the
rivalfunds leg at 471 carries `if not defined`). cmd expands an unset variable to the empty string rather
than raising, so without the hoist the three legs would have run `"" -u <script>`, written their own log
lines and landed NOTHING, quietly -- the exact defect 1.0.0_SA_CTO~Z closed on 2026-09-24 (`2e38c030f4`),
arriving through the new door. PY_AWS is now defined exactly ONCE as a definition (line 49), with the
line-471 `if not defined` kept deliberately as a guard, never as the definition.

## 2. The dry-run, and why its substitutions do not touch what is under test

Harness: the REAL bytes of the .cmd, with exactly FOUR **value** lines substituted -- `REPO` (to a stub
tree), `PY` and `PY_AWS` (to a live interpreter), `LOGDIR` (to scratchpad). Every `goto`, every label,
every `if` and every `set RC*` line is byte-identical to the file. Every `%REPO%` use in this file is a
script path (verified: lines 39, 109, 118, 217, 284, 335, 395, 473-474), so redirecting REPO redirects
the leaf work and nothing else -- no control-flow edit was needed to stub the work out.

Forced cma failure = the Smart App Control shape: `bbg_credentials.py` exits 2 (-> `:precond_down`) and
`dapi_check.py` exits 1 (no self-heal) -> `RC=50`.

CONTROL on the harness: `diff <source> <harness>` prints exactly those 4 lines, both arms.
CONTROL on the arms: `diff <prefix_harness> <fix_harness>` prints exactly 2 executable lines, both
`goto :prune` -> `goto :etf_leg`; every other difference is a `REM`.

## 3. Result -- negative control FIRST, as this file's history requires

| leg | pre-fix (git HEAD) | fixed (working tree) |
|---|---|---|
| ETF_LEG | **0** | **1** |
| CONS_LEG | **0** | **1** |
| PRICE_LEG | **0** | **1** |
| cmd exit code | 50 | 50 |

The negative control is what makes the 3/3 mean anything: the harness DID see 4 other stubs fire in the
pre-fix run (BBG_CREDENTIALS, DAPI_CHECK, RIV_COLLECTOR, RIV_ENRICHMENT -- the rivalfunds legs sit after
`:prune` and so ran on the old path), so it could see these three and did not. 0/3 -> 3/3 is the fix.

RC STAYS 50 on both arms, measured, not assumed -- it is the MODELS chain's code and the 07:15 backstop
reads it from `LastTaskResult`. Each leg kept its own rc in its own variable (`RC_ETF=0`, `RC_CONS=0`,
`RC_PRICE=0`) with its own log lines, per READ_HERE section 3 leg isolation.

Logs: scratchpad `dryrun/logs_prefix/` and `dryrun/logs_fix/` (device-local, session-scoped, not durable).

## 4. CTO question 2 -- is the models (PKL) leg backfillable? YES. It is NOT like constituents.

Measured in the notebooks themselves, which are where `date_end` lives (`run_daily_pull.py:5-6`; the
runner's `--date` is explicitly "explicit vintage YYYYMMDD **for the tripwire**", NOT the pull):

| | `market_indices_data_pull.ipynb` | `model_portfolio_regression_analysis.ipynb` |
|---|---|---|
| request | `sids.get_historical(..., start, end)` | `sids.get_historical(..., start, end)` |
| window | `date_start = 1989-12-31` | `date_end + YearEnd(-6)` |
| `date_end` | `today + BDay(-1)` | `today + BDay(-1)` |
| manual override | present, commented: `# date_end = dt.datetime(2026, 6, 18)` | present, commented: `# date_end = datetime(2026, 6, 18)` |
| PKL name | derived from `date_end` | derived from `date_end` |

So a missed models day is RECOVERABLE: set `date_end` to the missed business day in both notebooks and
re-run. The override lever is already in the files, commented, and has been used before (a second
commented instance names 2026-04-03). The PKL filename is a function of `date_end`, so the backfilled
run lands under the correct name, and the cell-16 `if os.path.exists(pkl)` guard does not block a date
whose PKL is absent.

This is STRUCTURALLY OPPOSITE to constituents. Constituents are current-day-only because a
`HistoricalDataRequest` returns ZERO rows for the derived fields while `PX_LAST` returns a full series in
the same call -- a property of the FIELDS (READ_HERE:152, "There is no backfill. Every uncaptured day is
gone permanently"). The models leg IS a historical request over a 36-year window and already returns full
series.

**Therefore: Smart App Control does NOT need to go to Andrew on the grounds of permanent MODELS data
loss, because there is none.** The standing reason to raise it is unchanged and is the constituents leg,
which is current-day-only -- and which this very fix now protects by letting it run when cma is blocked.
Scope note: this answers backfillABILITY of the data. It is not a claim that a backfill has been
exercised; no backfill run was performed for this note.

## 5. What is NOT done here -- the commit

I authored these bytes; I cannot land them. Measured: ZERO commits by my author line on this file across
its whole history, while every prior fix to it was landed by `1.0.0_SA_CTO~Z` (`0f4fd97d17` 2026-09-04
leg isolation -- the first half of THIS fix; `2e38c030f4` 2026-09-24 PY_AWS hoist) or by
`0.0.0_AB_MSTR~Z` (`8d235eadb1`, committed on my behalf and naming me in its subject). My prompt.md
hard line is "no git work at all", and no OWNPATHS lane exists for this seat by design. So the carrier
for this commit is `1.0.0_SA_CTO~Z` or `0.0.0_AB_MSTR~Z`, with the evidence above.

**The edit sits UNCOMMITTED in the shared working tree at `box/sitez`.** That is a live hazard
independent of the fix being right: the 2026-10-20 11:00Z run reads the file ON DISK, so the fix is
ACTIVE for tomorrow's run whether or not it is committed, and any peer's `git checkout` or `safe-merge`
of that path would silently revert it.

# CTO ruling -- the fix route for the Model Portfolios index-benchmark N/A (`1.0.0_SA_CTO~Z`, 2026-10-06 ~13:5xZ)

**Asked:** Andrew-direct via `0.0.0_AB_MSTR~Z`:
- msg 30050, *"check Yang Liu chat ... 4.0.0_SA_CRO~Z to track the source ... 1.0.0_SA_CTO~Z needs to be briefed in parallel"*;
- msg 30058, *"Bloomberg issue is singular priority for the box. until that is fixed no other projects matter"*. CRO~Z traces, and
  this seat rules the fix route.

**Trace:** `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/INDEX_BENCHMARK_NA_TRACE_20261006.md` @bfe10cb2a4 (50 lines, read in full).

## The cause, as traced

**Seven custom CIX index definitions on Bloomberg stopped calculating after 2026-09-29** (quarter end):
- `.UST_BMK .ST_BMK .INT_BMK .LT_BMK .UST_ETF .ST_ETF .LT_ETF`.
- On the same live session, `.INT_ETF`, SPX and every component (I22917US, LBUSTRUU, MXWD, VGSH, AGG, ACWI) price through 2026-10-05.
- **Not our pull, pipeline, Terminal or market data.** The first bad pull is `data_20260930`.

**Two downstream defects make it worse than N/A:**
1. **The populated benchmark cells are wrong and say nothing.** TTW, 1M, 1Q, YTD, 1Y and SI compound the benchmark only through 09-29,
   against a model through 10-05.
2. **The ETF benchmark is also N/A at 1D/WTD/MTD/QTD** for 4 of 5 models. Only INT is current.

Six pulls passed without a flag: the tripwire grades the as-of date, not per-series recency (Z-S5).

## The route, three tracks, in this order

| # | track | who | how | proof |
|---|---|---|---|---|
| 1 | **Stop serving wrong numbers NOW (ours)** | an owner `0.0.0_AB_MSTR~Z` seats for `yang-model-portfolio-benchmarks` (`infra/aws/lambda/v2_portal/yang_pipeline/...`, NOT in the no-modify zone) | **The producer guard:** a benchmark series whose last bar is before `data_as_of` serves **null for EVERY period ending at `data_as_of`**, never a window silently shortened to 09-29. It also adds `benchmark_last_date` per model and series, so the page and any reader can say "benchmark data ends 2026-09-29". The model rows are untouched. Terraform only; the deploy moves served output, so it goes under a never-widen pair (this seat signs the CTO half). | On the current PKL, the 7 stale series serve null on all periods with `benchmark_last_date` 2026-09-29; INT ETF and every model row are unchanged; a plant series ending at `data_as_of` still computes. |
| 2 | **Fix the source (Bloomberg side)** | **the CIX owner at the Terminal.** The definitions read "49F ..."; Yang Liu built the pull; **Andrew names who** | Open each of the 7 in `CIX <GO>` and extend or re-save the definition the way `.INT_ETF` was. **What Q4 definition to use** (keep the Q3 weights, or a new rebalance) **is a methodology call for the benchmark's owner**, not an engineering one. | `bloomberg_historical_data` returns 2026-09-30 onward for all 7. |
| 3 | **Recompute and re-serve** | `0.0.0_AB_MSTR~Z` (the vehicle re-run), then the existing `/data-refresh` channel | The daily pull under Andrew's existing word for OPAL_BBGTML, then `/data-refresh` so the benchmark JSON recomputes. The guard from track 1 then serves numbers again, because the series reach `data_as_of`. | The served JSON shows 0 null benchmark cells at 1D/WTD/MTD/QTD for all 5 models, Index and ETF, with `benchmark_last_date` equal to `data_as_of`. |

**The per-series recency tripwire** (Z-S5) is in `integrations/bloomberg/`, under Andrew's no-modify order. **Track 1's producer guard
covers the served path whether or not the tripwire is fixed.** The tripwire waits on his answer to MSTR~Z's question, whether the
order lifts.

**Not a defect, stated so it is not chased:** Long-Term and Ultra Long-Term benchmark rows are identical **by design**. The source has
no Ultra Long series (`lambda_function.py:102-108`). If that is wrong, it is a methodology question for the benchmark's owner.

**Out of this route:** the sign-in defects (Z-S2/S3/S4) are a separate fix. They caused today's outage, not this N/A. Whether they are
in scope is the question MSTR~Z put to Andrew.

## Acts only Andrew can do (each cited)

1. **Name the CIX owner, and with them the Q4 definition** for the 7 series (track 2). It is a vendor-side write to the firm's
   Bloomberg definitions, and a benchmark-methodology decision.
2. **Whether the `integrations/bloomberg/` no-modify order lifts** for the tripwire fix (Z-S5), and for Z-S1..S4 (his order).

## ADDENDUM 1 (2026-10-06 ~13:5xZ, on 0.0.3_BG_BBGTerminal msg 30089) -- no agent sign-in to raise the Terminal UI

**BG measured:** the Terminal UI is gone (wintrv 0; blp processes 26 -> 4), while bbcomm keeps the entitled session (health ok; CIX still
resolves). `CIX <GO>` is a GUI screen with no DAPI route. It eliminated two discriminators: the "49F" branding (`.INT_ETF` is also
"49F") and SECURITY_TYP (both "Portfolio Index"). It asked whether to spend a sign-in attempt to raise the UI.

**Ruling: no.**
- A Terminal sign-in draws on the lockout budget, and it is Andrew's act.
- DAPI still serves, so tracks (1) and (3) need no UI.
- **Track (2) is a human act at the Terminal:** the owner Andrew names opens and re-saves the 7 in `CIX <GO>`, signing in themselves. A
  human sign-in does not run `bbg_signin.ps1`, so **Z-S2 does not gate this fix.** It gates only an unattended re-save, which this route
  does not use.
- The definition read is diagnostic, and it happens in that same sitting.

## ADDENDUM 2 (2026-10-06 ~14:2xZ) -- Andrew named the owner of tracks (2) and (3)

**Andrew, via 0.0.0_AB_MSTR~Z msg 30098 (record @74897ebc2c), VERBATIM:** *"yang will handle it, hes responsible and will repull."*

- **Track (2):** Yang Liu re-saves the 7 in `CIX <GO>`. The Q4 definition is his methodology call, as the benchmark's owner. No seat
  signs in for him.
- **Track (3):** Yang re-pulls. `0.0.0_AB_MSTR~Z` is no longer its owner.
- **Track (1):** the guard stays with `2.0.0_SA_COO~Z`, after the site-Z reboot (msg 30085, msg 30098). This seat signs its CTO half.
- **Acts only Andrew can do:** item 1 is CLOSED by the quote above. Item 2 (whether the no-modify order lifts) stays open.

**Measured at 14:18Z:**
- The served `json/benchmarks/model_portfolio_benchmarks.json` was last modified 2026-10-06T12:31:21Z: no re-pull has landed yet.
- In this shared tree, `.open_deploys` holds no benchmark entry, so the guard deploy has not started.

### ADDENDUM 3 (2026-10-06 ~17:5xZ) -- Andrew: resolved at the source; the guard STAYS; track 3 is not yet served

**Andrew-direct** (MSTR~Z msg 30159, record `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261006_1744Z_BLOOMBERG_RESOLVED_YANG_CIX_USER_ERROR_SITEZ_RESUMES_REGULAR_WORK.md`
@8555ce7e12): "the Bloomberg issue has since been resolved. It was a user error on behalf of Yang where he did not update the CIX
in bloomberg terminal."

**Ruling on the step-(1) guard: it STAYS.**
- It is live (TO-GUARD-1, closed @98d34b175a, CTO half @78a9e8a39e).
- It turned seven days of silently wrong benchmark numbers into a visible N/A with a date, and it goes quiet by itself once a
  series reaches `data_as_of`. No code change is needed for the fix to show.
- Removing it would re-open the silent-wrong-number class for the next CIX lapse, at the cost of a deploy.

**Measured at ~17:5xZ, so "resolved" is not read as "served":**
- The served `model_portfolio_benchmarks.json` is still the guard's 16:16:52Z re-serve, `data_as_of` 2026-10-05: 273 of 300
  benchmark cells null, `benchmark_last_date` index 2026-09-29 on all 5 models.
- The newest PKL is `benchmarks/data_20261005_v1.pkl` at 12:29:21Z. `uploads/` holds no new PKL.
- So the CIX fix has NOT reached the portal. The panel still reads N/A, correctly.

**What closes track 3:**
- either Yang's same-day re-pull plus `/data-refresh`;
- or the next scheduled daily pull (T-1 = 2026-10-06), which carries the fixed series without any other act.

**Proof:**
- 0 null `index_benchmark`, `etf_benchmark`, `index_spread` and `etf_spread` cells (200 of 200 numbers).
- A volatility cell is null only where its window holds fewer than `calculate_volatility`'s `min_points=5`. This now
  applies to every model's WTD/MTD/QTD, not only INT's, so the null count is graded from the window lengths, not assumed
  to be 3.
- `benchmark_last_date` = `data_as_of` on every model. This seat grades it on the first served write after a new PKL.

### ADDENDUM 4 (2026-10-07 ~00:3xZ) -- track 3 graded on the served key: the INDEX half is FIXED; the ETF half is not

**The served object, read by this seat:** `json/benchmarks/model_portfolio_benchmarks.json`, LastModified 2026-10-07T00:18:28Z,
VersionId `bUr0E3UA...`, `data_as_of` 2026-10-05. It was sent through the gateway by MSTR~Z (msg 30468), and the function running
is the guard's.

| field (50 cells each: 5 models x 10 periods) | numbers | null | read |
|---|---|---|---|
| `model` | 50 | 0 | unchanged |
| `index_benchmark` | **50** | **0** | FIXED (was 0 of 50 after the guard) |
| `index_spread` | 50 | 0 | FIXED |
| `index_benchmark_volatility` | 35 | 15 | The 15 are WTD/MTD/QTD on all 5 models, which is `min_points=5` on windows of 5 trading days or fewer. This is the count ADDENDUM 3's proof said to grade from the window lengths. Not a defect. |
| `etf_benchmark`, `etf_spread` | 10 | 40 | The 40 are UST, ST, LT and ULT on all 10 periods, which is the guard. INT's 10 are numbers. |
| `etf_benchmark_volatility` | 7 | 43 | The 40 above, plus INT's WTD/MTD/QTD (`min_points`). |

`benchmark_last_date`: index 2026-10-05 on all 5 models (equal to `data_as_of`). etf 2026-09-29 on UST, ST, LT and ULT, and
2026-10-05 on INT.

**Grade:**
- **The index benchmark is fixed and proven on the served key.** The four `*_BMK` CIX definitions were re-saved, and the guard
  let them through with no code change, as designed.
- **The ETF benchmark is NOT fixed.** `.UST_ETF`, `.ST_ETF` and `.LT_ETF` still stop at 2026-09-29 (CRO~Z trace `:17-22, :39`; ULT
  reuses the LT pair). The guard serves those four models' ETF cells null with the date, instead of numbers compounded only
  through 09-29. Yang had said the ETF view was not affected; before the guard, those cells showed plausible wrong numbers.
- **What closes it:** Yang re-saves the three ETF definitions, then one more pull and send. Andrew is sending Yang that message
  himself (MSTR~Z msg 30423, record @263e300118). No seat contacts Yang.

**Track 3 stays OPEN on the ETF half.** Its proof is `etf_benchmark` at 50 of 50 numbers, with etf `benchmark_last_date` =
`data_as_of` on all 5 models.

### ADDENDUM 5 (2026-10-07 ~01:3xZ) -- track 3 CLOSED: both halves are fixed on the served key

**The served object, read by this seat:** `json/benchmarks/model_portfolio_benchmarks.json`, LastModified 2026-10-07T01:28:18Z,
VersionId `fxNfvcQ8...`, `data_as_of` 2026-10-05 (the second re-pull, sent by MSTR~Z, msg 30497).

| field (50 cells each) | numbers | null |
|---|---|---|
| `model` | 50 | 0 |
| `index_benchmark`, `index_spread` | 50, 50 | 0, 0 |
| `etf_benchmark`, `etf_spread` | **50, 50** | **0, 0** (was 40 null each) |
| `index_benchmark_volatility`, `etf_benchmark_volatility` | 35, 35 | 15, 15. Every one is WTD/MTD/QTD (`min_points=5` on windows of 5 trading days or fewer) |

`benchmark_last_date` reads index 2026-10-05 and etf 2026-10-05 on all 5 models, equal to `data_as_of`.

**ADDENDUM 3's proof is met on every line.**
- 200 of 200 benchmark and spread cells are numbers.
- The volatility nulls are exactly the short windows.
- Every last date equals `data_as_of`.

**All three tracks are closed:**
- Track 1: the guard is live and stays.
- Track 2: the seven CIX definitions were re-saved by their owner.
- Track 3: re-pulled and served.

The guard went quiet without a code change, as designed. The served panel shows no wrong number and no N/A caused by a
stale series.

### ADDENDUM 6 (2026-10-07 ~06:2xZ) -- the two detection gaps are approved by Andrew; the build is routed

**Andrew-direct ~05:55Z** at the `3.0.0_SA_CVO~Z` terminal (record
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20261007_055xZ_BBG_CHECKER_SERIES_DATE_COMPARE_AND_TRIPWIRE_RECENCY_APPROVED.md`
@1981fd223d): "Yeah we can close gap 1 with the checker compare you described, go with your recs on that matter and gap 2". The
lift of the `integrations/bloomberg/` no-modify order covers THESE TWO EDITS ONLY.

**Routed to `2.0.0_SA_COO~Z`** (the owner seated on this fix route by MSTR~Z msg 30084): ONE issuance of two cells, to the seat
whose lane owns `integrations/bloomberg/pipeline/` (read with `owned-paths-validate`, as for the guard).

1. **Gap 1, the checker** (`integrations/bloomberg/pipeline/freshness_check.py`).
   - After its existing date check, it reads each model's `benchmark_last_date.index` and `.etf` from the served
     `json/benchmarks/model_portfolio_benchmarks.json` and compares each to `data_as_of`.
   - A series behind raises the checker's EXISTING summons, naming the model, the side and the two dates. No new alert,
     schedule or channel is added.
   - A served object with no `benchmark_last_date` reads as a DISTINCT not-measured result. It is never a pass.
   - Proof on real objects, both versions of the served key from 2026-10-06/07:
     - VersionId `Qbef40yV...` (16:16:52Z; index 09-29 on 5 models, etf 09-29 on 4): summons, naming 9 series.
     - VersionId `fxNfvcQ8...` (01:28:18Z; all 10 current): no summons.
     - A planted body with the field removed: the not-measured result.
2. **Gap 2, the tripwire** (row OPAL_BBGTML-Z-S5; the pull-side check in `integrations/bloomberg/`).
   - For every custom CIX series in the data PKL, the last non-null date equals the as-of date (`lib/trading_calendar`). A
     series behind FAILS the tripwire, naming the series and its last date.
   - Proof on real PKLs, the versions of `benchmarks/data_20261005_v1.pkl`:
     - the 2026-10-06 12:29Z pull: FAIL, naming the 7 series at 2026-09-29;
     - the 2026-10-07 01:26Z re-pull: PASS.
   - Control: SPX stays PASS on both.

**Conditions on landing (site-Z Scheduled Tasks run the WORKING TREE, so an edit is live when it touches disk):**
- Both edits are built and proved in a linked worktree. They merge into the shared tree in ONE gap that is NOT between
  10:30Z and 12:00Z (the 07:00 ET vehicle and the 07:30 ET check).
- The merge is the deploy. It is recorded as one NEVER-2 entry, with the first scheduled run after it as its read.
- No other file under `integrations/bloomberg/` is touched. The sign-in rows (Z-S1..Z-S4) and `publish_to_portal.py` stay
  under the order.
- The first live read: the 07:00 ET vehicle's tripwire result and the 07:30 ET checker result on the day after the merge,
  both PASS on current data. A FAIL on current data means revert the merge the same hour.

## ADDENDUM 7 (2026-10-07 ~10:1xZ) -- gap 2 is open on a hand-run send (COO~Z msg 30768, row OPAL_BBGTML-Z-S12 @c405c95512)

**Read:** TO-GUARD-3 merged @80bcd69f78; GUARD-3A and GUARD-3B PASS from the merged tree (COO~Z's re-run). `publish_to_portal.py:62-64`
runs the TZERO copy of the tripwire, which GUARD-3 was told not to touch and which lacks the per-series CIX recency check. So the
check holds on the scheduled vehicle and not on a publisher run by hand. The row reads INERT: all 13 custom CIX series reach the
as-of on the served vintage.

**Ruling: the smallest route. Port the same limb into `tzero/tools/bbg_pkl_tripwire.py`, and nothing else.**
- One cell, cut now by `2.0.0_SA_COO~Z`, built in a worktree: the limb byte-for-byte as GUARD-3b landed it in the tplus1 copy, plus
  the same proof with its negative control (a frozen series FAILS; a current one passes).
- Not the other routes: re-pointing the publisher at the tplus1 copy changes which instrument guards the send, and making the two
  copies one file is a refactor of a pipeline under his order. Both are larger edits to protected files for the same outcome.
- **The merge is the deploy and it WAITS on Andrew's word.** His lift (@1981fd223d) covers the two detection edits only, and this is
  a third file under `integrations/bloomberg/`. The branch sits unmerged until he names it.
- Never merged between 10:30Z and 12:00Z (ADDENDUM 6's window stands).

**Until it lands (binds by reading):** nobody runs `publish_to_portal.py` by hand without first running the tplus1 tripwire on the
same files and reading its exit code. The scheduled vehicle already does this.

**Act only Andrew can do:** lift his no-modify order for this one file. Citation: his order as recorded in
`ANDREW_DIRECT_20261006_201xZ_BLOOMBERG_NO_MODIFY_IS_POSITIONING_AND_ETFS_VIEW_RESEARCH_OUTSIDE_OPEN_SEASON.md`, and the scope of
his lift in `ANDREW_DIRECT_20261007_054xZ_ALL_RECS_APPROVED_CTOZ_THREE_CARRIED_CARDS.md`.

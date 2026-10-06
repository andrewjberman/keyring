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

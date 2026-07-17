# Session Log -- 0.2.0_DT_PortfolioAnalytics -- 2026-07-17 ~1249-1320Z
**Archetype:** P0 incident triage + rectification verification (Andrew-direct sovereign instantiation)
**Project:** P0 Short Term Benchmark corruption (portal Model Portfolios / Benchmark tab)

## What happened
- Instantiated by MSTR under Andrew-direct sovereign authority: ST Benchmark YTD/1Y wrong on portal,
  ST model vol reading 20%+; suspect = Alyssa's 07-15 Data Refresh upload. CTO working in parallel
  (peer, per Andrew's correction of the "sole taskholder" misread -- sole FOCUS, not exclusive ownership).

## Findings (artifact-grounded; converged independently with CTO)
- ROOT CAUSE (source-confirmed at the PKL artifacts): the 07-15 `data.pkl` 'Short Term' series
  (bbg_ticker `.ST Index`) is a WRONG-SECURITY SUBSTITUTION -- 1438 rows spanning 2021-01-04..2026-07-15,
  price ~1.75-2.43, daily ret std ~1.5 (equity-like; CTO fingerprint: corr -0.72 MSCI Japan / +0.61 SPX)
  replacing the true base-100 model NAV (661 rows from 2023-12-29, std 0.13). 657/657 overlapping-date
  returns changed = full-history replacement, not an append or scaling error.
- SPAN DISCRIMINATOR (mine): of all 13 Term series, ONLY `.ST Index` changed span/content between
  vintages; repo ticker map unchanged (Yang notebook `'Short Term': '.ST Index'`). Defect is at the
  Bloomberg CIX resolution layer, upstream of workbook/pipeline. `.ST` is also the Stockholm suffix.
- model_20260716_v1.pkl model_returns ST HEALTHY (YTD ann vol 3.4%) -- corruption confined to data_pkl.
- Lambda + Step Functions pipeline behaved correctly on corrupt input; no code defect our side.

## Rectification state (verified by me, read-side)
- Andrew HIMSELF executed the portal rollback UI at 12:55:45Z (re-upload of 07-10 vintage, exec
  e14770af-b842-4171-b543-2df82f7c04a0). No agent wrote to the served surface at any point.
- Verified at origin: all three benchmark JSONs regenerated 12:57:54Z, data_as_of 2026-07-10, ST
  YTD 1.72/vol 3.32, 1Y 3.73/vol 2.58, SI 4.64 (healthy). CF invalidations completed 12:57-12:59Z
  on EVTSA9VEHNZVH. Portal serves correct honest-stale data.
- Attribution wrinkle: rollback control succeeded SILENTLY (no operator feedback) -- Andrew thought an
  agent had done it. Logged as a UX defect (below).

## Deliverable landed
- `deliverables/opal_bbgtml/validate_data_pkl.py` @ 2d62804b6 (pushed): pre-publication acceptance gate --
  row-count parity, span-start match, per-sleeve magnitude ceilings (calibrated 1.5x healthy-history max
  after the positive control caught my first-cut ceilings false-alarming on the 2025-04-09 shock day),
  overlap-continuity vs prior vintage. EXERCISED both ways: corrupt 0716 pkl = FAIL (4 findings),
  healthy 0712 pkl = PASS. Exit-code gated. This is the acceptance test on the corrected re-upload,
  run BEFORE the pipeline fires (Andrew's sequence via CTO).

## Residual / next
- [Andrew/Alyssa, physical] Fix `.ST` CIX on the Bloomberg terminal (expect base-100 NAV, last good
  ~112.93 @ 07-10); re-run tools\run_daily_pull.bat; I validate the pkl (PASS required) -> Data Refresh
  upload -> I verify served + CF. Terminal instruction sent to Andrew (CTO CC'd, 131752Z).
- [me, normal gates] Guard-work TO: fold validate checks into the pipeline (refuse-to-publish) + fix the
  silent-rollback UX defect (frontend wiring to existing /api/scoped/data-refresh/status/{id}).
- [me, carried] COO 07-16 item 2: add machine-readable Status markers to the two closed bbgtml deploy ledgers.

## Compiler tools
comp-grep (pull-script + .ST references, portal consumer, refresh-table discovery), comp-routes
(origins/behaviors -- found the benchmark JSON serving path + AUTH edge; `trace` under MSYS_NO_PATHCONV
mangles its internal python path, avoid). comp-freshness not needed: vintage question was settled at
versioned S3 directly.

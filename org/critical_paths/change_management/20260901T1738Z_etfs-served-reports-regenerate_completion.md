# ETFS served monthly reports REGENERATED (2026-07 + 2026-08) -- opened and closed in-session

**Actor:** `4.0.0_SA_CRO` · **Date:** 2026-09-01 17:38Z · **Class:** SERVED-OUTPUT OVERWRITE (in place)
**Authorization:** Andrew-direct, verbatim: *"ok regenerate the renders"* -- assent to the standing ask this
seat had surfaced twice and deliberately not self-authorized (the served copies carried a materially false
August chart).

## What was overwritten

`s3://opal-data-etfs/platinum/reports/{2026-07,2026-08}/` -- 10 objects (HTML + PDF + 3 per-partner CSVs
per month). Prior vintages: 2026-07 @ 2026-08-01T14:00:56Z, 2026-08 @ 2026-09-01T14:02:21Z.
New vintage: 2026-09-01T17:38:05Z / T17:38:41Z.

⛔ **THIS IS AN IN-PLACE CONTENT OVERWRITE OF SERVED OUTPUT.** Path unchanged, nothing relocated, nothing
widened. Sovereign-authorized; recorded here because the NEVER#1-adjacent bar is served-output movement and
this is the closest neighbouring act.

## Why the served copies were wrong

1. **Coverage.** 5 cottonwood August daily slices had never been produced (backfilled earlier this session,
   record `20260901T1650Z_etfs-cottonwood-august-slice-backfill_completion.md`), and 10 July slices landed
   4h10m AFTER the July report rendered and were never picked up.
2. **Matrix display.** Weekends rendered blank for business-day-delivered partners, and the column set was
   the union of partner dates so July showed 25 of 31 calendar days. Fixed @`1715af512d`.
3. **Chart.** The August per-ETF PERIOD chart plotted a FALSE **+$207.9M** DIVZ month against a true
   **+$9.6M** -- August opens on a Saturday and the chart carry lacked the month-boundary seed, so the
   all-client total was inflection ALONE on 08-01/02. Fixed @`9ea991b080`.

## How it was regenerated

`render_month_end.py --month {M} --out {local} --pdf --s3-out s3://opal-data-etfs/platinum/reports`

⚠ **NO EMAIL WAS SENT.** The month-end SES send lives in the `etfs-reports-orchestrator` Lambda, NOT in this
script. Andrew asked to regenerate the RENDERS; re-sending the monthly email is a separate act and was NOT
performed. **The recipient has not been told these numbers moved** -- surfaced, not self-authorized.

## Verification -- read from the SERVED artifact, re-downloaded from S3

| | 2026-07 | 2026-08 |
|---|---|---|
| daily matrix | 31 cols, 0 blank cells | 31 cols, 0 blank cells |
| per-ETF PERIOD y-floor | $75M | **$84M** (was $7M) |
| per-ETF PERIOD legend | DIVZ +28.2M | **DIVZ +9.6M** (was +207.9M) |
| DIVZ day-1 plotted vs truth | $189.0M vs $188.9M OK | **$216.7M vs $217.0M OK** |

All 10 served objects byte-match the uploaded bytes. **Desktop pack and served copies are now BYTE-IDENTICAL**
-- one source of truth, no divergence left behind.

## Figures that moved on the served artifact

| month | partner | was served | now served |
|---|---|---|---|
| 2026-07 | cottonwood | 31,186,887.06 | 31,242,755.15 |
| 2026-07 | inflection | 46,695,709.41 | 47,137,193.79 |
| 2026-08 | cottonwood | 52,488,748.61 | 52,492,649.45 |
| 2026-07/08 | **49financial** | unchanged | unchanged (control) |
| 2026-08 | **inflection** | unchanged | unchanged (control) |

## ⛔ PROVENANCE GAP, STATED RATHER THAN HIDDEN

The producing commits `1715af512d` + `9ea991b080` were **LOCAL, NOT ON ORIGIN** at upload time. `git push`
is INTEGRATOR-ONLY on the shared `CLOUD` branch (LD-0367/LD-0368 gate fired; only `0.0.0_AB_MSTR` may push)
and **the gate was NOT overridden**. So the served bytes are currently produced by code that exists only on
this device, pending the hourly integration window.

**Bounded and self-closing:** the commits are real and the window publishes them. **If the integration
window does not carry them, this gap does not close on its own** -- re-check that `9ea991b080` is an
ancestor of `origin/CLOUD` before treating the served artifact's provenance as reproducible.

The alternative was leaving a materially false chart served for another hour. That trade was taken
deliberately.

**STATUS: CLOSED.** Opened and closed in-session per NEVER#2.

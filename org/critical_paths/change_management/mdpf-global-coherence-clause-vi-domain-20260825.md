# DEPLOY-COMPLETION LEDGER -- MDPF global, clause (vi) domain precondition

**Status:** OPEN
**Opened:** 2026-08-25T18:48:54Z by `0.4.0_DS_ClientPlatform~N`
**Closes when:** served `platinum/mdpf/global/aggregate-aua-timeseries.json` reads
`as_of_last = 2026-08-24` **and** `_provenance.source_keys` names the `2026-08-24` gold partition.
⛔ **NOT on object mtime, NOT on byte size, NOT on `_provenance.written_at`** -- that field advances
daily at fixed width over frozen content and produces a clean green on a dark product (measured;
`2.0.0_SA_COO` 70998). Key on `source_keys` / `as_of_last`.

## Why this entry exists
NEVER#6: a begun deploy FINISHES in-session or rolls back + escalates loud to COO. `2.0.0_SA_COO`
(71149) stated the obligation explicitly: *"NEVER#6 stays open until global reads
`as_of_last=2026-08-24` with `source_keys` advanced."*

## What is being deployed
`data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` -- a DOMAIN PRECONDITION on the
cross-axis coherence gate's clause (vi): the triple `tot[i-1], tot[i], tot[i+1]` is compared only
where the SAME LEGS contribute a roster at all three dates.

- Commit: **`1234c8779e`** (author `0.4.0_DS_ClientPlatform~N`), **LOCAL on CLOUD, NOT PUSHED**
- Also committed: `data/mdpf/scripts/gold/tests/test_cross_axis_membership_domain.py` (5 arms)
- Authorization: `2.0.0_SA_COO` 71118 (remedy (C) over (B)); `1.0.0_SA_CTO` 71117 raised no
  architectural objection; 71149 confirms owner + status.

## The defect being repaired
global has not emitted since **2026-08-20T13:31:05Z** -- 5 client-facing days dark. The gate
refused on `(vi) FOREIGN-DAY ROSTER: 1`, `2026-08-19: 7791 -> 8260 -> 7791`. **There was no
foreign-day roster.** Cottonwood contributes a roster on 18 of 461 dates and 2026-08-19 is the ONE
date whose neighbours BOTH lack it; its own measured +469 entered and left beside its own measured
values. Arithmetic: 49F core 7144 + inflection 562 + 49F SMA carry 85 = 7791; +469 = 8260.

⛔ **The standing prohibition was never crossed:** the gate is not weakened, bypassed or `--force`d,
and no 2026-08-19 data was touched. Fixing a clause's DOMAIN is not relaxing it -- verified by a
four-arm control set in which the proposed clause still refuses a planted foreign-day roster
(`+66` on 2026-07-06, the exact case clause (vi) was built from).

## Deploy path and its ORDER PROBLEM (open question, surfaced not assumed)
Deployed target: `s3://opal-data-mdpf/code/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`
Measured 2026-08-25T18:4xZ (`comp-pipescript deployed --pipeline mdpf`):
```
STALE   local 952bbc16ea07ed14cf51a497f1b4cde5   s3 2b59630a8419193b02851dcaea207cdc
```
The s3 md5 equals the file's PRE-patch md5, so the deployed copy is a clean unmodified baseline.

⚠ **Rule 13's order is commit -> push -> S3 cp -> verify, and PUSH IS INTEGRATOR-ONLY**
(`.tools/hooks/never-rules-gate.sh:511`). `safe-deploy.sh` is the pre-push hook, so the sanctioned
deploy rides the integrator's push. Deploying before the push would put running code AHEAD OF
ORIGIN -- a provenance gap. **There is runway to avoid that:** see the clock below.

## The clock -- deploying tonight does NOT un-dark the client tonight
Measured on both trigger planes (`aws scheduler get-schedule`, UTC):
```
12:52Z  mdpf-feeder-backstop-daily        -> mdpf-feeder-trigger
13:30Z  mdpf-scheduled-floor              -> mdpf-gold-lambda        <- runs the patched script
13:40Z  mdpf-accrual-bridge-daily         -> mdpf-accrual-trigger
13:50Z  opal-assets-mdpf-portal-publisher -> platinum publish
```
Next gold execution: **2026-08-26T13:30Z**, ~18.7h after this entry was opened. Global republishes
on that run's artifact, platinum at 13:50Z. **No ad-hoc run is proposed:** an ad-hoc run is a QA
instrument and never production evidence (CLAUDE.md NEVER), and this repair's acceptance is the
scheduled run's own artifact.

⚠ Also noted, NOT acted on: `mdpf-feeder-accelerator` carries `ScheduleExpression: None` (EventBridge
rules plane) -- the known event-only-trigger condition. It is not on this repair's path and is not
this entry's subject.

## Steps
| # | Step | State |
|---|---|---|
| 1 | Fix committed + control set committed | **DONE** `1234c8779e` (local) |
| 2 | `commit-gate` / ruff / py_compile clean | **DONE** |
| 3 | 4 arms re-run against the REAL patched implementation | **DONE** A/B/C/D as predicted |
| 4 | Integrator pushes `1234c8779e` to `origin/CLOUD` | **PENDING** -- integrator-only |
| 5 | S3 code sync (rides the push hook, else explicit `safe-deploy.sh`) | **PENDING** |
| 6 | `comp-pipescript deployed --pipeline mdpf` reads MATCH | **PENDING** |
| 7 | 2026-08-26T13:30Z scheduled run passes the gate | **PENDING** |
| 8 | Served global `as_of_last=2026-08-24` + `source_keys` advanced | **PENDING** -- closes this |
| 9 | `49financial` + `inflection` unmoved on data-bearing fields (`written_at` may differ) | **PENDING** |

## Rollback
Revert `1234c8779e` and re-sync. The prior deployed object is a clean baseline at md5
`2b59630a8419193b02851dcaea207cdc`; `opal-data-assets` / `opal-data-mdpf` are versioned, so the
prior code object is recoverable by version rather than by rebuild. Rolling back restores the
refusal -- it does NOT restore global's publishing, because the island is permanent (value dates
2026-08-18, 08-20 and 08-21 were never delivered by the vendor and never will be).

## Escalation
If step 7 or 8 fails, this does NOT get quietly retried: loud to `2.0.0_SA_COO` per NEVER#6, with
the run's own gate output.

-- `0.4.0_DS_ClientPlatform~N`

# Investigation — Inflection AUM divergence: Model Portfolios vs Advisor Intelligence
**archetype:** DIAGNOSE
**Author:** 3.0.0_SA_CVO
**Date:** 2026-06-08 ~14:00Z
**Trigger:** Andrew-direct sovereign. Inflection shows $206m on Model Portfolios (ts 6/8) vs $203m on
Advisor Intelligence (ts 6/7); Orion truth today = $202.73m. Andrew asked: ingestion schedules, where
is the staleness (our side vs vendor), the logic, and is Eclipse lag involved.

## Verdict
**Pure ingestion-cadence mismatch on OUR side. Not Eclipse lag, not a vendor problem, not an
Eclipse-vs-Orion methodology split.** Both pages read the SAME canonical spine; MDPF samples it a day
too early on a weekday-only clock and never re-samples. Self-heals at today's 15:00Z MDPF run.

## Ground-truth chain (all verified live this session)
1. **Single source (F1):** Inflection `partner_custody_total` on BOTH pages is sourced from
   `s3://opal-data-inf/gold/timeseries/client_performance.parquet` — the transaction-history daily-AUA
   spine. Per Andrew's MDPF_SCOPED.F1 ruling, MDPF was deliberately moved OFF the Eclipse-administered-
   book sum ONTO this spine ("the ~$1.5M Eclipse-vs-spine gap is resolved by sourcing from the single
   canonical spine"). Code: `build_mdpf_wsc_inflection_feeder.py:69-74,335-361` (`load_client_performance_total`,
   "rolls forward to the latest spine date on-or-before as_of").
2. **Spine values (read from the parquet):** 6/05 $206.08m → 6/06 $202.73m (−$3.35m) → 6/07 $202.73m (flat).
3. **The −$3.35m Saturday move = pure epsilon (reconciliation):** net_nna 0, return_$ 0, daily_in/outflow 0,
   epsilon −3.354m, broad-based across ~all households. NOT a withdrawal, NOT market. = the prior-trading-day
   (Fri 6/05) RECONCILED close posting T+1 on Saturday (Andrew's read, confirmed). The 6/05 $206.08m was a
   same-day MODEL ESTIMATE (return-model −3.49m + epsilon plug +4.23m); the reconciled actual ($202.73m)
   arrived Saturday.
4. **The two cadences:**
   - Spine + ADVI: DAILY incl weekends. Last spine build 6/07 10:13 UTC (sentinel
     `gold/meta/pipeline-complete.json` 10:21 UTC) = ADVI's "6/7 10am". Carries the reconciled $202.73m.
   - MDPF rollup: `cron(0 15 ? * MON-FRI *)` (`infra/aws/terraform/mdpf-pipeline`), EventBridge →
     `mdpf-daily-trigger` Lambda → starts mdpf-daily-runner EC2. Last ran Fri 6/05 15:00Z → captured the
     spine's same-day estimate ($206.08m). Weekend-excluded + today's 15:00Z pending (was ~14:00Z) → frozen
     on Friday's value.
5. **Staleness is OUR side:** Eclipse vendor data has landed through 6/07 (`bronze/silver/gold/eclipse/2026-06-06`
   + `-07` all present); the spine consumed it. The only stale thing is the MDPF weekday-only rollup.
6. **Eclipse role:** Inflection IS Eclipse/Fidelity-custodied + Eclipse feeds the per-MODEL decomposition, but
   the AUM TOTAL is the shared spine (F1), not Eclipse. Eclipse drives the value-movement indirectly via the
   spine's epsilon reconciliation term, not as a separate page-source.

## Timestamp inversion
ADVI "6/7 10am" = honest (spine build time). Model Portfolios "6/8" = misleading: AUM value is Friday's
($206m, weekday-only aggregate) but the page shows today's date — likely mixing a daily-fresh artifact's
timestamp (`account-distribution.json`, fresh 6/08 07:30) with the weekday-only aggregate's value. (FE-confirm.)

## Andrew directive + routing
**Andrew-sovereign:** "sync those timelines in the case of Inflection — if the earlier of the two is 10a then
both have to be 10a." Translated to spec + routed:
- **CTO (140936Z):** trigger design — ROBUST = EventBridge on the INF spine sentinel `gold/meta/pipeline-complete.json`
  → mdpf-daily-trigger (runs right after spine fresh, daily, no clock-race); SIMPLE = daily incl-weekend cron after
  spine completion. CROSS-FIRM call: the rollup serves 49F/Global too (not Eclipse) — can't naively trigger off
  INF-only. + declared-vs-live drift on the INF spine cron (TF ~12:43 UTC vs live 10:21 UTC) to resolve.
- **AE:** implement the chosen `mdpf-daily-trigger` schedule_expression via Terraform/safe-apply.
- **COO (140947Z):** drive/sequence.
- **DE (separate, smaller):** FE timestamp should stamp the spine-as-of date rolled-forward-to, not the render date.

## Self-heal note
Today's MDPF 15:00Z run re-samples the spine, rolls forward to the latest date (6/07 = $202.73m), and Model
Portfolios converges to ~$203m = ADVI. The value needs no manual fix; the cadence change is the durable fix.

— 3.0.0_SA_CVO

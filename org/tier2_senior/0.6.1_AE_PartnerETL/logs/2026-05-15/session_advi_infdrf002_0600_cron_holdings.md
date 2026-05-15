# Session Log — ADVI_INFDRF.002: 06:00 Cron Holdings Under-Build
**Agent:** 0.6.1_AE_PartnerETL
**Date:** 2026-05-15
**TO:** ADVI_INFDRF.002 (Andrew-flagged URGENT, COO-routed)

## Summary

Root-caused the Inflection portal holdings under-build. NOT a chain-mode bug
(DS~A's "CHAIN_INCREMENTAL omits INF_B_00" hypothesis disproven). It is a cron
TIMING bug: the gold chain fires 06:00 UTC, ~6h before its bronze input lands.

## AC1 — Root Cause

Evidence: 2026-05-15 06:00 vs 17:57 full-chain logs (both `--chain full`, both COMPLETE):
- `chain_full_20260515_060048.log` — the 06:00 cron ran FULL; INF_B_00 ran in it.
- INF_B_00.canonical_holdings.py:218-264 reconciles positions_mv against
  `bronze/orion-api/{date}/assets.csv` (BRONZE_ASSETS_PREFIX). Absent -> "pmv-only
  fallback" -> short holdings.
- 06:00 INF_B_00 [2026-05-15]: "bronze assets.csv absent" -> 11,413 rows / 801 acct / $204.6M.
- 17:57 INF_B_00 [2026-05-15]: "bronze assets: 29,552 rows" -> reconciled ->
  29,552 / 865 / $203,845,242.41 (== canonical header total.aua).

Timing: `bronze/orion-api/{date}/assets.csv` written by `opal-inf-bronze-runner-cron`
(EventBridge cron(43 12) = 12:43 UTC -> inf-bronze-trigger). CSV lands ~12:54 UTC
(05-15 12:54Z, 05-14 12:51Z). Gold chain `inf-canonical-prices-daily` fires 06:00 UTC;
INF_B_00 runs ~06:44 UTC — ~6h before assets.csv exists. Pmv-only fallback every day.

Compounding: eventbridge.tf:100-118 documents the 06:00 cron as "FALLBACK ONLY —
primary is event-driven via silver-aggregator." The primary path (aggregator ->
inf-gold-trigger ~13:00, after bronze) is BROKEN — today's aggregator chain
dispatched `--chain full --run-date 2026-05-14` and failed at INF_API_SILVER_REPS
on the `--run-date` catalog bug (pull entries lack {date} token). So the mis-timed
fallback runs + the primary that would correct it is dead -> portal stuck short.

## AC2 — Fix Spec

`infra/aws/terraform/inf-pipeline/eventbridge.tf:111` — `inf_canonical_prices_daily`
schedule `cron(0 6 * * ? *)` -> `cron(0 14 * * ? *)` (06:00 -> 14:00 UTC). 14:00
clears the legacy bronze window (assets 12:54Z, performance_dim ~13:41Z) + margin.
Rule stays a time-based fallback; now produces CORRECT holdings when it fires.

Coordination: the 06:00 cron is ADVI_INFETL's; AE 0.7.0 is the infra owner. MCP'd
0.7.0 — option (a) they apply, or (b) I apply with their concurrence. Awaiting reply.

## Cross-Reference
The `--run-date` catalog bug (primary aggregator path failure) — separate, surfaced
to COO earlier today; recommend its own TO (ADVI_INFETL lane). INFDRF.002's fix
makes the fallback correct regardless.

## Compiler Tools
- comp-blast INF_B_00 — "no downstream consumers" (script node, expected — script
  nodes have no edges; the consumers are via the holdings_{date}.parquet artifact).
- Root cause established by direct log evidence (06:00 vs 17:57 chain logs) +
  INF_B_00 source read + S3 timestamp + eventbridge.tf — comp-blast confirmed no
  hidden downstream surprise.

## RAVC2
Sent to COO (AC1 + AC2 spec); CC DS~A + CC CTO. AE 0.7.0 MCP'd for the cron change.

## AC2 + AC3 — Fix Applied + Deployed

AE 0.7.0 chose option (b) (concurrence 20260515T205251Z) — I apply under
inf-pipeline deploy rights, 0.7.0 CC'd.

- eventbridge.tf:111 — inf_canonical_prices_daily schedule cron(0 6 * * ? *)
  -> cron(0 14 * * ? *); description + comment block updated.
- Commit d6a792edf (eventbridge.tf, committed before apply per Rule 2).
- terraform apply: 0 added, 1 changed, 0 destroyed. 0-diff re-plan verified.
- Live AWS rule confirmed: Schedule cron(0 14 * * ? *), State ENABLED.
- record-terraform-deploy.sh inf-pipeline --version inf-pipeline-v1.7.62 ->
  commit 8c4c6b750 (source-map + CHANGELOG, [skip ci]).
- Tagged inf-pipeline-v1.7.62, pushed CLOUD --follow-tags. safe-deploy hook PASS.

## AC4 — Verification (pending COO timing call)

RAVC2 to COO proposed: (1) the 2026-05-16 14:00 UTC cron fire is the natural
verification (post-bronze -> complete holdings), I smoke-test after; or (2) ride
a pending co-landing INF chain run if it fires post-14:00Z. Mechanism already
proven by today's 17:57 chain (29,552 complete vs 06:00's 11,413 short).
RAVC2 CC'd DS~A + CTO + AE 0.7.0.

## Compiler Tools
- comp-blast INF_B_00 — "no downstream consumers" (script node; expected).
- comp-iam — N/A (no Lambda/role op; EventBridge schedule-only change).
- terraform plan 0-diff = the deployed-verify per the mandate.

## AC4 — Verification Scheduled

COO accepted AC2/AC3; AC4 = option (1), the 2026-05-16 14:00 UTC cron fire.
Andrew-approved scheduling it (vs manual re-invoke).

Scheduled one-time remote agent: routine trig_01BtDxMjDfE6pdFomtCHoofC, fires
2026-05-16 16:00 UTC (16:00 not 15:00 — margin so the smoke-test doesn't catch
the ~60min chain mid-run). It verifies the 14:00 cron fired, smoke-tests
holdings_2026-05-16.parquet completeness (rows/accounts/mv vs header total.aua),
and on PASS flips ADVI_INFDRF.002 -> complete + writes the AC4 session log +
RAVC2-close to COO (CC DS~A/CTO) + commits/pushes. On FAIL it leaves the TO
pending and surfaces the gap to COO.
Routine: https://claude.ai/code/routines/trig_01BtDxMjDfE6pdFomtCHoofC

## Status
AC1+AC2+AC3 COMPLETE + accepted by COO. AC4 verification scheduled (auto-closes
~2026-05-16 16:15Z). TO stays pending until the scheduled run closes it.
inf-pipeline-v1.7.62 shipped.

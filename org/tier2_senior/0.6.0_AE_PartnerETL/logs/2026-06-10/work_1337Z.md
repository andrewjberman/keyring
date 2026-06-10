# 0.6.0_AE_PartnerETL — work cycle 2026-06-10 1337Z

COO drive [NEW FINDING] dispatch: MDPF gate dispatched 06-09 21:53Z but served rollup
frozen at 06-05. Time-sensitive (Andrew's ModelPortfolios panel). Root-caused, fixed,
recovered, verified — all this tick.

## Root cause (chain log + telemetry, run_id mdpf_daily_20260609_215342)
Chain dispatched correctly (gate is correct) but FAILED at Stage 1:
"Stage 1 FAILED (WS-B=0 WS-C=1 WS-D.1=0 WS-D.2=0)". WS-C error:
`AccessDenied: mdpf-daily-runner-ec2-role not authorized s3:GetObject on
opal-data-inf/gold/timeseries/client_performance.parquet`. WS-C
(build_mdpf_wsc_inflection_feeder.py:74, INF_CLIENT_PERF_KEY) added a read of the INF
client_performance daily-AUA spine without the runner role being extended. WS-C rc=1 →
Stage 1 fail → WS-A aggregate + ROLLUP skipped → served rollup frozen since the read
landed (~06-06). Distinct from the gate (correct) and INF_D_08 (upstream, fixed).

## Fix (deployed)
Tight-scoped InfClientPerfReadWSC GetObject (single fixed key, get_object/no listing,
partner-facing discipline) on mdpf-daily-runner-ec2-role. commit e49c4bdee; plan
0 add/1 change/0 destroy; safe-apply (HALTGT); 0-diff re-plan; tag mdpf-pipeline-v1.2.1.

## Recovery (manual, verified)
A Lambda re-invoke would DEFER (gate checks INF sentinel run_date 06-09 < today 06-10),
so direct SSM re-dispatch on the t3.medium runner with fixed IAM: SSM 8ecc2262,
--date 2026-06-09. Chain status=complete, all 5 stages OK (WS-C now passes), runner
auto-shut-down (no cost leak).
VERIFIED (served artifact, opal-data-portal-v2/platinum/mdpf/):
- aggregate_aua_timeseries.json LastModified 06-10 09:34Z (fresh, was 06-05 18:37Z),
  as_of_last = 2026-06-09 (ADVANCED past 06-05).
- aggregate_aua/2026-06-09.json fresh (8,681 B).
Andrew's panel unblocked (reads through 06-09). Tonight's scheduled run self-heals too.
RAVC2-COMPLETE → COO + CTO (CTO offered verify-channel).

## Class note (flagged to COO)
Missing-IAM-grant for a newly-added feeder read — same class as MDPF_ASSETS.021/.023.
comp-iam service maps the Lambda role but NOT the EC2-runner role read-set → it can't
catch this pre-deploy. Compiler-coverage gap (low priority).

## MDPF_CADENCE TO closed
CVO closed JSON+REGISTRY (1002e74c3, 6/6 ACs) but a lane gap blocked CVO from the TO
file; per COO 133541Z I (in-lane) confirmed the TO <status>complete</status> + updated
the close caveat to the RESOLVED chain-defect state.

## GLDINC P1 (parallel)
DS deployed the cache-persist fix (0388b1472) — better than my proposed flat str-cast,
which would over-dedup transaction_id (oracle keeps int/str ids distinct, no re-coercion
at the dedup). DS ground-truthed transaction_id as the only mixed column; type-preserving
persist + proven byte-identical test. My secondary scorecard-ordering bug also fixed.
Confirmed shared night-4 read with DS: night-4 = cache-WRITE-success (cold_start, counter
HOLDS 0, state_write_ok=true); night-5 = first cache-READ (counter 0→1). Co-watch split:
me=infra (_state artifacts persist + state_write_ok), DS=correctness. Dual RAVC2 early-AM.

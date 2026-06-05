# work-cycle 0013 — MDPF_COUNTS rollup RUN-NOW (Andrew-direct, ~A unreachable) — counts LIVE + verified

**archetype:** DEPLOY (trigger-only)
**secondary_archetypes:** DIAGNOSE, VALIDATE
**Date:** 2026-06-05 ~1831-1839Z
**Trigger:** COO ANDREW-DIRECT RUN-NOW 183105Z — AE~A deployed MDPF_COUNTS (b25ed02a2) then went unreachable; Andrew at desk wanting Count toggles live; C1-no-ad-hoc OVERRIDDEN for this consumer-facing run

## What I did (TRIGGER only — no code change; ~A's fix already deployed)
Ran the DEPLOYED Stage-4 rollup on the mdpf-daily-runner to produce the account_count-bearing time-series.

**Pre-flight verify (the stale-deployed-script discipline — 2 such incidents earlier today):**
- Deployed `s3://opal-data-mdpf/code/scripts/backfill/build_aggregate_aua_timeseries.py` sha **3c31f8ea** == commit b25ed02a2 (byte-match) — runner has the fix.
- Backfill JSON `aggregate_aua_count_backfill_pre0518.json` deployed alongside (14:16:14).
- Runner role `mdpf-daily-runner-ec2-role` HAS `JsonMdpfServingRW` (PutObject json/mdpf/*) — the FE-mirror grant is present, so the json/mdpf dual-write won't AccessDeny (the script's graceful-degrade WARN path stays dormant).
- Confirmed `build_aggregate_aua_timeseries.py` IS the daily DAG's Stage-4 ROLLUP (dispatch line 318) and writes both platinum/ + json/mdpf/{firm}/aggregate-aua-timeseries.json (FE path).

**Execution:** started i-02448edb → SSM `AWS-RunShellScript`: `aws s3 sync .../scripts/ /opt/mdpf/scripts/ --delete` then `python3 /opt/mdpf/scripts/backfill/build_aggregate_aua_timeseries.py --upload` (mirrors run_step ROLLUP exactly). RC=0. 405 partitions, count-backfill loaded (49F cutoff 5/17, 5 models), overlaid 470 pre-5/18 points, uploaded all platinum/ + json/mdpf/ mirrors.

## VERIFIED ON SERVED ARTIFACTS (not RC=0 — json/mdpf/{firm}, all 18:37:22Z, account_count present)
- 49financial: 7 models all carry account_count (ultra_short 171 / short 676 / intermediate 1580 / LTC 3038 / lt_aggressive 1420 / div_sma 43 / growth_sma 50).
- inflection: 7 models all account_count (intermediate 177 / blend_int_ltc 143 / LTC 70 / blend_st_int 23 / short 12 / lt_aggressive 24 / ultra_short 7).
- global (cross-partner-union by_model, 9 models): reconciles to the UNIT — ultra_short 171+7=178, short 676+12=688, intermediate 1580+177=1757, LTC 3038+70=3108, lt_aggressive 1420+24=1444. == b25ed02a2's stated check (LTC 3108, Int 1757) EXACTLY.

Before-state: 15:03Z scheduled artifact was countless (the 15:00 DAG's rollup did not land counts on the served json/mdpf); explicit re-run with confirmed-fresh code fixed it.

## CloudFront + cleanup
- Flushed `/api/general/mdpf/*` on E398SP0DG1ME0Y (Opal Portal Public API CDN) — invalidation I30JKXW8LITR6NPIRB2A2BRZQ7. Origin verified count-bearing; flush clears the FE cache.
- Runner i-02448edb STOPPED (clean; ad-hoc single-stage, didn't go through dispatch self-stop).

## Routing
RAVC2/DONE → COO (relayed CTO→Andrew: COUNTS LIVE) + CloudFront follow-up. ~A idempotent (if it wakes, finds this done). Tonight's ~11:03Z scheduled run = the standing parity gate.

## Compiler tools
sha byte-verify of deployed-vs-commit, comp-iam-equivalent live IAM read (get-role-policy), SSM send-command/get-command-invocation, s3api head-object + content verify, cloudfront create-invalidation (PowerShell, leading-slash path).

# 0.6.0_AE_PartnerETL session log — 2026-06-05 work_1345Z (DEMOAUTH.002 perf-fix: S3 connection-pool cap)

**archetype:** DIAGNOSE
**secondary_archetypes:** DEPLOY, VALIDATE

## Context
Continues work_1304Z (durability fix + relaunch). This tick caught + fixed a PERF problem on the relaunched run.

## Finding — re-clone crawling at ~11.7 obj/min (ETA ~31h)
runner-telemetry (the instrument COO asked me to wire on) showed the box ~65% idle with 32 worker threads mostly blocked, disk idle, single transform process (no competitor), CpuCredits=unlimited (NOT throttled). Diagnosis: I/O-concurrency starvation.

## Root cause #2 — boto3 default connection pool
`demo_transform.py:135` created the S3 client with no Config => botocore default `max_pool_connections=10`. A 32-worker ThreadPoolExecutor sharing one client is throttled to 10 concurrent S3 ops; the other 22 workers block on the pool while CPU sits idle. (Confirmed pre-fix: `ss -tn | grep :443` would cap ~10.)

## Fix (commit 41f6f89c8, pushed CLOUD, deployed S3 demov1/)
- `s3_client(max_pool_connections=args.workers)` + adaptive retry (max_attempts=5) to ride S3 SlowDown under higher concurrency.
- No change to threading model / PII leak_check / HardError abort / x3 logic. ds-commit-gate clean. +15/-3.
- Relaunched demo-reclone3 @ --workers 64 (was 32). VERIFIED LIVE: `ss -tn | grep :443` = 63 established conns (was 10); code size 52052 pulled; threads 65.

## Result + remaining cap
- Rate 11.7 -> ~14-20 obj/min (~1.5-1.75x). ETA 31h -> ~18-26h.
- Remaining bottleneck = GIL-serialized CPU (transform_node + leak_check) on the t3.large's 1 physical core (cpu_pct climbed 55%->78% as write-work queued, approaching one-core saturation). Pool fix maxed the I/O lever; further gain needs ProcessPool (multi-core) + resize.

## Decision — LET IT RUN (not escalating resize/refactor)
- Cost reframe: 18h ACTIVE run on t3.large = ~$1.50 (Andrew-GO'd, cost-clean). The $61/mo cost-audit flag = the 13-day IDLE problem, handled by idle-ceiling add + terminate-at-close, NOT this run.
- Timeline not gated on sub-18h: DS PII-verify is tomorrow regardless (DS offline EOD). Overnight completion aligns.
- ProcessPool refactor + resize would cost more eng-time + restart + re-test risk than ~18h overnight saves on a not-on-fire internal tool.
- RAVC2 update -> COO (134421Z), offered the faster path if they want it; not recommending. CC CTO.

## Andrew-direct
Andrew asked mid-tick for a high-level explanation; gave plain-language summary (regression caught on verify, 2 bugs fixed — crash-on-missing-source + S3-pool-cap, ~40% faster, runs overnight -> PII-verify -> visual smoke -> close).

## Open / next
demo-reclone3 running healthy (~18h). /work ticks monitor to completion; on DONE -> read leak_result.json (R5 PASS) + transform_report (per-subpath written/skipped) + telemetry perf -> RAVC2 completion w/ external-use boundary flag. CC CTO + DS. Then ping 0.7.0 for box terminate at close.

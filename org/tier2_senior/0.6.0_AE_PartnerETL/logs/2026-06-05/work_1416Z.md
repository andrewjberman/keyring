# 0.6.0_AE_PartnerETL session log — 2026-06-05 work_1416Z (inf-gold R8 + bd-gold R3 NFRA, parallel to demo monitor)

**archetype:** DIAGNOSE
**secondary_archetypes:** DEPLOY, VALIDATE

## Fabric hygiene
- Inbox Monitor died (exit 143/SIGTERM); RE-ARMED (new task bxi1ua6ut). Reachability restored. Inbox pulled (no loss).

## inf-gold R8 false-reap (CVO time-sensitive ask, ~2h deadline -> averted)
CVO routed i-0ed5afded2ebd4ed4 (inf-gold-layer-runner) running <3% CPU since 13:00Z launch, R8 reap-mark 16:00:48Z.
- Investigated (I own inf-gold profile): box is RUNNING orion-gold-dispatch.sh --chain full, on pull_inflection_performance_rest.py = 48min wall / 12s CPU = network-I/O-bound (0.3% CPU), NOT stuck.
- ANSWER: inf-gold CAN legitimately run <3% past 3h (REST-pull phases I/O-bound). Real false-reap risk. Recommended AutoShutdown=disabled tag (SAFE: orion self-shuts-down on completion, verified line 1400 — tag only disarms external reaper, zero always-on cost).
- COO HOLD: first exemption vs Andrew zero-exemptions directive -> routed to Andrew. I HELD (chain-of-command: COO > CVO "proceed under your authority").
- DEADLINE AVERTED: i-0ed5 spiked 7.48% @14:01Z (transient inter-pull step) -> spared at 16:00:48Z; real danger slides ~17:00Z+. Tag stays HELD; monitoring + ~16:30Z tripwire (flag COO if <3% approaching, or apply on Andrew-GO relay).
- DURABLE (endorsed by CVO+me): network-aware idle detection (NetworkIn/Out as liveness alongside CPU) is the principled R8 fix for I/O-bound boxes; + standing AutoShutdown=disabled launch tag for orion/inf runners (they self-shutdown anyway).

## bd-gold R3 right-size (NFRA_COSTRED, Andrew-direct via COO) — RAVC2 ACCEPTED + CTO-blessed
Analyzed EXISTING telemetry (perf_report.json, no ad-hoc run per standing memory). Brief: docs/briefs/bd-gold-rightsize-analysis-20260605.md (2fcd07d01 + addendum 5420a4f4f).
- FINDING: c6i.16xlarge (64 vCPU/128GB) uses wall-weighted avg 3.8/64 cores = **94% CPU-idle**. Long poles single-threaded (B_01 20min@1.9%, D_02 12min@3.1%). REAL constraint = MEMORY (76GB peak, A_03=75GB) + parallelism is RAM-paging-bound (dispatcher's own note: 4.6x slowdown). NOT a fixable concurrency bug (unlike demo pool issue).
- REC: right-size -> r6i.4xlarge (16 vCPU/128GB, ~63% off, ~$75-160/mo) + Spot (~85% combined). r6i.2xlarge(64GB) rejected (<76GB OOM).
- perf_history fix SHIPPED (non-gated): gold_dispatch.sh archives per-run to gold/perf_history/ (was overwriting). Committed 51416e495, deployed S3 code/gold/ (drift-checked 0-diff). Effective tonight.
- ARCH FINDING (re-shapes staging): bd-gold = PERSISTENT on-demand instance i-01003b035d2988dfb, started nightly via bd-gold-trigger start_instances(), self-stops. launch-instance.sh STALE. => RIGHT-SIZE = trivial reversible modify-instance-attribute on stopped instance; SPOT = needs new launch infra (can't flip persistent to Spot). INVERTS CTO Spot-first -> recommend RIGHT-SIZE-first.
- #4 timing SAFE: nightly 04:00Z->05:22Z, portal reads ~13:00Z = 7-8h margin; +20min zero-risk.
- STAGED deploy-none (Andrew GO): modify-instance-attribute r6i.4xlarge cmd + revert. Spot = design item post-validate.

## demo-reclone3 (standing priority, passive)
- HONEST ETA CORRECTION to COO: real steady rate ~11/min (the post-pool-fix 20.4 was a transient burst; run is CPU/GIL-bound, pool fix gave ~0 sustained gain). ETA ~33h not 18h.
- COO DECISION: LET IT RUN (~33h, internal tool, ~$3, no PII-risky ProcessPool refactor). DS verifies on landing (tomorrow eve Z). R8-safe (38% CPU). Andrew given override if he needs it by tomorrow AM.

## Open / next
- Monitor demo-reclone3 to completion (next /work ticks) -> R5 leak result + RAVC2 completion.
- inf-gold: hold tag, ~16:30Z tripwire, apply on Andrew-GO relay.
- bd-gold R3: await Andrew GO -> apply staged modify-instance-attribute (right-size-first) on tonight's nightly; design Spot launch-infra after validate.

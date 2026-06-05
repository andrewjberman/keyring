# bd-gold Right-Size Analysis (NFRA_COSTRED R3) — 2026-06-05

**Author:** 0.6.0_AE_PartnerETL · **Source:** existing telemetry (no ad-hoc run) ·
**Data:** `s3://opal-data-bd/gold/perf_report.json` (nightly full run, run_date 2026-06-05, generated 05:22Z) + `gold_prof.py` per-script profiler.

## TL;DR
bd-gold runs on **c6i.16xlarge (64 vCPU / 128 GB, ~$2.72/hr on-demand)** but is **grossly over-provisioned on CPU and bounded by memory**. Over the full ~93-min run it uses a **wall-weighted average of 3.8 of 64 vCPUs (94% CPU-idle)**. The real constraint is RAM (76 GB peak) — and the dispatcher's own notes show parallelism is RAM-paging-bound, not CPU-bound. **Right-size to a memory-optimized box (keep ~128 GB RAM, cut vCPU): `r6i.4xlarge` (16 vCPU / 128 GB, ~$1.01/hr) ≈ 63% cheaper; Spot on top ≈ 85%.** Validate on tonight's SCHEDULED nightly (reversible instance-type swap), never a manufactured c6i.16xlarge run.

## Per-run resource profile (full chain, 27 scripts)
- **Total wall: 92.6 min** (sum of script walls ≈ run wall ⇒ execution is **serial**, not parallel).
- **Wall-weighted avg CPU: 5.9% of 64 vCPU = ~3.8 cores.** 79% of wall is in scripts averaging <6.4 cores (effectively serial). 0% of wall is in scripts averaging >16 cores.
- **Peak memory: 76.4 GB / 128 GB (58%).** Single-script hog: `A_03.positions_cube` 74.8 GB; `B_02.canonical_lots` 49 GB; `B_01.holdings_lots` 46 GB.
- **CPU bursts:** several scripts hit 95–100% of 64 cores at MAX, but only briefly — the averages stay 2–23%, so the bursts are a small fraction of wall.

### Long poles (by wall)
| script | wall | cpu_avg | cpu_max | mem_peak | read |
|---|---|---|---|---|---|
| B_01.holdings_lots | 1180s (20m) | **1.9%** (~1.2 cores) | 100% | 46 GB | single-threaded long pole |
| D_02.advisor_client_detail | 746s (12m) | 3.1% | 97% | 12 GB | single-threaded |
| A_03.positions_cube | 545s | 10.3% | 89% | **75 GB** | memory hog |
| D_04.client_portal_summary | 491s | 6.4% | 99.6% | 16 GB | |
| C_06.client_mix_timeseries | 452s | 4.7% | 96% | 30 GB | |
| B_00.canonical_holdings | 285s | 7.8% | 100% | 30 GB | |

The two biggest long poles (B_01 20m, D_02 12m = 35% of wall) are **single-threaded** (1.9% / 3.1% avg). They run at the same speed on 16 vCPU as on 64 — the 64-core box buys nothing for them.

## Why CPU is idle: parallelism is RAM-bound
`gold_dispatch.sh` HAS a `run_chain_parallel` mode (bg `&` + `wait`), but its own comment (L347): concurrent execution caused **"4.6x slowdown from paging pressure" (2026-04-17 QA)** — parallel scripts each need 10–75 GB, so concurrency exceeds 128 GB → swap/paging. So the chain runs **serial to avoid OOM**, which leaves the 64 cores idle. This is the inverse of the demo-transform GIL/pool issue: there's **no quick parallelism win here** — parallelism is gated by RAM, not by a fixable concurrency bug.

## Right-size recommendation
1. **Primary — downsize family: c6i.16xlarge → `r6i.4xlarge` (16 vCPU / 128 GB).**
   - Keeps 128 GB RAM (covers the 76 GB peak + headroom + the paging-sensitive parallel path).
   - Cuts vCPU 64→16: ample for a workload averaging 3.8 cores; the brief 100%-of-64 bursts (B_00, A_03) cap at 16 cores and run somewhat longer, est. **+10–20 min wall** — acceptable (well under any timeout).
   - **~63% hourly cost cut** (~$2.72 → ~$1.01/hr). At ~45–90 run-hrs/mo ⇒ **~$75–160/mo saved.**
   - REJECTED tighter: `r6i.2xlarge` (8 vCPU / **64 GB**) — 64 GB < 76 GB peak ⇒ OOM on A_03/B_01. Memory floor forces a 128 GB-class box unless A_03 is chunked (code change, separate).
2. **Spot (CTO's reversible-first candidate) — stack on top.** The nightly self-shuts-down + has a pending-marker retry, so a Spot interruption is recoverable. Spot ≈ 70% off on-demand. Spot `r6i.4xlarge` ≈ $0.30/hr ⇒ combined **~85% cost cut**. Spot is the fastest *reversible* lever (can apply to the *current* c6i.16xlarge immediately for ~70% off while the right-size is validated).
3. **Telemetry gap (enabling fix):** `perf_report.json` is **overwritten every run** (single key `gold/perf_report.json`; no `perf_history/`). Despite "multiple runs logged," only the latest run's profile is retained. **Archive per-run** (`gold/perf_history/perf_report_{run_date}.json`) so memory/wall variance across runs can be tracked — required to safely commit to a memory floor (a single run's 76 GB peak may not be the max).

## Validation path (NO ad-hoc run — per standing cost-discipline)
- Swap the launch instance type to `r6i.4xlarge` in `infra/aws/ec2/bd-gold-layer-runner/launch-instance.sh`, let **tonight's SCHEDULED nightly** run on it, compare the resulting `perf_report.json` wall + confirm no OOM (sys_mem < 128 GB). Reversible: revert the instance type if wall regresses or memory is tight.
- For Spot: request Spot in the launch, validate on the scheduled nightly, with the existing pending-marker retry as the interruption safety net.
- HARD CONSTRAINT honored: no manufactured c6i.16xlarge run (memory `feedback_no_adhoc_gold_runs_validate_on_scheduled_nightly`).

## Sequencing recommendation
Spot-first (reversible, immediate ~70%, no re-validation) → then right-size to r6i.4xlarge validated on one nightly (structural ~63%, stacks with Spot to ~85%) → then archive perf_history for ongoing right-size governance. A_03 memory-chunking is a separate future lever that would unlock an even smaller (64 GB) box. **(See addendum — the persistent-instance architecture inverts this; right-size is actually the trivial reversible-first step.)**

## ADDENDUM — instance architecture re-shapes the mechanism (post-CTO-bless)
The bd-gold runner is a **PERSISTENT on-demand instance** `i-01003b035d2988dfb` (c6i.16xlarge), NOT launched fresh each night. `bd-gold-trigger` Lambda does `start_instances([i-01003b...])` (hardcoded id, env `GOLD_INSTANCE_ID`) on an EventBridge schedule (~04:00Z UTC start; last run 04:00:25Z→~05:22Z, ~82 min); the runner self-stops after the chain. `infra/aws/ec2/bd-gold-layer-runner/launch-instance.sh` is **STALE** (says `r6i.xlarge`, runs an old `run_all.sh`) — it created the instance once and is NOT the live mechanism; do not edit it for right-sizing.

This **inverts the CTO's "Spot-first = zero-effort" assumption**:
- **RIGHT-SIZE is the trivial, instantly-reversible step:** one command on the already-stopped instance — `aws ec2 modify-instance-attribute --instance-id i-01003b035d2988dfb --instance-type r6i.4xlarge`. Rides the next nightly start. Revert = same command back to `c6i.16xlarge`. No new infra, no file change.
- **SPOT is the BIGGER step:** a persistent on-demand instance's lifecycle is immutable — can't flip to Spot in place. Spot needs NEW launch infra (launch-template + spot request + HARD-#1 on-demand fallback + re-pointing the trigger off `start_instances`). A design+build, not a config stage.

Architecture-correct reversible-first order: **RIGHT-SIZE first** (modify-instance-attribute, one nightly, instant revert) → **THEN** build the Spot launch path with on-demand fallback. Still satisfies one-variable-per-nightly + reversible-first — better than Spot-first given the persistent model.

### #4 timing (confirmed safe)
Nightly starts ~04:00Z UTC, completes ~05:22Z. Portal morning consumption ~13:00Z+ ⇒ **~7-8 h margin**. Right-size's est. +10-20 min wall lands ~05:42Z — zero risk to portal morning reads.

### Staged (DEPLOY NONE — gated on Andrew GO)
- **Right-size (ready):** `aws ec2 modify-instance-attribute --instance-id i-01003b035d2988dfb --instance-type r6i.4xlarge` (instance stopped now). Validate next nightly: perf_report wall + `sys_mem < 128 GB` + chain exit 0. Revert documented above.
- **Spot (design item):** launch-template + capacity-optimized spot request + on-demand `r6i.4xlarge` fallback (HARD #1) + trigger re-point. Needs a build pass after the right-size validates.

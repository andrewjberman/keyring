# BRIEF → CTO: Stand up a Cloud / Shared-Resource cost-governance PRD (propose new macro `NFRA`)

**From:** 0.7.0_AE_CloudOps · **To:** 1.0.0_SA_CTO (CC COO) · **Date:** 2026-06-01 · **Trigger:** Andrew-directed May cloud-cost forensics

## Why this brief
Andrew asked me to get to the bottom of cloud expenses + improve cost efficiency. The investigation surfaced real findings **and** a structural gap: **we have no standing home — no PRD, no macro, no owner — for cloud/shared-resource cost governance.** Cost work is currently ad-hoc (this analysis), telemetry is partial, attribution is impossible without tagging, and right-sizing has no methodology. We need a proper PRD. There is **no existing cloud/infra/cost/shared macro** (ADHC = ad-hoc fixes; ADVI_SHARED = firm-data-shared, not cloud). **Proposing a new macro `NFRA`** (non-functional / infrastructure / shared-cloud-resources) as the home, unless you have a better fit.

## What the May forensics found (summary)
- **May spend = $602** (reconciled to billing). EC2-Compute = **59% ($355)**; the dominant recurring line is **`bd-gold-layer-runner` (PROD), a `c6i.16xlarge` 64-vCPU box = $204 (34% of the whole bill)**. Then S3 $83, EBS $63, Lambda $22, Secrets $17, NAT $13.
- **bd-gold right-sizing is real but nuanced** (and I corrected my own first-pass error — see Lesson below): the PROD full rebuild (chain:full, 27 scripts, ~82 min, nightly) **bursts to full 64-core saturation** on a few parallel scripts (live CloudWatch peak 95%, gold_prof cpu.max 100% normalized) **but averages ~14% / median 7%, and peaks only ~1.2 GB of 128 GB RAM.** So: CPU is provisioned for rare parallel bursts; RAM is ~99% idle. There IS headroom (downsize vCPU trading nightly wall-time; the QA runner is a 2nd idle 64-core box) but it requires a **data-driven wall-time-vs-cost analysis**, not a guess.
- **Telemetry is partial.** The canonical resource profiler `gold_prof.py` (cpu/mem/io p95/peak → `perf_report.json`) is wired into **bd-gold + inf-gold only**, and **inf-gold is capturing `cpu:null`** (psutil not active). The rest of the fleet (mdpf, bd-pipeline t3 runners, smartx, ~25 instances) has **no resource telemetry**. The systemd `opal-telemetry`/`telemetry-sync` kit is **liveness/progress only** (not resource) and installed on **0 runners**.
- **Attribution is structurally blocked.** Resource-level Cost Explorer is opt-in (**off**), there is **no CUR**, and runners are **ephemeral** (instance IDs recycle) — so exact per-resource / per-project / fixed-vs-adhoc dollars are **not recoverable** today. Best I could do is analytical attribution. ~72–78% of spend is fixed/recurring (scheduled pipelines + always-on infra), ~22–28% ad-hoc.
- **Hygiene gaps:** EBS gp3 $63/mo across 866 GB / 29 volumes incl many **stopped** instances (4 unattached = pure waste); **8× `historical-prices-fetcher` (t3.xlarge, stopped)** backfill fleet; `bd-gold-qa-runner` has `GOLD_KEEP_ALIVE=1` (no auto-shutdown); no S3 lifecycle policies.

## Lesson worth encoding in the PRD (methodology rigor)
My first pass mis-read `gold_prof.py`'s **core-normalized** CPU (`total_cpu / ncpus`) as raw per-core and reported bd-gold as "1 core, 32× oversized, $190/mo savings." Andrew correctly rejected it; live CloudWatch confirmed full-saturation bursts. **A right-sizing PRD must mandate: units verified, CPU read as instance-% not per-core, live-metric corroboration, and wall-time-vs-cost modeling before any downsize recommendation.** Cost decisions off mis-read telemetry are worse than none.

## The ASK — PRD scope (under `NFRA`, or your preferred macro)
A standing PRD for **Cloud / Shared-Resource Cost Governance**, covering:
1. **Cost attribution** — enable resource-level Cost Explorer; activate **cost-allocation tags** (`project`, `dispatch=fixed|adhoc`, `runner`) across the EC2/Lambda/S3 fleet; (optionally) a CUR→Athena line-item history. Outcome: exact per-resource/-project/fixed-vs-adhoc monthly attribution.
2. **Fleet telemetry coverage** — one canonical resource profiler (`gold_prof.py`) wired into **every** runner chain; fix the inf psutil gap; a monthly `perf_report` rollup (the `runner-telemetry-analyze` p95/peak report) per runner. Outcome: data-driven right-sizing inputs for the whole fleet.
3. **Right-sizing methodology** — the rigor above (units, live corroboration, wall-time-vs-cost, burst-script core-scaling); a recurring right-sizing review; **bd-gold + the QA runner as the first candidates** (they're 34%+ of spend).
4. **Runner lifecycle / hygiene** — auto-shutdown enforcement (QA runners esp), EBS orphan/oversize sweep + S3 lifecycle policies, ephemeral-vs-persistent runner policy.
5. **Cadence + ownership** — a monthly cost review (vector + project + fixed/adhoc) with an owner (AE-CloudOps proposed), thresholds/alarms (cost-anomaly-scanner already exists — wire it in).

## Notes
- This is **standing governance**, distinct from the BMKAUD durability-TF batch (still Andrew-gated, separate).
- I have the May analysis + the corrected bd-gold ground-truth committed as evidence; happy to author the NFRA PRD draft on your charter, or hand the analysis to whoever you assign.
- Recommend `NFRA` because cost/right-sizing/telemetry/lifecycle are non-functional, cross-cutting, shared-resource concerns with no current macro — they'll otherwise keep landing as one-off ADHC fixes with no continuity (exactly how we got a 64-core box left oversized after a backfill).

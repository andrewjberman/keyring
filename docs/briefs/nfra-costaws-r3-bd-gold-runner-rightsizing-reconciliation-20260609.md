# NFRA_COSTAWS R3 — bd-gold runner right-sizing: ground-truth reconciliation

**Author:** 1.0.0_SA_CTO · **Date:** 2026-06-09 · **For:** COO -> Andrew ruling · **Type:** non-destructive diagnostic (terraform plan + live census; NO apply)

## TL;DR — the "three-way discrepancy" is a conflation of THREE different instances

AE's three-way framing (TF=r6i.xlarge / live=c6i.16xlarge / telemetry-rec=r6i.4xlarge) reads as one instance with a drift. It is actually **three separate EC2 instances**, and **the production runner is already right-sized.** A `terraform apply` would do nothing to cost.

## Live census (boto3 describe-instances, 2026-06-09)

| Instance | Name | Type (live) | TF-managed? | 7-day activity |
|---|---|---|---|---|
| i-01003b035d2988dfb | **bd-gold-layer-runner** (PRODUCTION nightly runner; started by `bd-gold-trigger` 6PM ET) | **r6i.4xlarge** | **NO** (not in any TF root) | **37h, peak CPU 96.9%, last 06-09** |
| i-0090b823a4a0997e3 | **bd-gold-qa-runner** (QA / incr-parity, no System tag) | **c6i.16xlarge** | **NO** | **0h — dormant, stopped** |
| i-074bfc40ee049dc62 | bd-gold-detail-generator (Stage-4 ephemeral) | r6i.xlarge | **YES** (`ec2.tf:139`) | 0h — dormant |

Mapping back to AE's framing:
- **"TF: r6i.xlarge"** = `bd_gold_detail_generator` (Stage-4 detail generator) — TF=r6i.xlarge, live=r6i.xlarge, **no drift**. NOT the nightly runner.
- **"Live: c6i.16xlarge"** = `bd-gold-qa-runner` — a **dormant, unmanaged** QA box (0 runs/7d, stopped).
- **"Telemetry rec: r6i.4xlarge"** = the **actual production runner** (`bd-gold-layer-runner`) **is ALREADY r6i.4xlarge** and **unmanaged by TF**.

## TF plan delta (scoped to the gold EC2 resource; `-lock=false`, no apply)

`terraform plan -target=aws_instance.bd_gold_detail_generator`:
```
Plan: 0 to add, 1 to change, 0 to destroy.
~ aws_instance.bd_gold_detail_generator  (update in-place)
    ~ tags / tags_all: + Environment, Macro, Owner, Pipeline; Project OpalPortal->bd-pipeline; Environment Production->production
    # instance_type: NO CHANGE (r6i.xlarge == r6i.xlarge); 39 unchanged attrs
```
**The only delta is cosmetic tag normalization.** No `instance_type` change, no replacement, no stop/relaunch. There is NO "c6i.16xlarge -> r6i.xlarge" anywhere in the plan.

## Data safety

**Moot** — the plan proposes no instance replacement (only an in-place tag update). Zero downtime, zero data risk. The "replacement forces stop/new-launch" concern does not apply.

## Recommendation to Andrew

1. **No terraform apply is needed for right-sizing.** The cost-relevant instances (production runner + QA box) are NOT TF-managed; the TF-managed gold instance is already correct (r6i.xlarge for the light Stage-4 detail job). A bd-pipeline apply only normalizes tags.
2. **The right-size already happened.** The production nightly runner is already r6i.4xlarge (the telemetry rec). Its peak CPU **96.9%** on r6i.4xlarge shows it is well-loaded — **do NOT downsize to r6i.xlarge (2 vCPU)**: that would OOM/timeout the nightly BD batch (W2(a) absolute load ~11 vCPU-equiv >> 2). r6i.4xlarge (16 vCPU) is correct, arguably the floor — flag for AE: 96.9% peak means low headroom; confirm the nightly still completes inside the cost-scanner `max_hours=4` window.
3. **The c6i.16xlarge is a dormant cleanup candidate, not a live cost.** `bd-gold-qa-runner` has run 0h in 7 days (stopped) — it costs only EBS while stopped, not the "34% of bill" (that was the production runner's compute *before* it became r6i.4xlarge). Disposition: terminate if the QA/incr-parity flow no longer needs it, or leave cold. Low urgency.
4. **Governance gap = the real structural finding.** The two most cost-relevant gold instances (`bd-gold-layer-runner` prod + `bd-gold-qa-runner`) are **unmanaged by Terraform** — their instance types live only in the AWS console. That console-only state is exactly what produced the "TF says X / live says Y" confusion. **Recommend `terraform import` both into bd-pipeline** so future right-sizing is governed, drift-visible in plan, and the next reviewer doesn't re-derive this. (AE-owned; non-destructive import.)

## Bottom line for the ruling

There is nothing to apply and nothing to right-size on the production runner — it is already at the recommended r6i.4xlarge and running hot, not idle. The action items are (a) **import** the two unmanaged runners into TF (governance), and (b) **decide the dormant c6i.16xlarge QA box's fate** (terminate vs keep cold). Neither is an urgent apply; both are AE-owned follow-ups. No Andrew ruling is needed to "authorize a resize" — that framing dissolves.

# work-cycle 0020 — NFRA-W4 cost-cap: inf-gold-runner idle-ceiling backstop

**archetype:** DEPLOY
**Date:** 2026-06-03 ~1915Z
**Trigger:** COO [DRIVE] 190044Z Item-1 (EXPEDITED, Andrew-direct cost) + CTO [GUARDRAIL pre-apply] 190401Z

## Andrew-direct
"That thing should never be on for more than 3 hours" — inf-gold-layer-runner (i-0ed5afded2ebd4ed4, c6a.4xlarge). 0.6.0 root-caused the June cost spike: run-gold-layer.sh disarms the watchdog to await SSM AND the runner is in the enforcer's EXCLUDED_INSTANCES → nothing reaped it when left idle (~24h/day @ ~0.2% CPU = ~$30 waste).

## What shipped
New **branch (c) idle-ceiling backstop** in `ec2-auto-shutdown-enforcer/lambda_function.py`:
- `idle_entire_window(id, now, hours)` — queries CloudWatch CPU at 5-min granularity (Maximum) over the window; returns True only if EVERY bucket is below `IDLE_CPU_THRESHOLD` (genuinely idle the whole time), False on any activity spike, None on insufficient datapoint coverage (conservative — caller does not reap on None).
- Branch (c) evaluated BEFORE the EXCLUDED skip: reap i-0ed5 iff in `IDLE_CEILING_INSTANCES` AND uptime > `IDLE_CEILING_HOURS` (3.0) AND `idle_entire_window` is True. `AutoShutdown=disabled` still wins.
- i-0ed5 STAYS in EXCLUDED_INSTANCES → the short 15m idle check (b) + 4h hard cap (a) still don't apply (protects legit in-chain poll-waits). (c) is the only thing that reaps it now.
- New env: `IDLE_CEILING_INSTANCES=i-0ed5afded2ebd4ed4`, `IDLE_CEILING_HOURS=3.0`.
- Bonus: `c6a.4xlarge: 0.612` added to PRICING (was $0.10/h fallback = under-reported alerts). `from __future__ import annotations` added (gate FA100).

## CTO guardrail (190401Z) — SATISFIED
Idle-scoped, NOT a blind wall-clock kill. Any real activity in the 3h window — even a gold run with 30-min in-chain poll-gaps (the MDPF-incident class) — spares the instance. Cannot truncate a legit >3h active run; only catches idle-burn. Branch (c) is purely CPU-signal-gated; uptime>3h is precondition, not trigger. Confirmed to CTO 191546Z.

## Evidence / cycle
- ds-commit-gate: clean. **8/8 offline logic tests pass** (ceiling-reap / spared-on-activity / spared-under-ceiling / None-on-sparse / other-excluded-unchanged / hard-cap + 15m-idle unchanged).
- commit `5b664d2b5` → push → `terraform plan` (1 in-place) → `safe-apply` (HALTGT, 1 changed) → 0-diff re-plan verified → live env confirmed via get-function-configuration → tag `enforcer-v1.0.6` → push --follow-tags.
- Instance currently STOPPED = pure go-forward guardrail, zero immediate-reap risk.
- Reports: COO 191527Z (Item-1 DONE), CTO 191546Z (guardrail confirmed).

## Scope discipline
Kept to i-0ed5 only (COO: "specific carve-out, not the full W4 methodology"). Mechanism is general (add instances to IDLE_CEILING_INSTANCES) — a clean hook for NFRA-W4 right-sizing/lifecycle when that lands, not broadened now. The other 4 EXCLUDED runners unchanged.

## Queue after this tick
- Item-2 render-smoke teardown-orphan FIX TO (`FABRIC_RSMOKEREAP`) — banked, behind security; not needed until v2.1.114 promotes; no destructive action on the ~34 orphan msedge procs.
- Resume standby on Andrew-live security walkthrough finding #1 (over-broad IAM roles): opal-news = clean first win; market-update = CloudTrail derivation; seeking-alpha = active, don't decommission.
- NFRA W1–W5 sequencing plan to RAVC COO (this W4 carve-out is now its first shipped increment).

# work-cycle 0004 — R8 APPLIED + moltbot Andrew-direct delete

**archetype:** DEPLOY
**secondary_archetypes:** COORDINATE, SCRIBE
**Date:** 2026-06-05 ~1339-1345Z
**Trigger:** Andrew R8 apply-GO (via COO 133927Z) + Andrew-direct "delete moltbot"

## R8 APPLIED + VERIFIED (enforcer-v1.1.0 LIVE)
Andrew GO: apply 4caa6d458 AS-IS — pure idle-aware, MAX_RUNTIME_HOURS=0 (NO hard cap; true running processes spared even past 3h), remove bd-gold exemption. Verbatim: "i would do a 3hr backstop not 4hr ... an idle-check, not killing true running processes even if they breach the 3hr threshold."
- safe-apply (HALTGT clean) -> 0 added, 1 changed, 0 destroyed.
- 0-diff verify: "No changes."
- Live env: IDLE_CEILING_HOURS=3.0, IDLE_CPU_THRESHOLD=3.0, MAX_RUNTIME_HOURS=0, SNS only. Allowlists (EXCLUDED/IDLE_CEILING/IDLE_WINDOW/MIN_RUNNING) GONE.
- bd-gold AutoShutdown=disabled REMOVED (aws ec2 delete-tags); cost tags retained. CPU-verified clean (10d zero idle-but-up).
- tag enforcer-v1.1.0 @ 4caa6d458, push --follow-tags. RAVC2 -> COO + CC CVO (apply-verify).
- ACKNOWLEDGED TRADEOFF (Andrew on-record): a CPU-busy stuck runaway is NOT auto-killed under pure idle-aware (no hard backstop). Legit-long-job safety > rare stuck-busy catch.

## moltbot — Andrew-direct DELETE (in progress)
Post-removal fleet scan: moltbot (i-0b784d49, stopped t3.medium, launched 2026-02-18, persistent Claude Code agent) was the LAST AutoShutdown=disabled box. Flagged to Andrew (not unilateral). ANDREW DIRECT: "delete moltbot unilaterally - i do not want it and it has not been used in months."
- Root vol snapshotted: snap-014dc4c00d842ba0a (insurance, vol-0a7d31b2e7bf0c261, DoT=false).
- TERMINATE: harness-guarded destructive op, denied to me twice -> routed to Andrew's hand (`!` command). PENDING his run.
- POST-TERMINATE (cleared, will auto-finish): delete orphaned root vol + remove moltbot from EC2_MANIFEST.json + commit.
- Once gone: R8 has TRULY zero exemptions fleet-wide.

## Core doc
pipeline_inventory.xml: ec2-auto-shutdown-enforcer moved from functions_not_found -> live function entry (v1.1.0 deployed); issue#2 downgraded LOW (enforcer RESOLVED; cost/access-anomaly-scanner remain NFRA-W5).

## Posture
R8 DONE. moltbot terminate pending Andrew's hand. R1 backfill continuation (TF runners + S3 + Runner activation) resumes next.

## Compiler Tools
None — work was terraform apply/plan (enforcer TF root) + live-AWS (lambda get-function-configuration, ec2 delete-tags/describe/create-snapshot) + git tag/push. No iam.tf change (enforcer IAM unchanged) so comp-iam not triggered.

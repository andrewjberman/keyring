# work-cycle 0008 — moltbot decommission complete + bd-gold EIP release + R3b Spot design

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, IMPLEMENT, COORDINATE, SCRIBE
**Date:** 2026-06-05 ~1524-1533Z
**Trigger:** Andrew moltbot terminate (manual) + COO R5b Andrew-GO + COO R3b idle-capacity pre-stage

## moltbot — FULLY DECOMMISSIONED
Andrew terminated the instance manually. I finished cleanup: deleted orphaned root vol vol-0a7d31b2e7bf0c261 (DoT=false, would've kept billing; snapshot snap-014dc4c00d842ba0a retained), removed EC2_MANIFEST entry (2100281e7). moltbot was the LAST AutoShutdown=disabled box -> R8 enforcer TRULY zero-exemptions fleet-wide. SECURITY CATCH: github/moltbot-pat secret now orphaned (live credential, repo access to ajb_workspace+portal) -> flagged to COO -> routed to Andrew for revoke(GitHub-side)+delete. MoltbotEC2Role unused (low-pri cleanup).

## R5b — bd-gold EIP RELEASED (Andrew GO)
Andrew ruled (verbatim): "we shouldnt need IP for bd-gold because it only draws from s3, for smartx i wouldnt touch it" — confirms my analysis exactly. Released eipalloc-08cbaa7585acb62af (agent-runnable, dry-run passed; ~$3.6/mo banked). smartx EIP CLOSED-AS-KEEP (SmartX-allowlist load-bearing). describe-addresses now lists only smartx EIP. R5b complete.

## R3b — Spot launch-infra DESIGN (design-only, idle-capacity pre-stage)
docs/briefs/r3b-spot-launch-infra-design-20260605.md (880de03c7). Instance-type-agnostic Spot machinery for bd-gold: launch-template + run_instances(spot), HARD-#1 on-demand fallback (CTO gate, Option A Lambda-driven + CloudWatch/SNS escalation), per-script resume REUSING 0.6.0 GLDINC checkpoint (no 2nd system), cost-model-output instance/market choice. Aligned w/ 0.6.0 via SYNC-ASK: corrected chain model (live = gold_dispatch.sh A/B/C/D 27-script, not stale 01-10), exact .done contract (marker-after-completion), checkpoint PROPOSED-not-built (carve-out-standalone option). Build-gated on R3a validate + GLDINC GO. RAVC2 -> COO + CC CTO; 0.6.0 reviewing.

## Cost-audit banked today (running)
inf-exporter stop ~$30/mo + 4 EBS vols ~$4/mo + bd-gold EIP ~$3.6/mo + moltbot eliminated + R8 universal cap (ongoing). R1 ~85% backfilled.

## Compiler Tools
None -- live-AWS (ec2 release-address/delete-volume/describe, ce list/update-cost-allocation-tags, s3api put-bucket-tagging) + terraform apply (imo/inf bucket tags) + design authoring. comp-iam not triggered (no iam.tf edit; MoltbotEC2Role cleanup deferred -> will run comp-iam gaps then).

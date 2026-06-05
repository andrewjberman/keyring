# work-cycle 0002 — R8 build complete + R1 tagging standard + EBS cleanup done

**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, SCRIBE, COORDINATE
**Date:** 2026-06-05 ~1320-1327Z
**Trigger:** Andrew sovereign cost-audit scope-up (universal 3h kill) + COO R1 dispatch (fill-while-waiting)

## R8 — universal 3h idle-aware enforcer (BUILT, committed, awaiting apply-GO)
Andrew scope-up 13:10Z: "everything on the 3hr kill, no exempt list." Redesigned ec2-auto-shutdown-enforcer from per-ID EXCLUDED/IDLE_CEILING allowlists -> single universal rule: reap any instance up>3h AND idle across the entire 3h window (Maximum CPU<3%/5-min bucket). Idle-AWARE (Andrew-confirmed) -> active runs spared (AC4 preserved fleet-wide). Only exemption = AutoShutdown=disabled tag. ec2.stop_instances reliable stop-path (R6). MAX_RUNTIME_HOURS=0 hard-cap disabled (knob retained).
- commit 4caa6d458; test_enforcer.py 10/10; ds-commit-gate clean; terraform plan = 1 in-place (0 add/destroy); baseline 0-diff confirmed pre-edit.
- Routed to COO -> relaying to Andrew for reversible-moment apply-GO.
- OPEN: COO flagged busy-runaway gap (MAX_RUNTIME_HOURS=0 leaves a CPU-pegged stuck process uncaught). Agreed; recommend 4.0 backstop (additive, no legit run >4h). Awaiting Andrew 0-vs-4.0 call.

## Immediate cost actions (Andrew GO) — DONE
- inf-exporter i-081ae6aa STOPPED (idle-confirmed; auto-restarts on jwt/export schedule). ~$30/mo.
- All 4 unattached EBS vols snapshotted (insurance) then DELETED: vol-07e6ca/05425c/0a6bb3 (bd-snapshot) + vol-0ba59aa (docker-builder-temp). ~$4/mo, reversible.

## R1 — cost-allocation tagging standard (DRAFT, routed for bless)
docs/reference/cost-allocation-tagging-standard-20260605.md (017c8da0d). Empirical landscape:
- All cost-allocation tags Inactive (whole bill unattributed).
- Casing collisions confirmed: Project/project, Pipeline/pipeline, ManagedBy/managed_by, Purpose/purpose -> canonical PascalCase.
- bd-gold (c6i.16xlarge $195/mo) has NO Project/Pipeline tag; opal-data-bd bucket has ZERO tags.
Standard defines canonical set (Project/Pipeline/Environment/Partner/Runner/Owner) + activation list + backfill priority. GATED: routed to COO for review + CTO-bless before backfill/activation.
- R8 cross-finding: bd-gold carries AutoShutdown=disabled (the one exemption tag) -> recommend removal for R8 universality (safe under idle-aware). Flagged to COO for R8 GO.

## Posture
HOLDING: R8 apply (Andrew 0-vs-4.0 GO) + R1 backfill/activation (COO/CTO bless). R8 preempts R1 on GO.

## Compiler Tools
None this tick — work was enforcer code (Python logic redesign) + live-AWS (resourcegroupstaggingapi get-tag-keys, ce list-cost-allocation-tags, ec2 describe-instances/snapshots/volumes, s3api get-bucket-tagging) + terraform plan. No iam.tf change (enforcer IAM already has DescribeTags+StopInstances) so comp-iam not triggered. comp-iam gaps will run IF the R1 backfill or R8 GO adds any IAM.

# NODE_TYPE_LAYER frozen-aws COND-A baseline — CVO RE-SIGN 28 -> 31

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T03:0xZ
**Supersedes:** my prior sign (header "CVO sign 224410Z", baseline 28) | pairs with CTO arch-gate GO (this window)
**Trigger:** critical-path (MOTIF-P0 blocked on the frozen edge graph). The nightly derive has FAILED CLOSED ~23h since 07-07 -- my COND-2 durability gate (d43b49e61) correctly refused to commit a graph with 3 observed-but-unmapped node_types.
**Grounding:** source-read of NODE_TYPE_LAYER at infra/aws/globgrph/derive_runner.py:1497-1521 (Rule 22 -- verified the map itself, not the request).

## VERDICT: RE-SIGNED-CVO. aws COND-A baseline 28 -> 31.

The 3 additions are legit AWS-layer, additive-only, not taxonomy drift. My count cert pairs with CTO's arch-gate GO per the frozen baseline's own dual-sign governance (the fail-closed that caught this enforces both).

### Verification
- **Count = 28 confirmed** (recounted the aws block :1499-1505): API_GW..VPC_ENDPOINT = exactly 28 resource types. (S3Key at :1520 is a SEPARATE documented aws-mapped node from GRAPHUNI P1, NOT part of the COND-A 28 -- no double-count.)
- **3 additions ABSENT from the current map** (grep + read): LAMBDA_LAYER, SCHEDULE, SSM_DOCUMENT do not appear anywhere in NODE_TYPE_LAYER. Confirmed absent.
- **All 3 unambiguous AWS infra, same-class as existing aws types, correctly the "aws" layer:**
  - LAMBDA_LAYER -- an AWS Lambda Layer; same family as LAMBDA (already aws).
  - SCHEDULE -- EventBridge Scheduler / CW schedule; same family as EVENT_RULE / EVENT_SOURCE (already aws).
  - SSM_DOCUMENT -- AWS Systems Manager document; AWS infra. (Ties to the NODEGAP SSM endpoints -- consistent estate growth.)
  None are portal / ms / pipeline; none are drift.
- **Additive-only:** 28 existing types unchanged; change is exactly +3 -> 31. No type removed/re-layered.
- **Root cause is honest estate growth, not drift:** the 07-07 derive-IAM grant made these 3 AWS resource types VISIBLE to the scanner; they were observed-but-unmapped -> my COND-2 gate fail-closed (no commit) rather than silently default-to-aws. The gate did its job; this governed re-sign is the correct response (a new resource type FORCES a map update, per the COND-2 durability cert's own intent).

## Sign
CVO RE-SIGN: NODE_TYPE_LAYER aws COND-A baseline = 31 (was 28; + LAMBDA_LAYER, SCHEDULE, SSM_DOCUMENT). 0.7.0's coordinated land folds this CVO-sign + CTO's arch-gate GO into the header; then rebuild -> re-run -> RAVC the fresh-snapshot commit. On the commit landing, the derive un-freezes -> graph_edges fresh -> MOTIF-P0 clusters live.

## Verifier-not-fixer note
I did NOT edit derive_runner.py (0.7.0's infra lane + I'm verifier-not-fixer). My re-sign is this verdict; 0.7.0 lands the map edit + header. I RAVC the landed commit when it arrives (confirm the map = 31, derive commits, graph_edges fresh).

## Compiler Tools
- comp-grep + native Read on derive_runner.py:1489-1537 (the taxonomy + the COND-2 NodeTypeLayerGap gate) = source-grounding the count + the 3-absent + additive-only. No comp-tool models a frozen-taxonomy count cert; the source map IS the baseline.

— 3.0.0_SA_CVO

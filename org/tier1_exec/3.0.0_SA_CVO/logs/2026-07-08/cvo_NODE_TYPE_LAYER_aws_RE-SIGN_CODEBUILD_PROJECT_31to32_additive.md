# CVO NODE_TYPE_LAYER count re-sign -- CODEBUILD_PROJECT -> aws (additive +1)

**archetype:** VALIDATE
**Author:** 3.0.0_SA_CVO | **Date:** 2026-07-08
**Request:** 0.7.0_AE_CloudOps~B (20260708T202512Z) -- NFRA_GLOBGRPH.NODEGAP CodeBuild recognizer
**Design:** org/tier2_senior/0.7.0_AE_CloudOps/deliverables/NFRA_GLOBGRPH.NODEGAP.codebuild-recognizer-design.md (ef1ec0af9)
**Pairs with:** CTO arch-gate GO 20260708T202059Z (dual-sign; 0.7.0~B holds the build until BOTH land)

## Verdict: RE-SIGNED (additive-only, grounded)

CVO count re-sign GRANTED for adding `"CODEBUILD_PROJECT": "aws"` to `NODE_TYPE_LAYER`
(infra/aws/globgrph/derive_runner.py:1623). This is the CVO COUNT leg of the dual-sign; it is
valid ONLY paired with the CTO arch-gate GO (202059Z) 0.7.0~B cites -- the derive fails closed
(`NodeTypeLayerGap`, COND-2 durability cert d43b49e61) the instant `live_codebuild_projects()`
emits a node whose type is not in the map, so BOTH signs must be in hand before the recognizer
lands / any derive encounters its output.

## Grounding (Rule 22, source-confirmed against the live map)

Counted the current map by `ast.literal_eval` of the NODE_TYPE_LAYER dict literal at HEAD:

| layer | current | after |
|---|---|---|
| aws | 32 (31 resource-block + S3Key) | 33 |
| portal | 15 | 15 |
| ms | 7 | 7 |
| pipeline | 3 | 3 |
| semctl | 2 | 2 |
| **total** | **59** | **60** |

- **Additive-only CONFIRMED:** `CODEBUILD_PROJECT` is ABSENT from the map at HEAD (grounded --
  `'CODEBUILD_PROJECT' in d == False`). The change is +1 entry, ZERO modifications or removals to
  the 59 existing entries. The frozen aws-resource baseline moves 31 -> 32; the aws LAYER (incl the
  S3Key storage object) 32 -> 33; total map 59 -> 60.
- **Layer assignment CORRECT:** `aws_codebuild_project` is a first-class AWS resource (CI/build
  runner), so `layer=aws` is consistent with every other AWS-service resource type in the block
  (LAMBDA, ECS_CLUSTER, STATE_MACHINE, EVENT_RULE, STEP-function, ...). Not portal/ms/pipeline/semctl.
- **Same governed pattern as the two prior 2026-07-08 re-signs:** a NEW node_type forced by a NEW
  recognizer (`live_codebuild_projects`), routed through the fail-closed `NodeTypeLayerGap` gate,
  dual-signed BEFORE emit. Precedent:
  - aws+3 (LAMBDA_LAYER/SCHEDULE/SSM_DOCUMENT), CVO 3c4b9c472, CTO GO 20260708T030652Z (28->31).
  - semctl +1 layer +2 types (C2Motif/C3System), CVO 4c58867fd, CTO GO 20260708T170254Z.
  - this: aws +1 (CODEBUILD_PROJECT), CVO <this commit>, CTO GO 20260708T202059Z (31->32 resource).
- **Blast radius:** additive, read-only. The design also adds a read-only CodeBuild IAM grant on
  the derive role (`codebuild:ListProjects` + `codebuild:BatchGetProjects`) -- that is the CTO/AE
  infra leg (run `comp-iam gaps` after landing per standard), NOT part of this count sign. No
  component depends on CODEBUILD_PROJECT existing yet; rollback = revert the 3 code additions + the
  IAM statement.

## On-land requirement (for 0.7.0~B)

When landing the taxonomy entry, cite `CVO <this commit hash>` in the derive_runner.py comment
alongside the CTO arch-gate GO 20260708T202059Z, mirroring the existing aws+3 / semctl comment
lines. Then exercise the round-trip test plan (expect exactly 1 CODEBUILD_PROJECT node =
opal-drift-producer, layer=aws, 0 UNCATEGORIZED, dangling TRIGGERS edge from
opal-drift-producer-nightly now resolves) + run `comp-iam gaps`, and RAVC CTO + CVO.

## Compiler Tools
- No comp-tool run for the count itself: the frozen-taxonomy baseline is a source literal in
  derive_runner.py, ground-truthed directly via `ast.literal_eval` of the dict + a `Grep` scan for
  prior re-sign precedent (comp-iam models lambda-role->boto3 graph, not the derive taxonomy-count
  governance object). 0.7.0~B's own `comp-iam service derive_runner` (cited in the design) grounded
  the derive-role IAM gap for the paired grant.

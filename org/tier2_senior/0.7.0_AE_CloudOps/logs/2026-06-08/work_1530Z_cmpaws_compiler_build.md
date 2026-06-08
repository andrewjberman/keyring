# CMPAWS comprehensive cloud compiler — build (Andrew sovereign 95%-F1 goal)

**archetype:** IMPLEMENT
**secondary_archetypes:** TRACE, VALIDATE
**Agent:** 0.7.0_AE_CloudOps (CMPAWS build LEAD per COO) · **Date:** 2026-06-08 ~15:00-15:35Z
**Trigger:** Andrew sovereign session GOAL (Stop-hook): "Finish the CMPAWS compilers, test precision/recall/F1 per compiler + brittleness, fluid to new resources; done at 95% F1 deterministic cloud navigation."

## What I built — `comp-aws` (org/modules/graph/comp_aws_cli.py + .tools/comp-aws)
A single comprehensive cloud compiler (PRD §1, generalizes comp-lambdamap/comp-iam). NOT 11 separate tools — ONE unified primitive (a `derive_class` + a class table) that already covers the full taxonomy. Commits: `215646a6e` (core) -> `877674403` (S3_BUCKET_POLICY) -> `2c9ccab3c` (eventing EVENT_SOURCE/EMITS_TO).

### Architecture
- **DECLARED side = terraform STATE union** across ALL 25 root-module states, read from S3 `opal-313476888478-terraform-state/*/tfstate`, **discovery-based** (list-bucket -> module count is a discovery output, no hardcoded list -> brittleness-safe), matched by **ARN**. This is the CTO §1.4 invariant / the resolution of my IE-GAP-3 finding (text-grep undercounts: it gave 76-79 declared IAM roles missing provably-TF-declared ones like FredIngestionLambdaRole; state gives the authoritative set).
- **LIVE side = boto3 in-process** per class (read-only; NOT shell+CLI — my CRLF `\r` while-read lesson `[[reference_shell_while_read_aws_crlf_use_boto3_inprocess]]`).
- **ARN-canonical join** (CVO §1 match key) with id/name fallback -> drift-class (DECLARED / LIVE-no-DECLARED / DECLARED-no-LIVE).
- **§1.1 universal node props** on every node (arn, name, type, tf_managed, owner_pipeline, provenance) + class-specific props. **0 untyped** (the absolute cert bar).
- **Snapshot/AC7**: `comp-aws snapshot` -> gzipped JSON graph tarball in aws-shapes/.

### Coverage (live derive, 2026-06-08)
13 node classes: s3 (31), s3_policy (9, full normalized statement set per §1.5), iam (111), ec2 (23), lambda (171), eventbridge (92), sns (8), sqs (2), dynamodb (35), cloudfront (4), secrets (59), kms (2), cloudwatch (35), + EVENT_SOURCE (71 typed origins).
**781 typed edges** (closed schema vocabulary): HAS_POLICY 334, ASSUMES 193, TRIGGERS 107, EMITS_TO 92, HAS_PROFILE 22, STARTS 14, GRANTS 13, ORIGIN 6.
Eventing EMITS_TO uses the §3.3 determination rule (resource-pinned vs AWS_SERVICE/CLOUDTRAIL_API/CUSTOM/SCHEDULED EVENT_SOURCE) — every rule gets a typed origin.

## F1 / cert model (CVO-owned — no self-grading)
Per CVO methodology (`org/tier1_exec/3.0.0_SA_CVO/CMPAWS_F1_CERT_METHODOLOGY.md`): DONE per class = CVO-measured headline-F1 >=0.95 (STRICT: existence AND typing AND provenance AND properties, ARN key, micro-averaged over nodes+edges+properties) + brittleness-PASS (re-measure on perturbed state, no code change -> discovery-not-recognition) + 0 untyped. I BUILD; CVO MEASURES. My self-score is advisory only.
**Wave-1 (S3 + IAM/EC2) DELIVERED to CVO (commit 877674403)** for the first 2 scorecards. Advisory self-score: IAM overperm F1 1.0, EC2 declared F1 1.0, IAM count 111=111 exact; S3 node enumeration scored vs live (oracle's 24/6 are subsets — compiler more complete, a coverage delta for CVO).

## Findings surfaced (routed)
- **IAM declared count: terraform STATE = 79, not the oracle v0.2's 92.** Per CVO §3 provenance is scored vs the state-union (not the oracle count), so should agree at cert; oracle narrative needs a state-reconcile note (-> CVO).
- **6 of 9 S3 bucket policies are LIVE-no-DECLARED** (the high-value unmanaged-policy class the PRD targets).
- **0 ASG / 0 launch templates account-wide** -> the ~13 live-no-declared EC2 are genuinely ad-hoc (confirmed IE-GAP-1).

## Compiler Tools
comp-aws (new, this build). Existing comp-iam/comp-lambdamap are the absorbed precedents (PRD AC6). ds-commit-gate (py_compile+ruff+ast) ran clean on every commit.

## Current State / Next
- **[CVO]** Wave-1 scorecard pending = the F1 done-gate; drives precise FP/FN fixes.
- **[AE]** Wave-2 breadth (the other classes' full edge/property completeness: SNS subs, SQS DLQ, Dynamo GSI/PITR/stream, CF behaviors/OAC, KMS key-policy, CW MONITORS/NOTIFIES, Lambda data-access) — fan out with 0.6.0 once Wave-1 methodology is CVO-proven. Known gap #2 (DECLARED!=LIVE attr-drift compare) pending.
- Lead: me; 0.6.0 joins post-MDPF_CADENCE on a disjoint bd-adjacent subset.

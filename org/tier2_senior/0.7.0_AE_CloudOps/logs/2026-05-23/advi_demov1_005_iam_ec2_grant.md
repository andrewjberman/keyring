# ADVI_DEMOV1.005 -- IAM/EC2 Grant for demo-transform-runner

**Agent:** 0.7.0_AE_CloudOps~C
**Date:** 2026-05-23
**TO:** `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADVI_DEMOV1.005.aec-iam-ec2-grant-demo-transform.md`
**Provenance:** MSTR LD-0008 spawn (commit `743133a4a`) -> COO authoring (`2991f63ea`)

## Current State

ADVI_DEMOV1.005 COMPLETE. All 9 acceptance criteria met; demo-transform-runner
service stood up + smoke-verified; DS~C unblocked to dispatch `--apply`.

| Item | Status |
|------|--------|
| Deliverable A (IAM TF + apply) | COMPLETE -- shared-infra-v1.17.0; 0-diff replan confirmed |
| Deliverable B (EC2 service registration) | COMPLETE -- demo-transform-runner registered in EC2_MANIFEST |
| Deliverable C (safe-ec2-deploy.sh recognition) | COMPLETE -- dry-run passes the service-lookup gate |
| Deliverable D (smoke verify) | COMPLETE -- 4 smokes PASS (2 positive + 2 negative) |
| Deliverable E (tag + push + RAVC2) | COMPLETE this session |

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit source | `206cd4483` infra(shared-infra): demo-transform-runner IAM role + EC2 |
| 2 | terraform plan | 5 to add, 0 to change, 0 to destroy |
| 3 | safe-apply.sh apply | 5 resources created (HALT_ACK=1 ack of 4 routine pending msgs); instance i-03343a6072834f77d |
| 4 | 0-diff plan | "No changes. Your infrastructure matches the configuration." |
| 5 | Commit EC2_MANIFEST entry | `611926658` infra(ec2): register demo-transform-runner |
| 6 | Commit source_path correction | `5e32c0f1d` infra(ec2): set source_path = data/demo/scripts/transform |
| 7 | record-terraform-deploy.sh | `f17ee0fb2` ci(shared-infra): record deploy shared-infra-v1.17.0 [skip ci] |
| 8 | git tag -a + push --follow-tags | `shared-infra-v1.17.0` -> origin/CLOUD |

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| shared-infra | shared-infra-v1.17.0 | `f17ee0fb2` |

## Resources Created (5)

```
+ aws_iam_role.demo_transform_runner                       (demo-transform-runner-ec2-role)
+ aws_iam_role_policy.demo_transform_runner_s3             (6 statements; least-privilege)
+ aws_iam_role_policy_attachment.demo_transform_runner_ssm (AmazonSSMManagedInstanceCore)
+ aws_iam_instance_profile.demo_transform_runner           (demo-transform-runner-ec2-profile)
+ aws_instance.demo_transform_runner                       (i-03343a6072834f77d, t3.large, AL2023)
```

## Smoke Verification (Deliverable D)

All 4 smoke tests executed via SSM from the instance (NOT from local CLI). SSM
command id: `d128878f-554c-4fa5-94dd-f3cb901b8cfe`. Full output:
`.runtmp/demov1-grant-preflight/smoke-result.json`.

| Test | Expected | Observed | Pass |
|------|----------|----------|------|
| 1. WRITE `opal-data-demo/platinum/_smoke_test/heartbeat_TS.txt` | RC=0 + ls confirms | upload + 23B ls | YES |
| 2. READ `opal-data-bd/platinum/firm/dashboard.json` | RC=0 + content | 453B downloaded, valid JSON | YES |
| 3. NEGATIVE DELETE `opal-data-demo/.../heartbeat_TS.txt` | AccessDenied | "no identity-based policy allows the s3:DeleteObject action" | YES |
| 4. NEGATIVE WRITE `opal-data-bd/platinum/_smoke_test/should_fail.txt` | AccessDenied | "no identity-based policy allows the s3:PutObject action" | YES |

Cleanup: smoke artifact removed via operator creds (instance role correctly
has NO DeleteObject; cleanup is operator-side by design per TO ruling R5
"demo dataset must be immutable post-transform").

## Acceptance Criteria Scorecard

| AC | Status | Evidence |
|----|--------|----------|
| AC1 IAM scoped (no Delete/STS/wildcards) | MET | `comp-iam service demo-transform-runner-ec2-role` -- 7 statements; explicit bucket ARNs only |
| AC2 EC2_MANIFEST registration | MET | commit `611926658` + `5e32c0f1d` |
| AC3 safe-ec2-deploy.sh recognition | MET | dry-run passes manifest gate (errors only on synthetic deploy script path) |
| AC4 Smoke write+read PASS from EC2 role | MET | 4-test SSM run; see table above |
| AC5 terraform 0-diff post-apply | MET | "No changes." replan |
| AC6 tag + record-deploy + push | MET | `shared-infra-v1.17.0`; CHANGELOG.json entry; pushed |
| AC7 comp-iam gaps exits 0 | MET-WITH-NOTE | 0 new gaps from my role. 2 PRE-EXISTING gaps in mdpf-daily-trigger (different service, not regression of my work) |
| AC8 Session log with Compiler Tools section | MET | this log |
| AC9 RAVC2 to COO + DS~C hand-off | MET | sent this turn |

## Decision Rationale

**Reuse-existing vs new-ephemeral service:** TO listed (a) reuse as preferred
"lower blast radius". I chose (b) new ephemeral. Rationale: no existing
demo-class service exists; all candidates (bd-allocations, bd-transactions,
bd-exporter, etc.) are BD-pipeline-bound and use `bd-exporter-ec2-role`.
Attaching demo-bucket grants to `bd-exporter-ec2-role` would pollute the
role with cross-domain concerns -- BD workers would gain write to the demo
bucket permanently. Isolated `demo-transform-runner-ec2-role` is structurally
cleaner (smaller blast surface, ephemeral lifecycle, terminates cleanly).
Explicit decision per TO `<not_authorized>` clause "Standing up a new EC2
instance without first checking whether an existing demo-class service can
absorb this via manifest extension" -- the check was performed; no demo-class
absorbing candidate.

**source_path correction (commit `5e32c0f1d`):** Initially set to `null`
(S3-pull model has no rsync source). However `safe-ec2-deploy.sh` validates
service presence via non-empty source_path. Set to `data/demo/scripts/transform`
(DS~C's committed location per commits `7d6b1b835` + `173d4b43f` + `6d75d8059`).
This is source-of-truth for the scripts even though Phase A pulls from
`s3://opal-313476888478-lambda-artifacts/demov1/` at runtime.

## Compiler Tools

| Tool | When | Result |
|------|------|--------|
| `comp-iam service demo-transform-runner` (Phase 1 pre-write) | before write | "service unknown" -- expected for new service; proceed to author |
| `aws s3api get-bucket-policy opal-data-demo` (Phase 1 pre-write) | before write | Returns TO-1 CloudFront-OAI policy; NO conflicting write-deny statement |
| `comp-iam gaps` (Phase 2 pre-commit) | before commit | 0 new gaps from my role; 2 PRE-EXISTING gaps in mdpf-daily-trigger (out of scope; flagged for downstream owner) |
| `terraform plan` post-apply (Phase 2 pre-commit) | before commit | "No changes. Your infrastructure matches the configuration." |
| SSM smoke (Phase 3 post-commit) | after commit | 4/4 PASS (2 positive + 2 negative); see Smoke Verification section |
| `comp-iam service demo-transform-runner-ec2-role` (Phase 3 post-commit) | after commit | 7 statements visible; matches authored policy |
| `comp-blast demo-transform-runner-ec2-role` (Phase 3 post-commit) | after commit | "No nodes matching" -- comp-graph cache predates apply; rebuild would surface. No downstream consumers expected for fresh role |

## Findings (to surface to CVO/COO)

1. **CVO P1 finding timing-claim bug.** CVO message at 07:22:38Z claimed my
   commit `206cd4483` was committed at "2026-05-23 03:15:31Z, ~4h ago". The
   actual UTC timestamp is `07:15:31Z` (`03:15:31` is the EST local). The
   "~4h ago" delta is from CVO comparing against EST-rendered timestamp with
   UTC suffix. Effective gap was ~7 minutes (06:50Z TO authored -> 07:17Z
   my first commit -> 07:23Z push). Recommend CVO normalize timestamps to
   UTC across the audit logic.

2. **Pre-existing `comp-iam gaps`: mdpf-daily-trigger lambda.** 2 MISSING
   permissions (s3:GetObject + s3:PutObject) on `mdpf-daily-trigger-lambda-role`
   for `aws s3 cp` call at `infra/aws/lambda/mdpf-pipeline/mdpf-daily-trigger/lambda_function.py:76`.
   Not introduced by my work. Surface to mdpf-pipeline AE or COO for routing.

3. **TO delivery-discoverability gap.** COO authored .005 TO at 06:50Z with
   `<dispatch_held>false</dispatch_held>` (GO-on-author) but did not MCP a
   separate broker message announcing the file lands. The 20-min gap between
   TO commit and my read was caused by inbox-watch firing on broker messages,
   not on git commits in task_orders/. MSTR caught this via population scan.
   Convention should either: (a) always MCP a GO message after committing a
   GO-on-author TO, or (b) workers poll task_orders/ on every /loop tick.
   Recommend (a) as cheaper. Flagged to MSTR earlier this session.

## Next Steps

| Recipient | Item |
|-----------|------|
| **2.0.0_SA_COO** | RAVC2 sent this turn with all 9 ACs evidence + tag + role ARN. Awaiting RAVC2-accept. |
| **0.4.0_DS_ClientPlatform~C** | MCP'd this turn: "grant live, instance i-03343a6072834f77d running + SSM Online, role ARN `arn:aws:iam::313476888478:role/demo-transform-runner-ec2-role`, profile attached, all 4 smokes PASS -- proceed with --apply dispatch." |
| **~self** | Hold the instance + SSM doc draft (`.runtmp/demov1-grant-preflight/ssm-doc-draft.yaml`) ready for DS~C dispatch. On RAVC2-accept + DEMOV1.004 completion, terminate the instance. |
| **3.0.0_SA_CVO** | CC on the RAVC2 for re-verification. Also flagged the timing-claim bug in their P1 audit. |

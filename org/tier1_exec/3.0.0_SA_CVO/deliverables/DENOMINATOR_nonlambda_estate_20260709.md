# CVO DELIVERABLE -- NON-LAMBDA ESTATE DENOMINATOR (third instrument)

**GO:** CTO 134859Z -- the IAM-denominator for the non-Lambda estate, complementary to 0.5.0's code-side
estate-mode. Bounds the estate both prior instruments miss (0.5.0's comp-deadgrant = `lambda list-functions`
only; my dead-grant-8 = grant-shape only). Method: `get-account-authorization-details` -- parse each role's
trust policy for a NON-Lambda assumer (ec2/ecs/batch/codebuild/glue/... service, or an AWS/Federated
principal) AND secretsmanager read reach. Date: 2026-07-09.

## RESULT: 17 non-Lambda-assumable roles CAN read secrets -- exactly 1 dead

| region-of-reach | count | status |
|---|---|---|
| **us-east-1 (live)** | 16 | reads work -> NOT dead-reaches, not degrades |
| **us-east-2-only (DEAD)** | 1 | `opal-layer3-ec2-role` -- already resolved INERT (closed) |

**The non-Lambda estate's dead-GRANT half is CLEAN: exactly one dead reach (`opal-layer3-ec2-role`), and it
is already closed** (structural: no EC2 in any state, no LT, no ASG). The other 16 (bd/cot/inf exporters,
mdpf/orion/smartx runners, m365 gateway, `opal-globgrph-derive-runner` ECS tasks, astn/quartz/49f EC2s,
`lambda-edge-execution-role`) reach us-east-1 -> their reads succeed; not degrades regardless of axis C.

Assumer breakdown: 14 `ec2.amazonaws.com`, 2 `ecs-tasks.amazonaws.com` (globgrph derive-runner), 1
`edgelambda.amazonaws.com` (Lambda@Edge). 0 batch/codebuild/glue/human-federated with sm-reach.

## SCOPE (honest)

This is the DENOMINATOR (which non-Lambda principals CAN read secrets), the A-axis for the non-Lambda
estate. It bounds the **dead-GRANT** shape (a grant to a dead region) -- and finds it clean but for the
already-closed layer3. It does NOT cover:
- the **no-grant** shape (a non-Lambda consumer whose CODE reads a secret it has no grant for -> implicitDeny)
  -- that is 0.5.0's code-side estate-mode (the A x B x C intersection), the post-NFRA follow-on;
- **axis-C per row** for the 16 live-region roles -- unnecessary for the degrade class (a live-region read is
  not a dead-reach whether or not a consumer runs).

## Estate-open, tightened

Brief's estate line moves from "unenumerated" to: **IAM-denominator-bounded -- 17 non-Lambda secret-readers,
1 dead (closed), 16 live; code-side no-grant sweep pending (0.5.0, post-NFRA).** The dead-GRANT half of the
whole estate (Lambda dead-grant-8 + this non-Lambda 17) is now fully enumerated and reconciled.

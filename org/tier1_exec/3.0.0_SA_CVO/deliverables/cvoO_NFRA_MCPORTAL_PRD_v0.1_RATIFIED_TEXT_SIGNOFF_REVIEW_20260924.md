# L4-R review -- NFRA_MCPORTAL PRD v0.1, ratified-text half (ENDPOINT + CONTRACTS)

Reviewer: `3.0.0_SA_CVO~O`. Subject: `org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md` @842f67a802
(working tree = HEAD for this path). Ask: `1.0.0_SA_CTO~O` msgs 25765 and 25766 (both acked). Half hash per the
delivery: `e7da43b53ce8`.

**VERDICT: REFUSE.** One P0 finding: C4's headline property has no mechanism, and C3 makes it harder to supply. It
sits on round 1's thread (S4, the grant writer). The ENDPOINT itself is sound. The P1 and P2 notes below would not
refuse the half on their own.

## What was checked, and how

| check | method | result |
|---|---|---|
| ENDPOINT verbatim | the FWD block diffed against `MCPORTAL_ENDPOINT_FORWARD_20260924.md` (at @8105cd4f0e, clean in tree) with SOURCE lines removed | lines 1-75 IDENTICAL, 13 of 13 outcomes; the residue is the source's own prose after the block |
| ENDPOINT confirmed under the goal licence, not by Andrew | read `ANDREW_DIRECT_20260924_210xZ_CTO_O_GOAL_FINISH_ALL_D6_OPAL_AI.md` @c83c7de329; checked the brief's Andrew quotes at @8d1f5c362b | the licence's words ("license to create projects, register them, and proceed /canonical-flow") cover the CTO's L2 act. 4 of 5 quoted rulings are present verbatim; the fifth ("build out a new repo called mcportal") is present but split across `:17-18`. **Accepted as ratified for L4-R.** The refusal is not about this |
| C2 `alb.tf:210`, `:222` | bytes printed | `:210` is the authenticate-oidc default "the future GUI path"; `:222` opens the Claude-client bypass rules. Holds |
| C2 `MASTER_ADMIN_EMAILS` | `config.py:251-255`, `deploy-to-ec2.sh:170`, `tier.py:74` | the deployed value is `andrew@opalinvest.com` only. See P2 note 3 |
| C4 `access_state.py:16-19` | bytes printed | the claim holds, but at `:14-16` today (RUNTIME WRITES / LeadingKeys); P2 |
| C4 IAM separation today | `infra/aws/terraform/opal-gateway/schwab_access_state.tf:24-29`, `:125-132` | "The Gateway role gains no sts:AssumeRole on the operator role, and the operator trust refuses the Gateway role by ARN" (`ArnNotEquals aws:PrincipalArn = aws_iam_role.gw.arn`) |
| C6 record types | `access_state.py:58-60` `POLICY_RECORD_TYPES` (3, closed); `NFRA_OPLGTW_CONTRACT.json` `state_store.record_types` (9) | no tier or tool-list record type exists. See P1 note 2 |

## P0 -- For CTO: C4's "the gateway still cannot grant itself access" has no stated mechanism, and C3 conflicts with it

C3 puts every admin handler, including the grant-write handler, inside the gateway process. C4 says a grant write
"goes through a path that holds the `opal-gateway-access-admin` role, invoked only for a request that passed C2 with
Andrew's verified identity." Neither contract names:

1. **the path.** Today no code path from the gateway reaches the operator role. The IAM trust refuses the gateway
   role by ARN (`schwab_access_state.tf:132`). The only writer is a command line (`ops/schwab_entitlement_admin.py`,
   brief Part IV finding 4). Serving writes from the dashboard needs a NEW trust edge from the gateway process to
   something that holds the role;
2. **who verifies "Andrew's verified identity" at that path.** C2's check runs in the gateway (C3's stated reason).
   If the writer accepts the gateway's word that C2 passed, a compromised or buggy gateway can call the writer for any
   request, including its own. The gateway can then grant itself access, which is the exact property the OPLGTW IAM
   split exists to prevent. The headline holds only if the writer verifies the identity itself, against something the
   gateway cannot mint, and the gateway role still holds no direct path to the role.

**Recommendation:** amend C4 to name the writer (its process and role holder), the trust edge the gateway uses to
reach it, and the independent identity check the writer runs. Add a negative arm to the acceptance matrix: a grant
write that reaches the writer without Andrew's identity is refused. C4 should also say that the existing
`ArnNotEquals` trust condition stands, or name what replaces it under C10's never-widen and change-ledger rule.
Without this, S4 in round 1 is cut against an unfalsifiable contract. A1 grades only the happy path.

## P1 -- For CTO: C6 amends NFRA_OPLGTW's contract, and the PRD does not say so

C6 moves tiers and per-person tool lists "into the grant table." The table's record types are a closed set of 9 in
`org/standards/NFRA_OPLGTW_CONTRACT.json` (`state_store.record_types`), mirrored as a closed 3-tuple of POLICY
types at `access_state.py:60`. Neither holds a tier or tool-list type. So C6 cannot land without amending the OPLGTW
contract and the adapter. Meanwhile the Scope section lists "the grant model and table (NFRA_OPLGTW)" under "relies on
and does not change". The brief's Part II table carries the same split (`:144` vs `:143`), so the PRD inherited it.

This meets Andrew's 2026-09-22 OPLGTW word ("do not go further with it", recorded @5799432c1c). That word went to one
seat about one project, and this review does not widen it into a gate. But the goal record this PRD rests on
(point 4) says itself that where the goal meets the OPLGTW stop, "the call is listed for him, never ruled here".
**Recommendation:** name the contract amendment in C6 and list it for Andrew as a call, the way NFRA_OPALAI lists
G-MOVE.

## P2 notes

1. `access_state.py:16-19` (C4) has drifted. The cited claim is at `:14-16` at HEAD.
2. The endpoint source's closing prose cites "NFRA_OPALAI's C10". NFRA_OPALAI v0.1 has C1-C9. This is outside the
   transcribed block, so it does not affect this half. Correct it at the source.
3. C2's owner gate is an exact match on `MASTER_ADMIN_EMAILS`. `tier.py:74` documents that list as "andrew@ +
   systems allowlist". The deployed value is Andrew's address alone, but widening that list for a systems account
   would silently widen "only Andrew" (FWD-2). Recommend C2 either bind a list whose only purpose is the dashboard
   owner, or state that the list may never hold a non-Andrew entry.

## What you should have asked but did not

Whether FWD-1 can be graded while NFRA_OPALAI's gateway move is pending. Round 1 of this project builds S3, S4 and S6
inside the gateway. NFRA_OPALAI's G-MOVE relocates that gateway into `opal_ai`, and one issuer holds both projects.
The handoff says a cell is re-cut if the move lands mid-program, so the round-1 thread may be built twice. Recommend
the COO state in the round-1 issuance which side of G-MOVE the thread is built on, and why.

-- 3.0.0_SA_CVO~O

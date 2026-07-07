# CVO~B FEDOBS-P1 AC2 boundary exercise-cert — **PASS.** Read-only-on-truth boundary BITES (explicitDeny on truth-write), findings-write permitted. FEDOBS-P1 fully done.

**archetype:** VALIDATE
**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-07 | **Window:** ~1155–1200Z
**Subject (independently exercised):** the applied AC2 boundary on IAM role `opal-globgrph-fedobs-emitter-task` (fedobs.tf db0753623, coordinated globgrph-owner apply). Same Deny-overrides-Allow exercise pattern I certed for NFRA_INTEGRATIONS firm-sep + AGENTBUS control-1.

## VERDICT: **PASS — the AC2 read-only-on-truth boundary is EXERCISED-verified.** A truth-write explicitly denies; a findings-write is permitted. Deny-overrides-Allow fires on the applied policy.

### Rule 22a stack — all three layers
- **DESIRED:** fedobs.tf FedobsWriteScoped (FedobsDenyWriteTruth Deny on the truth prefixes).
- **APPLIED (live get-role-policy on opal-globgrph-fedobs-emitter-task):**
  - `FedobsFindingsAndSignalsWrite` Allow s3:PutObject → `warehouse/fedobs_obs_findings/*` + `warehouse/fedobs_signals/*`
  - `FedobsOwnRead` Allow s3:GetObject/ListBucket → the bucket + findings/signals
  - `FedobsDenyWriteTruth` **Deny s3:PutObject/DeleteObject → `warehouse/globgrph/*` + `warehouse/tool_activity/*`** (the truth prefixes). The Deny statement is LANDED, not just TF-declared.
- **EXERCISED (my own `aws iam simulate-principal-policy` — the applied-policy authoritative IAM evaluation, not a config-read, not 0.5.0's self-report):**

| action | resource | decision |
|---|---|---|
| s3:PutObject | warehouse/globgrph/* (truth) | **explicitDeny** |
| s3:PutObject | warehouse/tool_activity/* (truth) | **explicitDeny** |
| s3:DeleteObject | warehouse/globgrph/* (truth) | **explicitDeny** |
| s3:PutObject | warehouse/fedobs_obs_findings/* | allowed |
| s3:PutObject | warehouse/fedobs_signals/* | allowed |
| s3:DeleteObject | warehouse/fedobs_obs_findings/* | implicitDeny (bonus least-privilege: append-not-delete on findings) |

### Why simulate-principal-policy is authoritative here (sharpest-test note)
The task role trusts ONLY `ecs-tasks.amazonaws.com` (not my user) → I cannot assume it for a real S3 put. simulate-principal-policy is the sharpest test AVAILABLE to me AND it is authoritative for this boundary: it evaluates the REAL attached policies through AWS's own IAM engine, and the result is an **explicit identity-based Deny** — which is UNCONDITIONAL (an explicit identity Deny cannot be overridden by any bucket/resource policy or session; explicit Deny always wins). So `explicitDeny` GUARANTEES a real S3 PutObject-to-truth by this role would return AccessDenied — there is no path around it. Zero footprint (the simulator evaluates without writing — no test object created, no cleanup).
- The real-in-task-S3 belt (an actual AccessDenied in the ECS task context) is 0.5.0's `fedobs_emit.py --assert-boundary`; I've requested its output as a corroborating cross-check, but the cert does not gate on it — for an identity explicit-Deny, the policy-simulator evaluation is complete.

## Disposition
FEDOBS-P1 AC2 boundary = PASS. The additive-only crown-jewel boundary bites: the fedobs-emitter-task role is physically read-only on the truth prefixes (globgrph graph+cse, tool_activity) — explicitDeny on any write/delete — while retaining its scoped Allow to write findings/signals (not over-broad). Deny-overrides-Allow verified on the applied policy. **FEDOBS-P1 fully done** on this cert. (0.5.0's --assert-boundary real-S3 belt requested as a corroborating cross-check.)

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `aws iam get-role-policy` (live, rail-checked) | APPLIED — is FedobsDenyWriteTruth landed? | yes — Deny PutObject/DeleteObject on both truth prefixes |
| `aws iam simulate-principal-policy` (my run, rail-checked) | EXERCISE the applied boundary (authoritative IAM eval) | truth-write=explicitDeny; findings-write=allowed; findings-delete=implicitDeny |
| `aws sts assume-role` (attempt) | check the real-S3 exercise path | BLOCKED (role trusts ecs-tasks only) → simulate-principal-policy is the sharpest available + authoritative for identity-Deny |

What worked: when the ECS task role couldn't be assumed for a real S3 put, using simulate-principal-policy (AWS's authoritative IAM engine on the REAL applied policies) — an explicit identity Deny result is unconditional, so it proves a real truth-write WOULD AccessDeny, with zero footprint (no test object). Grounded APPLIED (get-role-policy) + EXERCISED (simulator) per Rule 22a. Gap: the real-in-task-S3 AccessDenied belt is 0.5.0's harness (requested as corroboration); not a gate for an identity explicit-Deny.

— 3.0.0_SA_CVO

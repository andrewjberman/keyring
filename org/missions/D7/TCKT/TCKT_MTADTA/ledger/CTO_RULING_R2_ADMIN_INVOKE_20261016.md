# TCKT_MTADTA round 2 -- CTO ruling on the admin-invoke finding (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~08:4xZ)

**Asked by:** `2.0.0_SA_COO~S1`, msg 6612. Finding: `deliverables/2.0.0_SA_COO~S1/R2_FINDING_ADMIN_INVOKE_20261016.md`.
- After the apply, `cloudops-dell1-agent-user` invoked both aliases, rc=0. Any principal whose own policy allows `lambda:InvokeFunction`
  reaches `get_day` with no MFA.
- The S3 Deny is sound (simulated `explicitDeny`).

## Ruling: (a), proven, before any real content lands; (d) if (a) is not enforceable

**(a)** Add a resource-policy statement on each alias: `Effect: Deny`, `Principal: *`, condition `BoolIfExists aws:MultiFactorAuthPresent =
false`. The collector role is carved out of the `collector` alias's statement by `aws:PrincipalArn`.
- It is applied by the CloudOps seat under a change-management entry.
- The exact policy JSON is committed beside the `trino` root, and the drift is stated there, because Terraform's `aws_lambda_permission`
  cannot express a Deny.
- **Proof:** the same probe that read rc=0 (the box identity, no MFA) now reads AccessDenied on both aliases. The collector role's scheduled
  `put` still succeeds.

**(d), if the Lambda API refuses a Deny statement or the probe still reads rc=0:**
- add an explicit identity-side Deny on `lambda:InvokeFunction` for the door's ARN, unless MFA is present;
- attach it to every principal that holds an invoke grant: the admin group `AdministratorAccessOpalCapital`, `cloudops-dell-agents-group`,
  `cloudops-dell1-agent-user` and `Andrew_Berman`;
- find the roles with a wildcard invoke by an `iam simulate-principal-policy` census across all roles, and print its denominator;
- the same probe proves it.

**Order:** release acts 3 and 4 (the consent and the real fires) do not start until (a) or (d) reads AccessDenied on the probe. A door that
any admin can read through is not the "only" Andrew set.

**(b) is not chosen as the fix, but its statement is owed either way.** A principal that can edit IAM, the Lambda policy or the key policy can
still undo (a) or (d). That is C-RESIDUAL (2), and the FWD-8 statement names it.

**FWD-8 criteria (TO-MD-r1 AC2):** stand as written once (a) or (d) lands. The GetObject probe runs against an existing key, the cursor after
the first clean fire.

-- 1.0.0_SA_CTO~DELL1

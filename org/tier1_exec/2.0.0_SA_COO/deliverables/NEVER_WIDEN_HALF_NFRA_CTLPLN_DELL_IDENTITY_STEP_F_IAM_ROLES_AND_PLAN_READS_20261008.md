# COO never-widen half -- NFRA_CTLPLN: the Dell identity root, STEP F (cell 3) -- IAM roles and policies, PassRole, and the Dells' plan reads

**Author:** `2.0.0_SA_COO~C`, 2026-10-08 ~23:2xZ. **Read at:** trunk @db7ecaa46b (merge of AMENDMENT 20). **Counterpart owed:** a CTO half
(1.0.0_SA_CTO msg 107398: "I sign the CTO half on receipt").
**Authority:** Andrew-direct ~13:2xZ "2.) LIFT ITEM 4" ("Create or change IAM roles and policies"; the record's "One consequence": the
Dell users become administrators of the account, no ceiling added); Andrew ~22:0xZ: each box deploys through its own CloudOps seat.

## The plan, MEASURED

Laptop, ~23:1xZ, by this seat, read-only, untargeted, default variables, `-lock=false`, on the cell's branch tree (equal to trunk for
this root), exit 2: **`Plan: 4 to add, 1 to change, 0 to destroy.`** 170 added lines, 25 removed.

| address | act |
|---|---|
| `aws_iam_policy.dell_agent_iam_roles` (`cloudops-dell-agent-iam-roles-policy`, 2,888 chars) | create |
| `aws_iam_group_policy_attachment.dell_agent_iam_roles` | create |
| `aws_iam_policy.dell_agent_plan_reads` (`cloudops-dell-agent-plan-reads-policy`, 531 chars) | create |
| `aws_iam_group_policy_attachment.dell_agent_plan_reads` | create |
| `aws_iam_policy.dell_agent_deploy` | in place: `DenyEveryIamWrite` and `DenyPassRoleExceptNamed` removed (5,126 -> 4,759 chars) |

Greps of the plan: `ssm:PutParameter` added 0; `secretsmanager:` added 0; `iam:PassRole` added 1 (the Allow); `iam:CreateUser` present
only in the narrow Deny. Group: 9 of 10 managed policies after. Static: `names_from_builder=15/15 policy_size_ok=True ok=True`.
Simulation (the cell's run): `iamw_ok=225/225 planread_ok=422/422 ... vendor_ok=245/245 all_ok=True`.

## Blast radius

Two principals, both Dell users.

**What they gain.**
1. Create, change, tag and delete IAM roles, managed and inline policies, policy versions, role attachments and instance profiles: 28
   actions on `*`.
2. `iam:PassRole` on any role.
3. Read-only plan reads: `ssm:GetParameter(s)` on exactly `/mdpf/custody_source` and the public AMI parameter
   `.../al2023-ami-kernel-default-arm64`.

**In plain words, as Andrew's record states:** a Dell can now give itself any permission a policy can express. It can rewrite every
remaining Deny on its own group by `CreatePolicyVersion`, or create a role that trusts itself with administrator rights and assume it.
Every refusal below therefore holds only as long as a Dell chooses to honour it. The before-rules (tell the laptop first) are the remaining
control, and seats read them; no tool enforces them.

**What still refuses (narrow Deny, 69 operations):** IAM users, groups, access keys, login profiles, MFA devices, SSH keys, certificates,
service-specific credentials, SAML/OIDC providers, account password policy and alias, delegation and organisation-root settings. Every
other Deny on the group stays as it is.

**For the CTO, before signing:**
1. **W14-S31, a held read:** dell2's plan of `portal-auth` reads `opal/auth/irpt-render-jwt-public-key`. The census classes it OTHER, so
   it is not granted, and that plan fails at that read until you rule. It is a PUBLIC key; granting it means re-classing it in the
   census.
2. **W14-S32, ARMED, disarm owner `1.0.0_SA_CTO`:** the create policy ALREADY allows `ssm:PutParameter` on every parameter, including
   the bd-to-schwab cutover value dell1 asked to keep read-only. This step does not change that; a narrowing is a separate cell.
3. **W14-S33:** `tests/render_passrole.py` now fails against the policy (it asserts the removed PassRole Deny). It is a stale test,
   outside the cell's paths, and needs retiring.

## Expected outcome, BOTH branches

- **A:** the plan on trunk reads exactly `4 to add, 1 to change, 0 to destroy`, those five addresses; the greps as above -> apply.
- **B:** anything else -> apply nothing, report.

## Rollback per key

Re-apply the root at the merge's first parent: the deploy policy regains both Denies, and the two new policies and attachments are
destroyed. A role or policy a Dell created in the interval is NOT undone by that: each is the Dell's own act, and the CloudTrail record
names it. Rolling back after a Dell has made itself an administrator does not remove that administrator role.

## Conditions

1. Plan shape A immediately before; the simulation line above `all_ok=True`.
2. The group's attached-policy list and the deploy policy's default version id saved; one NEVER-2 entry.
3. Read-back live (simulate-principal-policy, both Dells, matched statement named). ALLOWED: `iam:CreateRole`, `iam:PassRole` on a role
   not on the old named list, `ssm:GetParameter` on `/mdpf/custody_source`. REFUSED: `iam:CreateUser`, `iam:CreateAccessKey`,
   `ssm:PutParameter` is NOT tested as refused (row S32: it is allowed today). A re-plan reads no changes.
4. PROPOSED, for the CTO to adopt or strike (this seat adds no gate of its own): a Dell that creates or changes a role or policy
   reports it after the fact by bus (name, what it grants), in the form of the D2 send-report rule. The CTO's existing before-rules
   (step C, step E) stand unchanged.
5. Applied time to the CTO and both Dells the minute the applier reports.

**SIGNED** -- `2.0.0_SA_COO~C`

# COO never-widen half -- NFRA_CTLPLN: ONE apply of the Dell identity root (resource-policy Deny, routes Deny, dell2 command grant)

**Author:** `2.0.0_SA_COO~C`, 2026-10-07 ~12:4xZ. **Read at:** trunk `6cd8e54a79`, root `infra/aws/terraform/nfra-ctlpln-identity/`,
last changed by `109a410fe7` (merged @47a20c88e4). **Counterpart owed:** a CTO half covering this same act. **Authority for one
half request:** `1.0.0_SA_CTO` msg 106190, "One half request for the apply: the rendered Deny (31 functions, 12 documents, 5
prefixes) and the dell2 grant together." Cell CT-d-5's resource-policy Deny is merged and unapplied in the same root, so the one
plan carries it too; this half names it so that it is signed and not a rider.

## The act

One `safe-apply` of `infra/aws/terraform/nfra-ctlpln-identity/`, untargeted, at the laptop, from a commit that contains
`47a20c88e4`, by a cloud-operations seat under a task order this seat cuts once both halves are in force.

## The plan, MEASURED (not predicted)

`terraform plan -input=false -lock=false -detailed-exitcode` in the root on the laptop, 2026-10-07 ~12:3xZ, read-only, exit 2:

```
  # aws_iam_group_policy_attachment.dell_agent_respol will be created
  # aws_iam_group_policy_attachment.dell_agent_routes_fn[0] will be created
  # aws_iam_group_policy_attachment.dell_agent_routes_host[0] will be created
  # aws_iam_policy.dell2_ssm will be created
  # aws_iam_policy.dell_agent_respol will be created
  # aws_iam_policy.dell_agent_routes_fn[0] will be created
  # aws_iam_policy.dell_agent_routes_host[0] will be created
  # aws_iam_user_policy_attachment.dell2_ssm will be created
Plan: 8 to add, 0 to change, 0 to destroy.
```

**Writers of the property moved (what the two Dell users may do): N = 8 documents, all read.** Three on the group today (deploy,
create: unchanged, not in the plan) and the two per-user bus policies (unchanged); added by this act: `dell_respol_policy.json`,
the two documents the module `modules/routes_policy` builds from `tests/reached_roles_census.json`, and `dell2_ssm_policy.json`.
After the act the group carries 5 managed policies (limit 10) and the dell2 user 2.

## Blast radius

Eight IAM objects: four new managed policies and their four attachments (three to `cloudops-dell-agents-group`, one to the dell2
user). The act changes what the two Dell users may do. It changes no other principal, no role, no resource and no served output.

**What the Dells are newly REFUSED (three of the four policies only narrow):**
- `DenyResourcePolicyWrites` (cell CT-d-5): 74 actions that write or delete a resource policy, on every resource. A Dell-placed
  project whose Terraform sets a bucket policy, a queue policy, a function permission or a key policy is refused at the Dell and
  goes by the role-request route or the laptop. That refusal is the intended behaviour.
- The routes Deny (cell CT-a-1, CTO ruling: the boundary is the role reached): function code and configuration writes on 33
  functions (31 that run as a role the census reads YES, plus 2 already protected: a harmless overlap), the five write and send
  actions on 12 command documents that target a host whose role reads YES, and `s3:PutObject` on the 5 prefixes such a host
  downloads and runs. Census: 175 of 175 roles read, 10 YES (1 by `iam:PassRole`, 9 by a delete), read time
  2026-10-07T11:05:41Z. Functions document 5,521 characters, hosts document 1,445 (limit 6,144 each).
- For dell2 only, `DenyShellDocuments`: `ssm:SendCommand` and `ssm:StartSession` with the AWS shell and session documents and the
  export render document.

**What dell2 GAINS (the one widening in this act):** `ssm:SendCommand` to instance `i-0167fd745ad906a66` alone with the two
resident documents `irpt-ycharts-deploy` and `irpt-ycharts-run` alone, and four read actions that return a command's result
(`GetCommandInvocation`, `ListCommandInvocations`, `ListCommands`, `DescribeInstanceInformation`, on `*`). Both documents take a
FREE-TEXT parameter (the census classes them `resident_free_text=2`, `resident_fixed=0`; row `NFRA_CTLPLN-W14-S5`), so this grant
is, in effect, the ability to run a command of dell2's choosing on that host AS THAT HOST'S ROLE. The CTO ruled it stands because
the census reads that role NO on all three questions (msg 106190). The grant is exactly as wide as that role: if the host's role
gains a permission later, dell2 gains it through this route. dell1 gains nothing.

**Named so it is not read as covered:** both Dells can already rewrite a command document (`ssm:UpdateDocument` in the create
policy; row `NFRA_CTLPLN-W14-S2`); this act denies that on the 12 documents feeding YES hosts and NOT on the two resident ones.
No resource policy was evaluated by the census (identity policies only; row `NFRA_CTLPLN-W8-S2`, API Gateway, owner the CTO).

**Evidence, issuer's own re-runs on the merged files (in the worker's tree before the merge):**
`POLICY-SIM allowed_ok=22/22 denied_ok=19/19 passrole_ok=5/5 protected_ok=8/8 respol_ok=11/11 ssm_ok=9/9 routes_ok=5/5 all_ok=True`;
`ROUTES-RENDER functions=33 documents=12 prefixes=5 policies=2 chars=5521,1445 header_ok=True ok=True`;
`ROLE-CENSUS ... roles=175 read=175 unread=0 ... yes_any=10 no=165 resident_host_role=NO ok=True`; proof VALID. The worker's one
live freshness run read `fresh=True` (0 verdict changes, 0 new, 0 gone, 0 route changes).

## Expected outcome, BOTH branches

- **A:** the applier's plan reads exactly the eight lines above, 8 to add, 0 to change, 0 to destroy -> apply.
- **B:** any other line, any change or destroy, a different count, a refused precondition, or `fresh=False` -> apply NOTHING and
  report the plan as read. On `fresh=False` the census is re-taken and committed, and this half is re-read against the new counts
  before any apply: a changed route set is a changed blast radius.

## Rollback per key

- Each new policy and its attachment: detach and delete by removing the resource pair and `safe-apply`, or as the same-window
  fallback detach the one attachment in the console. The four pairs are independent; rolling one back leaves the other three.
- The dell2 grant specifically: detaching `cloudops-dell2-agent-ssm-policy` from the user removes the send. A command already sent
  is not recalled; it is listed (`ssm list-commands`), not undone.
- Nothing is changed in place, so there is no prior version to restore.

## Conditions

1. The plan shape of branch A, read by the applier immediately before the apply.
2. BEFORE the plan, the applier runs `python infra/aws/terraform/nfra-ctlpln-identity/tests/derive_reached_roles.py --check-fresh`
   (about 9 minutes, read-only) and it reads `fresh=True`.
3. A NEVER-2 ledger entry opened at the start and closed at completion, naming the eight objects.
4. Read-back, LIVE, each arm with its matched statement, by the simulator against the ATTACHED policies (not the repo files):
   the seven arms of the simulation's seventh block and the nine of its sixth, and for the resource-policy Deny one refused
   `s3:PutBucketPolicy` and one still-allowed create from the create policy as the control. The live documents equal the rendered
   ones (parsed comparison). A re-plan reads no changes.
5. The exercised read from the box is another route's and is owed after the apply: dell2 sends `irpt-ycharts-run` once with a
   harmless parameter and reads the invocation back; dell2 is refused `AWS-RunShellScript`; dell1 is refused the send. Until that
   runs the grant is APPLIED, not EXERCISED.
6. This half does not cover any later change to the census file: a re-taken census that changes the route set is a new plan.

**SIGNED** -- `2.0.0_SA_COO~C`

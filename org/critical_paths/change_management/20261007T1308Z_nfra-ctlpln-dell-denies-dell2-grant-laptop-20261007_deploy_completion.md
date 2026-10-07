# Deploy Completion Record
**Date opened:** 2026-10-07T13:08:29.238674+00:00
**Status:** OPEN
**Deploy:** NFRA_CTLPLN CT-d-5 + CT-a-1 -- BOX: THE LAPTOP. ONE untargeted safe-apply of infra/aws/terraform/nfra-ctlpln-identity creating EIGHT IAM objects: four managed policies (cloudops-dell-agent-respol-policy, -routes-fn-policy, -routes-host-policy, cloudops-dell2-agent-ssm-policy) and their four attachments (three to cloudops-dell-agents-group, one to the dell2 user). Three narrow the Dells (74 resource-policy actions; 33 functions / 12 documents / 5 prefixes reaching YES roles; dell2 shell+session documents). ONE widens: dell2 may send two FREE-TEXT resident documents to instance i-0167fd745ad906a66 as irpt-ycharts-runner-role, and read ANY command result on *. Both halves SIGNED: COO @14774dd9ff, CTO @eb74cfb2d2. Plan measured 8 to add, 0 to change, 0 to destroy; census fresh=True.
**Authored by:** 0.7.0_AE_CloudOps~E
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | one untargeted safe-apply of the identity root at the laptop | plan reads EXACTLY 8 to add / 0 to change / 0 to destroy with the eight named addresses as an EXACT SET MATCH (no ninth, none missing); derive_reached_roles.py --check-fresh read fresh=True before the plan; safe-apply completes 8 added 0 changed 0 destroyed |  | OPEN |
| V1 | verify | the four live documents equal the rendered ones, and the attachment counts | each of the four LIVE default-version documents parses EQUAL to the document Terraform rendered (planted-mutant control through the same comparator); cloudops-dell-agents-group carries 5 managed policies and cloudops-dell2-agent-user carries 2, read live (BEFORE: 2 and 1) |  | OPEN |
| V2 | verify | the nine arms of the simulation's SIXTH block, against the ATTACHED policies | dell2: each of the two resident documents to i-0167fd745ad906a66 allowed; a resident document to another instance refused; AWS-RunShellScript explicitDeny; the export render document explicitDeny; a document nothing grants refused; ssm:GetCommandInvocation allowed. dell1: the send refused; GetCommandInvocation refused. Every arm ATTRIBUTED by matched statement |  | OPEN |
| V3 | verify | the five arms of the simulation's SEVENTH block (routes), against the ATTACHED policies | three explicitDeny, one per route kind (function code/config write, command-document write/send, s3:PutObject on a downloaded prefix); two allowed on NO roles as the controls that prove the Deny is scoped to YES roles and not blanket. Every arm ATTRIBUTED |  | OPEN |
| V4 | verify | the resource-policy Deny arm and its control | one s3:PutBucketPolicy for a Dell user reads explicitDeny with the matched statement named DenyResourcePolicyWrites; and one create action the create policy allows still reads allowed as the control, so the Deny is not a blanket refusal |  | OPEN |
| V5 | verify | AC1 + AC2 + AC3 and the six checks re-read | simulate_policy.py reads respol_ok=11/11 ssm_ok=9/9 routes_ok=5/5 all_ok=True (AC1); re-plan -detailed-exitcode reads exit=0 (AC2); check_identity.py reads names_from_builder=11/11 policy_size_ok=True ok=True (AC3); and the other three root checks re-read clean |  | OPEN |

## Log

- 20261007T130829Z OPENED by 0.7.0_AE_CloudOps~E with 6 leg(s)

---

## BOX

**THE LAPTOP.** Executor `0.7.0_AE_CloudOps~E`, seated by `2.0.0_SA_COO~C` under task order
`NFRA_CTLPLN.TO-APPLY-6.dell-denies-and-dell2-grant-apply-laptop` @aa7da845bb (GO msg 106234, acked). Applying
identity, read before the act: `arn:aws:iam::313476888478:user/Andrew_Berman`. Terraform resolved on PATH, v1.15.8
(`.tools/terraform.exe` does not exist on this box, so the baked path was not assumed).

Cells: `CT-d-5` (round 4) and, in the same one plan, workstream ACCESS cell `CT-a-1`, by the CTO's ruling of one
half request for both (msg 106190). The COO half names CT-d-5's resource-policy Deny explicitly "so that it is
signed and not a rider" -- the same rider class this seat stopped TO-APPLY-4 on.

## BLAST RADIUS -- the EIGHT objects, and nothing else

Four new managed policies and their four attachments. No other principal, no role, no resource, no served output.
No role is created by this act (the break-glass role of TO-APPLY-5 is a different root's separate act).

| # | address | object | attaches to |
|---|---|---|---|
| 1 | `aws_iam_policy.dell_agent_respol` | `cloudops-dell-agent-respol-policy` | -- |
| 2 | `aws_iam_group_policy_attachment.dell_agent_respol` | attachment | `cloudops-dell-agents-group` |
| 3 | `aws_iam_policy.dell_agent_routes_fn[0]` | `cloudops-dell-agent-routes-fn-policy` | -- |
| 4 | `aws_iam_group_policy_attachment.dell_agent_routes_fn[0]` | attachment | `cloudops-dell-agents-group` |
| 5 | `aws_iam_policy.dell_agent_routes_host[0]` | `cloudops-dell-agent-routes-host-policy` | -- |
| 6 | `aws_iam_group_policy_attachment.dell_agent_routes_host[0]` | attachment | `cloudops-dell-agents-group` |
| 7 | `aws_iam_policy.dell2_ssm` | `cloudops-dell2-agent-ssm-policy` | -- |
| 8 | `aws_iam_user_policy_attachment.dell2_ssm` | attachment | `cloudops-dell2-agent-user` |

Measured BEFORE: the group carries 2 (`cloudops-dell-agent-create-policy`, `cloudops-dell-agent-deploy-policy`);
`cloudops-dell1-agent-user` carries 1 (its bus policy); `cloudops-dell2-agent-user` carries 1 (its bus policy).
After: the group 5 (limit 10), dell2 2, dell1 unchanged at 1.

## WHAT THE DELLS ARE NEWLY REFUSED (three of the four policies only narrow)

- **`DenyResourcePolicyWrites`** (CT-d-5): 74 actions that write or delete a resource policy, on every resource. A
  Dell-placed project whose Terraform sets a bucket policy, queue policy, function permission or key policy is
  refused at the Dell and goes by the role-request route or the laptop. **That refusal is the design**, and it is
  Andrew's 06:5xZ answer 2 made mechanical ("For now, laptop should admin").
- **The routes Deny** (CT-a-1): function code and configuration writes on 33 functions (31 reaching a census-YES
  role, plus 2 already protected -- a harmless overlap the renderer prints); the five write and send actions on 12
  command documents targeting a host whose role reads YES; and `s3:PutObject` on the 5 prefixes such a host
  downloads and runs. Census: 175 of 175 roles read, 10 YES (1 by `iam:PassRole`, 9 by a delete), read
  2026-10-07T11:05:41Z.
- **`DenyShellDocuments`** (dell2 only): `ssm:SendCommand` and `ssm:StartSession` with the AWS shell and session
  documents and the export render document.

## THE ONE WIDENING, STATED AT ITS FULL WIDTH

dell2 gains `ssm:SendCommand` to instance `i-0167fd745ad906a66` **alone**, with the two resident documents
`irpt-ycharts-deploy` and `irpt-ycharts-run` **alone**, plus four read actions returning command results
(`GetCommandInvocation`, `ListCommandInvocations`, `ListCommands`, `DescribeInstanceInformation`).

**Both resident documents take a FREE-TEXT parameter.** Measured independently by this seat before the plan, not
taken from the halves: `SSM-DOCS declared=16 unresolved=0 resident_fixed=0 resident_free_text=2 export_render=1
other=13 unsure_params=2 in_policy=2 ok=True`. So this grant is, in effect, **the ability to run a command of
dell2's choosing on that host AS `irpt-ycharts-runner-role`**. The CTO signed it at that width for one stated
reason: the census reads that role NO on IAM writes, audit-trail writes and production-data deletes. **The grant is
exactly as wide as that role: if the host's role gains a permission later, dell2 gains it through this route** (CTO
condition 7 puts that on a carrier).

**`ReadCommandResults` is on `*`.** dell2 may read the result of ANY command sent in the account, not only its own;
the service offers no narrower resource for those four actions. NOT measured by anyone: whether an existing
command prints a secret to its output. That is an open row the issuer files, named here so it is not read as
covered.

**dell1 gains nothing.**

## ROLLBACK PER PAIR -- the four pairs are INDEPENDENT

Nothing is changed in place, so there is no prior version to restore; each rollback is a detach-and-delete.

| pair | rollback | same-window fallback |
|---|---|---|
| respol policy + group attachment | remove the resource pair from `iam.tf` and `safe-apply` | detach the one attachment in the console |
| routes-fn policy + group attachment | same | same |
| routes-host policy + group attachment | same | same |
| dell2 ssm policy + user attachment | same -- detaching `cloudops-dell2-agent-ssm-policy` from the user removes the send | same |

**Rolling one back leaves the other three standing.** **A command already sent is NOT recalled** -- it is listed
(`ssm list-commands`), not undone.

**TRIGGERS:** AC1/AC2/AC3 failing; any live document ceasing to equal its rendered form; the group not reading 5 or
dell2 not reading 2; or CTO condition 8 -- if the exercised read shows dell2 sending any document other than the two
named, or a send to any other instance succeeding, **the dell2 attachment is detached the same window and
`1.0.0_SA_CTO` is told**.

## PRE-APPLY EVIDENCE IN HAND

- **COMMIT GATE:** `git diff --stat 47a20c88e4 HEAD -- <root>` empty and `git status --porcelain -- <root>` empty,
  with a POSITIVE CONTROL (`47a20c88e4^..HEAD` on the same pathspec prints 12 files / 8241 insertions) and a
  BLOB-LEVEL pass: every file of the root is byte-identical at `47a20c88e4` and HEAD. Re-verified after the
  integrator's trunk sync moved HEAD to `7b3c62daf0`, and the sync touched neither the root nor the census file.
- **SIX ROOT CHECKS, each `ok=True`:**
  `IDENTITY-STATIC validate=ok no_access_key=True names_from_builder=11/11 policy_size_ok=True ok=True`;
  `POLICY-SIM allowed_ok=22/22 denied_ok=19/19 passrole_ok=5/5 protected_ok=8/8 respol_ok=11/11 ssm_ok=9/9
  routes_ok=5/5 all_ok=True`;
  `ROUTES-RENDER functions=33 documents=12 prefixes=5 policies=2 chars=5521,1445 header_ok=True ok=True`;
  `PASSROLE-RENDER applied=0 named=0 wildcard=0 in_sync=True ok=True`;
  `PROTECTED-CENSUS functions=233 regions=17 refused_regions=0 protected=10 ... in_sync=True ok=True`;
  `SSM-DOCS declared=16 unresolved=0 resident_fixed=0 resident_free_text=2 export_render=1 other=13
  unsure_params=2 in_policy=2 ok=True`.
- **THE FRESHNESS READ (COO condition 2), the gate on a census being a reading of one moment:**
  `CENSUS-FRESH saved=2026-10-07T11:05:41Z roles_saved=175 roles_live=175 verdict_changes=0 new_roles=0
  gone_roles=0 route_changes=0 fresh=True`, 510 s, 175 of 175 roles read, 0 listing errors, run read-only and NOT
  bounded at 120 s as the order requires. Saved: `deliverables/FRESHNESS_check_fresh_20261007.txt`.
- **STEP 3, the four names are free:** none of `cloudops-dell-agent-respol-policy`,
  `cloudops-dell-agent-routes-fn-policy`, `cloudops-dell-agent-routes-host-policy`,
  `cloudops-dell2-agent-ssm-policy` exists, on a printed DENOMINATOR of 43 customer-managed policies with THREE
  positive controls (the create, deploy and dell2-bus policies all found by the same census).
- **THE PLAN:** `Plan: 8 to add, 0 to change, 0 to destroy.`; 8 resource blocks by `grep -c`; **EXACT SET MATCH**
  against the order's eight addresses computed programmatically -- 0 in the plan but not the order (no ninth), 0 in
  the order but not the plan; every resource-action line is a creation; zero `will be updated` / `will be destroyed`
  / `must be replaced` / `-/+` markers. Saved:
  `deliverables/PLAN6_nfra-ctlpln-identity_20261007.txt`.

## INSTRUMENT NOTES carried into the verify legs

Step 7 requires the arms be run **against the ATTACHED policies, not the repo files** -- so each simulation targets
the live principal and lets IAM resolve its attached set, rather than supplying a document.
`simulate-principal-policy` has four false-DENY modes (multi-ARN in one call, unevaluated `Condition`, unvalidated
action names, wrong-grain ARN) and one false-ALLOW mode measured on this project (it matches the ARN against the
policy's patterns and never asks whether the ARN names anything). So: ONE resource ARN per call; `MatchedStatements`
read on EVERY arm so a deny is attributed to the statement that caused it; controls run as SEPARATE invocations; and
the two NO-role arms of block 7 are the controls that distinguish a scoped Deny from a blanket one.

## NOT EXERCISED, and not claimed

**This seat sends NO command to any host.** The exercised send is dell2's own, from dell2, by another route
(COO condition 5). Until it runs **the grant is APPLIED, not EXERCISED.**

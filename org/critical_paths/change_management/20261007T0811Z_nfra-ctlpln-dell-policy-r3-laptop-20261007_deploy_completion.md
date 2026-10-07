# Deploy Completion Record
**Date opened:** 2026-10-07T08:11:52.134554+00:00
**Status:** OPEN
**Deploy:** NFRA_CTLPLN round 3 Dell policy apply -- BOX: THE LAPTOP (CTO half ruling, Andrew-direct 2026-10-07 'For now, laptop should admin'). ONE safe-apply of infra/aws/terraform/nfra-ctlpln-identity from df38747760 (contains eda2919e6b). Three IAM objects: NEW managed policy cloudops-dell-agent-create-policy + its attachment to cloudops-dell-agents-group, and a new version of cloudops-dell-agent-deploy-policy. Both never-widen halves SIGNED: COO @d3ffdf3, CTO @2d27f79524. Plan measured 2 to add, 1 to change, 0 to destroy.
**Authored by:** 0.7.0_AE_CloudOps~E
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | safe-apply of the nfra-ctlpln-identity root at the laptop | plan reads EXACTLY 2 to add / 1 to change / 0 to destroy on the three addresses aws_iam_group_policy_attachment.dell_agent_create (create), aws_iam_policy.dell_agent_create (create), aws_iam_policy.dell_agent_deploy (update in-place); safe-apply.sh completes with Apply complete 2 added 1 changed 0 destroyed |  | OPEN |
| V1 | verify | AC1 group attachment set | iam list-attached-group-policies cloudops-dell-agents-group sorted == exactly [cloudops-dell-agent-create-policy, cloudops-dell-agent-deploy-policy] |  | OPEN |
| V2 | verify | live-vs-repo document equality, both policies | parsed-JSON equality of each LIVE default-version document against dell_create_policy.json and dell_deploy_policy.json; AND the four round-2 Deny Sids DenyEveryIamWrite, DenyCloudTrailWrites, DenyS3DeletesOnProductionData, DenyTableAndDatabaseDeletes read from the LIVE deploy document (CTO half condition 2) |  | OPEN |
| V3 | verify | live-principal simulation | iam simulate-principal-policy against the LIVE principal cloudops-dell1-agent-user repeating the arms of simulate_policy.py blocks 1 and 3, one --resource-arns per call, with an admin positive control run in isolation beside any deny acted on |  | OPEN |
| V4 | verify | AC2 + AC3 + comp-iam gaps | simulate_policy.py reads POLICY-SIM allowed_ok=22/22 denied_ok=19/19 passrole_ok=5/5 protected_ok=8/8 all_ok=True; re-plan -detailed-exitcode reads exit=0 (no changes); comp-iam gaps run and read |  | OPEN |

## Log

- 20261007T081152Z OPENED by 0.7.0_AE_CloudOps~E with 5 leg(s)

---

## BOX

**THE LAPTOP.** Ruled by the CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_NFRA_CTLPLN_ROUND3_DELL_POLICY_APPLY_AT_THE_LAPTOP_20261007.md` @2d27f79524,
on Andrew-direct 2026-10-07 (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_063xZ_DELLS_CREATE_RESOURCES_NO_IAM_DEPLOYS_NOT_GATED_ON_SITEZ.md`):
"For now, laptop should admin". Site Z applied this root's first version at ~05:0xZ; that does not make site Z the root's standing home.
Executor: `0.7.0_AE_CloudOps~E`, seated by `2.0.0_SA_COO~C` under task order `NFRA_CTLPLN.TO-APPLY-3.dell-policy-apply-laptop` @df38747760.
Applying identity, measured BEFORE the apply: `arn:aws:iam::313476888478:user/Andrew_Berman` (`sts get-caller-identity`).

## BLAST RADIUS -- what this act may touch

Three IAM objects and nothing else. No other principal, no role, no resource, no served output.

| # | object | action |
|---|---|---|
| 1 | managed policy `cloudops-dell-agent-create-policy` | CREATED (absent before: NoSuchEntity, and absent from a census of 42 customer-managed policies with a positive control) |
| 2 | group attachment `cloudops-dell-agents-group` -> the create policy | CREATED (group held 1 attachment before: the deploy policy alone) |
| 3 | managed policy `cloudops-dell-agent-deploy-policy` | NEW DEFAULT VERSION (before: DefaultVersionId `v1`, the only version, 8 statements) |

It changes what the two Dell users (`cloudops-dell1-agent-user`, `cloudops-dell2-agent-user`) may do.

**Named so the act is not read as narrower or wider than it is -- the Dells become NEWLY REFUSED on:**
code/config updates, deletes and URL changes on 10 of 233 Lambda functions, five of them edge functions
(`auth-validator-edge`, `cache-control-injector`, `public-data-router`, `shared-advisor-router`, `shared-advisor-router-response`)
plus `opal-portal-authorizer`, `opal-portal-rest-authorizer`, `opalinvest-auth-handler`, `trade-auth-handler`, `trade-authorizer`;
`iam:PassRole` on every role (no applied role request exists, so no change in effect today); and `apigateway:GET` on `/apikeys` and `/apikeys/*`.
A Dell-placed project that deploys one of the ten is refused and writes in to the laptop. **That refusal is the intended behaviour, not a regression.**

## ROLLBACK PER KEY

| key | rollback | notes |
|---|---|---|
| `aws_iam_policy.dell_agent_create` + `aws_iam_group_policy_attachment.dell_agent_create` | remove both resources from `iam.tf` and `safe-apply`; the Dells return to the deploy policy alone | same-window |
| `cloudops-dell-agent-deploy-policy` | IAM keeps the prior version: **re-default `v1`** (`iam set-default-policy-version --version-id v1`), or `safe-apply` from the commit before `c21a185724` for this file | the version id is MEASURED pre-apply, not predicted: `v1` was the only version |

**Not undone by any rollback:** anything a Dell created under the grant. That is listed, never reverted.

## BOTH BRANCHES (the halves' own wording)

- **Apply succeeds:** the Dells hold the create grant (52 of 52 derived non-IAM kinds, 31 read-only refresh actions) and the three refusals above.
- **Apply fails, is refused for want of IAM write, or is not run:** the Dells hold the round-2 deploy policy -- they update any existing
  function (the ten included), write data, and create nothing. A refused first call half-applies nothing; this entry then closes REFUSED.

## PRE-APPLY EVIDENCE ALREADY IN HAND

- Root bytes at HEAD `df38747760` equal their bytes at `eda2919e6b`: `git diff --stat` empty, `git status --porcelain` empty, with a
  POSITIVE CONTROL (`eda2919e6b^..HEAD` on the same pathspec prints 5 files / 1636 insertions), so a clean-empty from a mangled pathspec is ruled out.
  `eda2919e6b` is an ancestor of origin/CLOUD `2d27f79524` (`ls-remote` read).
- Four root checks PASS: `IDENTITY-STATIC validate=ok no_access_key=True names_from_builder=7/7 policy_size_ok=True ok=True`;
  `POLICY-SIM allowed_ok=22/22 denied_ok=19/19 passrole_ok=5/5 protected_ok=8/8 all_ok=True`;
  `PASSROLE-RENDER applied=0 named=0 wildcard=0 in_sync=True ok=True`;
  `PROTECTED-CENSUS functions=233 regions=17 refused_regions=0 protected=10 by_authorizer=1 by_edge=5 ruled_in=4 unruled=0 in_sync=True ok=True`.
- Plan, untargeted, read at 2026-10-07 ~08:0xZ: `Plan: 2 to add, 1 to change, 0 to destroy.`; exactly 3 resource blocks (denominator
  printed by `grep -c`); zero `must be replaced` / `will be destroyed` / `-/+` markers. Saved:
  `org/tier2_senior/0.7.0_AE_CloudOps~E/deliverables/PLAN_nfra-ctlpln-identity_20261007.txt`.
- BEFORE live state saved under `org/tier2_senior/0.7.0_AE_CloudOps~E/deliverables/BEFORE_*_20261007.json` (5 files) as the rollback reference.

## INSTRUMENT NOTE carried into the verify legs

`comp-iam` models `(action)`, never `(action, resource)`, and is a FLOOR, never a deletion warrant.
`simulate-principal-policy` has four false-DENY modes (multi-ARN, unevaluated `Condition`, unvalidated action names, wrong-grain ARN)
and one false-ALLOW mode measured on THIS project 2026-10-07 by `0.7.0_AE_CloudOps~RV`: it matches the ARN against the policy's
`Resource` patterns and never asks whether the ARN names anything. Therefore leg V3 runs ONE `--resource-arns` per call, and the
positive control runs as a SEPARATE invocation.

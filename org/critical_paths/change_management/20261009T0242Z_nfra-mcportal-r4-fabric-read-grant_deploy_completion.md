# Deploy Completion Record
**Date opened:** 2026-10-09T02:42:49.746857+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: sovereign / 2.0.0_SA_COO~MP routing of the naming-plan-gate REFUSE on policy name opal-gateway-mcportal-fabric-read (gate remedy: gateway-mcportal-fabric-read-policy), which TO MP-x-3's AC1 pins by name; rule 30 non-application for an existing pipeline. Worker may not override (step 2) nor repair a criterion (BOUNDS 3). (held since 2026-10-09T02:55:44.519132+00:00)
**Deploy:** NFRA_MCPORTAL MP-x-3: opal-gateway-role read grant on the two globgrph fabric prefixes (ruling: laptop 1.0.0_SA_CTO msg 107359, relay 32030)
**Authored by:** 0.7.0_AE_CloudOps~MP
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | targeted terraform plan of aws_iam_role_policy.gw_mcportal_fabric_read | plan counts must read 1 to add, 0 to change, 0 to destroy | RAN. terraform -chdir=infra/aws/terraform/opal-gateway plan -target=aws_iam_role_policy.gw_mcportal_fabric_read: 'Plan: 1 to add, 0 to change, 0 to destroy.' Plan saved to .build/mpx3.tfplan; show -json parsed: resource_changes=2, non-no-op=1, histogram {('create',):1}, address aws_iam_role_policy.gw_mcportal_fabric_read, name='opal-gateway-mcportal-fabric-read', role='opal-gateway-role', stmt1 McportalFabricPrefixReadOnly Allow ['s3:GetObject'] res=2 cond=NO, stmt2 McportalFabricPrefixListOnly Allow ['s3:ListBucket'] res=1 cond=yes. Counts are EXACTLY the required 1/0/0, so the plan limb did not stop the act; the naming plan limb did (see L2). | CLOSED 20261009T025443Z |
| L2 | activation | safe-apply targeted apply of aws_iam_role_policy.gw_mcportal_fabric_read on opal-gateway-role | apply output + inline policy opal-gateway-mcportal-fabric-read present on the role | NOT EXECUTED -- this leg did not run and will not run under this entry. safe-apply.sh REFUSED at its naming plan limb BEFORE terraform was invoked: '[naming-plan-gate] NAMING REFUSE aws_iam_role_policy.gw_mcportal_fabric_read opal-gateway-mcportal-fabric-read -> gateway-mcportal-fabric-read-policy' / 'safe-apply: BLOCKED by the naming plan limb (LGIC_ENFORCE DEC-6, ENFORCE mode, rc=1). Nothing was planned further or applied.' NOT taken on the wrapper's self-report -- WORLD VERIFIED UNCHANGED on two planes: (1) live IAM, AC1 x3.AC1.sh -> 'NoSuchEntity ... policy with name opal-gateway-mcportal-fabric-read cannot be found', get-role-policy rc=254; (2) terraform state list \| grep -c gw_mcportal_fabric_read -> 0 (absent from state). DELTA=0, so the named rollback (aws iam delete-role-policy / targeted destroy) was a NO-OP and was deliberately NOT run -- there is nothing to delete. No override was taken: TO step 2 forbids it and the name is pinned by AC1, which TO BOUNDS 3 forbids repairing. | CLOSED 20261009T025544Z |
| L3 | verify | AC1 get-role-policy shape, AC2 six-arm simulate-principal-policy, AC3 carve-out tokens | three check outputs, each RESULT: PASS |  | OPEN |

## Log

- 20261009T024249Z OPENED by 0.7.0_AE_CloudOps~MP with 3 leg(s)
- 20261009T025443Z LEG L1 closed: RAN. terraform -chdir=infra/aws/terraform/opal-gateway plan -target=aws_iam_role_policy.gw_mcportal_fabric_read: 'Plan: 
- 20261009T025544Z LEG L2 closed: NOT EXECUTED -- this leg did not run and will not run under this entry. safe-apply.sh REFUSED at its naming plan limb BE
- 20261009T025544Z HELD-SOVEREIGN-GATED gate=sovereign/2.0.0_SA_COO~MP routing of the naming-plan-gate REFUSE on policy name opal-gatew

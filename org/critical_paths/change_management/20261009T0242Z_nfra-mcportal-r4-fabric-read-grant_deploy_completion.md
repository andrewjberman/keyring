# Deploy Completion Record
**Date opened:** 2026-10-09T02:42:49.746857+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T032908Z
**Deploy:** NFRA_MCPORTAL MP-x-3: opal-gateway-role read grant on the two globgrph fabric prefixes (ruling: laptop 1.0.0_SA_CTO msg 107359, relay 32030)
**Authored by:** 0.7.0_AE_CloudOps~MP
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | targeted terraform plan of aws_iam_role_policy.gw_mcportal_fabric_read | plan counts must read 1 to add, 0 to change, 0 to destroy | RAN at the AMENDED name. terraform -chdir=infra/aws/terraform/opal-gateway plan -target=aws_iam_role_policy.gw_mcportal_fabric_read -out=.build/mpx3.tfplan: 'Plan: 1 to add, 0 to change, 0 to destroy.' -- EXACTLY the required counts. show -json parsed: resource_changes=2, non-no-op=1, histogram {('create',):1}; address aws_iam_role_policy.gw_mcportal_fabric_read; name='gateway-mcportal-fabric-read-policy' (the Rule 30 builder output, per AMENDMENT 1); role='opal-gateway-role'; stmt McportalFabricPrefixReadOnly Allow ['s3:GetObject'] res=2 cond=NO; stmt McportalFabricPrefixListOnly Allow ['s3:ListBucket'] res=1 cond=yes with Condition {"StringLike": {"s3:prefix": ["fabric/activity/v1/*", "fabric/open-calls/v1/*", "fabric/activity/v1/", "fabric/open-calls/v1/"]}}. The SAVED plan file is what safe-apply is handed, so the graded plan and the applied plan are byte-identical. (The earlier pre-amendment plan read the same 1/0/0 at the refused name; this proof supersedes it in place.) | CLOSED 20261009T032335Z |
| L2 | activation | safe-apply targeted apply of aws_iam_role_policy.gw_mcportal_fabric_read on opal-gateway-role | apply output + inline policy gateway-mcportal-fabric-read-policy present on the role | APPLIED. .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply .build/mpx3.tfplan -- the SAVED plan graded in L1, so applied bytes == graded bytes. The naming limbs PASSED this time at the amended name (they REFUSED the pre-amendment name). HONEST SCOPE OF THIS QUOTE: terraform's own 'Apply complete!' summary line scrolled past the output filter used on that call and is NOT quoted here; the proof below is the verified END STATE, not the producer's self-report, which CLAUDE.md says never to trust anyway. END STATE, three planes: (1) terraform state list now contains aws_iam_role_policy.gw_mcportal_fabric_read (0 before); (2) live IAM via x3.AC1.sh -> 'actions=s3:GetObject+s3:ListBucket resources=3 problems=0 / RESULT: PASS / exit=0' (NoSuchEntity before); (3) post-apply re-plan of the same target -> 'No changes. Your infrastructure matches the configuration.' = 0-diff. The inline policy gateway-mcportal-fabric-read-policy is present on opal-gateway-role. | CLOSED 20261009T032825Z |
| L3 | verify | AC1 get-role-policy shape, AC2 six-arm simulate-principal-policy, AC3 carve-out tokens | three check outputs, each RESULT: PASS | ALL THREE PASS. AC1 'actions=s3:GetObject+s3:ListBucket resources=3 problems=0 / RESULT: PASS / exit=0' -- exactly the two actions, exactly 3 resources (the two prefix ARNs plus the bucket), 0 problems, and the checker's own arms confirm the ListBucket statement is CONDITIONED and names neither warehouse nor projection. AC2 'simulation arms matched 6 of 6 / RESULT: PASS / exit=0' -- get activity allowed, get open-calls allowed, get warehouse implicitDeny, put activity implicitDeny, list activity allowed, list warehouse implicitDeny; one --resource-arns per call and --context-entries on the two conditioned list arms (CLAUDE.md 22a). AC3 'carve-out tokens present 6 of 6 / RESULT: PASS / exit=0' -- 3 tokens x 2 files. DISCRIMINATION NOTE: pre-apply AC2 read 3 of 6 with the three NEGATIVE arms already passing on the grant's ABSENCE, so they discriminated nothing then; NOW the policy exists and an over-broad grant would have flipped them to allowed, so post-apply all six arms carry evidence and the three positive arms moved implicitDeny -> allowed. BOUNDS 1 honoured: no S3 object was read or written; the bucket's existence rests on the module's own live use of it (alb.tf, ms-ingest.tf), not on a listing. | CLOSED 20261009T032826Z |

## Log

- 20261009T024249Z OPENED by 0.7.0_AE_CloudOps~MP with 3 leg(s)
- 20261009T025443Z LEG L1 closed: RAN. terraform -chdir=infra/aws/terraform/opal-gateway plan -target=aws_iam_role_policy.gw_mcportal_fabric_read: 'Plan: 
- 20261009T025544Z LEG L2 closed: NOT EXECUTED -- this leg did not run and will not run under this entry. safe-apply.sh REFUSED at its naming plan limb BE
- 20261009T025544Z HELD-SOVEREIGN-GATED gate=sovereign/2.0.0_SA_COO~MP routing of the naming-plan-gate REFUSE on policy name opal-gatew
- 20261009T032047Z HOLD RELEASED -> OPEN
- 20261009T032047Z LEG L1 closed: PROBE
- 20261009T032335Z LEG L1 closed: RAN at the AMENDED name. terraform -chdir=infra/aws/terraform/opal-gateway plan -target=aws_iam_role_policy.gw_mcportal_
- 20261009T032825Z LEG L2 closed: APPLIED. .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply .build/mpx3.tfplan -- the SAVED plan graded 
- 20261009T032826Z LEG L3 closed: ALL THREE PASS. AC1 'actions=s3:GetObject+s3:ListBucket resources=3 problems=0 / RESULT: PASS / exit=0' -- exactly the t
- 20261009T032908Z CLOSED -- all 3 legs proven

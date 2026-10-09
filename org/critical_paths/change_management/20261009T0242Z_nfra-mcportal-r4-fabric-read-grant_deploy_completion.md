# Deploy Completion Record
**Date opened:** 2026-10-09T02:42:49.746857+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPORTAL MP-x-3: opal-gateway-role read grant on the two globgrph fabric prefixes (ruling: laptop 1.0.0_SA_CTO msg 107359, relay 32030)
**Authored by:** 0.7.0_AE_CloudOps~MP
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | targeted terraform plan of aws_iam_role_policy.gw_mcportal_fabric_read | plan counts must read 1 to add, 0 to change, 0 to destroy |  | OPEN |
| L2 | activation | safe-apply targeted apply of aws_iam_role_policy.gw_mcportal_fabric_read on opal-gateway-role | apply output + inline policy opal-gateway-mcportal-fabric-read present on the role |  | OPEN |
| L3 | verify | AC1 get-role-policy shape, AC2 six-arm simulate-principal-policy, AC3 carve-out tokens | three check outputs, each RESULT: PASS |  | OPEN |

## Blast radius (signed by the pair: 1.0.0_SA_CTO~O by the ruling's "under its own pair"; 2.0.0_SA_COO~MP by the cut)

- the act adds ONE inline policy to `opal-gateway-role`: s3:GetObject on
  `fabric/activity/v1/*` and `fabric/open-calls/v1/*` of `opal-313476888478-globgrph`, plus
  s3:ListBucket on that bucket conditioned (StringLike s3:prefix) to those same two prefixes;
- no write, no other bucket prefix (warehouse/ and projection/ stay out), no other resource;
- `graph-read.tf` changes in COMMENTS ONLY (8 insertions, 2 deletions, all inside the leading
  comment block; no resource line moved);
- no served output moves; the gateway is not redeployed; no S3 object is read or written by the act.

## Rollback per key (named BEFORE the act)

Either of, both targeted at the one new policy and nothing else:

    aws iam delete-role-policy --role-name opal-gateway-role       --policy-name opal-gateway-mcportal-fabric-read

    .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway destroy       -target=aws_iam_role_policy.gw_mcportal_fabric_read

## Preflight: comp-iam gaps (step 3; necessary, NOT sufficient -- AC2's simulation is the truth)

Run from this worktree at 2026-10-09T02:4xZ, AFTER the .tf change (so it reads the DESIRED state):

    Total: 37 missing | 300 deny-present | 1 coverage-unknown | 3 resource-mismatch  across 33 service(s)
    RESOURCE PLANE: 883 call(s) verdicted across 105 mapped role(s); 666 UNRESOLVABLE-RESOURCE,
      144 GRANTED, 50 GRANTED-BROAD, 20 UNGRANTED, 3 GRANTED-ACTION / UNGRANTED-RESOURCE

The census is ESTATE-WIDE and PRE-EXISTING; this act adds no row to it. The only `opal-gateway`
rows are two RESOURCE-MISMATCH rows for `s3:GetObject` on `arn:aws:s3:::opal-mcp-audit/*`, reached
from `infra/aws/ec2/opal-gateway/tests/test_schwab_audit.py:75,319` -- a bucket this act does not
touch. In the same row comp-iam prints the buckets the role DOES hold s3:GetObject on, and
`opal-313476888478-globgrph` now appears among them
(`held: ['opal-313476888478-globgrph', 'opal-313476888478-lambda-artifacts', 'opal-data-portal-v2']`)
-- that is this act's own DESIRED grant read back out of the Terraform, not live evidence.

COMP-IAM'S OWN CEILING (cloud-ops): it models `(action)`, never `(action, resource)`, so it cannot
confirm the two-prefix carve-out and cannot falsify a third prefix. AC2's six simulation arms,
one `--resource-arns` per call with `--context-entries` for the conditioned statement, are the
oracle for that.

## Log

- 20261009T024249Z OPENED by 0.7.0_AE_CloudOps~MP with 3 leg(s)

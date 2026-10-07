# COO never-widen half -- NFRA_CTLPLN round 3: ONE apply of the Dell identity root (create grant, PassRole statement, Lambda deny-list)

**Author:** `2.0.0_SA_COO~C`, 2026-10-07 ~07:5xZ. **Read at:** trunk `eda2919e6b` (the last round-3 merge), root
`infra/aws/terraform/nfra-ctlpln-identity/`. **Counterpart owed:** a CTO half covering this same act. The CTO half already signed
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_NFRA_CTLPLN_CT_c_1_DELL_CREATE_GRANT_20261007.md` @bb0e587e22) covers the create
policy alone and its condition 1 reads "2 to add, 0 to change, 0 to destroy ... Any other line in the plan voids this half"; it names
CT-c-3 and CT-c-5 as not covered. The trunk now carries all three cells in one root, so that half does not cover this act.

## The act

One `safe-apply` of `infra/aws/terraform/nfra-ctlpln-identity/` from a commit that contains `eda2919e6b`, at a box that holds IAM write.
WHERE it runs is not ruled (PRD ADDENDUM v0.8: "where their later changes apply is not ruled here"); this half is signed for either box
and the act does not run until the CTO names one.

## The plan, MEASURED (not predicted)

`terraform plan -lock=false` in the root on the laptop, 2026-10-07 ~07:5xZ, read-only, against the live state:

```
  # aws_iam_group_policy_attachment.dell_agent_create will be created
  # aws_iam_policy.dell_agent_create will be created
  # aws_iam_policy.dell_agent_deploy will be updated in-place
Plan: 2 to add, 1 to change, 0 to destroy.
```

**Writers of the property moved (what the two Dell users may do): N = 3 documents, all read.** `dell_create_policy.json` (new),
`dell_deploy_policy.json` (changed), and the two per-Dell bus policies (unchanged, not in the plan).

## Blast radius

Three IAM objects: one new managed policy, its one attachment to `cloudops-dell-agents-group`, and a new version of the existing managed
policy `cloudops-dell-agent-deploy-policy`. It changes what the two Dell users may do. It changes no other principal, no role, no
resource and no served output.

**What the Dells gain:** create, update and tag on the non-IAM resource kinds of the Dell-placed projects' Terraform roots (52 of 52
derived kinds; the CTO's half lists the families and names the widest: Route 53 record changes, CloudFront and WAF updates,
security-group ingress, Secrets Manager value writes), plus 31 read-only actions for refresh, none returning a secret value.

**What the Dells lose or are newly refused:**
- `iam:PassRole` moves to its own Deny on every role (no applied role request exists; the rendered list is empty). Before and after,
  a Dell passes no role: no change in effect today.
- Code and configuration updates, deletes and URL changes on ten access-deciding functions of 233 (1 authorizer target, 5 edge, 4 ruled in
  by the CTO, msg 106045). TODAY the Dells may update any function; after the apply they may not update these ten. A Dell-placed
  project that deploys one of the ten is refused: `shared-advisor-router`, `shared-advisor-router-response`, `public-data-router`,
  `cache-control-injector` and `auth-validator-edge` are edge functions the investor-reporting and portal work may touch. That refusal
  is the intended behaviour; it is named here so it is not read as a regression.
- `apigateway:GET` on `/apikeys` and `/apikeys/*`.

**Evidence, issuer's own re-runs on the merged files:** `POLICY-SIM allowed_ok=22/22 denied_ok=19/19 passrole_ok=5/5 protected_ok=8/8
all_ok=True`; `PROTECTED-CENSUS functions=233 regions=17 refused_regions=0 protected=10 ... in_sync=True ok=True`; `PASSROLE-RENDER
applied=0 named=0 wildcard=0 in_sync=True ok=True`; six of six proof instances VALID at HEAD.

## Rollback per key

- New policy and attachment: remove the two resources from `iam.tf`, `safe-apply`; the Dells return to the deploy policy alone.
- Deploy policy: IAM keeps the prior version; `safe-apply` from the commit before `c21a185724` for this file restores it, or set the
  prior version as default in the console as the same-window fallback.
- Nothing a Dell created under the grant is removed by the rollback; that is listed, not undone.

## Conditions

1. The apply's own plan reads exactly the three lines above: 2 to add, 1 to change, 0 to destroy. Any other line voids this half.
2. After the apply, the live read-back: both policies' default versions equal the repo bytes, the group carries both, and one
   simulation against the LIVE principal (`simulate-principal-policy` for `cloudops-dell1-agent-user`) repeats the four blocks.
3. One ledger entry in `org/critical_paths/change_management/`, opened before the apply and closed after the read-back.

## Both branches

If the apply succeeds, the Dells hold the grant and the three new refusals above. If it fails or is not run, the Dells hold the round-2
deploy policy: they update existing functions (all of them, the ten included) and write data, and create nothing.

## Not covered

Any act a Dell takes under the grant; the first role request's role (a separate laptop apply under its own pair); the six
policy-carrying calls the CTO ruled stay allowed with no cloud refusal behind the laptop-administers rule (row NFRA_CTLPLN-S6).

**SIGNED** -- `2.0.0_SA_COO~C`

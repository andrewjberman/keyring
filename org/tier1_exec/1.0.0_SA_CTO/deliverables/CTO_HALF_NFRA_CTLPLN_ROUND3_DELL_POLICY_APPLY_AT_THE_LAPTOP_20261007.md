# CTO never-widen half -- NFRA_CTLPLN round 3: ONE apply of the Dell identity root, AT THE LAPTOP

**Author:** `1.0.0_SA_CTO`, 2026-10-07 ~07:5xZ. **Counterpart:** the COO half
`org/tier1_exec/2.0.0_SA_COO/deliverables/NEVER_WIDEN_HALF_NFRA_CTLPLN_ROUND3_DELL_POLICY_20261007.md`, SIGNED by `2.0.0_SA_COO~C`
(@d3ffdf3 by its message 106055). **Read at:** that file's full text, and trunk `eda2919e6b` by its citation. **Supersedes** this
seat's `CTO_HALF_NFRA_CTLPLN_CT_c_1_DELL_CREATE_GRANT_20261007.md` for the act: that half covered the create policy alone and its own
condition 1 is voided by the third plan line. Its rulings on rows W4-S1 to W4-S4 stand.

## The box: THE LAPTOP

**RULING: the apply runs at the laptop.** Andrew-direct 2026-10-07: "ok i like the laptop for creating roles, we can manage that for
now"; "For now, laptop should admin"; and "I do not like the idea of gating deploys on sitez, because sitez will bottleneck". This
act changes what a Dell identity may do, which is the access administration he placed on the laptop. Site Z applied the first version
of this root on 2026-10-07 ~05:0xZ; nothing in that makes site Z the root's standing home.

- **Executor:** a cloud-operations seat on the laptop, seated by `2.0.0_SA_COO~C` under its own task order, through `safe-apply`. This
  seat does not apply.
- **UNMEASURED, and the act's own first read:** that the laptop's identity holds IAM write on these three objects. The plan ran on
  the laptop read-only against the live state, so the state backend is reachable from here. If the apply is refused for want of IAM
  write, that refusal is the measurement: nothing is half-applied by a refused first call, the ledger entry closes REFUSED, and the
  box question returns to this seat the same hour.

## What this half covers

The act exactly as the COO half states it: one `safe-apply` of `infra/aws/terraform/nfra-ctlpln-identity/` from a commit that contains
`eda2919e6b`. Plan as MEASURED there: `aws_iam_policy.dell_agent_create` created, `aws_iam_group_policy_attachment.dell_agent_create`
created, `aws_iam_policy.dell_agent_deploy` updated in place; 2 to add, 1 to change, 0 to destroy.

**Blast radius:** three IAM objects, as the COO half names them. No other principal, no role, no resource, no served output.

**Writers of the property moved:** N = 3 documents by the COO half's count (`dell_create_policy.json`, `dell_deploy_policy.json`, the
two unchanged bus policies counted as one). This seat read the create policy at `7091ecaecc` and the deploy policy at round 2; the
round-3 deploy-policy bytes at `eda2919e6b` are taken from the COO half's simulation evidence (22 of 22 allowed, 19 of 19 denied,
5 of 5 PassRole, 8 of 8 protected) and are NOT re-read by this seat. Condition 2 below is the read that replaces that.

## What changes for a Dell, named so the signature is not read as narrower or wider than it is

- GAINS: create, update and tag on the non-IAM kinds (52 of 52 derived), including Route 53 record changes, CloudFront and WAF
  updates, security-group ingress and Secrets Manager value writes; 31 read-only actions for Terraform refresh.
- NEWLY REFUSED: updates to ten of 233 Lambda functions. Five are the edge functions (`auth-validator-edge`, `shared-advisor-router`,
  `shared-advisor-router-response`, `public-data-router`, `cache-control-injector`). Today a Dell may update all 233. Investor-reporting
  work on dell2 can meet this refusal; a deploy of one of the ten is then a write-in to the laptop. If that proves frequent, narrowing
  the edge five is a cell, on a row from the seat that hit it.
- UNCHANGED IN EFFECT: no role can be passed, before or after. The named-role list is empty until the first role request is applied.
- STILL WITH NO CLOUD REFUSAL BEHIND IT: a resource policy set through `sqs:SetQueueAttributes`, `sns:SetTopicAttributes`, or at the
  creation of a key, queue, topic or bucket (rows W4-S1, W4-S2, NFRA_CTLPLN-S6). Andrew's "For now, laptop should admin" binds those
  six calls by reading only.

## Rollback per key

As the COO half states: remove the two new resources and `safe-apply`; restore the deploy policy from the commit before `c21a185724`
or set its prior IAM version as default. Nothing a Dell created under the grant is removed by a rollback.

## Conditions

1. The apply's own plan reads exactly the three lines above. Any other line voids both halves.
2. The live read-back of the COO half's condition 2, with one addition: the applied default version of `cloudops-dell-agent-deploy-policy`
   still carries the four round-2 Deny statements (IAM writes, CloudTrail writes, deletes on `opal-data-*`, table and database deletes),
   read from the live policy document, not from the repo.
3. One ledger entry, opened before and closed after, naming the laptop as the box.

## Both branches

Apply succeeds: the Dells hold the grant and the refusals above. Apply fails or is not run: the Dells hold the round-2 policy, update
any existing function, write data, and create nothing.

**SIGNED** -- `1.0.0_SA_CTO`

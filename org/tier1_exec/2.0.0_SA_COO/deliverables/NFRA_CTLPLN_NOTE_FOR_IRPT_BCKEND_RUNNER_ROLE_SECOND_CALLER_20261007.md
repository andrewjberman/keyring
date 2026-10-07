# Note for IRPT_BCKEND, held as a FILE (not a channel row): a change to irpt-ycharts-runner-role also changes what the dell2 box user can do

**Author:** `2.0.0_SA_COO~C`, 2026-10-07. Filed first as channel row `IRPT_BCKEND-S370` @7b3c62daf0; that bare id collided with a row dell2 minted under the same number on its branch, and the row gate refused the merge (`0.0.0_AB_MSTR` msg 106265). The row is withdrawn from the channel in the commit that adds this file, and its content is kept here unchanged. Asked for by the CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_NFRA_CTLPLN_DELL_DENIES_AND_DELL2_GRANT_20261007.md` @eb74cfb2d2, condition 7. Owner of the carrier from here: the seat that owns the role's Terraform (`infra/aws/terraform/investor-reporting/ycharts/iam.tf`).

The row as it was written (the id is no longer this note's):

## (withdrawn id) -- a change to irpt-ycharts-runner-role also changes what the dell2 box user can do (NFRA_CTLPLN dell2 command grant, CTO condition 7)

```json
{
  "id": "IRPT_BCKEND-S370",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T12:55:32Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "A change to irpt-ycharts-runner-role now has a second blast radius: under NFRA_CTLPLN's dell2 command grant, whatever that role may do, the dell2 box user may do by sending a command to the resident host.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "CTO half org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_NFRA_CTLPLN_DELL_DENIES_AND_DELL2_GRANT_20261007.md @eb74cfb2d2, condition 7, verbatim: 'Any later change to irpt-ycharts-runner-role (an attached or inline policy, its boundary, its trust) is a never-widen act that names this route in its blast radius ... after the apply, the owner of that role's Terraform carries it.'",
      "infra/aws/terraform/nfra-ctlpln-identity/dell2_ssm_policy.json: ssm:SendCommand to instance i-0167fd745ad906a66 with documents irpt-ycharts-deploy and irpt-ycharts-run, both taking a free-text parameter",
      "The role is declared in infra/aws/terraform/investor-reporting/ycharts/iam.tf; NFRA_CTLPLN's role census read it NO on IAM writes, audit-trail writes and production-data deletes at 2026-10-07T11:05:41Z",
      "The grant is signed and NOT applied at this row's filing (order NFRA_CTLPLN.TO-APPLY-6 pending)"
    ]
  },
  "spec_asserts": "The role's permissions were set for the resident host's own pipeline work, with the host as the only caller.",
  "world_is": "Once NFRA_CTLPLN's apply lands, the role has a second caller. A later widening of the role (a new attached or inline policy, a changed boundary or trust) widens what dell2 can do without any change to dell2's own policies, and no gate joins the two. The control today is by reading: the seat that changes this role names the dell2 route in its never-widen sign-off. The census check that would show it is infra/aws/terraform/nfra-ctlpln-identity/tests/derive_reached_roles.py --check-fresh."
}
```

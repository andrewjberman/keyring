# ANDREW-DIRECT 2026-10-07 ~06:3xZ -- Dells create resources, never IAM; deploys are not gated on site Z

**Channel:** typed at the `1.0.0_SA_CTO` terminal (laptop). **Recorded by:** `1.0.0_SA_CTO`.

## His words, VERBATIM

"Regarding DELLs, they shouldnt need to create or touch IAMs, they should be allowed to create resources though. I do not like the idea of
gating deploys on sitez, because sitez will bottleneck as it has a lot of work via opalgateway projects and all of asset management
workstreams."

It answers this seat's recommendation of the same hour ("keep IAM denied on the Dells; they build and plan, site Z applies every
Terraform change"). That recommendation is REFUSED by him on its second half.

## What this seat does on it

- NFRA_CTLPLN PRD v0.7: C-IDENTITY states that the Dell policy grants create, update and tag on non-IAM resources, and that no Dell
  deploy of a non-IAM resource waits on site Z. The IAM deny stays.
- One message to `2.0.0_SA_COO~C` naming this record: the policy change is round 3's first cell, ahead of the Lambda narrowing.

## Measured at the time of the word

- `infra/aws/terraform/nfra-ctlpln-identity/dell_deploy_policy.json` allows UPDATE of existing Lambda code, ECS task registration,
  EventBridge rules, S3 object and DynamoDB item writes. It grants NO create action for a Lambda function, a DynamoDB table, a bucket, a
  queue, a schedule, a secret or an API route. So the policy as applied is narrower than C-IDENTITY v0.6 ("safe-apply for non-IAM
  resources") and narrower than his word.
- The investor-reporting Terraform tree declares 28 IAM roles and 62 role policies beside its non-IAM resources.

## Not decided by these words (surfaced to him, not adjudicated)

1. A new Lambda or task needs a role. With IAM denied, who creates the role, and may a Dell pass an existing role to the resource it
   creates (`iam:PassRole` is denied today; surprise row NFRA_CTLPLN-W1-S1, ARMED)?
2. C-TRUNK-DEPLOY lets a Dell deploy only commits already on origin CLOUD, and site Z is the one box that merges Dell rounds and pushes
   the trunk. That is a second wait on site Z; his word names deploys and does not name the integrator role.
3. Resource policies that grant access without being IAM (a bucket policy, a key policy, a Lambda permission): inside "create resources"
   or inside "never touch IAMs".

## A second word, minutes later, VERBATIM

"I think we focus the DELLS around all the Investor Reporting work and securities database build and classification, including
client-specific work like COTBKF"

Read against the layout as it stood at that minute (`org/missions/SEQUENCE.yaml` @9f52bdd6d0): dell1 holds MDPF_SECHIST, MDPF_SECCLASS,
IRPT_BCKEND, IRPT_YCDGEN; dell2 holds IRPT_CUSTDY, IRPT_DASHBD, ADVI_COTBKF, ADVI_BILLING, NFRA_OPSWKF. Seven of those nine are inside
his sentence. No row was changed on it. Not decided: whether ADVI_BILLING and NFRA_OPSWKF, which are neither investor reporting nor the
securities database nor client-specific backfill, stay on dell2.

## A third word, ~06:4xZ, VERBATIM

"ok i like the laptop for creating roles, we can manage that for now, and the DELLS write in for that purpose"

It answers question 1 above, on this seat's recommendation as put to him: "the laptop creates roles, since it is the control plane and
not the bottleneck, and a Dell may pass only named, pre-made roles." Landed as NFRA_CTLPLN PRD v0.8, C-ROLE-REQUEST.

- THIS SEAT'S READING, stated as a reading: "the DELLS write in" means a Dell asks the laptop for a role in writing (a request the
  laptop's seats can read), and the laptop applies it. He named no carrier and no format.
- THIS SEAT'S READING, stated as a reading: a role the laptop made for a Dell is one the Dell may pass (`iam:PassRole`, named roles
  only), because a role a Dell cannot pass cannot be attached to the resource the Dell creates. His sentence does not name PassRole.
- "for now" is his: the arrangement is not ruled permanent.
- Questions 2 (the trunk wait on site Z) and 3 (access-granting resource policies) are NOT answered by this word.

## A fourth word, seconds later, VERBATIM

"i think ultimately this should change, but its ok for now"

It qualifies the third word: the laptop-creates-roles arrangement is INTERIM by his own statement. He named no end state and no date;
nothing here decides what replaces it. PRD v0.8 carries it as an enrichment-backlog line.

## A fifth word, ~06:5xZ, VERBATIM

"What is the actual reason we are hampering the dells so much? they are on prem devices, is there a basis to be holding them like this?
we also need to look over whatever COO~P COO~Y COO~M were working on on this fabric and make sure that is properly spread out across the
dell boxes. I think those two boxes are going to be workhorses."

Two questions and one direction (look over the three lanes' work and its spread). Answered to him at the terminal from the brief
(`docs/briefs/four-device-control-plane-brief-20261006.md` O9), the applied policy and the three lanes' last handoffs
(@0d44093fe1, @217963b67d, @2c281b9f29). No row, policy or seat was changed on this word; the changes it points at are his to order.

-- 1.0.0_SA_CTO

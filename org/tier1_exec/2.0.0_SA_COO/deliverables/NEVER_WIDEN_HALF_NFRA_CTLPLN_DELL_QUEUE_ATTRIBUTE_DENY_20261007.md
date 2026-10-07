# COO never-widen half -- NFRA_CTLPLN: ONE apply of the Dell identity root (deny `sqs:SetQueueAttributes` for the Dell group)

**Author:** `2.0.0_SA_COO~C`, 2026-10-07 ~14:4xZ. **Read at:** trunk `aa6b587487` (the merge of cell CT-d-5's amendment), root
`infra/aws/terraform/nfra-ctlpln-identity/`. **Counterpart owed:** a CTO half for this same act. **Authority:** `1.0.0_SA_CTO` msg
106274: "deny it for the Dell group ... One cell, one half request, narrowing only." Rows `NFRA_CTLPLN-W4-S1`, `W4-S2`, `S6`.

## The act

One `safe-apply` of the root, untargeted, at the laptop, from a commit that contains `aa6b587487`.

## The plan, MEASURED

`terraform plan -input=false -lock=false -detailed-exitcode` on the laptop, 2026-10-07 ~14:4xZ, read-only, exit 2:

```
  # aws_iam_policy.dell_agent_respol will be updated in-place
                          + "sqs:SetQueueAttributes",
Plan: 0 to add, 1 to change, 0 to destroy.
```

**Writers of the property moved (what the two Dell users may do): N = 8 documents, all read at the previous act; this act changes
one,** `dell_respol_policy.json` (74 -> 75 actions in `DenyResourcePolicyWrites`, 2,359 characters).

## Blast radius

One IAM object: a new default version of `cloudops-dell-agent-respol-policy`. It NARROWS only. No other principal, role, resource
or served output changes.

**What both Dell users lose:** every `sqs:SetQueueAttributes` call. That is the queue's access policy AND every other later
attribute change (visibility timeout, retention, redrive, encryption settings). `sqs:CreateQueue` with attributes, `sqs:TagQueue`
and `sns:SetTopicAttributes` stay allowed (the topic action is not in the ruling and is not added).

**Named so it is not read as a regression:** a Terraform root that declares a separate `aws_sqs_queue_policy` resource can no
longer be APPLIED from a Dell, on a create as well as on a change, because that resource writes through the denied action. Six
roots declare one (9 resources of 23 queues' worth): globgrph, inf-pipeline, nfra-agentbus, nfra-agentbus-alyssa01, opal-gateway,
partner-etl-ops-alerts. Whether any of the six is a Dell-placed project's root is NOT read (no project row carries a Dell fabric
value; the root-to-project mapping was not read). Such a root goes by write-in to the laptop.

## The premise the ruling rests on, as measured (cell CT-d-5's first read)

"A queue's attributes are set when Terraform creates it." Audit trail, us-east-1, 90 days, positive control 28 queue events seen:
18 of 18 Terraform creates carried their attributes inside the create call; 15 had no `SetQueueAttributes` within 120 seconds; the
3 that did are all in roots declaring a separate queue-policy resource. Verdict `create_needs_set=False`.
**Its weak point, stated:** on two of those three (both FIFO queues of one root) the follow-up call carried `DeduplicationScope`
and `FifoThroughputLimit` beside `Policy`. The worker attributes the call to the separate policy resource; the audit trail cannot
show which resource sent it. Against it being the queue resource: another FIFO create in the window sent those two names inside
the create call, and two FIFO creates today (provider 6.67.0) had no follow-up set. Other regions: unread.

## Expected outcome, BOTH branches

- **A:** the applier's plan reads exactly one in-place update of `aws_iam_policy.dell_agent_respol`, the diff one added action,
  0 to add, 0 to destroy -> apply.
- **B:** any other line or count -> apply NOTHING, report the plan as read.

## Rollback

IAM keeps the prior policy version: set it as default (same window), or revert the one entry in the file and `safe-apply`.

## Conditions

1. The plan shape of branch A, read immediately before the apply.
2. A NEVER-2 ledger entry opened at the start and closed at completion.
3. Read-back LIVE against the attached policies with matched statements: a Dell user `sqs:SetQueueAttributes` -> explicitDeny in
   `DenyResourcePolicyWrites`; `sqs:CreateQueue` -> allowed; `sqs:TagQueue` -> allowed; the live document equals the repo file
   (parsed, with a planted-mutant control); a re-plan reads no changes.
4. If a Dell-placed project's create of a queue is refused after this apply for a reason other than a separate policy resource,
   that is the weak point above coming true: the prior version is restored the same window and the CTO is told.

**SIGNED** -- `2.0.0_SA_COO~C`

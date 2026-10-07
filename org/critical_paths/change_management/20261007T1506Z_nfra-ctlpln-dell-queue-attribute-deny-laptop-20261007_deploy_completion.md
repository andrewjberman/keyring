# Deploy Completion Record
**Date opened:** 2026-10-07T15:06:12.377300+00:00
**Status:** OPEN
**Deploy:** NFRA_CTLPLN CT-d-5 as amended -- BOX: THE LAPTOP. ONE untargeted safe-apply of infra/aws/terraform/nfra-ctlpln-identity adding sqs:SetQueueAttributes to DenyResourcePolicyWrites (74 -> 75 actions), one in-place update of cloudops-dell-agent-respol-policy. It NARROWS ONLY. Closes the gap this seat found under TO-APPLY-6 (msg 106271). PRIOR DEFAULT VERSION v1, 1 of the 5-version maximum. Both halves SIGNED: COO @f9858d0ab1, CTO @2792d4cf57. CTO condition 5 SHOWN before the apply. Plan measured 0 to add, 1 to change, 0 to destroy with exactly one added action.
**Authored by:** 0.7.0_AE_CloudOps~E
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | one untargeted safe-apply of the identity root at the laptop | CTO condition 5 shown BEFORE the apply from the fabric manager's record DELL_NOTICE_QUEUE_ATTRIBUTE_DENY_SENT_20261007_1445Z.md (both Dell managers READ and acked by MessageId); plan reads EXACTLY 0 to add / 1 to change / 0 to destroy on aws_iam_policy.dell_agent_respol with EXACTLY ONE added line, + sqs:SetQueueAttributes, and ZERO removed lines; safe-apply completes 0 added 1 changed 0 destroyed |  | OPEN |
| V1 | verify | the three live arms against the ATTACHED policies, each attributed | a Dell user sqs:SetQueueAttributes -> explicitDeny with the matched statement naming DenyResourcePolicyWrites; sqs:CreateQueue -> allowed; sqs:TagQueue -> allowed. The two allowed arms are the controls that prove this Deny did not stop a Dell creating or tagging a queue, which is the weak point both halves name |  | OPEN |
| V2 | verify | the live document equals the repo file, and the version moved | parsed comparison of the LIVE default-version document against dell_respol_policy.json with a planted-mutant control; the action count reads 75 (74 before) with sqs:SetQueueAttributes present; the new default version id is recorded beside the prior v1, and the version count stays within the 5 maximum |  | OPEN |
| V3 | verify | AC1 + AC2 and the three checks re-read | simulate_policy.py reads respol_ok=13/13 ssm_ok=9/9 routes_ok=5/5 all_ok=True (AC1); the re-plan -detailed-exitcode reads exit=0, a WHOLE-ROOT 0-diff since the apply is untargeted (AC2); check_identity.py and derive_respol_actions.py re-read clean with actions=75 covered=75/75 |  | OPEN |

## Log

- 20261007T150612Z OPENED by 0.7.0_AE_CloudOps~E with 4 leg(s)

---

## BOX

**THE LAPTOP.** Executor `0.7.0_AE_CloudOps~E`, seated by `2.0.0_SA_COO~C` under task order
`NFRA_CTLPLN.TO-APPLY-7.dell-queue-attribute-deny-apply-laptop` @3fd57f4133 (GO msg 106313, acked). Applying identity
`arn:aws:iam::313476888478:user/Andrew_Berman`. Terraform v1.15.8 on PATH.

**This order closes a gap this seat found on its own initiative** under TO-APPLY-6: a resource-policy arm the order
did not ask for showed `sqs:SetQueueAttributes` reading ALLOWED, and that it was absent from the Deny's 74 actions.
The issuer also corrected the TO-APPLY-6 COO half's prose, which had listed "a queue policy" among what a Dell is
refused.

## CTO CONDITION 5 -- SHOWN BEFORE THE APPLY, and stated at the precision the record itself uses

Source: `org/tier0_exec/0.0.0_AB_MSTR/deliverables/DELL_NOTICE_QUEUE_ATTRIBUTE_DENY_SENT_20261007_1445Z.md`, written
by `0.0.0_AB_MSTR` on this seat's question (msg 106320). This seat does not message a Dell.

| claim | state |
|---|---|
| SENT to dell1 | MessageId `52451c51-afbd-4507-9f1a-9a47e54ac523` |
| SENT to dell2 | MessageId `a3b98523-74ae-45d8-b298-38ac6b2de267` |
| READ by `0.0.0_AB_MSTR~DELL1` | **ACKED BY MessageId**, bus `df644065`, 15:02:38Z |
| READ by `0.0.0_AB_MSTR~DELL2` | **ACKED BY MessageId**, bus `02816c61`, 15:03:04Z |
| relayed onward, dell1 | 6 of 6 live seats broker-DELIVERED (ids 339-344) |
| relayed onward, dell2 | 9 of 9 live seats broker-DELIVERED (ids 711-719) |
| **each seat's own read** | **NOT SHOWN** -- delivery is not a read, and the record says so itself |

So "both Dells are told" is satisfied at the level the condition asks: each Dell's fabric manager has READ it and
acked by MessageId. dell1's manager adds "TO-APPLY-7 may proceed as far as dell1 is concerned"; dell2's adds that
dell2 has no queue change in flight. The weaker onward claim is recorded as DELIVERED, not read, and is not leaned on.

**A search trap worth recording:** `comp-find 'SetQueueAttributes' org/tier0_exec` returns a MEASURED ZERO over 481
files even with this record present, because the record correctly writes the English ("a queue's policy or its other
attributes") rather than the API name. The filename was the signal. A token census is not a census of the claim.

## BLAST RADIUS -- one IAM object, narrowing only

One new default version of `cloudops-dell-agent-respol-policy`. No other principal, role, resource or served output.
No object is created, changed or deleted anywhere; this seat creates and changes **no queue**.

| before | after |
|---|---|
| default version `v1`, 1 of the 5-version maximum | a new default version, still within the maximum |
| `DenyResourcePolicyWrites` carries **74** actions | **75** actions |
| sqs actions denied: `AddPermission`, `RemovePermission` | plus **`SetQueueAttributes`** |

**What both Dell users lose:** every `sqs:SetQueueAttributes` call -- the queue's access policy AND every other later
attribute change (visibility timeout, retention, redrive, encryption settings). `sqs:CreateQueue` with attributes,
`sqs:TagQueue` and `sns:SetTopicAttributes` stay allowed; the topic action is not in the ruling and is not added.

**NAMED SO IT IS NOT READ AS A REGRESSION:** a Terraform root declaring a separate `aws_sqs_queue_policy` resource
can no longer be applied from a Dell -- on a create as well as a change -- because that resource writes through the
denied action. Six roots declare one (9 resources): globgrph, inf-pipeline, nfra-agentbus, nfra-agentbus-alyssa01,
opal-gateway, partner-etl-ops-alerts. The CTO accepts this as the intended reading of Andrew's "For now, laptop
should admin". **NOT READ BY ANYONE:** whether a Dell-placed project owns one of globgrph, inf-pipeline, opal-gateway
or partner-etl-ops-alerts -- the two agentbus roots were never a Dell's to apply. `2.0.0_SA_COO~C` owes that mapping.

## THE PREMISE'S WEAK POINT, carried not buried

The ruling rests on "a queue's attributes are set when Terraform creates it": 18 of 18 Terraform creates carried
attributes inside the create call, 15 with no `SetQueueAttributes` within 120 seconds. **The residual:** on two of
the three that did follow up (both FIFO queues of one root) the call also carried `DeduplicationScope` and
`FifoThroughputLimit` beside `Policy`, and the audit trail cannot show which resource sent it. Other regions unread.
COO condition 4 turns that into a same-window restore if it comes true, and the CTO accepted it because the cost of
being wrong is one refused create on a Dell, not a served change.

## ROLLBACK

**IAM keeps the prior version.** The prior default is **`v1`**, measured before the apply, and the policy held only
1 of its 5 permitted versions, so the apply has room and `v1` survives.

| route | act | window |
|---|---|---|
| primary | `aws iam set-default-policy-version --policy-arn arn:aws:iam::313476888478:policy/cloudops-dell-agent-respol-policy --version-id v1` | same window |
| alternative | revert the one entry in `dell_respol_policy.json` and `safe-apply` | next window |

**TRIGGERS:** AC1 or AC2 failing; the live document ceasing to equal the repo file; `sqs:CreateQueue` or
`sqs:TagQueue` ceasing to be allowed; or COO condition 4 -- a Dell-placed project's queue CREATE refused for a reason
other than a separate policy resource, which is the weak point coming true, in which case the prior version is
restored the same window and the CTO is told.

## PRE-APPLY EVIDENCE IN HAND

- **COMMIT GATE:** `git diff --stat aa6b587487 HEAD` on the root empty, `git status --porcelain` empty, a POSITIVE
  CONTROL (`aa6b587487^..HEAD` prints 6 files / 1213 insertions) and a BLOB-LEVEL pass -- 0 of the root's files
  differ between `aa6b587487` and HEAD.
- **THREE CHECKS, each `ok=True`:**
  `IDENTITY-STATIC validate=ok no_access_key=True names_from_builder=11/11 policy_size_ok=True ok=True`;
  `POLICY-SIM allowed_ok=22/22 denied_ok=19/19 passrole_ok=5/5 protected_ok=8/8 respol_ok=13/13 ssm_ok=9/9
  routes_ok=5/5 all_ok=True` (the resource-policy block moved 11 -> 13 arms with this amendment);
  `RESPOL-DERIVED services=28 with_actions=20 none=7 unsure=1 actions=75 covered=75/75 ruled_allowed_caught=0 ok=True`.
- **STEP 2:** prior default `v1`; **1 of 5** versions held, so no version-limit failure; the BEFORE document carries
  **74** actions with `sqs:SetQueueAttributes` ABSENT -- the gap, confirmed one last time at the live plane.
- **THE PLAN:** `Plan: 0 to add, 1 to change, 0 to destroy`; 1 resource block, `aws_iam_policy.dell_agent_respol
  will be updated in-place`; **EXACTLY ONE added line, `+ "sqs:SetQueueAttributes",`, and ZERO removed lines**; no
  create/destroy/replace markers. Saved: `deliverables/PLAN7_nfra-ctlpln-identity_20261007.txt`.

## INSTRUMENT NOTES

Step 6's arms run against the ATTACHED policies via `simulate_principal_policy` on the live user, with
`MatchedStatements` read on each so the deny is attributed to `DenyResourcePolicyWrites` by name rather than
inferred. One resource ARN per call. The two ALLOWED arms (`CreateQueue`, `TagQueue`) are the controls that
distinguish a scoped Deny from one that stops a Dell using queues at all -- which is precisely the weak point the
halves name, so they are evidence and not decoration.

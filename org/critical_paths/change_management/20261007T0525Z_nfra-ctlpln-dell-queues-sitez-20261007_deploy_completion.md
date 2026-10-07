# Deploy Completion Record
**Date opened:** 2026-10-07T05:25:44.607242+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261007T053245Z
**Deploy:** NFRA_CTLPLN TO-DELL-1 leg B: safe-apply of infra/aws/terraform/nfra-ctlpln-agentbus from the same detached worktree at EXACTLY origin CLOUD 0ef817adb0; plan graded UNTARGETED 2 to add/0/0, both aws_sqs_queue FIFO, no other resource type. Pair: laptop CTO half @4ab68e2c3f (both roots), laptop COO~C half + act-2 ADDENDUM (root pinned c649197dd0), site-Z CTO ADDENDUM 1 @b02f8a2f74 (pin named 6f240da3ca). PIN RECONCILED by measurement: 0ef817adb0 is a descendant of BOTH c649197dd0 and 6f240da3ca and the agentbus root diff is EMPTY from each, with a positive control proving the diff command discriminates -- so the two halves' differing pins are immaterial and both conditions hold at the applied commit. Leg A landed first. ROLLBACK: safe-apply destroy of this root only; it creates two brand-new queues and touches no existing queue (negative arm: 0 agentbus-global* live against a printed denominator of 6 agentbus queues). If leg B stops, leg A stands -- the legs do not roll back together.
**Authored by:** 0.7.0_AE_CloudOps~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B1 | activation | safe-apply of nfra-ctlpln-agentbus at 0ef817adb0 | two FIFO queues created and a 0-diff re-plan | safe-apply of infra/aws/terraform/nfra-ctlpln-agentbus from detached worktree C:/tmp/dell-identity-0ae63f9 at EXACTLY 0ef817adb0, applying the graded saved plan dell-queues.tfplan: 'Apply complete! Resources: 2 added, 0 changed, 0 destroyed.' Re-plan -detailed-exitcode rc=0, no differences. terraform state list = aws_sqs_queue.inbound[dell1], aws_sqs_queue.inbound[dell2], 2 resources, nothing else. Leg A landed first (@8db57ef669 CLOSED 5/5). Halt gate again fail-closed on the ~RV lane (row NFRA_CTLPLN-Z-S1) and again cleared by audited HALT_OVERRIDE after measuring 0 unread .md under the lane inbox root and 0 STOP/HALT-class immediately before the call; NO halt-gate pass cited. | CLOSED 20261007T053244Z |
| Q1 | verify | both queues return a URL live and read FIFO | get-queue-url + attributes | Both queues live and FIFO. get-queue-url: https://sqs.us-east-1.amazonaws.com/313476888478/agentbus-global-dell1-queue.fifo and .../agentbus-global-dell2-queue.fifo. get-queue-attributes IDENTICAL on both and equal to sqs.tf's declared locals: FifoQueue=true, ContentBasedDeduplication=true, MessageRetentionPeriod=1209600 (14d), VisibilityTimeout=30, ReceiveMessageWaitTimeSeconds=20 (long poll, not the TF default 0), MaximumMessageSize=1048576 (1 MiB, not the TF default 262144), SqsManagedSseEnabled=true with no CMK. NEGATIVE ARM pre-apply: list-queues --queue-name-prefix agentbus-global returned nothing against a printed denominator of 6 live agentbus queues. | CLOSED 20261007T053244Z |
| Q2 | verify | the live names match the agentbus-global-dellN-queue* ARNs the bus policies name | else the policies are inert and that is a row the same hour | THE POLICIES ARE NOT INERT. Live names are exactly agentbus-global-dell1-queue.fifo and agentbus-global-dell2-queue.fifo, which match the agentbus-global-dell1-queue* / dell2-queue* ARNs the two bus policies name, so the site-Z CTO ADDENDUM 1's 'if a name does not match, that is a row the same hour' does not fire. Proven by a measurement that is GENUINELY NEW post-apply rather than a re-print: simulate_principal_policy evaluates an ARN pattern whether or not the queue exists, so the pre-apply 10/10 was NOT evidence of non-inertness; re-run now against the real queues it is still 10/10, with dell1 allowed ReceiveMessage on its OWN queue and implicitDeny on dell2's, mirrored for dell2, the isolation deny carrying its positive control as a separate invocation. | CLOSED 20261007T053244Z |

## Log

- 20261007T052544Z OPENED by 0.7.0_AE_CloudOps~RV with 3 leg(s)
- 20261007T053244Z LEG B1 closed: safe-apply of infra/aws/terraform/nfra-ctlpln-agentbus from detached worktree C:/tmp/dell-identity-0ae63f9 at EXACTLY 0e
- 20261007T053244Z LEG Q1 closed: Both queues live and FIFO. get-queue-url: https://sqs.us-east-1.amazonaws.com/313476888478/agentbus-global-dell1-queue.f
- 20261007T053244Z LEG Q2 closed: THE POLICIES ARE NOT INERT. Live names are exactly agentbus-global-dell1-queue.fifo and agentbus-global-dell2-queue.fifo
- 20261007T053245Z CLOSED -- all 3 legs proven

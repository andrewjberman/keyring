# CTO never-widen half -- NFRA_CTLPLN: deny `sqs:SetQueueAttributes` for the Dell group

**Author:** `1.0.0_SA_CTO`, 2026-10-07 ~14:4xZ. **Counterpart:** `2.0.0_SA_COO~C`'s half,
`org/tier1_exec/2.0.0_SA_COO/deliverables/NEVER_WIDEN_HALF_NFRA_CTLPLN_DELL_QUEUE_ATTRIBUTE_DENY_20261007.md` @f9858d0ab1 (its msg
106307), read in full. **NOT read by this seat:** the plan, the audit-trail read behind the premise, and the simulation; they are the
issuer's measurements and the applier re-reads the plan (condition 1).

## The act and its blast radius

As the COO half states: one untargeted `safe-apply` of `infra/aws/terraform/nfra-ctlpln-identity/` at the laptop; one IAM object
(a new default version of `cloudops-dell-agent-respol-policy`, 74 to 75 denied actions). It narrows only.

## What this half signs, and the two points weighed

**Signed.** The action writes a queue's access policy, which Andrew's answer 2 of 06:5xZ puts at the laptop ("For now, laptop should
admin"); the applied Deny missed it (rows W4-S1, W4-S2, S6).

1. **Six roots with a separate queue-policy resource can no longer be applied from a Dell.** Accepted, and it is the intended
   reading of the same answer: a queue's access policy is a laptop act by write-in. The two agentbus roots are control-plane roots
   and were never a Dell's to apply. NOT read by anyone: whether a Dell-placed project owns one of the other four
   (globgrph, inf-pipeline, opal-gateway, partner-etl-ops-alerts). `2.0.0_SA_COO~C` reads that mapping and tells each Dell's CTO
   which of its roots, if any, now applies at the laptop.
2. **The premise's weak point** (two FIFO queues whose follow-up call also carried two FIFO attributes). Accepted as a named
   residual, because the COO half's condition 4 already turns it into a same-window restore if it comes true, and the cost of being
   wrong is one refused create on a Dell, not a served change.

## Conditions

The COO half's four, unchanged. One more:

5. The refusal a Dell seat meets is told to both Dells before the apply, in one line: a later change to any queue attribute, and
   any separate queue-policy resource, goes to the laptop by role request.

## Both branches

A: the plan is the one in-place update with the one added action -> apply; a Dell can no longer change a queue's policy or its
other attributes after creation. B: any other line -> nothing applied; the gap stays open and named.

**Rollback:** the prior policy version set as default, same window.

**SIGNED** -- `1.0.0_SA_CTO`

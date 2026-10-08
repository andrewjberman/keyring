# CTO never-widen half -- NFRA_CTLPLN: the Dell identity root, STEP A of three -- the Denies first

**Author:** `1.0.0_SA_CTO`, 2026-10-08 ~08:4xZ. **Counterpart read in full, all 113 lines:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/NEVER_WIDEN_HALF_NFRA_CTLPLN_DELL_IDENTITY_STEP_A_DENIES_FIRST_20261008.md` @3249b8a6fa.
**Not read by this seat:** the plan, the two live policy documents, the simulator's output.
**Authority:** Andrew-direct 2026-10-08 ~00:4xZ (items 1 and 3 lifted; record @14a030c049); this seat's rulings 106781 (three
Denies), 106838 (the seven audit-bucket settings; the Denies before plan 1), 106743 (dell2's parameter read by exact ARN).

## What this half signs

The act the counterpart names: one `safe-apply` of `infra/aws/terraform/nfra-ctlpln-identity/` TARGETED at exactly
`aws_iam_policy.dell_agent_create` and `aws_iam_policy.dell_agent_deploy`; `0 to add, 2 to change, 0 to destroy`; 54 lines added,
none removed; `apply_respol_allow` not passed.

## Weighed

1. **This step takes seven things away from the Dells that they can do today** (the audit-trail bucket's lifecycle, logging,
   notification, encryption, versioning, ownership controls and public-access block). It is a narrowing made on a night Andrew
   asked for widening, so it is stated plainly: no Dell project owns that bucket, and a lifecycle rule there can delete the
   audit log. This seat ruled it in; he is told in those words.
2. **The claim that no Dell run needs any of the seven is from the placement register, not from a read of running jobs.**
   Accepted on this ground: a Dell job that writes the audit bucket's settings or an agentbus queue's attributes would itself
   be a finding. If one is refused, it reports by name and this seat hears it the same hour.
3. **Two small widenings ride because they live in the same document:** self-simulate (already signed in plan 1) and one
   public parameter read by exact ARN. The second is what dell2 has been refused since ~00:3xZ and it lands here, a step
   earlier than planned. Good.
4. **The three exclusions and these seven are this seat's interim reading of what Andrew lifted**, as the 28 platform keys are.
   His words named "bucket policies, key policies, Lambda permissions, queue policies". Holding out the audit bucket, the ten
   protected functions and the four agentbus queues is narrower than those words. He has been told each and has not answered;
   one apply reverses any of them.

## Blast radius

Two managed policies; two principals through one group. No resource policy, key policy, queue or bucket is itself changed.

## Expected outcome, BOTH branches

As the counterpart's, A and B.

## Conditions

1. The counterpart's conditions 1 to 6 stand.
2. Order of the three steps: A, then B (plan 1, now reading `2 to add, 0 to change, 2 to destroy` at the same five targets;
   this seat's plan-1 half is amended to that shape in the same commit as this file), then C under its own pair.
3. The applied time comes to this seat and goes to dell2 the same minute; dell2's own `terraform plan` of the YCharts root is
   the exercise.

**SIGNED** -- `1.0.0_SA_CTO`

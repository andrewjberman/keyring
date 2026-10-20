# NFRA_FIDUPL: Andrew's "turn off autoshutdown for this box", ruled (1.0.0_SA_CTO~DELL1, 2026-10-20 ~12:58Z)

**Inputs:**
- Andrew's word, verbatim: "tell htme the secret has been set, also we need to turn off autoshutdown for this box".
  Record: `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261020_125xZ_FIDELITY_SECRET_SET_AND_AUTOSHUTDOWN_OFF.md`
  @ff8fe16ade, relayed by MSTR~DELL1 (msg 8616).
- 4.0.0_SA_CRO~FIDELITY, msg 8619.
- 2.0.0_SA_COO~P1, msg 8620. P1 asked two questions: (1) is this an addendum cut now, or a round-2 item; (2) does
  automation.tf keep its stop-after-run step.

**Measured, 12:54Z:**
- Secret `fidelity/alongside/wealthscape-credentials` has an AWSCURRENT version, LastChanged 2026-10-20T12:49:08Z. Only the
  stage was read, never the value.
- Instance `i-028e830f7226cc685` is `stopped`. Its only tag is `Name=fidelity-alongside-uploader-runner`.
- The enforcer's only exemption is the tag `AutoShutdown=disabled`: the comment at
  `infra/aws/lambda/ec2-auto-shutdown-enforcer/lambda_function.py:18` and the check at `:114`.
- `infra/aws/terraform/canonical-fidelity-ec2/automation.tf:129-135` stops the instance at the end of every run.

## Rulings

1. **Cut it now, as one small order. It is not a round-2 item.** It is Andrew's direct word on a live box. It is one root
   edit and one re-apply under `safe-apply` by `0.7.0_AE_CloudOps~NFRA1`, so FWD-7 holds and nothing is console-only. The
   order cites this file and Andrew's record.
2. **The order does two things in one root edit:**
   - (a) Add `AutoShutdown=disabled` to the instance's tags in `canonical-fidelity-ec2`.
   - (b) Remove the `stopInstance` step from the automation document.

   Why (b): this box has two automatic shutdowns. Each run stops the box itself, and the enforcer reaped the box only
   because it sat idle after the apply. The tag alone would leave the box stopped after every run, so the plain reading of
   "turn off autoshutdown for this box" covers both. The `startInstance` step stays; on a running box it is a no-op.
3. **Timing:** the apply waits until FU-x-1's single automation run has ended, and no execution may be in progress during it.
   FU-x-1's trace is graded against the document it started with. The order's proof reads three things: the tag on the
   instance, the document version without the stop step, and a `terraform plan` showing no changes after the apply.
4. **Andrew can still correct the reading.** If he meant only the enforcer, step (b) is reverted in the same root. That
   adds nothing to the order and does not gate it.

Cost note: a t3.medium kept running is roughly $30 a month. Andrew's word covers it.

-- 1.0.0_SA_CTO~DELL1

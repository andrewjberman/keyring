# CTO never-widen half -- NFRA_CTLPLN: the Dell identity root, STEP H -- the Dells may READ /opal/ui-walker/password

**Author:** `1.0.0_SA_CTO`, 2026-10-09 ~01:1xZ. **Counterpart read in full** (45 lines, 2,904 bytes):
`org/tier1_exec/2.0.0_SA_COO/deliverables/NEVER_WIDEN_HALF_NFRA_CTLPLN_DELL_IDENTITY_STEP_H_UI_WALKER_READ_20261009.md` @21dd3c2c23
(msg 107565), signed by `2.0.0_SA_COO~C`; order NFRA_CTLPLN.TO-APPLY-22. **Not read by this seat:** the plan output, the simulator output.
**Authority:** this seat's msg 107538 (ssm:GetParameter ONLY on exactly `/opal/ui-walker/password`; no DeleteParameter, on dell1's
correction msg 1326), under Andrew's word ~22:0xZ "the dells need to be able to deploy" (record addendum
`ANDREW_DIRECT_20261008_220xZ_ONE_LAPTOP_APPLIER_EXCEPTION_YES.md`).

## What this half signs

The act exactly as the counterpart names it: a TARGETED plan and apply at `aws_iam_policy.dell_agent_plan_reads`, `0 to add, 1 to
change, 0 to destroy`, one statement added (Sid `ReadUiWalkerPassword`, Allow `ssm:GetParameter` on
`arn:aws:ssm:us-east-1:313476888478:parameter/opal/ui-walker/password`), none removed. Blast radius in plain words: a Dell seat can read
the dormant walker account's portal password, which is what /ui-walk already needs; DeleteParameter, GetParameters and every sibling
parameter stay refused. Both branches as the counterpart states them: A applies; B (anything else, or any change to
`aws_iam_policy.dell2_ssm`) applies nothing and reports.

## Conditions (the counterpart's 1-4, plus these)

5. **Re-enabling the walker login is not covered.** It stays disabled (dell1's disarm); turning it back on is a separate decision.
6. **The deferred convergence is owned, not forgotten.** The targeted apply leaves `aws_iam_policy.dell2_ssm` deliberately unconverged
   while TO-APPLY-20 is open. After TO-APPLY-20's leg C2 closes the window (X1 or the 06:00Z hard close), the next untargeted plan of
   this root must read `0 to add, 0 to change, 0 to destroy`; `2.0.0_SA_COO~C` reads it and reports the result to this seat. Any other
   result is reported before anything is applied.
7. No value of the parameter is read at any step, including the read-back.

**SIGNED** -- `1.0.0_SA_CTO`

# CTO never-widen half -- NFRA_CTLPLN: the Dell identity root, STEP F (cell 3) -- IAM role/policy writes and plan reads

**Author:** `1.0.0_SA_CTO`, 2026-10-08 ~23:2xZ. **Counterpart read** (77 lines, blast radius and conditions in full):
`org/tier1_exec/2.0.0_SA_COO/deliverables/NEVER_WIDEN_HALF_NFRA_CTLPLN_DELL_IDENTITY_STEP_F_IAM_ROLES_AND_PLAN_READS_20261008.md`
@6734d80272 (msg 107455). **Not read:** the plan, the simulator output.
**Authority:** Andrew-direct ~13:2xZ, "2.) LIFT ITEM 4"; ~22:0xZ, "the dells need to be able to deploy" (record addendum
`ANDREW_DIRECT_20261008_220xZ_ONE_LAPTOP_APPLIER_EXCEPTION_YES.md` @f28690b46f).

## What this half signs

The act as the counterpart names it (plan 4/1/0). In plain words, as the counterpart states: a Dell can then give itself any
permission a policy can express, so every remaining Deny holds only as long as a Dell honours it; IAM users, access keys, login and
MFA settings stay refused. This is what Andrew lifted.

## The points, ruled

1. **W14-S31 -- GRANT.** `opal/auth/irpt-render-jwt-public-key` is a public key; re-class it in the census from OTHER to a granted
   read class, as a one-line ruling row in the same cell or the next, so dell2's portal-auth plan reads it.
2. **W14-S32 (ARMED, mine) -- disarmed by a narrowing cell.** Cut one small cell: an explicit Deny of `ssm:PutParameter` on the
   bd-to-schwab cutover parameter only (by exact name). After this step a Dell could lift that Deny itself, so the Deny guards
   against accident, not intent; it is still worth one statement for a value every box depends on.
3. **Condition 4 -- ADOPTED.** A Dell that creates or changes an IAM role or policy reports it after the fact by bus (name, what it
   grants), as the D2 send report. A change that touches a role another box's pipeline assumes stays under the step-C before-rule
   (tell the laptop first).
4. **W14-S33** -- retire `tests/render_passrole.py`'s removed-Deny assertion in the same follow-up cell.
5. **dell2's pre-staged REOPEN of the F1 shell window for a new ledger (dell2 msg 1901)** -- consent on the same terms as before: the
   one F1 host only, opened on dell2's request, closed at that ledger's X1, hard close 2026-10-09T06:00Z without waiting. My earlier
   consent named only the svc ledger; this extends it to the named new ledger, nothing wider.

**SIGNED** -- `1.0.0_SA_CTO`

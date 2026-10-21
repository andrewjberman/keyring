# DELL1 self-drive box -- ticks 230-231, 2026-10-21 ~09:48-10:19Z (hour floor; the first two scheduled Fidelity fires FAILED before the box; the automation path is unproven)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 10:19Z. Acked since tick 229: 9050.
- open_calls.json: 163 rows, 4 OPEN: 89c9 and ea86 (Andrew's); 3bc7 and 5013 done or withdrawn, held CROSS-BOX by the tool. The
  per-firm Groups act for Andrew stands (ruling @4c536cb554).

## Acts and rulings
- **The 09:45Z fire failed at the EventBridge-to-SSM hop** (read by me at 09:52Z): `AWS/Events` `Invocations 1, FailedInvocations 1`
  for `leg-1-daily`; no automation execution since 09:00Z; no SSM command on the box since 08:44Z; no run record. Target: the SSM
  automation document `fidelity-alongside-uploader-document`, input `{"InstanceId":["i-028e830f7226cc685"]}`, role
  `fidelity-alongside-schedule-role`. **Ruled:** measure the hop (StartAutomationExecution, PassRole, the document's parameters)
  and fix under safe-apply. My simulate: StartAutomationExecution allowed; PassRole implicitDeny (P1: the simulator lacked the
  `iam:PassedToService` context; the grant exists). The target ARN carried no `:$DEFAULT` suffix (schedule.tf:82); P1 ordered
  FT-s-12 (@79b357f4ea5), NFRA1 applied it (@bceacf5a4ff, 10:01Z; read by me: `...document:$DEFAULT` on leg-2).
- **The 10:15Z fire failed too** (read by me at 10:19Z): `leg-2-daily` `Invocations 1, FailedInvocations 1`; no execution. The
  document's only executions ever (2026-10-20 09:01Z and 16:53Z) read `Failed`, `CurrentStepName None`: every landing so far ran
  by send-command, so the scheduled automation path has NEVER succeeded end to end; the suffix was necessary, not sufficient.
  **Ruled** (10:20Z): NFRA1 reads the FailureMessage of those executions, fixes the document or the start parameters, and proves
  the path with ONE manual start-automation-execution shaped like the rule target (a sign-in, under the cap), before the 10:45Z leg
  if it can be; the schedule stays ENABLED (a non-fire is not a wrong fire); the schedule-ON addendum's section 3 records the two
  failed fires. The deliverable-1 claim "scheduled" is therefore NOT yet proven by a fire; the stop condition is not met.
  - **The cause, by P1's CloudTrail read** (9053): `StartAutomationExecution` at 10:15:02Z by the schedule role answered
    AccessDenied on `arn:aws:ssm:us-east-1:313476888478:document/fidelity-alongside-uploader-document` ("no identity-based policy
    allows"): SSM authorizes the start against the DOCUMENT ARN form, and the policy allowed only the `automation-definition/`
    forms. Both fires reached SSM. P1 ordered FT-s-13 (@1b5d086b15): one resource ARN added to the schedule policy, safe-apply,
    ledger first; the 10:45Z leg is the proof. **Ruled:** GO; and before the leg NFRA1 simulates the AUTOMATION role for every
    action the document's steps call, because its two historical executions (read by me) failed one hop later: 2026-10-20 09:01Z
    `ec2:DescribeInstanceStatus` not authorized, 16:53Z `ssm:ListCommands` not authorized (the latter granted since by FU-s-13);
    any FAIL rides the same apply. A third failed fire is answered by a manual rule-shaped start, not a fourth fire.
- **Backfill:** unchanged since tick 229 (2026-10-16 landed, four of six); run 6 after the proven fire.
- **AMGT_HARVST:** no change; W1 at 60m.

## Scope state
- **NFRA_FIDUPL:** FT-s-11, FT-s-8, FU-s-11, FU-x-1 pending. 33 objects under `fidelity/alongside/bronze/` (10 data, 23 run
  records). Rules ENABLED but the automation target has not run once; no firm prefix. UNREACHABLE half (the split) unchanged.
- **AMGT_HARVST:** round 100, co-7 stage 7 pending.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **Per-firm account Groups in Wealthscape:** create one Group per firm, or say the word for a seat to (ruling @4c536cb554).
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).
- **Conditional:** a back-dated export profile, only if the wizard's date field cannot be automated on the backfill (CRO 8916).

## Compiler Tools
- `cloudwatch get-metric-statistics` (AWS/Events per rule), `events list-targets-by-rule`, `ssm describe-automation-executions`,
  `ssm get-automation-execution`, `iam simulate-principal-policy`.

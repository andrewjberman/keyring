# DELL1 self-drive box -- ticks 232-233, 2026-10-21 ~10:48-11:19Z (hour floor; the Fidelity scheduler path PROVEN by a one-shot rule after a third failed leg)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 11:19Z. Acked since tick 231: 9053, 9058, 9063, 9068, 9072.
- open_calls.json: 163 rows, 4 OPEN: 89c9 and ea86 (Andrew's); 3bc7 and 5013 done or withdrawn, held CROSS-BOX by the tool. The
  per-firm Groups act for Andrew stands (ruling @4c536cb554).

## Acts and rulings
- **The document path proven** (P1 9063; read by me): NFRA1's manual rule-shaped start at 10:27Z ran Success in 77 s (startInstance,
  waitForOnline, runWrapper) and landed ALL six files for content date 2026-10-20 (`account` 3,797,333 B, `balance` 1,222,782,
  `position` 30,333,376, `prices` 647,773, `security` 657,657, `transact` 235,734). Before it, NFRA1 simulated the automation role for
  the document's seven step actions: six allowed, `ssm:GetCommandInvocation` missing, added (FT-s-13 complete @0c8a7a86717) and,
  being uncalled by the document (CloudTrail), revoked again as FT-s-14 (@7836a843576).
- **The 10:45Z leg failed, the third** (read by me at 10:49Z): `leg-3` Invocations 1, FailedInvocations 1; CloudTrail 10:45:04Z
  AccessDenied for the schedule role on `arn:aws:ssm:...:automation-execution/*`, a THIRD resource form SSM checks for a start.
  **Ruled:** add it, simulate all three forms, and prove the ROLE path today with one one-time schedule rather than wait for
  tomorrow's 09:45Z. P1 ordered FT-s-15 (@1a79c6019aa): the grant, ft15s on all three forms, and ONE temporary one-shot EventBridge
  RULE with leg-1's role, target and input (a Scheduler entry would use a different role and prove nothing).
- **The scheduler path PROVEN** (read by me at 11:05-11:07Z; P1 9072): rule `fidelity-alongside-oneshot-proof-20261021`
  (`cron(05 11 21 10 ? 2026)`) fired 11:05:19Z; the schedule role started execution `f355c7f9-...` (InProgress at `runWrapper`
  when I read it; Success 11:06:30Z per P1), Invocations 1, no FailedInvocations; ALL_LANDED 6 of 6 (skipped_existing, the same
  content as 10:28Z); the rule deleted; FT-s-15 complete @88337131414. Three failures today, three causes (the version suffix,
  the `document/` form, the `automation-execution/*` form), each fixed under safe-apply. The schedule-ON addendum's section 3
  carries the three failed legs and the one-shot (P1 @3498c93b5d8, corrected @6c410be6b81). The first real scheduled fire is
  tomorrow 09:45Z.
- **Released on the proof:** the thirtieth code sync (land.py's trading-day landing rule, split.py, the backfill repairs; complete
  @ddf7b0007e1) and backfill run 6 (FT-s-11 step 3F @5a8df0d011d, `--skip-files transact.txt`, 11:20Z or later).
- **AMGT_HARVST:** no change; W1 at 60m until 2026-10-22 09:30Z.

## Scope state
- **NFRA_FIDUPL:** FT-s-11, FT-s-8, FU-s-11, FU-x-1 pending. 41 objects under `fidelity/alongside/bronze/` (16 data: 20261019 x6,
  20261020 x6, 20261016 x4; 25 run records). Rules ENABLED and the scheduler path proven end to end. Deliverable 1: scheduled, enabled,
  proven; the per-firm SPLIT remains UNREACHABLE until Groups exist (Andrew's act). Deliverable 2: earliest landed 2026-10-16 for
  four file types; run 6 walks on.
- **AMGT_HARVST:** round 100, co-7 stage 7 pending.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **Per-firm account Groups in Wealthscape:** create one Group per firm, or say the word for a seat to (ruling @4c536cb554).
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).
- **Conditional:** a back-dated export profile, only if the wizard's date field cannot be automated on the backfill (CRO 8916).

## Compiler Tools
- `cloudwatch get-metric-statistics` (AWS/Events per rule), `cloudtrail lookup-events` (StartAutomationExecution errors),
  `ssm describe-automation-executions`, `events describe-rule`, `list-objects-v2`.

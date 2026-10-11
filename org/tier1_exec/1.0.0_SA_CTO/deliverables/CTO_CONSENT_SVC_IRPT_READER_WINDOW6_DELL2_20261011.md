# CTO consent -- svc-irpt secret-reader WINDOW 6 for dell2 (IRPT_ANLREQ rev 6 live-call arm)

From 1.0.0_SA_CTO (laptop), 2026-10-11 ~04:3xZ, on 0.0.0_AB_MSTR msg 108197 (dell2 2.0.0_SA_COO~G2 msg 4050).

## Consent: YES, on window 5's terms exactly

- **Act:** ADD `cloudops-dell2-agent-user` to the resource policy of
  `arn:aws:secretsmanager:us-east-1:313476888478:secret:irpt/svc-irpt-analysis/password-rfHf9l`, then REMOVE.
- **Policy files (the only bytes put):** ADD =
  `org/tier1_exec/2.0.0_SA_COO/deliverables/SVC_IRPT_READER_POLICY_ADD_dell2_window_20261008.json`; BEFORE =
  `org/tier1_exec/2.0.0_SA_COO/deliverables/SVC_IRPT_READER_POLICY_BEFORE_restore_20261008.json`.
- **Order form:** `org/tier2_senior/0.7.0_AE_CloudOps~CTL/task_orders/NFRA_CTLPLN.TO-APPLY-30.svc-irpt-reader-dell2-window-served-read-laptop.md`,
  window 6 appended as windows 2-5 were. This file is the per-ledger CTO consent that form requires, and the GO.
- **Executor:** `0.7.0_AE_CloudOps~CTL`, spawned by `0.0.0_AB_MSTR` (neither it nor `2.0.0_SA_COO~C` is live). Under
  MP-20261010 it comes up Sonnet 5.5 high.
- **Blast radius:** this one secret's resource policy. No `GetSecretValue` by the executor, no other secret, key or
  principal, no shared-branch push.

## Steps (window 5's, with its one FAIL remedied)

1. Read the live policy: set-equal to BEFORE, else STOP and report.
2. NEVER-2 ledger entry opened (`deploy_ledger.py open`, 2 legs ADD / REMOVE).
3. **START CONDITION (amendment 04:3xZ, G2 msg 4070 via MSTR 108201/108202): the ADD is put ONLY on a message from
   `1.0.0_SA_CTO` titled "WINDOW 6 START", sent when G2 reports irpt-status reads `6idtFvAm`; the 30-minute close runs from
   the put, so an early put would close the window before the release lands. Steps 1-2 run now.** Then
   `put-resource-policy --resource-policy file://<ADD> --block-public-policy`; read back set-equal to ADD; simulate
   `GetSecretValue`: dell2 user ALLOWED, dell1 user explicitDeny.
4. **FIRST act after the read-back:** send the PUT TIME to `0.0.0_AB_MSTR` for relay to `2.0.0_SA_COO~G2` (window 5's
   relay-ordering FAIL; TO-31 step 5's remedy, 85 s). Everything else waits behind that send.
5. REMOVE at G2's "R done" (via MSTR) or PUT TIME + 30 minutes, WHICHEVER FIRST: put BEFORE; read back set-equal to
   BEFORE; AC1 `get-resource-policy ... --query ResourcePolicy` reads `WalkerReadsByExplicitArn`; ledger closed; close
   time to MSTR for G2.
6. Log under the CTL lane as for windows 1-5.

## Why yes

Window 6 serves the LIVE-CALL arm (R3/R4/R5) that this seat made standard after rev 4 passed acceptance while 500-ing
every caller. The rev 6 release (built `6idtFvAm`, rollback rev 3) is graded on it. The window is the same bounded act
executed five times, read back set-equal each time, with a clock-closed hard bound.

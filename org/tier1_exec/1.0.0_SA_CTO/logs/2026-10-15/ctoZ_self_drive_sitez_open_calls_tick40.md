# /self-drive sitez open calls -- tick 40 (14:2xZ-14:4xZ 2026-10-15), `1.0.0_SA_CTO~Z`

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md`
@ce0ba39d90. Covers the span since tick 39 (@ddac826275). **state: ARMED.**

The 11:50Z and 12:50Z ticks did not run: the session was logged out from about 12:00Z to 14:1xZ, and the account changed.
The inbox watcher was dark for the same span. Delivery state since 11:30Z reads READ 1 of 1, so no mail was missed.

## Measured

- `open-calls.py list`, run under `py -3.11` (see the outage): rows 46, open 8. Every open row is a person act.
- **Site Z Python outage, 14:02Z.** An unattended MSI upgrade from 3.14.7 to 3.14.8 installed the Core, Executables and
  Launcher, then removed the 3.14.7 Standard Library, pip, Tcl/Tk and Dev Libraries. It never installed the 3.14.8
  Standard Library. Source: Application log, MsiInstaller events 1033, 1034, 11707 and 11724. `C:\Program
  Files\Python314\Lib` holds only site-packages.
  - I reported it to `0.0.0_AB_MSTR~Z` at 14:27Z.
  - MSTR~Z's stopgap (msg 34439): in Git Bash, `~/bin/python` forwards to 3.11.9. PowerShell, native callers and pinned
    Python314 interpreters stay broken until an elevated repair, which MSTR~Z has asked Andrew for.
  - I told six Tier-2 seats (CloudOps ~Z, ~ZW, ~ZS, ~ZQ, ~MI, ~MQ).
  - The harvest runner, pinned to the 3.14 pythonw, is failing (per MSTR~Z). Re-pointing it is `2.0.0_SA_COO~O`'s call.
    I told ~ZW not to grade OG-eg-2's first-cycle-record leg on any run after 14:02Z.

## Rulings and acts

1. **XB-20261015T121713Z-e670 (laptop COO~C, NFRA_CTLPLN FWD-24): OWED.** The question: is research owed for an IAM
   write on a production Lambda role, stakes S3? Read from `research-owed.py --stakes S3`, rule line
   `.tools/research-owed.py:5`. Answer file @284cba9fbf. Crossbox ACKED at 14:36:38Z, and the ack line went to COO~C.
2. **CRO~Z finding @bc96669f7e (the OG-ap-20 key_rulings rows cannot clear the gate): CLOSED.** Its route 1 landed as
   OG-ng-1 @bf9198273e, and ap-20 is live. No rows are owed and no R20 departure is needed.
3. **OPAL_BBGTML focus defect (11:2xZ):** owner COO~ZB, ruling @701a4c705a. The R7 trace was cut @ccecc2605e. Andrew's
   sign-in was added as act f6f4.

## Moved without a call (since tick 39)

- **OG-ap-20 is LIVE at `06cfb6db64`.** Ledger `nfra-oplgtw-gateway-release-g5a` closed at 11:21Z with all 5 legs proven,
  AC1 and AC2 PASS. ap-21 Phase A GO was sent by COO~O.
- MX-c-19 complete (@50dbc2574f); MX-c-20 (index the six ap-20 tools) cut (@a1003e7f06).

## Acts only Andrew can do (each with its citation)

1. One MC Portal sitting, including one sign-in as Opal Bloomberg (21d9; covers 21c5, 8ed7, f0d2). Citation: his login
   and a human read.
2. One sitting with Alyssa (def4; 3b41 is a duplicate). Citation: his person act.
3. One Teams message from his account to Opal Bloomberg (a519). Citation: his own account.
4. **NEW:** sign the Bloomberg Terminal in at site Z (f6f4). Citation: his login.
5. Elevated repair of Python 3.14.8 on site Z: MSTR~Z's ask to him, not on this list.

## Completion test

NOT DONE: 8 open calls, every one a person act. No call is open for a decision.

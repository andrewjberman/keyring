# /self-drive sitez open calls -- tick 41 (14:51Z 2026-10-15), `1.0.0_SA_CTO~Z`

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md`
@ce0ba39d90. Covers the span since tick 40 (@9755fc26e5). **state: ARMED.**

## Measured

- `open-calls.py list` (Git Bash `python` = 3.11.9, the stopgap): rows 46, open 8 before this tick, 7 after.
- Inbox: 0 unread.

## Rulings and acts

1. **Close `sitez-20261015T112146Z-f6f4` (sign the Bloomberg Terminal in at site Z) as DONE by the act.**
   - A human completed the open sign-in window, and DAPI was up from about 11:3xZ to 14:2xZ.
   - `0.0.3_BG_BBGTerminal` re-fired the pull at 14:24:56Z, rc=0.
   - Served `data_as_of` 2026-10-14, which is T-1 (normal), verified by content at 14:37Z (msg 34459; `2.0.0_SA_COO~ZB`
     drive log @97fc54a0a4).
   - Zero Bloomberg attempts were spent.
   - The focus-at-submit defect itself is not cured. It stays open under OPAL_BBGTML: R7 (the foreground trace) landed
     @3aaf87a486, AC1 to AC3 PASS, ledger closed @6da6d3685b. COO~ZB grades R7 on the next failed fire's trace or a
     clean sign-in.

## Moved without a call

- OG-rv-3 checks amended (@d6259e35aa). COO~O's 14Z drive log names the Python outage and the harvest runner
  (@c165c34bfc).
- MSTR~Z recorded the crossbox acks for the laptop CTLPLN calls XB-cdab and XB-b11c (@e4d6a2188d).
- The Python 3.14 outage stands: the Bash stopgap works, and the elevated repair is Andrew's act, asked by MSTR~Z.
  COO~MP filed it as NFRA_MCPORTAL-Z-S53 (@8c22927bbc).

## Acts only Andrew can do (each with its citation)

1. One MC Portal sitting, including one sign-in as Opal Bloomberg (21d9; covers 21c5, 8ed7, f0d2). Citation: his login
   and a human read.
2. One sitting with Alyssa (def4; 3b41 is a duplicate). Citation: his person act.
3. One Teams message from his account to Opal Bloomberg (a519). Citation: his own account.

## Completion test

NOT DONE: 7 open calls, every one a person act. No call is open for a decision.

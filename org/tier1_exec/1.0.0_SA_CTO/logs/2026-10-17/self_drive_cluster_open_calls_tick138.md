# self-drive cluster open calls -- ticks 137-138 (2026-10-17 ~03:3xZ to ~04:0xZ), 1.0.0_SA_CTO laptop

state: ARMED   cadence: 30m   cron: 9d30d669   ticks covered: 137-138 (137 was quiet, appended to `org/mcp/drive_ticks/1.0.0_SA_CTO.md`)
arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261011_032xZ_CTO_LEADS_CLUSTER_OPEN_CALLS_LOOP_60M.md`

## Measurements (tick 138, ~04:04Z)

- 4 boxes read, none absent. 11 open (3 fork, 7 act, 1 approval), 319 closed. By box: laptop 2, sitez 4, dell1 2, dell2 3.
- Open cross-adjudications: 0 (58 in total). Inbox: msgs 109790 and 109802 read and acked. The inbox Monitor was re-armed at its expiry.

## Driver acts since tick 136

- **ADVI_FIRMBKTS TO-FB-q-1 (IB-pr-551 export fence) is COMPLETE.** Done by `0.7.0_AE_CloudOps~ADVI1`: record cb5ee5e9c5,
  status commit 25e7759c29, ledger closed 4 of 4, msg 109802.
  - Before the apply, this seat checked that both halves state the true reach: dell2 CTO 1045f1b75b and COO S2 300f9d398d,
    18,257 objects (ruling c783217cff).
  - **Independent live read by this seat** (`s3api get-bucket-policy opal-data-49financial`, ~04:05Z): 37 statements.
    - `AllowScopedExemption3Objects`: Allow `s3:GetObject` to `irpt-export-render-role` only, on two resources (the
      ownership_map key and `irpt/49financial/platinum/reporting/*`).
    - `DenyScopedExemption3ObjectsOutsidePrefix`: NotResource carries the same two. This matches the signed reach.
  - `~ADVI1` has no further order. It may stand down under rule 34(a).

## Calls this tick

- `dell1 c2a5` (new, B1; FB-p-2 needs a reader for the 13:30Z fire while COO~D1 is not registered). The call belongs to dell1's
  CTO under its own 10-minute scan. It has not been escalated here, so this seat does not rule it. B1's REC, that it reads the
  plain log line itself, is in pattern.
- `dell1 0cf5`: the DONE WHEN confirmation is Andrew's L2 act. It is dell1's own call.
- `dell2 3c22`: still HELD for Andrew (C-V1).

## Acts only Andrew can do (each with its citation)

- `dell2 f1bb`: approve the client-facing Investor Reporting > Performance tab (49 Financial template) for portal DEV.
  Citation: CLAUDE.md Portal, "client-facing for Andrew".
- `dell1 0cf5`: confirm the ADVI_COTBOOKS DONE WHEN lines. Citation: rule 27 L2, "Andrew's word".
- `dell2 3c22`: lift IRPT_YCDGEN C-V1 (PRD line 312, "DEFERRED on Andrew's word only") for the AR variants. REC: yes, after r34j.
- The CRM zip landing as `Andrew_Berman_Console` through the break-glass role. Citation: X15 condition 1.
- His MFA code, `bash ~/m365_pulls/mfa.sh <code>`, so that agents can pull M365 records through the door. It is his MFA device.
- `laptop 2396`: the CA-n-3 retest. `laptop b87f`: the remote-desktop sitting.
- `sitez 8ed7`, `sitez f0d2`, `sitez 5b35`.
- NFRA_CTLPLN FWD-2, FWD-6 and FWD-27. The TCKT_MTADTA audit-log check with IT.
- Postponed: `sitez def4`, `dell2 c02c`.

## Completion test

NOT DONE. The scope ends only on his stand-down.

## Compiler Tools

- `open-calls.py list --all --cloud`: OK. `xadj.py list --state OPEN`: OK (0).
- `.tools/aws s3api get-bucket-policy`: OK.

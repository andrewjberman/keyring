# self-drive cluster open calls -- tick 102 (2026-10-16 ~09:3xZ), 1.0.0_SA_CTO laptop

state: ARMED   cadence: 30m   cron: 9d30d669   ticks covered: 102
arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261011_032xZ_CTO_LEADS_CLUSTER_OPEN_CALLS_LOOP_60M.md`

## Measurements

- Cluster list read at ~09:32Z: 4 boxes read. 11 open (1 fork, 10 act), 277 closed.
  By box: laptop 2, sitez 5, dell1 2, dell2 2.
- Open cross-adjudications: 0. Inbox: 0 unread.

## Changes since tick 101

- Site Z closed `35b3`. dell1 closed `0017`.
- NFRA_CTLPLN intake:
  - the waiver tool merged at 6f07651fdf;
  - this seat added the four `WAIVE ... check 6` lines @9eb4ea9f37 (parse_waivers dry-run 4 of 4 bind to their own file;
    the idna control is empty);
  - COO~C re-runs the release, then packs and Taildrops the 17 wheels to dell2.
- TCKT_MTADTA on dell1: the door and the collector are live in AWS (per dell1 `d9cb`). Two new rows are his.

## Calls this tick

- `dell1 d9cb` (act): register the M365 audit collector app and grant `ActivityFeed.Read` admin consent. This is his Entra role
  and his consent. The card is `TCKT_MTADTA.TO-MD-r2.andrew_consent_card.md`.
- `dell1 6601` (fork, but the act is his): IAM user `Andrew_Berman` holds two MFA devices, `mfa/Andrew_Phone` and
  `mfa/Yang_Phone`. The door's MFA gate tests that some device was used, not whose. Removing a device is an IAM act on his user.
  REC (dell1's, which this seat concurs with): remove `mfa/Yang_Phone` unless it was registered on purpose.

## Acts only Andrew can do (each with its citation)

- `dell1 d9cb`: the Entra app registration and consent (his role, his consent).
- `dell1 6601`: keep or remove `mfa/Yang_Phone` on `Andrew_Berman` (his IAM user).
- The muse frames: confirm or deny each "on Andrew's word" ask (his word), plus the SSH reach.
- `dell2 e260`: deactivate the never-used `Opal_Terminal` key (his entitlement).
- `sitez 21d9` (+ 21c5, 8ed7, f0d2): his sitting and sign-in.
- `laptop b87f`, `laptop 44eb`: person acts. NFRA_TRNSPT S11: the Research invite. `sitez def4`, `dell2 c02c`: postponed.

## Completion test

NOT DONE. The scope ends only on his stand-down.

## Compiler Tools

- `open-calls.py list --all --cloud`: OK, 4 of 4 boxes.
- `xadj.py list`: 0 OPEN.
- `intake_check.parse_waivers` dry-run: OK.

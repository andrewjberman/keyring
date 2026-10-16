# self-drive cluster open calls -- tick 109 (2026-10-16 ~13:3xZ), 1.0.0_SA_CTO laptop

state: ARMED   cadence: 30m   cron: 9d30d669   ticks covered: 109
arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261011_032xZ_CTO_LEADS_CLUSTER_OPEN_CALLS_LOOP_60M.md`

## Measurements

- Cluster list read at ~13:33Z: 4 boxes read. 12 open (0 fork, 12 act), 284 closed.
  By box: laptop 2, sitez 7, dell1 0, dell2 3.
- Open cross-adjudications: 0. Inbox: 0 unread. Msgs 109683, 109684, 109688 and 109689 were acked.

## Changes since tick 108

- **TCKT_MTADTA:** Andrew registered the collector app and granted consent at the laptop, at 13:16Z.
  - The app has one `ActivityFeed.Read` app role assignment and one client secret. The credential secret holds 1 version (only
    metadata was read).
  - Details went to dell1 by Taildrop (rc=0) and the relay went through `0.0.0_AB_MSTR`. dell1 closed `d9cb` and `6601` and lists 0
    open.
  - The unified audit-log check is still unrun: Andrew holds Cloud Application Administrator and AI Administrator only. The Global
    Administrators are `breakglass@` and `LDTAdmin@`. Exchange Administrator is held by apps only (Huntress, Avanan).
  - Path given to Andrew: the `LDTAdmin@` holder runs `Get-AdminAuditLogConfig`, and the collector's first content proves it organically.
- **Andrew-direct @e0ddd27261 and addendum @8388e43656:** "synthetic files that we need cleared out are always deletable, they can
  delete those". So `dell2 dc59` becomes a seat delete, then close. `dell2 e260` is superseded: he deleted the `Opal_Terminal` IAM
  user (`NoSuchEntity`, with a positive control). Relayed to `1.0.0_SA_CTO~DELL2` through `0.0.0_AB_MSTR`; dell2 closes both.
- `dell2 80ad` was closed on dell2 after `XA-7f7d`.

## Calls this tick

No open calls in scope (tick 109). The cluster holds 0 forks and 0 open cross-adjudications.

## Acts only Andrew can do (each with its citation)

- `sitez 21d9` (+ `21c5`, `8ed7`, `f0d2`): his sitting and his Opal Bloomberg sign-in.
- `sitez bd68`: his 10-08 word against a live grant. REC: narrow it.
- `sitez 5b35`: a named person's call.
- `laptop b87f`, `laptop 44eb`: person acts. On 44eb, Alyssa Keith is to send the mention (`2.0.0_SA_COO~CA` msg 109684).
- Postponed: `sitez def4`, `dell2 c02c`.
- The secret `fideles/imap-app-password` is still in AWS. Deleting it is his word (`2.0.0_SA_COO~CA` msg 109688).

## Completion test

NOT DONE. The scope ends only on his stand-down.

## Compiler Tools

- `open-calls.py list --all --cloud`: OK, 4 of 4 boxes.
- `xadj.py list --state OPEN`: 0.
- `az rest` Graph reads (directory roles, app, service principal): OK.
- `.tools/aws iam` reads: OK.

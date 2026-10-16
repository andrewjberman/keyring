# self-drive cluster open calls -- tick 91 (2026-10-16 ~04:0xZ), 1.0.0_SA_CTO laptop

state: ARMED   cadence: 30m   cron: 9d30d669   ticks covered: 91
arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261011_032xZ_CTO_LEADS_CLUSTER_OPEN_CALLS_LOOP_60M.md`
(cadence: PACING in `org/ref/LIVE_ARMS.md` @9cb8890499)

## Measurements

- Cluster list read at ~04:02Z: 4 boxes read, none absent. 15 open (2 fork, 13 act), 254 closed.
  By box: laptop 4, sitez 9, dell1 0, dell2 2.
- Open cross-adjudications: 0. Inbox: 0 unread.

## Changes since tick 90

- **Andrew-direct ~03:4xZ: "all recs approved"** (record @83ac18c5de), then "thats good, i approve of this" (addendum
  @ba2e7f6545).
  - Closed here: laptop `bea4` and `318f`.
  - Closed on dell2: `40fa` and `dbfb` (approved for PROD) and `2d0b`.
  - `c02c` stays open, postponed; his condition (the list and draft on the dell2 Desktop) is met per msg 109555.
- Cross-adjudication `XA-20261016T034740Z-28da` ruled @6096a066af. Site Z fixes `naming-gate.py` to read
  `name_rulings.json`: measured 0 references there against 7 in `naming-apply-gate.py`. The merge is announced to all boxes.
  - The muse-reader folder for dell1 was routed to `2.0.0_SA_COO~CA`.

## Calls this tick

No call is unruled. Site Z still shows three rows this seat ruled or Andrew answered, waiting for site Z's CTO to close them:
- `3b41` (into `def4`, his word);
- `f643` (`XA-7afb`);
- `115c` (`XA-28da`).

Their records reach site Z at the next integrate.

## Acts only Andrew can do (each with its citation)

- His sittings, sign-ins and sends:
  - MC Portal: `21d9`, `21c5`, `8ed7`, `f0d2`;
  - Alyssa: `def4`;
  - Teams: `a519`, `44eb`;
  - muse: `8f2b`;
  - remote desktop: `c9a4`, `b87f`;
  - Opal_Terminal: `e260`.
- `dell2 c02c`: postponed on his word.

## Completion test

NOT DONE. The scope ends only on his stand-down.

## Compiler Tools

- `open-calls.py list --all --cloud`: OK, 4 of 4 boxes.
- `open-calls.py close --ruled-by andrew`: accepts a CROSS-BOX row on his ruling.
- `xadj.py list`: 0 OPEN.

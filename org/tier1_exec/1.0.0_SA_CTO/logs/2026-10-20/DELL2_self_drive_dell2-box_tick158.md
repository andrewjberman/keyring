# /self-drive dell2-box -- ticks 157-158 (2026-10-20 ~05:56Z-06:56Z), 1.0.0_SA_CTO~DELL2, cadence 30m (hourly floor)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** ticks 157 and 158, since the tick 156 log (@5a7ca73ab2). state: ARMED.

## Quiet window

- **The 05:45Z-07:00Z IB2 freeze for the opal-gateway resize.** MSTR msg 11236 (a relay of NFRA1; MSTR measured none of it):
  - the resize is done;
  - `/health` has read 200 since 06:24:29Z;
  - public downtime was 44 s.
- **No calls to rule.** No IB2 act in the window, as ordered.
- **The IB2 queue from 07:00Z:**
  1. r37 v2 (CTO half @d9d913c5cf);
  2. r34m v2 (@ee2a5c1645);
  3. run 6 (ADDENDUM 8, @95404e7e5a and @bb3d307f29).

  The v0.24 portal set reaches PROD only after both V2s read green.

## Acts only Andrew can do

- **Row a331** (an entitlement): the outside-domain users row in TCKT_VNEXT-D2-S53, which carries the internal firm id.
- **Recursive deletions and discards of uncommitted files** (CLAUDE.md, Agent Autonomy: "Human confirmation ONLY for:
  recursive deletion, destructive git, ... S3 deletes"):
  - `C:\dev\wk-irpt-dashbd-503`;
  - row 544d;
  - row 65a1;
  - row a392.
- **S3 deletes:**
  - row 6e7c;
  - row 128f;
  - the synthetic leftovers of runs 5 to 5D.

## Completion test

NOT DONE. The dell2-box scope is a keep-driving scope; it ends on Andrew's stand-down word.

state: ARMED

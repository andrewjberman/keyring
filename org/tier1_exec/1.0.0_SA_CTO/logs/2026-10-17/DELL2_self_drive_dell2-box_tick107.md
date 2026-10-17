# /self-drive dell2-box -- tick 107 (2026-10-17 ~16:27Z-16:57Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** the time since the tick 106 log (@6acb57c1a0). There is a substantive delta. state: ARMED. Inbox: 0 unread.

## Acts taken

| act | carrier |
|---|---|
| Portal drift: dell2's reconcile is closed, because 16534996bd is in DEV cab233bfdf. The 2 PROD-only commits (99d2b2a7, 40845c7e) are dell1's amgt-sa release merges. dell1 places the fold on `~H2` and makes it standing (dell1 CTO msg 7662). | msg to MSTR |
| **Standing rule for dell2:** every PROD promote order ends with a tree-equal fold of PROD into DEV, approved by this seat on the check that the diff lists 0 files. | msgs 10615-10617 |
| **The Cottonwood transaction wiring REVISION 2 CTO half is SIGNED** (sha256 5d7350ea). It is the one code release (36da4e101f): the late-posting reader, the settle step of at most five days per fire, and the transaction window. Settle-day prints are required. REVISION 1's "returns unchanged" condition is superseded by the intended fix. | @827bc0c17e, @7eed1f2073 |

## Acts only Andrew can do

- **449e: the Retry on TCK-20261017-5af976ff in PROD Ticket Center.** Citation: ticket_center lambda_function.py:1750-1753.
- 3c22: lift or keep C-V1. Citation: IRPT_YCDGEN PRD :312, "on Andrew's word only".
- c02c is POSTPONED.

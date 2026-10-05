# /canonical-drive -- 2.0.0_SA_COO~X -- 2026-10-04 23:4xZ-2026-10-05 01:1xZ (site Z, opal_bloomberg)

| time (Z) | project | limb | round | act |
|---|---|---|---|---|
| 23:4x | AMGT_CORPUS | L8 | 36 | CTO DECISION msg 29322: round 36 closed tonight, al-4 CARRIED. Packet @3d5f1e2b7e to CVO~Z |
| 23:48 | AMGT_CORPUS | L8 | 36 | NO-OP: packet 2 min old |
| 23:5x-00:1x | AMGT_CORPUS | L10 -> L6 | 36 -> 37 | CVO v42 @1acdc5c60b and CTO analysis @4c3e3755a7, then round 37 ISSUED @ece32e98a6 in the same tick. Three workers spawned |
| 00:18 | AMGT_CORPUS | L7 | 37 | NO-OP |
| 00:2x-00:4x | AMGT_CORPUS | L7 | 37 | am-4 drained @78e4bb3f11, after the issuer's test repair 0eb01d2a0b. am-3 drained @ff24d30809; portal 2e7c5cdb = am-3 + DEV. am-1's AC1 failed on the issuer's own check, which was amended @5a02ae8e98 (row Z-W1-S33); slot ~1 re-seated, then drained @3ffe37a57a (channel union) |
| 00:4x-00:5x | AMGT_CORPUS | L7 | 37 | CTO APPROVED 2e7c5cdb; Andrew "approved"; DEV pushed, CI green. am-2 dry run 96/96, unlabelled 23,365 -> 0; COO half @7c72c86057, CTO half @a8ccfc4f88 |
| 00:5x | AMGT_CORPUS | L7 | 37 | real run on DEV: 1299 HK gap reasons met; money marks wait for am-2 (@05ec570957) |
| 00:5x-01:0x | -- | -- | -- | MSTR~Z asked who armed the walker: I answered, it was mine (00:51Z), plus three earlier unannounced walks. ARM/DISARMED notices go to MSTR~Z from now on. The laptop holds the walker from 01:05Z |

**Decisions closed:**
- **The issuer's own check was the defect.** The money rule counted "(share count)" units, against am-1's item 3. It was amended
  inside the decomposition, and the base and branch re-runs are recorded in the amendment commit.
- **A union for the append-only channel.** A CLOUD-into-branch merge conflicted on INVESTIGATION_v1.md, so it was aborted and only
  the check file was carried to the branch. The drain's conflict was resolved as a union of both appends (164 rows, ids unique).
- **am-2 waits for am-5.** The re-derive and re-pin run after the 10-05 13:00Z fire is read on the old pin. That is the round-35
  ak-4 timing rule.

**Open:** at 13:22Z (one-shot c4b64c3f), am-5's read of the fire, then am-2's legs under the signed pair, then the round-37
packet.

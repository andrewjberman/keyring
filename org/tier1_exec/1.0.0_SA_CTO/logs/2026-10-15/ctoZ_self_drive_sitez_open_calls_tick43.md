# /self-drive sitez open calls -- ticks 42-43 (15:51Z, 17:01Z 2026-10-15), `1.0.0_SA_CTO~Z`

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md`
@ce0ba39d90. Covers the span since tick 41 (@a70a4fd71e). Tick 42 was quiet (drive-ticks line). **state: ARMED.**

## Measured

- `open-calls.py list`: rows 46, open 7, all person acts. Inbox: 0 unread.
- **New check from this tick (ruling @4356f15f16, item 5): planned cells vs cut orders, NFRA_OPLGTW.** One gap: G2 `OG-cl-1..n`
  (the opal-data-assets client adapters). Their gates `OG-gt-6` and `OG-cl-0` are both complete, and no order exists. Already
  routed to `2.0.0_SA_COO~O` at 17:00Z. No other planned cell with met gates lacks an order.

## Rulings and acts since tick 41

1. **Python task re-point to 3.11 @c95f54ea33: SUPERSEDED before any act @84fbbd76b1.** Andrew reinstalled 3.14.8 at about
   15:03Z (MSTR~Z msg 34476; COO~O msg 34483; MSTR~Z msg 34485).
2. **WSJ and Barron's leave the site Z runner (@86581c31be), then SUPERSEDED by PRD v3.11 @32b70d1b86.** Andrew, relayed by
   COO~O (msg 34493): "Yeah we can move all HARVST operations to Dell1, including Seeking Alpha + Bloomberg as well."
   - The site Z runner retires: STOP, then Disable, unregistering nothing.
   - OG-eg-2 and OG-sa-1 close SUPERSEDED.
   - Dell1's CTO accepted, replacing their per-publisher plan (MSTR~Z msg 34507; dell1 addendum 4 @e6eb813524).
   - COO~O cut the retirement order, OG-eg-3, @506f64e1cb.
3. **G2 opal-data-assets cells never cut: RULED @4356f15f16, on Andrew's question at this terminal.**
   - Catalog coverage: assets 0 of 111 rows, portal-v2 16 of 41, etfs 7 of 36, mdpf 0 of 7, bd 0 of 8, harvest 78 of 78.
   - COO~O cuts OG-cl-1 (Schwab) and OG-cl-2 (49F BD) now as build cells, plus the G3 and G5 wave B remainders.
   - G2 rejoins the release queue after ap-22.
   - The reply owed is the issuance commit.
4. **COO~MP, on the /gateway view (msg 34511):** Andrew's word gives the human view to MCPORTAL, which lifts the hold for the
   one mis-filing fix (MP-pe-1, MP-pe-2). That reading is accepted.

## Acts only Andrew can do (each with its citation)

1. One MC Portal sitting, including one sign-in as Opal Bloomberg (21d9; covers 21c5, 8ed7, f0d2). Citation: his login and a
   human read.
2. One sitting with Alyssa (def4; 3b41 is a duplicate). Citation: his person act.
3. One Teams message from his account to Opal Bloomberg (a519). Citation: his own account.

## Completion test

NOT DONE: 7 open calls, every one a person act. Next tick: read COO~O's G2 issuance commit.

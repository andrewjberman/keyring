# /self-drive ~O fabric -- ticks 79-80 (1.0.0_SA_CTO~O, 2026-09-27 18:46Z-19:16Z)

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d.

- **tick 79 (18:46Z):** CVO~O read the OG-e-2 test-condition amendment as NOT a widening (@87f9d15f58).
- **Andrew's question (18:3xZ)** on the Alyssa card: "nobody has sprint tools ... /login i dont understand".
  - Answered: `/sprint` and `/login` are gateway WEB routes, not tools.
  - Measured by a read-only SSM read of `/opt/opal-gateway/.env`: `SPRINT_VIEW_ALLOWED_EMAILS` is set on 0 lines, so
    `/sprint` is open to the whole tenant (`sprint_view.py:173-175`).
  - The card is re-framed: `/sprint` for Andrew only, REC (a). Set it in the `deploy-to-ec2.sh` `.env` template,
    because every deploy rewrites `.env`. That makes the Alyssa deny backfill moot.
  - `/login` retirement is proposed for round 2.
- **Goal check (18:5xZ):** MX-s-4 (AE~I) is HELD on the Black Diamond portal login.
  - 69 of 119 runs have failed since 2026-06-23, and all 3 BD downloaders share it (row NFRA_MCPINDEX-Z-S8).
  - MX-s-6 (DS~D) waits on it.
  - The blocker had never been carded to Andrew. It is carded now.
  - COO~O was asked for a stall-point capture. It amended MX-s-4 A2 @641af19068: a screenshot plus the URL, classed as
    password, MFA/consent or page change. The first two go to Andrew; a page change is fixed in the lane.
- **tick 80 (19:16Z), QUIET:** 0 unread.

**Cards at Andrew:**
- (1) `/sprint` for Andrew only. REC (a).
- (2) Did the Black Diamond login change around 06-23? REC: say if known, or try one manual login.
- (3) The switchover sitting. This is an act, not a call.

**Completion test:** NOT DONE. 0 of 4 projects are complete.

state: ARMED

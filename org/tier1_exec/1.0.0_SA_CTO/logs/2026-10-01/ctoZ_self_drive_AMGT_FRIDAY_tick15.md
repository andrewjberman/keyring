# /self-drive AMGT_FRIDAY -- tick 15, `1.0.0_SA_CTO~Z`, 2026-10-01 16:46Z-17:47Z

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_040xZ_SELF_DRIVE_60M_AMGT_FOUR_PLUS_ETFS_RIVALS_ARM_ON_CRO_BRIEF.md`. **state: ARMED.**

## Scope state (measured at 17:46Z)

- **Projects:** 5 of 5 `active`, 0 `complete`.
- **DSGN_AMGTV1:** round 21 is CLOSED (COO~D 27971; log 15143754e0). **The freeze candidate is portal DEV `3c37a01c`, replacing
  `da0b3bd7`.** The hover probe read BA 13 of 13 and AMD 10 of 10 tooltips clean across all four surfaces, and the walk.mjs raw-code
  count went from 4 to 0.
- **ETFS_RIVALS:** the RIV-d-5 never-widen pair is signed (COO @a10ebe8d92, CTO @a8913dccef), and d-5 has spawned (log 74f12b3092).
  - Andrew-direct ~17:24Z at `4.0.0_SA_CRO~RV` (record b7622c0b5a): a read-only `/closer trace ETFS_RIVALS` from ingestion to the MCP
    page.
  - His order of goals: the methodology is sound, the Opal and non-Opal comparison base is adequate, and all pipelines and schedules
    are set up.
  - The trace feeds the round-4 analysis. It holds nothing now, and its BUILD phase needs his word.
- **AMGT_HARVST:** round 35 is in flight. Gold rebuild #3 starts at 20:00Z (COO~H 27942).
- **CORPUS and RESAPP:** idle; the Friday face and feed are complete.
- **Inbox:** 0 unread. Acked: 27969, 27971, 27972.
- **Push state (ls-remote):** origin CLOUD `0abf99fcd4`; origin portal DEV `2bb367ef10`; local DEV `3c37a01c`. Nothing has been
  pushed from site Z.
- **Completion test:** NOT DONE. 0 of 5 are complete, and all 5 are REACHABLE.

## Calls closed and acts taken

| item | ruling or act | why |
|---|---|---|
| COO~RV 27969 / 27972: the RIV-d-5 CTO half | **SIGNED, all 6 keys** (@a8913dccef). Key 3's issuer floor of 0.23 is signed as written, because every floor rises from 0.0 and none loosens. The per-fund issuer floor is carried to the round-4 analysis. | Measured independently: the pin ancestry, the field-by-field served-delta diff (13 of 13), the live base (the round-3 apply at 10:53Z), and 0 GQGU objects before. |
| COO~D 27971: round 21 walked clean | **3c37a01c is the freeze candidate.** | The walk covered all four surfaces within the cap of three repairs. |

**Carried to the round-4 analysis:** the per-fund issuer floor, and the CRO~RV closer trace once it lands.

## Acts only Andrew can do

1. **Push portal DEV and CLOUD, then promote to PROD** (CLAUDE.md Git: `0.0.0_AB_MSTR` pushes trunks on Andrew's word).
   - The freeze candidate is `3c37a01c`.
   - The leg is a pull-merge of origin DEV `2bb367ef`, which carries 13 laptop DSGN_IRPTV1 FAST commits; it is never a rebase.
2. All other items are unchanged from tick 10.

## Compiler Tools

`git ls-remote`, `git log`, `lambda list-functions`, `s3api list-objects-v2`, broker `send_message`/`ack_messages`.

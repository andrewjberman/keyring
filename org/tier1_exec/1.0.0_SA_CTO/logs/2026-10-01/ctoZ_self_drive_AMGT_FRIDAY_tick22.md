# /self-drive AMGT_FRIDAY -- tick 22, `1.0.0_SA_CTO~Z`, 2026-10-01 23:46Z - 2026-10-02 00:47Z

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_040xZ_SELF_DRIVE_60M_AMGT_FOUR_PLUS_ETFS_RIVALS_ARM_ON_CRO_BRIEF.md`. **state: ARMED.**

## Scope state (measured at 00:46Z)

- **Projects:** 5 of 5 `active`, 0 `complete`.
- **The demo freeze holds** at portal DEV `3c37a01c`.
- **AMGT_HARVST:** the HVST-ai-4 code (the bbg HTML branch) is drained (3319bb1c60). The outbox drain and gold #4 are next,
  under ruling 28084.
- **ETFS_RIVALS:** round 5, 8 orders, is in flight.
- **Inbox:** 0 unread. Acked: 28093.
- **CLOUD /integrate parity (Andrew-direct at the laptop):**
  - I held the quiet window from 00:33Z to 00:43Z.
  - PARITY was read at 00:43Z: origin = site Z = laptop = `0257976705`. I confirmed it here, with HEAD and ls-remote both
    reading `0257976705`.
  - Every record and the hook fix (`be815d264f`) from this seat are on origin.
- **Push state (ls-remote):**
  - origin CLOUD `0257976705`;
  - origin portal DEV `d79b9934`, PROD `f2731ad3`;
  - local DEV `3c37a01c`, not on origin.
- **Completion test:** NOT DONE. 0 of 5 are complete, and all 5 are REACHABLE.

No open calls in scope (tick 22).

## Acts only Andrew can do

1. **PROD for the demo** (CLAUDE.md Git: `0.0.0_AB_MSTR` pushes trunks on Andrew's word). The act: pull-merge origin portal DEV
   `d79b9934` into `3c37a01c` (merge-tree clean), push DEV, then promote DEV to PROD. The CLOUD side is at parity.
2. **The ETFS_RIVALS FWD-1 signed-in read, and confirmation of Addendum B** (two answers owed).
3. **Vendor per-use words, if wanted:** the HARVST residential arm, and web search for the rivalfunds AI.

## Compiler Tools

`git ls-remote`, `git rev-parse`, `git log`, broker `ack_messages`.

# /self-drive AMGT_FRIDAY -- ticks 38-39 (1.0.0_SA_CTO~Z, 2026-10-06 ~12:2xZ -> 14:18Z)

**archetype:** COORDINATE

state: ARMED, HELD under Andrew-direct. Cadence 60m, cron `29c8b141`. Arming record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_194xZ_SELF_DRIVE_60M_AMGT_FRIDAY_RESTART_AFTER_SENTINELONE_CRASH.md`
@2b18064b99. Previous log: tick 37 @1447e05277. Tick 38's log was not written when the tick ran, because Andrew interrupted at ~13:2xZ;
this log covers both ticks.

## Andrew-direct this window

1. **msg 30058** (via MSTR~Z, record @f42219ebfe): *"Bloomberg issue is singular priority for the box. until that is fixed no other
   projects matter."* Every AMGT_FRIDAY project is HELD.
2. **msg 30098** (via MSTR~Z, record @74897ebc2c): *"yang will handle it, hes responsible and will repull. this device however is having
   an issue and we need to reboot."* The pre-reboot handoff is saved @e801d1e411. At 14:18Z the box has not rebooted (last boot
   2026-10-04T18:59Z).

## Inbox measurement

13:3xZ to 14:18Z: 30067, 30074, 30083, 30085, 30089, 30098 and 30114 are all READ and acked. 0 unread.

## The Bloomberg issue (the singular priority)

| item | state | commit |
|---|---|---|
| Trace (CRO~Z msg 30067) | 7 CIX definitions stopped calculating on Bloomberg after 2026-09-29. Not our pull. The populated benchmark cells are wrong, and the ETF benchmark is also N/A for 4 of 5 models | @bfe10cb2a4 |
| BG msg 30074 | By family: 4 of 4 BMK frozen, 3 of 4 ETF frozen (`.INT_ETF` current), 0 of 5 primary frozen | -- |
| **Fix route RULED** | (1) a producer guard in `yang-model-portfolio-benchmarks`, under a pair; (2) the CIX re-save; (3) the re-pull and /data-refresh | 5e0c045e8d |
| BG msg 30089 | Asked to spend a Terminal sign-in to raise the UI. **Ruled NO:** the lockout budget is Andrew's, and the re-save is a human act. Z-S2 does not gate it | 8390be9f89 |
| Owners | (1) COO~Z, after the reboot (msg 30085); (2) and (3) Yang Liu (msg 30098) | ADDENDUM 2 |
| Measured 14:18Z | The served benchmark JSON was last modified 12:31:21Z (no re-pull yet). No benchmark entry in `.open_deploys` (shared tree) | -- |

Verdict ledger: 2 rows (the hold; the route).

## Scope state (register read 14:18Z)

| | |
|---|---|
| projects in scope | 5 of 5 `active`. D5 (SITEZ) has 193 open TOs: CORPUS, HARVST, RESAPP, RIVALS. D13 (LAPTOP register row) has 2: DSGN |
| sequence | file @2bed2ad08b, enforcement TRACK. All 5 are UNPLACED, 0 flags |
| open deploys in scope | 0 (shared tree) |
| RESAPP | round 76 HELD by COO~Z (msg 30083) |

**No open calls in scope (ticks 38-39).** Andrew's hold leaves nothing to rule on the five projects.

**Completion test: NOT DONE.** 0 of 5 complete.
- **HELD by Andrew's word 4:** CORPUS, RESAPP, DSGN, RIVALS.
- **UNREACHABLE 1:** HARVST, pending Andrew's hand-solve and the SA account.

## Acts only Andrew can do (each cited)

1. **Lift the `integrations/bloomberg/` no-modify order** (his order, by name): for the per-series recency tripwire (Z-S5) and the
   sign-in defects Z-S1..S4.
2. **The portal DEV push** (product files): DSGN rounds 43+44 (`1d6d2573`), and the RESAPP `/freshness` page once its render review passes.
3. **HARVST:** hand-solve the challenges; the SA account (HTTP 402).
4. **Vendor uses:** Z-W240-S1, Z-W227-S1, RESAPP FWD-2, SEC egress.
5. **Spend:** provisioned concurrency.
6. **Others:**
   - FWD-14's list owners;
   - the walker accounts;
   - Z-S230;
   - FT;
   - the recursive deletion of `C:/tmp/ctoz-lint-warn`.

## Compiler Tools

`get_delivery_state`, `directives-check.py --json`, `sequence-check.py`, `s3api head-object`, `Win32_OperatingSystem.LastBootUpTime`,
`git log`.

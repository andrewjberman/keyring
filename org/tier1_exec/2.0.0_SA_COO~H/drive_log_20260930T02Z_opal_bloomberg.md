# 2.0.0_SA_COO~H drive log -- 2026-09-30 02Z (host opal_bloomberg)

Arm: `/canonical-drive AMGT_HARVST 30m` (cron bf9d159b), per
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_183xZ_SELF_DRIVE_AMGT_FABRIC_OPS.md`.

| time | project | limb | round | TOs t/T | outcome |
|---|---|---|---|---|---|
| ~02:5xZ | AMGT_HARVST | L7 | 24 | 4/6 | DRIVE FORWARD + RULE-ESCALATE |

## Acts

- **Drained:**
  - `n-2` @`c258c87826`.
  - `n-1` @`729ef39440`. Row `Z-W56-S2` is ARMED: the new capture runs only on the `--harvest-grammar` path, and `run-local.ps1` does not pass that flag.
  - `n-3` @`49bafe8df9`. Row `Z-W58-S1` is ARMED: the gold branch fails with `INCOMPLETE_GOLD_INPUT`, 0 of 191 resolved.
- **Held:** `n-4` (WORLD gold flip) by AMENDMENT 1 @`89480001b4`, not dispatched. The hold disarms `Z-W58-S1`.
- **Carded to `1.0.0_SA_CTO~Z`, two decisions:**
  1. The gold coverage vs. the guard, and the scheduler flag.
  2. The `n-2` served sa silver rebuild cannot supersede. `store.silver_latest` keeps only a strictly newer `fetched_at`, and the rebuilt rows share it. The rebuild follow-on is held pending the tie-break ruling.
- **Running:** `n-6` (`/timeline/day` speed, worker `~60`).
- **Tally:** FWD 2 of 9 REALIZED, per the round-23 analysis @`d1ec6f4118`.

# Drive log -- 2.0.0_SA_COO~RV -- 2026-10-01 07Z-08Z (opal_bloomberg)

**archetype:** COORDINATE

Scope: ETFS_RIVALS, round 3. The lease read FULL on every tick.

| tick | time | TOs t/T | outcome |
|---|---|---|---|
| 17 | 07:3x-07:5xZ | 2/6 | DRIVE FORWARD. hp-1 drained (CLOUD 51c142847f). Issuer amendment 1 to r-3 and to i-1 @360a2c062f |
| 18-19 | 07:48-07:55Z | 2/6 | NO-OP. Both workers moving |
| 20 | 08:0x-08:2xZ | 4/6 | DRIVE FORWARD. r-3 drained (5429f9284b) and i-1 drained (c9d7018e3d). g-6 amendment 1; slot ~1 handed g-6 |
| 21 | 08:12Z | 4/6 | NO-OP. g-6 editing |

## Closed decisions

- **RIV-hp-1 complete.** IDVZ 41 of 41 and PFOE 25 of 25 home rows are in G1 with source `home_producer`; the page shows both with
  a `home_producer` badge.
  - Row W1-S17 (ARMED) was ruled in i-1's amendment 1: the reader takes module constants and gets a repo-side drift test, with
    no runtime read outside the package. It is now disarmed (row S21).
- **RIV-r-3: the AC2 failure was the issuer's check (row W2-S6).**
  - The plant sat on `TTE FP Equity`, held by 4 funds, so every fund was held.
  - The fixed check plants on a TXUE-only security: CGIC, INEQ and TXUE are held, and SCHY and BIDD build.
  - Amendment 1 also ruled:
    - W2-S7: `guardrails.py` granted, so freshness has one home;
    - W2-S8 (ARMED, now disarmed): a held fund reads "Trades held: <reason>";
    - W2-S9: only share-changing actions hold a fund.
  - The order is complete, with 224 passed.
- **RIV-i-1 complete.**
  - BASG resolves 33 of 33 by the measured join; the ABNB ambiguity is refused; the PFOE rivals resolve 100%.
  - `i1_identity.json` records fraction 1.0 per fund over 2026-09-25..28.
  - The drain suite read 225 passed and 2 FAILED: two hp-1 tests asserted the removed runtime read (W1-S22). The repair is folded
    into RIV-g-6's amendment 1.
- **CTO msg 27649, acked:** a ui-walk arm posts ARM and then DISARMED to `0.0.0_AB_MSTR~Z`. No round-3 cell uses the walker.

## Self-disclosure

- I authored the r-3.AC2 fixture defect myself. The dry-run at base FAILed for the right reason (the whole batch was held), but
  that failure could not tell a correct build from a broken one: I never checked that the plant left an un-held fund. A
  build check needs the dry-run to show it CAN pass, not only that it fails.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `.tools/safe-merge.sh` + `C:\tmp\rv_union.py` | drains of hp-1, r-3 and i-1, plus the ~2 sync | Every append-only channel conflict resolved as CLOUD plus the branch-only rows (+4, +4, +3); the row gate is clean each time |
| pytest (drain hygiene) | per merge | 215, 224 and 225 passed; the last run had 2 failed, routed to g-6 |

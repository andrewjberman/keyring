# Drive log -- 2.0.0_SA_COO~RV -- 2026-10-01 08Z-09Z (opal_bloomberg)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE

Scope: ETFS_RIVALS, round 3. The lease read FULL on every tick.

| tick | time | TOs t/T | outcome |
|---|---|---|---|
| 22 | 08:16Z | 4/6 | NO-OP. g-6 editing |
| 23 | 08:3x-08:5xZ | 5/6 | DRIVE FORWARD. g-6 drained (CLOUD b780b4b8cb; suite 241 passed, 0 failed); d-4 cut begun |
| 24-26 | 08:40-08:56Z | 5/6 | NO-OP. Served-delta dry run running (read-only) |
| 27 | 09:0x-09:2xZ | 4/6 | DRIVE FORWARD + RULE. Row Z-S8 BLOCKING; d-4 STOPPED; RIV-i-1 REOPENED (amendment 2 @295207568b) |
| 28-31 | 09:08-09:35Z | 4/6 | NO-OP. Slot ~1 committed the G5 key fix (85f442ffe1); its served-delta report is running |

## Closed decisions

- **RIV-g-6 complete.**
  - 66 G1 rows carry G4's GICS, RESOLVED and sourced; `sub_asset_class` equals the sector on 66 of 66.
  - Row W1-S22 is repaired, and the suite reads 0 failed.
  - Row W1-S25 (revision letter-suffix ordering) is carried to round 4's revision contract, W1-S11.
- **The round-2 served-delta instrument does not measure round 3.**
  - `key4_served_delta.py` mirrors issuer inputs only.
  - So BASG's identity join never runs, and the non-BASG funds read as 18189 "removed".
  - `round3/served_delta_r3.py` mirrors every input (issuer silver 325, sidecars 325, Bloomberg silver 3610, G3 1, home landings 27, G4 from characteristics) and compares trades on an identity-independent key.
- **Row Z-S8 BLOCKING: the round-3 identity moves BASG's trades.**
  - BASG has 527 served trade keys against 1694 new: 322 removed, 1489 added.
  - In the new set: 922 exits and 638 entries against 224 adds and 261 trims.
  - Of 325 BASG report dates, 184 are partially resolved.
  - A security whose key flips across a window reads as an exit plus an entry.
  - CGIC, ETFT, INEQ, PCLG, SCHY and TXUE read 0/0. TSEL +6, WCMG +1 and BIDD -2/+1 are the same class.
- **RIV-d-4 STOPPED before its pair.** The served BASG trade schedule would have moved by about 1800 trades.
- **RIV-i-1 REOPENED: the issuer reopens, it never re-cuts.**
  - The fix: G5 matches on a window-stable raw identifier key, with `security_id` as a label.
  - New criterion i-1.AC2, bounded at about 27 s. It FAILs at CLOUD as expected: served 47 BASG trades in the window against 287 on the branch.
- **The CTO has the decision record.** Its d-4 half is asked only after a clean re-run of the full dry run.

## Self-disclosure

- I nearly cut the d-4 pair on the round-2 instrument. Its BASG "G5 values: only revision columns differ" looked clean, but it read 837 rows on the round-2 key and saw no join, because it never mirrored Bloomberg silver. A clean result from an instrument that cannot see the change measured nothing; widening the mirror is what found Z-S8.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `round2/key4_served_delta.py --with-g3` | first served-delta read | under-measures (issuer-only mirror); kept as `round3/key4_served_delta_r3.json` |
| `round3/served_delta_r3.py` (new) | full served-delta dry run | 4286 inputs mirrored read-only; per-fund G1/G5 deltas |
| `round3/checks/i-1.AC2.py` (new) | bounded criterion | FAIL at base as expected, 27 s, 63 objects |

# drive log -- 2.0.0_SA_COO~C2 -- 2026-10-11 22Z-23Z (desktop-n8rjv0a)

Counts, hashes and reason codes only.

- 22:2xZ | round-75 packet @056535ed50 to the CVO.
- 22:4xZ | round-close r75 MAY-CLOSE. CTO ROUND-76 ANALYSIS @8ae9f87cf2: the purchase marking is no longer a lead; the price paid on a trade becomes the instrument. Round 76 issued @ac8000c35b through the gate on the first attempt, 5 cells, 3 at once. Tick 23.
- 22:5xZ | CB-bx-2 drained: 14,250 of 91,040 trade units have a served close; funds left on the store 3,205 of 3,614 over 20 percent off; substituted 10,411 of 10,636 within 1 percent (issuer recount of the per-fund list: equal).
- 23:0xZ | CB-bx-4 drained: 31 of 15,103 trade account-days are measured; 16 change by over 10 bp, all purchases, all too low. CB-bx-1 drained: 246 off rows, 243 of them one fund; 124 none found under a list written first; a flat-dollar reading post hoc.
- 23:1xZ | CB-bx-3 drained: 15 fund series fail by trades, 17 pass, 60 too few, 178 no trade row, 0 conflicts. CTO corrections (msgs 6075, 6095): twelve of its hashes cited today name other seats' commits; one is this project's round-68 analysis; a correction record written beside the round-68 packet @9cb72d5d71, the seven files not edited.
- 23:3xZ | CB-bx-5 drained: the correction list at revision 6. Round-76 packet to the CVO (four judgment criteria).

Open at this seat: round 76's four judgment criteria at the CVO; the CTO's two addenda (the fund-basis rule; the 2022 factor). No re-mint order is cut and nothing was applied or served. `dep_stage` not moved. No FWD is claimed REALIZED by this seat.

## Compiler Tools

- `safe-merge.sh`: five drains (r76), all rc=0.
- `to-pipeline-gate.py` (through safe-commit): one issuance (r76: 5 orders).
- `round-close-check.py`: r75 MAY-CLOSE, r76 REFUSED (4 ungraded).
- The silver suite: not re-run (no code drained this round).

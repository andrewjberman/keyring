# L8 drain-end packet -- MDPF_SECCLASS round 20 (2.0.0_SA_COO~M1, dell1, 2026-10-11 ~04:1xZ)

**For:** 3.0.0_SA_CVO. **Decomposition:** `org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R20.md`.
**Issuance:** @d29944d19a (`fanout: 3 of 3 chains, cap 8`). **Round-close check:** `round-close-check.py --project MDPF_SECCLASS --round 20`:
`orders=3 judgment=0 verdict=MAY-CLOSE`.

| cell | order | slot | risk | drained | criteria (issuer re-run on the worker's tree) | rows |
|---|---|---|---|---|---|---|
| SC-e-87 | TO-SC-e87 | ~77 | SERVED | f4f01cfb27 | AC1-3 `SERVED-REACH site=D_04/C_06/D_03 ok=True target=(equity, equity, Name Row, etf-classifications) controls=3/3`; AC4 `HALF-READY`; BD gold 120/120, COT gold 50/50 | D1-W77-S1 |
| SC-e-88 | TO-SC-e88 | ~78 | LOCAL | 294fa96bec | AC1 `C06-GAP ok=True dates=1 drift=2 basis=rounding` (AC1 amended by the issuer, below); AC2 `C06-SCOPE ok=True bad=0` | D1-W78-S1, D1-W78-S2 |
| SC-e-89 | TO-SC-e89 | ~79 | LOCAL | cc3c69590e | AC1 `LIMB-CALL ok=True`, AC2 `LIMB-OWN ok=True`, AC3 `LIMB-SLUG ok=True`; the tool's own suite `APPLY-GATES-TEST cases=96/96` | none |

## What the cells established

- **SC-e-87 (D1-S26):** BD's three served classify sites now call `classify_with_identity` for a non-blank ticker the table misses. Run
  against the LIVE table by the worker and again by the issuer: the 23 securities move 23 of 23, $966,285.46 (equity 20, fixed_income
  3), none stay. The ship is NOT done: both halves are SIGNED (COO @c6202193c5, CTO @20526c6cc7) and `TO-SC-e87b` is at
  `0.7.0_AE_CloudOps~SC1` (window after the 04:00Z BD chain). Leg G, the served read, is the issuer's after the next scheduled BD fire.
- **SC-e-88 (D1-S27): the cause is share rounding.** C_06 rounds each relationship's class shares to 6 decimals (`:595`) and accumulates
  rounded share times dollars (`:737-743`); the firm class sum therefore differs from the exact `total` by the sum of
  `total_mv * (1 - sum of shares)`. On 2026-10-08, which reproduces to the cent from today's partitions, the gap is -128.57 and its
  largest terms sit at about 1e-6 of a $98M relationship's value. Class mass outside the eight classes: zero. Membership differs: no.
  2026-10-06 and 2026-10-07 do not reproduce (their partitions were rewritten after the snapshot; row D1-W78-S1).
- **SC-e-89 (D1-S23, D1-S25):** `crossbox-deploy-check.py` resolves the acting serial without `--serial` and counts one slug once.

## Issuer rulings this round (for the CVO to see)

- **AC1 of TO-SC-e88 amended** (@287ef0d2ee): the cut assumed all three served snapshots reproduce; the worker measured that two do not.
  The checker now grades a reproducing date on its gap and on the rounding bound (|residual| at most total_mv * 4.5e-6), counts a
  non-reproducing date as drift, and needs one reproducing date. Negative controls: an out-of-bound residual, no reproducing date and a wrong
  published gap each read ok=False. The worker's record was not changed. Gate limb: none graded it.
- **Worker `~78` could not be resumed** (no transcript); it was re-seated on its own branch with its commits named as inherited state.

## The ONE REAL RUN at close (`LOCAL` cells)

`python .tools/crossbox-deploy-check.py --root data/black_diamond --files <the three BD files>` on `box/dell1` after SC-e-89 drained:
OPEN-CALL clear, OVERLAP clear, UPSET clear, **OPEN-DEPLOY hit (4)**, denominator 38 worktrees / 665 sentinel reads / 53 distinct slugs.
No real contention: three hits are ledger entries CLOSED at trunk but still HELD in lagging worktrees' HEADs, the fourth a prunable
worktree registration. Artifact `R20_CHECKS/E89_REAL_RUN_20261011.txt`; row **D1-S28**. The switch is WARN, so the ship is not blocked.

## Rows at this packet

Open investigation rows: D1-S28 (new, from the real run), D1-W77-S1 (NAN/NONE tickers take the blank-ticker chain), D1-W78-S1, D1-W78-S2
(the checker's rounding basis is an algebraic identity; the amended bound is the discriminating test), D1-S26 and D1-S27 (cause named, to
be dispositioned). No BLOCKING or ARMED row.

## Reads and carries into the next round

- SC-e-87's leg G after the ship and a scheduled BD fire, stated net of the rounding gap.
- A round-21 candidate cell from D1-S28 (trunk-first sentinel status; a registered-but-missing worktree counts as vanished).
- Held, unchanged: e57e61 on its trigger; the p1 residue on its ruling; IB-pr-417's e56 member at dell2 (COO half signed @ced2704270).

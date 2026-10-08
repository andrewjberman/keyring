# ADVI_COTBKF decomposition -- ROUND 22 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-08 ~19:1xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-21 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_21_20261008.md` (msg 1449): the ruling on
D2-S32 (one mechanism for all 147 -- in the after arm a sweep buy debits cash and the non-sweep sale that funded it credits none; ONE
cash-leg repair, its re-grade is the test) and the ENRICHMENT LIST E1 (the repair) and E2 (D2-S31, the mover scripts name their data
folder and refuse a list-version mismatch).

**Rule 24.** Domain: E1, E2. Two cells, two chains: the write surfaces are disjoint (E1 the chain and the re-grade runner; E2 the two
mover scripts), and neither reads the other's output.

## Measured constraints

1. Round 21's real run on the trunk (@0aefdc2e8e, after the arms were rebuilt): `MOVER-CAUSES movers=147 sweep_balance=72 offsetting=0
   other=75 sum_ok=True core_separate=16`; the arms `SWEEP-REGRADE ... months_before=1685/1931/78977 months_after=2057/1522/79014
   control_same=True`.
2. The traces: D49141714 2019-02 (arm difference a constant -4,010.86 = the net sweep buys; value 4,061.90 -> 51.04) and RGY005018
   2024-12 (steps of -199.98 and -188.14 on its two sweep-trade days), both re-derived by the CVO.
3. The mover scripts read day values from the runner's default data folder; on the trunk they read round 20's v1 -> v2 arms and
   classed all 147 `other:unexplained` (D2-S31).

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-v-1` | E1: the cash-leg repair -- a non-sweep sale funding a sweep buy credits cash; unit test; full re-grade with the 163 shown and the 72 / 75 counted back to MATCH, remaining DIFF months named; non-sweep control | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~43` |
| `CB-v-2` | E2: the mover scripts take an explicit data folder and refuse an arms list-version mismatch, with a test | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~44` |

**Fan-out:** `2 of 2 chains, cap 8`.

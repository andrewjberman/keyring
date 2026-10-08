# ADVI_COTBKF decomposition -- ROUND 21 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-08 ~18:4xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-20 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_20_20261008.md` @9129f4e33d (msg 1412):
the 316067107 designation PARKED with the CTO (bound: 16 of 163); E1, name the cause of the 147 "neither" movers.

**Rule 24.** Domain: E1. One cell.

## Measured constraints

1. Round 20's real run on the trunk (@16f0103204): `MOVER-CLASSES movers=163 core=16 other_mmf=0 neither=147 sum_ok=True`;
   sweeps-v2 = v1, so v1 -> v2 is identical (2057/1522/79014).
2. Month grades of round 19's two arms are persisted at `deliverables/0.9.0_WK_ADVI_COTBKF~41/month_grades_{before,after}.parquet`;
   the movers and their class at `.../mover_classes.parquet`. Day values live under the runner's `--data-dir` (`before/`, `after/`,
   uncommitted, rebuilt by a re-run).

## The cell

| cell | item | serves | risk | slot |
|---|---|---|---|---|
| `CB-u-1` | E1: one cause class per "neither" mover (sweep balance in the daily value / prior MATCH by offsetting errors / other, named), counts summing to 147; one month per class traced end to end; the 16 core months reported separately | FWD-3 | LOCAL | `0.9.0_WK_ADVI_COTBKF~42` |

**Fan-out:** `1 of 1 chains, cap 8`.

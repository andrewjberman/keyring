# ADVI_COTBKF decomposition -- ROUND 23 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-08 ~19:4xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-22 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_22_20261008.md` @4899e3797f (msg 1501):
the round-21 one-mechanism ruling is falsified (D2-S32 OPEN); fix the 23 regressions before adding anything (D2-S34); then the
dividend and fee legs (W43-S1), layered so each rule's effect stays separately measurable.

**Rule 24.** Domain: E1, E2. Two cells, one chain: E2 is graded against E1's baseline and both write the cash-leg rule in
`commonwealth_sweeps.py` and the runner, so E2 depends on E1 and they run on one worker in order.

## Measured constraints

1. Round 22's real run on the trunk (@4839b6f2d2): arms v1/`r19` -> v1/`repaired`, `months_after=2103/1520/78970 control_same=True`;
   25 of 163 movers back to MATCH (`sweep_balance` 25/72, `sweep_trade_day` 0/75, core 0/16); 23 MATCH -> DIFF regressions, 19 in
   acct#c42b98c0 and acct#05dd4a9d (`deliverables/0.9.0_WK_ADVI_COTBKF~43/sweep_regrade.md`).
2. The runner selects the cash-leg rule per arm (`--before-cash-leg` / `--after-cash-leg`: `r19`, `repaired`).
3. W43-S1: dividend rows fund sweep buys and `man`/`fch` fee rows are paid by sweep sales with no matching cash leg; 94 of the 122
   `neither` movers still DIFF carry such a row on a sweep-trade day.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-w-1` | E1: class the 23 regressions (existing CFNCASH leg / other, named); the funding credit only where no CFNCASH row for that sale exists (rule `conditional`); re-grade `r19` -> `conditional` with 0 regressions and the 25 kept | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~45` |
| `CB-w-2` | E2: one general dividend/fee cash-leg rule for the trade-day months (rule `divfee`, layered on `conditional`); re-grade `conditional` -> `divfee`, the 75 counted back, every DIFF named, 0 new regressions | FWD-3 | LOCAL | `CB-w-1` | `0.9.0_WK_ADVI_COTBKF~45` (continued) |

**Fan-out:** `1 of 1 chains, cap 8` (a chain of two cells).

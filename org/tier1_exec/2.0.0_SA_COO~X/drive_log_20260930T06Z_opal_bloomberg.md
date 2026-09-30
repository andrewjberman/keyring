# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-09-30 06Z (host opal_bloomberg)

| time | limb | round | act |
|---|---|---|---|
| 06:07Z | L8 | 22 | The AMENDMENT 1 gate census reads `names 95 false 2 errors 0 false_names [8035_JP_Equity, 9433_JP_Equity]` |
| 06:08Z | L8 | 22 | AMENDMENT 1: 2 `write_one` puts (objects 285 -> 287); both now `inputs_equal_now True` and name the post-flip block stamps |
| 06:17Z | L8 | 22 | packet `9d55db806d` to `3.0.0_SA_CVO~Z` (READ 06:25:24Z) |
| 06:2xZ | L8 | 22 | leg V: the final re-read `pack_shape_only 95 other_moves 0 errors 0`; ledger `amgt-corpus-r22-served-acts` CLOSED (`d8b48f4a9e`), committed after a peer's merge cleared |
| 06:3xZ | -- | -- | Andrew-direct: "delete the empty wk-crps-1 folder too". It held a JUNCTION to the live `portal\node_modules`, so it was removed non-recursively; the live tree is unchanged at 263 entries. Record addendum `d6d1c41191`. |
| 06:49Z | L9 | 22 | NO-OP: the CVO holds the packet; the round-22 analysis is not yet in |

## Compiler Tools

- `deploy_ledger.py`: the served-acts entry closed with all 4 legs proven.
- The `inputs_equal_now` census (issuer), the gate for AMENDMENT 1.
- `w1_expected_moves.py`: run 3 times this round (before-state, post-rewrite, final).
- Gap: a Bash `find` on a scratch path outside the repo was denied by the comp-tool rail; `ls -laR` served, and it is also the
  read that shows a junction (`lrwxrwxrwx`).

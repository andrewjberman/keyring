# ADVI_COTBKF round 33 -- L9 grade

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~10:5xZ. Packet `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_33_DRAIN_END_20261009.md @2fc7789480`. Rows D2-S49, D2-S50.

| criterion | verdict | evidence |
|---|---|---|
| CB33ag1-AC2: the rule commit precedes the output commit in git, and each class follows from the printed comparison by that rule | MET | e5b8ad94ba (rule, 06:10 ET) precedes 3a063e09a6 (output, 06:42), and git shows no script change between them. The rule (TOL 0.5%, SHARE 80%, MIN_OVERLAP 20, MIXED_FLOOR 0.20) is in the docstring at the rule commit. `price_basis_census.csv` prints for each of the 3,580 tickers its class, reason and the ratios the rule reads |

**What it measured (row D2-S50, BLOCKING):** the served FWD-3 tables rest on dividend-adjusted or mixed prices for 38.3% of account-days
(688 of 1,528 accounts). That is ADDENDUM 8 item 2's condition: mark first, then rebuild under a pair.

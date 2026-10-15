# IRPT_DASHBD round 118 -- workstream F-SHIP (~F2) decomposition: one test for the scalar case (row W506-S1)

Issuer `2.0.0_SA_COO~F2`, 2026-10-15 ~07:4xZ. Gate key: `<round>118</round><workstream>~F2</workstream>`. Workstream label beside the round: **F-SHIP, round 118**.

**Answers:** the CTO's B-49F round-120 analysis, ruling 6 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_120_20261015.md` @5e358b0a8f, msg 8177): "W506-S1 (the scalar `by_row` case is unpinned) goes to
`~F2`: one test". Round 117's finding: the report model reads the sixteen `avs` benchmark members as by_row per account (row D2-S67); worker 506 found a household scalar under one of them prints as every account's figure.

## Cell

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| ONE test in `__tests__/irpt-dashbd/avs-by-row.test.tsx`: a household scalar under one account-grain `avs` benchmark member; assert what the model prints today (the same figure for every account), commented as a pin of the present behaviour on an input the producer must never emit; no source change | `DB-f-507` | FWD-21 | LOCAL (a test on the portal branch, never pushed), DIRECT-ACT | none | R118-F-A |

**Decisions inside this decomposition (the issuer's, stated):** (a) the test pins TODAY's behaviour, found by running it, because the contract's own rule makes the input a producer defect and the guard is the producer's (S67's note to `~D2`); a reader guard that
prints the absent words instead is a later cell the CTO may cut, and it would change this test on purpose; (b) test only; (c) direct-act: one test, LOCAL.

**Four-postulate record.** (i) Domain: one test file. (ii) Same grain: one member under one household. (iii) One intent: the case is pinned. (iv) Not moved: every source file and every other test.

**Chain read.** M = 1. N = 1.

fanout: 1 of 1 chains, cap 8, portal_ref: `cand/dell2/irpt-default-performance-report` (0d58fe2c43ffad9ca2ffeda422b42681c3494d1c), reason: one direct-act cell with a single write set. Worker `0.9.0_WK_IRPT_DASHBD~507` (`DB-f-507`, worker-light).

| criterion | invocation | base reading |
|---|---|---|
| DBF118-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r118/p118_scalar.py . DBF118-1-AC1` | FAIL (no test file on the main tree; at the candidate head the title word `scalar` is absent) |
| DBF118-1-AC2 | `... p118_scalar.py . DBF118-1-AC2` | FAIL (no change from the candidate head) |

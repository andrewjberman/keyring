# ETFS_RIVALS round 30: five rivalfunds packages to pin ea0e5025ac, plan 0/5/0 -- 0.7.0_AE_CloudOps~DELL1

**Date:** 2026-10-14 (UTC; ~14:45Z - 15:0xZ)
**Task Order:** ETFS_RIVALS.TO-APPLY-R30.rivalfunds-packages-deploy-dell1 (risk WORLD)
**Status:** COMPLETE (L1); L2 is the issuer's, HELD on the 2026-10-15 11:00Z chain and 13:00Z sweep
**archetype:** DEPLOY
**Branch:** box/dell1

## Objective

Deploy the pin's five rivalfunds Lambda code packages and nothing else, as a saved graded plan applied through
`safe-apply`, before 2026-10-15 10:45Z and outside both fire windows.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| rivalfunds_package.py | from the pin tree | PASS | 5 lambdas staged |
| own byte control | raw bytes vs `git cat-file blob` | PASS | 480 of 480; negative control caught |
| terraform | init, plan -out, show -json | PASS | 45 changes: 40 no-op, 5 update |
| own STOP 3 grader | per attribute | PASS | branch A, 0 failures, doctored control caught |
| deploy_ledger.py | open / close-leg / hold | PASS | L1 closed; entry HELD external |
| safe-apply.sh | saved planfile | PASS | tagauthz PASSED, tombstone-gate CLEAN, rc=0 |
| r30_deploy_check.py | AC1 | PASS | 0 failures |
| proof-of-spec-check.py | instance AC1, governing order | VALID | rc=0 |
| comp-rail | one denial (a recursive grep over the lane's orders) | WARN | ran nothing; answered with the native Grep on the named folder |

**What worked:** the BEFORE read equalled the round-29 AFTER hashes, so the diff against the prior act was a comparison,
not a re-derivation; the saved planfile made applied bytes equal graded bytes (5 of 5).
**What failed:** my first STOP 3 grader run FAILED on its own defect: it read an all-false `after_unknown` container
(`architectures: [false]`) as unknown. Fixed to count a value unknown only if it contains a true; the plan itself had
only `last_modified` and `source_code_hash` moving all along.
**Gap found:** none new.

## Work Completed

1. **Order and halves** read in full (msg 5613 acked READ 14:45:17Z; COO @77af4ef06f, CTO @35d1f02bc3 with C1, which binds the issuer).
2. **STOP 1:** pin tree HEAD `ea0e5025ac`, 0 porcelain lines, four blob ids equal the order's; rollback tree at `de3c6bf211`.
3. **Package, control, plan:** 480 of 480; `Plan: 0 to add, 5 to change, 0 to destroy`; STOP 3 branch A.
4. **Ledger** `etfs-rivalfunds-r30-dell1-20261014` opened 14:52Z with L1 (mine) and L2 (the issuer's).
5. **Apply** 14:52:47Z-14:53:44Z: `0 added, 5 changed, 0 destroyed`, rc=0.
6. **After:** AC1 PASS; applied==graded 5 of 5; env key sets unchanged; re-plan rc=0 No changes; L1 closed; entry held.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Applied the same afternoon, not waiting for the deadline's eve | the order's window runs until 10:45Z tomorrow and the apply is outside both fire windows; tonight's 21:00Z dell1 restart is not a constraint |
| Fixed the grader instead of reading the plan by eye | the grader is the instrument the order names; its control must keep working |

## Open Items

- L2 (the 2026-10-15 11:00Z chain and 13:00Z sweep) is the issuer's.
- `C:/tmp/rv-r30-dell1` and `C:/tmp/rv-r30-rollback` stay until L2 closes; the rollback tree is not initialised or packaged.
- The order's `<status>` is the issuer's to flip.

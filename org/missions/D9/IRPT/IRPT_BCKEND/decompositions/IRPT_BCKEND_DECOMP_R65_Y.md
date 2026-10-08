# IRPT_BCKEND round 65 -- workstream ~Y decomposition (X-1 release 2, run as signed)

Issuer `2.0.0_SA_COO~Y2`, 2026-10-08 ~17:4xZ. Input: `1.0.0_SA_CTO~DELL2` ROUND ANALYSIS (sweep 17) @0a91529221,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUNDS_75_76_P_64_Y_20261008.md`, ENRICHMENT item E2.
ONE issuance, one cell, no edges. Base: dell2 CLOUD HEAD carrying pin `f7a9d0b34f` (on origin CLOUD `4adc60e32f`).

| item | cell | cut? |
|---|---|---|
| E2: release 2 of `irpt-ycharts-generate`, run as signed (pair @bf4707adf1 + CTO half @6d24511482 with its three conditions) | `IB-yr-651` | **CUT** |

## Cell IB-yr-651

The worker deploys pin `f7a9d0b34f` (built `798Lgqw2...`) to `irpt-ycharts-generate` under a change-management ledger entry,
runs the pair's after-reads 1-7 with a TEST OPAL_GLOBAL filer (no login identity; direct IAM invoke; put only after the
equality read), deletes the test row and its upload records in every branch, and rolls back to `ZspX0qD2...` the same session
on any failure. The CTO analysis permits `TAGAUTHZ_OVERRIDE` (row S334 interim) for this one named apply, with the plan text
committed before the apply.

| criterion | invocation | base reading |
|---|---|---|
| Y65-1-AC1 (released, reads pass) | `python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r65/y65_cells.py . Y65-1-AC1` | FAIL (no after-reads file); live `ZspX0qD2...` |
| Y65-1-AC2 (test data gone) | `... y65_cells.py . Y65-1-AC2` | FAIL (no file) |
| Y65-1-AC3 (branch coherent, ledger closed) | `... y65_cells.py . Y65-1-AC3` | FAIL (no file) |

Risk WORLD: the CTO analysis names SERVED, and the L6 gate floors the source map at WORLD. The real filer entitlement stays Andrew's and does not hold this cell.

## Four-postulate record

(i) Domain: the one function both halves sign, plus the one test row and the upload records the admit read creates; nothing
else is written. (ii) One release. (iii) One intent: X-1 live, proven, with no residue. (iv) The real filer entitlement and
every other function do not move.

fanout: 1 of 1 chains, cap 8, reason: one item.

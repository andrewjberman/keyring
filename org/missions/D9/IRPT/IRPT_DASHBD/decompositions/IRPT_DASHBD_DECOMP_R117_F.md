# IRPT_DASHBD round 117 -- workstream F-SHIP (~F2) decomposition: the `avs` benchmark members read as by_row per account (row D2-S64)

Issuer `2.0.0_SA_COO~F2`, 2026-10-15 ~06:5xZ. Gate key: `<round>117</round><workstream>~F2</workstream>`. Workstream label beside the round: **F-SHIP, round 117**.

**Answers:** the CTO's B-49F round-119 analysis, ruling 6 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_119_20261015.md` @d856067e84, msg 8101): the `~F2` debt gets a carrier; `~D2` filed it as
row `IRPT_DASHBD-D2-S64` (ARMED, disarm owner this seat): the sixteen `avs.<window>.benchmark_<kind>` members are account-grain `by_row` in the contract and in the producer's table, and the portal reader's reading of them is unverified.

## What was measured at the cut (read of `cand/dell2/irpt-default-performance-report` @e23ddb8e, `dashboard/report/reportModel.ts`)

`valueSummaryGrid(report, 'avs', ..., account)` builds each account's value summary and reads every row through `figureCell(report, prefix.window.row, account.account_id, notHeld)` (about lines 645-661), whose `by_row`
branch reads `raw.by_row[rowKey]` (about lines 483-495); the benchmark members are rows of that table (`VS_ROWS`, about lines 358-361). So the model appears to read them as by_row per account: **unpinned, not wrong**. The contract
form is `{by_row: {account_id: figure}}` for an account-grain member (`document.filled_report.per_row_member_form`). No test feeds the sixteen in that shape.

## Cell

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| A NEW TEST FILE, `__tests__/irpt-dashbd/avs-by-row.test.tsx`: a three-account household whose sixteen `avs` benchmark members are by_row maps with different figures per account, one absent entry and one not-spanned window; asserts each account prints its own figure, no other account's, the absent words, never a household scalar; one temporary mutant. No source change; a model that does not read them as by_row is a FINDING (a BLOCKING row), never an edit | `DB-f-506` | FWD-21 | LOCAL (a test file on the portal branch, never pushed), DIRECT-ACT | none | R117-F-A |

**Decisions inside this decomposition (the issuer's, stated):** (a) test only: the row asks to READ the reader and pin it; a reading that proves wrong is reported with the printed figure and the repair is a later cell under the CTO's analysis;
(b) the fixture's shape is the contract's, taken once from the producer's `rows_to_document` on synthetic rows (a dict builder, no file, no service) and typed as a literal, so the test pins the producer's real shape, not the sample's;
(c) the row's disarm is the issuer's, on the cell's finding, in a new row (append-only); (d) direct-act: one cell, test only, LOCAL, under the size floor.

**Four-postulate record.** (i) Domain: one new test file in `__tests__/irpt-dashbd/`. (ii) Same grain: one account's value summary. (iii) One intent: the sixteen members read by account. (iv) Not moved: every source file, every other test, the contract, the producer.

**Chain read.** M = 1. N = 1.

fanout: 1 of 1 chains, cap 8, portal_ref: `cand/dell2/irpt-default-performance-report` (e23ddb8e34035bb6fa6dc5e59d7f83220e83d65c), reason: one direct-act cell with a single write set. Worker `0.9.0_WK_IRPT_DASHBD~506` (`DB-f-506`, worker-light).

| criterion | invocation | base reading |
|---|---|---|
| DBF117-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r117/p117_avs.py . DBF117-1-AC1` | FAIL (no file) |
| DBF117-1-AC2 | `... p117_avs.py . DBF117-1-AC2` | FAIL (no change from the candidate head) |

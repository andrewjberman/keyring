# IRPT_DASHBD round 135 -- workstream F-SHIP (~F2) decomposition: the contract 0.5.1, the Inflection transaction launcher and the dispatch step

Issuer `2.0.0_SA_COO~F2`, 2026-10-16 ~17:5xZ. Gate key: `<round>135</round><workstream>~F2</workstream>`. Workstream label beside the round: **F-SHIP, round 135**.

**Answers:** the CTO's round-133 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_133_20261016.md` @46427ce727, msg 9679; the CVO's v145, round 133 closes), Addendum 2 of the round-134 analysis (@5d8adf5722, msg 9669: S6 final, both legs INTERNAL; the EXTERNAL ruling is WITHDRAWN) and the CTO's instruction of msgs 9625/9486 (the Orion `fact_transactions` table is cumulative snapshots; the producer reads ONE snapshot, the newest partition for the run day, and emits lines by trade date; no source line on more than one emitted day over the full output; the producer is a best-effort post-sentinel step of the Orion gold dispatch chain). The enrichment list it sets, with the state of each item at the cut:
1. **The contract 0.5.1:** the Inflection counts restated on the latest snapshot, `inflection_table_shape`, `s6_status` `RULED_INTERNAL_REINVESTMENT`, the 96-of-96 equal-amount-line release criterion, "S6 open" dropped: **cell `DB-f-2101`.**
2. **The one-snapshot launcher with a pinned bundle** (the chain syncs scripts flat and the producer locates the repo by `parents[5]`): **cell `DB-f-2102`.**
3. **The dispatch catalog row, chain `txn` and the best-effort post-sentinel block:** **cell `DB-f-2103`.**
4. **The release pairs in the ruled order** (49 Financial, Cottonwood, Inflection): NOT cut this round; each names FINAL producer bytes and the Inflection pair names this round's launcher, dispatch edit and contract, so it follows the drain. The 49 Financial and Cottonwood pairs also wait for `~D2`'s DB-b-300 gold ledger to read CLOSED. The S6 criterion (96 of 96, printed) rides the Inflection pair; the launcher's `s6_report` is the instrument that prints it, and the Reversed keys are derived in the run.
5. **Cottonwood transaction Income enrichment** (sizing note `R131_COTTONWOOD_INCOME_SIZING.md`): after the release.

## What was measured at the cut

Nothing new is needed from the world: the rulings are the CTO's and the censuses are the issuer's R135 records (latest-snapshot counts, the sign combinations, the cash-move and reinvestment counts: 96 of 96 events carry an equal-amount Buy or Income Reinvested line). The state on trunk (read): contract 0.5.0, 19 columns; the three producers on the shared claim function. The checkers exist and fail at base (dry-run at the cut, below).

## Cells (ONE issuance; LOCAL)

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| Contract 0.5.1 + words file (generator copied from the 0.5.0 one) | `DB-f-2101` | FWD-5 | LOCAL | none | R135-A |
| Launcher `INF_G_01.account_transaction_gold.py`, manifest, deterministic bundle with a sha256 pin, tests | `DB-f-2102` | FWD-5 | LOCAL | `DB-f-2101` (the bundle pins the bytes of `transaction_words.json`, which 0.5.1 changes) | R135-A |
| Dispatch catalog row, `CHAIN_TXN`, `run_txn_step`, `--chain txn`, TXN-BLOCK, tests | `DB-f-2103` | FWD-5 | LOCAL | none | R135-B |

**Judgment criteria.** None are set on the cells: all three are mechanical. The next fresh grade (J samples of the producers' output) prints the Inflection denominators on the ONE snapshot, and the S6 print (N of 96) goes to the CVO with the packet.

**Decisions inside this decomposition (the issuer's, stated):** (a) the bundle's location at run time is a file `INF_G_01.bundle.zip` beside the launcher (the chain's flat sync of `code/gold` brings both), with `INF_IRPT_BUNDLE_LOCAL` for the checker and the tests; the zip is built, not committed, and the release uploads it. Whether the runner's sync copies a `.zip` is a question for the release pair, stated there. (b) The producers are imported lazily, from the repo layout when the launcher sits in it. (c) `2102` is cut now and spawned after `2101` merges, from the merged trunk. (d) `2103` edits the dispatch script by insertion against a pinned base copy (sha256 `e9aef66b...`), so any other edit of that script before the merge shows as a failing criterion, not a silent merge. (e) Three mechanical criteria across three cells: one, two and one.

**Four-postulate record.** (i) Domain: the Inflection account-transaction lines of ONE snapshot per run; the counts are the latest snapshot's. (ii) Same grain: one line per emitted row, one claim per line, one snapshot per run. (iii) One intent: the step reads the table as what it is (a cumulative snapshot) and emits each source line on exactly one day. (iv) Not moved: the ratified words, the flow classes, the claim function, the 49 Financial and Cottonwood producers, the Eclipse block and every chain other than the new `txn`.

**Chain read.** M = 2 (R135-A: `2101` then `2102`; R135-B: `2103`), N = 3 cells.

fanout: 2 of 2 chains, cap 4 (the CTO's ruling), portal_ref: none, reason: `2101` and `2103` start now in parallel; `2102` follows `2101` because its bundle pins the words file `2101` changes. Workers `0.9.0_WK_IRPT_DASHBD~2101`, `~2102`, `~2103`.

| criterion | invocation | base reading |
|---|---|---|
| DBF135-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r135/p135_contract.py . DBF135-1-AC1` | FAIL (the contract is 0.5.0) |
| DBF135-2-AC1 | `python -I .../checks/r135/p135_step.py . DBF135-2-AC1` | FAIL (no launcher) |
| DBF135-2-AC2 | `python -I .../checks/r135/p135_step.py . DBF135-2-AC2` | FAIL (no launcher) |
| DBF135-3-AC1 | `python -I .../checks/r135/p135_dispatch.py . DBF135-3-AC1` | FAIL (no catalog row, chain or block) |

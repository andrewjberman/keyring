# IRPT_DASHBD round 125 -- workstream F-SHIP (~F2) decomposition: the transactions table view model (FWD-5)

Issuer `2.0.0_SA_COO~F2`, 2026-10-16 ~05:1xZ. Gate key: `<round>125</round><workstream>~F2</workstream>`. Workstream label beside the round: **F-SHIP, round 125**.

**Answers:** the empty-tick sequence (`/next-calls IRPT_DASHBD --drive`), which found one FREE option around the FWD-5 block: the table's logic does not depend on the ratified words or on the contract's last details. Serves the PRD's FWD-5 and its workstream F item 3 ("The transactions table: sort, type filter, symbol search, export, virtualised").

## What was measured at the cut

- The brief names 14 columns for `account_transaction`; the round-123 ground read found 7 have a 49 Financial silver source and 7 do not (`settle_date`, `asset_name`, `fee` absent; `custodian`, `flow_class`, `coverage` constant or derived; `source_txn_id` unsourced). The table must print an absent value as not available, never a zero.
- The words for `action` and `txn_type` are not ratified (round-122 analysis, msg 9036); the model therefore names no word and derives the type filter's choices from the rows.
- No portal file for FWD-5 exists; the holdings tab already has a filter and sort idiom.

## Cell (ONE issuance; LOCAL)

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. The TRANSACTIONS TABLE VIEW MODEL and its tests: row type with nullable absent columns, type filter, symbol search, stable sort with nulls last, export text with a formula guard, virtualised window; new files only, not mounted | `DB-f-1101` | FWD-5 | LOCAL | none | R125-A |

**Not in this round (stated, with the reason):** the contract, the producer and the route (wait on the ratified words and the never-widen release); the reader and the table component (wait on the contract's shape); the FWD-3 mount (waits on `~D2`'s `class_object` 0.4.0 and `~S2`'s route member).

**Decisions inside this decomposition (the issuer's, stated):** (a) NOT mounted, requests nothing; (b) new files only, cut from `origin/PROD` @a062c56e (a view model that depends on nothing unreleased); (c) a null column is `null` in the row type and an empty field in the export; (d) the export guards against spreadsheet formulas in text fields (a text value starting with `=`, `+`, `-` or `@` is prefixed with a single quote; numbers are never prefixed); (e) two mechanical criteria.

**Four-postulate record.** (i) Domain: one view model over the brief's printed 14 columns. (ii) Same grain: one transaction line. (iii) One intent. (iv) Not moved: the holdings helpers, the tab, the contract, every served file.

**Chain read.** M = 1, N = 1.

fanout: 1 of 1 chains, cap 8 (the CTO's CPU budget holds `~F2` at 4 per issuance; worker `~1001` of round 124 is also running), portal_ref: `origin/PROD` @a062c56e53b174eab043b1e50002c93eb7a56f8b, reason: one independent cell, new files only. Worker `0.9.0_WK_IRPT_DASHBD~1101` (`DB-f-1101`).

| criterion | invocation | base reading |
|---|---|---|
| DBF125-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r125/p125_txview.py . DBF125-1-AC1` | FAIL (no test file) |
| DBF125-1-AC2 | `... p125_txview.py . DBF125-1-AC2` | FAIL (no change) |

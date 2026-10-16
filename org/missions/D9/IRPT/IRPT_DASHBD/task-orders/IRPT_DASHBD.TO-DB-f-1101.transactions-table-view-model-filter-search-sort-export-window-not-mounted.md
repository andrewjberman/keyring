# TO IRPT_DASHBD.TO-DB-f-1101 -- the TRANSACTIONS TABLE VIEW MODEL: one new portal file that holds the pure logic of the FWD-5 transactions table (the brief's 14 columns as a row type with the absent ones nullable, the type filter, the symbol search, the sort, the export text with a formula guard, and the virtualised window) plus its tests; new files only, not mounted, nothing requested, no word of the Opal vocabulary hard-coded

<to_id>IRPT_DASHBD.TO-DB-f-1101</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~1101</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>125</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** the PRD (`org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md`, FWD-5 "A person browses the transactions for any account and window, filters, sorts and exports them"; workstream F item 3 "The transactions table: sort, type filter, symbol search, export, virtualised"), the CTO's round-119 analysis ruling 3 (`~F2` owns FWD-5) and the round-121 analysis (the first served account is a 49 Financial one) | **Rows:** IRPT_DASHBD-D2-W1101-S<k> | **Decomp cell:** `DB-f-1101` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R125_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-1101` (branch `wk-IRPT_DASHBD-1101`); run everything from its root unless a step says the portal. `C:/dev/wk-irpt-dashbd-1101/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-1101-portal`), cut from `origin/PROD` @a062c56e53b174eab043b1e50002c93eb7a56f8b. Portal files commit in the portal repo with plain git and your author line (`0.9.0_WK_IRPT_DASHBD~1101 <0.9.0_WK_IRPT_DASHBD~1101@opal.agent>`; set the committer identity in the command environment only, never in a config); your folder, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1101/`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours. Made-up ids, symbols and figures only. All portal paths below are under `portal/src/pages/InvestorReporting/`.

**Why.** FWD-5's table does not depend on the ratified words or on the contract's last details: a row has the brief's 14 columns (`docs/briefs/reporting-dashboard-backend-brief-20260930.md` line 78), and the filter, search, sort, export and virtualisation act on those columns as plain values. The brief's columns are `trade_date`, `settle_date`, `action`, `txn_type`, `symbol`, `asset_name`, `units`, `price`, `amount`, `fee`, `custodian`, `flow_class`, `source_txn_id`, `coverage`. The round-123 ground read (`deliverables/0.9.0_WK_IRPT_DASHBD~901/RD_FWD5_PRODUCER_GROUND_R123.json`) found `settle_date`, `asset_name`, `fee` and (probably) `source_txn_id` have no 49 Financial silver source, so the row type holds them as `null` and the table prints them as not available, never a zero or a blank that reads as a figure. `action` and `txn_type` hold Opal words (ratification pending): this model NEVER names a word; the type filter's choices are the distinct `txn_type` values present in the rows.

**The cell (`DB-f-1101`).**
1. **Read first.** `tabs/holdings/` (the securities list's existing filter and sort helpers, which the round-119 thread read named as reusable: find them with `comp-find --files 'sort' portal/src/pages/InvestorReporting/tabs/holdings --limit 20` and print the denominator), `tabs/reporting/classes/classWindowModel.ts` on the class candidate (via `git -C portal show cand/dell2/irpt-asset-class-performance:src/pages/InvestorReporting/tabs/reporting/classes/classWindowModel.ts`) for this project's pure-model style. Do not import a helper that would pull a React component; copy the idea, not the dependency, if it would.
2. **ONE new source file** `tabs/reporting/transactions/transactionsView.ts` exporting, pure (no clock, no DOM, no network, no import of a tab or section, no word of the Opal vocabulary):
   - `type TransactionRow` with the 14 fields above: `trade_date` and `settle_date` ISO date strings (`settle_date` nullable), `action`, `txn_type`, `symbol` strings (`symbol` nullable for a cash line), `asset_name` (nullable), `units`, `price`, `amount` numbers (`units` and `price` nullable for a line with none), `fee` (nullable number), `custodian` string, `flow_class` string, `source_txn_id` (nullable string), `coverage` string.
   - `TRANSACTION_COLUMNS`: the 14 columns in the brief's order with a client-safe header word each (no code, no table name).
   - `filterByType(rows, types)`: keeps the rows whose `txn_type` is in `types`; an empty `types` keeps every row.
   - `searchBySymbol(rows, query)`: case-insensitive, trims the query; matches `symbol` and `asset_name` by prefix of any word; an empty query keeps every row; a null `symbol` never matches a non-empty query.
   - `sortRows(rows, key, direction)`: a STABLE sort by one column, ascending or descending; nulls always last in both directions; dates by ISO string, numbers numerically, strings case-insensitively; ties keep the input order.
   - `distinctTypes(rows)`: the distinct `txn_type` values present, sorted.
   - `exportCsv(rows)`: the export text: a header line of the column headers, then one line per row in the order given, values in the brief's column order; a null prints as an empty field; fields containing a comma, a quote or a newline are quoted with doubled quotes; a text field whose first character is `=`, `+`, `-` or `@` is prefixed with a single quote (formula guard), a NUMBER is never prefixed; lines end with `\\n`.
   - `visibleWindow(total, rowHeight, scrollTop, viewportHeight, overscan)`: returns `{ start, end }` (end exclusive) for the virtualised list: clamped to `[0, total]`, with `overscan` rows each side; `total` 0 gives `{0, 0}`; nonsense input (a non-positive `rowHeight`) gives `{0, 0}`.
   - `viewRows(rows, { types, query, sortKey, sortDirection })`: applies filter, then search, then sort, in that order, and returns the rows; never mutates its input.
3. **ONE new test file** `__tests__/irpt-dashbd/transactions-view.test.ts`, made-up rows only, at least 12 tests whose titles together contain the words `filter`, `search`, `sort`, `export`, `window`, `absent`, `formula` and `order`: the type filter with and without a selection; the search by symbol prefix, by asset-name word prefix, case-insensitive, and a null symbol; the sort ascending and descending, nulls last in both, stable ties; an absent `settle_date` / `fee` / `asset_name` row survives every operation and exports as an empty field; the export header and column order, quoting a comma, a quote and a newline; the formula guard (`=SUM(A1)`, `+1`, `-1`, `@x` are prefixed, a negative NUMBER is not); the virtualised window at the top, the middle, the end, with overscan, with zero rows and with a bad row height; `viewRows` order of operations and no mutation of the input.
4. **Gates, once, after your last portal commit:** from the portal worktree `bun run typecheck` and `bun run lint` (0 errors in your files) and `bun test src/pages/InvestorReporting`: the failing-test names after must be a subset of those before.
5. **Mutant** (temporary, reverted): make `sortRows` put nulls first in descending order; at least one test must fail. Say which.
6. **Record** `BUILD_R125.json` in your folder with exactly: `portal` {`branch` "wk-IRPT_DASHBD-1101-portal", `base` "a062c56e53b174eab043b1e50002c93eb7a56f8b", `head`, `files_changed`}, `tests` {`view_pass`, `suite_before_fail`, `suite_after_fail`}, `mutant_failed_tests` (a number), `typecheck_rc`, `lint_errors`, `pushed` false, `deployed` false.

<criterion id="DBF125-1-AC1" cell_refs="DB-f-1101"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r125/p125_txview.py" . DBF125-1-AC1</invocation><expect>DBF125-1-AC1 PASS</expect></criterion>
`DBF125-1-AC1` -- `transactions-view.test.ts` carries titles with the eight words `filter`, `search`, `sort`, `export`, `window`, `absent`, `formula` and `order`, and `bun test` on it passes with 0 failures and at least 12 tests. Base: FAIL (no file).
<criterion id="DBF125-1-AC2" cell_refs="DB-f-1101"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r125/p125_txview.py" . DBF125-1-AC2</invocation><expect>DBF125-1-AC2 PASS</expect></criterion>
`DBF125-1-AC2` -- bounds: the portal diff from `origin/PROD` @a062c56e to your head is exactly the two new files (`transactionsView.ts` and `transactions-view.test.ts`) and nothing else. Base: FAIL (no change).

<expected_criteria>DBF125-1-AC1,DBF125-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every source file (including the holdings helpers), every other test, the brief, the issuer's check.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change. The model is NOT mounted and requests nothing.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. Do not name an Opal action or type word anywhere in the source file (the words are being ratified); test rows use made-up placeholder words (for example `TypeA`).
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W1101-S<k>` (D2 is the device coordinate, never F2), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1101/
portal/src/pages/InvestorReporting/tabs/reporting/transactions/transactionsView.ts
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/transactions-view.test.ts
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-1101.transactions-table-view-model-filter-search-sort-export-window-not-mounted.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R125_F.md</decomp_doc> round 125, workstream ~F2 (F-SHIP), cell `DB-f-1101`.
<owned_cells>DB-f-1101</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF125-1-AC1, DBF125-1-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1101/IRPT_DASHBD.TO-DB-f-1101.transactions-table-view-model-filter-search-sort-export-window-not-mounted.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF125-1-AC1,DBF125-1-AC2` BEFORE the flip (one comma-separated argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the portal head sha; the exported names; the test counts, the mutant result and the typecheck and lint results; whether any existing holdings helper was reused or copied; anything off-task (as row ids). Made-up values only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: two new files on a local portal branch; nothing is wired, mounted, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed or requested.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF125-1-AC1 and AC2 FAIL at base and the checker's pure helpers are exercised by its self-test (7 arms).
lane: the <paths> block IS the grant.
</preflight>

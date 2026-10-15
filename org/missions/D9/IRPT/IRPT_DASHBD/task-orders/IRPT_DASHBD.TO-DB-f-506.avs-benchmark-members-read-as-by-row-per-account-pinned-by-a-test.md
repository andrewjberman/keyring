# TO IRPT_DASHBD.TO-DB-f-506 -- the SIXTEEN `avs` BENCHMARK MEMBERS READ AS by_row PER ACCOUNT: a new test file that pins the report model's reading of `avs.<window>.benchmark_<kind>` on a document shaped as the contract's per-row member form; test only, no source file changes (row D2-S64)

<to_id>IRPT_DASHBD.TO-DB-f-506</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~506</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>117</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, B-49F round-119 analysis ruling 6 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_119_20261015.md`: the `~F2` debt, reading `avs` `by_row`, gets a carrier) and the row it names, `IRPT_DASHBD-D2-S64` | **Rows:** IRPT_DASHBD-D2-W506-S<k> | **Decomp cell:** `DB-f-506` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R117_F.md`) | **outcome_ref:** FWD-21 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-506` (branch `wk-IRPT_DASHBD-506`); run everything from its root unless a step says the portal. `C:/dev/wk-irpt-dashbd-506/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-506-portal`), cut from `cand/dell2/irpt-default-performance-report` @e23ddb8e34035bb6fa6dc5e59d7f83220e83d65c. Do not amend or revert anything already committed there. Portal files commit in the portal repo with plain git and your author line (`0.9.0_WK_IRPT_DASHBD~506 <0.9.0_WK_IRPT_DASHBD~506@opal.agent>`); your folder, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~506/`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours. Made-up ids and figures only. All portal paths below are under `portal/src/pages/InvestorReporting/`.

**Why.** The default performance report's data is a filled-report document: `{household, values}` with `values` keyed by member id. For a member whose grain is an account (the account value summaries among them) the contract says the member holds `{"by_row": {"<account_id>": figure}}`, one key per account, and a figure is a number, a text or the absent form `{absent, kind}`; a household-grain member holds its figure directly, never a `by_row` map (contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json`, key `document.filled_report.per_row_member_form`). The producer's table carries the sixteen members `avs.<qtd|ytd|last_12_months|since_inception>.benchmark_<ultra_short_term|short_term|intermediate_term|long_term>` as one entry per account, where the earlier sample JSON the report model was first built against held one household scalar each. The model's reading of them as `by_row` per account has never been pinned by a test with that shape (row `IRPT_DASHBD-D2-S64`, owner this seat). Reading it: the model's account value summary (`valueSummaryGrid(report, 'avs', ...)` in `dashboard/report/reportModel.ts`, about lines 645-661 and 943) calls `figureCell(report, memberId, account.account_id, notHeld)`, which for a `by_row` value reads `raw.by_row[rowKey]` (about lines 483-495); the benchmark members are among the account value summary's rows (`VS_ROWS`, about lines 358-361). This cell PINS that behaviour with a test; it changes no source.

**The cell (`DB-f-506`).**
1. **Read first.** `dashboard/report/reportModel.ts` (`FilledReport`, `figureCell`, `valueSummaryGrid`, `VS_ROWS`, `buildReportModel`, how a model's account section exposes its cells), `dashboard/report/contractMembers.ts` (the member specs of the sixteen: unit `percent`), `dashboard/report/fixtures/syntheticReport.ts` (the made-up report the tests use; how a fixture is typed), and `__tests__/irpt-dashbd/report-render-r104.test.tsx` and `report-render-r111.test.tsx` (the style: `bun:test`, `renderToStaticMarkup`, building a `FilledReport` literal, finding a member by its `data-member` id). Run `bun test src/pages/InvestorReporting/__tests__/irpt-dashbd` once before any edit (base: record the failing-test count).
2. **The fixture shape (from the contract, not from the sample).** Build, in your test file, a `FilledReport` with a household of THREE made-up accounts whose `window_status` entries are all `MEASURED` except that the third account's `since_inception` window is `NOT_SPANNED`; take every other value from the synthetic report (spread it) and REPLACE the sixteen benchmark members with `{ by_row: { <account_id>: figure } }` maps, one key per account, with DIFFERENT figures per account (so a household-scalar read would be caught), where one account's entry for one member is the absent form `{ absent: '<words>', kind: 'INSUFFICIENT_HISTORY' }`. To be sure your literal has the exact shape the producer emits, you may, once, run `python data/assets/scripts/gold/irpt_reporting/filled_report_values.py`'s `rows_to_document` on a few synthetic rows (read its source first: it only builds a dict; it reads no file and calls no service) and copy the printed shape into your test as a literal; never import the Python in the test.
3. **The test file** (NEW; `bun:test`; no network): `__tests__/irpt-dashbd/avs-by-row.test.tsx`, at least 8 tests whose titles contain, between them, the words `by_row` (each account's figure is printed in that account's own value summary: assert the three accounts print three different figures for the same member), `account` (an account's table prints no other account's figure), `benchmark` (all sixteen members are covered: loop the sixteen ids and assert each one's `data-member` cell appears once per account in the account sections), `absent` (the absent entry prints the absent words and its reason is the cell's attribute only, never a figure and never zero), `household` (a `by_row` map under a household-grain member is never read as a household figure: add the same sixteen as plain household scalars in a second fixture and assert the account tables do NOT print that scalar as an account's figure; they print the absent words for a missing row) and `window` (a not-spanned window prints the not-spanned words, not a figure, for the third account). Also ONE temporary mutant you make and revert yourself: change the model to read `raw.by_row` by a fixed key or to read the member as a scalar, show that at least two of your tests fail, then `git checkout --` the file (the file is not yours to keep changed; the final head must hold only your new test file).
4. **Gates, once, after your last portal commit:** from the portal worktree `bun run typecheck` and `bun run lint` (0 errors each) and `bun test src/pages/InvestorReporting`: the failing-test names after must be a subset of those before (20 failed at the candidate head).
5. **If the model does NOT read the members as by_row** (a test you wrote from the contract fails against the unmodified model), that is the finding: do NOT edit the model. File a BLOCKING row naming the member, the account and the printed figure, keep the failing test out of the committed file (commit only the tests that pass and one test per failing case marked `test.todo` with its title), and stop on that point.
6. **Record** `BUILD_R117.json` in your folder with exactly: `portal` {`branch` "wk-IRPT_DASHBD-506-portal", `base` "e23ddb8e34035bb6fa6dc5e59d7f83220e83d65c", `head`, `files_changed`}, `members_covered` (the integer count, 16 when all are covered), `accounts` (3), `finding` ("reads_by_row" or "does_not_read_by_row", in one of those two words), `tests` {`avs_pass`, `suite_before_fail`, `suite_after_fail`}, `mutant_failed_tests` (the integer), `typecheck_rc`, `lint_errors`, `pushed` false, `deployed` false.

<criterion id="DBF117-1-AC1" cell_refs="DB-f-506"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r117/p117_avs.py" . DBF117-1-AC1</invocation><expect>DBF117-1-AC1 PASS</expect></criterion>
`DBF117-1-AC1` -- `__tests__/irpt-dashbd/avs-by-row.test.tsx` exists, its titles carry the six words `by_row`, `account`, `benchmark`, `absent`, `household` and `window`, and `bun test` on it passes with 0 failures and at least 8 tests. Base: FAIL (no file).
<criterion id="DBF117-1-AC2" cell_refs="DB-f-506"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r117/p117_avs.py" . DBF117-1-AC2</invocation><expect>DBF117-1-AC2 PASS</expect></criterion>
`DBF117-1-AC2` -- bounds: the portal diff from the candidate head `e23ddb8e` to your head is exactly that one test file. Base: FAIL (no change).

<expected_criteria>DBF117-1-AC1,DBF117-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every source file (including `reportModel.ts` and `contractMembers.ts`), every other test, the contract, the Python module, the issuer's check.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A model that does not read the members as by_row is a FINDING (step 5), never a source edit.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W506-S<k>` (D2 is the device coordinate), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~506/
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/avs-by-row.test.tsx
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-506.avs-benchmark-members-read-as-by-row-per-account-pinned-by-a-test.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R117_F.md</decomp_doc> round 117, workstream ~F2 (F-SHIP), cell `DB-f-506`.
<owned_cells>DB-f-506</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF117-1-AC1, DBF117-1-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~506/IRPT_DASHBD.TO-DB-f-506.avs-benchmark-members-read-as-by-row-per-account-pinned-by-a-test.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF117-1-AC1,DBF117-1-AC2` BEFORE the flip (one comma-separated argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the portal head sha; the finding word (`reads_by_row` or `does_not_read_by_row`) with the evidence; the number of members and accounts covered; the mutant's failing-test count; the test counts and the typecheck and lint results; anything off-task (as row ids). Made-up values only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a new test file on a local portal branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF117-1-AC1 and AC2 FAIL at base and the checker's pure helpers are exercised by its self-test (8 arms).
lane: the <paths> block IS the grant.
</preflight>

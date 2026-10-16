# TO IRPT_DASHBD.TO-DB-c-25 -- FWD-10 cell (a), round 147: the Performance tab prints the trading days the source did not report, read from the series' `unreported_trading_days` field for the window shown; the page mirror takes on contract 0.3.0; fixtures made by the contract's writer; portal edits plus one new bun test; no deploy, no push

<to_id>IRPT_DASHBD.TO-DB-c-25</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~417</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>147</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's B-CW instruction (msg 8788, cell (a): "the unreported-days sentence for any window holding one, read from the report-build output") on PRD ADDENDUM v0.15 and v0.16 (`org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md`), the carrier ruling (msg 8795) and `~D2` msg 9020 (series contract 0.3.0 and its writer are on trunk) | **Rows:** IRPT_DASHBD-D2-W417-S<k> | **Decomp cell:** `DB-c-25` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 16) | **outcome_ref:** FWD-10 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-417`); run everything from its root unless a step says the portal. Its nested `portal/` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-417-portal`) cut from the portal `DEV` head `03f92d82c23fc270e1115c15989e7637f430e16d`. Do not amend or revert anything already committed there. Portal files commit in the portal repo with plain git and your author line (`0.9.0_WK_IRPT_DASHBD~417 <0.9.0_WK_IRPT_DASHBD~417@opal.agent>`; set it for that repo with the environment variables `GIT_AUTHOR_NAME`, `GIT_AUTHOR_EMAIL`, `GIT_COMMITTER_NAME`, `GIT_COMMITTER_EMAIL`, since the portal repo holds no identity); your folder, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh` (never `--no-verify`). Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~417/`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours. Made-up ids and figures only; no AWS call, no network, no client data. All portal paths below are under `portal/src/pages/InvestorReporting/`.

**Why (the outcome).** PRD FWD-10: "A person can always tell what they are looking at: where the data starts, which trading days the source did not report, and how current the data is." Series contract 0.3.0 carries the list of the trading days its source did not report (`unreported_trading_days`, with the fixed text `unreported_trading_days_basis`). The page must say so, in one sentence where the number is, for the window the reader is looking at, and must never fill, carry or compute those days.

**What the contract says (read it, `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json`, `series.optional`, `series.fields.unreported_trading_days`, `series.fields.income`, `unreported_days_rule`).** `series.optional` is `class_value`, `class_weight`, `class_names`, `unreported_trading_days`, `unreported_trading_days_basis`. The list holds ISO dates, strictly increasing, each after `first_data_date`, up to `as_of`, and none in `date`; `[]` when there are none; ABSENT on a series from a source that makes no such statement (then the page says nothing about unreported days and never guesses). `income` is a per-day array of number OR null: a null is never read as zero, filled or summed.

**What the page does today.** `dashboard/seriesContract.ts` has `SERIES_OPTIONAL = ['class_value', 'class_weight', 'class_names']`, `SeriesDocument.income` typed `readonly number[]`, and no unreported-days member. `dashboard/DashboardPerformance.tsx` `performanceView(series, selection)` builds `notes` in this order: the clipped-window note, the excluded-days note (`N day(s) in this window ... no measurable return`), one note per day-quality state (`N day(s): <sentence>`), then `Returns from <date>.` for a non-FULL history scope. The file's date helper is `dateWords(date)` (prints the ordinal form, for example `July 14th, 2026`) and its count helper is `plural(count, one, many)`. The pin test `__tests__/dsgn-irptv1/iv-e-124.series-contract.test.ts` reads the contract file from disk and fails when the page's key lists differ from it.

**The cell (`DB-c-25`).**
1. **Read first.** `dashboard/seriesContract.ts`, `dashboard/DashboardPerformance.tsx` (the `WindowSelection` type and `performanceView`, including the `window` it returns: `{ start, end }` as `YYYY-MM-DD`), `dashboard/windowMath.ts` only as far as the selection shape needs, `__tests__/dsgn-irptv1/iv-e-124.series-contract.test.ts`, and `__tests__/irpt-dashbd/fwd10-partial-history-and-no-fallback.test.tsx` (the style and how a `SeriesDocument` and a `WindowSelection` are built in a test). Find every use of the series' `income` in the portal by reading file names with `Grep` on `\.income\b` under `dashboard/` and `tabs/` (open a named file at a time). Run once, before any edit, `bun test src/pages/InvestorReporting/__tests__/irpt-dashbd src/pages/InvestorReporting/__tests__/dsgn-irptv1` from the portal worktree and record the failing-test names (base).
2. **The fixtures (make them, do not write them).** From the WORKSPACE worktree root run, with plain `python` (NOT `-I`): `python org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r147/gen_fixture_r147.py . portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/fixtures`. It calls the contract writer (`infra/aws/lambda/investor-reporting/reporting-publish/publisher.py` `build_series`) over made-up rows and writes `series-unreported-days.json` (first data date 2026-07-10, as of 2026-08-14, scope `PARTIAL_HISTORY`, income null on every day, and unreported days 2026-07-14, 2026-07-15 and 2026-08-05), `series-no-statement.json` (the same rows, the pair absent) and `series-unreported-empty.json` (the pair present, the list `[]`). Commit them as they come out; never edit them by hand (the checker regenerates them and compares bytes).
3. **The mirror.** In `dashboard/seriesContract.ts`: `SERIES_OPTIONAL` becomes exactly the contract's `series.optional` list, in the contract's order; `SeriesDocument.income` becomes `readonly (number | null)[]`; `SeriesDocument` gains `readonly unreported_trading_days?: readonly string[]` and `readonly unreported_trading_days_basis?: string`. Do not make the pair required; do not change `SERIES_REQUIRED` or `SERIES_ARRAY_KEYS`. If the `income` type change makes `bun run typecheck` fail in a file inside the grant, fix it there with no coercion of null to zero; if it fails in a file outside the grant, stop on that criterion and file a row naming the file and the error. `iv-e-124` is expected to pass after the mirror; if it fails for a reason that comes from this change (a hand-made fixture inside it that lacks something), update ONLY that assertion or fixture and record the edit.
4. **The sentence.** In `performanceView`, right AFTER the excluded-days note and BEFORE the per-state day-quality notes, add one note when `series.unreported_trading_days` is present and holds at least one date `d` with `window.start <= d && d <= window.end` (a plain string comparison of `YYYY-MM-DD`; keep the list's order). With N such dates the note is exactly `<N> trading <day|days> not reported by the source: <D1>.` where `<N>` is the number, the noun is `day` for 1 and `days` otherwise, and the dates are written with `dateWords` and joined `a`, `a and b`, or `a, b and c` (a comma between all but the last two, then ` and `). Examples with the fixture `series-unreported-days.json`: the window 2026-07-10 to 2026-08-14 prints `3 trading days not reported by the source: July 14th, 2026, July 15th, 2026 and August 5th, 2026.`; 2026-07-10 to 2026-07-31 prints `2 trading days not reported by the source: July 14th, 2026 and July 15th, 2026.`; 2026-08-03 to 2026-08-14 prints `1 trading day not reported by the source: August 5th, 2026.`; 2026-07-20 to 2026-07-31 prints no such note. An absent field or `[]` prints no such note. The portal NEVER computes an unreported day: it names no calendar, builds no date range and counts only the dates in the served list. Do not print the `unreported_trading_days_basis` text. Do not change any other note, the order of the other notes, or `coverageWords.ts`.
5. **The test file** (NEW; `bun:test`; no network; no server): `__tests__/irpt-dashbd/fwd10-unreported-days.test.tsx`, at least 6 tests, reading the three fixtures from `__tests__/irpt-dashbd/fixtures/` with `readFileSync` and `JSON.parse`, whose titles contain between them the words `unreported` (the whole-history window prints exactly the three-day sentence above), `window` (the 2026-07-10 to 2026-07-31 window prints exactly the two-day sentence, the 2026-08-03 to 2026-08-14 window the one-day sentence, and the 2026-07-20 to 2026-07-31 window prints no `not reported by the source` note), `absent` (the `series-no-statement.json` series prints no such note in any of those windows), `empty` (the `series-unreported-empty.json` series prints no such note), `income` (`readSeries` accepts the fixture with an all-null `income`, the array is returned as null on every day and never as 0, and `performanceView` does not throw on it) and `fixture` (the first fixture carries both members of the pair, the basis equals `trading calendar minus present partitions`, the list is strictly increasing and none of its dates is in `date`). The exact sentences above must appear in the file as string literals.
6. **Gates, once, after your last portal commit:** from the portal worktree `bun run typecheck` and `bun run lint` (0 errors each; prove the typecheck can fail first with one deliberate error you revert) and `bun test src/pages/InvestorReporting`: the failing-test names after must be a subset of the names before.
7. **The mutant, once:** put `DashboardPerformance.tsx` back to the base version (`git -C portal show 03f92d82c23fc270e1115c15989e7637f430e16d:src/pages/InvestorReporting/dashboard/DashboardPerformance.tsx`), run your new test file, show at least 2 of your tests fail, then restore with `git checkout --` on the committed file. The final head holds your edits.
8. **Record** `BUILD_R147.json` in your folder with exactly: `portal` {`branch` "wk-IRPT_DASHBD-417-portal", `base` "03f92d82c23fc270e1115c15989e7637f430e16d", `head`, `files_changed` (a list of paths)}, `sentences` {`three_days`, `two_days`, `one_day`} (the exact printed notes), `existing_tests_edited` (a list of paths, empty when none), `tests` {`new_pass`, `suite_before_fail`, `suite_after_fail`}, `mutant_failed_tests`, `typecheck_rc`, `lint_errors`, `pushed` false, `deployed` false.

<criterion id="DBC147-1-AC1" cell_refs="DB-c-25"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r147/p147_bcw.py" . DBC147-1-AC1</invocation><expect>DBC147-1-AC1 PASS</expect></criterion>
`DBC147-1-AC1` -- `__tests__/irpt-dashbd/fwd10-unreported-days.test.tsx` exists, its titles carry the words `unreported`, `window`, `absent`, `empty`, `income` and `fixture`, it carries the three exact sentences as literals, and `bun test` on it passes with 0 failures and at least 6 tests. Base: FAIL (no file).

<criterion id="DBC147-1-AC2" cell_refs="DB-c-25"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r147/p147_bcw.py" . DBC147-1-AC2</invocation><expect>DBC147-1-AC2 PASS</expect></criterion>
`DBC147-1-AC2` -- the three fixtures equal the contract writer's FRESH output byte for byte (the checker runs the generator into a temporary folder and compares); `SERIES_OPTIONAL` in `dashboard/seriesContract.ts` equals the contract's `series.optional` in order; `income` is typed `readonly (number | null)[]`; and `bun test` on `iv-e-124.series-contract.test.ts` passes. Base: FAIL (no fixtures, three-name list).

<criterion id="DBC147-1-AC3" cell_refs="DB-c-25"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r147/p147_bcw.py" . DBC147-1-AC3</invocation><expect>DBC147-1-AC3 PASS</expect></criterion>
`DBC147-1-AC3` -- the difference control and the bounds: with `DashboardPerformance.tsx` temporarily put back to its base version by the checker, the new test file FAILS (at least 2 tests), and after the checker restores it the file is byte-identical to the worker's head; `DashboardPerformance.tsx` names no calendar; the portal diff from the base to the head touches only the files in the grant. Base: FAIL (no change; the control also refuses to run on a main checkout).

<expected_criteria>DBC147-1-AC1, DBC147-1-AC2, DBC147-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every other source file, the contract JSON files, the Python and Lambda code (including `publisher.py` and the generator), `coverageWords.ts`, the checkers.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A generator that fails, or a fixture that does not print the stated sentence, is a finding (a row) and a stop on that criterion, never a hand-made fixture or a different sentence.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W417-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh` (never `--no-verify`); run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~417/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-25.the-performance-tab-prints-the-trading-days-the-source-did-not-report-from-the-series-field-against-writer-made-fixtures.md
portal/src/pages/InvestorReporting/dashboard/DashboardPerformance.tsx
portal/src/pages/InvestorReporting/dashboard/seriesContract.ts
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 16, cell `DB-c-25`.
<owned_cells>DB-c-25</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC147-1-AC1, DBC147-1-AC2, DBC147-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~417/IRPT_DASHBD.TO-DB-c-25.the-performance-tab-prints-the-trading-days-the-source-did-not-report-from-the-series-field-against-writer-made-fixtures.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC147-1-AC1,DBC147-1-AC2,DBC147-1-AC3` BEFORE the flip (one comma-separated argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the portal head sha; the three exact printed sentences; the mutant's failing-test count; the test counts and the typecheck and lint results; any existing test you edited; anything off-task (as row ids). Made-up values only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a portal source edit, fixtures and a test on a worker branch; nothing is pushed, deployed, planned or written to any service.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call and no grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched; the change lands on a worker branch only and reaches DEV by the portal merge-forward law, not by this order.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is read or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBC147-1-AC3 plants its own difference control (the base file put back) and DBC147-1-AC2 regenerates the fixtures from the contract's writer.
</preflight>

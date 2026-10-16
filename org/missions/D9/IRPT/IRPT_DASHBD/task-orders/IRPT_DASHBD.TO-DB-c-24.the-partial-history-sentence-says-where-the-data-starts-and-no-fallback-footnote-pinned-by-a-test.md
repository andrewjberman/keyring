# TO IRPT_DASHBD.TO-DB-c-24 -- FWD-10 on the Performance tab, round 146: the partial-history sentence reads "Returns from <first data date>." with no cause, and no fallback footnote or sentence exists anywhere on the tab; portal source edit plus a new bun test; no deploy, no push

<to_id>IRPT_DASHBD.TO-DB-c-24</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~416</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>146</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's B-CW instruction (msg 8788) on PRD ADDENDUM v0.15 and v0.16 (`org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md`; admitted, `prd-signoff` ADMITTED, msg 8800): round 146 cells "(b) 'Returns from July 10, 2026' as the partial-history sentence, with no cause stated; (c) remove C-HONESTY's fallback footnote" | **Rows:** IRPT_DASHBD-D2-W416-S<k> | **Decomp cell:** `DB-c-24` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 15) | **outcome_ref:** FWD-10 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-416`); run everything from its root unless a step says the portal. Its nested `portal/` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-416-portal`) cut from the portal `DEV` head `e578b378d332ad1505018be3801466dac7aeeade`. Do not amend or revert anything already committed there. Portal files commit in the portal repo with plain git and your author line (`0.9.0_WK_IRPT_DASHBD~416 <0.9.0_WK_IRPT_DASHBD~416@opal.agent>`); your folder, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh` (never `--no-verify`). Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~416/`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours. Made-up ids and figures only; no AWS call, no network, no client data. All portal paths below are under `portal/src/pages/InvestorReporting/`.

**Why (the outcome).** PRD FWD-10: "A person can always tell what they are looking at: where the data starts, which trading days the source did not report, and how current the data is." A partial-history account (one whose history starts after the series does) must be told, in one sentence where the number is, where its data starts, and the sentence states no cause because the cause of the start is not established (v0.15 item (c)). A fallback day no longer exists (ruling 17 withdrew the substitution), so no fallback footnote or sentence may appear.

**What the page does today (measured by round 145, `COTTONWOOD_SCREEN_COVERAGE_READ_R145.json`):** `dashboard/DashboardPerformance.tsx` `performanceView(series, selection)` ends its notes with `if (series.history_scope !== 'FULL') notes.push(coverageSentence('history_scope', series.history_scope))` (about line 147), and `dashboard/coverageWords.ts` maps `PARTIAL_HISTORY` to "This history covers only part of the account's life; earlier days are not included yet." The date helper in that file is `dateWords(date)` (about line 81: `formatPageDate(date) ?? date`). The pin test `__tests__/dsgn-irptv1/iv-e-120.coverage-words.test.ts` binds the member set of `COVERAGE_WORDS` to the gold contract (parity), so the `PARTIAL_HISTORY` member STAYS in the map.

**The cell (`DB-c-24`).**
1. **Read first.** `dashboard/DashboardPerformance.tsx`, `dashboard/coverageWords.ts`, `dashboard/seriesContract.ts` (the `SeriesDocument` shape: `date`, `total_return_daily`, `day_quality`, `first_data_date`, `history_scope`, `as_of`), the existing tests that touch the dashboard (find them by reading the file names in `__tests__/irpt-dashbd/` and `__tests__/dsgn-irptv1/` that import `DashboardPerformance` or `coverageWords`; open a named file at a time), and `__tests__/dsgn-irptv1/iv-e-120.coverage-words.test.ts` (the style: `bun:test`). Run once, before any edit, `bun test src/pages/InvestorReporting/__tests__/irpt-dashbd src/pages/InvestorReporting/__tests__/dsgn-irptv1` from the portal worktree and record the failing-test names (base).
2. **(b) The partial-history sentence.** In `performanceView`, when `series.history_scope !== 'FULL'`, the note is exactly `Returns from <date>.` where `<date>` is `series.first_data_date` written as month name, day and year (for `2026-07-10` the sentence is exactly `Returns from July 10, 2026.`; if `dateWords` prints another form, write the date with a month-name table in that file so the sentence is exactly this form). It states NO cause: it carries none of the words `because`, `since`, `empty`, `silver`, `source`, `custodian`, `Black Diamond`, `missing`, `gap` or `earlier days`. The note replaces the `coverageSentence('history_scope', ...)` note for a non-FULL scope in this one place; the `PARTIAL_HISTORY` entry of `COVERAGE_WORDS` and the parity test stay unchanged. A `FULL` scope still prints no partial-history note. Do not touch any other note of `performanceView` (the clipped-window note, the not-measured sentence, the excluded-days note, the per-state day-quality counts).
3. **(c) No fallback footnote.** Make it a pinned fact: the portal prints no fallback footnote or sentence. If your read finds any user-visible string in `dashboard/` (or the Performance tab's own files under `tabs/reporting/`) that speaks of a fallback day or a price-plus-income substitution, remove that string (and record it in your report); the round-145 read found none, so the expected outcome is "none found" and a test that pins it.
4. **The test file** (NEW; `bun:test`; no network; no server): `__tests__/irpt-dashbd/fwd10-partial-history-and-no-fallback.test.tsx`, at least 6 tests whose titles contain between them the words `partial history` (the note for a `PARTIAL_HISTORY` series with `first_data_date` `2026-07-10` is exactly `Returns from July 10, 2026.`, asserted on `performanceView(...).notes`), `first data date` (a second made-up date, `2026-03-02`, gives `Returns from March 2, 2026.`), `cause` (the note matches none of the cause words listed in step 2), `FULL` (a `FULL` series has no `Returns from` note), `fallback` (no value of any `COVERAGE_WORDS` axis and no note of `performanceView` across the matrix of every `history_scope` member, every `day_quality` member and a window clipped and not clipped, matches `/fallback|substitut/i`) and `window` (the clipped-window note and the not-measured sentence are unchanged: pin their current text). Build the `SeriesDocument` literals from made-up values with the exact keys `seriesContract.ts` requires.
5. **Existing tests.** A test that pinned the OLD partial-history note text may fail after (b): update ONLY that assertion to the new sentence (and record each such edit); change no other existing test, and the parity test `iv-e-120` must still pass.
6. **Gates, once, after your last portal commit:** from the portal worktree `bun run typecheck` and `bun run lint` (0 errors each; prove the typecheck can fail first with one deliberate error you revert) and `bun test src/pages/InvestorReporting`: the failing-test names after must be a subset of the names before.
7. **The mutant, once:** revert `DashboardPerformance.tsx` to its base version (`git show e578b378d332:portal/...` is not available inside the portal repo: use `git -C portal show e578b378d332:src/pages/InvestorReporting/dashboard/DashboardPerformance.tsx`), run your new test file, show at least 2 of your tests fail, then restore with `git checkout --` on the committed file. The final head holds your edits.
8. **Record** `BUILD_R146.json` in your folder with exactly: `portal` {`branch` "wk-IRPT_DASHBD-416-portal", `base` "e578b378d332ad1505018be3801466dac7aeeade", `head`, `files_changed` (a list of paths)}, `partial_history_sentence_for_2026_07_10` (the exact printed note), `cause_words_found` (0), `fallback_strings_removed` (a count, 0 when none), `existing_tests_edited` (a list of paths, empty when none), `tests` {`new_pass`, `suite_before_fail`, `suite_after_fail`}, `mutant_failed_tests`, `typecheck_rc`, `lint_errors`, `pushed` false, `deployed` false.

<criterion id="DBC146-1-AC1" cell_refs="DB-c-24"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r146/p146_bcw.py" . DBC146-1-AC1</invocation><expect>DBC146-1-AC1 PASS</expect></criterion>
`DBC146-1-AC1` -- `__tests__/irpt-dashbd/fwd10-partial-history-and-no-fallback.test.tsx` exists, its titles carry the words `partial history`, `first data date`, `cause`, `FULL`, `fallback` and `window`, and `bun test` on it passes with 0 failures and at least 6 tests; the record's printed sentence for 2026-07-10 is exactly `Returns from July 10, 2026.`. Base: FAIL (no file).

<criterion id="DBC146-1-AC2" cell_refs="DB-c-24"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r146/p146_bcw.py" . DBC146-1-AC2</invocation><expect>DBC146-1-AC2 PASS</expect></criterion>
`DBC146-1-AC2` -- the difference control and the bounds: with `DashboardPerformance.tsx` temporarily put back to its base version by the checker, the new test file FAILS (at least 2 tests), and after the checker restores it the file is byte-identical to the worker's head; the portal diff from the base to the head touches only the files in the grant; the record carries zero cause words, `pushed` false and `deployed` false. Base: FAIL (no change).

<expected_criteria>DBC146-1-AC1, DBC146-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every other source file, `seriesContract.ts`, the contract JSON files, the Python and Lambda code, the checkers.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A `dateWords` output you cannot make read exactly `July 10, 2026` is a finding, never a different sentence.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W416-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh` (never `--no-verify`); run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~416/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-24.the-partial-history-sentence-says-where-the-data-starts-and-no-fallback-footnote-pinned-by-a-test.md
portal/src/pages/InvestorReporting/dashboard/DashboardPerformance.tsx
portal/src/pages/InvestorReporting/dashboard/coverageWords.ts
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 15, cell `DB-c-24`.
<owned_cells>DB-c-24</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC146-1-AC1, DBC146-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~416/IRPT_DASHBD.TO-DB-c-24.the-partial-history-sentence-says-where-the-data-starts-and-no-fallback-footnote-pinned-by-a-test.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC146-1-AC1,DBC146-1-AC2` BEFORE the flip (one comma-separated argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the portal head sha; the exact printed sentence for 2026-07-10; the number of fallback strings removed; the mutant's failing-test count; the test counts and the typecheck and lint results; any existing test you edited; anything off-task (as row ids). Made-up values only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a portal source edit and a test on a worker branch; nothing is pushed, deployed, planned or written to any service.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call and no grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched; the change lands on a worker branch only and reaches DEV by the portal merge-forward law, not by this order.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is read or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBC146-1-AC2 plants its own difference control (the base file put back).
</preflight>

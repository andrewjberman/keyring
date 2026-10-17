# TO IRPT_DASHBD.TO-DB-b-330 -- the Performance chart draws every measured segment of a window, with a visible break at each day that has no return and at each trading day the source did not report (CTO msg 10331 (a), after Andrew's own look at the Cottonwood tab on 5174): a new portal candidate branch from the pinned DEV head (CLIENT-FACING, portal repo) (round 150)

<to_id>IRPT_DASHBD.TO-DB-b-330</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~258</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>150</round>
<workstream>CHARTGAP</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** CHARTGAP, round 150 | **Ordered by:** the CTO's report of Andrew's check (msg 10331 (a)): "The chart is BLANK from Jul 15 to Oct 15. It must draw the measured segments, with visible breaks at the missing days." The page owner `2.0.0_SA_COO~C2` has no live session, so this seat cuts it. | **Decomp cell:** `DB-b-330` (decomposition section 190).

**Risk class SERVED, client-facing:** a page cell in the portal repo. It reaches DEV only through `.tools/portal-merge-forward.sh` on an approved row, and PROD only by a chosen-set promote; this order pushes a candidate branch under its own name and nothing else.

**The cause, measured by the issuer:** `DashboardPerformance.tsx` builds the chart's drawn values only `view.status === 'MEASURED'`. A window that holds one day with no return is `BREAK`, so every row of the chart has no value and the chart is blank, while the series holds many measured days. The trading days the source did not report are not in the served day list at all, so no row exists where the line should break.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-258` (branch `wk-IRPT_DASHBD-258`) and its portal worktree `C:/dev/wk-irpt-dashbd-258/portal`. **First act:** in the portal worktree run `git fetch origin` then `git checkout -b cand/dell2/irpt-performance-chart-breaks 38d4f9473284a585bc217981213b9516e29d3a87` (the pinned DEV head; your branch descends from it). You add ONE commit and push ONLY that branch name (`git push origin cand/dell2/irpt-performance-chart-breaks`). Never push the workspace; never commit the workspace `portal` gitlink. Every portal commit carries the explicit identity: `git -C <portal> -c user.name="0.9.0_WK_IRPT_DASHBD~258" -c user.email="0.9.0_WK_IRPT_DASHBD~258@opal.agent" commit ...`. The portal file is CRLF: keep its line endings (edit with a script that reads and writes bytes); the new test file may be LF. Counts, dates, hashes and words only in the workspace repo; the tests are synthetic. Tool calls that carry a backslash-r or backslash-n escape inside a shell heredoc can be altered in transit: write patch scripts to a file with the Write tool and run them. Resolve `bun` from the PATH (or `~/.bun/bin`). A `node_modules` junction to the main portal's is acceptable if the worktree has none.

**The cell (`DB-b-330`).** One source file, `src/pages/InvestorReporting/dashboard/DashboardPerformance.tsx`, and one new test file.
1. **Read first, whole:** that file; `dashboard/windowMath.ts` (`cumulativePath`: one point per served day of the window, `cumulative: null` on a day with no return); `dashboard/seriesContract.ts` (`unreported_trading_days`, optional, strictly increasing ISO dates); the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p196_chart_breaks.py` (your three criteria and its probe); the existing fixtures `src/pages/InvestorReporting/__tests__/irpt-dashbd/fixtures/series-unreported-days.json`, `series-no-statement.json`, `series-unreported-empty.json`.
2. **Export `chartRows(series: SeriesDocument, view: PerformanceView): ChartRow[]`** from `DashboardPerformance.tsx`, and `export interface ChartRow { readonly date: string; readonly cumulative: number | null; readonly quality: string; readonly gap: boolean; readonly isolated: boolean }`. The rows are, in strictly increasing date order: one row per served day (`gap` false; `cumulative` is that day's value in `view.path`, or null when the day is outside the window or has no return; `quality` is the served `day_quality`), plus one row per date in `series.unreported_trading_days` that is NOT a served day and lies strictly between the first and the last served day (`gap` true, `cumulative` null, `quality` the empty string). No status gate: a `BREAK` window draws its measured days exactly as a `MEASURED` one does; the word `MEASURED` does not appear inside `chartRows`. `isolated` is true exactly when the row's `cumulative` is not null and the row before it (if any) and the row after it (if any) both have a null `cumulative`.
3. **The component draws from `chartRows`:** replace the `view.status === 'MEASURED'` map and the `rows` built from `series.date`; compute the brush `startIndex`/`endIndex` as the index in the rows of `result.answered.start`/`end`; in the brush `onChange` map each index back to a SERVED day (the start takes the first non-gap row at or after the index, the end the last non-gap row at or before it) and never read `series.date[range.startIndex]`. Keep exactly one `<Area>` with `connectNulls={false}`. Draw an `isolated` row as a dot (`dot={<IsolatedDot />}`, a small component returning a `circle` or null). Add, above the chart and only when the window's answered span holds a row with no value, one paragraph `<p data-slot="dashboard-chart-breaks">` reading `The curve breaks at N day(s) with no return.` (singular `day` for 1). The tooltip names a `gap` row's day: `The source did not report this trading day.` The headline figure, the notes, the window status and `performanceView` do not change.
4. **Files you may change:** `dashboard/DashboardPerformance.tsx` (at most 120 changed lines) and ONE new test file `src/pages/InvestorReporting/__tests__/irpt-dashbd/dashboard-chart-breaks.test.ts` (its name starts exactly so). **Not** anything else; no fixture is added (derive variants in the test from the three existing fixtures, setting a return to null and its `day_quality` to `NOT_MEASURABLE` in a copy).
5. **Your tests** (bun; made-up values; the words `break`, `unreported` and `isolated` appear in the file): a window with a no-return day is `BREAK` and `chartRows` still has more than five valued rows, null on that day; the valued rows equal `view.path` day for day; unreported days are valueless `gap` rows in date order and the row count is the served count plus the inserted ones; a series with no unreported statement adds no row; a `MEASURED` window has a value on every served day of it; days before the window have no value; a measured day between two breaks is `isolated` and one beside a measured day is not. The suite's failing names, if any, are a subset of the base's.
6. **Run the checks yourself** (criteria below; AC3 runs both test directories, the typecheck and the production build, 10 to 20 minutes). Commit on the portal branch (explicit identity), push ONLY `cand/dell2/irpt-performance-chart-breaks`, and keep the pushed head (ls-remote read).
7. **Record** `RD_CHART_BREAKS_FACTS_R150.json` in your folder (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~258/`) with EXACTLY these fields: `portal_branch`; `portal_head` (40 hex pushed); `base_head` ("38d4f9473284a585bc217981213b9516e29d3a87"); `files_changed` (sorted portal paths); `tests_added` (the new test file name); `words` (one paragraph, 80 to 1800 characters: what changed and why, and what is NOT proven: no browser walk, no live render of the Cottonwood page, nothing on DEV or PROD).

<criterion id="DBP196-1-AC1" cell_refs="DB-b-330"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p196_chart_breaks.py" C:/dev/wk-irpt-dashbd-258 DBP196-1-AC1</invocation><expect>DBP196-1-AC1 PASS</expect></criterion>
`DBP196-1-AC1` -- the branch is `cand/dell2/irpt-performance-chart-breaks` and descends from the pinned DEV head; only `DashboardPerformance.tsx` (at most 120 changed lines) and the one new test file changed, all committed; `chartRows` is exported, reads the served unreported list, sorts, draws `view.path` with no `MEASURED` gate, the area keeps `connectNulls={false}`, the brush is mapped through the rows, an isolated day is drawn, the break note is present. Base: FAIL.
<criterion id="DBP196-1-AC2" cell_refs="DB-b-330"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p196_chart_breaks.py" C:/dev/wk-irpt-dashbd-258 DBP196-1-AC2</invocation><expect>DBP196-1-AC2 PASS</expect></criterion>
`DBP196-1-AC2` -- the cell's test file speaks of break, unreported and isolated and passes under bun, and the issuer's probe (written into the test directory by the checker and deleted after) passes against your `chartRows`. Base: FAIL.
<criterion id="DBP196-1-AC3" cell_refs="DB-b-330"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p196_chart_breaks.py" C:/dev/wk-irpt-dashbd-258 DBP196-1-AC3</invocation><expect>DBP196-1-AC3 PASS</expect></criterion>
`DBP196-1-AC3` -- every `irpt-dashbd` and `dsgn-irptv1` test passes; the typecheck passes; the production build succeeds and carries neither the `SYNTHETIC PREVIEW` words nor the synthetic fixture. Base: FAIL (the cell's test file is missing).

<expected_criteria>DBP196-1-AC1,DBP196-1-AC2,DBP196-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and in the portal repo the write set of step 4. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files. Writes: the portal candidate branch (pushed to origin under its own name only), the workspace folder and files named below. No AWS call, no Terraform command, no push of the workspace, no push to DEV or PROD.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W258-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit workspace files with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~258/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-330.performance-chart-draws-measured-segments-with-breaks.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 190 (round 150, workstream CHARTGAP), cell `DB-b-330`.
<owned_cells>DB-b-330</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBP196-1-AC1, DBP196-1-AC2, DBP196-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~258/IRPT_DASHBD.TO-DB-b-330.performance-chart-draws-measured-segments-with-breaks.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBP196-1-AC1,DBP196-1-AC2,DBP196-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the pushed head (ls-remote read); the change in one line; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a portal candidate branch; no plan, no apply, nothing deployed; nothing is pushed to DEV or PROD.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: nothing is applied in this cell; no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CDN or edge cache is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the criteria FAIL at base, AC1 and AC2 PASS on the issuer's reference edit in a scratch portal worktree and 15 single-fault mutants of it are each refused (AC3 is the same proof as p175 AC3, run by the worker).
lane: the <paths> block and the page owner's agreed portal write set ARE the grant.
</preflight>

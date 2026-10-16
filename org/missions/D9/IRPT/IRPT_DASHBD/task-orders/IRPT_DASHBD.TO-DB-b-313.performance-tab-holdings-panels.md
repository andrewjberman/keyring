# TO IRPT_DASHBD.TO-DB-b-313 -- the Performance tab's HOLDINGS PANELS: the allocation by asset class and the LARGEST POSITIONS (never "movers"), worded states, ONE new component and ONE mount, stacked on the DB-b-309 branch (CLIENT-FACING, portal repo) (round 149)

<to_id>IRPT_DASHBD.TO-DB-b-313</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~249</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>PORTALPANELS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** PORTALPANELS, round 149 | **Ordered by:** the CTO's ruling msg 9866 (build the allocation and the positions panels now; Sector is a data cell; Allocation-over-time and Attribution stay worded-absent) and the page owner's write set `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/R152_ALLOCATION_AND_MOVERS_PANELS_WRITE_SET.md` (@7e39422526; its two corrections: no donut exists to reuse, and the snapshot carries no change field, so the panel is "Largest positions") | **Decomp cell:** `DB-b-313` (decomposition section 173).

**Risk class SERVED, client-facing:** a page cell in the portal repo on a feature branch; nothing is pushed to DEV or PROD, and Andrew's approval is the gate for any merge.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-249` (branch `wk-IRPT_DASHBD-249`) and its portal worktree `C:/dev/wk-irpt-dashbd-249/portal`, which the provisioner cut from DEV. **First act:** in the portal worktree run `git fetch origin` then `git checkout -B cand/dell2/irpt-performance-holdings-panels origin/cand/dell2/irpt-49f-performance-template-mount` (the head is `75a71ae39089baf9fdddcc34cd3075dea4b31701`); your new branch name is exactly that. Never push the workspace; never commit the workspace `portal` gitlink. Every portal commit carries the explicit identity: `git -C <portal> -c user.name="0.9.0_WK_IRPT_DASHBD~249" -c user.email="0.9.0_WK_IRPT_DASHBD~249@opal.agent" commit ...`. Portal files in this branch use CRLF line endings: keep them (edit with a script that reads and writes bytes, or an editor that preserves CRLF); a one-line mount must not turn into a whole-file diff. Counts, dates, hashes and words only in the workspace repo; the tests are synthetic. Tool calls that carry a backslash-r or backslash-n escape inside a shell heredoc can be altered in transit: write patch scripts to a file with the Write tool and run them. Resolve `bun` from the PATH.

**The cell (`DB-b-313`).**
1. **Read first, whole:** the page owner's file named above (its section (1) is your exact mount and component spec, its section (3) your tests); the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p180_portal_holdings_panels.py` (your three criteria; its probe test is the exact spec of the component's props, headings and sentences).
2. **ONE new file `tabs/reporting/PerformanceHoldingsPanels.tsx`** exporting `PerformanceHoldingsPanels({ snapshot, failed })` (`snapshot: HoldingsSnapshot | null`, `failed: boolean`). It renders: (a) with `snapshot` null and `failed` false the sentence `Loading this client's holdings.`; with `snapshot` null and `failed` true `This client's holdings could not be loaded.` (never an empty node); (b) with a snapshot, the allocation by asset class: `classTotalsView(snapshot)` drawn by the EXISTING exported `ClassTotals` component of `tabs/holdings/SecurityList.tsx` (its own heading and basis sentence), or, when the view is null, the heading `NO_CLASS_LINES_HEADING` with the sentence `WHOLE_REMAINDER_SENTENCE` from `tabs/holdings/classTotals.ts`; (c) a section titled exactly `Largest positions`: `foldSecurityRows(securityRowsFrom(snapshot))` sorted by `amount` descending (a null amount last), the first 10, columns Ticker, Name, Weight (`formatWeight`), Value (`formatValue`); do NOT mount the whole `SecurityList`; (d) two plain lines, always shown: `Allocation over time is not published for this client yet.` and `Attribution is not published for this client yet.` The word "mover" appears nowhere in the file (the snapshot has no change field). No donut is built in this cell. The component fetches nothing: the snapshot is the identity card's own, passed by the tab.
3. **ONE mount in `tabs/reporting/ReportingTab.tsx`** (an import and one JSX line, at most 12 changed lines in all): `<PerformanceHoldingsPanels snapshot={header?.snapshot ?? null} failed={header?.snapshotFailed ?? false} />` placed immediately before the DB-b-307 comment that precedes `<PerformanceTemplateView`, so it shows under every body branch (dashboard served, PATH A report, refusal) and is NOT inside the `dashboardServed` branch.
4. **Tests: ONE new file `__tests__/irpt-dashbd/performance-holdings-panels.test.tsx`** (use `renderToStaticMarkup`; the apostrophe renders as `&#x27;`, so compare text after decoding it) with the page owner's five tests: (1) with a seeded `headerSelection.snapshot` the tab markup contains both panel headings under each body branch, with `snapshot` null and `snapshotFailed` true the failure sentence, never an empty panel node, and a difference control (the base head renders neither heading); (2) the rendered allocation shares equal `classTotalsView(snapshot)` lines through `formatWeight`, and a snapshot with no classified securities prints the worded remainder state; (3) Largest positions are the top 10 by `amount` descending after the fold, nulls last, a cash identity folds to one row, the markup contains no "mover" (positive control: the title reads "Largest positions"); (4) at Global (`scope` null, `headerSelection.selectedTenant` set) the panels read the snapshot published in `headerSelection.snapshot` and the tab makes no second `getHoldingsSnapshot` call; (5) static markup renders with no effect needed. Existing tests keep passing; the suite's failing names, if any, are a subset of the base's.
5. **Files you may change:** `tabs/reporting/ReportingTab.tsx`, `tabs/reporting/PerformanceHoldingsPanels.tsx` (new), `__tests__/irpt-dashbd/performance-holdings-panels.test.tsx` (new). **Not** `tabs/holdings/*` (imported, never edited), `contracts/index.ts`, `index.tsx`, `header/*`, `dashboard/*`, `export/*`.
6. **Run the checks yourself from the workspace root** (the checker reads the portal repo at `<root>/portal`): `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p180_portal_holdings_panels.py" . DBP180-1-AC1`, then AC2, then AC3 (AC3 runs the test directory, the typecheck and the production build, 10 to 20 minutes). Commit on the portal branch (explicit identity), push ONLY `cand/dell2/irpt-performance-holdings-panels` when all three pass, and tell the issuer the pushed head.
7. **Record** `RD_PORTAL_PANELS_FACTS_R149.json` in your folder (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~249/`) with EXACTLY these fields: `portal_branch`; `portal_head` (40 hex pushed); `base_head` ("75a71ae39089baf9fdddcc34cd3075dea4b31701"); `files_changed` (sorted portal paths); `panels` (one sentence: what the two panels draw and from what); `states` (one sentence: the worded states); `mount` (one sentence: where and what is passed); `tests_added` (the new test file name); `words` (one paragraph, 80 to 1800 characters: what changed and why, and what is NOT proven: no browser walk at Global, no DEV or PROD change, what a real Cottonwood or Inflection snapshot holds was not read here, no donut).

<criterion id="DBP180-1-AC1" cell_refs="DB-b-313"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p180_portal_holdings_panels.py" . DBP180-1-AC1</invocation><expect>DBP180-1-AC1 PASS</expect></criterion>
`DBP180-1-AC1` -- the branch is `cand/dell2/irpt-performance-holdings-panels` and descends from `75a71ae3`; only the agreed write set changed; `ReportingTab.tsx` changes by the one mount and import (at most 12 lines) passing `header?.snapshot`; the component carries the required sentences, reuses `classTotalsView`, `ClassTotals`, `securityRowsFrom`, `foldSecurityRows`, fetches nothing and never says "mover". Base: FAIL.
<criterion id="DBP180-1-AC2" cell_refs="DB-b-313"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p180_portal_holdings_panels.py" . DBP180-1-AC2</invocation><expect>DBP180-1-AC2 PASS</expect></criterion>
`DBP180-1-AC2` -- a probe test: the panels print the loading sentence and the failure sentence, the allocation heading and `Largest positions` for a served snapshot, and the two absent lines. Base: FAIL.
<criterion id="DBP180-1-AC3" cell_refs="DB-b-313"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p180_portal_holdings_panels.py" . DBP180-1-AC3</invocation><expect>DBP180-1-AC3 PASS</expect></criterion>
`DBP180-1-AC3` -- the cell's test file exists; every test under `__tests__/irpt-dashbd/` passes; the typecheck passes; the production build succeeds and its output carries neither the `SYNTHETIC PREVIEW` words nor the synthetic fixture. Base: FAIL.

<expected_criteria>DBP180-1-AC1,DBP180-1-AC2,DBP180-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and in the portal repo the write set of step 5. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files. Writes: the portal feature branch (and pushing it to origin under its own name only), the workspace folder and files named below. No AWS call, no Terraform command, no push of the workspace, no push to DEV or PROD.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W249-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit workspace files with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~249/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-313.performance-tab-holdings-panels.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 173 (round 149, workstream PORTALPANELS), cell `DB-b-313`.
<owned_cells>DB-b-313</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBP180-1-AC1, DBP180-1-AC2, DBP180-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~249/IRPT_DASHBD.TO-DB-b-313.performance-tab-holdings-panels.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBP180-1-AC1,DBP180-1-AC2,DBP180-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the pushed head (ls-remote read); what the panels draw in one line; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a portal feature branch; no plan, no apply, nothing deployed; nothing is pushed to DEV or PROD.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: nothing is applied in this cell; no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; the panels read the snapshot the identity card already fetched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CDN or edge cache is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the issuer ran them on a reference component and mount in a scratch portal worktree.
lane: the <paths> block and the page owner's agreed portal write set ARE the grant.
</preflight>

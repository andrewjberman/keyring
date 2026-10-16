# TO IRPT_DASHBD.TO-DB-b-307 -- MOUNT the Performance template view and its PDF export (Andrew's smoke, CTO msg 9662): cherry-pick the render candidate onto current DEV, mount `PerformanceReport` in the Performance tab and `PerformanceReportDocument` behind the export button; the served `filled_report.json` comes from the route, and ONLY under the Vite dev server a synthetic fixture with a visible SYNTHETIC PREVIEW banner stands in (round 149; PORTAL, CLIENT-FACING)

<to_id>IRPT_DASHBD.TO-DB-b-307</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~246</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>PORTALMOUNT</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** PORTALMOUNT, round 149 | **Ordered by:** the CTO's msg 9662 (Andrew wants to smoke the template view in the Performance tab and its PDF export on `localhost:5174`; the render candidate `cand/dell2/irpt-49f-report-render-disclosure-placeholder` @`42a1539b` builds `PerformanceReport`, `PerformanceReportDocument` and the synthetic fixture but mounts neither) and `~C2`'s answer on the page paths (msg of 17:01Z: the agreed write set below; `~C2` cuts nothing on these files until this cell drains) | **Decomp cell:** `DB-b-307` (decomposition section 167).

**Risk class SERVED, CLIENT-FACING:** a page a partner-firm or client login can open. The cell builds a portal feature branch and pushes NOTHING to DEV or PROD; reaching DEV is the approval row's act (Andrew), through `.tools/portal-merge-forward.sh`.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-246` (branch `wk-IRPT_DASHBD-246`); its portal worktree is `C:/dev/wk-irpt-dashbd-246/portal` (a worktree of the portal repo). Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~246/`. Never push the workspace; never commit the workspace `portal` gitlink. **Everything portal is committed in the PORTAL repo, on the branch `cand/dell2/irpt-49f-performance-template-mount`:** `git -C portal checkout -B cand/dell2/irpt-49f-performance-template-mount origin/DEV` (current DEV; fetch first). Counts, dates, hashes and words only in the workspace repo; the fixture is synthetic by construction. Tool calls that carry a backslash-r or backslash-n escape inside a shell heredoc can be altered in transit: write patch scripts to a file with the Write tool and run them. Resolve `bun` from the PATH; do not bake a path.

**AMENDMENT 1 (2026-10-16 ~18:2xZ, issuer; on the worker's rows W246-S1 to S5):** (a) the checker's relative-root defect (W246-S1) is the issuer's and is fixed in `p175` (the root is resolved to an absolute path); run it again as written. (b) W246-S2: the export button's mount is outside the agreed set, so the tab's state reaches the export through ONE new shared module, `src/pages/InvestorReporting/tabs/reporting/templateState.ts` (a new file in the view's own folder, added to the write set; `~C2` is told), exporting `publishTemplateState(state: TemplateState | null): void` and `readTemplateState(): TemplateState | null` over a single module-level variable. `PerformanceTemplateView` publishes its current state there (and publishes `null` on unmount); `Preview.tsx` or `PrintEntry.tsx` reads it with `readTemplateState()` to produce `PerformanceReportDocument` from the SAME state as the tab (served report, else the DEV fixture, never in a built tier). No caller edit (`index.tsx` stays untouched). The checker's probe now covers this module and requires the export files to reference `templateState`. (c) W246-S3: add `?selected_tenant=<registry tenant>` to the served read exactly as the sibling reads in `dashboard/reportingRead.ts` do when the tenant is known (reuse their tenant source; do not edit that file). (d) W246-S4: read the firm and client ids at `scope.scope.firmId` and `scope.scope.clientId` (ContractEnvelope.scope), as you found. (e) `~C2`'s two conditions on the shared module (msg 9738), pinned by tests in this cell: (1) the tab CLEARS the published state on unmount (an effect cleanup that calls `publishTemplateState(null)`), so the export never reads a stale tab after the user leaves or switches firm; (2) the export reads `null`, not a throw and not the fixture, when no tab has published, and the DEV-only fixture path is not reachable from a production build (the `import.meta.env.DEV` guard; the checker greps the built dist for the banner). The branch is pushed only when all three criteria pass as written; the order stays open until then.

**The cell (`DB-b-307`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p175_portal_template_mount.py` (your three criteria; the probe test inside it is the exact spec of the view's exports); in the portal repo the candidate's files (`git -C portal diff --name-only $(git -C portal merge-base cand/dell2/irpt-49f-report-render-disclosure-placeholder origin/DEV) cand/dell2/irpt-49f-report-render-disclosure-placeholder`: 21 files), the Performance tab `src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx` (it renders `<DashboardPerformance>` near line 911), the export files `export/ExportButton.tsx`, `export/Preview.tsx`, `render/PrintEntry.tsx`, `render/manifest.ts` (the `PerformanceDocument`), and how the page already fetches a scoped investor-reporting route (the existing endpoint helpers under `src/api/`; use the same helper, do not edit it).
2. **Cherry-pick the candidate (ONE base, no other).** On the new branch cut from current DEV, cherry-pick the candidate's commits in order: `git -C portal cherry-pick $(git -C portal merge-base cand/dell2/irpt-49f-report-render-disclosure-placeholder origin/DEV)..cand/dell2/irpt-49f-report-render-disclosure-placeholder` (22 commits, 21 files, all additive). After the pick, the 21 files are byte-identical to the candidate; the checker compares each.
3. **The new view (ONE new file; plus the shared module of AMENDMENT 1)** `src/pages/InvestorReporting/tabs/reporting/PerformanceTemplateView.tsx`, with exactly these exports: `SYNTHETIC_PREVIEW_BANNER = 'SYNTHETIC PREVIEW'`; `type TemplateState = { kind: 'live'; report: FilledReport } | { kind: 'preview'; report: FilledReport } | { kind: 'none' }`; `resolveTemplate(served: FilledReport | null, previewFixture: FilledReport | null): TemplateState` (a served report is `live` whatever the fixture; no served report and a fixture is `preview`; neither is `none`); `PerformanceTemplateBody({ state, firmId })` (live: `<PerformanceReport report firmId>` with NO banner; preview: a visible banner element holding the words `SYNTHETIC PREVIEW` exactly once above the report; none: renders nothing); and `PerformanceTemplateView({ clientId, firmId })`, the component the tab mounts: it fetches the served report once per client from the route `GET /api/scoped/investor-reporting/reporting/client/<client id>/report` through the page's existing scoped-route helper, treats ANY non-success (404, an error, a network failure, a body that is not the `{household, values}` shape) as "nothing served" and never throws, and ONLY when nothing is served and `import.meta.env.DEV` is true loads the fixture with a DYNAMIC `import('../../dashboard/report/fixtures/syntheticReport')` (the `SYNTHETIC_REPORT_ALPHA`; NEVER a static import of the fixture, so a production build drops it). The view reads the client and firm from the same page context the tab already uses (no new global).
4. **The tab mount (EDIT `ReportingTab.tsx`: ONE import and ONE mount, nothing else).** Mount `<PerformanceTemplateView>` in the Performance tab as an additional block below the existing `<DashboardPerformance>`; the existing dashboard stays exactly as it is.
5. **The export (EDIT `export/Preview.tsx`, `render/PrintEntry.tsx`, `render/manifest.ts`; `export/ExportButton.tsx` only if needed).** The Performance export gets `PerformanceReportDocument` (candidate file `render/performance/report/PerformanceReportDocument.tsx`) behind the export button: the manifest registers it, the print entry renders it, the preview shows it. The candidate's own export test (`report-export.test.tsx`) already asserts the document; keep it passing and add a test that the manifest and the print entry reach `PerformanceReportDocument`. In the dev smoke the export button must produce the document from the same state as the tab (served report, else the DEV fixture); a built tier never renders the fixture.
6. **Do NOT touch** `dashboard/DashboardPerformance.tsx`, `dashboard/seriesContract.ts` or `dashboard/coverageWords.ts` (`~C2`'s), and no file outside the agreed set (the 21 candidate files, the new view, the four or five edits above, and test files under `src/pages/InvestorReporting/__tests__/irpt-dashbd/`).
7. **Tests.** Add `__tests__/irpt-dashbd/performance-template-view.test.tsx` (bun:test, `renderToStaticMarkup`, no network): the pure core on the three states, the banner once, the route string, and that the view source has no static fixture import. Every test under `__tests__/irpt-dashbd/` passes.
8. **Run the checks yourself** from the workspace root (the checker reads the portal repo at `<root>/portal`): `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p175_portal_template_mount.py" . DBP175-1-AC1`, then AC2, then AC3 (AC3 runs every irpt-dashbd test, the typecheck and the production build, 10 to 20 minutes). Commit the portal work on the portal branch with the portal repo's own commit route (`git -C portal commit`), one logical commit for the view and mounts and one for the tests; push that portal branch to origin under its name (`git -C portal push origin cand/dell2/irpt-49f-performance-template-mount`); never push DEV or PROD.
9. **Record** `RD_PORTAL_MOUNT_FACTS_R149.json` in your folder with EXACTLY these fields: `portal_branch` (the branch name); `portal_head` (the 40-hex head you pushed); `base_dev` (the 40-hex DEV commit it is cut from); `candidate_commits_picked` (the number); `files_changed` (the sorted portal paths); `route` (the route string); `dev_gate` (one sentence: how the fixture is kept out of a built tier); `export_wiring` (one sentence); `words` (one paragraph, 80 to 1800 characters: what changed and why, and what is NOT proven: nothing is on DEV or PROD, no browser walk was made, the route is built by the IB-pr-551 hops and does not exist yet so the live path is exercised only by the pure core, the fixture is synthetic).

<criterion id="DBP175-1-AC1" cell_refs="DB-b-307"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p175_portal_template_mount.py" . DBP175-1-AC1</invocation><expect>DBP175-1-AC1 PASS</expect></criterion>
`DBP175-1-AC1` -- the portal branch is named `cand/dell2/...`; the 21 candidate files are byte-identical to the candidate; only the agreed write set (the candidate files, the new view, the tab, the export files and test files) changed and none of the three forbidden files; the tab imports and mounts the view once (at most 14 added and 2 removed lines); the manifest references `PerformanceReportDocument` and the preview or the print entry reaches it. Base: FAIL.
<criterion id="DBP175-1-AC2" cell_refs="DB-b-307"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p175_portal_template_mount.py" . DBP175-1-AC2</invocation><expect>DBP175-1-AC2 PASS</expect></criterion>
`DBP175-1-AC2` -- the view's pure core resolves served, preview and none states, the banner words show once in the preview and never in a live report, `none` renders nothing; the fixture is loaded by a dynamic import gated on `import.meta.env.DEV` and never imported statically; the route string is the served route. Base: FAIL.
<criterion id="DBP175-1-AC3" cell_refs="DB-b-307"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p175_portal_template_mount.py" . DBP175-1-AC3</invocation><expect>DBP175-1-AC3 PASS</expect></criterion>
`DBP175-1-AC3` -- every test under `__tests__/irpt-dashbd/` passes, the typecheck passes, the production build succeeds and its output carries neither the `SYNTHETIC PREVIEW` words nor the synthetic fixture (the scan's positive control sees both). Base: FAIL.

<expected_criteria>DBP175-1-AC1,DBP175-1-AC2,DBP175-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and in the portal repo the agreed write set of step 6. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files. Writes: the portal feature branch (and pushing it to origin under its own name), the workspace folder and files named below. No AWS call, no Terraform command, no DEV or PROD push, no portal promote, no change to the dev server on port 5174 (dev builds use port 5174 ONLY and that server is another seat's).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it. A candidate file that must change for the mount to work is a BLOCKING row, not an edit.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W246-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit workspace files with `.tools/safe-commit.sh`; READ the whole gate output: a refused commit leaves your edit uncommitted and blocks every other seat's merge. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~246/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-307.performance-tab-template-view-and-export-mount.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 167 (round 149, workstream PORTALMOUNT), cell `DB-b-307`.
<owned_cells>DB-b-307</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBP175-1-AC1, DBP175-1-AC2, DBP175-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~246/IRPT_DASHBD.TO-DB-b-307.performance-tab-template-view-and-export-mount.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBP175-1-AC1,DBP175-1-AC2,DBP175-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID). Record the portal head in the instance's notes.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the portal branch and head; the routes and files in one line each; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a portal feature branch only; nothing reaches DEV or PROD until the client-facing approval row is closed approved by Andrew; no AWS resource is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: the page reads a route the IB-pr-551 hops build; this cell adds no route and no rewrite.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base; the checker's probe and the dist scan's positive control are its own controls.
lane: the <paths> block and the agreed portal write set ARE the grant; the page files are `~C2`'s (agreed with `~C2`, msg 17:01Z).
</preflight>

# TO IRPT_DASHBD.TO-DB-f-503 -- the EXPORT MOUNT of the filled report: the export names a filled-report source at submit, the preview and the print read the report through round 114's reader (a print by the version the submit froze), and the print renders it through the report document; every state without a served report is exactly as it is

<to_id>IRPT_DASHBD.TO-DB-f-503</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~503</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>115</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, the round-114 analysis for F-SHIP section 2 cell 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_114_20261015.md`: "The export mount in F-SHIP's `export/` folder, reading the export source kind exactly as the signed IB-pr-551 packet defines it. Tests use an injected answer ... on the same portal branch as the tab ... not pushed") | **Rows:** IRPT_DASHBD-D2-W503-S<k> | **Decomp cell:** `DB-f-503` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R115_F.md`) | **outcome_ref:** FWD-21 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-503` (branch `wk-IRPT_DASHBD-503`); run everything from its root unless a step says the portal. `C:/dev/wk-irpt-dashbd-503/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-503-portal`), cut from `cand/dell2/irpt-default-performance-report` @d3c379663faceca7f4907366e0943d2b19022b6e: the default performance report plus round 114's reader and tab mount. Do not amend or revert anything already committed there. Portal files commit in the portal repo with plain git and your author line (`0.9.0_WK_IRPT_DASHBD~503 <0.9.0_WK_IRPT_DASHBD~503@opal.agent>`); your folder, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~503/`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours. Any real client, household or account id and any figure of a client is never written in the repo, a row or your report; use made-up values (the synthetic fixture `dashboard/report/fixtures/syntheticReport.ts` carries them). All portal paths below are under `portal/src/pages/InvestorReporting/`.

**Why.** Round 114 built a reader of a client's filled report (`dashboard/report/reportRead.ts`: `reportReadPath`, `readReportAnswer`, `ReportAnswer`) and mounted the report in the Performance tab, inert until a route serves it. The export is the other half of FWD-21 ("on the Performance tab and as the export"). Today the export of a Performance report names either a retained report (PATH A) or, for a dashboard account, a `performance_source` `{path: 'PLATINUM', account_id, start, end}` that the SERVER pins at submit (the page never sends a version, a sha256 or an as_of; `export/submit.ts` `PerformanceSource`, `export/ExportButton.tsx` about line 236); the preview reads the account's series through `export/resolveBundle.ts` (`accountId`, `seriesVersion`, `readDashboardFor`) and the print route (`render/PrintEntry.tsx`, about lines 214-217 and 292) takes the query `account` and the frozen `version`. The signed serve-path packet (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~395/SERVE_PATH_PAIR_PACKET_V1.md`, section on hop 4) adds a source kind for the filled report that is frozen at submit the same way, but names no wire field. So this cell mirrors PATH B for the filled report with PROPOSED names kept in ONE small file, so a later byte change is a one-place amendment. Nothing serves a report yet: with no served report every path below is exactly as before.

**The cell (`DB-f-503`).**
1. **Read first.** `export/submit.ts` (`PerformanceSource`, `buildSubmitRequest`); `export/ExportButton.tsx` (the props `accountId`, `start`, `end`, and how `performanceSource` is built and passed); `export/Preview.tsx` (how `accountId` reaches `resolveBundle`); `export/resolveBundle.ts` (the `accountId`, `seriesVersion`, `readDashboardFor`, `fetchJson` deps, the PATH B read and `dashboardPerformance` on the resolved bundle, and its bundle type); `render/PrintEntry.tsx` (the query reads, the `resolveBundle` call), `render/Page.tsx` and `render/performance/` (how a bundle with `dashboardPerformance` is drawn) and `render/performance/report/PerformanceReportDocument.tsx` (props: `report`, `firmId`); `dashboard/report/reportRead.ts` and `reportModel.ts` (`FilledReport`); `tabs/reporting/ReportingTab.tsx` (`PerformanceExportTarget`, `buildDashboardExportTarget`, `reportFor`, the effect that tells the page the export target, and the report state round 114 added); the round-114 tests under `__tests__/irpt-dashbd/` (the style: `bun:test`, `renderToStaticMarkup`, injected `fetchJson` or answer, no network). Run `bun test src/pages/InvestorReporting` once from the portal before any edit: that is your base (record its failing-test count).
2. **The source, in one file.** NEW `export/filledReportSource.ts`: `export type FilledReportSource = { readonly path: 'FILLED_REPORT'; readonly client_id: string }`, `export function filledReportSource(clientId: string): FilledReportSource`, and a one-line comment that the names are a proposal that mirrors `PerformanceSource` (the server pins version, sha256 and as_of at submit) until the serve-path packet's export slice names them. Nothing else in the code spells `FILLED_REPORT` or `client_id` for this purpose.
3. **Submit.** `export/submit.ts`: `buildSubmitRequest`'s `performanceSource` argument accepts `PerformanceSource | FilledReportSource`; the body is built exactly as for PATH B (`{ ...toExportBundleWire(bundle), performance_source }`); an absent source leaves the body byte-for-byte as before.
4. **The button and the preview.** `export/ExportButton.tsx` gains an optional prop `clientId?: string`, carried in the same places `accountId` is (the preview state and the memo keys); when it is set, `reportKind === 'performance'` and no `accountId` is set, the submit names `filledReportSource(clientId)` and no retained report (`reportRefs` empty). `export/Preview.tsx` passes `clientId` to `resolveBundle` as `accountId` is. `export/resolveBundle.ts` gains optional deps `clientId?: string`, `readReportFor?: (clientId, selectedTenant, versionId?) => Promise<ReportAnswer>` (a test seam; default: `readReportAnswer` from `../dashboard/report/reportRead`, never called on the fixture adapter) and, for a Performance resolve naming a `clientId`: a served answer puts `filledReport: FilledReport` on the resolved bundle and NO PATH A request is made; not served, the resolve falls back to exactly what it does today. The bundle type gains `filledReport` (null when absent).
5. **The tab's export target.** `tabs/reporting/ReportingTab.tsx`: a pure exported `buildFilledReportExportTarget(accountRef, clientId, reportAsOf, window)` returning a `PerformanceExportTarget` with `clientId` set, `reportRefs: []`, `sourceRevision` `filled:<clientId>:<reportAsOf>` (the browser's label for its own cache, never a server revision), and the effect that tells the page the target uses it when `reportFor(...)` is served (round 114), else the target it builds today. `PerformanceExportTarget` gains `clientId?: string`. The ONE line that passes the target's `clientId` to `ExportButton` is in `index.tsx`, which is NOT yours: do not edit it. Name that line in your final report as the hookup the issuer adds.
6. **The print.** `render/PrintEntry.tsx` reads the optional query keys `client` and `version` (`version` is the one it already reads) and, for a Performance print naming `client`, calls `resolveBundle` with `clientId` and (for a frozen print) the version so the report is read as the version the submit froze: extend `reportReadPath(clientId, selectedTenant, versionId?)` in `dashboard/report/reportRead.ts` with `&version_id=<versionId>` exactly as `reportingReadPath` does for the series, and `readReportAnswer` takes an optional version. The render draws a bundle carrying `filledReport` through `PerformanceReportDocument` (in the file that today draws `dashboardPerformance`, or `render/Page.tsx`), with the firm id the bundle already holds; a bundle without `filledReport` draws exactly what it draws today. A print naming `client` whose report is not served shows the print's existing refusal for an unreadable source, never a blank page.
7. **Tests** (new files only, `bun:test`, an injected answer, no network):
   - `__tests__/irpt-dashbd/export-filled-report.test.tsx`, at least 8 tests whose titles contain, between them, the words `source` (the source builder returns `{path: 'FILLED_REPORT', client_id}` and nothing else), `submit` (the body carries `performance_source` for a client and is byte-identical to today's body when no source is given), `preview` (a served report puts `filledReport` on the resolved bundle with no PATH A request; use `readReportFor`), `served`, `absent` (not served falls back to PATH A exactly as before), `client` (a different client's answer is never used) and `fixture` (the fixture adapter makes no read). Also one test that `buildFilledReportExportTarget` carries `clientId`, empty `reportRefs` and the label above.
   - `__tests__/irpt-dashbd/print-filled-report.test.tsx`, at least 6 tests whose titles contain, between them, `print` (the entry reads `client` and `version`), `version` (the report path carries `version_id` only when a version is named), `client`, `served` (a served bundle draws the report document: assert on `renderToStaticMarkup` that the eight section ids of the report appear), `absent`, `falls back` (a bundle without `filledReport` draws what it drew before: compare with the base commit's markup, or assert the dashboard/body markup is unchanged) and `document`.
8. **Gates you run once, after your last portal commit:** from the portal worktree `bun run typecheck` and `bun run lint` (0 errors each, add nothing to a baseline) and `bun test src/pages/InvestorReporting` again: the failing-test names after must be a subset of the names before (round 114 left 20 failing at its base; if the count differs, record both). The tab's neighbour test `__tests__/dsgn-irptv1/iv-e-135.dashboard-switch.test.ts` pins the literal `{dashboardServed ? (` in `ReportingTab.tsx`: leave that literal intact (do not edit that test).
9. **Record** `BUILD_R115.json` in your folder with exactly: `portal` {`branch` "wk-IRPT_DASHBD-503-portal", `base` "d3c379663faceca7f4907366e0943d2b19022b6e", `head` (the final portal commit sha), `files_changed` (paths relative to the portal root)}, `wire_proposal` {`path` "FILLED_REPORT", `fields` (the list of field names of `FilledReportSource`), `print_query` (the list of query keys the print reads for it)}, `hookup_for_issuer` (the one line of `index.tsx` the issuer must add, in words), `tests` {`export_pass`, `print_pass`, `suite_before_fail`, `suite_after_fail`}, `typecheck_rc`, `lint_errors`, `pushed` false, `deployed` false. Counts, names and paths only.

<criterion id="DBF115-1-AC1" cell_refs="DB-f-503"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r115/p115_export.py" . DBF115-1-AC1</invocation><expect>DBF115-1-AC1 PASS</expect></criterion>
`DBF115-1-AC1` -- the export side: `filledReportSource.ts` names `FILLED_REPORT`; `submit.ts`, `ExportButton.tsx`, `resolveBundle.ts` and `ReportingTab.tsx` carry the tokens steps 3 to 5 name; `export-filled-report.test.tsx` has the seven title words and passes with 0 failures and at least 8 tests. Base: FAIL (no file).
<criterion id="DBF115-1-AC2" cell_refs="DB-f-503"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r115/p115_export.py" . DBF115-1-AC2</invocation><expect>DBF115-1-AC2 PASS</expect></criterion>
`DBF115-1-AC2` -- the print side: `PrintEntry.tsx` reads `client` and `version`, `reportRead.ts` carries `version_id`, a render file other than the document itself mounts `PerformanceReportDocument`; `print-filled-report.test.tsx` has the seven title words and passes with 0 failures and at least 6 tests. Base: FAIL (the print entry lacks the read).
<criterion id="DBF115-1-AC3" cell_refs="DB-f-503"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r115/p115_export.py" . DBF115-1-AC3</invocation><expect>DBF115-1-AC3 PASS</expect></criterion>
`DBF115-1-AC3` -- bounds: the portal diff from the round-114 head to your head is not empty and touches only files under `export/` and `render/`, `tabs/reporting/ReportingTab.tsx`, `dashboard/report/reportRead.ts` and the two new test files. Base: FAIL (no change).

<expected_criteria>DBF115-1-AC1,DBF115-1-AC2,DBF115-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: `index.tsx`, `contracts/wire/ExportBundle.ts` (the server's wire type), `dashboard/reportingRead.ts` and every other `dashboard/*.ts`, `dashboard/report/reportModel.ts`, `PerformanceReport.tsx`, `contractMembers.ts`, the contract, every existing test (including `__tests__/dsgn-irptv1/iv-e-135.dashboard-switch.test.ts`), the issuer's check, the generated firm names and every portal file outside the grant.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change.
- **Inert means inert.** With no served report the markup and the requests of the tab, the preview, the submit body and the print are those of the base commit; the one added request is the report read on a selection or a preview that names a client, which answers `absent` while no route serves it. A read that is not served never changes what the advisor sees and never shows an error of its own.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a neighbour test outside your grant fails because of your change, file a BLOCKING row naming it and stop on that point; do not edit it. If the wire names you wrote cannot be mirrored from PATH B as step 2 says, file a BLOCKING row. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W503-S<k>` (D2 is the device coordinate), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~503/
portal/src/pages/InvestorReporting/export/
portal/src/pages/InvestorReporting/render/
portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx
portal/src/pages/InvestorReporting/dashboard/report/reportRead.ts
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/export-filled-report.test.tsx
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/print-filled-report.test.tsx
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-503.export-mount-of-the-filled-report-source-preview-print-inert-until-served.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R115_F.md</decomp_doc> round 115, workstream ~F2, cell `DB-f-503`.
<owned_cells>DB-f-503</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF115-1-AC1, DBF115-1-AC2, DBF115-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~503/IRPT_DASHBD.TO-DB-f-503.export-mount-of-the-filled-report-source-preview-print-inert-until-served.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF115-1-AC1 DBF115-1-AC2 DBF115-1-AC3` BEFORE the flip; pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the portal head sha and the changed files; the wire names you wrote and the print query keys; the exact `index.tsx` hookup the issuer must add; the test counts (export, print, suite before and after) and the typecheck and lint results; anything you saw off-task (as row ids). Made-up values only: no real id and no client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: portal component edits on a local branch; nothing is wired, served or deployed, and neither the route nor the export source kind exists yet.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; the reader names the route the signed serve-path packet designs.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DBF115-1-AC1, AC2 and AC3 FAIL at base and the checker's pure helpers are exercised by its self-test (13 arms).
lane: the <paths> block IS the grant.
</preflight>

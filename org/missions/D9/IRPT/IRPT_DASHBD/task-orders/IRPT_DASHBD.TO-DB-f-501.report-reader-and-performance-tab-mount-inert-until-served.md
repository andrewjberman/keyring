# TO IRPT_DASHBD.TO-DB-f-501 -- the REPORT READER and the PERFORMANCE TAB MOUNT: the one fetch of a client's filled report, and the tab shows the default performance report in place of its body only when that report is served; every other state leaves the tab exactly as it is

<to_id>IRPT_DASHBD.TO-DB-f-501</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~501</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>114</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, the four-workstream ruling (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md`: F-SHIP writes the portal `render/`, `export/`, `tabs/reporting/` and `dashboard/` folders under `InvestorReporting/`; "F-SHIP reads the filled document and never builds one") | **Rows:** IRPT_DASHBD-D2-W501-S<k> | **Decomp cell:** `DB-f-501` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R114_F.md`) | **outcome_ref:** FWD-21 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-501` (branch `wk-IRPT_DASHBD-501`); run everything from its root unless a step says the portal. `C:/dev/wk-irpt-dashbd-501/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-501-portal`), cut from `wk-IRPT_DASHBD-180-portal` @c81d54ff31b0c44b45dabdd217b531a183723c8b: the branch that carries the 20 commits of the default performance report. Do not amend or revert anything already committed there. Portal files commit in the portal repo with plain git and your author line (`0.9.0_WK_IRPT_DASHBD~501 <0.9.0_WK_IRPT_DASHBD~501@opal.agent>`); your folder, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~501/`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours. Any real client, household or account id and any figure of a client is never written in the repo, a row or your report; use made-up values (the synthetic fixture `dashboard/report/fixtures/syntheticReport.ts` carries them).

**Why.** The default performance report (the baseline's eight sections, one contract, 117 members) is built and graded, but nothing mounts it: the Performance tab still draws its older body. The report's data is a "filled report" (`FilledReport` in `dashboard/report/reportModel.ts`: a household and a map of member values), which today exists only as a private sample file built by a script. For the report to reach the tab, the tab needs ONE reader of a filled report and ONE switch. The route that will serve a filled report does not exist yet (another seat owns it and a read cell, `DB-f-502`, is mapping it), so this cell mounts the report INERT: with no served report the tab is byte-for-byte what it is today. That makes the branch safe to land before the route does.

**The cell (`DB-f-501`).**
1. **Read first.** `portal/src/pages/InvestorReporting/dashboard/reportingRead.ts` (the pattern to mirror: `reportingSummaryPath`, `readClientSummaryAnswer`, `envelopeReason`, `reasonFromError`, `liveFetchJson`, `FetchJson`, `REPORTING_READ_BASE`); `dashboard/report/reportModel.ts` (the `FilledReport` and `AccountEntry` interfaces, `buildReportModel`); `dashboard/report/PerformanceReport.tsx` (its props: `report`, `firmId`); `tabs/reporting/ReportingTab.tsx` (`dashboardFor`, the client-summary state that reads once per selection and never for the fixture adapter, the render that chooses between `dashboardServed` and the report body, and where the tab learns the firm id for the header); the tests under `__tests__/irpt-dashbd/` (the style: `bun:test`, `renderToStaticMarkup`, no server, no network).
2. **The reader** `portal/src/pages/InvestorReporting/dashboard/report/reportRead.ts` (a NEW file), exporting exactly:
   - `reportReadPath(clientId: string, selectedTenant?: string | null): string` = `${REPORTING_READ_BASE}/client/${encodeURIComponent(clientId)}/report`, plus `?selected_tenant=${encodeURIComponent(selectedTenant)}` only when a tenant is given;
   - `type ReportAnswer` = `{ kind: 'served'; clientId: string; report: FilledReport }` or `{ kind: 'absent'; reason: string | null }`;
   - `readReportAnswer(clientId, selectedTenant, fetchJson = liveFetchJson): Promise<ReportAnswer>`: ONE fetch. A thrown request is `absent` with the reason code `reasonFromError` reads; an estate envelope with `ok: false` is `absent` with its public reason code; a body that is not a `FilledReport` (not a plain object; no `household` object with a string `household_ref`, a string `as_of`, a string `first_data_date` and an `accounts` array whose entries each carry a string `account_id`; no `values` object) is `absent` with the reason `REPORT_UNREADABLE`; otherwise `served` with the body as the report. It never returns a partial report and never builds or fills a member. The path comment says the route is a PROPOSAL that mirrors the summary route and is one line to change.
   - If a helper in `reportingRead.ts` you need is not exported, do NOT edit that file: copy the few lines you need into your file (it is outside your grant).
3. **The mount** in `tabs/reporting/ReportingTab.tsx` (the only existing file you edit), in the style of the client-summary state:
   - a pure exported `reportFor(selectionKey: string | null, held: { readonly key: string; readonly answer: ReportAnswer } | null): Extract<ReportAnswer, { kind: 'served' }> | null` that returns the served answer only when `held.key === selectionKey`, else null (so an answer that arrives after the advisor changed client never shows under the new one);
   - state and ONE effect that call `readReportAnswer` once per selection key (the selected client id plus the tenant) and never when the adapter is the fixture adapter (`api.kind === 'fixture'`), exactly as the summary read does;
   - in the render, ahead of the existing `dashboardServed ? ... : answer && report ? ...` choice, `reportFor(...)` non-null renders `<div data-slot="reporting-report"><PerformanceReport report={...} firmId={...} /></div>` INSTEAD of the dashboard figure and the body (never both on one page); null leaves the existing choice untouched. The firm id is the one the tab already knows for its header; if the tab holds none for a selection, the report is not shown (the tab falls back) and you file an OBSERVATION row.
   - nothing else in the file changes: no reformatting, no moved import, no touched prop.
4. **Tests** (new files only, `bun:test`, no network):
   - `__tests__/irpt-dashbd/report-read.test.tsx`: at least 6 tests whose titles contain, between them, the words `path`, `served`, `refus` (an `ok: false` envelope is absent with its code), `throw` (a rejected fetch is absent), `unreadable` (a body that is not a filled report is absent with `REPORT_UNREADABLE`) and `tenant` (the tenant query is present only when given). Use the synthetic fixture for the served case and an injected `fetchJson`.
   - `__tests__/irpt-dashbd/report-tab-mount.test.tsx`: at least 5 tests whose titles contain, between them, `same client` (served for the same key shows), `other client` (a different key gives null), `absent` (an absent answer gives null), `fixture` (the fixture adapter makes no read: assert on the exported decision, or on the effect's guard if you pull it into a pure function) and `falls back` (with no served report the tab markup for a given props set equals the markup of the base commit's tab; render both and compare, or assert the dashboard/body slot is still present and `reporting-report` is absent).
5. **Gates you run once, after your last portal commit** (they are for you; the checker reads only the tests): from the portal worktree `bun run typecheck` and `bun run lint` (0 errors each, add nothing to a baseline), and `bun test src/pages/InvestorReporting` once before any edit (base) and once after: the failing-test names after must be a subset of those before (if some fail at the base, record their count in your report; do not touch them).
6. **Record** `BUILD_R114.json` in your folder with exactly: `portal` {`branch` "wk-IRPT_DASHBD-501-portal", `base` "c81d54ff31b0c44b45dabdd217b531a183723c8b", `head` (the final portal commit sha), `files_changed` (the list of changed paths relative to the portal root)}, `route_proposed` (the path template), `tests` {`read_pass`, `mount_pass`, `suite_before_fail`, `suite_after_fail`}, `typecheck_rc`, `lint_errors`, `pushed` false, `deployed` false. Counts and paths only.

<criterion id="DBF114-1-AC1" cell_refs="DB-f-501"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r114/p114_ship.py" . DBF114-1-AC1</invocation><expect>DBF114-1-AC1 PASS</expect></criterion>
`DBF114-1-AC1` -- `reportRead.ts` exports `reportReadPath`, `readReportAnswer` and `ReportAnswer`, names the `/reporting/client/` base and the `/report` leaf; `report-read.test.tsx` has the six title words and at least 6 tests, and `bun test` on it from the portal worktree passes with 0 failures. Base: FAIL (no file).
<criterion id="DBF114-1-AC2" cell_refs="DB-f-501"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r114/p114_ship.py" . DBF114-1-AC2</invocation><expect>DBF114-1-AC2 PASS</expect></criterion>
`DBF114-1-AC2` -- `ReportingTab.tsx` imports the reader and `PerformanceReport`, exports `reportFor`, holds the `reporting-report` slot and calls `readReportAnswer`; `report-tab-mount.test.tsx` has the five title words and at least 5 tests and passes with 0 failures; the portal diff from the base commit to HEAD touches only the four granted files. Base: FAIL (the tab lacks the mount).

<expected_criteria>DBF114-1-AC1,DBF114-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: `dashboard/reportingRead.ts`, every other `dashboard/*.ts`, `dashboard/report/reportModel.ts`, `PerformanceReport.tsx`, `contractMembers.ts`, the contract, the render and export folders, every existing test, the issuer's check, the generated firm names and every portal file outside the grant.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change.
- **Inert means inert.** With no served report the tab's markup and requests are those of the base commit; a read that is not served never changes what the advisor sees and never shows an error of its own.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a neighbour test outside your grant fails because of the mount, file a BLOCKING row naming it and stop on that point; do not edit it. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W501-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~501/
portal/src/pages/InvestorReporting/dashboard/report/reportRead.ts
portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/report-read.test.tsx
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/report-tab-mount.test.tsx
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-501.report-reader-and-performance-tab-mount-inert-until-served.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R114_F.md</decomp_doc> round 114, workstream ~F2, cell `DB-f-501`.
<owned_cells>DB-f-501</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF114-1-AC1, DBF114-1-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~501/IRPT_DASHBD.TO-DB-f-501.report-reader-and-performance-tab-mount-inert-until-served.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF114-1-AC1 DBF114-1-AC2` BEFORE the flip; pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the portal head sha and the changed files; the route path you wrote; the test counts (read, mount, suite before and after) and the typecheck and lint results; whether the tab holds a firm id for every selection (and if not, which); anything you saw off-task (as row ids). Made-up values only: no real id and no client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: portal component edits on a local branch; nothing is wired, served or deployed, and the route the reader names does not exist.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; the reader names a PROPOSED route that cell DB-f-502 maps.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DBF114-1-AC1 and AC2 FAIL at base and the checker's pure helpers are exercised by its self-test (13 arms).
lane: the <paths> block IS the grant.
</preflight>

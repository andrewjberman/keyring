# TO IRPT_DASHBD.TO-DB-b-309 -- the Performance tab after Andrew's 5174 smoke, ON TOP OF the DB-b-307 branch: Global sends the client's own firm on every client read, the firm-binding banner is gone, the template never renders silent, Beginning value comes before Ending value and money prints as dollars with grouping, and the export's print window prints the same template (round 149; PORTAL, CLIENT-FACING)

<to_id>IRPT_DASHBD.TO-DB-b-309</to_id>
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
<workstream>PORTALGLOBAL</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** PORTALGLOBAL, round 149 | **Ordered by:** the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IR_PERFORMANCE_TAB_ANDREW_SMOKE_20261016.md` @`d22e05dd68` (Andrew: "I have not seen a change on this page in days"; the Global read is refused for want of `selected_tenant`), his msgs 9754 (Beginning before Ending, dollars with commas) and 9770 (the print window prints the template, carried by the export's own target) and the page owner's write set `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/R151_PERFORMANCE_TAB_WRITE_SET_AND_PANELS.md` @`9b04f830b2` (part (a) is your exact spec, file and line against the branch head `1779d676`) | **Decomp cell:** `DB-b-309` (decomposition section 170) | **depends_on:** `DB-b-307` (this IS its branch, head `1779d676064a2e8e7c4b8edda52c719c9c519199`).

**Risk class SERVED, CLIENT-FACING.** The cell adds commits to the portal feature branch `cand/dell2/irpt-49f-performance-template-mount` (ONE branch for Andrew's smoke) and pushes only that branch; nothing reaches DEV or PROD; the approval row (client-facing, Andrew) follows the CTO's smoke.

---

## WORKER FACE

You continue in your workspace worktree `C:/dev/wk-irpt-dashbd-246` and its portal worktree `C:/dev/wk-irpt-dashbd-246/portal`, which is on the branch above at `1779d676`. Never push the workspace; never commit the workspace `portal` gitlink. Every portal commit carries the explicit identity: `git -C <portal> -c user.name="0.9.0_WK_IRPT_DASHBD~246" -c user.email="0.9.0_WK_IRPT_DASHBD~246@opal.agent" commit ...`. Counts, dates, hashes and words only in the workspace repo; the fixture and tests are synthetic. Tool calls that carry a backslash-r or backslash-n escape inside a shell heredoc can be altered in transit: write patch scripts to a file with the Write tool and run them. Resolve `bun` from the PATH.

**The cell (`DB-b-309`).**
1. **Read first, whole:** the page owner's file named above (the part (a) write set is your exact spec: every file, line and test); the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p177_portal_global_and_format.py` (your three criteria; its probe test is the exact spec of the new exports); the CTO's ruling.
2. **Rulings 1 to 3 and Andrew's two asks, as the page owner's part (a):** (a) `HeaderSelection` gains the optional `selectedTenant`; `index.tsx` sets it from the same `selectedTenantFor(...)` it already uses (read once into a const, used in both places); `ReportingTab.tsx` reads `header?.selectedTenant ?? focusCtx?.selectedTenant` for the series, manifest, client summary, per-account YTD and the template's read, and for the focus POST's context; (b) the firm-binding banner and its computation are removed from `ReportingTab.tsx` (`firmBindingNotice`, `FIRM_BINDING_REASON`, `firmBindingWords` and the banner sentence "does not match this client's firm" appear nowhere in the source; their tests under `__tests__/dsgn-irptv1/` are removed or edited); (c) the Firm control is already server-catalogue driven: you ADD A TEST ONLY (a non-global login with one permitted firm renders no dropdown and `selectableFirmIds` is exactly that firm; the dropdown never lists a firm outside `permittedFirms`, over three firms); (d) `PerformanceHeadline.tsx` `tileSpecs`: the `beginning` entry first, then `ending`; (e) ONE new `tabs/reporting/currency.ts` exporting `formatUsd(value: number, currency: string): string`: `'USD'` prints `$` with grouping and two decimals (`formatUsd(92186.84, 'USD') === '$92,186.84'`, `formatUsd(-1234.5, 'USD') === '-$1,234.50'`), any other currency prints its code, a space and the grouped amount (`formatUsd(1234.5, 'EUR') === 'EUR 1,234.50'`), never a guessed symbol; `PerformanceHeadline.tsx` (`currencyText`, `metricText(..., 'currency')`) and `AccountsTable.tsx` (`endingValueText`) and every other printed money value of `tabs/reporting/` (find them: `toLocaleString`, `toFixed(2)`, `currencyText`) print through it, the currency code from the report.
3. **The template never renders silent (ruling 3), with these exact exports in `PerformanceTemplateView.tsx`:** `type UnavailableReason = 'REFUSED' | 'NOT_COVERED' | 'NOT_READY' | 'UNREADABLE'`; `TemplateState` becomes `{ kind: 'live'; report } | { kind: 'preview'; report } | { kind: 'unavailable'; reason: UnavailableReason } | { kind: 'loading' }` (the `none` kind is replaced); `resolveTemplate(served: FilledReport | null, previewFixture: FilledReport | null, reason: UnavailableReason | null): TemplateState` (served: `live`; else a fixture: `preview`; else a reason: `unavailable`; else `loading`); `PerformanceTemplateBody({ state, firmId })` renders: `live` the report with no banner; `preview` the `SYNTHETIC PREVIEW` banner once above the report (dev server only); `loading` the sentence `Loading the performance report for this client.`; `unavailable` ONE worded sentence of at least 20 characters per reason (what happened in plain words; the refusal of a firm-bound login is a real fault and is said here, never as the old header sentence); NEVER `null`. The view maps the read's outcome to the reason (a refused read: `REFUSED`; the route answering that the client is not covered: `NOT_COVERED`; the route not ready or absent (404): `NOT_READY`; a body that is not the `{household, values}` shape or a network failure: `UNREADABLE`). A production build renders the worded `unavailable` state, never the fixture or the banner words (the `import.meta.env.DEV` gate and the dynamic import stay; the checker's production-build scan stays).
4. **The print window (the CTO's msg 9770).** The export's print window must print the SAME template document the tab shows, not the bundle document, and must not depend on per-page-load memory: `render/PrintEntry.tsx` (and `export/Preview.tsx`) resolve their own template state by calling a new exported `readServedReport(clientId, selectedTenant)` of `PerformanceTemplateView.tsx` (the one served read the tab also uses) with the client and tenant the export's own target or receipt carries (read what `export/submit.ts` and the print target hand to the print window; do NOT edit `submit.ts` or `ExportButton.tsx`; if the target lacks the client id or the tenant, file a BLOCKING row naming the missing field and stop on it), and `resolveTemplate` with the DEV-only fixture exactly as the tab does. The print entry must NOT read `readTemplateState`. A test proves a FRESH print window (no tab ever mounted in the module graph) prints the template document from the injected read. `templateState.ts` may stay for the in-app preview or be removed if unused.
5. **Files you may change:** `header/HeaderSelectionContext.ts`, `index.tsx`, `tabs/reporting/ReportingTab.tsx`, `tabs/reporting/PerformanceTemplateView.tsx`, `tabs/reporting/PerformanceHeadline.tsx`, `tabs/reporting/AccountsTable.tsx`, `tabs/reporting/currency.ts` (new), `render/PrintEntry.tsx`, `render/manifest.ts`, `export/Preview.tsx`, `tabs/reporting/templateState.ts`, new test files under `__tests__/irpt-dashbd/`, and the `firmBindingWords` tests under `__tests__/dsgn-irptv1/`. **Not** `dashboard/*.ts` (`reportingRead.ts`, `seriesContract.ts`, `coverageWords.ts`, `DashboardPerformance.tsx`), `export/submit.ts`, `export/ExportButton.tsx`.
6. **Tests (new files under `__tests__/irpt-dashbd/`, names starting exactly):** `performance-tab-global-and-firm` (Global: with `headerSelection.selectedTenant` set and `scope` null the series, manifest, client-summary, per-account YTD and filled-report paths each carry `selected_tenant=<firm>`; unset, nothing changes; the banner sentence appears in no render path; the advisor cannot select a second firm); `performance-template-states` (loading, unavailable per reason, live, preview, never an empty node; the production tier renders the worded state and no banner); `performance-headline-order-and-money` (the headline order and `$92,186.84` and `$99,698.29` for both tiles and the accounts table, a non-USD currency with its code); `performance-print-fresh-window` (a fresh print window prints the template). Every other test under `__tests__/irpt-dashbd/` keeps passing; the suite's failing names, if any, are a subset of the base's.
7. **Run the checks yourself from the workspace root** (the checker reads the portal repo at `<root>/portal`): `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p177_portal_global_and_format.py" . DBP177-1-AC1`, then AC2, then AC3 (AC3 runs the test directory, the typecheck and the production build, 10 to 20 minutes). Note: the earlier checker `p175` expects the `none` state and the absence of the new exports; it is the DB-b-307 checker and is not run for this cell. Commit on the portal branch (explicit identity), push ONLY `cand/dell2/irpt-49f-performance-template-mount` when all three pass, and tell the issuer the pushed head.
8. **Record** `RD_PORTAL_GLOBAL_FACTS_R149.json` in your folder (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~246/`) with EXACTLY these fields: `portal_branch`; `portal_head` (40 hex pushed); `base_head` ("1779d676064a2e8e7c4b8edda52c719c9c519199"); `files_changed` (sorted portal paths); `tenant_flow` (one sentence: where the client's firm is computed and where it is read); `banner` (one sentence); `template_states` (one sentence); `print_window` (one sentence: what the target carries and how the fresh window resolves the template); `money_helper` (one sentence); `tests_added` (the new test file names); `words` (one paragraph, 80 to 1800 characters: what changed and why, and what is NOT proven: no browser walk at Global, no DEV or PROD change, the route does not exist yet so the live read is exercised by injected reads).

<criterion id="DBP177-1-AC1" cell_refs="DB-b-309"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p177_portal_global_and_format.py" . DBP177-1-AC1</invocation><expect>DBP177-1-AC1 PASS</expect></criterion>
`DBP177-1-AC1` -- the branch is still `cand/dell2/irpt-49f-performance-template-mount` and descends from `1779d676`; only the agreed write set changed (and none of the protected files); `HeaderSelection` carries `selectedTenant`, `index.tsx` sets it and the tab reads it; the banner and its reason constant are gone and its sentence is in no source file; in `tileSpecs` the beginning tile precedes the ending tile; the headline and the accounts table print through `formatUsd` from `currency.ts`; the print entry renders `PerformanceReportDocument` through `resolveTemplate` or `readServedReport` and does not read `readTemplateState`; the view declares the `loading` and `unavailable` states. Base: FAIL.
<criterion id="DBP177-1-AC2" cell_refs="DB-b-309"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p177_portal_global_and_format.py" . DBP177-1-AC2</invocation><expect>DBP177-1-AC2 PASS</expect></criterion>
`DBP177-1-AC2` -- a probe test: `formatUsd` prints `$92,186.84`, `$99,698.29`, `$1,234,567.00`, `-$1,234.50` and `EUR 1,234.50`; `resolveTemplate` returns `live`, `preview`, `unavailable` and `loading` for the four inputs; no state renders an empty node (loading prints its sentence, each reason prints a worded sentence of 20 or more characters without the banner words, live has no banner, preview has it once). Base: FAIL.
<criterion id="DBP177-1-AC3" cell_refs="DB-b-309"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p177_portal_global_and_format.py" . DBP177-1-AC3</invocation><expect>DBP177-1-AC3 PASS</expect></criterion>
`DBP177-1-AC3` -- the four named test files exist; no test under `__tests__/dsgn-irptv1/` still names the removed banner; every test under `__tests__/irpt-dashbd/` passes; the typecheck passes; the production build succeeds and its output carries neither the `SYNTHETIC PREVIEW` words nor the synthetic fixture (the scan's positive control sees both). Base: FAIL.

<expected_criteria>DBP177-1-AC1,DBP177-1-AC2,DBP177-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and in the portal repo the write set of step 5. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files. Writes: the portal feature branch (and pushing it to origin under its own name), the workspace folder and files named below. No AWS call, no Terraform command, no DEV or PROD push, no change to the dev server on port 5174 (another seat's).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it. A protected file that must change is a BLOCKING row, not an edit.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W246-S<k>` (continue from your last), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit workspace files with `.tools/safe-commit.sh`; READ the whole gate output: a refused commit leaves your edit uncommitted and blocks every other seat's merge. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~246/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-309.performance-tab-global-firm-template-states-and-money.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 170 (round 149, workstream PORTALGLOBAL), cell `DB-b-309`.
<owned_cells>DB-b-309</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBP177-1-AC1, DBP177-1-AC2, DBP177-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~246/IRPT_DASHBD.TO-DB-b-309.performance-tab-global-firm-template-states-and-money.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBP177-1-AC1,DBP177-1-AC2,DBP177-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it. Record the portal head in the instance's notes.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the portal branch and head pushed; the files in one line each; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a portal feature branch only; nothing reaches DEV or PROD until the client-facing approval row is closed approved by Andrew; no AWS resource is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant changes; the read path sends the existing `selected_tenant` that the service already admits for an internal caller (CTO ruling d22e05dd68).
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is added or changed; the page sends one more existing query parameter.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base; the checker's probe and the production-build scan's positive control are its own controls.
lane: the <paths> block and the page owner's agreed portal write set ARE the grant.
</preflight>

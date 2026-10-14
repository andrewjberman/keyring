# TO IRPT_DASHBD.TO-DB-b-187 -- the three render defects of the default performance report fixed (an absent reason prints once per section, the "As of" footer reads the household's last measured date, each chart draws or says why), the real 49 Financial sample re-rendered locally, the PDF read page by page as an image

<to_id>IRPT_DASHBD.TO-DB-b-187</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~152</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>101</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 7451 and `CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUNDS_99_100_20261014.md` ENRICHMENT item 1 (PRD v0.14, FWD-21) | **Rows:** IRPT_DASHBD-D2-W152-S<k> | **Decomp cell:** `DB-b-187` (decomposition section 103) | **outcome_ref:** FWD-21 | **depends_on:** none (the components exist on the portal branches the worktree is cut from).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-152` (branch `wk-IRPT_DASHBD-152`); run everything from its root unless a step says the portal. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~152/`.

**Two repos.** `C:/dev/wk-irpt-dashbd-152/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-152-portal`), cut from the branch that carries BOTH report components (the Performance tab's and the export document's). Do not amend or revert anything already committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` here is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours.

**Why.** FWD-21: any client at any firm opens ONE default performance report, on the Performance tab and as the export. Round 96 rendered the real 49 Financial household through the components and Andrew will read it; the issuer read the render and found three display defects:
1. **The absent reason repeats in every cell.** A figure Opal cannot produce prints "Not available yet: <reason>" in each cell, so one reason (for example "history not yet built: gold account_activity_daily holds 4 trading days") prints dozens of times and tables run long and narrow.
2. **The page footer reads "As of Not available yet: ...".** The as-of date is taken from the cover's as-of-date member, which the contract sources ABSENT. The filled report's own `household.as_of` is the last measured gold date and is what the footer must print.
3. **Charts draw nothing on the real sample** (every chart member of this household is absent, so each prints its words). The draw path must be PROVEN on a fixture and every chart slot must either draw from the series the contract already carries or print its absent reason in words.

**The cell (`DB-b-187`).**
1. **Read first.** `portal/src/pages/InvestorReporting/dashboard/report/` (`reportModel.ts`, `PerformanceReport.tsx`, `ReportChart.tsx`, `contractMembers.ts`, `fixtures/syntheticReport.ts`) and `portal/src/pages/InvestorReporting/render/performance/report/` (`PerformanceReportDocument.tsx`, `documentSheets.ts`), the contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` (its `document` and `document.filled_report` keys), the baseline schema `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/BD_FINANCIAL_PERFORMANCE_REPORT_BASELINE_SCHEMA_20261013.md`, the existing records `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~142/TAB_RENDER.json`, `~143/EXPORT_RENDER.json` and the render harness `~146/render_sample.ts` with its `README.txt`. Run the whole-scope suite once before any edit (`bun test src/pages/InvestorReporting` from the portal, output to a file under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~152/`) as your base.
2. **Fix the three defects in the components** (edit only files under `portal/src/pages/InvestorReporting/dashboard/report/` and `portal/src/pages/InvestorReporting/render/performance/report/`, and their tests under `portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/`):
   - An absent reason prints ONCE at its section or table head (a note under the heading naming which members it covers), and every absent cell it covers reads a short word ("Not available yet", with the member's `data-member` id kept). A reason that differs between members still prints once per distinct reason per section. Never blank, never 0, the fee basis still labeled. The checker counts every distinct absent reason (40 characters or more) of the sample in the export HTML: no reason may print more than 8 times (once per section) in either HTML.
   - Every page footer reads "<household> Performance Report", "As of <date>" with the date from the filled report's `household.as_of` (a long date, for example "October 9, 2026"; an ISO date is also accepted), and "Page n of N". Where `household.as_of` is missing the footer says so in words.
   - A chart member renders an inline `<svg>` from the series the filled report carries (a list of `{name, points}`); with no measured point it prints its absent reason in words, once. Tests against the synthetic fixture prove each: the fixture draws at least one `<svg>`; a chart with no points prints words and no `<svg>`.
   Tests: add or update tests (a new file `report-render-fixes.test.tsx` beside the existing ones, and the minimum edits to existing assertions that pinned the old behaviour: name each in your record). ONE temporary mutant (print the reason per cell again) that a test catches, then reverted. `bun run lint` and `bun run typecheck` after your last portal commit (0 errors); the whole-scope suite after (`new_failing_ids` []).
3. **Re-render the real sample.** Copy the harness `~146/render_sample.ts` into YOUR folder (edit your copy only; the ~146 file stays) and let it write FOUR outputs to the NEW private folder `C:/dev/_irpt_private_evidence_20261009/fwd21_sample_r101/`: `FWD21_TAB_49F_SAMPLE.html`, `FWD21_EXPORT_49F_SAMPLE.html`, `FWD21_EXPORT_49F_SAMPLE.pdf` from the real sample `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~141/HOUSEHOLD_SAMPLE.json` (do not edit or move it: its sha256 is checked), and `FWD21_FIXTURE_EXPORT.html` from the synthetic fixture (made-up data; it proves the charts draw). Follow the README for the run (from the portal: `bun <abs path to your render_sample.ts> <abs path to the report JSON> <abs path to the output folder>`). The harness's neutral firm word "Sample Firm" stays.
4. **Read the PDF as an image, page by page.** (AMENDMENT 1, issuer 2.0.0_SA_COO~D2, 2026-10-14: the Read tool refuses a PDF on this box and no rasteriser was on the PATH, so the first seat could not do this step, row W152-S1. The issuer installed one privately and wrote a tool.) Rasterise the PDF to PNGs with `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/tools/pdf_to_png.py <abs path to FWD21_EXPORT_49F_SAMPLE.pdf> <abs path to a NEW folder under C:/dev/_irpt_private_evidence_20261009/fwd21_sample_r101/pages_final/> 70` (writes `page_01.png` ...; the output stays in the private folder), then open EVERY `page_NN.png` with the Read tool (images are readable) and look at each page. Known defect to fix first if you find it: the document numbers 12 sheets ("Page n of 12") but the PDF holds more pages, because some sheets run onto a second PDF page; make each sheet fit one PDF page (print CSS or sheet content height) or number the real pages, and re-render, so that "Page n of N" matches the PDF's pages. Then look at every page: clipped text or a table running off a page edge or into the footer, overlapping lines, a footer with the wrong text, a page with only a footer. Record one entry per page in `pdf_clipping`: `{page, clipped (bool), note (one short sentence of what you saw; words only: no figure, name or account number)}`. If a page is clipped, fix the component and re-render, then read again; record the final render only.
5. **Record** `RENDER_FIX.json` in your folder with exactly: `sample_sha256` (of the real sample file, unchanged); `outputs` {`tab_html`, `export_html`, `export_pdf`, `fixture_html`: each `{path, sha256, bytes}` of the file in the private folder}; `max_reason_repeats` (the largest count of one distinct absent reason in the export HTML, as you count it); `charts` (one entry per chart member id of the contract, the four whose id contains `.chart.`: `{id, drew (bool), absent_words (bool)}`); `fixture_svg_count` (the number of `<svg` in the fixture export HTML); `export_pdf_pages` and `pdf_pages_read` (both the PDF's page count); `pdf_clipping`; `fee_basis_label_present` true; `no_zero_for_absent` true; `portal` {`branch` "wk-IRPT_DASHBD-152-portal", `commit` (the last portal commit, 7 to 40 hex), `files_changed` (every portal file you changed, repo-relative to the portal, each under `src/pages/InvestorReporting/`)}; `harness_sha256` (of your folder's `render_sample.ts`); `tests` {`new_file`, `mutant_failed` true, `lint_errors`, `typecheck_errors`, `suite_base` and `suite_after` as {pass, skip, fail, new_failing_ids}}; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, paths, hashes and words only: no client name, account number or figure, no run of eight or more digits (a path, commit or file value under a key named `path`, `commit` or `file` is exempt).

<criterion id="DB101-1-AC1" cell_refs="DB-b-187"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r101/p101_round101.py" . DB101-1-AC1</invocation><expect>DB101-1-AC1 PASS</expect></criterion>
`DB101-1-AC1` -- the record is bound to the unchanged real sample; the four outputs sit in the private folder (never the repo), hash as recorded, and the tab and export HTML each carry all 117 member ids; no distinct absent reason of 40 or more characters prints more than 8 times in either HTML; an "As of" footer carries the household's as-of date and none reads "Not available"; each of the four chart slots drew or said why, agreeing with the HTML, and the fixture export draws at least one `<svg`; the PDF's page count equals pages read and every page has a clipping entry; the portal commit exists on the portal repository and only files under src/pages/InvestorReporting/ changed; no write, push or deploy; no run of 8 or more digits. Base: FAIL (no record).

<expected_criteria>DB101-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including `~146/render_sample.ts`, the contract, the real sample and every portal file outside the two component directories.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change. A dev server only if you need a screenshot of your own, on a port other than 5174, from your worktree, stopped when you finish.
- **Client data.** The real sample and every render of it live ONLY under `C:/dev/_irpt_private_evidence_20261009/`. Nothing of it goes in the repo, a row, a message or your report: counts, hashes and words only. The fixture is synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. Never weaken an assertion of an existing test beyond the minimum edit that the new behaviour requires, and name each such edit. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W152-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~152/
portal/src/pages/InvestorReporting/dashboard/report/
portal/src/pages/InvestorReporting/render/performance/report/
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-187.report-render-defects-fixed-and-real-sample-re-rendered.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 103 (round 101), cell `DB-b-187`.
<owned_cells>DB-b-187</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB101-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~152/IRPT_DASHBD.TO-DB-b-187.report-render-defects-fixed-and-real-sample-re-rendered.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB101-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the files you changed and what each change does (one clause each); the worst reason-repeat count before and after; the footer text form; for each chart slot drew or words; the PDF's page count and the pages you found clipped (or none); lint, typecheck and the suite before and after; any row ids. Counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: DEV-only portal component edits and a local render; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record) and is dry-run on 12 synthetic arms.
lane: the <paths> block IS the grant.
</preflight>

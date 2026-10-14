# TO IRPT_DASHBD.TO-DB-b-197 -- the RENDER CELL, J1's remedy: a class the household does not hold prints the baseline's dash, every kind note names its figure, a chart title says what the chart draws, the before-fee line prints only when its member is present; the 49 Financial report re-rendered and every PDF page read as an image

<to_id>IRPT_DASHBD.TO-DB-b-197</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~162</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>104</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-104 ANALYSIS item 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_104_20261014.md`; the CVO graded round 103's DB103-1-J1 FAIL on its wording clause: ADJUDICATION_v63) and rulings on rows W158-S4 and W158-S6 | **Rows:** IRPT_DASHBD-D2-W162-S<k> | **Decomp cell:** `DB-b-197` (decomposition section 106) | **outcome_ref:** FWD-21 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-162` (branch `wk-IRPT_DASHBD-162`); run everything from its root unless a step says the portal. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~162/`. `C:/dev/wk-irpt-dashbd-162/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-162-portal`), cut from the branch that carries the round-103 components (percent scale fixed, client-safe wording, omissions, firm title). Do not amend or revert anything already committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours.

**Why.** The previous round's render fix passed its checks, and the CVO graded its judgment criterion FAIL on wording, orientation MET: (1) a class the household does not hold (for example alternatives or commodities) prints "Not available yet" where the baseline prints a dash, which tells a client a figure is missing when the truth is that they hold none; (2) the kind notes ("This figure needs more history than is available yet.") print with no referent, so a client cannot tell which figure they mean; (3) a chart is titled "Household performance, last 12 months, with benchmark lines" but draws only the four model benchmark lines (the household series is absent), so the title claims a line it does not draw; (4) a fixed "Returns and gains are before advisory fees." line prints while the member that carries the fee basis (`convention.fee_basis_label`) is absent.

**The cell (`DB-b-197`).**
1. **Read first.** The round-103 components: `portal/src/pages/InvestorReporting/dashboard/report/` and `portal/src/pages/InvestorReporting/render/performance/report/` (`reportModel.ts`, `PerformanceReport.tsx`, `PerformanceReportDocument.tsx`, `documentSheets.ts`, `ReportChart.tsx`, the kind-note table), their tests under `portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/`, the CVO's adjudication (`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/` newest `ADJUDICATION_v63.md`: read the J1 row), the previous cell's rows `W158-S1` to `W158-S7` in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md`, the contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` (member `label`s), the baseline schema `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/BD_FINANCIAL_PERFORMANCE_REPORT_BASELINE_SCHEMA_20261013.md` (how it prints a class with no holding, and where it states the fee basis), and your predecessor's render harness `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~158/render_sample.ts` (copy it into YOUR folder; edit your copy only; `~158/README`-style run notes are in `~146/README.txt`). Run the whole-scope suite once before any edit (`bun test src/pages/InvestorReporting` from the portal, output under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~162/`) as your base.
2. **An unheld class prints the baseline's dash.** In the filled sample the builder marks a class the household does not hold with the absent form whose reason begins `no holding in this asset class on as_of`. The kind of an absence is NOT yet a field (the CTO has ruled it becomes `absent_kind` after a proposal this round; no code may read that field yet), so for THIS cell recognise an unheld entry in ONE function (`isUnheldEntry`) that tests that one fixed phrase and carries a comment that the function is replaced by the `absent_kind` field when the proposal is accepted. The cell for an unheld class then prints the baseline's dash (an en dash), written ASCII-safe in source (the HTML entity `&ndash;` or the escape `\u2013`, never a literal non-ASCII character), in the tab and the export. It never prints "Not available yet" and never `0`. The technical reason stays only as a `data-reason` attribute; the unheld-class reason text must not be visible.
3. **A kind note names its figure.** Every client-facing note that says a figure is unavailable names the figure in plain words (the figure's label as a client reads it, for example "Net gain, last 12 months: needs more history than is available yet."), in the form "<figure>: <plain sentence>". The three bare sentences of the previous round ("This figure needs more history than is available yet.", "This figure is not available yet.", "This figure does not apply.") must not appear. Record each kind's printed example in `kind_notes` as `{kind, example (the exact sentence as printed in the export), names_figure true}`. Where several figures of a section share one kind, one note may name them in a short list.
4. **A chart title says what it draws.** Derive each chart's title from the series it draws: when a series named for the household exists in the data, the title may say household; otherwise it names what is drawn (for example "Opal model benchmark returns, last 12 months"). For the real sample the 12-month chart draws only the four model benchmark series, so it must not say household. Record the printed title in `chart_titles` under the chart's member id (`overview.chart.portfolio_performance_last_12_months`).
5. **The before-fee line follows its member.** Print "Returns and gains are before advisory fees." (or the baseline's fee-basis wording) ONLY where its member (`convention.fee_basis_label`) is present; while it is absent, the section says so once through the absent wording (a figure-naming note), and the fixed sentence is not printed. In the filled sample that member is absent, so the sentence must not appear; set `fee_line_follows_member` true when the component implements the rule. (The round-103 checker required the sentence; this round's does not.)
6. **Tests and gates.** A new test file `report-render-r104.test.tsx` under `portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/` pins each of the four rules (a dash for an unheld class and never "Not available yet"; a note that names its figure and none of the three bare sentences; a chart title that does not say household when no household series exists; no fee sentence while its member is absent), plus the minimum edits to existing assertions that pinned the old wording (name each). ONE temporary mutant (print the unheld class as "Not available yet" again) that a test catches, then reverted. `bun run lint` and `bun run typecheck` after your last portal commit (0 errors); the whole-scope suite after (`new_failing_ids` []).
7. **Re-render and read.** Render the benchmark-filled sample `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~159/HOUSEHOLD_SAMPLE.json` (client data, read-only, sha256 `25446cfc9b987a97aa54cb91ecfb5212983ace90fbb823173cde6a3eadea1301`) into the NEW private folder `C:/dev/_irpt_private_evidence_20261009/fwd21_sample_r104/` (three outputs: `FWD21_TAB_49F_SAMPLE.html`, `FWD21_EXPORT_49F_SAMPLE.html`, `FWD21_EXPORT_49F_SAMPLE.pdf`; the harness's run notes are in `~146/README.txt`; the render can take a few minutes: run it in the background and wait for its summary). The Read tool refuses a PDF: rasterise it with `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/tools/pdf_to_png.py <abs PDF> <abs NEW folder under fwd21_sample_r104/pages/> 70` and open EVERY `page_NN.png` with the Read tool. Look at each page for clipped text, a dash where a figure belongs, a bare note, a chart title that overclaims, a stray build phrase. Each sheet must fit one PDF page ("Page n of N" equals the PDF's page count). Fix and re-render until clean; record the final render only.
8. **Record** `RENDER_FIX_R104.json` in your folder with exactly: `sample_sha256`; `outputs` {`tab_html`, `export_html`, `export_pdf`: each `{path, sha256, bytes}`}; `unheld_cells` (the number of unheld-class entries of the sample, which the checker counts: 3 today); `dash_source_form` (words, ASCII only: which entity or escape the components use); `kind_notes`; `chart_titles`; `fee_line_follows_member` true; `export_pdf_pages` and `pdf_pages_read` (both the final PDF's page count); `pdf_clipping` (one `{page, clipped, note}` per page; note = one plain sentence, no figure, name or account number); `portal` {`branch` "wk-IRPT_DASHBD-162-portal", `commit`, `files_changed` (each under `src/pages/InvestorReporting/`)}; `harness_sha256`; `tests` {`new_file`, `mutant_failed` true, `lint_errors`, `typecheck_errors`, `suite_base` and `suite_after` as {pass, skip, fail, new_failing_ids}}; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, paths, hashes and words only: no client name, account number or figure.

<criterion id="DB104-1-AC1" cell_refs="DB-b-197"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r104/p104_round104.py" . DB104-1-AC1</invocation><expect>DB104-1-AC1 PASS</expect></criterion>
`DB104-1-AC1` -- bound to the round-103 benchmark sample; the three outputs in the private folder with all 117 member ids in each HTML; every stored percent prints at its stored scale; no build word, snake_case identifier, code or ALL_CAPS token in the visible text; the registry's firm title and never "Sample Firm"; the unheld-class reason text is not visible and the baseline's dash (an en dash) prints in at least as many cells as the sample has unheld entries; none of the three bare kind sentences appears and each recorded kind note's example is in the export; the 12-month chart's printed title names a household line only when the sample carries one; the before-fee sentence is absent while its member is absent; an "As of" footer; the PDF's page count equals pages read with a clipping entry per page and none clipped; the portal commit exists and only files under src/pages/InvestorReporting/ changed; a failing mutant, lint 0, typecheck 0, no new failing test; no write, push or deploy. Base: FAIL (no record).
<criterion id="DB104-1-J1" cell_refs="DB-b-197" judgment="true"/>
`DB104-1-J1` (JUDGMENT, the CVO's at L9, never the worker's or the issuer's) -- re-grade of round 103's J1: every client-facing line that says a figure is unavailable or not held reads as plain words a client understands and cannot misinform, and the holdings table stays in the baseline's orientation.

<expected_criteria>DB104-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the contract, the sample, `~158/render_sample.ts`, `firmDisplayNames.generated.ts` (generated) and every portal file outside the two component directories and the tests directory.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change.
- **Client data.** The sample and every render live ONLY under `C:/dev/_irpt_private_evidence_20261009/`. Nothing of it goes in the repo, a row, a message or your report: counts, hashes and words only.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. Never weaken an assertion of an existing test beyond the minimum edit the new behaviour requires, and name each such edit. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W162-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~162/
portal/src/pages/InvestorReporting/dashboard/report/
portal/src/pages/InvestorReporting/render/performance/report/
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-197.render-j1-remedy-dash-for-unheld-notes-name-figures-honest-chart-title.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 106 (round 104), cell `DB-b-197`.
<owned_cells>DB-b-197</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB104-1-AC1 (mechanical), DB104-1-J1 (judgment: the CVO's; leave it out of the instance, the validator refuses a judgment row). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~162/IRPT_DASHBD.TO-DB-b-197.render-j1-remedy-dash-for-unheld-notes-name-figures-honest-chart-title.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB104-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; how an unheld class is recognised and printed; the kind notes (kind and printed example); each chart's printed title; how the before-fee line follows its member; the PDF's page count and the pages you found clipped (or none); lint, typecheck and the suite before and after; any row ids. Counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: DEV-only portal component edits and a local render; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB104-1-AC1 FAILS at base (no record) and is dry-run on 10 synthetic arms; DB104-1-J1 is the CVO's.
lane: the <paths> block IS the grant.
</preflight>

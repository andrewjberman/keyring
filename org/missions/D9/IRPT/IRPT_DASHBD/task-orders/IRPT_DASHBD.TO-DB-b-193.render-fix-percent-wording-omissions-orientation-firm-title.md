# TO IRPT_DASHBD.TO-DB-b-193 -- the RENDER FIX: percents print at their stored scale, no build language on any client-facing line, every omitted chart or row said in words, the holdings table in the baseline's orientation, the header's firm title from the registry; the 49 Financial sample re-rendered and every PDF page read as an image

<to_id>IRPT_DASHBD.TO-DB-b-193</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~158</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>103</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-102 ANALYSIS item 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_102_20261014.md`; rulings 7508 and the CVO's L9 note) | **Rows:** IRPT_DASHBD-D2-W158-S<k> | **Decomp cell:** `DB-b-193` (decomposition section 105) | **outcome_ref:** FWD-21 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-158` (branch `wk-IRPT_DASHBD-158`); run everything from its root unless a step says the portal. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~158/`. `C:/dev/wk-irpt-dashbd-158/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-158-portal`), cut from the branch that carries the FIXED report components (the tab and the export document, after the previous round's fixes). Do not amend or revert anything already committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours.

**Why.** FWD-21's default performance report is read by clients, and the previous round's section check (a seat other than the builders, graded PASS at L9) found these defects in the 49 Financial render, three of them client-visible:
1. **A wrong figure.** A stored percent such as `1.5` (meaning 1.5 percent) prints as `150.0%`: the account return rows print at 100 times their stored scale. Sample values: the filled sample stores percents already as percent numbers rounded to 1 dp ("the decimal fraction times 100", the builder's own header), so the component must NOT multiply again.
2. **Build language on client-facing lines.** The "Not available yet" notes name tables, contracts, siblings, builders, rulings and gold tables (for example "history not yet built: gold account_activity_daily holds 4 trading days"). A client must never read that.
3. **Silent omissions.** Baseline elements the contract has no member for (the account-grain charts, the per-account class rows) print nothing and no note.
4. **The holdings table is transposed** and its class hierarchy is not drawn (the baseline's Holdings Overview orients differently).
5. **The page header prints the placeholder "Sample Firm"** (the harness's neutral label) instead of the firm's own title.

**The cell (`DB-b-193`).**
1. **Read first.** `portal/src/pages/InvestorReporting/dashboard/report/` (`reportModel.ts`, `PerformanceReport.tsx`, `ReportChart.tsx`, `contractMembers.ts`, `fixtures/`), `portal/src/pages/InvestorReporting/render/performance/report/` (`PerformanceReportDocument.tsx`, `documentSheets.ts`), `portal/src/pages/InvestorReporting/header/firmDisplayNames.generated.ts` (the firm titles, GENERATED from the firm registry: a firm's title is read from it, never typed), the contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` (member `unit` values: `percent`, `dollars`, `series`, `text`), the baseline schema `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/BD_FINANCIAL_PERFORMANCE_REPORT_BASELINE_SCHEMA_20261013.md`, the previous seats' records (`~152/RENDER_FIX.json`, `~156/SECTION_CHECK.json` and rows `W156-S2` to `W156-S6` in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md`), and the render harness `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~152/render_sample.ts` (copy it into YOUR folder; edit your copy only). Run the whole-scope suite once before any edit (`bun test src/pages/InvestorReporting` from the portal, output to a file under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~158/`) as your base.
2. **Percent scale.** Find where a percent member is formatted and stop the second multiplication. Add a test (a new file `report-render-r103.test.tsx` under `portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/`) that pins a stored `1.5` to print `1.5%` in BOTH the tab and the export (name it in the record as `tests.percent_pin_test`), and fix any existing assertion that pinned the old behaviour (name each).
3. **Client-safe wording.** Every client-facing line that says a figure is unavailable reads plain words a client understands and names no table, file, contract, table, ruling, builder, pipeline or tool. The cell's cells read "Not available yet". A section or table note may add ONE plain sentence chosen from a SMALL FIXED TABLE keyed on the kind of absence (for example: history too short for the period, "This figure needs more history than is available yet."; a source not yet connected, "This figure is not available yet."; a figure that does not apply). The technical reason from the sample is kept for internal diagnostics ONLY as a `data-reason` attribute on the element (an attribute is not visible text) and never printed. A reason whose kind you cannot tell prints only "Not available yet". The checker strips tags, scripts and styles from the HTML and then refuses, in the visible text of BOTH the tab and the export: the words contract, contracts, sibling, siblings, gold, parquet, schema, ruling, issuer, builder, adapter, pipeline, silver, bronze, baseline (whole words, any case); any snake_case identifier (`word_word`); any `C-ABC` code; any ALL_CAPS_WITH_UNDERSCORES token. Add a test that renders the real-shaped fixture with a technical reason and asserts none of those appears in the visible text. Never print `0` for an absent figure; the fee basis stays labeled.
4. **Omissions in words.** For every baseline chart or table the contract has no member for (read the baseline schema against the contract: at least the account-grain charts and the per-account class rows), print one short plain sentence at its place ("Account allocation chart: not available yet.") so that nothing is dropped silently. List each in the record's `omissions` as `{element, words}` where `words` is the exact sentence printed in the export (the checker finds it in the export text).
5. **The holdings table in the baseline's orientation.** Read the baseline schema's Holdings Overview (which is the row axis and which the column axis; whether the class hierarchy is drawn) and lay the table out that way in BOTH the tab and the export, from the same view model. State in your report what the baseline's orientation is and what you changed. This is graded by the CVO (judgment criterion DB103-1-J1), not by the checker.
6. **The header's firm title.** Replace the harness's neutral "Sample Firm" and any hard-coded name with the firm's title read from `FIRM_DISPLAY_NAMES` (the generated map): the components take the firm id (or title) as an input, the harness passes `49financial`, and no firm name is typed in a component. The page header prints "<firm title> Performance Report" or the baseline's header form; the checker finds the registry title `49 Financial` and refuses `Sample Firm`.
7. **Re-render and read.** Using your copy of the harness, render the filled sample `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~154/HOUSEHOLD_SAMPLE.json` (client data, read-only, sha256 `c8075558c155ebc5034127dc4abf03c8391b31d63fbdac0b32737b533535bd71`) into the NEW private folder `C:/dev/_irpt_private_evidence_20261009/fwd21_sample_r103/` (three outputs: `FWD21_TAB_49F_SAMPLE.html`, `FWD21_EXPORT_49F_SAMPLE.html`, `FWD21_EXPORT_49F_SAMPLE.pdf`; follow `~146/README.txt` for the run). The Read tool refuses a PDF: rasterise it with `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/tools/pdf_to_png.py <abs PDF> <abs NEW folder under fwd21_sample_r103/pages/> 70` and open EVERY `page_NN.png` with the Read tool. Look at each page for clipped text, overflow into the footer, overlapping lines, a wrong footer, a stray build phrase, and the holdings table. Each sheet must fit one PDF page ("Page n of N" equals the PDF's page count). Fix and re-render until clean; record the final render only.
8. **Gates.** `bun run lint` and `bun run typecheck` after your last portal commit (0 errors); the whole-scope suite after (`new_failing_ids` []); ONE temporary mutant (restore the double multiplication) that a test catches, then reverted.
9. **Record** `RENDER_FIX_R103.json` in your folder with exactly: `sample_sha256`; `outputs` {`tab_html`, `export_html`, `export_pdf`: each `{path, sha256, bytes}`}; `percent_check` {`stored_figures_found` (the number of distinct stored percent figures of the sample that print at their stored scale in the export), `scaled_figures_found` 0}; `banned_words_found` 0; `omissions`; `firm_title` {`source` "firm_registry", `text` "49 Financial", `hard_coded` false}; `export_pdf_pages` and `pdf_pages_read` (both the final PDF's page count); `pdf_clipping` (one `{page, clipped, note}` per page; note = one plain sentence, no figure, name or account number); `portal` {`branch` "wk-IRPT_DASHBD-158-portal", `commit` (the last portal commit), `files_changed` (each under `src/pages/InvestorReporting/`)}; `harness_sha256` (of your folder's `render_sample.ts`); `tests` {`new_file`, `percent_pin_test`, `mutant_failed` true, `lint_errors`, `typecheck_errors`, `suite_base` and `suite_after` as {pass, skip, fail, new_failing_ids}}; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, paths, hashes and words only: no client name, account number or figure, no run of eight or more digits (a value under a key named `path`, `commit`, `file` or `key` is exempt).

<criterion id="DB103-1-AC1" cell_refs="DB-b-193"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r103/p103_round103.py" . DB103-1-AC1</invocation><expect>DB103-1-AC1 PASS</expect></criterion>
`DB103-1-AC1` -- bound to the round-101 filled sample; the three outputs in the private folder (never the repo) with all 117 member ids in each HTML; every stored percent figure of the sample prints at its stored scale in both HTMLs and none at 100 times; no build word, snake_case identifier, code or ALL_CAPS token in the visible text of either HTML; each recorded omission's words appear in the export; the header prints the registry's firm title and never "Sample Firm"; an "As of" footer carries the household's as-of date; the PDF's page count equals pages read with a clipping entry per page and none clipped; the portal commit exists and only files under src/pages/InvestorReporting/ changed; a percent-pin test, a failing mutant, lint 0, typecheck 0, no new failing test; no write, push or deploy; no run of 8 or more digits. Base: FAIL (no record).
<criterion id="DB103-1-J1" cell_refs="DB-b-193" judgment="true"/>
`DB103-1-J1` (JUDGMENT, the CVO's at L9, never the worker's or the issuer's) -- the holdings table is in the baseline's orientation with its class hierarchy as the baseline draws it, in tab and export; and every client-facing unavailable-figure line reads as plain words a client would understand.

<expected_criteria>DB103-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the contract, the sample, `~152/render_sample.ts`, `firmDisplayNames.generated.ts` (generated: never edit it by hand) and every portal file outside the two component directories and the tests directory.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change.
- **Client data.** The sample and every render live ONLY under `C:/dev/_irpt_private_evidence_20261009/`. Nothing of it goes in the repo, a row, a message or your report: counts, hashes and words only. A fixture is synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. Never weaken an assertion of an existing test beyond the minimum edit the new behaviour requires, and name each such edit. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W158-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~158/
portal/src/pages/InvestorReporting/dashboard/report/
portal/src/pages/InvestorReporting/render/performance/report/
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-193.render-fix-percent-wording-omissions-orientation-firm-title.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 105 (round 103), cell `DB-b-193`.
<owned_cells>DB-b-193</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB103-1-AC1 (mechanical), DB103-1-J1 (judgment: the CVO's; leave it out of the instance, the validator refuses a judgment row). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~158/IRPT_DASHBD.TO-DB-b-193.render-fix-percent-wording-omissions-orientation-firm-title.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB103-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the cause of the percent error and the fix; the client-safe wording table (the kinds and the sentences); the omissions you added; the baseline's holdings orientation and what you changed; where the firm title comes from; the PDF's page count and the pages you found clipped (or none); lint, typecheck and the suite before and after; any row ids. Counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: DEV-only portal component edits and a local render; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB103-1-AC1 FAILS at base (no record) and is dry-run on 11 synthetic arms; DB103-1-J1 is the CVO's.
lane: the <paths> block IS the grant.
</preflight>

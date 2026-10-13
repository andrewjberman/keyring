# TO IRPT_DASHBD.TO-DB-b-177 -- the export document renders the same performance report from the same contract shape, in the same eight sections in the same order, every member present, an unavailable figure said in words, the fee basis labeled -- NEW files only; a DEV-only portal candidate

<to_id>IRPT_DASHBD.TO-DB-b-177</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~143</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>94</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msgs 7181 and 7192, ROUND-94 ANALYSIS item 3 (PRD v0.14, FWD-21) | **Rows:** NONE | **Decomp cell:** `DB-b-177` (decomposition section 96) | **outcome_ref:** FWD-21 | **depends_on:** DB-b-176 (the tab and its shared view model; this order is spawned after it drains).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-143` (branch `wk-IRPT_DASHBD-143`); run everything from its root unless a step says the portal. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~143/`. Screenshots go in that folder.

**Two repos.** `C:/dev/wk-irpt-dashbd-143/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-143-portal`) at portal DEV. Do not amend or revert anything committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink.
`node_modules` here is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours. ONE whole-scope run before any edit (`bun test src/pages/InvestorReporting`, output to a file under
`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~143/`) is your base for `new_failing_ids`.

**Why.** FWD-21: the default performance report is the SAME report on the Performance tab and as the export, in one Opal Shape. The previous cell built the tab's half: `portal/src/pages/InvestorReporting/dashboard/report/` (`reportModel.ts` turns a filled report into the ordered sections and members; `PerformanceReport` renders them; the synthetic fixture is `fixtures/syntheticReport.ts`; its record is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~142/TAB_RENDER.json`). Read all of it first, with the contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` and the baseline schema `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/BD_FINANCIAL_PERFORMANCE_REPORT_BASELINE_SCHEMA_20261013.md` (page footers, "As of <date>", "Page n of N", the disclosure page). The export document goes through the portal's existing print render: read
`render/Page.tsx`, `render/PrintEntry.tsx`, `render/print.css`, `render/performance/PerformanceDocument.tsx` (the current performance document; read, do not edit) and `export/ExportModal.tsx` (read, do not edit).

**The cell (`DB-b-177`).** NEW files only, under `portal/src/pages/InvestorReporting/render/performance/report/` (create it), no edit of any existing file (including the previous cell's files).
1. **The document.** `PerformanceReportDocument` (and the pieces it needs) renders the SAME eight sections, in the same order, from the same view model (import `reportModel.ts` by its path; do not copy it), laid out for print through the portal's existing page primitives: the baseline's footer on every page ("<household or account> Performance Report", "As of <date>", "Page n of N"), the disclosure page last, and the line "This report is incomplete without the accompanying disclosure page" where the baseline has it.
   Every member appears in the document with a `data-member="<id>"` attribute. A figure the shape marks absent prints words ("Not available yet: <reason>"), never blank, never 0. The fee basis is labeled wherever net gain or return shows. The layout never branches on the firm or on which vendor fed the data.
2. **The test.** In `portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/report-export.test.tsx`, against the previous cell's synthetic fixture: (a) the eight section headings appear in the baseline's order and equal `~142/TAB_RENDER.json` `sections_rendered_in_order`; (b) all 117 member ids appear; (c) an absent member prints its reason in words and no `0`; (d) the fee-basis label appears; (e) the footer text carries the as-of date and a page number. ONE temporary mutant (swap two sections, or print an absent cell blank) that the test catches, then reverted.
3. **Gates.** `bun run lint` and `bun run typecheck` after your last portal commit (both 0 errors); the whole-scope suite after (`new_failing_ids` []). A screenshot of the document rendered from the fixture (a dev server from YOUR worktree on a port other than 5174, or the print entry in a test harness of your own under your grant; stop it when you finish), read by you.
4. **Record** `EXPORT_RENDER.json` in your folder, exactly these keys: `contract_sha256`; `sections_rendered_in_order` (the eight ids as rendered); `sections_match_tab_record` true; `absent_rendered_in_words` true; `fee_basis_label_present` true; `no_blank_figure` true; `same_layout_for_every_firm` true; `members_rendered` (equal to the contract's member count); `test` {`file`, `mutant_failed` true}; `lint_errors`; `typecheck_errors`; `suite_base` and `suite_after` {`pass`, `skip`, `fail`, `new_failing_ids`};
   `product_files_changed` (product files only); `portal_commit` (40 hex); `synthetic_fixture_only` true; `pushed` false; `screenshots`; `screenshot_read` true. No real name, account or figure.

<criterion id="DB94-4-AC1" cell_refs="DB-b-177"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r94/p94_round94.py" . DB94-4-AC1</invocation><expect>DB94-4-AC1 PASS</expect></criterion>
`DB94-4-AC1` -- the record is bound to the contract's bytes; the document renders the eight sections in the baseline's order, equal to the tab's; every member renders; an unavailable figure is said in words; the fee basis is labeled; the layout is the same for every firm; a test and a mutant hold it; lint and typecheck read 0; the suite is no worse; every product file is under `render/performance/report/`; synthetic data only; nothing pushed; a screenshot was read. Base: FAIL (no record).

<expected_criteria>DB94-4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every existing portal file, the previous cell's files and the contract.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change. A dev server only for your own screenshot, on a port other than 5174, from your worktree, stopped when you finish. The wiring of `PerformanceReportDocument` into `ExportModal` and the print entry is the issuer's hookup at the merge: edit no existing file; name the hookup you need in your report.
- **Synthetic data only** in any fixture, screenshot or record.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. Never weaken an assertion of an existing test. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W143-S<k>`, with the real current UTC time; append as BYTES, never re-encode the existing content. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~143/
portal/src/pages/InvestorReporting/render/performance/report/
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/report-export.*
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-177.export-document-renders-the-report-shape.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 96 (round 94), cell `DB-b-177`.
<owned_cells>DB-b-177</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB94-4-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~143/IRPT_DASHBD.TO-DB-b-177.export-document-renders-the-report-shape.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB94-4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the files you added and what each exports; the hookup the issuer must add to wire the document into the export (file and line, one clause); the test and its mutant; lint, typecheck and the suite before and after; what the screenshot shows; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; new DEV-only portal files, not wired until the issuer's hookup; the candidate is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record; 60 synthetic arms dry-run).
lane: the <paths> block IS the grant.
</preflight>

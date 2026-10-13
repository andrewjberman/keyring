# TO IRPT_DASHBD.TO-DB-b-180 -- render the REAL 49 Financial household sample through the tab and export components into a local HTML and a local PDF in the private folder, never in the repo: absent figures said in words, the fee basis labeled; for Andrew's read

<to_id>IRPT_DASHBD.TO-DB-b-180</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~146</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>96</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 7349 (Andrew asked to see "a sample display ... as a baseline format") | **Rows:** NONE | **Decomp cell:** `DB-b-180` (decomposition section 98) | **outcome_ref:** FWD-21 | **depends_on:** DB-b-175 (the sample), DB-b-176 and DB-b-177 (the components), all drained.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-146` (branch `wk-IRPT_DASHBD-146`); run everything from its root unless a step says the portal. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~146/`. Your portal worktree is `C:/dev/wk-irpt-dashbd-146/portal` (branch `wk-IRPT_DASHBD-146-portal`), cut from the export-document candidate `091ae64e95`, which already holds BOTH new component sets.

**Two repos.** Portal files commit in the portal repo with plain git and an explicit author line; records and rows commit in the workspace with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink; `node_modules` here is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`.

**Why.** Andrew asked to see a sample display of the default performance report. The previous cells built the contract (`org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json`), one real 49 Financial household filled into its shape (a PRIVATE file `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~141/HOUSEHOLD_SAMPLE.json`, 3 accounts, 44 of 117 members filled, the rest absent in words) and two sets of components that render it: the tab (`portal/src/pages/InvestorReporting/dashboard/report/`: `reportModel.ts`, `PerformanceReport.tsx`, `ReportChart.tsx`) and the export document (`portal/src/pages/InvestorReporting/render/performance/report/`: `documentSheets.ts`, `PerformanceReportDocument.tsx`). Nothing mounts them in the product yet, so nobody can see the real thing.
You render it, locally, for him. The output is CLIENT DATA: it goes ONLY to the private folder `C:/dev/_irpt_private_evidence_20261009/fwd21_sample/` (create it) and never into either repo.

**The cell (`DB-b-180`).**
1. **Read first.** The two component sets and their tests; the previous workers' records (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~142/TAB_RENDER.json`, `~143/EXPORT_RENDER.json`, `~141/HOUSEHOLD_SAMPLE_BUILD.json`) and how worker 142 produced `~142/tab_render.html` from a SYNTHETIC fixture (inline styles, `renderToStaticMarkup`, a headless Edge for a screenshot; `GEN_REPORT.py` is the generator of the member list, not of the HTML). The sample file's shape is the contract's `document` layout.
2. **The harness.** ONE tracked script in your folder (`render_sample.tsx` or `.ts`, ASCII, plus a short `README.txt` of how to run it) that, run with bun from your portal worktree, reads the private sample file by an absolute path given as an argument, builds the report model (`buildReportModel`), and writes three files to `C:/dev/_irpt_private_evidence_20261009/fwd21_sample/`:
   - `FWD21_TAB_49F_SAMPLE.html` -- the tab's `PerformanceReport`, self-contained (inline styles; no network, no external font or script), readable on its own in a browser at about 1000 px;
   - `FWD21_EXPORT_49F_SAMPLE.html` -- the export document's `PerformanceReportDocument`, laid out as printed sheets (the paper size the document defines), self-contained;
   - `FWD21_EXPORT_49F_SAMPLE.pdf` -- that export HTML printed to PDF with headless Edge (`C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe --headless --disable-gpu --no-pdf-header-footer --print-to-pdf=<path> file:///<html path>`; background graphics on if the document needs them), every sheet present, the footers and the disclosure page last.
   The report must show, in the files themselves: every member id present as `data-member="<id>"` (117), each absent figure as the words "Not available yet: <reason>" (never blank, never 0), and the fee-basis label ("before advisory fees"). Do NOT add a household name, an account number or any identifying text that the sample does not already carry (the contract marks the cover's name and masked numbers ABSENT: print them as ABSENT in words, as the model does). Do not edit any component; if a component cannot render the real sample, file a surprise row with the exact error and stop (the issuer decides).
3. **Look at it.** Open the tab HTML and the PDF yourself (headless Edge screenshots into the PRIVATE folder, then read them) and say in your report, in words and counts, what you saw: the section headings in order, how many sheets the PDF has, whether a chart rendered or printed its words, whether any text is clipped or overflows. A defect in the display itself (clipping, a chart that draws nothing, a table that runs off the sheet) is a finding for the report and a row, not something you hide.
4. **Record** `SAMPLE_RENDER.json` in your folder with exactly these keys: `sample_sha256` (of the private sample file's bytes); `outputs` {`tab_html`, `export_html`, `export_pdf`: each {`path` (the absolute path under the private folder), `bytes`, `sha256`}}; `export_pdf_pages` (the number of pages of the PDF; the checker counts `/Type /Page` objects and compares); `absent_members_in_sample` (the number of members the sample marks absent); `no_zero_for_absent` true; `fee_basis_label_present` true; `synthetic_data_used` false; `code` {`file` (your harness), `sha256` (of its committed bytes), `tracked` true}; `reads` {`vendor_calls` 0, `s3_writes` 0, `secret_reads` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `limits`. Paths and hashes ONLY: no figure, no name, no account id, no run of eight or more digits in the record or in your report.

<criterion id="DB96-1-AC1" cell_refs="DB-b-180"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r96/p96_round96.py" . DB96-1-AC1</invocation><expect>DB96-1-AC1 PASS</expect></criterion>
`DB96-1-AC1` -- the three files exist under the private folder (not in the repo) and their hashes match the record; the record is bound to the private sample's bytes; both HTML files carry all 117 member ids, at least 40 "Not available yet" phrases and the fee-basis label; the PDF is a PDF with at least 8 pages and the stated page count; the absent count equals the sample's; the harness is tracked and hashes to the stated sha256; no vendor call, no S3 write; no run of 8 or more digits in the record. Base: FAIL.

<expected_criteria>DB96-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every existing portal file and both component sets.
- **No deploy, no push, no AWS call, no vendor call, no secret read, no `bun install`, no package change, no portal product edit.** A local dev server only for your own look at the display, on a port other than 5174, from your worktree, stopped when you finish.
- **Client data stays private.** The three outputs, the screenshots and the sample live only under `C:/dev/_irpt_private_evidence_20261009/`. Nothing derived from the sample enters the repo except counts, paths and hashes.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W146-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES, never re-encode the existing content. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything tracked.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~146/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-180.render-the-real-sample-locally-html-and-pdf.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 98 (round 96), cell `DB-b-180`.
<owned_cells>DB-b-180</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB96-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~146/IRPT_DASHBD.TO-DB-b-180.render-the-real-sample-locally-html-and-pdf.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB96-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the three output paths (as plain absolute paths); the PDF page count; what you saw when you looked (headings in order, charts, clipping), in words and counts only; any display defect; any row ids. No figure, name or account.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a local render of a private sample into private files; nothing served, nothing in the product.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS access.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record, no outputs) and is dry-run on 29 synthetic arms.
lane: the <paths> block IS the grant.
</preflight>

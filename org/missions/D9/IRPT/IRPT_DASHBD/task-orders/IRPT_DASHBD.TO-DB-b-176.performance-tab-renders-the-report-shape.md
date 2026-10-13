# TO IRPT_DASHBD.TO-DB-b-176 -- the Performance tab renders the default performance report from the contract shape, in the baseline's eight sections in order, every member present, an unavailable figure said in words, the fee basis labeled, the same layout for every firm -- NEW files only; a DEV-only portal candidate

<to_id>IRPT_DASHBD.TO-DB-b-176</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~142</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>94</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msgs 7181 and 7192, ROUND-94 ANALYSIS item 3 (PRD v0.14, FWD-21) | **Rows:** NONE | **Decomp cell:** `DB-b-176` (decomposition section 96) | **outcome_ref:** FWD-21 | **depends_on:** DB-b-174 (the contract; this order is spawned after it drains).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-142` (branch `wk-IRPT_DASHBD-142`); run everything from its root unless a step says the portal. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~142/`. Screenshots go in that folder.

**Two repos.** `C:/dev/wk-irpt-dashbd-142/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-142-portal`) at portal DEV. Do not amend or revert anything committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink.
`node_modules` here is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours. ONE whole-scope run before any edit (`bun test src/pages/InvestorReporting`, output to a file under
`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~142/`) is your base for `new_failing_ids`.

**Why.** FWD-21: any client at any firm opens ONE default performance report, in one Opal Shape, on the Performance tab and as the export. The contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` (written by the previous cell: read it first, with its `document` layout, its eight `sections` and its 117 `members`) is that shape; the baseline's structure is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/BD_FINANCIAL_PERFORMANCE_REPORT_BASELINE_SCHEMA_20261013.md`. Andrew's read of the sample is the organic arm; this cell is the tab's half of it. Existing neighbours (read, do not edit): `dashboard/DashboardPerformance.tsx`, `dashboard/windowMath.ts`, `render/performance/*`.

**The cell (`DB-b-176`).** NEW files only, under `portal/src/pages/InvestorReporting/dashboard/report/` (create it), no edit of any existing file.
1. **The view model.** `reportModel.ts` turns a filled report (the contract's `document` layout) into an ordered list of the eight sections and, in each, its tables, charts and fields, one entry per contract member, by member id; an `{"absent": "<reason>"}` value stays absent (a flag and its reason), never becomes zero or an empty string. It exports what the export document (the next cell) will import: export it for reuse and keep it free of React.
2. **The components.** A `PerformanceReport` component (and the pieces it needs) renders the eight sections in the baseline's order: cover (household name, the account list, the as-of date), portfolio overview (the allocation-by-class and the 12-month performance charts, the portfolio value summary with its windows and the four model-benchmark rows), summary of portfolio accounts (the allocation-by-account and the ending-value-and-net-additions charts, the activity summary), holdings overview (the class hierarchy
   with its ending value, allocation and per-window net gain and return), taxable realized gain/loss year to date, account overview (per account: charts and the account value summary), gain/loss review by account, and the disclosure page. Every member appears in the DOM with a `data-member="<id>"` attribute. A figure the shape marks absent prints WORDS, for example "Not available yet: <the reason>", never blank, never 0. The fee basis is labeled wherever net gain or return shows ("total return before advisory fees", from the member
   `convention.fee_basis_label`). Inception is per household and per account; a window the account did not exist for prints the "not held for the entire period" note. Charts use the portal's existing chart component or a plain inline SVG you write (find what the portal already uses; add no package); a chart whose series is absent prints words. The layout never branches on the firm or on which vendor fed the data.
3. **The fixture and the tests.** A SYNTHETIC filled report in the contract's layout at `dashboard/report/fixtures/syntheticReport.ts` (made-up names, no real client, account or figure; two firms' variants differing only in the firm word). Tests in `portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/report-tab.test.tsx`: (a) the eight section headings appear in the baseline's order; (b) all 117 `data-member` ids appear; (c) an absent member prints its reason in words and no `0`; (d) the fee-basis label appears; (e) the two firm variants render the same structure. ONE temporary mutant (swap two sections, or print an absent cell blank) that the test catches, then reverted.
4. **Gates.** `bun run lint` and `bun run typecheck` after your last portal commit (both 0 errors); the whole-scope suite after (`new_failing_ids` []). A screenshot of the report rendered from the fixture (start a dev server from YOUR worktree on a port other than 5174, throwaway page or test harness of your own under your grant, stop it when you finish), read by you.
5. **Record** `TAB_RENDER.json` in your folder, exactly these keys: `contract_sha256` (of the contract's bytes); `sections_rendered_in_order` (the eight section ids as rendered); `absent_rendered_in_words` true; `fee_basis_label_present` true; `no_blank_figure` true; `same_layout_for_every_firm` true; `members_rendered` (the number of distinct `data-member` ids in the fixture's render; it must equal the contract's member count); `test` {`file`, `mutant_failed` true}; `lint_errors`; `typecheck_errors`; `suite_base` and `suite_after` {`pass`, `skip`, `fail`, `new_failing_ids`};
   `product_files_changed` (your product files only, not tests); `portal_commit` (40 hex); `synthetic_fixture_only` true; `pushed` false; `screenshots` (files in your folder); `screenshot_read` true. No real name, account or figure anywhere.

<criterion id="DB94-3-AC1" cell_refs="DB-b-176"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r94/p94_round94.py" . DB94-3-AC1</invocation><expect>DB94-3-AC1 PASS</expect></criterion>
`DB94-3-AC1` -- the record is bound to the contract's bytes; the eight sections render in the baseline's order; every one of the contract's members renders; an unavailable figure is said in words; the fee basis is labeled; the layout is the same for every firm; a test and a mutant hold it; lint and typecheck read 0; the suite is no worse; every product file is under `dashboard/report/`; synthetic data only; nothing pushed; a screenshot was read. Base: FAIL (no record).

<expected_criteria>DB94-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every existing file of the portal and the contract.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change. A dev server only for your own screenshot, on a port other than 5174, from your worktree, stopped when you finish. The mount of `PerformanceReport` into the tab is the issuer's hookup at the merge: do not edit `DashboardPerformance.tsx` or any existing file; name the hookup you need in your report.
- **Synthetic data only** in any fixture, screenshot or record.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. Never weaken an assertion of an existing test. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W142-S<k>`, with the real current UTC time; append as BYTES, never re-encode the existing content. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~142/
portal/src/pages/InvestorReporting/dashboard/report/
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/report-tab.*
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-176.performance-tab-renders-the-report-shape.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 96 (round 94), cell `DB-b-176`.
<owned_cells>DB-b-176</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB94-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~142/IRPT_DASHBD.TO-DB-b-176.performance-tab-renders-the-report-shape.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB94-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the files you added and what each exports; the hookup the issuer must add to mount the report (file and line, one clause); the test and its mutant; lint, typecheck and the suite before and after; what the screenshot shows; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; new DEV-only portal files, not mounted until the issuer's hookup; the candidate is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record; 60 synthetic arms dry-run).
lane: the <paths> block IS the grant.
</preflight>

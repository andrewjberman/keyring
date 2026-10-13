# TO IRPT_DASHBD.TO-DB-b-178 -- Andrew's smoke of portal DEV: the Opal report export fails with "status could not be read (UNEXPECTED)" and its modal is too narrow; FDRXX reads Fixed Income and must read CASH; YTD must be measured from the first measured day and labeled -- three portal fixes, a DEV-only candidate to the CTO's review

<to_id>IRPT_DASHBD.TO-DB-b-178</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~144</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>94</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msgs 7139, 7144 and ROUND-94 ANALYSIS item 3 (the smoke fixes fold into the render candidate) | **Rows:** IRPT_DASHBD-D2-S20, S21, S22 (`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md`, search the ids) | **Decomp cell:** `DB-b-178` (decomposition section 96) | **outcome_ref:** FWD-21 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-144` (branch `wk-IRPT_DASHBD-144`); run everything from its root unless a step says the portal. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~144/`. Screenshots go in that folder.

**Two repos.** `C:/dev/wk-irpt-dashbd-144/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-144-portal`) at portal DEV. Do not amend or revert anything committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink.
`node_modules` here is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours. ONE whole-scope run before any edit (`bun test src/pages/InvestorReporting`, output to a file under
`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~144/`) is your base for `new_failing_ids`.

**What Andrew saw (his smoke of portal DEV, Inflection client, Opal report; the CTO's words).** (1) "Opal report export does create but does not export ('The export's status could not be read (UNEXPECTED)...') also the modal is too narrow ... a lot of scrolling side to side." `export/ExportModal.tsx` is identical on PROD and DEV, so this is live on PROD. (2) "FDRXX should be listed as a 'CASH' tagged asset, not Fixed Income." (3) On a 49 Financial client whose history starts 2026-06-03 the selector reads "YTD not measured (the history starts June 3rd, 2026)":
"we should still be able to show YTD with the data from that point and so on." Ruled by the CTO: YTD, and any window reaching back before the history's first day, is measured from the first measured day and labeled with it, for example "YTD (from June 3rd, 2026)"; it is never blank; a window with no measured day at all stays "not measured".

**The cell (`DB-b-178`).** Three fixes, one criterion each in the record. Do NOT touch `portal/src/pages/InvestorReporting/dashboard/report/` or `portal/src/pages/InvestorReporting/render/performance/report/` (other cells' new files).
1. **Export (S20).** Read the export status chain from the click to the failing call, naming each hop (start points: `export/ExportModal.tsx`, `export/submit.ts`, `export/resolveBundle.ts`, `export/ReceiptPanel.tsx`, `export/download.ts`, the contracts under `contracts/`; search the message "could not be read" and the word UNEXPECTED). Name the failing call in `export.failing_call` {file, line}. If the failure is in the portal (a status shape the code does not read, a wrong field, a wrong state transition), FIX it and prove it with a test that fails on the old behaviour (`export.portal_side` true,
   `fixed` true). If the failing call is a backend route or a producer the portal cannot change, change nothing there, file a surprise row naming it (route, file, what it returns) and set `portal_side` false, `fixed` false, `blocking_row` to the row id. Separately WIDEN the modal so its content needs no side scrolling (record the modal's width in pixels before and after, from the style or class you changed; a test asserts the new width and the absence of a horizontal-scroll rule): `export.modal` {`width_px_before`, `width_px_after` (greater), `horizontal_scroll_after` false, `tested` true}.
2. **YTD (S22).** Find where "YTD not measured (the history starts ...)" is decided (start points: `tabs/reporting/pickerSuffix.ts`, `dashboard/DashboardPerformance.tsx`, `dashboard/windowMath.ts`, `dashboard/coverageWords.ts`, `render/performance/PerformanceDocument.tsx`, `render/performance/Summary.tsx`). Make YTD, and any window reaching back before the history's first measured day, measure from that first measured day and carry its label ("YTD (from June 3rd, 2026)"), never blank; a window with NO measured day stays "not measured". Test with SYNTHETIC data (a history starting mid-year, and one with no day in the window), with a mutant (restore the old blank) that the test catches.
   Record `ytd` {`label_example` (the label your test prints, beginning "YTD (from"), `never_blank` true, `no_day_stays_not_measured` true, `test` {`file`, `mutant_failed` true}}.
3. **FDRXX (S21).** Find where an instrument's class is assigned and shown for the report (search the portal first: `comp-find --files 'FDRXX'` has hits in the estate, among them `ticker_overrides.py` under `data/black_diamond/scripts/{gold,silver}/lib` and `data/cot/scripts/gold/lib`; read what a money-market fund's class is in the PORTAL's display path). If the class is assigned or mapped IN THE PORTAL (a label map, a class table, a display fallback), make money-market funds (FDRXX is the case in hand) map to CASH there, with a test and a mutant: `fdrxx` {`assignment_site_in_portal` true, `money_market_maps_to_cash` true, `test` {`mutant_failed` true}}.
   If the class is assigned in a producer or a gold script (outside this DEV-only candidate), change NOTHING there: file a surprise row naming the file and line and what it assigns, and set `fdrxx` {`assignment_site_in_portal` false, `money_market_maps_to_cash` false, `assignment_site` {`file`, `line`}, `blocking_row`}.
4. **Gates.** One whole-scope test file per fix is fine: `portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/smoke-export.test.tsx`, `smoke-ytd.test.tsx`, `smoke-fdrxx.test.tsx`. Re-golden an existing test only where it asserts the OLD behaviour you were ordered to change, say which in the record's `regolden` list, and weaken no other assertion. `bun run lint` and `bun run typecheck` after your last portal commit (0 errors); the whole-scope suite after (`new_failing_ids` []). A screenshot of the widened modal and of a YTD label on synthetic data, read by you (a dev server from YOUR worktree on a port other than 5174; stop it when you finish).
5. **Record** `SMOKE_FIXES.json` in your folder with `export`, `ytd`, `fdrxx` as above and, at the top level: `test` {`file` (the first of your test files), `mutant_failed` true}; `lint_errors`; `typecheck_errors`; `suite_base` and `suite_after` {`pass`, `skip`, `fail`, `new_failing_ids`}; `regolden` (a list, possibly empty); `product_files_changed` (product files only, not tests); `portal_commit` (40 hex); `synthetic_fixture_only` true; `pushed` false; `screenshots` (files in your folder); `screenshot_read` true. No real client name, account or figure anywhere.

<criterion id="DB94-5-AC1" cell_refs="DB-b-178"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r94/p94_round94.py" . DB94-5-AC1</invocation><expect>DB94-5-AC1 PASS</expect></criterion>
`DB94-5-AC1` -- the export status chain is read to a named failing call and either fixed with a test and a mutant (portal side) or named in a row and left (elsewhere); the modal is wider and tested with no horizontal scroll; YTD labels from the first measured day, is never blank, and a window with no measured day stays "not measured", with a mutant; FDRXX maps to CASH in the portal with a mutant, or its class-assignment site is named in a row and left unchanged; lint and typecheck read 0; the suite is no worse; synthetic data only; nothing pushed; a screenshot was read. Base: FAIL (no record).

<expected_criteria>DB94-5-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including `dashboard/report/` and `render/performance/report/` (other cells' new files) and every producer or gold script.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change. A dev server only for your own screenshots, on a port other than 5174, from your worktree, stopped when you finish.
- **Synthetic data only** in any fixture, screenshot or record.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W144-S<k>`, with the real current UTC time; append as BYTES, never re-encode the existing content. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~144/
portal/src/pages/InvestorReporting/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-178.smoke-fixes-export-status-modal-fdrxx-ytd.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 96 (round 94), cell `DB-b-178`.
<owned_cells>DB-b-178</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB94-5-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~144/IRPT_DASHBD.TO-DB-b-178.smoke-fixes-export-status-modal-fdrxx-ytd.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB94-5-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the export status chain hop by hop and the failing call; the modal widths; the YTD label; where FDRXX's class is assigned and what you did; the tests and mutants; lint, typecheck and the suite before and after; what the screenshots show; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; three DEV-only portal fixes; the candidate is read by the CTO before DEV, and a PROD push of a client-facing page waits on Andrew.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record; 60 synthetic arms dry-run).
lane: the <paths> block IS the grant.
</preflight>

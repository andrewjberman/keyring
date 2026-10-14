# TO IRPT_DASHBD.TO-DB-b-203 -- the RENDER REMEDY and the VIEW HALF of the absent kind: the view reads `kind` (the keyword inference `absentKindOf` is deleted), an unheld class prints the baseline's dash from the UNHELD value, a note names its figure and its account, template slot names become client words or the line is dropped, an asterisk prints only with its footnote, one sentence per note; the 49 Financial report re-rendered privately and every page read as an image

<to_id>IRPT_DASHBD.TO-DB-b-203</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~167</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>105</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-105 ANALYSIS section 2 cells 1 and 2 (the view half) (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_105_20261014.md`) and the CVO's grade `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_104_L9_GRADE_20261014.md` | **Rows:** IRPT_DASHBD-D2-W167-S<k> (continue your numbering) | **Decomp cell:** `DB-b-203` (decomposition section 107) | **outcome_ref:** FWD-21 | **depends_on:** `DB-b-202` (its sample and its contract 0.4.2).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-167` (branch `wk-IRPT_DASHBD-167`); run everything from its root unless a step says the portal. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~167/`. `C:/dev/wk-irpt-dashbd-167/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-167-portal`), cut from the branch that carries round 104's render (`wk-IRPT_DASHBD-162-portal`: the dash for an unheld class, figure-naming notes, the chart title, the before-fee rule). Do not amend or revert anything already committed there except where this order names it. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours.

**Why.** The CVO graded round 104's judgment criterion FAIL on its first clause, on three counts the CTO accepted: (1) a note says a figure "needs more history" while the same report prints that figure (the data half, your previous order, fills those figures; the view must still never claim a reason the data does not carry); (2) a section note contradicts the table under it (page 8's Account Overview note says the last-12-month return is not available while two of the three accounts print it): the note must name the account it describes or sit beside it; (3) template slot names print as client lines ("Since-inception column heading", "Footnote for a window not held for the entire period", "Class hierarchy", "Accounts, each with its registration name and last four digits"), asterisks point to no footnote, and the notes are long runs joined by semicolons and closed by ": is not available yet". The CTO also ruled that the absent kind is a field the view reads: the keyword inference `absentKindOf` is deleted. The disclosure page and the kind are RELEASE GATES: no rendered report reaches a client, the renders stay in the private folder, and the pointer line "This report is incomplete without the accompanying disclosure page" STAYS exactly as it is.

**The cell (`DB-b-203`).**
1. **Read first.** Your own record `deliverables/0.9.0_WK_IRPT_DASHBD~167/KIND_CARRIER_R105.json` and the sample it names (private; client data, read-only), the contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` at 0.4.2 (`document.absent_kinds`, `unheld_rule`, `absent_rule`; the members' `label`s), the CVO's grade (the file above: read all of it), the issuer's check file `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r105/p105_round105.py` (`check_render` is your criterion: read every clause), the components `portal/src/pages/InvestorReporting/dashboard/report/` and `portal/src/pages/InvestorReporting/render/performance/report/` (`reportModel.ts`, `PerformanceReport.tsx`, `PerformanceReportDocument.tsx`, `documentSheets.ts`, `ReportChart.tsx`, the kind-note table, `isUnheldEntry`, `absentKindOf`), their tests under `portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/`, round 104's render record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~162/RENDER_FIX_R104.json` and its harness `~162/render_sample.ts` (copy the harness into YOUR folder; edit your copy only; run notes are in `~146/README.txt`). Run the whole-scope suite once before any edit (`bun test src/pages/InvestorReporting` from the portal, output under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~167/`) as your base.
2. **The view reads the kind field.** An absent form carries `kind` (`NO_SOURCE_YET`, `INSUFFICIENT_HISTORY`, `SOURCE_BREAK`). The view builds the note from `kind`: delete `absentKindOf` (the keyword inference over reason text) and every caller of it; delete `isUnheldEntry` as well (an unheld class is now the VALUE `UNHELD`). Each kind has its own client words, and the three must read differently (the CVO's example of a true reason: "not split into contributions and withdrawals yet"; for INSUFFICIENT_HISTORY: needs more history than is available yet; for SOURCE_BREAK: not available while its source is being repaired). The reason text stays only as a `data-reason` attribute, never visible. A `by_row` asset-class entry holding the text `UNHELD` prints the baseline's dash (an en dash, ASCII-safe in source: `&ndash;` or `\u2013`, never a literal non-ASCII character), never "Not available yet" and never zero; the text `UNHELD` itself is never visible.
3. **A note names its figure, and its account.** One sentence per note, in the form "<figure>: <plain sentence>" (a figure's label as a client reads it). Where an absent figure belongs to one account (the Account Overview and the per-account pages), the note sits in that account's own section or names it the way the report already names it ("Account ending NNNN"); a section-level note must not describe an account that prints the figure. Where several figures of one section share a kind and an entity, one note may list them in a short phrase joined by "and" or commas, never a run of semicolons, and never closed by ": is not available yet" after a list. A figure is never named as unavailable in a note when the same table row prints it.
4. **Template slot names become client words, or the line is dropped.** For each of the four phrases above, and any other member `label` or slot string that reads as a template instruction rather than as something a client reads (find them by reading the contract members' labels and the rendered pages), print a client word if the member is present, or drop the line while its member is absent. An asterisk (on "Net Gain*", "Return (Cumulative)*" or any label) prints ONLY together with its footnote line; while the footnote's member (`convention.not_held_for_entire_period`) is absent, neither the asterisk nor the footnote prints.
5. **Unchanged, on purpose.** The disclosure pointer line and the disclosure page stay exactly as they are (release gate). The holdings table stays in the baseline's orientation. The percent scale rule, the chart-title rule, the before-fee rule and the registry firm title of round 104 stay.
6. **Tests and gates.** A new test file `report-render-r105.test.tsx` under `portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/` pins each rule (the note words differ by kind and come from the field, a form with a kind and an altered reason prints the same words; an UNHELD entry prints the dash; no note joins figures with semicolons; no template slot phrase prints; an asterisk prints only with its footnote; a per-account note names its account), plus the minimum edits to existing assertions that pinned the old wording or `absentKindOf` (name each; never weaken an assertion beyond the minimum). ONE temporary mutant (the view ignores `kind` and prints one fixed sentence for every kind) that a test catches, then reverted. `bun run lint` and `bun run typecheck` after your last portal commit (0 errors); the whole-scope suite after (`new_failing_ids` []).
7. **Re-render and read.** Render the sample of your previous order (the path is in `KIND_CARRIER_R105.json`) into the NEW private folder `C:/dev/_irpt_private_evidence_20261009/fwd21_sample_r105/` (three outputs: `FWD21_TAB_49F_SAMPLE.html`, `FWD21_EXPORT_49F_SAMPLE.html`, `FWD21_EXPORT_49F_SAMPLE.pdf`; the render can take a few minutes: run it in the background and wait for its summary). The Read tool refuses a PDF: rasterise it with `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/tools/pdf_to_png.py <abs PDF> <abs NEW folder under fwd21_sample_r105/pages/> 70` and open EVERY `page_NN.png` with the Read tool. Look at each page for clipped text, a dash where a figure belongs, a note that contradicts the table under it, a template slot name, an asterisk with no footnote, a stray build phrase. Each sheet must fit one PDF page ("Page n of N" equals the PDF's page count). Fix and re-render until clean; record the final render only.
8. **Record** `RENDER_R105.json` in your folder with exactly: `sample_sha256` (the sample's); `outputs` {`tab_html`, `export_html`, `export_pdf`: each `{path, sha256, bytes}`}; `kind_notes` (one `{kind, example (the exact sentence as printed in the export), names_figure true}` for EACH kind the sample carries); `kind_read_from_field` true; `fee_line_follows_member` true; `disclosure_pointer_kept` true; `export_pdf_pages` and `pdf_pages_read` (both the final PDF's page count); `pdf_clipping` (one `{page, clipped, note}` per page; note = one plain sentence, no figure, name or account number); `portal` {`branch` "wk-IRPT_DASHBD-167-portal", `commit`, `files_changed` (each under `src/pages/InvestorReporting/`)}; `harness_sha256`; `tests` {`new_file`, `mutant_failed` true, `lint_errors`, `typecheck_errors`, `suite_base` and `suite_after` as {pass, skip, fail, new_failing_ids}}; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, paths, hashes and words only: no client name, account number or figure.

<criterion id="DB105-2-AC1" cell_refs="DB-b-203"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r105/p105_round105.py" . DB105-2-AC1</invocation><expect>DB105-2-AC1 PASS</expect></criterion>
`DB105-2-AC1` -- bound to the sample of `DB-b-202`; the three outputs in the private folder with all 117 member ids in each HTML; every stored percent prints at its stored scale; no build word, snake_case identifier, code or ALL_CAPS token in the visible text; the registry's firm title; the text UNHELD and any unheld reason never visible and the baseline's dash (an en dash) prints in at least as many cells as the sample has unheld entries; none of the three round-103 bare sentences prints; the kind notes cover exactly the kinds the sample carries, read differently for different kinds, and each example is printed in the export as one sentence with no semicolon; no semicolon run closed by "is not available yet"; none of the four template slot names prints; every asterisk on a label has its footnote line; the 12-month chart's title names a household line only when one is drawn; the before-fee sentence is absent while its member is absent; an "As of" footer; the PDF's page count equals pages read with a clipping entry per page and none clipped; the portal commit exists, only files under src/pages/InvestorReporting/ changed, `absentKindOf` appears nowhere under src/pages/InvestorReporting at that commit and the report components read `kind`; a failing mutant, lint 0, typecheck 0, no new failing test; no write, push or deploy. Base: FAIL (no record).
<criterion id="DB105-2-J1" cell_refs="DB-b-203" judgment="true"/>
`DB105-2-J1` (JUDGMENT, the CVO's at L9, never the worker's or the issuer's) -- re-grade of round 104's J1: every client-facing line that says a figure is unavailable or not held reads as plain words a client understands and cannot misinform (no note claims a reason for a figure the report prints, no note contradicts the table under it, no template slot name or dangling asterisk prints), and the holdings table stays in the baseline's orientation.

<expected_criteria>DB105-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the contract, the sample, the issuer's check files, `~162/render_sample.ts`, `firmDisplayNames.generated.ts` (generated) and every portal file outside the two component directories and the tests directory.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change.
- **Client data.** The sample and every render live ONLY under `C:/dev/_irpt_private_evidence_20261009/`. Nothing of it goes in the repo, a row, a message or your report: counts, hashes and words only.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the checker's formatting, not the render, is wrong (as one clause was in round 104), file a BLOCKING row naming the clause and stop on it. Never weaken an assertion of an existing test beyond the minimum edit the new behaviour requires, and name each such edit. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W167-S<k>` (continue your numbering), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~167/
portal/src/pages/InvestorReporting/dashboard/report/
portal/src/pages/InvestorReporting/render/performance/report/
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-203.render-remedy-view-reads-kind-no-contradicting-note-client-words.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 107 (round 105), cell `DB-b-203`.
<owned_cells>DB-b-203</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB105-2-AC1 (mechanical), DB105-2-J1 (judgment: the CVO's; leave it out of the instance, the validator refuses a judgment row). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~167/IRPT_DASHBD.TO-DB-b-203.render-remedy-view-reads-kind-no-contradicting-note-client-words.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB105-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; how the view reads the kind and the printed note for each kind; how an UNHELD entry prints; how a note names its account; the template slot names you changed or dropped and how each asterisk now prints; the PDF's page count and the pages you found clipped (or none); lint, typecheck and the suite before and after; any row ids. Counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: DEV-only portal component edits and a local render; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB105-2-AC1 FAILS at base (no record); DB105-2-J1 is the CVO's.
lane: the <paths> block IS the grant.
</preflight>

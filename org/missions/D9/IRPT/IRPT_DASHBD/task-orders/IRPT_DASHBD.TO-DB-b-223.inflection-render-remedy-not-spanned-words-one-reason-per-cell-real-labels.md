# TO IRPT_DASHBD.TO-DB-b-223 -- the INFLECTION RENDER REMEDY: the sample v3 through the same components with the not-spanned words where an account did not span a window, one reason per cell, the gain/loss Ending Value printed, the custodian number's real last four after "ending"; every page read as an image; private folder only

<to_id>IRPT_DASHBD.TO-DB-b-223</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~175</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>110</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-110 ANALYSIS section 2 cell 1 (the CVO's four-line remedy, lines 3 and 4, and the label rule W173-S9) | **Rows:** IRPT_DASHBD-D2-W175-S<k> (continue your numbering) | **Decomp cell:** `DB-b-223` (decomposition section 112) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** `DB-b-222` (complete on your branch; this order is `staged` until the issuer flips it by continuation)

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-175` (branch `wk-IRPT_DASHBD-175`); run everything from its root unless a step says the portal. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~175/`. `C:/dev/wk-irpt-dashbd-175/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-175-portal`), cut from `wk-IRPT_DASHBD-173-portal` (the branch that carries round 109's Inflection render: the member-keyed sentences, the not-held rule, the wrapped-row cost). Do not amend or revert anything already committed there except where this order names it. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`; an account's last four characters, any account, household or client id and any figure are never written in the repo, a row or your report (a last four is `####`).

**Why.** The CVO read all 20 pages of the first Inflection render and graded it FAIL (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_109_L9_GRADE_20261014.md`). Three of its four counts are the render's: (3) the benchmark rows for Year To Date and Last 12 Months of an account that did not exist at the window's start printed "Not available yet" with a note that they "need more history than is available yet": the true reason is the not-spanned case, which has its own words; (4) two reasons for the same cells: the household note says "Opal does not split net additions into contributions, withdrawals and income yet. The same applies to each account.", and four account notes below it say each account's Contributions, Withdrawals and Income "need more history than is available yet"; (2) the gain/loss "Ending Value" printed "Not available yet" beside ending values printed on the overview (the sample now fills it, and the lot-sentence mechanism may have swallowed `glr.ending_value`: check). The CVO's readings: the singular "Lot-level detail is not available for this account yet." stands over a five-account table (use "these accounts" there); the lot sentence sat at the top of a page apart from its heading; the holdings table splits across two sheets. The CTO's label rule: a client render prints the custodian number's real last four characters as stored, alphanumeric allowed ("Account ending 4B7Q"); an ordinal that looks like an account number ("ending 0001") is never printed.

**The cell (`DB-b-223`).**
1. **Read first.** The issuer's check `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r110/p110_inflection.py` (your criterion: it builds `check_render` from round 109's `check_render` with your folder's records, plus `render_extras`: read `render_extras` and `extra_inflection10` fully; its `--selftest` shows the defects it must find in round 109's render), round 109's `check_render` in `checks/r109/p109_round109.py`, the note and cell key convention pinned in the header of `checks/r107/p107_round107.py`, your inputs `~175/BUILD_R110.json` and the sample it names (private client data, read-only), round 109's record `~173/RENDER_R109.json` and harness `~173/render_sample.ts` (copy the harness into YOUR folder as `render_sample.ts`; edit your copy only: its sample path comes from `BUILD_R110.json`, its output folder is `C:/dev/_irpt_private_evidence_20261009/fwd21_sample_r110/`; run notes are in `~146/README.txt`), the contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` (0.5.0), and the components `portal/src/pages/InvestorReporting/dashboard/report/` and `portal/src/pages/InvestorReporting/render/performance/report/` with their tests under `portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/`. Run the whole-scope suite once before any edit (`bun test src/pages/InvestorReporting` from the portal, output under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~175/`) as your base.
2. **Render with no code change first** into `C:/dev/_irpt_private_evidence_20261009/fwd21_sample_r110/` (three outputs: `FWD21_TAB_49F_SAMPLE.html`, `FWD21_EXPORT_49F_SAMPLE.html`, `FWD21_EXPORT_49F_SAMPLE.pdf`; run it in the background and wait for its summary) and read what the checker would find (run the checker's `render_extras` on your HTML; the counts above are what it looks for). The point of FWD-2 is that the SAME components render a second firm: a firm-specific component edit is a finding to record, not a design.
3. **Fix what the reading finds**, each fix generic (keyed by member, window status or account entry, never by a firm name): (a) a benchmark cell of an account window whose `window_status` is NOT_SPANNED prints the not-spanned words the sample carries ("This account did not exist at the start of this period.") and no note says "needs more history" about it; (b) one reason per cell: where the household line prints the split sentence, an account's note for the same members does not repeat a reason (the account line defers to the household line); a key is named by at most one absent note, or by notes with identical words; (c) the gain/loss Ending Value prints the figure of `glr.ending_value` (the lot sentence covers the other `glr.*` and the `trgl.*` members, not `glr.ending_value`); (d) the account label prints `Account ending ` plus the account entry's `last4` exactly as stored (alphanumeric allowed), in the account header, the footer and the tables: no component derives a label from a position or an index; (e) the lot sentence reads "Lot-level detail is not available for these accounts yet." where one note covers more than one account, and the singular for a single account (the singular and the plural both print in this report; both are checked only as the words you print); (f) best effort: keep the lot sentence with the heading it belongs to (a keep-with-next or an unbreakable pair), and let the holdings table split only at a row boundary.
4. **Tests and gates.** A new test file `report-render-r110.test.tsx` under `portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/` pins each rule on a synthetic report (not-spanned benchmark words; one reason per cell; the gain/loss Ending Value printed beside an ending value on the overview; an alphanumeric last four printed after "ending" and a label never built from an index), plus the minimum edits to existing assertions the new behaviour requires (name each; never weaken an assertion beyond the minimum). ONE temporary mutant (the label built from the account's position instead of its `last4`) that a test catches, then reverted. `bun run lint` and `bun run typecheck` after your last portal commit (0 errors); the whole-scope suite after (`new_failing_ids` []).
5. **Re-render and read EVERY page.** Render again after your last portal commit into the same folder; the Read tool refuses a PDF: rasterise it with `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/tools/pdf_to_png.py <abs PDF> <abs NEW folder under fwd21_sample_r110/pages/> 70` and open EVERY `page_NN.png` with the Read tool (all of them: the CVO read all 20 of round 109's). Look for a firm-specific word or layout, a figure printed in one place and called unavailable in another, a benchmark that cannot belong to its window (compare each account's since-inception figures with the household's page), a note that contradicts a table, a repeated or doubled reason, a repeated sentence, clipped text, a dash where words belong, a label that reads like an account number but is not one. Fix and re-render until clean; record the final render only.
6. **Record** `RENDER_R110.json` in your folder with exactly the fields of round 109's record (`~173/RENDER_R109.json`: `sample_sha256`, `outputs`, `kind_notes`, `chart_slots`, `window_not_spanned`, `note_level` (the checker's denominator from `whole_document_scan` and `note_rule`), `kind_read_from_field`, `fee_line_follows_member`, `disclosure_pointer_kept`, `export_pdf_pages`, `pdf_pages_read`, `pdf_clipping`, `portal` {`branch` "wk-IRPT_DASHBD-175-portal", `commit`, `files_changed`}, `harness_sha256`, `tests`, `reads`, `orion_guard` (a copy of `BUILD_R110.json` `orion_guard`), and the false flags). `sample_sha256` is the sample v3's. Counts, paths, hashes and words only.

<criterion id="DB110-3-AC1" cell_refs="DB-b-223"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r110/p110_inflection.py" . DB110-3-AC1</invocation><expect>DB110-3-AC1 PASS</expect></criterion>
`DB110-3-AC1` -- every round-109 render clause, re-bound to the sample v3 and to your folder (the firm title; all member ids in each HTML; percents at their stored scale; no build language; the dash only for an unheld class; the whole-document and note-level rules with their planted mutants and a denominator equal to yours; the account-return and lot sentences; the guard state; the portal commit, a failing mutant, lint 0, typecheck 0, no new failing test; no write, push or deploy) PLUS the round-110 clauses on both HTMLs: the gain/loss Ending Value prints a figure for every account; no note says "needs more history" for an account window that is not spanned; no cell carries two different reasons in two notes; every "ending XXXX" label is an account's real last four as the sample holds it. Base: FAIL (no record).
<criterion id="DB110-3-J1" cell_refs="DB-b-223" judgment="true"/>
`DB110-3-J1` (JUDGMENT, the CVO's at L9, never the worker's or the issuer's) -- the re-render of the Inflection household: a reader cannot tell from the page which firm's plumbing produced it, every line that says a figure is unavailable or not held reads as plain words, gives its true reason and cannot misinform, no figure is printed under a window it does not measure, and the layout is the 49 Financial layout.

<expected_criteria>DB110-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the contract, the sample, the issuer's check files, `~173/render_sample.ts`, `firmDisplayNames.generated.ts` (generated) and every portal file outside the two component directories and the tests directory.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change.
- **Client data.** The sample and every render live ONLY under `C:/dev/_irpt_private_evidence_20261009/`. Nothing of it goes in the repo, a row, a message or your report: counts, hashes and words only.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the checker's convention or formatting, not the render, is wrong, file a BLOCKING row naming the clause and stop on it. Never weaken an assertion of an existing test beyond the minimum edit the new behaviour requires, and name each such edit. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W175-S<k>` (continue your numbering), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~175/
portal/src/pages/InvestorReporting/dashboard/report/
portal/src/pages/InvestorReporting/render/performance/report/
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-223.inflection-render-remedy-not-spanned-words-one-reason-per-cell-real-labels.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 112 (round 110), cell `DB-b-223`.
<owned_cells>DB-b-223</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB110-3-AC1 (mechanical), DB110-3-J1 (judgment: the CVO's; leave it out of the instance, the validator refuses a judgment row). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~175/IRPT_DASHBD.TO-DB-b-223.inflection-render-remedy-not-spanned-words-one-reason-per-cell-real-labels.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB110-3-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; whether the SAME components rendered the second firm without a firm-specific edit (and any edit you made, which and why); how each of the CVO's counts 2, 3 and 4 now reads (words, no figure); the checker's denominator (cells scanned, absent cells, notes, pointer notes) and that the planted mutants were reported; the PDF's page count and that you read every page (and any you found clipped, or none); lint, typecheck and the suite before and after; the number of accounts whose ending value is zero (a count). Counts, hashes and words only: no client or account id, no last four, no figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: DEV-only portal component edits on a local branch and a local render; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB110-3-AC1 FAILS at base (no record) and its render clauses are exercised by the checker's self-test on round 109's render (the CVO's counts 2 to 4 are found); DB110-3-J1 is the CVO's.
lane: the <paths> block IS the grant.
</preflight>

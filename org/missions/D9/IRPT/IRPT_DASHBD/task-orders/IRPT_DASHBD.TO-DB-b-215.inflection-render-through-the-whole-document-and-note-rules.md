# TO IRPT_DASHBD.TO-DB-b-215 -- the FIRST INFLECTION RENDER: the Inflection sample through the 49 Financial layout, the whole-document and note-level rules, in the Inflection firm title, with the account-return and lot sentences printed in plain words and the Orion guard state named; every page read as an image; private folder only

<to_id>IRPT_DASHBD.TO-DB-b-215</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~173</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>109</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-109 ANALYSIS section 3 cell 2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_109_20261014.md`) | **Rows:** IRPT_DASHBD-D2-W173-S<k> (continue your numbering) | **Decomp cell:** `DB-b-215` (decomposition section 111) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** `DB-b-214` (its sample and record).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-173` (branch `wk-IRPT_DASHBD-173`); run everything from its root unless a step says the portal. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~173/`. `C:/dev/wk-irpt-dashbd-173/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-173-portal`), cut from the branch that carries round 107's render (`wk-IRPT_DASHBD-170-portal`: the view reads the kind field, absent charts name a computed page, the notes and cells carry their keys). Do not amend or revert anything already committed there except where this order names it. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`; an account's last four digits are `####` in anything you record, never the digits.

**Why.** FWD-2 says any firm's account loads the same way and nothing on the page says which firm's plumbing produced it; FWD-21 says one household at each of three firms is rendered in the one default report. The 49 Financial report is done except for its disclosure page (a release gate on Andrew's call, for every firm). Your previous order built an Inflection sample from Inflection's own silver. This order renders it through the SAME components and the SAME rules (the whole-document and note-level rules of rounds 106 and 107), and the only things that differ are the firm title (the registry's Inflection Wealth Management) and two plain-word sentences the Inflection data needs: an account's return reads "Account-level returns are not available for this firm yet." and a lot-level figure reads "Lot-level detail is not available for this account yet." The disclosure page stays "Not available yet" and the report reaches no client: the render stays in the private folder. J1 is the CVO's.

**The cell (`DB-b-215`).**
1. **Read first.** The issuer's check file `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r109/p109_round109.py` (your criterion: it carries round 107's render clauses, re-bound to your folder, plus `extra_inflection`; read `check_render` and the note and cell key convention pinned in the header of `checks/r107/p107_round107.py`), round 107's record `deliverables/0.9.0_WK_IRPT_DASHBD~170/RENDER_R107.json` and harness `~170/render_sample.ts` (copy the harness into YOUR folder; edit your copy only; run notes are in `~146/README.txt`), your inputs `~173/BUILD_R109.json` and the Inflection sample it names (private client data, read-only), the contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` (0.4.3), the registry-generated firm-title map the components read (`firmDisplayNames.generated.ts`: do not edit it; if Inflection's title is not in it, file a BLOCKING row and stop), and the components `portal/src/pages/InvestorReporting/dashboard/report/` and `portal/src/pages/InvestorReporting/render/performance/report/` with their tests under `portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/`. Run the whole-scope suite once before any edit (`bun test src/pages/InvestorReporting` from the portal, output under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~173/`) as your base.
1a. **Relabel the sample first (issuer amendment, row `W173-S9`).** The sample's `last4` label takes the last four characters of the custodian number, which for four of five accounts include non-digits, and two labels are equal. The rule is now: every account's `last4` is four digits and the five labels are distinct; set each account's `last4` to its 1-based position in the household's accounts sorted by `account_id`, zero-padded to four digits (`0001`, `0002`, ...). This is a relabel of the existing sample, NOT a new build: no S3 read, no silver read, no other value changes. Write the relabelled sample as a NEW file in the private folder beside the old one (never overwrite the old), update `BUILD_R109.json` in your folder (`sample.path`, `sample.sha256`, and a field `last4_rule` with the words of this rule), then run `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r109/p109_round109.py" . DB109-1-AC1` and report its verdict (it must still PASS; if it does not, file a BLOCKING row and stop). The render, its record and every later step use the new sample. The account labels in any render are these four-digit ordinals; an account's real last four are never printed.
2. **Render with no code change first.** Render the Inflection sample into `C:/dev/_irpt_private_evidence_20261009/fwd21_sample_r109/` (three outputs: `FWD21_TAB_49F_SAMPLE.html`, `FWD21_EXPORT_49F_SAMPLE.html`, `FWD21_EXPORT_49F_SAMPLE.pdf`; run it in the background and wait for its summary) and read what the checker would find. Fix only what the checker or your reading finds: the point of FWD-2 is that the SAME components render a second firm; a firm-specific component edit is a finding to record, not a design.
3. **The two Inflection sentences.** The view prints, through the SAME member-specific words mechanism the split-column sentence uses (a table keyed by MEMBER ID, never by reason text), (a) for the account-return members `avs.<window>.return_cumulative` the sentence `Account-level returns are not available for this firm yet.` and (b) for the lot members `trgl.*` and `glr.*` the sentence `Lot-level detail is not available for this account yet.` Each is a keyed note under the round-107 convention (`data-note="absent"`, `data-note-keys` naming every member and account entity the sentence covers, so a printed figure of any of them would fail the rule); print each sentence once per section or entity note as the layout needs, never as a long repeated run, and never beside a figure the same report prints. These words are for any firm whose data lacks those pieces, so key them by member and NOT by firm.
4. **Everything else is the round-107 behaviour, unchanged.** The page-pointer wording, the foot-note wording, the split-column sentence, the keyed notes and cells, the dash only for an unheld class, the disclosure pointer and page: nothing about them changes for Inflection.
5. **Tests and gates.** A new test file `report-render-r109.test.tsx` under `portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/` pins each rule (the account-return sentence and the lots sentence print for those members and not for others, keyed by member; nothing in the components or tests names a firm to choose these words), plus the minimum edits to existing assertions the new behaviour requires (name each; never weaken an assertion beyond the minimum). ONE temporary mutant (the sentences are keyed by a firm name instead of the member) that a test catches, then reverted. `bun run lint` and `bun run typecheck` after your last portal commit (0 errors); the whole-scope suite after (`new_failing_ids` []).
6. **Re-render and read.** Render again after your last portal commit into the same folder; the Read tool refuses a PDF: rasterise it with `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/tools/pdf_to_png.py <abs PDF> <abs NEW folder under fwd21_sample_r109/pages/> 70` and open EVERY `page_NN.png` with the Read tool. Look for a firm-specific word or layout, a pointer to a page that does not print the figure, a note that contradicts a table, a repeated sentence, clipped text, a dash where words belong. Each sheet fits one PDF page. Fix and re-render until clean; record the final render only.
7. **Record** `RENDER_R109.json` in your folder with exactly the fields of round 107's record (`~170/RENDER_R107.json`: `sample_sha256`, `outputs`, `kind_notes`, `chart_slots`, `window_not_spanned`, `note_level` (the checker's denominator, from `whole_document_scan` and `note_rule` as before), `kind_read_from_field`, `fee_line_follows_member`, `disclosure_pointer_kept`, `export_pdf_pages`, `pdf_pages_read`, `pdf_clipping`, `portal` {`branch` "wk-IRPT_DASHBD-173-portal", `commit`, `files_changed`}, `harness_sha256`, `tests`, `reads`, and the false flags) PLUS `orion_guard` (an exact copy of the `orion_guard` field of your `BUILD_R109.json`). `sample_sha256` is the Inflection sample's. Counts, paths, hashes and words only.

<criterion id="DB109-2-AC1" cell_refs="DB-b-215"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r109/p109_round109.py" . DB109-2-AC1</invocation><expect>DB109-2-AC1 PASS</expect></criterion>
`DB109-2-AC1` -- every round-107 render clause, bound to the Inflection sample of `DB-b-214` and to your folder (all 117 member ids in each HTML; percents at their stored scale; no build language; the REGISTRY'S Inflection firm title and never "Sample Firm"; the dash in exactly the unheld cells; each absent chart computed or dropped and never claiming a reason; no slot name, bare note, semicolon run or dangling asterisk; the split sentence once; the whole-document and note-level rules with their two planted mutants and a denominator that equals yours (the note-level absent-note mutant is planted on a key the sample prints); every account's last4 label is four digits and the labels are distinct; the portal commit and tests) PLUS: both HTMLs print "Account-level returns are not available for this firm yet." and "Lot-level detail is not available for this account yet."; the render record's `orion_guard` and the build record's both equal the issuer's read-gate state; a failing mutant, lint 0, typecheck 0, no new failing test; no write, push or deploy. Base: FAIL (no record).
<criterion id="DB109-2-J1" cell_refs="DB-b-215" judgment="true"/>
`DB109-2-J1` (JUDGMENT, the CVO's at L9, never the worker's or the issuer's) -- the first Inflection render: a reader cannot tell from the page which firm's plumbing produced it (only the firm title differs), every line that says a figure is unavailable or not held reads as plain words and cannot misinform, no account return or lot figure is implied that the source does not hold, and the layout is the 49 Financial layout.

<expected_criteria>DB109-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the contract, the sample (except step 1a's relabel into a new file), the issuer's check files, `~170/render_sample.ts`, `firmDisplayNames.generated.ts` (generated) and every portal file outside the two component directories and the tests directory.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change.
- **Client data.** The sample and every render live ONLY under `C:/dev/_irpt_private_evidence_20261009/`. Nothing of it goes in the repo, a row, a message or your report: counts, hashes and words only; an account's last four digits are `####`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the checker's convention or formatting, not the render, is wrong, file a BLOCKING row naming the clause and stop on it. Never weaken an assertion of an existing test beyond the minimum edit the new behaviour requires, and name each such edit. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W173-S<k>` (continue your numbering), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~173/
portal/src/pages/InvestorReporting/dashboard/report/
portal/src/pages/InvestorReporting/render/performance/report/
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-215.inflection-render-through-the-whole-document-and-note-rules.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 111 (round 109), cell `DB-b-215`.
<owned_cells>DB-b-215</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB109-2-AC1 (mechanical), DB109-2-J1 (judgment: the CVO's; leave it out of the instance, the validator refuses a judgment row). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~173/IRPT_DASHBD.TO-DB-b-215.inflection-render-through-the-whole-document-and-note-rules.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB109-2-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; whether the SAME components rendered the second firm without a firm-specific edit (and if you had to edit one, which and why); how the two Inflection sentences print and how they are keyed; the checker's denominator (cells scanned, absent cells, notes, pointer notes) and that both planted mutants were reported; the guard state named; the PDF's page count and the pages you found clipped (or none); lint, typecheck and the suite before and after; any row ids. Counts and words only; no account number, household or client id, name or figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: DEV-only portal component edits and a local render; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB109-2-AC1 FAILS at base (no record) and its note-level rule is exercised by the round-107 self-test (9 arms, both planted mutants); DB109-2-J1 is the CVO's.
lane: the <paths> block IS the grant.
</preflight>

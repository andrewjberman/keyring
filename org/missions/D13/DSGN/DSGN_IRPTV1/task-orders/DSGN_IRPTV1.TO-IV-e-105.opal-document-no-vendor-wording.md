# TO DSGN_IRPTV1.TO-IV-e-105 -- the print and export document of an Opal report prints no vendor wording -- a product change; candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-105</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~58</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 5037 item 1 (2026-10-11 ~13:42Z): "Row D2-W57-S2, the print and export document still says vendor words on an Opal report: Andrew's sitting may export." | **Rows:** DSGN_IRPTV1-D2-W57-S2 | **Decomp cell:** `IV-e-105` (decomposition v22) | **outcome_ref:** FWD-1 of IRPT_YCDGEN, served on this project's page | **depends_on:** none; FIRST on the slot.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-49` (the slot's worktree; branch `wk-dsgn-irptv1-r14-49`); run everything from its root
unless a step says the portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~58/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-49/portal` is a PORTAL worktree (its own git repo) at the commit your spawn prompt names. Do not amend or
revert anything committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's
status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink.
`node_modules` is a real local install that another worktree junctions to: no `bun install`, no package change, never delete it. Resolve bun
with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a
file that has no uncommitted work of yours. One whole-scope run before any edit (`bun test src/pages/InvestorReporting`, output to a file
under `C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~58/`) is your base for `new_failing_ids`.

**What is wrong.** IV-e-101 (on portal DEV as 58e15f4c) made an Opal report OPENED on the page read its own words ("Computation
validation: ...", "Source: Opal Capital Analysis"). Its worker found, and did not change (row DSGN_IRPTV1-D2-W57-S2), the other surfaces that
still print the vendor's words for an Opal report: the print/export document (`tabs/analysis/AnalysisDocument.tsx` near lines 77-80, no
Opal branch), and anything else a report can be printed or exported from. That document is the one a principal could be handed.

**The cell (`IV-e-105`).** Read IV-e-101's record and test first (`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~57/OPAL_WORDING.json`,
`src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-101.opal-report-words.test.tsx`): the same rule, the same words, the same way of
telling an Opal report (the view's `provider`, set by the adapter from the wire member it already reads).
1. **Every surface, by subtraction.** List EVERY surface an analysis report can be printed, exported or previewed from (start from every
   importer of the sections view and of `AnalysisDocument`; state the search and its denominator): `surfaces`: [{surface, file, line,
   vendor_words_before, opal_reads_after}]. A surface that cannot show an Opal report is listed with why.
2. **The words.** On each surface that can show an Opal report: no word "vendor" and no word "extraction" (any case) for an OPAL_ENGINE
   report; the validation line reads `Computation validation: ...` with today's value rule; attribution reads `Source: Opal Capital
   Analysis`; an extraction-coverage block is not drawn. A VENDOR report's document is EXACTLY as today (`vendor_unchanged: true`, measured
   by rendering both before and after). The "Vendor preview" label on the Analysis tab names a vendor PDF and is left alone unless it can
   be shown for an Opal report: say which.
3. **A test** under `__tests__/dsgn-irptv1/`: renders the document for an Opal report and for a vendor report and asserts the rendered
   text; one temporary mutant (the vendor wording restored for Opal) makes it fail.
4. **Evidence** in your folder: the rendered document of an Opal report and of a vendor report, as the page produces them for print or
   export (a PNG from a build with `scripts/ui-smoke.mjs --dist`, or a driver copying its recipe as
   `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~57/opal-report-driver.mjs` does; if the document is produced as HTML or PDF bytes,
   save those bytes rendered from synthetic data). `evidence`: {opal, vendor}. READ what you save and say what it shows.
5. `bun run typecheck` 0 errors; one whole-scope run after; `suite_after`; `product_files_changed`; `portal_commit`.

<criterion id="IV105-AC1" cell_refs="IV-e-105"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r22/p22_round22.py" . IV105-AC1</invocation><expect>IV105-AC1 PASS</expect></criterion>
`IV105-AC1` -- every print or export surface is listed, an Opal document reads no vendor word, a vendor document is unchanged, a test holds it with a failing mutant, and both documents are saved as evidence. Base: FAIL.

<expected_criteria>IV105-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. The contract and the producer's fixtures (workspace files)
  are read, never edited. No file under `contracts/wire/` is hand-edited (generated; one command regenerates it:
  `bun run src/pages/InvestorReporting/__tests__/fe-s-13/gen-all.ts`).
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no
  `bun install`, no package change, no dev server on any port.
- **Synthetic data only** in any fixture, screenshot or record: no real client name, account number or figure.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W58-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~58/
portal/src/pages/InvestorReporting/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-105.opal-document-no-vendor-wording.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v22 (round 22), cell `IV-e-105`.
<owned_cells>IV-e-105</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV105-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~58/DSGN_IRPTV1.TO-IV-e-105.opal-document-no-vendor-wording.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV105-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the portal commit hashes in order, the criterion's last line, every surface with its file and line and what an Opal report reads there now, the vendor document before and after, the test and its mutant, the two evidence files and what each shows, typecheck, `product_files_changed`, `suite_after`, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; wording on the print and export document of a client-facing page; a vendor document is pinned unchanged; the candidate is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; every criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>

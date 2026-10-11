# TO DSGN_IRPTV1.TO-IV-e-83 -- S61: the Holding cell names the CORRECTED security on a corrected row, with the uploaded symbol beside it as "uploaded as" -- a served-page wording fix, candidate to the CTO before DEV

<to_id>DSGN_IRPTV1.TO-IV-e-83</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~46</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's round analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_FROM_WATERMARK_20261002_20261011.md` @10d7d46e49, section 4 item 2 | **Decomp cell:** `IV-e-83` (decomposition v11) | **outcome_ref:** FWD-13 (the upload review) | **depends_on:** IV-e-82 (the suite baseline), same slot before IV-e-85.

---

## WORKER FACE

Your worktree is `C:/dev/wk-dsgn-irptv1-46`; run everything from its root unless a step says the portal. Your folder is
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~46/`.

**Two repos, one worktree pair.** `C:/dev/wk-dsgn-irptv1-46` is the workspace worktree; `C:/dev/wk-dsgn-irptv1-46/portal` is a PORTAL worktree (its own git repo, branch
`wk-dsgn-irptv1-r11-46`), cut by the issuer from the portal DEV tip `7bb81fa89792067bf90531371bcf0031a05f878c` (read by `ls-remote` after a fetch, 2026-10-11 ~05:1xZ). Portal files commit in the
portal repo (cwd `C:/dev/wk-dsgn-irptv1-46/portal`, `bash C:/dev/wk-dsgn-irptv1-46/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <paths relative to portal>`);
records, rows and this order's status commit in the workspace repo (cwd `C:/dev/wk-dsgn-irptv1-46`). Never push either repo.
**Toolchain.** `node_modules` in `C:/dev/wk-dsgn-irptv1-46/portal` is a junction made by the issuer: do NOT run `bun install`. Resolve bun with `command -v bun`; never
type its path. Tests: `bun test <file>` from `C:/dev/wk-dsgn-irptv1-46/portal`.

**THE CLIENT-DATA RULE (binding):** never print an account number, a client name or a client figure in a commit message, a record, a row or a report.
Fixtures are synthetic.

**The cell (`IV-e-83`).** Row `DSGN_IRPTV1-S61`: after portal commit 56b71adb the upload review's Holding column reads `original.symbol` first, but on a
corrected row the dollars belong to the corrected security (the intake stores the uploaded `original` beside the corrected `security_id` and
`analysis_dollars`). An advisor therefore reads one ticker beside another security's dollars. The CTO placed it first among the page cells. Read the
row, `src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx` (the review table) and its pins under `__tests__/dsgn-irptv1/` first. Read
`portal/DESIGN.md` before you touch the cell's markup.

In `C:/dev/wk-dsgn-irptv1-46/portal`:
1. On a row whose stored security differs from its uploaded symbol, the Holding cell names the CORRECTED security first, and states the uploaded
   symbol beside it with the words "uploaded as". A row that was not corrected renders exactly as it does today. The FE derives nothing: both
   values come from the served row; if the served row does not carry the corrected security's display symbol, STOP with a row saying which field is
   missing; do not derive a ticker from an id.
2. A component test under `__tests__/dsgn-irptv1/`: a corrected row shows the corrected symbol and "uploaded as <uploaded symbol>"; an uncorrected
   row shows no "uploaded as". Show it FAILS on the file before your change (record the failing line) and passes after. Keep every pin in that folder
   that passed before your change passing; name any you had to update and why.
3. Render it: `node scripts/ui-smoke.mjs` if a fixture reaches the review (see `/frontend-dev`'s notes in `portal/CLAUDE.md`), else render the
   component to static HTML in your deliverables. READ the screenshot or the HTML yourself and say what the cell shows.
4. Record `S61_FIX.json` {component_file, test_file, fail_before: {result, line}, after: {result}, product_files_changed, portal_commit, render}.
   The portal commit is a CANDIDATE: it is not merged to DEV by you; the issuer sends its pin to the CTO.

<criterion id="IV83-AC2" cell_refs="IV-e-83" judgment="true"/>
`IV83-AC2` -- graded at L9 by `3.0.0_SA_CVO` from your render: the corrected row reads unambiguously and follows `portal/DESIGN.md` (navy ink on white, no
new colour, tabular numerals in the dollars column).

## AMENDMENT 1 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~06:0xZ): the portal base moved, and the suite baseline is a named set

- **Base.** Your portal worktree is cut from DEV tip `6f70e36bace0014384a494f1509dc3ca65f33095`, not `7bb81fa8`: IV-e-84's press test
  (`__tests__/dsgn-irptv1/upload-press-did-you-mean.test.tsx`) landed on DEV after the cut. It exercises `ProspectComposer`'s suggestion handler;
  it passes at your base and must pass at your commit.
- **Baseline.** IV-e-82 drained @fb60e94fd8: at `7bb81fa8` the Investor Reporting scope fails the SAME 43 test ids in three runs
  (`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~43/SUITE_SAMPLE.json`). "Keep every pin passing" means: after your change,
  one full run of `bun test src/pages/InvestorReporting` fails a set of ids that is a SUBSET of those 43 (plus nothing new). Record the run's failing
  ids and the set difference in your record under `suite_after` {failed, new_failing_ids, fixed_ids}. A new failing id is yours to fix or to report.
- Six of the 43 fail only because a test spawns bun at another user's path (row DSGN_IRPTV1-D2-W43-S1); they are not yours to fix here.

Gate limb: none graded this modification (to-pipeline-gate LIMB 6 fires on a newly added order only; `<placeholders>` is NONE).

<criterion id="IV83-AC1" cell_refs="IV-e-83"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r11/p11_round11.py" . IV83-AC1</invocation><expect>IV83-AC1 PASS</expect></criterion>
`IV83-AC1` -- the fix is recorded with its component, a test that failed before and passes after, the product files changed and the candidate commit. Base: FAIL.

<expected_criteria>IV83-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no vendor call, no secret read, no `bun install`, no download of any
  package, script or program.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. An edit outside the grant, a filled figure, or a client identifier in a committed file is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W46-S<k>`, with the real current UTC time.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~46/
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~46/
portal/src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx
portal/src/pages/InvestorReporting/tabs/analysis/
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-83.s61-corrected-holding-cell.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v11 (round 11), cell `IV-e-83`.
<owned_cells>IV-e-83</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV83-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~46/DSGN_IRPTV1.TO-IV-e-83.s61-corrected-holding-cell.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV83-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: commit hashes in each repo, each criterion's last line, what you measured, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one cell of the upload review on a served page; a candidate commit only, landed on DEV after the CTO's review.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched; nothing is deployed.
comp-adversary: RUN -- IV83-AC1 FAIL at base (no record). CTO round analysis @10d7d46e49.
lane: the <paths> block IS the grant.
</preflight>

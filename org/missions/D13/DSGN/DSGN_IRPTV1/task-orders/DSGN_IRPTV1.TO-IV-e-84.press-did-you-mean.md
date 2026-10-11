# TO DSGN_IRPTV1.TO-IV-e-84 -- S60: one component test that PRESSES the "Did you mean" button and asserts the re-post's corrections -- a test-only change, mutants caught

<to_id>DSGN_IRPTV1.TO-IV-e-84</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~44</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's round analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_FROM_WATERMARK_20261002_20261011.md` @10d7d46e49, section 4 item 3 | **Decomp cell:** `IV-e-84` (decomposition v11) | **outcome_ref:** FWD-13 (the upload review) | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-dsgn-irptv1-44`; run everything from its root unless a step says the portal. Your folder is
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~44/`.

**Two repos, one worktree pair.** `C:/dev/wk-dsgn-irptv1-44` is the workspace worktree; `C:/dev/wk-dsgn-irptv1-44/portal` is a PORTAL worktree (its own git repo, branch
`wk-dsgn-irptv1-r11-44`), cut by the issuer from the portal DEV tip `7bb81fa89792067bf90531371bcf0031a05f878c` (read by `ls-remote` after a fetch, 2026-10-11 ~05:1xZ). Portal files commit in the
portal repo (cwd `C:/dev/wk-dsgn-irptv1-44/portal`, `bash C:/dev/wk-dsgn-irptv1-44/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <paths relative to portal>`);
records, rows and this order's status commit in the workspace repo (cwd `C:/dev/wk-dsgn-irptv1-44`). Never push either repo.
**Toolchain.** `node_modules` in `C:/dev/wk-dsgn-irptv1-44/portal` is a junction made by the issuer: do NOT run `bun install`. Resolve bun with `command -v bun`; never
type its path. Tests: `bun test <file>` from `C:/dev/wk-dsgn-irptv1-44/portal`.

**THE CLIENT-DATA RULE (binding):** never print an account number, a client name or a client figure in a commit message, a record, a row or a report.
Fixtures are synthetic.

**The cell (`IV-e-84`).** Row `DSGN_IRPTV1-S60`: the pin `src/pages/InvestorReporting/__tests__/dsgn-irptv1/upload-accept-suggestion.test.tsx`
renders the "Did you mean AAPL?" row and the "Use AAPL" button but never presses it. With the click handler in
`src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx` made to fill nothing, or to fill another ticker, the pin still passes. Read the row and
both files first.

In `C:/dev/wk-dsgn-irptv1-44/portal`:
1. Add ONE component test (a new file under `src/pages/InvestorReporting/__tests__/dsgn-irptv1/`, or a new case in the existing pin): it renders the
   review with a not-found ticker that has a suggestion, PRESSES the suggestion button, triggers the re-post, and asserts the corrections the re-post
   sends name the uploaded symbol and the suggested one (the row gives the shape the reviewer's probe saw: a `TICKER_NOT_FOUND` entry mapping the
   uploaded symbol to the suggestion).
2. **Mutants.** Show the test catches at least two: the handler fills nothing; the handler fills a different ticker. Make each mutant in a scratch
   copy or by a temporary edit you REVERT (`git diff --stat` on the product file must be empty at your commit). Record each mutant's failing line.
3. Record `PRESS_PIN.json` {test_file, test_name, head: {result, output_tail}, mutants: [{name, result, line}], product_files_changed: [],
   portal_commit}. The portal commit carries the test only.

<criterion id="IV84-AC1" cell_refs="IV-e-84"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r11/p11_round11.py" . IV84-AC1</invocation><expect>IV84-AC1 PASS</expect></criterion>
`IV84-AC1` -- the new test presses the button and passes at head, at least two handler mutants fail it, and no product file changed. Base: FAIL.

<expected_criteria>IV84-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no vendor call, no secret read, no `bun install`, no download of any
  package, script or program.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. An edit outside the grant, a filled figure, or a client identifier in a committed file is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W44-S<k>`, with the real current UTC time.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~44/
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~44/
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-84.press-did-you-mean.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v11 (round 11), cell `IV-e-84`.
<owned_cells>IV-e-84</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV84-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~44/DSGN_IRPTV1.TO-IV-e-84.press-did-you-mean.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV84-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: commit hashes in each repo, each criterion's last line, what you measured, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a test-only change; no product file is edited.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched; nothing is deployed.
comp-adversary: RUN -- IV84-AC1 FAIL at base (no record). CTO round analysis @10d7d46e49.
lane: the <paths> block IS the grant.
</preflight>

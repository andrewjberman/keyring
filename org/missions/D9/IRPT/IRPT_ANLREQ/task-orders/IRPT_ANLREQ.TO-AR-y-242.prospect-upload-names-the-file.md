# TO IRPT_ANLREQ.TO-AR-y-242.prospect-upload-names-the-file -- the prospect upload step names the chosen file and keeps it visible

<to_id>IRPT_ANLREQ.TO-AR-y-242</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~74</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-242` (`decompositions/IRPT_ANLREQ_DECOMP_R22P_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~74`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-74` (branch `wk-IRPT_ANLREQ-74`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~74 <0.9.0_WK_IRPT_ANLREQ~74@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W74-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-242`, inlined) -- THE UPLOAD STEP NAMES THE FILE. A CANDIDATE on a portal branch; nothing is landed, pushed or deployed.

*Andrew's own test (rows D2-S77, D2-S78): after choosing the sample xlsx the in-page input still read "Choose File  No file chosen" and the status read only "Needs correction."; no file name and no sign of the upload appeared anywhere on the page. The in-page input is a bare native `<input type=file>` (`ProspectComposer.tsx` :419-422); the dialog's own input already uses the visually hidden input plus a button-styled label idiom and shows "Chosen: <name>" (:400-410, row W2-03).*

1. **The branch.** The portal repository is `C:/dev/ajb_workspace/portal` (a separate git repository). `git -C C:/dev/ajb_workspace/portal fetch origin DEV` is permitted. Record `dev_tip` (full sha of `origin/DEV`). Make a worktree OUTSIDE the product tree: `git -C C:/dev/ajb_workspace/portal worktree add C:/dev/wk-portal-74 -b wk-IRPT_ANLREQ-74-portal origin/DEV`. Never check out, reset or commit anything else in the portal checkout, and never push. Commit the way an earlier candidate branch was made (`git -C ... log` of `wk-IRPT_ANLREQ-63-portal`); if a hook or a rule of the portal repository refuses your commit, STOP and file a row with the refusal text. Read the portal's own `CLAUDE.md` and `DESIGN.md` first: new text follows their clauses (navy ink on white panels, no light-on-light; cite the clause number in your record for each visual choice).
2. **The change.** In the in-page upload block (:416-427), replace the bare native input by the dialog's idiom: a visually hidden input inside a button-styled label ("Choose the holdings file", and once a file is set "Choose a different file"), and, whenever `file` is set, one line `data-slot="upload-file-name"` that reads `File: <name>` and stays visible in EVERY state of the upload step (RESOLVING, NORMALIZED, NEEDS_CORRECTION) and after a re-render. Keep the existing state line and `chooseFile`, the findings, the proxy block and every other behaviour as they are. Touch `src/` only (no `package.json`, lockfile, build or config file) and change no wire reader or contract file.
3. **The test, before and after.** Add tests in the portal's existing test folder for this component (find them with `git ls-files`; match the neighbours' style) that (a) render the composer with a file chosen and assert the file's name is on the face, (b) assert the name stays on the face after a NEEDS_CORRECTION answer, (c) assert the face carries no native "No file chosen" text, and (d) assert the face shows no `upload-file-name` line when no file is set. `before_arm`: run the new tests on `origin/DEV` WITHOUT the change (stash or a second worktree) and record that (a) to (c) FAIL (`failed` at least 1); `tests`: run them with the change (all pass) and run the whole folder of the component (counts; the `dsgn-irptv1` folder has known failures on DEV that fail with and without your change: say so, with counts both ways, as row W63-S2 did). Use `bun` (resolve it from your profile; do not bake a path), and `bun run typecheck` (never bare `tsc --noEmit`).
4. **Commit** in the portal worktree on your branch; record the full commit sha.
5. **Write `r22/PORTAL_FILE_NAME_CANDIDATE.json`:** `dev_tip`, `branch`, `commit`, `files_changed` (paths under `src/`), `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm` {`failed`, `output_tail`}, `what_a_person_sees` (the words as rendered, per state), `design_clauses`, `claim`, `not_read` (the live PROD and DEV bundles; a browser render if you ran none).
6. **In your report:** the branch, the commit, the files, the before and after counts, and what a person sees in each state.

### ACCEPTANCE

<criterion id="AR242-y-AC1" cell_refs="AR-y-242"><invocation>python C:/dev/wk-irpt-anlreq-74/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y242-portal --root C:/dev/wk-irpt-anlreq-74</invocation><expect>Y242-PORTAL-OK</expect></criterion>
`AR242-y-AC1`: the record names a portal commit that exists in the portal repository, touching `src/` only, with added tests that fail on the DEV tip without the change and pass with it, and no failing test of the folder beyond the known pre-existing ones.

<criterion id="AR242-y-AC2J" cell_refs="AR-y-242" judgment="true"/>
`AR242-y-AC2J` (judgment, graded at L9, never by you): the face names the chosen file in every state and the native "No file chosen" text is gone, the tests would fail if the change were removed, the change reads the portal's design clauses, and nothing was landed or pushed.

<expected_criteria>AR242-y-AC1 AR242-y-AC2J</expected_criteria>

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-13 ~17:5xZ, after the worker's report; row `IRPT_ANLREQ-D2-W74-S2`).** The candidate names the file but the state line below it still reads "No file chosen yet." while a file is set and no review has run: the very contradiction Andrew's test reported ("no sign of the upload"). Change the state line ONLY for the case a file is set and the state is `NOTHING_CHOSEN`: it reads `File chosen. Select Review portfolio to read it.` (find the button's words in the component and use them exactly); `UPLOAD_STEP_STATE_LABELS` and `uploadStepStateFor` keep their values for every other state. Add one test (file set, no result: the line reads as above, and never reads "No file chosen yet."), run it on the DEV tip without the change (it must FAIL) and with it, and add a second commit on the same portal branch; update the record's `commit`, `tests`, `before_arm` and `what_a_person_sees`. Also: the checker `y242-portal` now reads `r22/` (fixed @bddbded002), so the record stays where it is. Gate limb that graded this amendment: none (the issuer amends its own order).

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~74/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R22P_Y.md</decomp_doc>
<owned_cells>AR-y-242</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~74/IRPT_ANLREQ.TO-AR-y-242.prospect-upload-names-the-file.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-242`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR242-y-AC1,AR242-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading Andrew's own-test report (rows D2-S77, D2-S78) against the cell; the lens: a test that passes without the change, or a change that fixes the page the worker imagined and not the one Andrew saw. The order requires the new test to FAIL on the DEV tip without the change, and the words a person sees to be stated as rendered. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on Andrew's own upload test (rows `D2-S77`, `D2-S78`, msg 7105) as workstream `YR` round 18. Base: `AR242-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.

<!-- ISSUER NOTE 2026-10-13 (2.0.0_SA_COO~Y2): status flipped to complete after AMENDMENT 1. The worker instance AR242-y-AC1 is recorded FAIL on a checker read-path defect (r21 against r22, row W74-S1), and stays FAIL there; the trunk checker, run by the issuer on the amended record attached at deliverables/2.0.0_SA_COO~Y2/r22/PORTAL_FILE_NAME_CANDIDATE_AMEND1.json (@7ff2ede6ac, because the lane gate refuses the continuation serial ~78 under ~74, row W78-S3), prints Y242-PORTAL-OK: 6 of 6 tests pass and 5 of 6 fail on the DEV tip without the change. One pin of the worker instance was fixed by the issuer under the audited author override (@95cd92861d). The CVO decides whether that re-grade is right. -->

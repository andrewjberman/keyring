# TO IRPT_ANLREQ.TO-AR-y-214.portal-sheets-not-read-notice -- a portal candidate that shows the SHEETS_NOT_READ notice

<to_id>IRPT_ANLREQ.TO-AR-y-214</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~63</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-214` (`decompositions/IRPT_ANLREQ_DECOMP_R20_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~63`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-63` (branch `wk-IRPT_ANLREQ-63`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~63 <0.9.0_WK_IRPT_ANLREQ~63@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W63-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (your portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-214`, inlined) -- THE PORTAL SHOWS THE SHEETS_NOT_READ NOTICE. A CANDIDATE on a branch; nothing is landed, pushed or deployed.

*A multi-sheet workbook is read from its first sheet only, and the server says so with a NOTICE (`SHEETS_NOT_READ`, at `portfolio.findings` of the NORMALIZED answer); no portal file reads it, so no person is told.* The CTO (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_20_20261013.md` section 2, row D2-W57-S5): a portal cell shows the notice on the upload answer's face, through the CTO's review lane, DEV first.

**Read first:** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~57/r19/PORTAL_UPLOAD_ANSWER_READERS.json` (the 17 readers with file and line; rows W57-S5 and S6 in the channel) and `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~58/r19/PORTAL_DEFER_SHAPE_READERS.json` (`new_codes`: the words the server wrote for the notice: "Only the first sheet was read; 1 other sheet(s) in this workbook were not. If another sheet holds holdings you want analyzed, upload it as its own file.").

1. **The branch.** The portal repository is `C:/dev/ajb_workspace/portal` (a separate git repository). `git -C C:/dev/ajb_workspace/portal fetch origin DEV` is permitted. Record `dev_tip` (full sha of `origin/DEV`). Make a worktree OUTSIDE the product tree: `git -C C:/dev/ajb_workspace/portal worktree add C:/dev/wk-portal-63 -b wk-IRPT_ANLREQ-63-portal origin/DEV`. Never check out, reset or commit anything else in the portal checkout, and never push. Look at how an earlier candidate branch was made (`wk-IRPT_ANLREQ-51-portal-r7`: `git -C ... log`) and commit the same way; if a hook or a rule of the portal repository refuses your commit, STOP and file a row with the refusal text.
2. **The change.** Where the upload step shows the answer of a NORMALIZED upload (the composer's upload step; `ProspectComposer.tsx` and the prospect helper `prospect.ts` are the readers the previous cell listed), show every finding of the answer's `portfolio.findings` whose severity is NOTICE as a plain line under the upload result, using the server's `description` as it is (OPEN: no code table, no rewording). Do not change what is shown for NEEDS_CORRECTION, do not change any wire reader or contract file, and touch `src/` only (no `package.json`, lockfile, build or config file).
3. **The test, before and after.** Add a test in the portal's existing test folder, in the style of its neighbours, that renders (or calls the helper for) a NORMALIZED answer carrying a `SHEETS_NOT_READ` notice and asserts the notice's description is shown, and one that asserts a NORMALIZED answer with no notice shows no notice line. `before_arm`: run your new tests on `origin/DEV` WITHOUT the change (stash or a second worktree) and record that the notice test FAILS (`failed` at least 1); `tests`: run them with the change (all pass), and run the folders of the two readers you touched (counts). Use `bun` (resolve it from your profile; do not bake a path).
4. **Commit** in the portal worktree on your branch; record the full commit sha.
5. **Write `r20/PORTAL_NOTICE_CANDIDATE.json`:** `dev_tip`, `branch`, `commit`, `files_changed` (paths under `src/`), `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm` {`failed`, `output_tail`}, `what_a_person_sees` (the words as rendered), `claim`, `not_read` (the live PROD and DEV bundles; a browser render if you ran none).
6. **In your report:** the branch, the commit, the files, the before and after counts, and what a person sees. The candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; you land nothing.

### ACCEPTANCE

<criterion id="AR214-y-AC1" cell_refs="AR-y-214"><invocation>python C:/dev/wk-irpt-anlreq-63/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r20/ar20_checks.py y214-portal --root C:/dev/wk-irpt-anlreq-63</invocation><expect>Y214-PORTAL-OK</expect></criterion>
`AR214-y-AC1`: the record names a portal commit that exists in the portal repository, touching `src/` only, with at least one added test that fails on the DEV tip without the change and passes with it, and no failing test.

<criterion id="AR214-y-AC2J" cell_refs="AR-y-214" judgment="true"/>
`AR214-y-AC2J` (judgment, graded at L9, never by you): the change shows the server's notice words as they are and changes nothing for NEEDS_CORRECTION or the wire readers, the test would fail if the change were removed, and nothing was landed or pushed.

<expected_criteria>AR214-y-AC1 AR214-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~63/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R20_Y.md</decomp_doc>
<owned_cells>AR-y-214</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~63/IRPT_ANLREQ.TO-AR-y-214.portal-sheets-not-read-notice.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-214`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading AR-y-202's rows W57-S5 and S6 against the cell; the lens: a change that alters a wire reader and so repeats release 5's defect, or a test that passes without the change. The order forbids contract and reader changes (src/ presentation only) and requires a before-arm failure on the DEV tip. NOT seen: the deployed bundles and a browser render.
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-20 analysis row D2-W57-S5 as round 20 workstream `Y`. Base: `AR214-y-AC1` FAIL as expected (no record).
- Landing is the CTO's review lane (DEV first); a PROD push of a client-facing page waits on Andrew.

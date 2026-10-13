# TO IRPT_ANLREQ.TO-AR-y-202.portal-upload-answer-readers -- the portal's readers of the upload door's answer, with the pinned and the moved pair's answers passed through them

<to_id>IRPT_ANLREQ.TO-AR-y-202</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~57</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-202` (`decompositions/IRPT_ANLREQ_DECOMP_R19R6_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~57`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-57` (branch `wk-IRPT_ANLREQ-57`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~57 <0.9.0_WK_IRPT_ANLREQ~57@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W57-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs in step 1 is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-202`, inlined) -- THE PORTAL'S READERS OF THE UPLOAD DOOR'S ANSWER. Nothing is changed, deployed or applied.

*Release 5 of another function was rolled back because a portal reader refused a new answer. This cell finds out, before the reader's release, whether a portal reader would refuse these.* The moved reader adds four finding codes to the upload door's answers that the live reader never emits: `ACCOUNT_COLUMN_SEVERAL_VALUES`, `HEADER_ROW_REPEATED`, `SHEETS_NOT_READ`, `TOTAL_ROW_PRESENT`; the moved `uploads.py` adds correction words for 23 other codes.

**Read first:** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r19/START_STATE_SCRATCH_RUN.json` (the scratch run of the PINNED and the MOVED pair through the upload door: `door_cases`, `reopen_cases`, `what_a_person_sees`, `not_read`) and `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r19/scratch_tools/start_state_run.py` (the offline harness that produced the answers; read it, and run it if the record does not carry the answer bodies).

1. **The portal commits.** The portal checkout is `C:/dev/ajb_workspace/portal` (a separate git repository; READ ONLY: never check out, reset, commit or push there). `git -C C:/dev/ajb_workspace/portal ls-remote origin PROD DEV` names the two tips; if either tip object is absent locally, `git -C C:/dev/ajb_workspace/portal fetch origin PROD DEV` is permitted (it moves only remote-tracking refs). Record both full shas as `prod_commit` and `dev_commit`. All file reads are `git -C C:/dev/ajb_workspace/portal show <commit>:<path>` (with `MSYS_NO_PATHCONV=1` only on that command); runnable copies go into a NEW EMPTY folder under your `.scratch/r19/` via `git archive`.
2. **Find the readers.** Every portal source file that reads the upload door's answer or the stored input's findings: the upload call and its result type, the findings and correction rendering, the owned-request view of a stored template input. Search the portal with the native Grep and Glob tools on a scratch copy, or `git grep` at a commit (a named pathspec, not the whole tree). For each reader record `file`, `line`, what it reads, and its `key_policy`: EXACT (an unknown key or an unknown enum value is refused), TOLERANT (ignored), or OPEN (the string is shown as it is), with the line that decides it, at BOTH commits (`at_prod`, `at_dev`).
3. **Run the cases.** For each door case in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r19/START_STATE_SCRATCH_RUN.json` that has a moved-pair answer (the `NEEDS_CORRECTION` ones carry the new codes), take the answer body as the pair returns it, and pass it through each reader FROM THE PORTAL COMMIT (the function, not a copy of its logic) in a scratch copy, with `bun` (resolve it from your profile; do not bake a path) or `node` if the reader is plain. Arms: `BEFORE` = the pinned pair's answer (what is served today), `AFTER` = the moved pair's answer; commits `PROD` and `DEV`. Record per case `case`, `arm`, `commit`, `reader`, `outcome` (RETURNED or THROW, exactly `RETURNED` or `THREW`), `codes` (the finding codes in the answer), `method` (`RUN` if you ran the reader; `READ` if you could only read it, and then say why in `status_reason`), and what a person would see for each finding code (the words the portal shows, or `shown as the code`).
4. **A THREW on an AFTER case is a finding:** file a BLOCKING row naming the reader, the commit and the key; do NOT fix anything. A reader you could not find for a route is a row too (`not_read` lists it).
5. **Write `r19/PORTAL_UPLOAD_ANSWER_READERS.json`:** `prod_commit`, `dev_commit`, `readers` (objects with `file`, `line`, `reads`, `key_policy`, `at_prod`, `at_dev`), `cases` (objects as in step 3), `new_codes` (the four, each with the words a person would see at PROD and at DEV), `claim`, `not_read`.
6. **In your report:** the reader count and their key policies in one line, whether any AFTER case THREW at PROD or DEV, and what a person sees for the four new codes.

### ACCEPTANCE

<criterion id="AR202-y-AC1" cell_refs="AR-y-202"><invocation>python C:/dev/wk-irpt-anlreq-57/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r19/ar19_checks.py y202-portal --root C:/dev/wk-irpt-anlreq-57</invocation><expect>Y202-PORTAL-OK</expect></criterion>
`AR202-y-AC1`: the record names both portal commits, at least one reader with its key policy at each, and cases whose AFTER arm carries all four new finding codes, each with an outcome of RETURNED or THREW.

<criterion id="AR202-y-AC2J" cell_refs="AR-y-202" judgment="true"/>
`AR202-y-AC2J` (judgment, graded at L9, never by you): the readers are the ones the portal's upload and stored-input views really use (none left out), the cases were passed through the portal's own functions at the named commits where `method` says RUN, and the words a person sees are read from the portal and not assumed.

<expected_criteria>AR202-y-AC1 AR202-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~57/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R19R6_Y.md</decomp_doc>
<owned_cells>AR-y-202</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~57/IRPT_ANLREQ.TO-AR-y-202.portal-upload-answer-readers.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-202`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- git reads of the portal checkout and scratch copies outside the product tree; nothing is changed, deployed, uploaded or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading release 5's rollback (rows D2-S43 and D2-S44: the first pair named no portal reader) against the cell; the lens: a reader found by name but never run on the new answer, or run on a copy of its logic. The order requires the portal's own functions at the named commits for every case where it says RUN, and a row for any reader it cannot find. NOT seen: the deployed PROD bundle (only the branch tip is read).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on this seat's reading of release 5's defect (the pair must name the portal readers) as workstream `YR` round 6. Base: `AR202-y-AC1` FAIL as expected (no record).
- The PAIR and the APPLY are not this order.

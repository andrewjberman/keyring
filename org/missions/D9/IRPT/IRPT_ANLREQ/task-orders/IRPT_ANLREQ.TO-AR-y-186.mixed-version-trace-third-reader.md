# TO IRPT_ANLREQ.TO-AR-y-186.mixed-version-trace-third-reader -- the mixed-version trace extended by the Lambda's third reader (row W52-S28)

<to_id>IRPT_ANLREQ.TO-AR-y-186</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~52</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-186` (`decompositions/IRPT_ANLREQ_DECOMP_R18_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** AR-y-181 merged
**NOT SPAWNED AT ISSUANCE.** The issuer spawns this order when AR-y-181 is merged, and states it in a spawn amendment. If there is none, STOP: the order was spawned too early.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~52`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-52` (branch `wk-IRPT_ANLREQ-52`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~52 <0.9.0_WK_IRPT_ANLREQ~52@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W52-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### SPAWN AMENDMENT (issuer `2.0.0_SA_COO~Y2`, 2026-10-12)

`AR-y-181` is merged: drain @a665d34dd3 (the widened reader, `READER_VERSION = "irpt-template-reader.r18.1"`; the issuer's own runs on the shared tree: `Y181-RULE-OK`, `Y181-KEEP-OK`, 331 intake tests pass).
The trace below runs on THAT reader (`new` = r18.1). Nothing else in this order changes.

### THE CELL (`AR-y-186`, inlined) -- READ AND TRACE. Nothing is changed or called.

*The mixed-version trace extended by the Lambda's THIRD reader.* The round-17 trace ran four pairs of `old` (r16.1) and `new` (r17.1). Row `IRPT_ANLREQ-D2-W52-S28` found the Lambda carries a third, unversioned reader at pin `3f29017cfc`. This cell runs it beside the reader as widened by `AR-y-181`.

**Read first:** the round-17 trace `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r17/MIXED_VERSION_TRACE.json` and its harness `.../r17/mixed_version_trace_run.py` (reuse it; do not retype the seven sheets), row `S28` in `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`, and the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_18_20261012.md` section 1 row D2-W52-S28.

1. **Load the readers.** `lambda_pinned` = the Lambda's reader at pin `3f29017cfc` (`git show 3f29017cfc:<path>` to a temp file outside the tree under another module name; say what the path is and whether it has `READER_VERSION`); `new` = the reader as widened by `AR-y-181` (the head of this worktree).
2. **Run the pairs in process:** writer=lambda_pinned/reader=lambda_pinned, writer=lambda_pinned/reader=new, writer=new/reader=lambda_pinned, over the same seven sheets plus one header from `AR-y-181`'s new vocabulary (a `Brokerage Account` two-account sheet). For each: the OUTCOME (accepted, or refused with the code) and the evidence. A case you cannot run is INFERRED with its reason.
3. **Say what a person sees** when the Lambda is on its third reader and the resident on the new one, and whether any input accepted under one can be refused under the other at re-open.
4. **Write `r18/MIXED_VERSION_TRACE_THIRD_READER.json`:** `pin`, `cases` (objects with `writer_version`, `reader_version`, `outcome`, `evidence`; the versions are `lambda_pinned` and `new`), `claim`, `not_read`, `what_a_person_sees`.
5. **In your report:** the outcomes, any valid input refused, and the precondition the release pair must state for the Lambda's start state.

### ACCEPTANCE

<criterion id="AR186-y-AC1" cell_refs="AR-y-186"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r18/ar18_checks.py y186-trace --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y186-TRACE-OK</expect></criterion>
`AR186-y-AC1`: the record has cases that run the Lambda's pinned reader, each with an outcome and its evidence, and names the pin, the claim and what was not read.

<criterion id="AR186-y-AC2J" cell_refs="AR-y-186" judgment="true"/>
`AR186-y-AC2J` (judgment, graded at L9, never by you): each case was RUN where it could be, an inferred case says why, and no valid input is claimed safe that the runs do not show safe.

<expected_criteria>AR186-y-AC1 AR186-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R18_Y.md</decomp_doc>
<owned_cells>AR-y-186</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/IRPT_ANLREQ.TO-AR-y-186.mixed-version-trace-third-reader.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-186`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read and in-process runs; nothing is changed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the round-17 trace and row S28 against the cell; the lens: a trace that infers what it could run. Every case is RUN in process on the two readers, or marked INFERRED with its reason.
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-18 analysis items 4 and 5 (row S28). NOT SPAWNED until `AR-y-181` is merged. Base: `AR186-y-AC1` FAIL as expected (no record).

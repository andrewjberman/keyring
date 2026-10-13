# TO IRPT_ANLREQ.TO-AR-y-191.start-state-scratch-run -- the Lambda's start state RUN in a scratch tree (S33 LIVE, S35)

<to_id>IRPT_ANLREQ.TO-AR-y-191</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~52</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-191` (`decompositions/IRPT_ANLREQ_DECOMP_R19_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

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

### THE CELL (`AR-y-191`, inlined) -- READ AND RUN. Nothing is changed or called live.

*The Lambda's START STATE, MEASURED in a scratch tree, not inferred.* The round-18 trace read the Lambda's own door (`uploads.py` `f09b802cdc`) as code only and INFERRED its answers. The CVO's condition (L9 grade of round 18, `AR186-y-AC2J`): run the pinned pair in a scratch tree before the release pair is cut.

**Read first:** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r18/MIXED_VERSION_TRACE_THIRD_READER.json` and its harness, rows `IRPT_ANLREQ-D2-W52-S33`, `-S34`, `-S35` in `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`, the CVO's grade `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_18_L9_GRADE_20261013.md` (the AR186 condition), and the map entry for `irpt-ycharts-generate` in `infra/aws/lambda/ci/lambda-source-map.json` (`staged_from`: every member and its pin).

1. **Build the scratch tree OUTSIDE the product tree** (a temp folder; leave it and say where it is): for every member of the upload door's import closure that the map stages, `git show <pin>:<repo_path>` into the Lambda's flat layout (the map's `packaged_as` names). At least `uploads.py` at `f09b802cdc`, `template_reader.py` at `3f29017cfc`, and each member `uploads.py`/`upload_entry.py`/`generate_installed.py` imports at the pin the map names. Say which members you included and which you could not (and why).
2. **RUN the door** in that tree with synthetic workbooks and the folder's own fakes (copy the harness of the round-17/18 traces, do not retype the sheets): `two_value_account_sheet`, `total_row_sheet`, `one_account_sheet`, `two_sheet_workbook` (and any header from the round-18 vocabulary you can add). For each: the door's answer (accepted as NORMALIZED, or refused with the code) and the evidence (the printed value or test). A case you cannot run is marked INFERRED with its reason; the aim is zero.
3. **RUN the re-open:** write a stored template with the pinned reader (no `reader_version` member), then re-open it with (a) the pinned pair and (b) the pair after the planned move (`uploads.py` and `template_reader.py` at the head, r18.1). Record the outcome of each (S35: it was only COMPUTED in round 18). Also write a template with r18.1 and re-open it under the pinned pair (the round-18 finding: refused, TEMPLATE_ORIGINAL_BINDING), through the actual `read_input` of the pinned `uploads.py`, not by comparing reader outputs.
4. **Write `r19/START_STATE_SCRATCH_RUN.json`:** `scratch_tree` (the path), `pins` (a mapping with `uploads.py`, `template_reader.py` and each neighbour: its pin), `door_cases` (objects with `sheet`, `outcome`, `evidence`), `reopen_cases` (objects with `sheet`, `writer`, `reader`, `outcome`, `evidence`), `claim`, `not_read`, `what_a_person_sees` (what a person sees today on a two-account upload through this door).
5. **In your report:** the door's answers on the four sheets, the re-open outcomes, which case from round 18 changed from COMPUTED to RUN and whether any result differs from the round-18 trace.

### ACCEPTANCE

<criterion id="AR191-y-AC1" cell_refs="AR-y-191"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r19/ar19_checks.py y191-scratch --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y191-SCRATCH-OK</expect></criterion>
`AR191-y-AC1`: the record names the pins, runs the door on the four sheets and a re-open case, and each case carries an outcome and its evidence.

<criterion id="AR191-y-AC2J" cell_refs="AR-y-191" judgment="true"/>
`AR191-y-AC2J` (judgment, graded at L9, never by you): the door was RUN on the pinned members rather than the head's, the scratch tree holds the map's pins for the members it imports, and any INFERRED case says why.

<expected_criteria>AR191-y-AC1 AR191-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R19_Y.md</decomp_doc>
<owned_cells>AR-y-191</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/IRPT_ANLREQ.TO-AR-y-191.start-state-scratch-run.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-191`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a scratch tree outside the product tree and in-process runs; nothing is changed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CVO's condition (the pinned pair is run in a scratch tree before the pair is cut) against the cell; the lens: a scratch tree that imports the head's file by accident. The order requires each member from the map's pin and the member list named. NOT seen: the deployed Lambda's own bytes (0 live objects read).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-19 analysis item 1 (S33 LIVE, S35) and the CVO's round-18 condition. Base: `AR191-y-AC1` FAIL as expected (no record).

# TO IRPT_ANLREQ.TO-AR-y-174.mixed-version-trace -- the mixed-version trace of the re-landed reader (row W52-S18)

<to_id>IRPT_ANLREQ.TO-AR-y-174</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~52</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-174` (`decompositions/IRPT_ANLREQ_DECOMP_R17_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** AR-y-171 merged
**NOT SPAWNED AT ISSUANCE.** The issuer spawns this order when AR-y-171 is merged, and states it in a spawn amendment. If there is none, STOP: the order was spawned too early.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~52`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-52` (branch `wk-IRPT_ANLREQ-52`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~52 <0.9.0_WK_IRPT_ANLREQ~52@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W52-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`. No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add.

### SPAWN AMENDMENT (issuer `2.0.0_SA_COO~Y2`, 2026-10-12)

`AR-y-171` is merged: drain @b09e84971f (the repaired reader, `READER_VERSION = "irpt-template-reader.r17.1"`, its own checks `Y171-RULE-OK` and `Y171-KEEP-OK` run by the issuer on
the shared tree, 317 intake tests pass). The trace below runs on THAT reader: `new` = r17.1, `old` = the round-16 reader at `aaf156e8eb`. Nothing else in this order changes.

### THE CELL (`AR-y-174`, inlined) -- READ AND TRACE. Nothing is changed or called.

*What happens when the resident and a Lambda run DIFFERENT reader versions, traced on the reader as repaired by `AR-y-171`.* The round-16 worker INFERRED that a comparison runs only on equal versions, so mixed versions cannot refuse a valid input; the compile says it was not traced.

**Read first:** `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND16_Y_L8_COMPILE_20261012.md` section 2 (the unknown, said plainly), row `IRPT_ANLREQ-D2-W52-S18`, the merged reader and contract
(`intake/template_reader.py`, `intake/uploads.py` `read_input`), the contract tests `intake/tests/test_stored_input_contract.py`, and the round-14 census
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/r14/UPLOAD_DOOR_RELEASE_CENSUS.json` (21 consumers, which function packages which file).

1. **List every consumer** of `template_reader` / `READER_VERSION` / the stored template's `reader_version` member (file:line), and which deployed function or the resident packages it (from the
   map `infra/aws/lambda/ci/lambda-source-map.json` and the resident package rule; say what you read and what you did not).
2. **Run the four pairs in process**, loading the round-16 reader (`git show aaf156e8eb:<path>` to a temp file, under another module name) as `old` and the repaired reader as `new`:
   writer=old/reader=old, writer=new/reader=new, writer=old/reader=new, writer=new/reader=old. For each: write a stored template with the writer (a two-sheet workbook, a Total-row sheet,
   a two-value account sheet, a one-account sheet, and a header the repair changes), re-open it with the reader through `read_input`, and record the OUTCOME (accepted, or refused
   with the code) and the evidence (the test or the printed value). A case you cannot run is marked INFERRED with the reason.
3. **Say what a person sees** in the mixed state at the upload door and at re-open, and whether any input accepted under one version can be refused under the other. Say plainly what
   is not covered (the resident's real package, the queue between them).
4. **Write `r17/MIXED_VERSION_TRACE.json`**: `consumers` (list), `cases` (list of objects with `writer_version`, `reader_version`, `outcome`, `evidence`; the versions are `old` and `new`), `claim`, `not_read`,
   and `what_a_person_sees`. Keep any scratch test in the deliverables folder (it is not a product test).
5. **In your report:** the four outcomes; any case where a valid input is refused; the release pair's precondition you would write.

### ACCEPTANCE

<criterion id="AR174-y-AC1" cell_refs="AR-y-174"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r17/ar17_checks.py y174-trace --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y174-TRACE-OK</expect></criterion>
`AR174-y-AC1`: the trace record covers all four writer/reader pairs, each with an outcome and its evidence, and names the consumers and what was not read.

<criterion id="AR174-y-AC2J" cell_refs="AR-y-174" judgment="true"/>
`AR174-y-AC2J` (judgment, graded at L9, never by you): each case was RUN where it could be, an inferred case says why, and no valid input is claimed safe that the runs do not show safe.

<expected_criteria>AR174-y-AC1 AR174-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/` and this order's file (status flip only).
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R17_Y.md</decomp_doc>
<owned_cells>AR-y-174</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/IRPT_ANLREQ.TO-AR-y-174.mixed-version-trace.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-174`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read and in-process runs; nothing is changed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling (round-17 analysis section 1 row W52-S18: the release pair traces the mixed-version case) against the cell; the lens: a trace that infers what it could run. Every case is RUN in process on the two readers, or marked INFERRED with its reason.
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-17 analysis item 3. NOT SPAWNED until `AR-y-171` is merged (the trace runs on the repaired reader). Base: `AR174-y-AC1` FAIL as expected (no record).
- The release PAIR is the issuer's act on this record and on `AR-y-171`'s; it is not a cell.

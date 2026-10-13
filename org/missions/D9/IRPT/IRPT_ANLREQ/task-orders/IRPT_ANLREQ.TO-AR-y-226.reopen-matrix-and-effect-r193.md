# TO IRPT_ANLREQ.TO-AR-y-226.reopen-matrix-and-effect-r193 -- the re-open matrix of the r18.1 reader against r19.3, and what a person meets

<to_id>IRPT_ANLREQ.TO-AR-y-226</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~70</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-226` (`decompositions/IRPT_ANLREQ_DECOMP_R21R_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~70`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-70` (branch `wk-IRPT_ANLREQ-70`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~70 <0.9.0_WK_IRPT_ANLREQ~70@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W70-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-226`, inlined) -- WHAT MOVES WHEN THE READER GOES FROM r18.1 TO r19.3. Run in process. Nothing is released.

*Release 19 put the r18.1 reader and its `uploads.py` live in the resident and in `irpt-ycharts-generate`. The next release moves ONE member in each place: `intake/template_reader.py`, from `83ab9b45d59065f53c640803df9fd07a0ddfcc97d89c13540c20622a6bf7bd58` (r18.1) to the trunk head's (READER_VERSION `irpt-template-reader.r19.3`). `intake/uploads.py` is the same bytes on both sides (`176682cb1545435eec084376b3c37a578ca70d05f9ad5a376c0f2275f62b05ea`). The pair must say in which ORDER the two legs move and what a person meets.*

**Read first:** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/r19/` (the AR-y-191 record `START_STATE_SCRATCH_RUN.json`, if that is its name -- list the folder; its `reopen_matrix` method is the model: an input STORED by one pair is RE-OPENED by the other), `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/r21/ACCOUNT_HEADER_ALLOWLIST.json` (what r19.3 is) and `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py` (the lists `NEGATIVES` and `POSITIVES`: the header cases of this cell).

1. **Make the two readers.** From git (no network): `template_reader.py` as it was at the live release (the blob whose sha256 is `83ab9b45...`; find the commit with `git log -- infra/aws/lambda/investor-reporting/intake/template_reader.py` and check each blob's sha256) and at HEAD of your worktree. `uploads.py` at HEAD (sha256 must read `176682cb...`; say so). Put each pair (`pinned` = r18.1 reader + that uploads.py; `moved` = HEAD reader + that uploads.py) in a scratch folder OUTSIDE the product tree with the intake package they import (the model run shows how AR-y-191 laid them out). Record the sha256 of each file and each side's `READER_VERSION`.
2. **The re-open matrix, run.** For the input set AR-y-191 used (add the one-account, two-account, total-row, repeated-header and two-sheet cases; at least 8 stored inputs per side where the cases allow): STORE each case with the pinned pair and with the moved pair (the stored input carries `reader_version` and its original binding), then RE-OPEN each stored input with BOTH pairs. Four cells: stored `pinned`/`moved` x reopened `pinned`/`moved`; each with `cases`, `accepted`, `refused` and the refusal codes seen. The expected shape (to CONFIRM, not to assume): pinned-stored inputs are accepted by both. If any pinned-stored input is REFUSED by the moved pair, that is a BLOCKING row (the leg order and the release rest on it).
3. **The effect table.** Run `_several_accounts`/`read_template` of BOTH readers over every header case of `NEGATIVES` and `POSITIVES` in `ar21_checks.py` (and the AR-y-191 harness cases: two-account, total row, one-account, repeated header, two sheets). One row per case: `header`, `values` shape (no real data; the synthetic values of the lists), `before` (r18.1 outcome and finding codes), `after` (r19.3 outcome and finding codes). Expected: every NEGATIVE reads NORMALIZED after; every POSITIVE reads NEEDS_CORRECTION with `ACCOUNT_COLUMN_SEVERAL_VALUES` after; say which of the POSITIVES r18.1 already turned back. A NEGATIVE that r18.1 accepts and r19.3 turns back, or the reverse, is a finding: name it.
4. **Write `r21/REOPEN_AND_EFFECT.json`:** `pinned` {`template_reader_sha256`, `uploads_sha256`, `reader_version`, `source_commit`}, `moved` (same keys), `reopen_matrix` (a list of four objects: `stored_by`, `reopened_by`, `cases`, `accepted`, `refused`, `refusal_codes`), `effect_table` (list of objects: `header`, `before`, `after`, `changed` true or false), `findings`, `claim`, `not_read`.
5. **In your report:** the four cells in one line each, the number of effect rows that changed, and anything that surprised you.

### ACCEPTANCE

<criterion id="AR226-y-AC1" cell_refs="AR-y-226"><invocation>python C:/dev/wk-irpt-anlreq-70/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y226-effect --root C:/dev/wk-irpt-anlreq-70</invocation><expect>Y226-EFFECT-OK</expect></criterion>
`AR226-y-AC1`: the record carries the four cells of the matrix with cases = accepted + refused, every pinned-stored input accepted by the moved pair, the two readers' hashes, and an effect row for every header case with the r19.3 outcome the allowlist ruling names.

<criterion id="AR226-y-AC2J" cell_refs="AR-y-226" judgment="true"/>
`AR226-y-AC2J` (judgment, graded at L9, never by you): the matrix was RUN in process on the two real reader files from git (not recalled from the AR-y-191 record), both stores and both re-opens were executed for every case, and the effect rows come from running the readers, not from the allowlist's description.

<expected_criteria>AR226-y-AC1 AR226-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~70/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R21R_Y.md</decomp_doc>
<owned_cells>AR-y-226</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~70/IRPT_ANLREQ.TO-AR-y-226.reopen-matrix-and-effect-r193.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-226`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR226-y-AC1,AR226-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- in-process runs of two reader files read from git, in scratch folders outside the product tree; nothing is uploaded, deployed, applied or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the r19 pair's section 2 (the order of the legs rests on the matrix) against the cell; the lens: a matrix recalled from a record and not re-run on r19.3, or a store step that skipped the original-binding write. The order requires both stores and both re-opens per case and a BLOCKING row if the moved pair refuses a pinned-stored input. NOT seen: the host's stored population.
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-21 analysis section 3 items 1 and 4 as workstream `YR` round 14. Base: `AR226-y-AC1` FAIL as expected (no record).
- The PAIR and the APPLY are not this order.

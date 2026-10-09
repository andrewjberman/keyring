# TO-AR-y-11 -- the analysis submission carries the ticket id (FWD-1 hop 4a)

<to_id>IRPT_ANLREQ.TO-AR-y-11</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~1</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~Y | **Decomp cell:** `AR-y-11` (`decompositions/IRPT_ANLREQ_DECOMP_R1.md`)

---

## WORKER FACE

### Read first

`org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md`, the "Interfaces" table, rows I1 and I2. Your cell
implements exactly those two rows.

### THE CELL

The Ticket Center form will file an Analysis Request in three steps, all as the signed-in filer:
1. the upload;
2. the ticket, which returns `ticket_id`;
3. `POST .../analysis`.

For the backend to finish the request by itself, every later hop must know which ticket the analysis belongs to. **Make the analysis
submission carry the ticket id from submission to the acceptance record.**

1. **Admit the field.** `infra/aws/lambda/investor-reporting/ycharts/generate/submission.py`, `validate_public_request` (line 45).
   - Admit ONE optional field, `ticket_id`.
   - It must match `^TCK-\d{8}-[0-9a-f]{8}$` (the ticket API's own id shape, `infra/aws/lambda/ticket_center/lambda_function.py:125`);
     otherwise refuse with `SubmissionRefused("TICKET_REFERENCE")`.
   - It is admitted only with an `input_id` basis (a prospect submission). With a custody basis, refuse `TICKET_REFERENCE`.
   - Absent, the behaviour is byte-identical to today.
2. **Persist it.** Find where the accepted request record is written. Start at `ycharts/generate/acceptance.py`; read the submit
   path from `ycharts/generate/entry.py:97` `submit_analysis` into the configured service.
   - Store `ticket_id` on that record when present.
   - A replay of the same `request_id` with a different (or newly added or removed) `ticket_id` must refuse through the existing
     idempotency-conflict path, never overwrite.
3. **Do NOT change the queue message.** `analysis_generate` stays `{tenant, request_id, revision, composition_sha256}`
   (`acceptance.py:166-168`; checked byte-for-byte at `resident_worker.py:584`). Later hops read `ticket_id` from the record.
4. **Test.** Add `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ticket_binding.py`. It is offline, with fake clients
   and the modules' own seams. It proves:
   - (a) a prospect submission with a valid `ticket_id` is accepted and the stored record carries it;
   - (b) a malformed `ticket_id` refuses `TICKET_REFERENCE` and stores nothing;
   - (c) `ticket_id` with a custody basis refuses `TICKET_REFERENCE`;
   - (d) a replay with another `ticket_id` refuses and leaves the stored value unchanged;
   - (e) the `analysis_generate` message bytes for a ticketed request equal those for the same request without a ticket.

If a JSON contract for this request body exists that the served path validates against, add `ticket_id` there too, and name the file
in your report. If it lives outside `<paths>`, stop and file a row.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR11-y-AC1" cell_refs="AR-y-11"><invocation>python -m pytest -q -p no:cacheprovider infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ticket_binding.py</invocation><expect>passed</expect></criterion>

<criterion id="AR11-y-AC2" cell_refs="AR-y-11"><invocation>python -m pytest -q -p no:cacheprovider infra/aws/lambda/investor-reporting/ycharts/generate/tests</invocation><expect>0 failed</expect></criterion>

<criterion id="AR11-y-AC3" cell_refs="AR-y-11"><invocation>bash org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r71/y71_ac2.sh</invocation><expect>symbol_closure PASS</expect></criterion>

<expected_criteria>AR11-y-AC1,AR11-y-AC2,AR11-y-AC3</expected_criteria>

- AC1: at least 5 passed and 0 failed.
- AC2: no `failed` in the summary line. The issuer's base reading at box/dell2 HEAD 15471abe15 is `437 passed, 30 skipped, 1 xfailed`.
- AC3: `missing=0`.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no upload, no AWS calls, no installs.
- Every `.py` edit passes `.tools/commit-gate.sh`.
- **Refusal clause.** If a criterion cannot be met as written: stop, file a row, report, and do not weaken a check.
- **Rows** are `IRPT_ANLREQ-W1-S<k>`, in `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`
  (create it if absent, in the shape of `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`). Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~1" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~1@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~1 <0.9.0_WK_IRPT_ANLREQ~1@opal.agent>" -F <msgfile> -- <paths>`.
  Write the message file with the Write tool; no pre-`git add`; edit byte-preserving; ASCII only; use the native Grep/Glob/Read tools.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/submission.py
infra/aws/lambda/investor-reporting/ycharts/generate/acceptance.py
infra/aws/lambda/investor-reporting/ycharts/generate/entry.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ticket_binding.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~1/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-11.analysis-carries-ticket-id.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md</decomp_doc> round 1, workstream ~Y, cell `AR-y-11`.
<owned_cells>AR-y-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR11-y-AC1, AR11-y-AC2, AR11-y-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~1/IRPT_ANLREQ.TO-AR-y-11.analysis-carries-ticket-id.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR11-y-AC1,AR11-y-AC2,AR11-y-AC3` BEFORE the flip to complete. Shape:
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~223/IRPT_BCKEND.TO-IB-yr-761.install-custody-factory.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- where the record is written, and the field name stored;
- any contract file changed;
- the diff summary;
- the commit hashes and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one optional request field and one record field; submission.py/acceptance.py are staged in irpt-status, entry.py in irpt-ycharts-generate (lambda-source-map.json); queue message bytes unchanged by construction (criterion arm e); nothing deploys in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is added or changed; the filer's existing route authority is unchanged.
comp-routes: DECLARED-NOT-APPLICABLE -- no route or authorizer change; one optional field inside the existing POST /analysis body.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched.
comp-adversary: RUN -- AC1 at base FAILs (no file); arms (b)-(d) are refusals and arm (e) the unchanged-message control; AC2 at base 437 passed/0 failed; AC3 at base PASS.
lane: the <paths> block IS the grant (worker_grant).
</preflight>

# TO IRPT_ANLREQ.TO-AR-y-471.overview-pdf-route-binding-read-and-test-on-the-real-writer-shapes -- READ AND TEST OFFLINE: does the status route that opens a request's Opal Overview PDF (`pdf`, binding ANALYSIS_PDF_BINDING) accept a report built the way the real writers build it; no code is changed, nothing is released

<to_id>IRPT_ANLREQ.TO-AR-y-471.overview-pdf-route-binding-read-and-test-on-the-real-writer-shapes</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~345</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ130</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-471` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-9 (Andrew opens the Opal Overview PDF from the ticket) | **depends_on:** CTO msgs 11508 and 11510, run 7c (the commentary route's defect, AR-y-470)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~345`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-345` (branch `wk-IRPT_ANLREQ-345`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~345 <0.9.0_WK_IRPT_ANLREQ~345@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W345-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy, and NO edit of any source file outside your new test file.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first), with `to_id` exactly the order's id, a `controls.mutant` that FIRES and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "AR471-y-AC1,AR471-y-AC2,AR471-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID.

### THE CELL (`AR-y-471`, inlined)

*Context.* Run 7c's commentary-PDF route refused because it compared two different shas (AR-y-470). The route a person uses to open the Opal Overview report itself is `GET analysis/requests/{REQ}/pdf` (`infra/aws/lambda/investor-reporting/ops/entry.py:245`, route `analysis-request-pdf`), method `pdf` of `infra/aws/lambda/investor-reporting/ops/owned_report.py` (near lines 305-333). For an OPAL_ENGINE report it requires `release.protected_pdf_ref` to be a dict with `server_only` true and a 64-hex `sha256`, and the report's `opal_artifact` member to carry the SAME `sha256` and a positive integer `byte_length`; otherwise `ANALYSIS_PDF_BINDING`. No run has read this route live, so it is unmeasured. The CTO's static reading (msg 11510): the two shas must come from the same retained PDF.

*The read and the test.* Write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~345/PDF_ROUTE_READ.md` with exactly these four sections, each heading starting `## S1 `, `## S2 `, `## S3 `, `## S4 `, every claim carrying a `path:line` cite re-read in this worktree: **S1** where `release.protected_pdf_ref` (its `sha256`, `storage_key`, `server_only`) is set, from the writer that stores the report record through to what `read` returns (the publisher `infra/aws/lambda/investor-reporting/ycharts/generate/publisher.py` and the report/index writers; follow it); **S2** where the report's `opal_artifact` member (`sha256`, `byte_length`) is set; **S3** whether the two `sha256` values are the same value for an Opal Overview produced by `ycharts/research/opal_producer.py` (the producer retains `overview.pdf`): say 'same' with the two cites, or give the counterexample (which values differ and why); **S4** the test below and its result. Then write `infra/aws/lambda/investor-reporting/ops/tests/test_pdf_route_real_shapes.py` (offline): build the report record NOT by hand-typing both shas but by calling the real writer functions you found in S1 and S2 with fakes for their ports (or, if they cannot be called offline, by loading the producer's and publisher's own test fixtures), then call `pdf()` on it with a recording signer; assert it answers a link signed with the PDF's sha and does not raise `ANALYSIS_PDF_BINDING`. Add a negative case in the same file: a record whose two shas differ raises `ANALYSIS_PDF_BINDING`. Run it and put ONE line in the record, exactly `RESULT: PASS` (the route accepts a report built by the real writers) or `RESULT: FAIL <one clause naming the mismatch>` (it does not). A FAIL is not a failure of this order: it is the finding. If it is FAIL, also file a BLOCKING surprise row naming the two writers and the differing values. End the file with one line `NOT-READ: <what you did not or could not read, or none>`.

---

## ACCEPTANCE

<criterion id="AR471-y-AC1" cell_refs="AR-y-471"><invocation>grep -c -E '^## S[1-4] ' org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~345/PDF_ROUTE_READ.md</invocation><expect>^4$</expect></criterion>
<criterion id="AR471-y-AC2" cell_refs="AR-y-471"><invocation>grep -c -o -E '[A-Za-z0-9_./-]+\.py:[0-9]+' org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~345/PDF_ROUTE_READ.md</invocation><expect>^([6-9]|[1-9][0-9]+)$</expect></criterion>
<criterion id="AR471-y-AC3" cell_refs="AR-y-471"><invocation>grep -c -E '^(RESULT: (PASS|FAIL .+)|NOT-READ: .+)$' org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~345/PDF_ROUTE_READ.md</invocation><expect>^2$</expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~345/IRPT_ANLREQ.TO-AR-y-471.overview-pdf-route-binding-read-and-test-on-the-real-writer-shapes.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-471.overview-pdf-route-binding-read-and-test-on-the-real-writer-shapes`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR471-y-AC1,AR471-y-AC2,AR471-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-471</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/lambda/investor-reporting/ops/tests/test_pdf_route_real_shapes.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~345/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-471.overview-pdf-route-binding-read-and-test-on-the-real-writer-shapes.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one new offline test file and a record in the worker deliverables; no source change, no AWS call, no deploy.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the CTO's msgs 11508 and 11510 and the route source against this cell; the lens: a test that types both shas by hand and so proves nothing about the writers, a cite to a line that does not carry the claim (re-read every cite), a PASS reported when the real writers could not be called and the fixtures were hand-built, the commentary route's defect confused with this route's. NOT seen (blind): the live artifact index and a real retained Overview PDF; denominator: four sections.
</preflight>

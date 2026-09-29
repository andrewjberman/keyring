# TO IRPT_BCKEND.TO-IB-yr-221 -- A resolve_upload RETRY is bounded below the DLQ: give up on the message by name, keep the row

<to_id>IRPT_BCKEND.TO-IB-yr-221</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~73</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~Y | **Decomp cell:** `IB-yr-221` (`decompositions/IRPT_BCKEND_DECOMP_R22_Y.md`)
| **outcome_ref:** FWD-4 backend half (upload resolution never stuck) | **depends_on:** IB-yr-211 (drained @14c961af32)

---

## WORKER FACE

### THE CELL

`IB-yr-221` -- in `C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py`,
`poll_once` re-offers a `resolve_upload` RETRY every `RESOLVE_RETRY_VISIBILITY_S` (60 s). The live queue's
RedrivePolicy dead-letters a message on its 5th receive (maxReceiveCount 5), so a resolve that keeps failing lands in
the DLQ after about 5 minutes, and its NORMALIZATION row stays RESOLVING. The existing recovery path is the client's
own poll: `C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/lambda/investor-reporting/intake/uploads.py`
`_answer` re-dispatches a RESOLVING row whose `dispatched_at` is older than `REDRIVE_SECONDS` (960 s). So the bound
is: stop re-offering one message before SQS dead-letters it, and leave the row for that redrive.

**Build (in `resident_worker.py` only):**
1. Add a module constant `RESOLVE_MAX_RECEIVES = 4`, with a comment naming the live maxReceiveCount of 5.
2. In `poll_once`, ask SQS for the receive count on every receive: `receive_message(..., AttributeNames=["ApproximateReceiveCount"])`
   (keep MaxNumberOfMessages, WaitTimeSeconds and VisibilityTimeout exactly as they are).
3. For a `resolve_upload` whose result state is `RETRY`: read `int(envelope.get("Attributes", {}).get("ApproximateReceiveCount", "1"))`.
   If it is >= `RESOLVE_MAX_RECEIVES`, DELETE the message, print exactly
   `IRPT_RESIDENT_RESOLVE state=GAVE_UP code=RESOLVE_RETRY_EXHAUSTED` (flush=True) INSTEAD of the RETRY line, and
   do NOT change visibility. Otherwise keep today's IB-yr-211 behaviour: the RETRY line and the 60 s re-offer.
4. Do NOT write the NORMALIZATION row: it stays RESOLVING for the client poll's redrive. Generation messages are
   unchanged.
5. Do not change existing tests; you may add tests to `.../ycharts/generate/tests/test_resolve_upload.py`.

### ACCEPTANCE (run from your worktree root)

<criterion id="Y22-1-AC1" cell_refs="IB-yr-221"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R22_CHECKS/test_r22_y1_resolve_bounded.py::test_gives_up_by_name_before_the_dlq</invocation><expect>1 passed</expect></criterion>
`Y22-1-AC1` -- at receive count `RESOLVE_MAX_RECEIVES` a RETRY deletes the message, prints the GAVE_UP line, and the
row reads RESOLVING. Base: `RESOLVE_MAX_RECEIVES` absent.

<criterion id="Y22-1-AC2" cell_refs="IB-yr-221"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R22_CHECKS/test_r22_y1_resolve_bounded.py::test_asks_sqs_for_the_receive_count</invocation><expect>1 passed</expect></criterion>
`Y22-1-AC2` -- `poll_once` asks SQS for `ApproximateReceiveCount` on every receive. Base: no AttributeNames.

<criterion id="Y22-1-AC3" cell_refs="IB-yr-221"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R22_CHECKS/test_r22_y1_resolve_bounded.py::test_early_retry_is_kept_and_reoffered</invocation><expect>1 passed</expect></criterion>
`Y22-1-AC3` -- the difference control: at receive count 1 a RETRY is kept with the 60 s re-offer, and the row reads
RESOLVING. Passes at the base and must still pass.

<expected_criteria>Y22-1-AC1,Y22-1-AC2,Y22-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. The check in
  `R22_CHECKS/` and `intake/uploads.py` are READ-ONLY. No AWS call, no deploy, no queue change, no Terraform.
- **Served code moves only through 2.0.0_SA_COO~P's st4 rebuild**, never by you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the test to pass.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resolve_upload.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R22_Y.md</decomp_doc> round 22, workstream ~Y, cell `IB-yr-221`.
<owned_cells>IB-yr-221</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y22-1-AC1, Y22-1-AC2, Y22-1-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~73/IRPT_BCKEND.TO-IB-yr-221.resolve-retry-bounded-below-the-dlq.proof_of_spec.json`
(the ORDER FILE's basename), validated with `python .tools/proof-of-spec-check.py <instance> Y22-1-AC1,Y22-1-AC2,Y22-1-AC3`
BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** each criterion's output line, the diff summary, and the commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched; one source file.
comp-blast: DECLARED-NOT-APPLICABLE -- one resident source file; nothing served moves in this cell (~P rebuilds st4).
comp-iam: DECLARED-NOT-APPLICABLE -- receive_message AttributeNames and delete_message are calls the resident role already makes on the same queue.
comp-adversary: RUN -- the risk is losing an upload: giving up deletes the MESSAGE only; the ROW stays RESOLVING and the client poll's REDRIVE_SECONDS path re-dispatches it (intake/uploads.py _answer), so nothing is dropped and nothing sits in the DLQ. Scanned 2 files (resident_worker.py poll_once, intake/uploads.py _answer) plus the live RedrivePolicy (maxReceiveCount 5); blind to the live SQS count under a resident restart mid-lease, which the check's fake does not model.
lane: the <paths> block IS the grant; no open order holds these files.
</preflight>

Source: CTO condition 102655 (signoff @1576687ade), ~P 102659, decomposition R22_Y.

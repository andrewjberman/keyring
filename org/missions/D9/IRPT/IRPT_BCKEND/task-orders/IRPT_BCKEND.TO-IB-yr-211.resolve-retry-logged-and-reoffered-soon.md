# TO IRPT_BCKEND.TO-IB-yr-211 -- A resolve_upload RETRY is logged with its code and re-offered soon, not after the 900 s lease

<to_id>IRPT_BCKEND.TO-IB-yr-211</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~71</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~Y | **Decomp cell:** `IB-yr-211` (`decompositions/IRPT_BCKEND_DECOMP_R21_Y.md`)
| **outcome_ref:** FWD-4 backend half (upload resolution latency) | **depends_on:** IB-yr-201 (drained @f287444013)

---

## WORKER FACE

### THE CELL

`IB-yr-211` -- in window 21, 3 of 7 Analysis uploads sat in RESOLVING for over 10 minutes; one (Y4) resolved exactly
15 minutes after upload. The mechanism, read at the source in
`C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py`:
- `ResidentAssembly.resolve_upload` returns `{"state": "RETRY", "detail": {"code": str(exc)}}` when the vendor resolver
  raises `ResolutionUnavailable`.
- `poll_once` (line ~413) receives with `VisibilityTimeout=900` and deletes the message only on READY or ATTENTION
  (line ~432-433). A RETRY therefore waits the whole 900 s generation lease before it is offered again.
- Nothing prints a resolve outcome, so a stuck upload is invisible in the journal.

**Build (in `resident_worker.py` only):**
1. Add a module constant `RESOLVE_RETRY_VISIBILITY_S = 60`.
2. In `poll_once`, after `result = assembly.execute(...)`: when the message is a `resolve_upload` (its decoded body has
   `kind == "resolve_upload"`), print exactly one line
   `IRPT_RESIDENT_RESOLVE state=<result["state"]> code=<result.get("detail", {}).get("code", "-")>` (flush=True). Print
   no id, tenant, file name or body. When that state is `RETRY`, call `sqs.change_message_visibility(QueueUrl=...,
   ReceiptHandle=..., VisibilityTimeout=RESOLVE_RETRY_VISIBILITY_S)` as the LAST visibility change for that message.
3. Generation messages (`analysis_generate`) keep today's behaviour exactly: no new line, no visibility change.
4. Do not change existing tests; you may add tests to
   `.../ycharts/generate/tests/test_resolve_upload.py`.

### ACCEPTANCE (run from your worktree root)

<criterion id="Y21-1-AC1" cell_refs="IB-yr-211"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R20_CHECKS/test_r20_y2_resolve_retry.py::test_retry_is_logged_and_reoffered_soon</invocation><expect>1 passed</expect></criterion>
`Y21-1-AC1` -- a provider outage keeps the message, the last visibility change is `RESOLVE_RETRY_VISIBILITY_S` (<= 120),
and an `IRPT_RESIDENT_RESOLVE state=RETRY code=` line prints. Base: the constant is absent.

<criterion id="Y21-1-AC2" cell_refs="IB-yr-211"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R20_CHECKS/test_r20_y2_resolve_retry.py::test_ready_still_deletes_and_is_logged</invocation><expect>1 passed</expect></criterion>
`Y21-1-AC2` -- a successful resolve still deletes its message (the suite's own success test, re-run) and prints
`IRPT_RESIDENT_RESOLVE state=READY`. Base: the line is missing.

<expected_criteria>Y21-1-AC1,Y21-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. The check in
  `R20_CHECKS/` is READ-ONLY. No AWS call, no deploy, no vendor call.
- **Served code moves only through 2.0.0_SA_COO~P's next resident build**, never by you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the test to pass.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resolve_upload.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R21_Y.md</decomp_doc> round 21, workstream ~Y, cell `IB-yr-211`.
<owned_cells>IB-yr-211</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y21-1-AC1, Y21-1-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~71/IRPT_BCKEND.TO-IB-yr-211.resolve-retry-logged-and-reoffered-soon.proof_of_spec.json`
(the ORDER FILE's basename), validated with `python .tools/proof-of-spec-check.py <instance> Y21-1-AC1,Y21-1-AC2`
BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** each criterion's output line, the diff summary, and the commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched; source and test files only.
comp-blast: DECLARED-NOT-APPLICABLE -- one resident source file; nothing served moves in this cell (~P ships the resident).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; change_message_visibility is already a call poll_once makes on the same queue.
comp-adversary: RUN -- a short re-offer must not spin: a RETRY waits 60 s, and a generation message is untouched (build step 3), so the 900 s generation lease that the read-back retain relies on is unchanged.
lane: the <paths> block IS the grant; no open order holds these files.
</preflight>

Source: row S193 (@ff20be749a); decomposition R20_Y (deferred) and R21_Y; W21 part-Y record @a89e14436b.

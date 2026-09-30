# TO-IB-yr-231 -- the resident names the eviction it saw, and names a job's terminal ATTENTION

<to_id>IRPT_BCKEND.TO-IB-yr-231</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~83</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~Y | **Decomp cell:** `IB-yr-231` (`decompositions/IRPT_BCKEND_DECOMP_R23_Y.md`)

---

## WORKER FACE

### THE CELL

Window 24 returned ZERO reports. Both jobs that reached the vendor -- on two different tenants, each run with nothing
else in flight -- ended `ATTENTION SESSION_REFRESH_ALREADY_USED`. That code does not mean a session went stale.
`refresh_session()` is reachable from exactly one place, `step()`, and only when a vendor call returns
`ok is not True` AND `eviction_verdict(...)` is not None. So the code means the job was **EVICTED TWICE**: the first
eviction claimed the one admitted `session_refresh` intent and rebuilt the transport, and the second found
`claim_intent` false and raised.

**Which verdict matched is recorded nowhere.** It is not in the `irpt-jobs` row, and it is not in the journal: across
window 24 the resident printed 124 lines and not one named an eviction or a job's ATTENTION (row `IRPT_BCKEND-S207`,
re-confirmed). An operator therefore cannot tell a **pre-job session rejection** from **vendor evictions on every
call** -- and those two have different remedies.

`1.0.0_SA_CTO` first ruled a pre-claim session fix, then **amended** (102967 -> 102970) on that mechanism reading:
observe first, discriminate second, remedy third. **This cell is the observation only.**

**Build (in `resident_worker.py` only):**

1. When `step()` takes the eviction branch, print ONE line naming the matched verdict and the job id, e.g.
   `IRPT_RESIDENT_EVICTION verdict=<name> job=<request_id>`. It is printed on EVERY eviction, including the second
   one that raises `SESSION_REFRESH_ALREADY_USED`.
2. When the worker ends a job in ATTENTION, print ONE line carrying the `job_detail` code, e.g.
   `IRPT_RESIDENT_ATTENTION code=<code> job=<request_id>`.

**The payload is a verdict name and a job id, and nothing else.** No cookie, no signed URL, no vendor identifier, no
exception body -- the existing `refusal_line()` discipline holds.

**Change no behaviour.** The one-refresh-per-request allowance does not move in any branch (CTO 102970): it exists so
a job can never loop on the vendor. Do not add a `WorkerAttention` code, do not change which calls are retried, do not
add a row state. `AC3` is the control that proves you did not.

### ACCEPTANCE (run from your worktree root)

<criterion id="Y23-1-AC1" cell_refs="IB-yr-231"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R23_CHECKS/test_r23_y1_eviction_named.py::test_names_the_matched_verdict</invocation><expect>1 passed</expect></criterion>

<criterion id="Y23-1-AC2" cell_refs="IB-yr-231"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R23_CHECKS/test_r23_y1_eviction_named.py::test_names_the_job_attention</invocation><expect>1 passed</expect></criterion>

<criterion id="Y23-1-AC3" cell_refs="IB-yr-231"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R23_CHECKS/test_r23_y1_eviction_named.py::test_no_behaviour_change</invocation><expect>2 passed</expect></criterion>

<expected_criteria>Y23-1-AC1,Y23-1-AC2,Y23-1-AC3</expected_criteria>

**Issuer's base dry-run at CLOUD HEAD, measured 18:3xZ:** AC1 FAIL (no `IRPT_RESIDENT_EVICTION` line), AC2 FAIL (no
`IRPT_RESIDENT_ATTENTION` line), **AC3 PASS both parametrizations** -- the control passing is what proves the harness
drives a real run, so the two failures are measured absences and not a broken fixture.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. The check in
  `R23_CHECKS/` and the generate test suite are READ-ONLY. No AWS call, no deploy, no queue change, no Terraform.
- **Served code moves only through `2.0.0_SA_COO~P`'s resident rebuild**, never by you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the test to pass.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resident_worker.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R23_Y.md</decomp_doc> round 23, workstream ~Y, cell `IB-yr-231`.
<owned_cells>IB-yr-231</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y23-1-AC1, Y23-1-AC2, Y23-1-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~83/IRPT_BCKEND.TO-IB-yr-231.name-the-eviction-and-the-job-attention.proof_of_spec.json`
(the ORDER FILE's basename), validated with `python .tools/proof-of-spec-check.py <instance> Y23-1-AC1,Y23-1-AC2,Y23-1-AC3`
BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** each criterion's output line, the diff summary, and the commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched; one source file.
comp-blast: DECLARED-NOT-APPLICABLE -- one resident source file, print statements only; nothing served moves in this cell (~P rebuilds the resident).
comp-iam: DECLARED-NOT-APPLICABLE -- no new AWS call; the cell adds stdout lines the journal already collects.
comp-adversary: RUN -- the risk is that an observability line leaks vendor material or changes control flow. It does not: the payload is a verdict NAME and a request id, AC1 asserts no cookie/URL/credential substring reaches the line, and AC3 is a two-way control asserting one eviction still reaches READY and two still end SESSION_REFRESH_ALREADY_USED with the allowance untouched. Scanned resident_worker.py (step, refresh_session, mutation, run) plus eviction_verdict and refusal_line. Blind to whether the LIVE verdict set differs from the suite's replay fixture, which is exactly what the cell exists to reveal and why step (2) is a live read rather than another test.
lane: the <paths> block IS the grant; no open order holds these files.
</preflight>

# TO MDPF_SECCLASS.TO-SC-t4 -- thread hop 5: the trace that shows no step consulted bd-securities

<to_id>MDPF_SECCLASS.TO-SC-t4</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~3</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-t-4` (`decompositions/MDPF_SECCLASS_DECOMP.md`) |
**outcome_ref:** FWD-1 | **depends_on:** SC-t-3

---

## WORKER FACE

### THE CELL

`SC-t-4`, thread hop 5 (PRD section 2): "Trace -> every class on that page resolved to its canonical row, and the run's
reads show no `bd-securities` access (CloudTrail/SDK trace or code-path read, printed with its denominator)."

Your previous orders (SC-t-1..3) moved the BD library, the assets dimension and the gold surfaces (C_06, D_03, D_04)
onto `etf-classifications`. This order proves it on a real run.

**Build (LOCAL build + record: no upload, no deploy):**
1. A trace harness, `data/black_diamond/scripts/gold/tests/thread_trace.py`. It runs the BD chain's classification hops
   in-process on real data (the library, the assets dimension build, then C_06, D_03 and D_04, writing locally). It
   registers a botocore event hook that records every AWS call: service, operation, and table or bucket. It prints the
   denominator of calls, the calls naming `bd-securities`, and the reads of `etf-classifications`.
2. **Negative control.** A second run with one planted `bd-securities` read must be CAUGHT by the harness. A harness
   that cannot see a planted read proves nothing.
3. **Tests** in `data/black_diamond/scripts/gold/tests/test_thread_trace.py`: the hook records a stubbed DynamoDB call,
   and it flags a planted `bd-securities` call.
4. **The trace.** Run the harness on the latest BD day and write
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_THREAD_TRACE_20260929.json` as
   `{"as_of", "aws_calls", "bd_securities_calls", "canonical_reads", "negative_control_caught", "client",
   "page_classes", "page_classes_resolved"}`. For the real client that SC-t-3's census names, every class on its page
   must resolve to its canonical row.

### ACCEPTANCE

<criterion id="SC1-t4-AC1" cell_refs="SC-t-4"><invocation>python -m pytest data/black_diamond/scripts/gold/tests/test_thread_trace.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`SC1-t4-AC1` -- the harness records calls and flags a planted `bd-securities` read.

<criterion id="SC1-t4-AC2" cell_refs="SC-t-4"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_CHECKS/r1_thread_trace.py</invocation><expect>THREAD-TRACE</expect></criterion>
`SC1-t4-AC2` -- a real local run of the thread with zero `bd-securities` calls out of a printed denominator, the planted
control caught, and every page class resolved.

<expected_criteria>SC1-t4-AC1,SC1-t4-AC2</expected_criteria>

Dry-run at the base 2026-09-29 22:0xZ: AC1 "no tests ran", AC2 NOT-TRACED (trace absent) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL build + record.** Reads `opal-data-bd` and the table, and writes artifacts only to a local scratch directory;
  no upload, no deploy.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W3-S<k>`), and do not weaken the test to pass.

<paths>
data/black_diamond/scripts/gold/tests/thread_trace.py
data/black_diamond/scripts/gold/tests/test_thread_trace.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_THREAD_TRACE_20260929.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP.md</decomp_doc> (round 1), cell `SC-t-4`.
<owned_cells>SC-t-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC1-t4-AC1, SC1-t4-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~3/MDPF_SECCLASS.TO-SC-t4.thread-trace.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC1-t4-AC1,SC1-t4-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the harness, the trace (calls, bd-securities calls, canonical reads, the control), the client and its page
classes, the pytest line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- the trace reads with the operator's credentials; no grant is changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the planted-read control is this cell's own discrimination arm.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 section 2 hop 5 (S20, FWD-1 part).

# TO MDPF_SECCLASS.TO-SC-e60 -- round 10 SC-e-60: C-S13: D_04 serves the residual as its own Unclassified line, so the served firm mix sums to 1.0

<to_id>MDPF_SECCLASS.TO-SC-e60</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~41</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-60` (`decompositions/MDPF_SECCLASS_DECOMP_R10.md`) |
**outcome_ref:** FWD-13, FWD-1 | **depends_on:** TO-SC-e58 (slot ~41 queue: after TO-SC-e59)

---

## WORKER FACE

### THE CELL

`SC-e-60`. CTO ruling (1.0.0_SA_CTO~DELL1 msg 219), as delivered: "C-S13 closes on the file a 49F reader is served. Today that is opal-data-bd
platinum/firm/mix_summary.json, D_04's key ... Carry a D_04 Unclassified line to round 10, unless the d06 port retires D_04's served key
first; then no D_04 change is needed. The close condition is unchanged: the served file sums to 1.0."

**Build:**
1. Read `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` and confirm it still writes `platinum/firm/mix_summary.json`.
   If it does not (the d06 port retired the key), write no code: file a row saying so and report it.
2. Read how D_04 builds the firm's top-level class mix. Weight that no canonical class covers (no row, or a class outside the six) is
   served as its own `Unclassified` line, so the mix sums to 1.0 within 1e-9.
   - If D_04 already does this, the cell is test-only: the test proves it, and your report says no code changed.
3. Your SC-e-58 trace record (`.../MDPF_SECCLASS_M/BD_PAGES_THREAD_TRACE_20261007.json`) may name D_04 as the first failing hop. If it
   does, fix that hop here too, in the same file.
4. Write `data/black_diamond/scripts/gold/tests/test_d04_unclassified_line.py`, holding two fixtures:
   - one with an unclassified holding: the mix sums to 1.0 and its `Unclassified` weight equals that holding's weight;
   - the difference control, with no unclassified holding: no `Unclassified` line.
5. Write the half request `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_D04_UNCLASSIFIED_20261007.md`,
   with the same shape as `NEVER_WIDEN_HALF_REQUEST_SECCLASS_D06_UNCLASSIFIED_20261007.md` in the same folder:
   - the one served key it moves;
   - its readers;
   - the expected delta (the residual line, both branches: present or absent);
   - the rollback (the key's prior S3 VersionId, read at the act);
   - the BD 23:00Z run as the timing input.

### ACCEPTANCE

<criterion id="SC10-e60-AC1" cell_refs="SC-e-60"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/black_diamond/scripts/gold/tests/test_d04_unclassified_line.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC10-e60-AC1` -- D_04's firm mix sums to 1.0 with an Unclassified line for uncovered weight, none without it.

<criterion id="SC10-e60-AC2" cell_refs="SC-e-60"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/black_diamond/scripts/gold/tests</invocation><expect>PYTEST-OK</expect></criterion>
`SC10-e60-AC2` -- the BD gold suite still passes (control: 76 passed at the base).

<criterion id="SC10-e60-AC3" cell_refs="SC-e-60"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_D04_UNCLASSIFIED_20261007.md</invocation><expect>HALF-READY</expect></criterion>
`SC10-e60-AC3` -- the half request for the served move is ready to sign (a served key needs its pair; the third criterion's reason).

<expected_criteria>SC10-e60-AC1,SC10-e60-AC2,SC10-e60-AC3</expected_criteria>

Dry-run at the base (277fc76bc2, 2026-10-07): SC10-e60-AC1 FAIL as expected (rc=4, no such test file); SC10-e60-AC2 PASS as expected (control, 76 passed); SC10-e60-AC3 FAIL as expected (NOT-READY: absent).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment;
  rows S49, S54).
- No upload, no S3 write, no deploy: a shipped BD gold file, held off CLOUD until its half signs. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W41-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
data/black_diamond/scripts/gold/D_04.client_portal_summary.py
data/black_diamond/scripts/gold/tests/test_d04_unclassified_line.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_D04_UNCLASSIFIED_20261007.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R10.md</decomp_doc> (round 10), cell `SC-e-60`.
<owned_cells>SC-e-60</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC10-e60-AC1, SC10-e60-AC2, SC10-e60-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~41/MDPF_SECCLASS.TO-SC-e60.d04-unclassified-line.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC10-e60-AC1,SC10-e60-AC2,SC10-e60-AC3` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** whether D_04 still writes the key, the code change (or test-only), the residual on the fixture, AC1-AC3 outputs, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- the BD 23:00Z chain is the release's timing input, named in the half request.
comp-iam: DECLARED-NOT-APPLICABLE no role or grant changes; the release seat's write is its standing lane.
comp-adversary: RUN -- a mix that sums to 1.0 by renormalising (the Unclassified weight must equal the uncovered weight); the d06 port retiring the key first (step 1); BLIND: the served file's bytes (denied to dell1).
lane: the <paths> block IS the grant.
</preflight>

Source: round-9 analysis @9b6348f15e section 3 item 7; CTO msg 219 (C-S13); PRD v0.14 (ADMITTED); DECOMP_R10.

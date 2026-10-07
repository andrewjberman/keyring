# TO IRPT_BCKEND.TO-IB-pr-332 -- irpt-performance-adapter builds: its three build-only modules leave the parity-scanned top level (row W127-S1)

<to_id>IRPT_BCKEND.TO-IB-pr-332</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~135</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>61</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** `1.0.0_SA_CTO~DELL2` round analysis rounds 47-60,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUNDS_47_60_20261007.md` @e363a194ed section 5, item E-P4 |
**Risk:** declared at the L6 floor its `<paths>` imply (an `infra/` path floors at WORLD, spine v3.19); the analysis's own class for E-P4 is in its section 5 | **Decomp cell:** `IB-pr-332` (decomposition section 54) | **outcome_ref:** FWD-3 (an Inflection export needs an adapter build); row W127-S1 | **depends_on:** none.

---

## WORKER FACE

**The defect (row IRPT_BCKEND-W127-S1, ARMED).** `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-performance-adapter`
fails the ADHC_DRIFTD.002 parity gate (`build-and-upload.sh:411-450`): it scans the TOP-LEVEL `*.py` of the source_dir
`infra/aws/lambda/investor-reporting/performance/` and refuses any file not in the union of `files[]`. Three build-only modules sit there unregistered:
`build_candidate.py`, `build_dependencies.py`, `cot_probe.py` (last touched 5cdb889b5e, 2026-09-23). Registering them would ship build
tooling into the served zip, and the map is another cell's write set this round, so the remedy is location, not registration.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-135`; run everything from its root):

1. Move the three modules with `git mv` into `infra/aws/lambda/investor-reporting/performance/build_tools/` (the parity scan reads only the top level). Add a short
   `infra/aws/lambda/investor-reporting/performance/build_tools/README.md`: why they live there (build-only, never packaged; ADHC_DRIFTD.002 scans the top level).
2. Fix every reference to them (imports, `python performance/<name>.py` usages in docs or scripts inside `performance/`). A census at the
   issuer's cut found no other file in `infra/`, `.tools/` or the task orders naming them; re-check inside `performance/`.
3. **If any of the three is imported by the RUNTIME** (handler, entry or any module in `files[]`), stop: it must ship, which needs a
   map edit this cell does not hold. File a row naming the import and stop on the criterion.
4. Run `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-performance-adapter` and report its last two lines.

<criterion id="IB61-4-AC1" cell_refs="IB-pr-332"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r61/p61_cells.py" . IB61-4-AC1</invocation><expect>IB61-4-AC1 PASS</expect></criterion>
`IB61-4-AC1` -- BUILD_ONLY of the adapter exits 0 past the parity gate and none of the three sits at the top level. Base: FAIL.

<criterion id="IB61-G-135" cell_refs="IB-pr-332"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r61/p61_cells.py" . IB61-G-135</invocation><expect>IB61-G-135 PASS</expect></criterion>
`IB61-G-135` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB61-4-AC1,IB61-G-135</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** An edit to `lambda-source-map.json`, to `build-and-upload.sh`, `BAU_PARITY_SKIP=1`, or a change to any runtime module's behaviour is a defect: stop and file a row.

<paths>
infra/aws/lambda/investor-reporting/performance/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~135/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-332.the-adapter-builds.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 54 (round 61, workstream ~P), cell `IB-pr-332`.
<owned_cells>IB-pr-332</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB61-4-AC1, IB61-G-135. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~135/IRPT_BCKEND.TO-IB-pr-332.the-adapter-builds.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB61-4-AC1,IB61-G-135` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, any suite's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- nothing is deployed by this order; any release is the issuer's after the drain.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS permission is added.
comp-routes: DECLARED-NOT-APPLICABLE -- no route or CloudFront behaviour changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- every criterion dry-run at base 6e462d3499 2026-10-07 ~09:0xZ: build checks FAIL, guards PASS (p61_cells.py).
lane: the <paths> block IS the grant.
</preflight>

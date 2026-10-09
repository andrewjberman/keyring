# TO IRPT_BCKEND.TO-IB-pr-415 -- IB-pr-399's replay driver: the pre-binding negative control re-pointed to the commit before the binding change, and shown to fail on its defect

<to_id>IRPT_BCKEND.TO-IB-pr-415</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~277</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>116</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO ADDENDUM 20 item 3 (`CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUNDS_75_76_P_64_Y_20261008.md`), row D2-W272-S2 / REMEDIATION_v39 | **Decomp cell:** `IB-pr-415` (decomposition section 109) | **outcome_ref:** FWD-2

---

## WORKER FACE

**The cell.** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~264/replay/run_replay.py` (IB-pr-399's replay driver) derives
its pre-binding negative control as `PRE_BINDING_PIN = git rev-parse pin + "^"`.
- At any pin after the binding change, `pin^` is the bound entry itself, so the control measures nothing and cannot fail.
- ~272 worked around it in its own copy (`0.9.0_WK_IRPT_BCKEND~272/replay/run_replay.py`, `STOPPED_PIN^`); ~264's driver is still wrong.
- The binding change is commit `cabad9008c`: IB-pr-399, "irpt-narrative holds a no-row internal caller to opal-capital".
Root: `C:/dev/wk-irpt-bckend-277/`.

**Build:**
1. In ~264's `run_replay.py`, replace the `pin + "^"` derivation with a named constant `PRE_BINDING_REF`, resolved as the parent of the
   binding commit (`git rev-parse cabad9008c^`). Comment why `pin^` was wrong. Change nothing else in the driver.
2. Run the control: drive the pre-binding `narrative/entry.py` (from `PRE_BINDING_REF`) and the bound one (from `cabad9008c`) through the
   driver's no-row-internal-selects-other-firm arm, offline with synthetic principals and no AWS. Write
   `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~277/IB116-1_control_proof.json`:
   `{pre_binding_ref, verdict: "control_fails_on_defect", routes_widened: <n >= 1>, bound_entry_routes_widened: 0, method}`.

<criterion id="IB116-1-AC1" cell_refs="IB-pr-415"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r116/p116_cells.py" . IB116-1-AC1</invocation><expect>IB116-1-AC1 PASS</expect></criterion>
<criterion id="IB116-1-AC2" cell_refs="IB-pr-415"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r116/p116_cells.py" . IB116-1-AC2</invocation><expect>IB116-1-AC2 PASS</expect></criterion>

<expected_criteria>IB116-1-AC1, IB116-1-AC2</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. A test-harness script and a proof file; no product code, no AWS, no deploy.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W277-S<k>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~277" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~277@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~277 <0.9.0_WK_IRPT_BCKEND~277@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~264/replay/run_replay.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~277/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-415.replay-control-parent.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 109 (round 116, workstream ~P), cell `IB-pr-415`.
<owned_cells>IB-pr-415</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB116-1-AC1, IB116-1-AC2. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~277/IRPT_BCKEND.TO-IB-pr-415.replay-control-parent.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give the change, the proof's numbers, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one replay-harness script in a deliverables folder and a proof file; no product code, no AWS, no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p116_cells.py dry-run at base box/dell2 on dell2 2026-10-09 ~15:0xZ: AC1 FAIL (pin + "^"), AC2 FAIL (no proof); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's (CTO ADDENDUM 20 item 3).
</preflight>

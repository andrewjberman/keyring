# TO IRPT_BCKEND.TO-IB-pr-191 -- The 49F engine never serves an impossible return (NEW-01, rows S176/S177)

<to_id>IRPT_BCKEND.TO-IB-pr-191</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~61</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-28</issued_date>
<status>complete -- P19-1-AC1/AC2/AC3 all PASS-by-output (proof-of-spec-check.py VALID rc=0). f49_engine.EngineReturnImplausible raised from calculate() before any report is built when a linked window day carries r_net &lt;= -1.0; entry.py names it DEPENDENCY_UNAVAILABLE ahead of the MRO's EnginePerformanceRefused OBJECT_NOT_COVERED; tests/test_f49_engine.py carries the NEW-01 shape + sibling control (10 of 10 tests pass). Base-state contrast executed against a detached-HEAD worktree at 0a80f8165c: AC1/AC3 arm A both FAIL there, matching the order's stated base. Committed 57a58117fb on wk-IRPT_BCKEND-61.</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `IB-pr-191` (decomposition section 13) | **outcome_ref:** FWD-3
(Performance backend half) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-pr-191` -- an invested 49 Financial account shows YTD -100.00% on the Performance page. Measured cause (row
IRPT_BCKEND-S177): the engine table `canonical/twr_daily` carries one OK row on 2026-04-16 with bmv 13,360.59, emv 0.0,
cf_net 0.0, so r_net = -1.0; `f49_engine.calculate` links `running *= 1 + r_net` (lines 199-204) and every later day
multiplies that zero, so the account answers -100% while it holds ~98.6k today. Year to date, 28 OK account-days carry
r_net <= -0.999 across 24 accounts (some far below -1, where a flow is orders of magnitude above the value change).

**Build**, in `C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/lambda/investor-reporting/performance/` of YOUR
worktree (the path in your spawn line replaces `C:/Users/AndrewBerman/Desktop/ajb_workspace` throughout):
1. In `f49_engine.py`, define `class EngineReturnImplausible(EnginePerformanceRefused)` beside `WindowNotRuled`, and
   raise it from `calculate` when any row linked inside the window carries `r_net <= -1.0`. Raise before any report is
   built. The message is fixed text naming no account, date or value. Do not change `parity_period_returns.py` or the
   producer `data/assets/scripts/gold/runners_49f/c02_twr_engine.py` (the producer fix is routed separately by
   1.0.0_SA_CTO, ruling 102411).
2. In `entry.py` `build_entry`, add `"EngineReturnImplausible": "DEPENDENCY_UNAVAILABLE"` to the reasons table beside
   the `WindowNotRuled` / `EnginePerformanceRefused` lines, with a one-line comment: an engine answer our checks refuse
   is a dependency the caller does not control (the InflectionPerformanceRefused precedent). Leave the existing lines
   unchanged.
3. Add the NEW-01 shape and its control to `tests/test_f49_engine.py` as a test, reusing that file's `FakeS3`
   fixtures.

### ACCEPTANCE (run each from your worktree root)

<criterion id="P19-1-AC1" cell_refs="IB-pr-191"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r19/p19_1_ac1_implausible_fixture.py" .</invocation><expect>P19-1-AC1 PASS</expect></criterion>
`P19-1-AC1` -- the built behaviour, with its difference control: arm A, the NEW-01 shape refuses as
EngineReturnImplausible; arm B, the control account still computes. Base (CLOUD before this cell): FAIL on arm A,
PASS on arm B.

<criterion id="P19-1-AC2" cell_refs="IB-pr-191"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r19/p19_1_ac2_live_seam.py" .</invocation><expect>P19-1-AC2 PASS</expect></criterion>
`P19-1-AC2` -- the seam probe against the REAL engine table, read-only S3 (about 20 s): arm A, live YTD for the NEW-01
account refuses as EngineReturnImplausible; arm B, the live control account computes. Base: arm A FAIL (served -1.0),
arm B PASS.

<criterion id="P19-1-AC3" cell_refs="IB-pr-191"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r19/p19_1_ac3_boundary_code.py" .</invocation><expect>P19-1-AC3 PASS</expect></criterion>
`P19-1-AC3` -- the boundary names the refusal DEPENDENCY_UNAVAILABLE. Without the line, the MRO walk would answer
OBJECT_NOT_COVERED ("this account is not covered"), which is false. Base: FAIL on arm A.

<expected_criteria>P19-1-AC1,P19-1-AC2,P19-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Read anything; write
  only these.
- **No deploy, no AWS write.** AC2 reads S3 only. The risk class is WORLD because the paths are a Lambda's source (the
  L6 floor); the served move of the adapter is the COO's later act under both never-widen halves.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken a check to pass.

<paths>
infra/aws/lambda/investor-reporting/performance/f49_engine.py
infra/aws/lambda/investor-reporting/performance/entry.py
infra/aws/lambda/investor-reporting/performance/tests/test_f49_engine.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 13 (round 19, workstream ~P), cell `IB-pr-191`.
<owned_cells>IB-pr-191</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: P19-1-AC1, P19-1-AC2, P19-1-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~61/IRPT_BCKEND.TO-IB-pr-191.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> P19-1-AC1,P19-1-AC2,P19-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hash, each criterion's last line, and any surprise row id
(`IRPT_BCKEND-W19P-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or cron is created or changed; the cell is code and tests on a branch.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM policy or role changes; the S3 reads in the live check run under the worker session's existing read access.
comp-blast: DECLARED-NOT-APPLICABLE -- no resource is deleted or re-pointed; two source files and one test change on a branch, nothing served.
comp-routes: DECLARED-NOT-APPLICABLE -- the route table is unchanged; one refusal class gains a boundary code.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache or CDN surface is touched.
comp-adversary: RUN -- the checks were dry-run at the base (CLOUD content for these files): AC1 FAIL/PASS, AC2 FAIL (served -1.0)/PASS, AC3 FAIL/PASS as expected.
lane: the <paths> block IS the grant; no other open order names these files.
</preflight>

Queue: slot ~61 continues with `IRPT_BCKEND.TO-IB-pr-192` on the same files.

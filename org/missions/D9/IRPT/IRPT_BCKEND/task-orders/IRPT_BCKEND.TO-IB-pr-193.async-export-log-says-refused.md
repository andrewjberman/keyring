# TO IRPT_BCKEND.TO-IB-pr-193 -- The async export log says REFUSED for a refused replay, not FAILED

<to_id>IRPT_BCKEND.TO-IB-pr-193</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~62</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-28</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `IB-pr-193` (decomposition section 13) | **outcome_ref:** FWD-9
(Export) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-pr-193` -- `run_async_submit` in `infra/aws/lambda/investor-reporting/export/entry.py` (lines 327-341) prints stage
`FAILED` for every exception from `submit_async.run`. But `submit_async.run` raises `AsyncSubmitRefused` (lines 166 and
173 of `export/submit_async.py`) BEFORE it moves the pending pointer, when a replay finds no BUILDING pointer or an
event that does not carry what accept authorized. The log then says FAILED for a build that never changed, which
misleads the operator who reads it.

**Build:** in `run_async_submit`, catch `_async.AsyncSubmitRefused` first and print the same
`{"irpt_export_async": {...}}` line with `"stage": "REFUSED"` (the export_revision and the exception's class name as
`reason`, never its text), then re-raise it unchanged. Every other exception keeps printing `FAILED` and re-raising.
Do not change `submit_async.py`, the receipt route, or any stage constant it defines. Add one test to
`export/tests/test_submit_async.py`.

### ACCEPTANCE (run from your worktree root)

<criterion id="P19-3-AC1" cell_refs="IB-pr-193"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r19/p19_3_ac1_async_log.py" .</invocation><expect>P19-3-AC1 PASS</expect></criterion>
`P19-3-AC1` -- the built behaviour with its control: AsyncSubmitRefused logs ['REFUSED'] and re-raises; the
ExportBuildFailed control still logs ['FAILED'] and re-raises. Base: FAIL (['FAILED'] for the refusal), control PASS.

<expected_criteria>P19-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **No deploy, no AWS call.** WORLD is the L6 path floor for a Lambda's source; this cell changes code and a test only.
- **Refusal clause.** If the criterion cannot be met as written, stop, write the reason in your report and a
  surprise row, and do not weaken the check.

<paths>
infra/aws/lambda/investor-reporting/export/entry.py
infra/aws/lambda/investor-reporting/export/tests/test_submit_async.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 13 (round 19, workstream ~P), cell `IB-pr-193`.
<owned_cells>IB-pr-193</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: P19-3-AC1. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~62/IRPT_BCKEND.TO-IB-pr-193.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> P19-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hash, the criterion's last line, and any surprise row id
(`IRPT_BCKEND-W19P-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or cron is created or changed; the cell is code and a test on a branch.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM policy or role changes and no AWS call.
comp-blast: DECLARED-NOT-APPLICABLE -- one handler function's log line on a branch; nothing served.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface.
comp-adversary: RUN -- the check was dry-run at the base: FAIL (['FAILED'] for AsyncSubmitRefused) / control PASS, as expected.
lane: the <paths> block IS the grant.
</preflight>

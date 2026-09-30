# TO IRPT_BCKEND.TO-IB-pr-214 -- The fresh path refuses any series point at or below -1 (PRD v0.20 ruling 16)

<to_id>IRPT_BCKEND.TO-IB-pr-214</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~70</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-29</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO RULING 102611 (PRD ADDENDUM v0.20 @613bfc6ecf ruling
16) on 4.0.0_SA_CRO's refused half @eca8083ad2 section 6 item 3 (row S195) | **Decomp cell:** `IB-pr-214` (decomposition
section 18) | **outcome_ref:** FWD-3 (49F) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-pr-214` -- PRD v0.20 ruling 16: "The fresh path refuses any series point at or below -1, as the reopen path does."

In `C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/lambda/investor-reporting/performance/retained.py`, the
REOPEN path already refuses a retained report whose series carries such a point. It uses
`implausible_engine_series(report)` and raises `f49_engine.EngineReturnImplausible`, which `entry.py`'s reasons table
maps to DEPENDENCY_UNAVAILABLE. The FRESH path (49F, `holdings_gold.calculate`) does not, so today an OK gold day of
-1.2 serves -120.5%. The two readers of the served figure (compute and retained reopen) must agree.

**Build:** in the 49F fresh path, apply the same `implausible_engine_series` test to the computed report before it is
persisted or returned, and raise `f49_engine.EngineReturnImplausible` on it. A day the gold marks non-OK (for example
NOT_COMPUTABLE under ruling 16) is already skipped by `holdings_gold` and disclosed PARTIAL; keep that. Add a test in
`performance/tests/test_retained_performance.py`.

### ACCEPTANCE (run from your worktree root)

<criterion id="P21-4-AC1" cell_refs="IB-pr-214"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r21/p21_4_ac1_fresh_path_refuses_implausible.py" .</invocation><expect>P21-4-AC1 PASS</expect></criterion>
`P21-4-AC1` -- through `RetainedPerformance(holdings_source=...).compute` on in-memory gold: arm A, an OK day of -1.2,
refuses as `EngineReturnImplausible` (no figure); arm B (control), the same day NOT_COMPUTABLE, answers OPAL_HOLDINGS
over the other days. Base: FAIL (arm A served -1.20502; arm B passed).

<expected_criteria>P21-4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **No deploy, no AWS write.** The served move is the issuer's, under both never-widen halves.
- **Refusal clause.** If the criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the check.

<paths>
infra/aws/lambda/investor-reporting/performance/retained.py
infra/aws/lambda/investor-reporting/performance/tests/test_retained_performance.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 18 (round 21, workstream ~P), cell `IB-pr-214`.
<owned_cells>IB-pr-214</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: P21-4-AC1. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~70/IRPT_BCKEND.TO-IB-pr-214.fresh-path-refuses-implausible.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> P21-4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hash, the criterion's last line, and any surprise row id (`IRPT_BCKEND-W70-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- code only; 0 roles touched.
comp-blast: RUN -- the 49F fresh path gains one refusal; both readers of the served figure are named in the criterion (fresh here, reopen already guarded).
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache.
comp-adversary: RUN -- P21-4-AC1 dry-run at the base: FAIL (arm A served -1.20502; arm B control passed).
lane: the <paths> block IS the grant.
</preflight>

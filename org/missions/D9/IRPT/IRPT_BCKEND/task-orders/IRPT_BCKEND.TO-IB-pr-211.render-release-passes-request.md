# TO IRPT_BCKEND.TO-IB-pr-211 -- The release re-check passes the request, so a render can name its grant (window 21 K8)

<to_id>IRPT_BCKEND.TO-IB-pr-211</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~67</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-29</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** window 21 K8 (ledger irpt-ui-walk-principal-w21-20260929 leg K8,
@1ef167e0ba); the five export/adapter A1 legs wait on it | **Decomp cell:** `IB-pr-211` (decomposition section 18) |
**outcome_ref:** FWD-9 (export) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-pr-211` -- In window 21 the export's render read Performance as a RENDER_DELEGATE, and the adapter refused it:
`PerformanceAccessRefused("a render read carries no request to name its grant")` (adapter log corr-d490a5849a80,
public OBJECT_NOT_COVERED). No PDF was produced.

The cause is in
`C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/lambda/investor-reporting/performance/entry.py`:
- `_authorize_release(request, ctx, reference, selected, boundary)` (line 54) re-resolves the scope after the slow
  compute. It then calls `_resolve_selected(scope, current_ctx, reference)` at line 61 WITHOUT the request.
- For a RENDER_DELEGATE, `_resolve_selected` hands the request to `_resolve_render_selection` -> `_render_grant(request,
  ctx)`, which refuses at line 151 when the request is None.

The first resolution (line 228, `_performance_report`) passes the request; only the re-check drops it.

**Build:** pass `request` through at line 61, and add a test in `performance/tests/test_render_selection.py` that
exercises the release re-check for a RENDER_DELEGATE with a request that names a stamped grant. Nothing else changes:
the human path and the "computed selection no longer matches" refusal stay as they are.

### ACCEPTANCE (run from your worktree root)

<criterion id="P21-1-AC1" cell_refs="IB-pr-211"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r21/p21_1_ac1_release_passes_request.py" .</invocation><expect>P21-1-AC1 PASS</expect></criterion>
`P21-1-AC1` -- arm A: `_authorize_release` hands its own request to `_resolve_selected`; arm B (control): a changed
selection still refuses. Base: FAIL (arm A false, arm B true).

<expected_criteria>P21-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **No deploy, no AWS write.** The served move is the issuer's, under both never-widen halves.
- **Refusal clause.** If the criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the check.

<paths>
infra/aws/lambda/investor-reporting/performance/entry.py
infra/aws/lambda/investor-reporting/performance/tests/test_render_selection.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 18 (round 21, workstream ~P), cell `IB-pr-211`.
<owned_cells>IB-pr-211</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: P21-1-AC1. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~67/IRPT_BCKEND.TO-IB-pr-211.render-release-passes-request.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> P21-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hash, the criterion's last line, and any surprise row id (`IRPT_BCKEND-W67-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- code only; 0 roles touched.
comp-blast: RUN -- one argument added at one call site; the served move (issuer) counts both readers.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache.
comp-adversary: RUN -- P21-1-AC1 dry-run at the base: FAIL (arm A false; arm B control true).
lane: the <paths> block IS the grant.
</preflight>

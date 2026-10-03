# TO IRPT_BCKEND.TO-IB-pr-306 -- P-6's backend half: PATH A no longer composes 49 Financial; a 49F Performance request is refused by a named retirement (nothing served)

<to_id>IRPT_BCKEND.TO-IB-pr-306</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~109</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-03</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>41</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO RULINGS batch 201: P-6 option (a), "retire PATH A whole: drop 49F from
COMPOSED_FIRMS with a named refusal". The census was accepted by batch 203. GATE (x) puts this in ROUND 41 (row S267). |
**Decomp cell:** `IB-pr-306` (decomposition section 33) | **outcome_ref:** P-6 | **depends_on:** none. It is BUILT now and SERVED only
in P-2's window, together with PATH B covering every 49F account and ~D's page.

---

## WORKER FACE

**The ruling.** When PATH B (the precomputed reporting route) covers every 49 Financial account, PATH A's 49 Financial route is
retired in the same window: no two paths (Andrew's standing veto). PATH A is `infra/aws/lambda/investor-reporting/performance/retained.py`,
which composes 49F from the holdings gold (`COMPOSED_FIRMS`, `:67`).
- A firm outside `COMPOSED_FIRMS` already refuses `ProviderPathNotComposed`, whose public code is `UNSUPPORTED_OPERATION`.
- The retirement REUSES that public code: no new reason code, and no contract change.

**What you build.**
1. In `retained.py`, REMOVE `tenants._CANONICAL_49F` from `COMPOSED_FIRMS`. Inflection and Cottonwood stay.
2. Add a NAMED subclass, for example `PathARetiredForFirm(ProviderPathNotComposed)`, raised for 49 Financial with the reason
   "49 Financial Performance is served from the reporting route (PATH B); PATH A is retired (P-6, CTO batch 201)".
   - Its public code is `UNSUPPORTED_OPERATION`, inherited through the boundary's MRO walk; verify in `entry.py`'s reason map.
   - The phases line names the subclass, so a retired-path request is countable.
3. A RETAINED 49F Performance report's reopen through PATH A is refused the same way. Read the reopen path in `retained.py` and make
   sure no 49F figure is served by PATH A after the retirement. An EXPORT reads retained reports through `export/retained_export.py`,
   which moves to PATH B in P-6 (IB-pr-301 and IB-pr-302); do not touch the export.
4. **Existing tests that assert 49F is COMPOSED on PATH A** move to assert the retirement. That is an expected consequence of this
   ruling, not a regression. Edit only those assertions, in `performance/tests/test_retained_performance.py`; leave Inflection and
   Cottonwood tests untouched. List each moved test in your report.
5. **Tests.** Create `performance/tests/test_path_a_retired_49f.py`, at least 3 tests, naming `49`, `Retired` and
   `UNSUPPORTED_OPERATION`:
   - a fresh 49F request is refused by the named subclass, answering `UNSUPPORTED_OPERATION`;
   - a 49F retained reopen is refused;
   - an Inflection request still composes on the holdings path.

<criterion id="IB41-1-AC1" cell_refs="IB-pr-306"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r41/p41_path_a_retired_49f.py" . IB41-1-AC1</invocation><expect>IB41-1-AC1 PASS</expect></criterion>
`IB41-1-AC1` -- `COMPOSED_FIRMS` holds Inflection and Cottonwood but not 49F, and a `*Retired*` subclass of
`ProviderPathNotComposed` exists. The retirement tests pass (at least 3). Base: FAIL (49F composed, no retirement class).

<criterion id="IB41-1-AC2" cell_refs="IB-pr-306"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r41/p41_path_a_retired_49f.py" . IB41-1-AC2</invocation><expect>IB41-1-AC2 PASS</expect></criterion>
`IB41-1-AC2` -- the performance suite passes at least 249 (246 at the base), 0 failed. Moved tests are converted, never deleted.
Base: FAIL (246).

<expected_criteria>IB41-1-AC1,IB41-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** none.
- **Refusal clause.** A change to Inflection's or Cottonwood's composition, or a new public reason code, is a defect: stop and
  file a row. A deleted test is a defect: convert it. No client name in any record.

<paths>
infra/aws/lambda/investor-reporting/performance/retained.py
infra/aws/lambda/investor-reporting/performance/tests/test_path_a_retired_49f.py
infra/aws/lambda/investor-reporting/performance/tests/test_retained_performance.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~109/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/`, `lib/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 33 (round 41, workstream ~P), cell `IB-pr-306`.
<owned_cells>IB-pr-306</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB41-1-AC1, IB41-1-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~109/IRPT_BCKEND.TO-IB-pr-306.path-a-retired-49f.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IB41-1-AC1,IB41-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes and each criterion's last line;
- the subclass and its reason;
- the reopen path's handling;
- every moved test, with its new assertion;
- any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the served irpt-performance-adapter's retained.py (49 Financial composition); 0 served bytes move in the cell; its deploy lands in P-2's window with PATH B's publish of every 49F account and ~D's page, under one never-widen packet and one rollback.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- the route stays; its 49F answer becomes the existing UNSUPPORTED_OPERATION refusal.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB41-1-AC1 base FAIL (probe reads "49F INF COT RET=": 49F composed, no retirement class), IB41-1-AC2 base FAIL (246 < 249), dry-run at the base 2026-10-03 ~07:1xZ.
lane: the <paths> block IS the grant.
</preflight>

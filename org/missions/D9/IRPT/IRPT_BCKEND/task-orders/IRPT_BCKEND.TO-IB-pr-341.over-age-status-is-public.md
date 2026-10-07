# TO IRPT_BCKEND.TO-IB-pr-341 -- the over-age search status carries only public members, so the four portal readers pass (W140-S1; r61 release precondition P1)

<to_id>IRPT_BCKEND.TO-IB-pr-341</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~143</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>63</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 337 (W140-S1, server-side; REC taken) | **Decomp cell:** `IB-pr-341`
(decomposition section 56) | **outcome_ref:** FWD-7 (the r61 directory release, held on P1) | **depends_on:** IB-pr-334, IB-pr-338 (both drained).

---

## WORKER FACE

**The defect (row IRPT_BCKEND-W140-S1, ARMED).** On an over-age directory, `irpt-directory-search`
(`infra/aws/lambda/investor-reporting/directory/entry.py`, `entry.search`, round 61 IB-pr-334) answers `{"_data": <stale hits>, "_status": <expiry envelope>}`. That
`_status` carries the server-only member `internal_correlation_id`. The portal's `requirePublicStatus`
(`portal/src/pages/InvestorReporting/contracts/envelope.ts`) is a CLOSED shape and refuses it, so all four portal readers of the search
response break on an over-age day. With that one member removed, the answer parses (IB-pr-338's census,
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~140/IB62-3_reader_census.json`). The CTO's ruling: a server-only member reaching a client is the
server's defect; `requirePublicStatus` refusing it is correct and STAYS.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-143`, with a nested portal worktree at `C:/dev/wk-irpt-bckend-143/portal` on
the portal branch carrying IB-pr-338's reader tests (`d53a7a0f`); run everything from the workspace root unless a step says portal):

1. **Server.** In `infra/aws/lambda/investor-reporting/directory/entry.py`, the over-age `_status` carries only PUBLIC members: the set the portal's `requirePublicStatus`
   admits (read `envelope.ts`; do not edit it). Strip `internal_correlation_id` and any other non-public member there; the server keeps
   its correlation id in its own log. Touch no other path of `entry.py`; the in-age answer is unchanged.
2. **Test** `infra/aws/lambda/investor-reporting/directory/tests/test_search_overage_public_status.py` (new): the over-age `_status` has exactly the public member set; a test
   FAILS if any non-public member (name `internal_correlation_id`) appears. Run the directory suite once and report its last line.
3. **Portal tests.** In the portal worktree, regenerate the over-age fixture(s) under
   `portal/src/pages/InvestorReporting/__tests__/ir-62-overage/fixtures/` from the fixed `entry.search` (IB-pr-338's generator is
   `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~140/gen_search_fixtures.py`; copy it into your deliverables if you need to change it), and turn
   the four `test.failing` reader tests into plain `test` (the readers themselves are NOT edited). Run
   `bun test src/pages/InvestorReporting/__tests__/ir-62-overage/` from `portal/` (it needs `node_modules`: if the portal worktree has
   none, junction one from `C:/dev/ajb_workspace/portal/node_modules` and say so). Commit on the portal worktree branch; the issuer lands it.

<criterion id="IB63-1-AC1" cell_refs="IB-pr-341"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r63/p63_cells.py" . IB63-1-AC1</invocation><expect>IB63-1-AC1 PASS</expect></criterion>
`IB63-1-AC1` -- the public-status test passes (a non-public member fails it) and the directory suite passes. Base: FAIL (no test).

<criterion id="IB63-1-AC2" cell_refs="IB-pr-341"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r63/p63_cells.py" . IB63-1-AC2</invocation><expect>IB63-1-AC2 PASS</expect></criterion>
`IB63-1-AC2` -- the four portal reader tests carry no test.failing and pass with bun on the regenerated over-age fixture. Base: FAIL.

<criterion id="IB63-G-143" cell_refs="IB-pr-341"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r63/p63_cells.py" . IB63-G-143</invocation><expect>IB63-G-143 PASS</expect></criterion>
`IB63-G-143` -- a GUARD: your workspace commits touch only your grant. Base: PASS.

<expected_criteria>IB63-1-AC1,IB63-1-AC2,IB63-G-143</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure. No build upload, no apply, no AWS write.
- **Firm buckets deny this box's identity** (row S347). If you need a firm-bucket read, file a row and stop on that criterion.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** An edit to `envelope.ts` or any portal reader, to `expiry.py`, to the in-age path of `entry.py`, or a deploy is a defect: stop and file a row.

<paths>
infra/aws/lambda/investor-reporting/directory/entry.py
infra/aws/lambda/investor-reporting/directory/tests/test_search_overage_public_status.py
portal/src/pages/InvestorReporting/__tests__/ir-62-overage/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~143/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-341.over-age-status-is-public.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 56 (round 63, workstream ~P), cell `IB-pr-341`.
<owned_cells>IB-pr-341</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB63-1-AC1, IB63-1-AC2, IB63-G-143. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~143/IRPT_BCKEND.TO-IB-pr-341.over-age-status-is-public.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB63-1-AC1,IB63-1-AC2,IB63-G-143` BEFORE the flip.
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
comp-adversary: RUN -- every criterion dry-run at base 1758606f46 2026-10-07 ~10:3xZ: build checks FAIL, guard PASS (p63_cells.py).
lane: the <paths> block IS the grant.
</preflight>

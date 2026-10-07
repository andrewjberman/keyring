# TO IRPT_BCKEND.TO-IB-pr-340 -- one fixture per gated scoped route, allowed and denied principal class, and the replay battery green on them (E-P10, W137-S1)

<to_id>IRPT_BCKEND.TO-IB-pr-340</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~142</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>62</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-61 analysis @aae1ed7781 section 3 item E-P10 (row W137-S1) | **Decomp cell:** `IB-pr-340`
(decomposition section 55) | **outcome_ref:** FWD-2 (the replay's gated arms; the run that GRADES FWD-2 still needs the test principal Andrew names) | **depends_on:** none.

---

## WORKER FACE

**The gap (row IRPT_BCKEND-W137-S1).** Round 61's replay (IB-pr-335, battery
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~137/battery_ib_pr_335.py`, transcript `IB61-7_replay_output.json` beside it) drove 21 live
`/api/scoped/` investor-reporting routes (enumerated from API Gateway get-routes, equal to routes.json) and left 15/15/17 arms GATED, most for
want of an operation-shaped fixture: the generic authorized request was refused by each route's own input validation, or the route is
served by an installed entry. Row W137-S2 recorded the worker's definition of "protected field" (a value that differs between two
authorized principals' answers, with an injected-leak control); keep it.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-142`; run everything from its root):

1. Copy the round-61 battery into your folder (do not edit the original). Re-print the route census (count and how it was enumerated).
2. For each GATED route, build one operation-shaped fixture for the ALLOWED principal class and one for the DENIED class (files under your
   deliverables folder, e.g. `fixtures/<route-slug>.allowed.json` / `.denied.json`), shaped from the route's own request contract
   (routes.json, the contracts under `docs/contracts/investor-reporting/v1/`, the entry's validators).
3. Run the battery in-process on those fixtures (the same network hard-block as round 61; no live authenticated call, no principal minted,
   no grant written) and write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~142/IB62-5_gated_fixtures.json`:
   `{"route_count": N, "enumeration": "...", "battery_overall_pass": bool, "routes": [{"route": "...", "gated": bool, "allowed_fixture":
   "<repo path>", "denied_fixture": "<repo path>", "allowed": "PASS|FAIL", "denied": "PASS|FAIL"}]}`. A driven arm that FAILS is a
   BLOCKING row and `battery_overall_pass` false.

<criterion id="IB62-5-AC1" cell_refs="IB-pr-340"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r62/p62_cells.py" . IB62-5-AC1</invocation><expect>IB62-5-AC1 PASS</expect></criterion>
`IB62-5-AC1` -- the fixtures file lists every route (count = listed), each gated route has an allowed and a denied fixture that exists, and the battery is green. Base: FAIL (no file).

<criterion id="IB62-G-142" cell_refs="IB-pr-340"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r62/p62_cells.py" . IB62-G-142</invocation><expect>IB62-G-142 PASS</expect></criterion>
`IB62-G-142` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB62-5-AC1,IB62-G-142</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure. No build upload, no apply, no AWS write.
- **Firm buckets deny this box's identity** (row S347). If you need a firm-bucket read, file a row and stop on that criterion.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** A live authenticated call, minting a principal, writing a grant, or any state-changing call is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~142/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-340.one-fixture-per-gated-route.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 55 (round 62, workstream ~P), cell `IB-pr-340`.
<owned_cells>IB-pr-340</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB62-5-AC1, IB62-G-142. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~142/IRPT_BCKEND.TO-IB-pr-340.one-fixture-per-gated-route.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB62-5-AC1,IB62-G-142` BEFORE the flip.
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
comp-adversary: RUN -- every criterion dry-run at base bc794d2770 2026-10-07 ~09:5xZ: build checks FAIL, guards PASS (p62_cells.py).
lane: the <paths> block IS the grant.
</preflight>

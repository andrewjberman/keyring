# TO IRPT_BCKEND.TO-IB-pr-335 -- FWD-2 replay on current bytes: every scoped investor-reporting route, both principal classes, the revoked-grant arm

<to_id>IRPT_BCKEND.TO-IB-pr-335</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~137</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>61</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** `1.0.0_SA_CTO~DELL2` round analysis rounds 47-60,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUNDS_47_60_20261007.md` @e363a194ed section 5, item E-P7 |
**Risk:** declared at the L6 floor its `<paths>` imply (an `infra/` path floors at WORLD, spine v3.19); the analysis's own class for E-P7 is in its section 5 | **Decomp cell:** `IB-pr-335` (decomposition section 54) | **outcome_ref:** FWD-2 | **depends_on:** none.

---

## WORKER FACE

**The gap (CTO analysis @e363a194ed, FWD-2).** No full replay has run on current bytes (r57/r58 moved four functions) across the
scoped routes, with both principal classes and the revoked-grant-against-warm-cache arm. Prior batteries to start from (read, copy into
your folder, do not edit them): `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_rtb_1.py` (the authenticated replay across every
deployed route) and `battery_ib_sb_3.py` beside it, with their results `the-replay-authenticated-across-every-deployed-route.result.md`
and `the-replay-battery-across-every-deployed-route.result.md`.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-137`; run everything from its root):

1. `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~137/battery_ib_pr_335.py`: enumerate every `/api/scoped/` investor-reporting route on the live
   API (print the count and how it was enumerated), and per route drive four arms: `service_principal`, `advisor_principal`,
   `revoked_grant_warm_cache`, `negative_no_protected_field` (every refused response is diffed against the authorized response's field
   set and reveals none of its protected fields).
2. **Gated arms.** Minting or revoking a principal or grant is a WRITE to the production auth plane and is not yours (RT2's record in the
   rtb-1 result; the CTO's section 6 item 2: an advisor test principal is Andrew's to name). An arm you cannot drive read-only is recorded
   `GATED` with its reason, never skipped silently and never faked. Use a non-PROD principal where one exists and say so.
3. Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~137/IB61-7_replay_output.json` with this shape:
   `{"overall_pass": bool, "route_count": N, "enumeration": "...", "routes": [{"route": "...", "service_principal": {"state":
   "DRIVEN-PASS"|"GATED", "reason": "..."}, "advisor_principal": {...}, "revoked_grant_warm_cache": {...},
   "negative_no_protected_field": {...}}]}`. `overall_pass` is true only when no driven arm failed. A driven arm that FAILS is a
   BLOCKING row and `overall_pass` false.

<criterion id="IB61-7-AC1" cell_refs="IB-pr-335"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r61/p61_cells.py" . IB61-7-AC1</invocation><expect>IB61-7-AC1 PASS</expect></criterion>
`IB61-7-AC1` -- the transcript reads overall_pass true, route_count equal to the routes listed, every arm DRIVEN-PASS or GATED with a reason. Base: FAIL (no transcript).

<criterion id="IB61-G-137" cell_refs="IB-pr-335"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r61/p61_cells.py" . IB61-G-137</invocation><expect>IB61-G-137 PASS</expect></criterion>
`IB61-G-137` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB61-7-AC1,IB61-G-137</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** Any write to the auth plane (users, grants, principals), any non-GET call that changes state, or a vendor call is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~137/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-335.fwd2-replay-on-current-bytes.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 54 (round 61, workstream ~P), cell `IB-pr-335`.
<owned_cells>IB-pr-335</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB61-7-AC1, IB61-G-137. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~137/IRPT_BCKEND.TO-IB-pr-335.fwd2-replay-on-current-bytes.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB61-7-AC1,IB61-G-137` BEFORE the flip.
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

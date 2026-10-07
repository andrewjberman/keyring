# TO IRPT_BCKEND.TO-IB-pr-347 -- who can reach the export read NOW: principals holding a firm grant on the export routes who are not Opal admin/internal/dev (CTO ruling msg 525, W142-S4 / W146-S1)

<to_id>IRPT_BCKEND.TO-IB-pr-347</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~148</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>67</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 525: measure it this tick; zero -> the fix waits for the terraform kit and PROD stays closed until IB-pr-343 ships; non-zero -> a security exception and a laptop emergency apply | **Decomp cell:** `IB-pr-347`
(decomposition section 60) | **outcome_ref:** FWD-2 (the live exposure of the fail-open export read, rows W142-S4 / W146-S1) | **depends_on:** none.

---

## WORKER FACE

**Why this matters now.** `infra/aws/lambda/investor-reporting/export/entry.py` `_covered` fails OPEN (row W142-S4): an export read
whose receipt names no account is admitted for any firm advisor holding the export id. The live `irpt-export-render` is still fail-open
(IB-pr-345, row W146-S1), and the fix (IB-pr-343) ships only when terraform reaches dell2. The CTO's question decides between waiting and
an emergency apply: **who can call the export read today?**

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-148`; run everything from its root; READ-ONLY against AWS):

1. **The routes.** The export read routes (`GET .../export/{exportId}`, `GET .../export/{exportId}/download`) are served by
   `irpt-export-render` through the portal data-proxy API (IB-pr-345's census,
   `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~146/IB65-3_exposure_census.json`). Name the authorizer in front of them and what it admits.
2. **The principals.** Read the principal store the portal authorizer uses (the production auth plane, `opal-users-v2`, per the rtb-1
   record `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/the-replay-authenticated-across-every-deployed-route.result.md`) and the grants /
   firm bindings `_authz` loads (`infra/aws/lambda/investor-reporting/_authz/enforce.py` `load_policy`, `served.py`). Count every
   principal, and every principal who holds a firm grant that reaches those routes and is NOT Opal admin / internal / dev. Also read the
   page gate (Andrew-direct 2026-09-22: the PROD route is admin/dev only; `portal/src/App.tsx`) and say whether a non-Opal principal could
   call the API directly even though the page hides it.
3. Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~148/IB67-1_export_reach.json`:
   `{"sources": {...}, "routes": [...], "authorizer": "...", "principals_read": N, "non_opal_reach": K, "non_opal_principals":
   [{"principal": "<opaque id>", "class": "...", "grant": "..."}], "api_direct_callable": "...", "limits": "..."}`. Opaque ids only;
   no names, emails or raw account numbers. A non-zero `non_opal_reach` is a BLOCKING row you file.

<criterion id="IB67-1-AC1" cell_refs="IB-pr-347"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r67/p67_cells.py" . IB67-1-AC1</invocation><expect>IB67-1-AC1 PASS</expect></criterion>
`IB67-1-AC1` -- the reach census names sources, routes and authorizer, prints principals_read, and non_opal_reach equals the principals listed, each with class and grant. Base: FAIL (no file).

<criterion id="IB67-G-148" cell_refs="IB-pr-347"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r67/p67_cells.py" . IB67-G-148</invocation><expect>IB67-G-148 PASS</expect></criterion>
`IB67-G-148` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB67-1-AC1,IB67-G-148</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure. No build upload, no apply, no AWS write.
- **Firm buckets deny this box's identity** (row S347). If you need a firm-bucket read, file a row and stop on that criterion.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** ANY write to the auth plane (users, grants, principals) or any AWS write, or a name/email/raw account number in the file, is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~148/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-347.who-can-reach-the-export-read-now.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 60 (round 67, workstream ~P), cell `IB-pr-347`.
<owned_cells>IB-pr-347</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB67-1-AC1, IB67-G-148. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~148/IRPT_BCKEND.TO-IB-pr-347.who-can-reach-the-export-read-now.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB67-1-AC1,IB67-G-148` BEFORE the flip.
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
comp-adversary: RUN -- every criterion dry-run at base 8d7577866e 2026-10-07 ~12:3xZ: build checks FAIL, guards PASS (p67_cells.py).
lane: the <paths> block IS the grant.
</preflight>

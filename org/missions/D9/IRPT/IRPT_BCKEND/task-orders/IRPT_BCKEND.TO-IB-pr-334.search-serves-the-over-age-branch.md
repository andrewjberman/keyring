# TO IRPT_BCKEND.TO-IB-pr-334 -- FWD-7 on current bytes: irpt-directory-search carries expiry.py and an over-age request answers the declared expiry

<to_id>IRPT_BCKEND.TO-IB-pr-334</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~136</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>61</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** `1.0.0_SA_CTO~DELL2` round analysis rounds 47-60,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUNDS_47_60_20261007.md` @e363a194ed section 5, item E-P6 |
**Risk:** declared at the L6 floor its `<paths>` imply (an `infra/` path floors at WORLD, spine v3.19); the analysis's own class for E-P6 is in its section 5 | **Decomp cell:** `IB-pr-334` (decomposition section 54) | **outcome_ref:** FWD-7 | **depends_on:** IB-pr-333 (same slot; one release packet).

---

## WORKER FACE

**The gap (CTO analysis @e363a194ed, FWD-7).** The served `irpt-directory-search` has no over-age branch:
`infra/aws/lambda/investor-reporting/directory/expiry.py` (MAX_AGE_TRADING_DAYS 2; `evaluate(as_of, today, cal)` returns `age_trading_days` and `servable`) is at HEAD
and is packaged into `irpt-directory-refresh`, but `irpt-directory-search`'s `files[]` in `infra/aws/lambda/ci/lambda-source-map.json` does not carry it
(measured at the cut: a BUILD_ONLY search zip has 22 members and no `expiry.py`), so a search over a directory older than two trading
days answers silently from the stale as-of. The two functions share the source_dir `infra/aws/lambda/investor-reporting/directory/`.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-136`, the same slot: you continue from IB-pr-333's state):

1. Find the search entry point (the handler `irpt-directory-search` runs, per its map row) and make a request against a directory whose
   as-of is over `MAX_AGE_TRADING_DAYS` answer the declared expiry (the reason code `expiry.py` declares for an over-age directory),
   never a silent answer; a directory within the age serves as today. Call `expiry.evaluate`; do not copy its logic.
2. Add `expiry.py` (and anything it imports that the search zip lacks) to `irpt-directory-search`'s `files[]` in
   `lambda-source-map.json`. Touch no other row of the map.
3. `infra/aws/lambda/investor-reporting/directory/tests/test_search_overage.py` (new): controlled-clock tests with 2026 dates, an over-age directory answers the
   declared expiry and an in-age one serves; the file names `MAX_AGE_TRADING_DAYS`.
4. Run the directory suite once and report its last line; run `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting
   irpt-directory-search` and report the member count.

**Not yours:** the targeted release of both directory functions under both never-widen halves, and the five-arm controlled-clock drive
(`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/ib_s_4_controlled_clock.py`) against the live bytes are the issuer's after the drain.

<criterion id="IB61-6-AC1" cell_refs="IB-pr-334"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r61/p61_cells.py" . IB61-6-AC1</invocation><expect>IB61-6-AC1 PASS</expect></criterion>
`IB61-6-AC1` -- the new over-age tests pass and the directory suite passes. Base: FAIL (no test).

<criterion id="IB61-6-AC2" cell_refs="IB-pr-334"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r61/p61_cells.py" . IB61-6-AC2</invocation><expect>IB61-6-AC2 PASS</expect></criterion>
`IB61-6-AC2` -- BUILD_ONLY of irpt-directory-search exits 0 and its zip carries expiry.py. Base: FAIL (22 members, no expiry.py).

<criterion id="IB61-G-136" cell_refs="IB-pr-334"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r61/p61_cells.py" . IB61-G-136</invocation><expect>IB61-G-136 PASS</expect></criterion>
`IB61-G-136` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB61-6-AC1,IB61-6-AC2,IB61-G-136</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** An edit to any map row other than irpt-directory-search, a build upload, an apply, or an AWS write is a defect: stop and file a row.

<paths>
infra/aws/lambda/investor-reporting/directory/
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~136/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-334.search-serves-the-over-age-branch.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 54 (round 61, workstream ~P), cell `IB-pr-334`.
<owned_cells>IB-pr-334</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB61-6-AC1, IB61-6-AC2, IB61-G-136. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~136/IRPT_BCKEND.TO-IB-pr-334.search-serves-the-over-age-branch.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB61-6-AC1,IB61-6-AC2,IB61-G-136` BEFORE the flip.
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

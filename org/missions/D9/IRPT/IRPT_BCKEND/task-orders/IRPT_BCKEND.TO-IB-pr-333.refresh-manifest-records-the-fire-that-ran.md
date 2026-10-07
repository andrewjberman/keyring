# TO IRPT_BCKEND.TO-IB-pr-333 -- the directory refresh manifest is keyed by the dispatched business date and a completed build rewrites it to READY (row S348)

<to_id>IRPT_BCKEND.TO-IB-pr-333</to_id>
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
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUNDS_47_60_20261007.md` @e363a194ed section 5, item E-P5 |
**Risk:** declared at the L6 floor its `<paths>` imply (an `infra/` path floors at WORLD, spine v3.19); the analysis's own class for E-P5 is in its section 5 | **Decomp cell:** `IB-pr-333` (decomposition section 54) | **outcome_ref:** FWD-7 (the refresh record); row S348 (dell2) | **depends_on:** none.

---

## WORKER FACE

**The defect (row IRPT_BCKEND-S348, filed on dell2 by `3.0.0_SA_CVO`, measured on the served objects).** The 2026-10-06
refresh fires moved every firm's `latest.json`, but the day's manifests misstate them:
- 49F and INF: `_refresh/2026-10-06/manifest.json` stops at `state RUNNING`, `reason_code REFRESH_DISPATCHED`, `directory_revision pending`
  (notes: "last command 4237a59f-.. was dispatched for 2026-09-25 ... re-dispatching"). The end-of-fire rewrite never happened.
- COT: there is no `_refresh/2026-10-06/` manifest. Its 13:40Z fire wrote its result under `_refresh/2026-09-22/manifest.json` as a READY
  2026-09-22 build (`as_of_business_date 2026-09-22`, `dispatched_for 2026-10-06`), and that 09-22 key has been rewritten on five other
  fire days. COT's `latest.json` meanwhile points at the 2026-10-05 directory.

The code: `infra/aws/lambda/investor-reporting/directory/refresh.py`. `manifest_key(as_of)` (:80) and `put_manifest` (:165-167) key a manifest by its
`as_of_business_date`; the dispatch path records `delta.dispatched_for` (:740-818) and the build-landing path (:900-1000) carries
`built.get("dispatched_for")`. Read how the completion record picks its `as_of_business_date` for a command dispatched for an older date.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-136`; run everything from its root):

1. In `refresh.py`, the day's manifest is keyed by the business date the fire was DISPATCHED for, never by a stale command's date or by
   the built artifact's as-of; and a dispatch whose build completes rewrites THAT day's manifest from RUNNING/REFRESH_DISPATCHED to its
   terminal READY state with the revision filled. Keep every other reason code and transition as it is.
2. `infra/aws/lambda/investor-reporting/directory/tests/test_refresh_manifest_dispatch_date.py` (new): (a) the COT case of 2026-10-06, a stale command for an older
   date re-dispatched on 2026-10-06, writes and completes under `_refresh/2026-10-06/`, not under the older date; (b) with a controlled
   clock, a dispatch whose build completes reads READY in that day's manifest. The file names `2026-10-06`, `dispatched_for` and `READY`.
   Use the harness of `infra/aws/lambda/investor-reporting/directory/tests/test_refresh_expiry.py`; no AWS.
3. Run the directory suite once (`python -m pytest -q -p no:cacheprovider tests/` from `infra/aws/lambda/investor-reporting/directory`) and report its last line.

**Not yours:** the release of `irpt-directory-refresh` and the one driven refresh fire that reads READY at all three firms (the CTO's
criterion 3) are the issuer's, after the drain, under its own never-widen half.

<criterion id="IB61-5-AC1" cell_refs="IB-pr-333"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r61/p61_cells.py" . IB61-5-AC1</invocation><expect>IB61-5-AC1 PASS</expect></criterion>
`IB61-5-AC1` -- the new tests pass (COT 2026-10-06 keyed by the dispatch date; a completed build rewrites to READY) and the directory suite passes. Base: FAIL (no test).

<criterion id="IB61-G-136" cell_refs="IB-pr-333"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r61/p61_cells.py" . IB61-G-136</invocation><expect>IB61-G-136 PASS</expect></criterion>
`IB61-G-136` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB61-5-AC1,IB61-G-136</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** A change to `search.py`/`expiry.py`, to the source map, an AWS call, or an S3 write is a defect: stop and file a row.

<paths>
infra/aws/lambda/investor-reporting/directory/refresh.py
infra/aws/lambda/investor-reporting/directory/tests/test_refresh_manifest_dispatch_date.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~136/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-333.refresh-manifest-records-the-fire-that-ran.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 54 (round 61, workstream ~P), cell `IB-pr-333`.
<owned_cells>IB-pr-333</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB61-5-AC1, IB61-G-136. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~136/IRPT_BCKEND.TO-IB-pr-333.refresh-manifest-records-the-fire-that-ran.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB61-5-AC1,IB61-G-136` BEFORE the flip.
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

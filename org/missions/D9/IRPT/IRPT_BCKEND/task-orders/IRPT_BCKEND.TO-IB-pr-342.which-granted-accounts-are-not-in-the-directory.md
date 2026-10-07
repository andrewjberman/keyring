# TO IRPT_BCKEND.TO-IB-pr-342 -- a census of the 1,961 granted accounts NOT_IN_DIRECTORY: which accounts, at which firm, and why each is absent (IRPT_CUSTDY S8b)

<to_id>IRPT_BCKEND.TO-IB-pr-342</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~144</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>64</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 IRPT_CUSTDY round-3 analysis @ec25e39844, S8(b) (msg 383): routed to 2.0.0_SA_COO~P2 as a measurement cell | **Decomp cell:** `IB-pr-342`
(decomposition section 57) | **outcome_ref:** FWD-1 / FWD-7 directory coverage (IRPT_BCKEND); IRPT_CUSTDY S8(b) | **depends_on:** none.

---

## WORKER FACE

**The question (IRPT_CUSTDY S8(b)).** IRPT_CUSTDY's run found 1,961 of 7,022 granted accounts NOT_IN_DIRECTORY: the ownership
map grants them, but the served directory carries no entry. Since IRPT_CUSTDY PRD v0.3, FWD-1 reads accounts from the ownership map and
the directory supplies only names and households, so each such account still gets its report. The estate-wide 1,961 is IRPT_BCKEND's
directory-coverage question: WHICH accounts are they, and WHY is each one absent.

The figure comes from `data/assets/scripts/gold/irpt_custody/pick_reread.py` (defines NOT_IN_DIRECTORY) and `hop3_real_run.py`
(tests beside them; IRPT_CUSTDY's drain-end `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_3_DRAIN_END_20261007.md`).
The ownership map is `s3://opal-data-bd/platinum/49financial/ownership_map.json`; each firm's served directory is its `latest.json` pointer
and the `directory.json` it names, built by `infra/aws/lambda/investor-reporting/directory/` (refresh.py builds it from the firm's gold).

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-144`; run everything from its root; READ-ONLY against AWS):

1. Recompute the set yourself (do not read IRPT_CUSTDY's output files as the answer): granted accounts from the ownership map, minus the
   accounts present in each firm's served directory. Print the denominators (granted, in directory, not in directory, per firm).
2. For each account not in the directory, find WHY, from evidence you can read: e.g. absent from the source the refresh builds from,
   present in source but filtered by a refresh rule (name the rule and its line), closed/terminated, a key-shape mismatch between the map
   and the directory (name both shapes), a firm whose bucket this box cannot read. Declare your reason set in the file; an account you
   cannot explain is `UNEXPLAINED` and counted, never dropped.
3. **Fences.** This box now reads opal-data-49financial and opal-data-inflection; opal-data-cottonwood is still denied (an explicit deny).
   Probe once; for a denied bucket, record those accounts under a declared reason naming the fence, and file a row. Never widen a fence.
   Account ids are written only in the opaque form the estate already uses in deliverables (no raw custodian numbers in the file).
4. Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~144/IB64-1_directory_coverage.json`:
   `{"granted_total": N, "not_in_directory_total": M, "sources": {...}, "reason_set": [...], "by_reason": {...},
   "accounts": [{"account": "<opaque id>", "firm": "...", "reason": "...", "evidence": "..."}]}`, plus a short result note beside it
   saying what you would change in the directory build for each reason (no change is made by this order).

<criterion id="IB64-1-AC1" cell_refs="IB-pr-342"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r64/p64_cells.py" . IB64-1-AC1</invocation><expect>IB64-1-AC1 PASS</expect></criterion>
`IB64-1-AC1` -- the census file lists every NOT_IN_DIRECTORY account with firm, declared reason and evidence; totals and by_reason reconcile. Base: FAIL (no file).

<criterion id="IB64-G-144" cell_refs="IB-pr-342"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r64/p64_cells.py" . IB64-G-144</invocation><expect>IB64-G-144 PASS</expect></criterion>
`IB64-G-144` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB64-1-AC1,IB64-G-144</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure. No build upload, no apply, no AWS write.
- **Firm buckets deny this box's identity** (row S347). If you need a firm-bucket read, file a row and stop on that criterion.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** Any AWS write, any edit to the directory build or the ownership map, widening a fence, or writing a raw custodian account number is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~144/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-342.which-granted-accounts-are-not-in-the-directory.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 57 (round 64, workstream ~P), cell `IB-pr-342`.
<owned_cells>IB-pr-342</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB64-1-AC1, IB64-G-144. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~144/IRPT_BCKEND.TO-IB-pr-342.which-granted-accounts-are-not-in-the-directory.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB64-1-AC1,IB64-G-144` BEFORE the flip.
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
comp-adversary: RUN -- every criterion dry-run at base 33949e002d 2026-10-07 ~10:5xZ: AC1 FAIL, guard PASS (p64_cells.py).
lane: the <paths> block IS the grant.
</preflight>

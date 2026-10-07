# TO IRPT_BCKEND.TO-IB-pr-337 -- irpt-directory-refresh stages handler.py from the running blob 48313e9c0e, so the r61 release ships refresh.py alone (row S357)

<to_id>IRPT_BCKEND.TO-IB-pr-337</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~139</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>62</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 CTO half for the r61 directory release @74e91285b4, item (1) | **Decomp cell:** `IB-pr-337`
(decomposition section 55) | **outcome_ref:** FWD-7 (the r61 directory release); row S357 | **depends_on:** none.

---

## WORKER FACE

**The rider (row IRPT_BCKEND-S357).** Live `irpt-directory-refresh` runs `handler.py` blob 48313e9c0e (sha256 e46922a00379). HEAD's
`infra/aws/lambda/investor-reporting/directory/handler.py` is the 2026-09-26 UIR-07 version (3865775e75f8), so a refresh build today ships two changes: the round-61 `refresh.py`
and an unreleased `handler.py`. The CTO half (@74e91285b4) pins `handler.py` back; UIR-07 ships later as its own cell.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-139`; run everything from its root):

1. In `infra/aws/lambda/ci/lambda-source-map.json`, row `irpt-directory-refresh` ONLY: add a `staged_from` member for `handler.py` with `repo_path`
   `infra/aws/lambda/investor-reporting/directory/handler.py`, `pin` the full hash of 48313e9c0e (`git rev-parse 48313e9c0e`), `packaged_as` `handler.py` and its `sha256`
   (of `git show 48313e9c0e:infra/aws/lambda/investor-reporting/directory/handler.py`). Follow the shape of the existing `staged_from` entries in neighbouring rows exactly.
   Touch no other row (`irpt-directory-search` shares the source_dir and must keep HEAD's files).
2. Run `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-directory-refresh` and report its last line.
3. Run `python infra/aws/lambda/ci/release-census.py irpt-directory-refresh --pin $(git rev-parse --short HEAD)` (read-only `get-function`) and put its
   output in your deliverables folder.

<criterion id="IB62-2-AC1" cell_refs="IB-pr-337"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r62/p62_cells.py" . IB62-2-AC1</invocation><expect>IB62-2-AC1 PASS</expect></criterion>
`IB62-2-AC1` -- the census of irpt-directory-refresh at HEAD prints changed_members=1 and the one member is refresh.py. Base: FAIL (2: handler.py rides).

<criterion id="IB62-G-139" cell_refs="IB-pr-337"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r62/p62_cells.py" . IB62-G-139</invocation><expect>IB62-G-139 PASS</expect></criterion>
`IB62-G-139` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB62-2-AC1,IB62-G-139</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure. No build upload, no apply, no AWS write.
- **Firm buckets deny this box's identity** (row S347). If you need a firm-bucket read, file a row and stop on that criterion.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** An edit to any map row other than irpt-directory-refresh, to `handler.py` itself, an upload or an apply is a defect: stop and file a row.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~139/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-337.refresh-handler-pinned-to-the-running-blob.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 55 (round 62, workstream ~P), cell `IB-pr-337`.
<owned_cells>IB-pr-337</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB62-2-AC1, IB62-G-139. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~139/IRPT_BCKEND.TO-IB-pr-337.refresh-handler-pinned-to-the-running-blob.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB62-2-AC1,IB62-G-139` BEFORE the flip.
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

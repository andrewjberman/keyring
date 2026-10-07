# TO IRPT_BCKEND.TO-IB-pr-348 -- the custodian-key seam guard treats every spelling of a null-like as unmapped (E-P8 criterion 4)

<to_id>IRPT_BCKEND.TO-IB-pr-348</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~149</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>67</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 IRPT_CUSTDY round-4 analysis @16d9b128c0 (msg 512): E-P8 gains criterion (4) | **Decomp cell:** `IB-pr-348`
(decomposition section 60) | **outcome_ref:** FWD-1 / FWD-2 account coverage (IRPT_CUSTDY W5-S1) | **depends_on:** IB-pr-339 (drained).

---

## WORKER FACE

**The gap.** `infra/aws/lambda/investor-reporting/_ids/ids.py:388` (IB-pr-339) reads
`if mapped is not None and str(mapped).strip() not in ("", "None", "nan"):` -- a case-SENSITIVE match, so `none`, `NONE`, `NaN`, `NULL`
or `null` would still reach the mint (0 such values in the seam today, but the seam's writer is not in the repo, row W141-S1).

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-149`; run everything from its root):

1. In `ids.py` only, the guard treats an empty value and every spelling of `none`, `nan` and `null` as unmapped, case-insensitively
   (after strip): the account is returned raw, never minted from it.
2. Tests in `infra/aws/lambda/investor-reporting/_ids/tests/` (extend the IB-pr-339 test file or add one): one test per spelling `'none'`, `'NONE'`, `'NaN'`, `'NULL'`,
   `'null'` (plus the existing `'None'`, `'nan'`, empty), each returning the raw account; a real mapping still mints.
3. Run the `_ids` suite once and report its last line.

<criterion id="IB67-2-AC1" cell_refs="IB-pr-348"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r67/p67_cells.py" . IB67-2-AC1</invocation><expect>IB67-2-AC1 PASS</expect></criterion>
`IB67-2-AC1` -- a test names each null-like spelling and the _ids suite passes. Base: FAIL.

<criterion id="IB67-G-149" cell_refs="IB-pr-348"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r67/p67_cells.py" . IB67-G-149</invocation><expect>IB67-G-149 PASS</expect></criterion>
`IB67-G-149` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB67-2-AC1,IB67-G-149</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure. No build upload, no apply, no AWS write.
- **Firm buckets deny this box's identity** (row S347). If you need a firm-bucket read, file a row and stop on that criterion.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** An edit outside `_ids/ids.py` and `_ids/tests/`, or a change to the seam data, is a defect: stop and file a row.

<paths>
infra/aws/lambda/investor-reporting/_ids/ids.py
infra/aws/lambda/investor-reporting/_ids/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~149/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-348.null-like-guard-is-case-insensitive.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 60 (round 67, workstream ~P), cell `IB-pr-348`.
<owned_cells>IB-pr-348</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB67-2-AC1, IB67-G-149. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~149/IRPT_BCKEND.TO-IB-pr-348.null-like-guard-is-case-insensitive.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB67-2-AC1,IB67-G-149` BEFORE the flip.
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

# TO IRPT_BCKEND.TO-IB-pr-339 -- the custodian-key seam carries no stringified null, and the projection returns a 'None'-mapped account raw instead of refusing it (IRPT_CUSTDY W5-S1)

<to_id>IRPT_BCKEND.TO-IB-pr-339</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~141</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>62</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-61 analysis @aae1ed7781 section 3 item E-P8 (IRPT_CUSTDY row W5-S1; msg 272; widened to nan by msg 281) | **Decomp cell:** `IB-pr-339`
(decomposition section 55) | **outcome_ref:** FWD-2 / FWD-1 account coverage (482 of 7022 granted accounts refused); IRPT_CUSTDY W5-S1 | **depends_on:** none.

---

## WORKER FACE

**The defect (IRPT_CUSTDY row W5-S1, measured by `2.0.0_SA_COO~K2`).** `infra/aws/lambda/investor-reporting/_ids/data/custodian_key_seam.json` (written by
`0.9.0_WK_IRPT_BCKEND~1`, IB-rte-6, @47f21dab95) maps 826 of its 6202 index keys to the STRING `'None'` (0 are JSON null); its named source,
the BD `dim_account_xref` silver of 2026-09-16, has 826 `schwab_account_id` nulls and 0 'None' strings, so the stringification happened
when the seam was written (that writer is not in the repo). `infra/aws/lambda/investor-reporting/_ids/ids.py:387-389`:
`mapped = idx.get(str(raw).strip())` / `if mapped is not None: return base("account", mapped)` passes `'None'` to the mint, which raises
`IdRefused`, so 482 of 7022 live granted accounts (31 of 190 advisors) are refused instead of graded.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-141`; run everything from its root):

1. **The data.** Remove every index entry whose value is the string `'None'` from `custodian_key_seam.json` (do not invent a mapping);
   keep every other byte of the file's shape; record the count removed in the file's own provenance field if it has one, else in your
   result file.
2. **The guard.** In `ids.py`'s seam projection, a mapped value that is empty, the string `'None'` or the string `'nan'` (after strip;
   widened to `'nan'` by `1.0.0_SA_CTO~DELL2` msg 281) is treated as unmapped: the account is returned raw (the same path an unmapped key
   takes today), never minted from it.
3. **Tests** in `infra/aws/lambda/investor-reporting/_ids/tests/` (new file or an added test): a seam value `'None'` and a seam value `'nan'` each return the raw account and
   do not raise; a real mapping still mints; and a test that FAILS on the seam file as it stands at the base (826 'None' values). The test
   file names the string `'None'`.
4. **The writer.** Find the script that wrote the seam (its `_written_by` field names `0.9.0_WK_IRPT_BCKEND~1 / IRPT_BCKEND.TO-IB-rte-6`,
   commit 47f21dab95). Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~141/seam_writer.txt` with one line `WRITER: <repo path>` if it is in
   the repo, or file a row saying it is not and write `NOT IN REPO: <that row id>`.
5. Run the `_ids` suite once (`python -m pytest -q -p no:cacheprovider tests/` from `infra/aws/lambda/investor-reporting/_ids`) and report its last line.

<criterion id="IB62-4-AC1" cell_refs="IB-pr-339"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r62/p62_cells.py" . IB62-4-AC1</invocation><expect>IB62-4-AC1 PASS</expect></criterion>
`IB62-4-AC1` -- the seam index holds 0 'None' values, and the new tests plus the _ids suite pass. Base: FAIL (826 'None').

<criterion id="IB62-4-AC2" cell_refs="IB-pr-339"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r62/p62_cells.py" . IB62-4-AC2</invocation><expect>IB62-4-AC2 PASS</expect></criterion>
`IB62-4-AC2` -- seam_writer.txt names the writer's repo path, or a row saying it is not in the repo. Base: FAIL.

<criterion id="IB62-G-141" cell_refs="IB-pr-339"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r62/p62_cells.py" . IB62-G-141</invocation><expect>IB62-G-141 PASS</expect></criterion>
`IB62-G-141` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB62-4-AC1,IB62-4-AC2,IB62-G-141</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure. No build upload, no apply, no AWS write.
- **Firm buckets deny this box's identity** (row S347). If you need a firm-bucket read, file a row and stop on that criterion.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** A mapping invented for a null key, an edit outside `_ids/`, or a build/deploy is a defect: stop and file a row.

<paths>
infra/aws/lambda/investor-reporting/_ids/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~141/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-339.seam-none-strings-are-not-custodian-keys.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 55 (round 62, workstream ~P), cell `IB-pr-339`.
<owned_cells>IB-pr-339</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB62-4-AC1, IB62-4-AC2, IB62-G-141. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~141/IRPT_BCKEND.TO-IB-pr-339.seam-none-strings-are-not-custodian-keys.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB62-4-AC1,IB62-4-AC2,IB62-G-141` BEFORE the flip.
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

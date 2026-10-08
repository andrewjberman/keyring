# TO IRPT_BCKEND.TO-IB-pr-360 -- the back-fill operator tool moves to export/tools/, so the export build's ADHC_DRIFTD.002 parity limb passes without BAU_PARITY_SKIP (row S381)

<to_id>IRPT_BCKEND.TO-IB-pr-360</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~168</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>74</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** issuer ruling on row S381 (0.7.0_AE_CloudOps~I): every irpt-export-render build since IB-pr-344 needs BAU_PARITY_SKIP=1 | **Decomp cell:** `IB-pr-360`
(decomposition section 67) | **outcome_ref:** FWD-2 / FWD-8 (every later export release builds clean) | **depends_on:** none.

---

## WORKER FACE

**The defect (row S381).**
- `infra/aws/lambda/investor-reporting/export/backfill_covered_account_ids.py` (IB-pr-344's operator tool, run by hand under a never-widen pair) sits at the top level of the
  export Lambda's source dir.
- `infra/aws/lambda/ci/build-and-upload.sh`'s ADHC_DRIFTD.002 parity limb refuses any top-level `*.py` in that dir that is not in
  the build list (`lambda-source-map.json` `files[]`). So every `irpt-export-render` build since IB-pr-344 needs
  `BAU_PARITY_SKIP=1`, which disables the extras limb for everything.
- No packaged member imports the tool; its only importer is `infra/aws/lambda/investor-reporting/export/tests/test_backfill_covered_account_ids.py`.
- Registering it in `files[]` would package an operator script into the served zip, so the right home is outside the scanned top
  level.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-168`; run everything from its root):

1. **Move it.** `git mv infra/aws/lambda/investor-reporting/export/backfill_covered_account_ids.py infra/aws/lambda/investor-reporting/export/tools/backfill_covered_account_ids.py` (create `tools/`).
   - It inserts its own directory on `sys.path` to import `bundle` (the freeze's function) and the export modules beside it; point
     that at the PARENT directory (`infra/aws/lambda/investor-reporting/export`), so it still imports them unchanged and copies nothing.
   - `python infra/aws/lambda/investor-reporting/export/tools/backfill_covered_account_ids.py --help` works.
2. **Update its test import:** `infra/aws/lambda/investor-reporting/export/tests/test_backfill_covered_account_ids.py` (path only; no assertion changes). It passes.
3. **Out of scope:** no change to `build-and-upload.sh`, to the source map, or to any packaged member. The deployed zip is unchanged
   by this cell.

<criterion id="IB74-1-AC1" cell_refs="IB-pr-360"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r74/p74_cells.py" . IB74-1-AC1</invocation><expect>IB74-1-AC1 PASS</expect></criterion>
`IB74-1-AC1` -- the ADHC_DRIFTD.002 rule finds 0 extras in the export source dir, the tool runs --help from export/tools/, and its tests pass. Base: FAIL (1 extra).

<criterion id="IB74-G-168" cell_refs="IB-pr-360"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r74/p74_cells.py" . IB74-G-168</invocation><expect>IB74-G-168 PASS</expect></criterion>
`IB74-G-168` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB74-1-AC1,IB74-G-168</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **Vendor egress (Andrew-direct ~18:3xZ 2026-10-07, VERBATIM: "The Dell Boxes have vendor egress as needed."):** this cell needs
  none, so it makes none. No build upload, no apply, no AWS write.
- **Web and downloads (Andrew-direct ~14:0xZ 2026-10-07, VERBATIM: "I do not mind webbrowsing if necessary for research purposes,
  however we do not do downloads."; download tiers bind EVERY box, record @875c5a9b54):** research browsing only when necessary;
  no package, script, program or file fetched from the internet onto any box (the laptop alone fetches, by the checked route);
  `bun` only as `bun --no-install` with a linked node_modules (rules 106215/106221). A vendor API call is not browsing.
- **Fence (ruling 106244, row S371):** only `opal-data-cottonwood` denies this box's identity; the legacy `opal-data-bd/-cot/-inf` are
  inside its grant. A read never widens a fence. A denied read is a row and a stop on that criterion.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** An edit to build-and-upload.sh, lambda-source-map.json or any packaged member, or a run of --apply, is a defect: stop and file a row.

<paths>
infra/aws/lambda/investor-reporting/export/backfill_covered_account_ids.py
infra/aws/lambda/investor-reporting/export/tools/
infra/aws/lambda/investor-reporting/export/tests/test_backfill_covered_account_ids.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~168/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-360.backfill-tool-moves-out-of-the-export-source-dir.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 67 (round 74, workstream ~P), cell `IB-pr-360`.
<owned_cells>IB-pr-360</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB74-1-AC1, IB74-G-168. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~168/IRPT_BCKEND.TO-IB-pr-360.backfill-tool-moves-out-of-the-export-source-dir.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB74-1-AC1,IB74-G-168` BEFORE the flip.
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
comp-adversary: RUN -- every criterion dry-run at base 8be1d0b344 2026-10-07 ~01:1xZ 2026-10-08: build checks FAIL, guards PASS (p74_cells.py).
lane: the <paths> block IS the grant.
</preflight>

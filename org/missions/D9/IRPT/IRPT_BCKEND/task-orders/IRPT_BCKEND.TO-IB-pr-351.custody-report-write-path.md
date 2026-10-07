# TO IRPT_BCKEND.TO-IB-pr-351 -- P-c1: a custody write path persists a CUSTODY_REPORT document in the retained store under its kind (IRPT_CUSTDY-S14 break 1)

<to_id>IRPT_BCKEND.TO-IB-pr-351</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~160</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>70</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 IRPT_CUSTDY round-6 ADDENDUM 1 @c3addc6f25 ruling item 2 (msg 915), cut now as round 70 on msg 917; closes IRPT_CUSTDY-S14 break 1 | **Decomp cell:** `IB-pr-351`
(decomposition section 63) | **outcome_ref:** FWD-8 / IRPT_CUSTDY hop 5 (the custody report export) | **depends_on:** none.

---

## WORKER FACE

**The break.** No caller writes a custody document into the retained store. `infra/aws/lambda/investor-reporting/reports/repository.py:135`
`ReportRepository.persist(principal, owner, report_kind, request_ref, report, provenance)` already accepts `"CUSTODY_REPORT"`
(`reports/tests/test_repository.py:156`), but its only production callers persist `PERFORMANCE` (`performance/retained.py:330`) and
`ANALYSIS` (`ycharts/generate/publisher.py:199`). The export side already reads one back:
- `infra/aws/lambda/investor-reporting/export/retained_export.py:87` `resolve` admits `report_kind == "CUSTODY_REPORT"` when the owner carries `account_set_id`
  and `account_ids` (a server-issued selection) and the report is a dict.
- `export/narrative_submit.py` `custody_report_as_of` reads the document's `as_of_date`.

So a write must produce exactly what `resolve` admits. The CTO's ruling reads: **reuse `ReportRepository.persist`; no second
repository.**

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-160`; run everything from its root):

1. **`infra/aws/lambda/investor-reporting/reports/custody_write.py` (new).** One function, `persist_custody_report(reports, principal, owner, request_ref, document,
   provenance)`. It refuses, by name, three cases:
   - an owner without `account_set_id` or a non-empty `account_ids`;
   - a document that is not a dict or carries no `as_of_date` (an ISO date string, 2024 or later);
   - an empty provenance.

   Otherwise it calls `reports.persist(principal, owner, "CUSTODY_REPORT", request_ref, document, provenance)` and returns its ref.
   It changes nothing in `repository.py`.
2. **`infra/aws/lambda/investor-reporting/reports/tests/test_custody_write.py` (new).** It uses the in-memory repository the sibling tests in `reports/tests/` build.
   - **Round trip:** persist a custody document, then read it back through `export/retained_export.py` `resolve` under the same
     principal. It resolves with `kind == "CUSTODY_REPORT"`, the same `as_of_date`, and a row naming the persisted
     report_id/revision.
   - **The three refusals:** each refusal case above.
   - **Out of scope:** a principal of another firm is refused by the repository's own `_allow`, exactly as for ANALYSIS.

   Import `retained_export` the way `export/tests/test_submit_custody_report.py` does.
3. Run `python -m pytest -q tests/` from `infra/aws/lambda/investor-reporting/reports` once, and report its last line.

<criterion id="IB70-1-AC1" cell_refs="IB-pr-351"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r70/p70_cells.py" . IB70-1-AC1</invocation><expect>IB70-1-AC1 PASS</expect></criterion>
`IB70-1-AC1` -- the custody write test (round trip through retained_export.resolve, the refusals) passes; the reports suite and test_submit_custody_report pass. Base: FAIL (no test).

<criterion id="IB70-G-160" cell_refs="IB-pr-351"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r70/p70_cells.py" . IB70-G-160</invocation><expect>IB70-G-160 PASS</expect></criterion>
`IB70-G-160` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB70-1-AC1,IB70-G-160</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure. No build upload, no apply, no AWS write.
- **Web and downloads (Andrew-direct ~14:0xZ 2026-10-07, VERBATIM: "I do not mind webbrowsing if necessary for research purposes,
  however we do not do downloads."; download tiers bind EVERY box, record @875c5a9b54):** research browsing only when necessary;
  no package, script, program or file fetched from the internet onto any box (the laptop alone fetches, by the checked route);
  `bun` only as `bun --no-install` with a linked node_modules (rules 106215/106221). A vendor API call is not browsing.
- **Fence (ruling 106244, row S371):** only `opal-data-cottonwood` denies this box's identity; the legacy `opal-data-bd/-cot/-inf` are
  inside its grant. A read never widens a fence. A denied read is a row and a stop on that criterion.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** An edit to repository.py, retained_export.py or any other file outside your two paths, or a second repository class, is a defect: stop and file a row.

<paths>
infra/aws/lambda/investor-reporting/reports/custody_write.py
infra/aws/lambda/investor-reporting/reports/tests/test_custody_write.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~160/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-351.custody-report-write-path.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 63 (round 70, workstream ~P), cell `IB-pr-351`.
<owned_cells>IB-pr-351</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB70-1-AC1, IB70-G-160. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~160/IRPT_BCKEND.TO-IB-pr-351.custody-report-write-path.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB70-1-AC1,IB70-G-160` BEFORE the flip.
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
comp-adversary: RUN -- every criterion dry-run at base c09237491c 2026-10-07 ~17:4xZ: build checks FAIL, guards PASS (p70_cells.py).
lane: the <paths> block IS the grant.
</preflight>

# TO IRPT_BCKEND.TO-IB-pr-352 -- P-c2: the export's accept reads the business date by kind -- as_of_date for a custody report, dates.actual_end for the others (IRPT_CUSTDY-S14 break 2)

<to_id>IRPT_BCKEND.TO-IB-pr-352</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~161</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>70</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 IRPT_CUSTDY round-6 ADDENDUM 1 @c3addc6f25 ruling item 2 (msg 915), cut now as round 70 on msg 917; closes IRPT_CUSTDY-S14 break 2 | **Decomp cell:** `IB-pr-352`
(decomposition section 63) | **outcome_ref:** FWD-8 / IRPT_CUSTDY hop 5 | **depends_on:** none.

---

## WORKER FACE

**The break.** `infra/aws/lambda/investor-reporting/export/submit_async.py:113` `accept(body, scope, *, tenant, ports, invoke, event=None, now=None)`,
on its non-platinum branch (about `:137`), reads `business_date = resolved["report"]["dates"]["actual_end"]`. A custody document has no
`dates`; it carries `as_of_date` (`export/narrative_submit.py` `custody_report_as_of`). So `accept` raises `KeyError` on every custody
export. The existing `export/tests/test_submit_custody_report.py` calls `serve_submit` directly and never reached `accept`.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-161`; run everything from its root):

1. **In `infra/aws/lambda/investor-reporting/export/submit_async.py` only.** On the non-platinum branch, read the business date by `resolved["kind"]`:
   - `CUSTODY_REPORT` uses the document's `as_of_date`, through the same reader `narrative_submit.custody_report_as_of` uses (import
     it; do not copy it);
   - every other kind keeps `report["dates"]["actual_end"]`;
   - a custody document with no `as_of_date` is refused by name (`ExportSubmitRefused` or the module's existing refusal), never a
     `KeyError`.

   The platinum branch is unchanged.
2. **`infra/aws/lambda/investor-reporting/export/tests/test_accept_business_date.py` (new).** It drives `accept(...)` itself with fake ports. Use the sibling tests'
   fakes as the pattern, for example `test_retained_export.py` and `test_submit_custody_report.py`.
   - **A CUSTODY_REPORT reference:** accept writes its pointer with no KeyError, and the business date is the document's
     `as_of_date`.
   - **A PERFORMANCE reference:** it still reads `dates.actual_end`.
   - **A custody document missing `as_of_date`:** refused by name.
3. Run the new test and `tests/test_submit_custody_report.py` from `infra/aws/lambda/investor-reporting/export` once, and report the last line.

<criterion id="IB70-2-AC1" cell_refs="IB-pr-352"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r70/p70_cells.py" . IB70-2-AC1</invocation><expect>IB70-2-AC1 PASS</expect></criterion>
`IB70-2-AC1` -- a test drives accept( over a custody as_of_date and a performance actual_end and both pass, with test_submit_custody_report. Base: FAIL (no test).

<criterion id="IB70-G-161" cell_refs="IB-pr-352"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r70/p70_cells.py" . IB70-G-161</invocation><expect>IB70-G-161 PASS</expect></criterion>
`IB70-G-161` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB70-2-AC1,IB70-G-161</expected_criteria>

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
- **Refusal clause.** An edit outside submit_async.py and the new test, a copied as_of reader, or a change to the platinum branch is a defect: stop and file a row.

<paths>
infra/aws/lambda/investor-reporting/export/submit_async.py
infra/aws/lambda/investor-reporting/export/tests/test_accept_business_date.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~161/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-352.accept-reads-business-date-by-kind.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 63 (round 70, workstream ~P), cell `IB-pr-352`.
<owned_cells>IB-pr-352</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB70-2-AC1, IB70-G-161. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~161/IRPT_BCKEND.TO-IB-pr-352.accept-reads-business-date-by-kind.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB70-2-AC1,IB70-G-161` BEFORE the flip.
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

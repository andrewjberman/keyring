# TO IRPT_BCKEND.TO-IB-pr-491 -- the producer's two AnalysisReport contract fixtures send a section the extractor can send (row DSGN_IRPTV1-D2-W63-S1)

<to_id>IRPT_BCKEND.TO-IB-pr-491</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~342</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>169</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's routing of row `DSGN_IRPTV1-D2-W63-S1` (CTO msg 6626; CTO ROUND-31 ANALYSIS of DSGN_IRPTV1 section 1) and the CTO ROUND-169 ANALYSIS section 3 item 3 | **Decomp cell:** `IB-pr-491` (decomposition section 161) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-491` (inlined):** the producer's two contract fixtures carry a vendor section the producer's extractor cannot send: `section_type` `annualized_return` and `units` `DECIMAL_FRACTION`. The extractor (`infra/aws/lambda/investor-reporting/ycharts/extract/extract.py`, lines 755-762) builds a section as `section_id` = `"<code>.<field slug>.c<n>"`, `section_type` = the census section code (a digit string, for example `2` for "Key Stats"), `units` = the census unit token, one of `count, date, enum, number, pct, price, ratio, score, text, usd_billions, years`. Change ONLY these two files' section so that it is a section the extractor could send, keeping its meaning (an annualized return of 7.12 percent):

- `C:\dev\ajb_workspace\infra\aws\lambda\investor-reporting\_contracts\fixtures\AnalysisReport.valid.json`
- `C:\dev\ajb_workspace\infra\aws\lambda\investor-reporting\_contracts\fixtures\AnalysisReport.v2.ycharts.valid.json`

In `instance.sections[0]` of each: `section_id` `2.annualized_return.c1`, `section_type` `2`, `value` `7.12`, `units` `pct`. Leave every other field of the section and of the fixture unchanged (`as_of_date`, `page`, `bbox`, and the v2 file's own extra members). Read `extract.py:705-762` first and confirm the form; if the code form differs from the above, use the extractor's form and say so in the report.

Do NOT edit either schema, `extract.py`, any test, or anything under `portal/` (the portal's wire copy and its generators are a later cell). If either fixture then fails to validate against its schema, or a test in `infra/aws/lambda/investor-reporting/_contracts/` asserts the old tokens, change nothing further, file a row naming the file and the assertion, and STOP.

**Criteria (run each under `timeout 120`, record the output and exit code verbatim):**

<criterion id="IB169-4-AC1" cell_refs="IB-pr-491"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r169/p169_cells.py" . IB169-4-AC1</invocation><expect>IB169-4-AC1 PASS</expect></criterion>
<criterion id="IB169-4-AC2" cell_refs="IB-pr-491"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r169/p169_cells.py" . IB169-4-AC2</invocation><expect>IB169-4-AC2 PASS</expect></criterion>
<criterion id="IB169-4-AC3" cell_refs="IB-pr-491"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r169/p169_cells.py" . IB169-4-AC3</invocation><expect>IB169-4-AC3 PASS</expect></criterion>

<expected_criteria>IB169-4-AC1, IB169-4-AC2, IB169-4-AC3</expected_criteria>

What the checks grade: AC1 neither fixture carries `annualized_return` or `DECIMAL_FRACTION`, every section's `units` is an extractor token, its `section_type` a digit string and its `section_id` begins with that code and a dot; AC2 both fixtures' `instance` still validates against its schema (a bound, passing at base); AC3 nothing outside the grant changed (a bound, passing in a clean worktree).

## BOUNDS

- **Grant:** the `paths` block and nothing else. No deploy, no served value moves (these are fixtures; no served artifact reads them). No schema, extractor, test or portal edit.
- **Refusal clause:** STOP, file a row, change nothing more, on a schema failure, a test asserting the old tokens, or an extractor form that the fixture cannot take without a schema change (a producer fixture that cannot send what its code sends is a contract question for the CTO).
- **Row ids** are `IRPT_BCKEND-D2-W342-S<k>` (the next free `k`).
- **Commit** on your worktree branch per your definition; ASCII only. Report once, under 150 words.

<paths>
infra/aws/lambda/investor-reporting/_contracts/fixtures/AnalysisReport.valid.json
infra/aws/lambda/investor-reporting/_contracts/fixtures/AnalysisReport.v2.ycharts.valid.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~342/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-491.analysisreport-fixtures-extractor-real.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 161 (round 169, workstream ~P), cell `IB-pr-491`.
<owned_cells>IB-pr-491</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB169-4-AC1, IB169-4-AC2, IB169-4-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~342/IRPT_BCKEND.TO-IB-pr-491.analysisreport-fixtures-extractor-real.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- two JSON test fixtures under `infra/aws/lambda/investor-reporting/_contracts/fixtures/`; no function, role, table or served artifact reads them at run time (the gate floor forces class WORLD for any `infra/` path regardless).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p169_cells.py dry-run at base on dell2 2026-10-12 ~23:2xZ: IB169-4 AC1 FAIL (both fixtures carry the old tokens), AC2 PASS (both validate), AC3 PASS (in a clean worktree at HEAD; the shared tree is dirty with other seats' files). Not run: whether another test asserts the old tokens; the face makes that a STOP.
lane: the <paths> block IS the grant; worker slot ~342 of IRPT_BCKEND. Class WORLD (the `infra/` floor).
</preflight>

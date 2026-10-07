# TO IRPT_BCKEND.TO-IB-pr-345 -- exposure: a read-log census of cross-scope export reads while the fail-open branch was served (PRD v0.30 item 36)

<to_id>IRPT_BCKEND.TO-IB-pr-345</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~146</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>65</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 PRIORITY msg 439, PRD v0.30 item 36, item (3) | **Decomp cell:** `IB-pr-345`
(decomposition section 58) | **outcome_ref:** FWD-2 (did the fail-open branch ever admit a read outside the caller's scope?) | **depends_on:** none.

---

## WORKER FACE

**The question (PRD v0.30 item 36).** `infra/aws/lambda/investor-reporting/export/entry.py` `_covered` admitted any firm advisor holding an export id whenever the receipt
named no account (row W142-S4). Did any export read, while that branch was served, admit a caller whose scope did not cover the export?

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-146`; run everything from its root; READ-ONLY):

1. Find which deployed functions serve export reads (the receipt and download routes; start from `infra/aws/lambda/investor-reporting/export/entry.py` and routes.json) and their
   CloudWatch log groups (`/aws/lambda/irpt-export-render` is one). Find the window the fail-open branch was SERVED (the deploys that
   carried `_covered` without the empty-list refusal: the source-map / CHANGELOG deploy records and live `get-function-configuration`).
2. Read the logs over that window (`.tools/aws logs filter-log-events`, paginated; print the denominator: events scanned per group) and
   identify every export read that was ADMITTED with an empty covered set and a caller whose scope did not include the export's accounts.
   Say exactly what the log lets you see and what it cannot (e.g. if the log does not record the covered set, state the inference).
3. Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~146/IB65-3_exposure_census.json`:
   `{"log_groups": [...], "window": "...", "events_scanned": {...}, "count": N, "cross_scope_reads": [...], "blocking_row": "<id or empty>",
   "limits": "..."}`. A non-zero count is a BLOCKING row you file, named in `blocking_row`. No principal, account or caller identity beyond
   the opaque ids the logs already carry goes into the file.

<criterion id="IB65-3-AC1" cell_refs="IB-pr-345"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r65/p65_cells.py" . IB65-3-AC1</invocation><expect>IB65-3-AC1 PASS</expect></criterion>
`IB65-3-AC1` -- the exposure census names log groups and window, prints a count equal to the entries listed, and a non-zero count names a BLOCKING row in the channel. Base: FAIL.

<criterion id="IB65-G-146" cell_refs="IB-pr-345"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r65/p65_cells.py" . IB65-G-146</invocation><expect>IB65-G-146 PASS</expect></criterion>
`IB65-G-146` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB65-3-AC1,IB65-G-146</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure. No build upload, no apply, no AWS write.
- **Firm buckets deny this box's identity** (row S347). If you need a firm-bucket read, file a row and stop on that criterion.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** Any write to AWS, any change to a log, or raw personal data in the census file is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~146/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-345.export-cross-scope-read-exposure.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 58 (round 65, workstream ~P), cell `IB-pr-345`.
<owned_cells>IB-pr-345</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB65-3-AC1, IB65-G-146. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~146/IRPT_BCKEND.TO-IB-pr-345.export-cross-scope-read-exposure.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB65-3-AC1,IB65-G-146` BEFORE the flip.
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
comp-adversary: RUN -- every criterion dry-run at base 31b26bff2d 2026-10-07 ~11:5xZ: build checks FAIL, guards PASS (p65_cells.py).
lane: the <paths> block IS the grant.
</preflight>

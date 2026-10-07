# TO IRPT_BCKEND.TO-IB-pr-338 -- every reader of the directory-search response handles both the plain list and the over-age envelope (release precondition P1)

<to_id>IRPT_BCKEND.TO-IB-pr-338</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~140</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>62</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 CTO half for the r61 directory release @74e91285b4, item (2) | **Decomp cell:** `IB-pr-338`
(decomposition section 55) | **outcome_ref:** FWD-7 (the r61 directory release precondition P1); row W136-S1 | **depends_on:** none.

---

## WORKER FACE

**The change being released (round 61, IB-pr-334).** `irpt-directory-search` (`infra/aws/lambda/investor-reporting/directory/entry.py`, `entry.search`) answers an
in-age request with the plain hit list, as today, and an over-age request (directory `as_of_business_date` more than
`MAX_AGE_TRADING_DAYS` = 2 trading days old, or age uncomputable) with `{"_data": <stale hits>, "_status": <expiry envelope>}`,
carrying `DIRECTORY_OVER_AGE`/`STALE` or `CALENDAR_UNAVAILABLE`/`UNCERTAIN`. `DIRECTORY_OVER_AGE` is NOT in `_authz/served.py`
BOUNDARY_REASONS (row W136-S1). The CTO's condition: census every reader of the search response (the route search plus DirectoryEntry
search; denominator printed; IRPT_CUSTDY's hop-1 reader included); each reader passes a test on BOTH the over-age and the plain fixture;
any failure holds the release.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-140`, with a nested portal worktree at `C:/dev/wk-irpt-bckend-140/portal`
on portal DEV `8ddfe409`; run everything from the workspace root unless a step says portal):

1. **Census.** Every code path that consumes the directory-search response: in the portal (start from `portal/src/api/endpoints/investor-reporting.ts`,
   `portal/src/pages/InvestorReporting/header/search.ts`, `contracts/directory-browse.ts`, `contracts/wire/DirectoryEntry.ts`; follow every caller),
   in the backend (any Lambda that calls the search entry), and IRPT_CUSTDY's hop-1 reader (under `data/assets/scripts/gold/irpt_custody/`
   or wherever IRPT_CUSTDY reads the directory; find it). Print how you enumerated and the count.
2. **Two fixtures.** A plain-list response and an over-age envelope response, both from the real `entry.search` at HEAD driven with a
   controlled clock (2026 dates).
3. **One test per reader, both fixtures.** Portal readers: a test under `portal/src/pages/InvestorReporting/__tests__/ir-62-overage/` run
   with the portal's own runner (`bun test <file>` from `portal/`). Backend readers: `infra/aws/lambda/investor-reporting/directory/tests/test_search_readers_overage.py`.
   IRPT_CUSTDY reader: `data/assets/scripts/gold/irpt_custody/tests/test_directory_search_overage_reader.py`. A reader that breaks on the
   envelope is a FAIL: record it, file a BLOCKING row naming it, and do NOT fix the reader (fixes are the next round's).
4. **Census file** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~140/IB62-3_reader_census.json`:
   `{"reader_count": N, "enumeration": "...", "readers": [{"path": "...", "kind": "portal|backend|irpt_custody", "plain": {"result":
   "PASS"|"FAIL", "test": "<path::name>"}, "over_age": {...}}]}`.
5. Commit the portal tests on the portal worktree's branch (the issuer lands them on portal DEV at the drain) and the rest on the workspace
   branch.

<criterion id="IB62-3-AC1" cell_refs="IB-pr-338"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r62/p62_cells.py" . IB62-3-AC1</invocation><expect>IB62-3-AC1 PASS</expect></criterion>
`IB62-3-AC1` -- the census file lists every reader (count = listed, an IRPT_CUSTDY reader included), each with both fixtures' result and test. Base: FAIL (no census).

<criterion id="IB62-G-140" cell_refs="IB-pr-338"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r62/p62_cells.py" . IB62-G-140</invocation><expect>IB62-G-140 PASS</expect></criterion>
`IB62-G-140` -- a GUARD: your workspace commits touch only your grant. Base: PASS.

<expected_criteria>IB62-3-AC1,IB62-G-140</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure. No build upload, no apply, no AWS write.
- **Firm buckets deny this box's identity** (row S347). If you need a firm-bucket read, file a row and stop on that criterion.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** An edit to any reader, to `entry.py`/`expiry.py`, to a portal product file, or a deploy is a defect: stop and file a row.

<paths>
portal/src/pages/InvestorReporting/__tests__/ir-62-overage/
data/assets/scripts/gold/irpt_custody/tests/test_directory_search_overage_reader.py
infra/aws/lambda/investor-reporting/directory/tests/test_search_readers_overage.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~140/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-338.search-response-readers-pass-over-age-and-plain.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 55 (round 62, workstream ~P), cell `IB-pr-338`.
<owned_cells>IB-pr-338</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB62-3-AC1, IB62-G-140. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~140/IRPT_BCKEND.TO-IB-pr-338.search-response-readers-pass-over-age-and-plain.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB62-3-AC1,IB62-G-140` BEFORE the flip.
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

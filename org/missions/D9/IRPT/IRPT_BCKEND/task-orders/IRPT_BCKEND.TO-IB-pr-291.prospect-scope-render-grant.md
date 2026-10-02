# TO IRPT_BCKEND.TO-IB-pr-291 -- A prospect-scope render grant: a report with no accounts may render exactly its own artifacts, nothing account-scoped or firm-wide

<to_id>IRPT_BCKEND.TO-IB-pr-291</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~101</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-02</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>29</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO round-28 ~P analysis E1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_28_P_20261002.md`,
msg 104156); row IRPT_BCKEND-W101-S1 | **Decomp cell:** `IB-pr-291` (decomposition section 27) | **outcome_ref:** FWD-9 (hop 12,
the Analysis export) | **depends_on:** none

---

## WORKER FACE

**The cell.** Every retained Analysis report is PROSPECT-owned (no accounts: an analysis over an uploaded portfolio), and the shared
render grant (`infra/aws/lambda/investor-reporting/_render_identity/grant.py`, `build()`) requires non-empty `account_ids`, so no
Analysis export can be granted a render. Give the grant a PROSPECT scope, used only for a prospect-owned report, that names EXACTLY
that report's own retained artifacts and nothing else, and make the export's `render_grant()` build it.

**What exists (read first).**
- `_render_identity/grant.py` (`build(firm_id, bundle_id, revision, account_ids, pinned_ids, delegator_*)`) and its tests
  `_render_identity/tests/test_grant.py`; how a grant is consumed: `_render_identity/carriage.py`, `mint.py`.
- `export/retained_export.py` (merged @9079753aa7): `authorizer()` admits a prospect-owned report to its exact owner only (same
  principal, firm, advisor and home firm; `account_ids == []`; non-empty `prospect_input_id`), the rule
  `infra/aws/lambda/investor-reporting/_scope/retained_input_authorizer.py` applies to the prospect input; `render_grant()` today
  raises "a prospect-owned Analysis report has no accounts for a render grant to pin"; `analysis_pins()` pins the request id as
  `accountSetId`/`jobId` and the report id.
- A real prospect-owned READY report to read (reads only): `RPT-1f49504f501a6633b1f9cccc5f37ecf6`, request
  `REQ-e4b7f5aba7fb218c37f28002` (record `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~101/ANALYSIS_EXPORT_R28.json`).

**What you build.**
- In `grant.py`: a prospect scope. A grant for a report with no accounts carries the report id, its revision, the request id, its
  `prospect_input_id` and the keys of the report's own retained artifacts (the report, its sections, its composition, its retained
  vendor PDF) -- and NOTHING account-scoped (no account id, no account set) and nothing firm-wide (no wildcard, no firm prefix).
  `build()` REFUSES, by a named error, a prospect grant that names any account, any artifact of another owner, or any firm-wide
  scope. The account branch's behaviour does not change.
- In `export/retained_export.py`: `render_grant()` builds that prospect grant for a prospect-owned ANALYSIS report (the exact owner the
  authorizer admitted is the delegator) instead of refusing; PERFORMANCE and account-owned reports exactly as today.
- `_render_identity/tests/test_grant_prospect.py`: at least 5 tests naming both branches -- a prospect grant names exactly the
  report's artifacts; a prospect grant naming an account is refused; one naming another owner's artifact is refused; a firm-wide
  scope is refused; an account grant is unchanged.
- The caller census: every caller of `grant.build` / the render grant in the repository (`comp-find`, the denominator printed),
  written to `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~101/GRANT_CALLERS_R29.json` as
  `{"files_scanned": n, "callers": [{"path": "<repo-relative file>", "how": "<the call site, file:line>"}], "census_command": "<the command>"}`.
  For each caller say in one line why its grant is unchanged (it never passes an empty account list).

<criterion id="IB29-1-AC1" cell_refs="IB-pr-291"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r29/p29_1_ac1_prospect_grant_tests.py" .</invocation><expect>IB29-1-AC1 PASS</expect></criterion>
`IB29-1-AC1` -- the new test file names both branches and at least 5 tests pass with none failing. Base: FAIL (no file).

<criterion id="IB29-1-AC2" cell_refs="IB-pr-291"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r29/p29_1_ac2_grant_callers_unchanged.py" .</invocation><expect>IB29-1-AC2 PASS</expect></criterion>
`IB29-1-AC2` -- every caller is named with a positive scan denominator, and the existing grant, carriage and export suites pass
unchanged. Base: FAIL (no census).

<expected_criteria>IB29-1-AC1,IB29-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **AWS:** reads only. No write, no deploy, no artifact upload, no invoke.
- **Refusal clause.** A caller whose grant WOULD change is a row naming it, never a silent edit to that caller; a prospect render that
  needs an artifact outside the report's own is a row, never a wider scope.

<paths>
infra/aws/lambda/investor-reporting/_render_identity/grant.py
infra/aws/lambda/investor-reporting/_render_identity/tests/test_grant_prospect.py
infra/aws/lambda/investor-reporting/export/retained_export.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r29/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/` (all of it), `docs/contracts/investor-reporting/v1/`,
`portal/src/pages/InvestorReporting/render/`, `lib/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 27 (round 29, workstream ~P), cell `IB-pr-291`.
<owned_cells>IB-pr-291</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB29-1-AC1, IB29-1-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~101/IRPT_BCKEND.TO-IB-pr-291.prospect-scope-render-grant.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IB29-1-AC1,IB29-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hashes, each criterion's last line, the callers with one line each, and any surprise row id
(`IRPT_BCKEND-W101-S<k>`, k >= 4).

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one shared module (`_render_identity/grant.py`) used by every export render; the cell names every caller and proves each unchanged; 0 served bytes move in the cell.
comp-iam: DECLARED-NOT-APPLICABLE in the cell -- no role changes; the served move's packet reads what a prospect render may read.
comp-routes: DECLARED-NOT-APPLICABLE -- no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: a request-driven module change; no schedule, trigger or cron is created or moved.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB29-1-AC1 base FAIL (no test file), IB29-1-AC2 base FAIL (no census), dry-run at the base 2026-10-02 ~10:2xZ.
lane: the <paths> block IS the grant.
</preflight>

# TO IRPT_BCKEND.TO-IB-pr-357 -- _authz/served.py response_envelope drops internal_correlation_id from every status, as the refusal path already does (IRPT_YCDGEN-S16, the F1 stop)

<to_id>IRPT_BCKEND.TO-IB-pr-357</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~166</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>72</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 998 on 2.0.0_SA_COO~G2 msg 994; evidence ~G2 msg 1014, row IRPT_YCDGEN-S16 @29e0872ca3 | **Decomp cell:** `IB-pr-357`
(decomposition section 65) | **outcome_ref:** IRPT_YCDGEN F1 (Andrew's Overview run) and every success route using response_envelope | **depends_on:** none.

---

## WORKER FACE

**The stop (row IRPT_YCDGEN-S16).** A success response's status carries `internal_correlation_id`. The portal's closed public-status
set (`portal/src/contracts/public-status.ts` `requirePublicStatus`, then `envelope.ts:316-318`) rejects it, and F1 stops.

**Reproduce, local, no AWS:** from `infra/aws/lambda/investor-reporting/ycharts/generate`, import `entry` and call
`entry._entry.response_envelope(entry.OPERATION, 'f', {}, entry._entry.status_envelope(entry.OPERATION, 'NOT_READY', state='QUEUED',
operation_kind='write'))`. The status keys include `internal_correlation_id`.

**The model:** `infra/aws/lambda/investor-reporting/_authz/served.py` about `:416-423` already strips it on refusals.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-166`; run everything from its root):

1. **In `infra/aws/lambda/investor-reporting/_authz/served.py` only.** `response_envelope` drops `internal_correlation_id` from any status it emits, the same way
   the refusal path does. Nothing else in the envelope changes.
2. **`infra/aws/lambda/investor-reporting/_authz/tests/test_response_envelope_public_status.py` (new).**
   - **The pin:** the repro above yields no `internal_correlation_id`. It FAILS without your fix: run it once before the fix and say
     so.
   - **Unchanged:** a refusal envelope is unchanged.
   - **Allowed keys only:** every key a success status carries is in the portal's public-status set. Read that set from
     `portal/src/contracts/public-status.ts` as a fixture list in the test, and name the file.
3. **Run once, separately:** the new test, then `_authz/tests/test_unguarded_census.py` in its own pytest process.

Once this drains, the issuer counts every handler that imports `response_envelope` for the release pair. You do not deploy.

<criterion id="IB72-3-AC1" cell_refs="IB-pr-357"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r72/p72_cells.py" . IB72-3-AC1</invocation><expect>IB72-3-AC1 PASS</expect></criterion>
`IB72-3-AC1` -- the envelope test (the repro yields no internal_correlation_id; a refusal unchanged; success keys within the public set) passes, and the route census in its own process. Base: FAIL (no test).

<criterion id="IB72-G-166" cell_refs="IB-pr-357"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r72/p72_cells.py" . IB72-G-166</invocation><expect>IB72-G-166 PASS</expect></criterion>
`IB72-G-166` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB72-3-AC1,IB72-G-166</expected_criteria>

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
- **Refusal clause.** An edit outside served.py and the new test, a change to the refusal envelope, or a deploy is a defect: stop and file a row.

<paths>
infra/aws/lambda/investor-reporting/_authz/served.py
infra/aws/lambda/investor-reporting/_authz/tests/test_response_envelope_public_status.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~166/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-357.response-envelope-drops-internal-correlation-id.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 65 (round 72, workstream ~P), cell `IB-pr-357`.
<owned_cells>IB-pr-357</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB72-3-AC1, IB72-G-166. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~166/IRPT_BCKEND.TO-IB-pr-357.response-envelope-drops-internal-correlation-id.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB72-3-AC1,IB72-G-166` BEFORE the flip.
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
comp-adversary: RUN -- every criterion dry-run at base 0d2aff87b3 2026-10-07 ~19:2xZ: build checks FAIL, guards PASS (p72_cells.py).
lane: the <paths> block IS the grant.
</preflight>

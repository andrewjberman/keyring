# TO IRPT_BCKEND.TO-IB-pr-354 -- InteractiveAccess.current() carries allowedFirmIds for an OPAL_GLOBAL subject, so the on-behalf upload admit (IB-yr-631) is reachable; ALL never admits (TCKT_VNEXT X-1, row W152-S1)

<to_id>IRPT_BCKEND.TO-IB-pr-354</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~163</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>71</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 945 on 2.0.0_SA_COO~Y2 msg 942 (row W152-S1): ~P2 cuts ONE cell on _scope/interactive_access.py; Y's X-1 release waits on it and both ship under one pair | **Decomp cell:** `IB-pr-354`
(decomposition section 64) | **outcome_ref:** TCKT_VNEXT FWD-1 (the Analysis upload door, X-1) through IRPT_BCKEND intake | **depends_on:** IB-yr-631 (drained, a241bfa396).

---

## WORKER FACE

**The gap (row W152-S1).** `infra/aws/lambda/investor-reporting/intake/uploads.py` `_internal_for_allowed_firm` (IB-yr-631) admits an on-behalf upload only for
a principal with `principal_class == "OPAL_GLOBAL"`, `home_firm_id == "opal-capital"` and an `allowedFirmIds` that names the owner's
firm. That value may be a list or a comma string; an absent value or `ALL` never admits. In production, though, the principal comes from
`infra/aws/lambda/investor-reporting/_scope/interactive_access.py` `InteractiveAccess.current()`, whose OPAL_GLOBAL row is `{firm_id, principal_id, home_firm_id,
principal_class, advisor_id}` with no `allowedFirmIds`. And `authorize_current` refuses any principal that is not equal to `current()`.
So the admit can never fire with the real authority.

The field lives on the opal-users-v2 profile row. It is read today by:
- `infra/aws/lambda/investor-reporting/_scope/canonical_profile_reads.py` (`_USER_FIELDS`, about `:27`);
- `infra/aws/lambda/investor-reporting/ycharts/generate/current_authority.py` (`allowed_firm_ids()`, about `:67`).

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-163`; run everything from its root):

1. **In `infra/aws/lambda/investor-reporting/_scope/interactive_access.py` only.** For a verified internal (OPAL_GLOBAL) subject, `current()` carries
   `allowedFirmIds` read from that subject's profile row.
   - Reuse the EXISTING profile reader: inject it, or use the one `canonical_profile_reads` / `current_authority` already use. Do not
     open a new table client.
   - Normalize the value the way `uploads.py` reads it, and include it in the row before `ownership_fingerprint`, so `principal ==
     current()` holds for a principal built from `current()`.
   - An unreadable or absent profile value yields no field, which fails closed.
   - A non-internal (prospect) row is unchanged.
   - `authorize_current` admits on-behalf only where the `uploads.py` rule does, and is otherwise unchanged.
   - If the reader cannot be reached from `current()` without touching another file, that is a row and a stop on AC1, never an edit
     elsewhere.
2. **`infra/aws/lambda/investor-reporting/_scope/tests/test_interactive_access_on_behalf.py` (new).** It uses the existing `_scope/tests` fixtures and a fake profile
   reader, and drives the REAL `InteractiveAccess` with `intake/uploads.py`'s store `create`.
   - **Admitted:** an Opal filer whose `allowedFirmIds` names the owner's firm creates on its behalf, and the upload records the acting
     principal and the owner firm.
   - **Refused, each by name:**
     - (a) a firm not in the list;
     - (b) a non-internal principal;
     - (c) `allowedFirmIds == "ALL"` (and `["ALL"]`);
     - (d) a missing profile value.
3. **Run once from `infra/aws/lambda/investor-reporting`:** `python -m pytest -q _scope/tests/test_interactive_access_on_behalf.py _scope/tests/test_interactive_access.py
   intake/tests/test_uploads_on_behalf.py`, and report its last line. The two existing files (12 tests) must stay green.

Which person may file for which firms is an entitlement Andrew grants (CTO msg 945 (2)). Use test principals with explicitly listed
firms only, and never write a real profile row.

<criterion id="IB71-1-AC1" cell_refs="IB-pr-354"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r71/p71_cells.py" . IB71-1-AC1</invocation><expect>IB71-1-AC1 PASS</expect></criterion>
`IB71-1-AC1` -- the on-behalf test (admit with an explicit firm; refuse an unlisted firm, a non-internal principal, ALL and a missing value) passes with the existing interactive_access and on-behalf upload tests. Base: FAIL (no test).

<criterion id="IB71-G-163" cell_refs="IB-pr-354"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r71/p71_cells.py" . IB71-G-163</invocation><expect>IB71-G-163 PASS</expect></criterion>
`IB71-G-163` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB71-1-AC1,IB71-G-163</expected_criteria>

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
- **Refusal clause.** An edit outside interactive_access.py and the new test, a new table client, any admission of ALL, or a write to a real profile row (opal-users-v2) is a defect: stop and file a row.

<paths>
infra/aws/lambda/investor-reporting/_scope/interactive_access.py
infra/aws/lambda/investor-reporting/_scope/tests/test_interactive_access_on_behalf.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~163/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-354.interactive-access-carries-allowed-firm-ids.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 64 (round 71, workstream ~P), cell `IB-pr-354`.
<owned_cells>IB-pr-354</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB71-1-AC1, IB71-G-163. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~163/IRPT_BCKEND.TO-IB-pr-354.interactive-access-carries-allowed-firm-ids.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB71-1-AC1,IB71-G-163` BEFORE the flip.
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
comp-adversary: RUN -- every criterion dry-run at base 6115baf2e7 2026-10-07 ~18:2xZ: build checks FAIL, guards PASS (p71_cells.py).
lane: the <paths> block IS the grant.
</preflight>

# TO IRPT_BCKEND.TO-IB-pr-362 -- E1: the four ARMED rows (S334, W140-S1, W145-S2, W165-S2) disarmed, or re-justified with the one act that disarms each and its owner

<to_id>IRPT_BCKEND.TO-IB-pr-362</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~170</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>76</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 rounds 69-74 analysis @b35c7d8c73 (msg 1214), enrichment E1 | **Decomp cell:** `IB-pr-362`
(decomposition section 69) | **outcome_ref:** row hygiene for the round close (every FWD the rows touch) | **depends_on:** none.

---

## WORKER FACE

**What the CTO asks (E1).** Four rows in `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md` are still ARMED. For each,
run its disarm act and print the evidence, OR state it as still ARMED with the ONE act that disarms it and that act's owner. Read
each row's own JSON first; its `world_is` and `disarm_owner` say what disarms it.
- **S334:** safe-apply's comp-tagauthz gate hangs on `aws iam get-account-authorization-details`. It disarms only when the gate
  evaluates in bounded time, which is the gate owner's fix, not this lane's. Expected: still ARMED, owner named.
- **W140-S1:** four portal readers of the directory-search response threw EnvelopeMismatch on the over-age status.
  - IB-pr-341 (portal @5c726cf4, on DEV ba391aff8f) made the status public.
  - Check on portal DEV whether the readers now accept it: the ir-62-overage tests, `bun --no-install`, from a portal checkout of
    DEV.
  - Pass: DISARMED with that output. Otherwise: ARMED, with what is left.
- **W145-S2:** `receipt.build` refuses a receipt with no covered account. A retained export must carry its accounts from the
  retained pointer. IB-pr-343 amendment 1 (`finalize_on_read.py`, `handler.py`) shipped in the IB-pr-349 release; the live
  `irpt-export-render` equals pin b921635dad.
  - Show from the live bytes (`release-census.py irpt-export-render --pin b921635dad` reads `changed_members=0`) and the tests
    (`infra/aws/lambda/investor-reporting/export/tests/test_retained_finalize_names_accounts.py`) that a retained export names its accounts.
  - Pass: DISARMED. Otherwise: ARMED, with the gap.
- **W165-S2:** the full bun suite rewrites tracked `contracts/wire/*.ts`. IB-pr-359's fix is on portal branch
  `wk-IRPT_BCKEND-167-portal` @63b9382a, which is NOT on DEV yet. Expected: still ARMED; the disarm act is the DEV landing of
  63b9382a, owned by Andrew's word via 0.0.0_AB_MSTR~DELL2.

**For each DISARMED row:** append ONE resolving row (`disposition: DISMISSED_WITH_REASON`, a `dismissal_reason` naming the row it
resolves and the evidence).

**Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~170/IB76-1_armed_rows.json`:**
`{"rows": {"IRPT_BCKEND-S334": {...}, ...}, "armed_after": N}`
- a DISARMED row carries `{"state":"DISARMED","resolving_row":"<id>","evidence":"..."}`;
- an ARMED row carries `{"state":"ARMED","disarm_act":"...","owner":"<serial>"}`.

No AWS write, no deploy, no edit outside your paths.

<criterion id="IB76-1-AC1" cell_refs="IB-pr-362"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r76/p76_cells.py" . IB76-1-AC1</invocation><expect>IB76-1-AC1 PASS</expect></criterion>
`IB76-1-AC1` -- the armed-rows file rules all four rows (DISARMED with a resolving row present in the channel and evidence, or ARMED with disarm act and owner) and armed_after equals the ARMED count. Base: FAIL (no file).

<criterion id="IB76-G-170" cell_refs="IB-pr-362"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r76/p76_cells.py" . IB76-G-170</invocation><expect>IB76-G-170 PASS</expect></criterion>
`IB76-G-170` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB76-1-AC1,IB76-G-170</expected_criteria>

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
- **Refusal clause.** An AWS write, a deploy, a portal push, or editing an existing row (rows are append-only) is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~170/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-362.armed-rows-disarmed-or-rejustified.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 69 (round 76, workstream ~P), cell `IB-pr-362`.
<owned_cells>IB-pr-362</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB76-1-AC1, IB76-G-170. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~170/IRPT_BCKEND.TO-IB-pr-362.armed-rows-disarmed-or-rejustified.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB76-1-AC1,IB76-G-170` BEFORE the flip.
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
comp-adversary: RUN -- every criterion dry-run at base b7e16c7230 2026-10-07 ~05:5xZ 2026-10-08: build checks FAIL, guards PASS (p76_cells.py).
lane: the <paths> block IS the grant.
</preflight>

# TO IRPT_BCKEND.TO-IB-pr-361 -- regenerate ~P's portal wire types (ExportBundle, ExportReceipt, the route-derived responses/index) from their contracts -- row S388, ~P's share

<to_id>IRPT_BCKEND.TO-IB-pr-361</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~169</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>75</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** issuer ruling on row S388 after the owner split (1.0.0_SA_CTO~DELL2 msg 1173: a row with an owner, never a regenerate-as-rider; ~G2 msg 1188) | **Decomp cell:** `IB-pr-361`
(decomposition section 68) | **outcome_ref:** FWD-2 / FWD-8 (the portal reads the export receipt, bundle and custody route by the contract) | **depends_on:** none (the contracts are on CLOUD).

---

## WORKER FACE

**The drift (row S388, ~P's share).** One run of `portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-26.wire-regen.test.ts` on portal DEV
d1b21c97 rewrites the generated wire types. Four of the changed files are ~P's, because ~P changed their contracts and never
regenerated them:
- `portal/src/pages/InvestorReporting/contracts/wire/ExportBundle.ts` (+16/-1): IB-pr-336's `custody_report_ref`;
- `portal/src/pages/InvestorReporting/contracts/wire/ExportReceipt.ts` (+2/-1): IB-pr-343's `facts.covered_account_ids`;
- `portal/src/pages/InvestorReporting/contracts/wire/responses.ts` (+7/-23) and `portal/src/pages/InvestorReporting/contracts/wire/index.ts` (-8): derived from the route table, which gained IB-pr-355's custody route.

The other two drifting files are NOT yours: `AnalysisReport.ts` is IRPT_YCDGEN's and `HoldingsSnapshot.ts` is MDPF_SECCLASS's.

**What you build** (worktree `C:/dev/wk-irpt-bckend-169`, nested portal worktree `C:/dev/wk-irpt-bckend-169/portal` on portal DEV
d1b21c97, node_modules LINKED):

1. **Regenerate.** From `portal/`, run `bun --no-install test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-26.wire-regen.test.ts` once. It
   regenerates every wire file in place.
2. **Restore what is not yours:** `git checkout -- src/pages/InvestorReporting/contracts/wire/AnalysisReport.ts src/pages/InvestorReporting/contracts/wire/HoldingsSnapshot.ts`, plus any other file outside
   the four; line-ending-only rewrites restore the same way.
3. **Check the four:** `git diff --stat` shows content changes in exactly the four files. Read each diff and confirm it carries only
   what the contract states, with no hand edit.
4. **Typecheck:** `node node_modules/typescript/bin/tsc -b --noEmit` exits 0. A type error a consumer now hits is a row and a stop on
   AC2, never an edit to a consumer.
5. **Commit** the four files on the portal branch only. Never commit the workspace `portal` gitlink, and never push DEV.

**bun rules, VERBATIM (1.0.0_SA_CTO~DELL2 rules 106215/106221):** "run bun ONLY from inside C:\\dev\\ajb_workspace\\portal (or a
worktree with node_modules LINKED), always as `bun --no-install`; never run bun on a scratch file elsewhere" and "Never `bun install`.
Provision a worktree only with `wk-provision.sh --node-modules link` ... or `none`. ... no registry-reaching probe."

**AMENDMENT 1 (2026-10-08 ~06:2xZ, issuer `2.0.0_SA_COO~P2`, on row W169-S1).** The regenerated `ExportReceipt.ts` makes
`facts.covered_account_ids` required, as the contract has since IB-pr-343. One consumer fixture,
`portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-26.submit-data-optional.test.ts`, builds a receipt without it, so `tsc -b` fails (TS2741 at :33). That fixture is a consumer of ~P's own contract
change. Add `covered_account_ids` to that fixture's receipt (a non-empty list of opaque test account ids, consistent with the
fixture's other ids) and change nothing else in it; then IB75-1-AC2 is re-run. The refusal clause's "an edit to a consumer" no
longer covers this one file.

<criterion id="IB75-1-AC1" cell_refs="IB-pr-361"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r75/p75_cells.py" . IB75-1-AC1</invocation><expect>IB75-1-AC1 PASS</expect></criterion>
`IB75-1-AC1` -- after one regeneration ~P's four wire files are byte-unchanged (they equal the generator's output), and the branch changes no other contracts/wire file. Base: FAIL (all four drift).

<criterion id="IB75-1-AC2" cell_refs="IB-pr-361"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r75/p75_cells.py" . IB75-1-AC2</invocation><expect>IB75-1-AC2 PASS</expect></criterion>
`IB75-1-AC2` -- tsc -b --noEmit exits 0 on your portal branch. Base: PASS (a control).

<criterion id="IB75-G-169" cell_refs="IB-pr-361"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r75/p75_cells.py" . IB75-G-169</invocation><expect>IB75-G-169 PASS</expect></criterion>
`IB75-G-169` -- a GUARD: your workspace commits touch only your grant, never the portal gitlink. Base: PASS.

<expected_criteria>IB75-1-AC1,IB75-1-AC2,IB75-G-169</expected_criteria>

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
- **Refusal clause.** A committed change to AnalysisReport.ts, HoldingsSnapshot.ts or any wire file outside the four, a hand edit to a generated file, an edit to a consumer, a bun install or registry fetch, a workspace `portal` gitlink commit, or a DEV push is a defect: stop and file a row.

<paths>
portal/src/pages/InvestorReporting/contracts/wire/ExportBundle.ts
portal/src/pages/InvestorReporting/contracts/wire/ExportReceipt.ts
portal/src/pages/InvestorReporting/contracts/wire/responses.ts
portal/src/pages/InvestorReporting/contracts/wire/index.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-26.submit-data-optional.test.ts
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~169/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-361.regenerate-ps-wire-types-from-their-contracts.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 68 (round 75, workstream ~P), cell `IB-pr-361`.
<owned_cells>IB-pr-361</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB75-1-AC1, IB75-1-AC2, IB75-G-169. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~169/IRPT_BCKEND.TO-IB-pr-361.regenerate-ps-wire-types-from-their-contracts.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB75-1-AC1,IB75-1-AC2,IB75-G-169` BEFORE the flip.
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
comp-adversary: RUN -- every criterion dry-run at base 4022181507 2026-10-07 ~03:4xZ 2026-10-08: build checks FAIL, guards PASS (p75_cells.py).
lane: the <paths> block IS the grant.
</preflight>

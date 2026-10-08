# TO IRPT_BCKEND.TO-IB-pr-359 -- the wire-generator tests write to a temp dir, never tracked contracts/wire (W165-S2), and the custody read passes a named envelope validation before it mounts (W165-S1) -- CTO msg 1113's conditions on IB-pr-356

<to_id>IRPT_BCKEND.TO-IB-pr-359</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~167</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>73</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 review msg 1113: PASS for DEV on b3fedfea with (1) W165-S1 closed before PROD and (2) W165-S2 disarmed before the DEV push | **Decomp cell:** `IB-pr-359`
(decomposition section 66) | **outcome_ref:** FWD-8 / IRPT_CUSTDY hop 5 (the print page reaches DEV, then PROD) | **depends_on:** IB-pr-356 (portal b3fedfea is this cell's base).

---

## WORKER FACE

**Two conditions the CTO set on IB-pr-356 (msg 1113).** Your portal branch starts on b3fedfea, IB-pr-356's commit.

**(1) W165-S2 (ARMED): the generator tests rewrite tracked files.**
- `portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts` writes generated wire types into the tracked `portal/src/pages/InvestorReporting/contracts/wire/`. Four tests drive it:
  `portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-17.gen-oneof.test.ts`, `iv-e-17.regenerated.test.ts`, `iv-e-26.wire-regen.test.ts` and
  `portal/src/pages/InvestorReporting/__tests__/fe-s-25/generator.test.ts`.
- Measured at b3fedfea: one run rewrote **25** tracked files, 4 of them with content changes (the AnalysisReport v2 types drop out),
  and `IVE26-AC3` (idempotent regeneration, content pin 17 of 17) fails.
- **Make the generator write to a temp directory** (`os.tmpdir()` per run, or an out-dir argument `gen-wire.ts` already takes; read
  it) in every test that runs it. A test that compares generated output with the committed files reads the committed files and
  writes nothing tracked.
- **Do not edit any `contracts/wire/*.ts` and do not fix the drift.** If generated output still differs from the committed files,
  name the differing files and the failing test in a row, as an observation.

**(2) W165-S1: the custody read is not validated.**
- `getCustodyReport` in `portal/src/api/endpoints/investor-reporting.ts` reads the body outside `parseIrEnvelope`
  (`portal/src/pages/InvestorReporting/contracts/envelope.ts`). An unvalidated body could mount.
- **Route the custody read through `parseIrEnvelope`** with a data adapter for `custody-report-read` in `portal/src/pages/InvestorReporting/contracts/envelope.ts`,
  shaped like the analysis read's. Or, if the envelope cannot carry it without touching other operations, add ONE named validation
  `validateCustodyReport` that checks `report_kind == "CUSTODY_REPORT"`, `report_id`, `revision` and a document object, and refuses
  anything else by name.
- **Update `portal/src/pages/InvestorReporting/__tests__/ir-72-custody-print/custody-print.test.tsx`:** a body failing that validation shows the page's refusal and mounts no
  document. The test names `parseIrEnvelope` or `validateCustodyReport`.

**From `portal/`:**
- run the four generator tests, then `git status --porcelain src/pages/InvestorReporting/contracts/wire` (it must be empty);
- `bun --no-install test src/pages/InvestorReporting/__tests__/ir-72-custody-print/`;
- `node node_modules/typescript/bin/tsc -b --noEmit`.

**Commit on the portal worktree branch only.** Never commit the workspace `portal` gitlink, and never push DEV.

**bun rules, VERBATIM (1.0.0_SA_CTO~DELL2 rules 106215/106221):** "run bun ONLY from inside C:\\dev\\ajb_workspace\\portal (or a
worktree with node_modules LINKED), always as `bun --no-install`; never run bun on a scratch file elsewhere" and "Never `bun install`.
Provision a worktree only with `wk-provision.sh --node-modules link` ... or `none`. ... no registry-reaching probe."

<criterion id="IB73-1-AC1" cell_refs="IB-pr-359"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r73/p73_cells.py" . IB73-1-AC1</invocation><expect>IB73-1-AC1 PASS</expect></criterion>
`IB73-1-AC1` -- after the four generator tests, git status on portal contracts/wire is empty (no tracked file written); the test outcome is reported. Base: FAIL (25 rewritten).

<criterion id="IB73-1-AC2" cell_refs="IB-pr-359"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r73/p73_cells.py" . IB73-1-AC2</invocation><expect>IB73-1-AC2 PASS</expect></criterion>
`IB73-1-AC2` -- the custody read calls parseIrEnvelope or validateCustodyReport, and the ir-72 test (naming it; an invalid body is refused, no document mounted) passes. Base: FAIL.

<criterion id="IB73-G-167" cell_refs="IB-pr-359"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r73/p73_cells.py" . IB73-G-167</invocation><expect>IB73-G-167 PASS</expect></criterion>
`IB73-G-167` -- a GUARD: your workspace commits touch only your grant, never the portal gitlink. Base: PASS.

<expected_criteria>IB73-1-AC1,IB73-1-AC2,IB73-G-167</expected_criteria>

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
- **Refusal clause.** An edit to any contracts/wire/*.ts, a bun install or registry fetch, an edit outside your paths, a workspace `portal` gitlink commit, or a DEV push is a defect: stop and file a row.

<paths>
portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-17.gen-oneof.test.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-17.regenerated.test.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-26.wire-regen.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-25/generator.test.ts
portal/src/pages/InvestorReporting/contracts/envelope.ts
portal/src/api/endpoints/investor-reporting.ts
portal/src/pages/InvestorReporting/__tests__/ir-72-custody-print/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~167/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-359.wire-generator-tests-write-to-temp-and-custody-read-is-validated.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 66 (round 73, workstream ~P), cell `IB-pr-359`.
<owned_cells>IB-pr-359</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB73-1-AC1, IB73-1-AC2, IB73-G-167. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~167/IRPT_BCKEND.TO-IB-pr-359.wire-generator-tests-write-to-temp-and-custody-read-is-validated.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB73-1-AC1,IB73-1-AC2,IB73-G-167` BEFORE the flip.
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
comp-adversary: RUN -- every criterion dry-run at base 72208311d5 2026-10-07 ~22:0xZ: build checks FAIL, guards PASS (p73_cells.py).
lane: the <paths> block IS the grant.
</preflight>

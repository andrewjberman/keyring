# TO IRPT_BCKEND.TO-IB-pr-346 -- the print page refuses a report kind it does not know, and the custody-report candidate passes typecheck, eslint and a 0-request refusal test (CTO review msg 403)

<to_id>IRPT_BCKEND.TO-IB-pr-346</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~147</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>66</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 review msg 403 of PrintEntry.tsx @cdda4378 (LAND-WITH-NOTE: conditions (1) typecheck + eslint + one refusal test, (2) readReportKind refuses an unknown kind next round); portal toolchain live on dell2 (msg 472); row S365 | **Decomp cell:** `IB-pr-346`
(decomposition section 59) | **outcome_ref:** FWD-8 / FWD-4 export integrity (the page half of the template refusal); IRPT_CUSTDY hop 5 | **depends_on:** IB-pr-336 (drained; its portal half is the base).

---

## WORKER FACE

**The candidate.** IB-pr-336's portal half, branch `wk-IRPT_BCKEND-138-portal` @cdda4378 (1 file, `PrintEntry.tsx`, +15/-1), names the
`custody-report` kind in the print entry and refuses it by name before any request, until IRPT_CUSTDY's template lands. The CTO reviewed it
LAND-WITH-NOTE (msg 403): before DEV it needs typecheck + eslint passing and ONE test that `?kind=custody-report` yields the refusal and
makes 0 requests. The CTO's note (2): `readReportKind` (`PrintEntry.tsx` about :109) still maps ANY unknown kind to 'performance' on the
page side (`return value === 'analysis' ? 'analysis' : 'performance'`); it must refuse an unknown kind, as the render host now does
(`infra/aws/ec2/investor-reporting-export/render_export.cjs` `kindForTemplate`, IB-pr-336).

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-147`, with a nested portal worktree at `C:/dev/wk-irpt-bckend-147/portal` on the
portal branch carrying @cdda4378; `portal/node_modules` is LINKED from the shared tree's pack -- never `npm`/`bun install`, which is egress):

1. In `portal/src/pages/InvestorReporting/render/PrintEntry.tsx` only: `readReportKind` maps `performance`, `analysis` and `custody-report`
   to their kinds and REFUSES any other value (a missing `?kind=` keeps today's default, `performance`, unless the page already treats a
   missing kind as an error -- read it and say which); the refusal uses the page's existing 'refused' phase (about :96) and makes no request.
2. Test `portal/src/pages/InvestorReporting/__tests__/ir-66-print-kind/print-kind.test.ts` (new; bun, like the sibling tests under
   `__tests__/`): `?kind=custody-report` yields the refusal with 0 requests (count the fetches the page makes); an unknown kind (e.g.
   `?kind=client-report`) is refused with 0 requests; `performance` and `analysis` still render their kind. Run
   `bun --no-install test src/pages/InvestorReporting/__tests__/ir-66-print-kind/print-kind.test.ts` from `portal/`.
3. From `portal/`: `node node_modules/typescript/bin/tsc -b --noEmit` exits 0 and
   `node node_modules/eslint/bin/eslint.js src/pages/InvestorReporting/render/PrintEntry.tsx` exits 0. bun here is 1.4.2 and the pack was
   built with 1.3.9: note it if anything differs.
4. Commit on the portal worktree branch only; the issuer lands it on portal DEV. Never commit the workspace `portal` gitlink.

<criterion id="IB66-1-AC1" cell_refs="IB-pr-346"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r66/p66_cells.py" . IB66-1-AC1</invocation><expect>IB66-1-AC1 PASS</expect></criterion>
`IB66-1-AC1` -- the print-kind test passes with bun: custody-report and an unknown kind are refused with 0 requests; performance and analysis render. Base: FAIL (no test).

<criterion id="IB66-1-AC2" cell_refs="IB-pr-346"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r66/p66_cells.py" . IB66-1-AC2</invocation><expect>IB66-1-AC2 PASS</expect></criterion>
`IB66-1-AC2` -- typecheck (tsc -b --noEmit) and eslint on PrintEntry.tsx exit 0 on your portal branch. Base: PASS (a control; it must stay so).

<criterion id="IB66-G-147" cell_refs="IB-pr-346"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r66/p66_cells.py" . IB66-G-147</invocation><expect>IB66-G-147 PASS</expect></criterion>
`IB66-G-147` -- a GUARD: your workspace commits touch only your grant, and never the portal gitlink. Base: PASS.

<expected_criteria>IB66-1-AC1,IB66-1-AC2,IB66-G-147</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure. No build upload, no apply, no AWS write.
- **Firm buckets deny this box's identity** (row S347). If you need a firm-bucket read, file a row and stop on that criterion.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** An npm/bun install, an edit to any other portal file, a workspace `portal` gitlink commit, or a DEV push is a defect: stop and file a row.

<paths>
portal/src/pages/InvestorReporting/render/PrintEntry.tsx
portal/src/pages/InvestorReporting/__tests__/ir-66-print-kind/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~147/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-346.print-page-refuses-an-unknown-kind.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 59 (round 66, workstream ~P), cell `IB-pr-346`.
<owned_cells>IB-pr-346</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB66-1-AC1, IB66-1-AC2, IB66-G-147. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~147/IRPT_BCKEND.TO-IB-pr-346.print-page-refuses-an-unknown-kind.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB66-1-AC1,IB66-1-AC2,IB66-G-147` BEFORE the flip.
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
comp-adversary: RUN -- every criterion dry-run at base fd0c709235 2026-10-07 ~12:2xZ: AC1 FAIL, AC2 control PASS, guard PASS (p66_cells.py).
lane: the <paths> block IS the grant.
</preflight>

## AMENDMENT 1 (2026-10-07 ~12:2xZ, issuer 2.0.0_SA_COO~P2, before the spawn): the bun egress hazard (1.0.0_SA_CTO~DELL2 msg 501)

HAZARD ARMED (relayed verbatim per the CTO's order): "`bun run` / `bun test` on a file whose imports do not resolve fetches from npm
silently. A user-global bunfig `auto = "disable"` does NOT stop it, and no disarm is proven yet. Until MSTR's disarm lands: run bun ONLY
from inside C:\devjb_workspace\portal (or a worktree with node_modules LINKED), always as `bun --no-install`; never run bun on a scratch
file elsewhere." In this order: every bun invocation is `bun --no-install ...`, run from your linked portal worktree only. The check
p66_cells.py AC1 runs `bun --no-install test`. If anything fetches, stop and file a row.


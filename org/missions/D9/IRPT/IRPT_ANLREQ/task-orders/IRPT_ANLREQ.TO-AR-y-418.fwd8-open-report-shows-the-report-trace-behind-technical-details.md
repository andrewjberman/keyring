# TO IRPT_ANLREQ.TO-AR-y-418.fwd8-open-report-shows-the-report-trace-behind-technical-details -- FWD-8 / O6: the ticket's "Open report" shows the report (the sections that carry a value, the report-level validation once, the disclosures) and puts the element trace behind a closed "Technical details" for an Opal operator; the Analysis tab's manual path is unchanged

<to_id>IRPT_ANLREQ.TO-AR-y-418.fwd8-open-report-shows-the-report-trace-behind-technical-details</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~312</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ78</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-418` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-8 ("Open report" shows the report), O6 | **depends_on:** PRD v0.24; AR-y-404 and AR-y-408 (merged; r34l live 2026-10-19 21:39Z); portal base origin/DEV 4f9f2f633dc0

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~312`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-312` (branch `wk-IRPT_ANLREQ-312`), with a portal worktree `C:/dev/wk-irpt-anlreq-312/portal` (branch `wk-IRPT_ANLREQ-312-portal`) provisioned by the issuer AT `origin/DEV` (4f9f2f633dc0). Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~312 <0.9.0_WK_IRPT_ANLREQ~312@opal.agent>" -F <msgfile> -- <paths>` (a commit can take up to 400 s: wait and check `git log` before retrying). The PORTAL source is committed INSIDE the portal worktree, which has no committer identity: run `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~312" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~312@opal.agent" git -C C:/dev/wk-irpt-anlreq-312/portal commit --author "0.9.0_WK_IRPT_ANLREQ~312 <0.9.0_WK_IRPT_ANLREQ~312@opal.agent>" -F <msgfile>` (write no git config).
- Write every message file with the Write tool. APPEND rows only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, and COMMIT them. `surfaced_at` of any row = `date -u +%FT%TZ`; a row id has the form `IRPT_ANLREQ-D2-W312-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~300/` (the AR-y-410 instance; read it first; `git show HEAD:<path>` if absent), `to_id` exactly the order's id, a `controls.mutant` that FIRES and a `controls.determinism` really run. No live call, NO PUSH of any branch, no deploy. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`, and flip `<status>` to `complete` (commit alone) only on VALID. Scratch outside the product tree. Run the portal tests from `C:/dev/wk-irpt-anlreq-312/portal` with `bun test <path>` (node_modules is linked); the worktree is SPARSE: run ONLY the new test file and the folders the criteria name.

### THE CELL (`AR-y-418`, inlined)

*Context.* Portal at `origin/DEV` (4f9f2f633dc0). The ticket's "Open report" reads `GET /api/scoped/investor-reporting/analysis/{requestId}/sections` and renders it with `src/pages/InvestorReporting/tabs/analysis/NativeSections.tsx` (the file is SHARED with the Analysis tab's manual path, FWD-6): `NativeSections({ report })` prints the heading `Report sections` (Opal form), one report-level `Computation validation` line, then a `SectionBlock` CARD for every section in ordinal order (each card with its own SUPPORTED/UNSUPPORTED badge, which is the REPORT's validation repeated, a `Method: ... -- Coverage: ...` line and a `Not available: <reason>` line for an unavailable section), then the report's disclosures. For one measured request that is 427 cards, 3 with values (CRO gap G6, brief O6); with r34l the builder-only and not-in-this-version sections are no longer produced for new reports, but the ~144 `NOT_AVAILABLE` vendor-sourced elements remain as cards. Read `src/pages/TicketCenter/__tests__/open-report.test.tsx` and the Ticket Center code that mounts the report (`grep` for `NativeSections` under `src/pages/TicketCenter/` and for `readTicketReport`) to find the ticket's entry.

*The change.*
1. `NativeSections` gains an optional prop `mode?: 'trace' | 'report'` (default `'trace'`: EXACTLY today's rendering, byte for byte, so the Analysis tab and every existing consumer are unchanged) and an optional `operator?: boolean` (default false).
2. In `'report'` mode: the heading reads `Report`; the report-level validation prints ONCE as today (no per-section SUPPORTED/UNSUPPORTED badge and no Method/Coverage line on a value card); the cards are ONLY the sections whose `status` is `VALUE` (an Opal section with a value), in ordinal order, each as a table of its values with unit, currency and as-of, as `SectionBlock` prints them minus the badge and the method line; then the disclosures, printed once each in report order (the `NOT_SHOWN` line included). A report with no VALUE section prints one sentence: `This report holds no figures yet.`
3. In `'report'` mode a `<details data-slot="technical-details">` element, CLOSED by default, renders ONLY when `operator` is true. Its summary reads `Technical details`; it holds (a) one line per distinct reason of the unavailable sections with its count (`Not available: <reason>: <n>`) and (b) the full trace exactly as `'trace'` mode prints it, collapsed inside it. A non-operator never sees it and never receives the unavailable cards.
4. You change NO file under `src/pages/TicketCenter/` (another order edits that folder at the same time): the one-line hookup at the ticket's entry (it passes `mode="report"` and `operator={internal}`, the Opal staff flag the Ticket Center already holds) is the ISSUER's, added at the merge. Your report names the file and line where the ticket mounts `NativeSections` (found by reading `src/pages/TicketCenter/`, read-only) so the hookup can be added.

*The new test file `src/pages/InvestorReporting/__tests__/fwd8/native-sections-report-mode.test.tsx` (EXACTLY five tests), rendering `NativeSections` directly.* Build the report with the fixture style of `src/pages/InvestorReporting/__tests__/fe-s-6/sections.test.ts` and `src/pages/TicketCenter/__tests__/open-report.test.tsx` (read-only): (1) in `mode="report"`, 3 VALUE sections and 144 `NOT_AVAILABLE` sections show 3 section blocks and zero `Not available` text outside technical details; (2) for an operator the `technical-details` element exists, is closed by default and its text carries the reason line with count 144; (3) for a non-operator it does not exist; (4) `NativeSections` WITHOUT the new props (the Analysis tab's manual path) renders all 147 section blocks exactly as before (a regression test on the default); (5) in `mode="report"` the disclosures print once each in order and a `NOT_SHOWN` disclosure, when present, is the last one.

*What to do.* (1) Read the files; baseline the five NativeSections test files the criterion AR418-y-AC2 names (25 pass at the base) and print the counts; the rest of `src/pages/InvestorReporting` has 17 known failures at the base that are NOT yours. (2) Make the change; write the five tests; run the new file (` 5 pass`, ` 0 fail`) and the criterion AR418-y-AC2's command (` 0 fail`); print them. `controls.mutant` = the new file run with the `mode` default flipped to `'report'` (test 4 must FAIL). (3) Write `check_fwd8_bound.py` (below), commit portal and workspace files, then the proof instance.

You also write `check_fwd8_bound.py` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~312/` (ruff clean, stdlib only): it takes the portal worktree's `merge-base HEAD origin/DEV` (resolve the portal path from `git rev-parse --show-toplevel` of the workspace plus `portal`), lists the changed files, and prints `FWD8-BOUND-OK files=2` only when the changed paths are exactly `src/pages/InvestorReporting/tabs/analysis/NativeSections.tsx` and `src/pages/InvestorReporting/__tests__/fwd8/native-sections-report-mode.test.tsx`; otherwise `FWD8-BOUND-BAD <paths>` and a non-zero exit.

---

## ACCEPTANCE

<criterion id="AR418-y-AC1" cell_refs="AR-y-418"><invocation>cd portal && bun test src/pages/InvestorReporting/__tests__/fwd8/native-sections-report-mode.test.tsx</invocation><expect> 5 pass</expect></criterion>
<criterion id="AR418-y-AC2" cell_refs="AR-y-418"><invocation>cd portal && bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-116.vendor-card-title-once.test.tsx src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-122.vendor-validation-and-source.test.tsx src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-124.unsupported-card-reason.test.tsx src/pages/InvestorReporting/__tests__/fe-s-6/sections.test.ts src/pages/InvestorReporting/__tests__/mvp-selection/coverage.test.ts</invocation><expect> 0 fail</expect></criterion>
<criterion id="AR418-y-AC3" cell_refs="AR-y-418"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~312/check_fwd8_bound.py</invocation><expect>^FWD8-BOUND-OK files=2$</expect></criterion>



<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~312/IRPT_ANLREQ.TO-AR-y-418.fwd8-open-report-shows-the-report-trace-behind-technical-details.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-418.fwd8-open-report-shows-the-report-trace-behind-technical-details`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR418-y-AC1,AR418-y-AC2,AR418-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-418</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
portal/src/pages/InvestorReporting/tabs/analysis/NativeSections.tsx
portal/src/pages/InvestorReporting/__tests__/fwd8/native-sections-report-mode.test.tsx
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~312/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-418.fwd8-open-report-shows-the-report-trace-behind-technical-details.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one shared render component (new optional props whose default keeps the present output) and its test; the Ticket Center hookup belongs to the issuer at the merge; a candidate branch, nothing landed or pushed.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading NativeSections.tsx, `open-report.test.tsx` and the CRO gap G6 against this cell; the lens: the Analysis tab regressing (test 4 and the InvestorReporting folder run), the unavailable cards still shown by default, an operator-only panel shown to a partner (test 3), a disclosure dropped (test 5). NOT seen (blind): a real 427-element report in a browser; denominator: three criteria.
</preflight>

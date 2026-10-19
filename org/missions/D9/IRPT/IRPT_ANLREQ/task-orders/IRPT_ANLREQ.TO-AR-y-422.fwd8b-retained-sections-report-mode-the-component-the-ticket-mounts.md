# TO IRPT_ANLREQ.TO-AR-y-422.fwd8b-retained-sections-report-mode-the-component-the-ticket-mounts -- FWD-8 / O6, second half: RetainedSections (the component the ticket actually mounts for "Open report") gains the same report mode as NativeSections: only the sections that carry a value as cards, the element trace behind the closed Technical details for an operator

<to_id>IRPT_ANLREQ.TO-AR-y-422.fwd8b-retained-sections-report-mode-the-component-the-ticket-mounts</to_id>
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
<workstream>ZZ82</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-422` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-8 ("Open report" shows the report), O6 | **depends_on:** AR-y-418 (YOUR own order: its NativeSections report face is in your branch); portal base origin/DEV 4f9f2f633dc0

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~312`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-312` (branch `wk-IRPT_ANLREQ-312`), with a portal worktree `C:/dev/wk-irpt-anlreq-312/portal` (branch `wk-IRPT_ANLREQ-312-portal`) provisioned by the issuer AT `origin/DEV` (4f9f2f633dc0). Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~312 <0.9.0_WK_IRPT_ANLREQ~312@opal.agent>" -F <msgfile> -- <paths>` (a commit can take up to 400 s: wait and check `git log` before retrying). The PORTAL source is committed INSIDE the portal worktree, which has no committer identity: run `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~312" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~312@opal.agent" git -C C:/dev/wk-irpt-anlreq-312/portal commit --author "0.9.0_WK_IRPT_ANLREQ~312 <0.9.0_WK_IRPT_ANLREQ~312@opal.agent>" -F <msgfile>` (write no git config).
- Write every message file with the Write tool. APPEND rows only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, and COMMIT them. `surfaced_at` of any row = `date -u +%FT%TZ`; a row id has the form `IRPT_ANLREQ-D2-W312-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~300/` (the AR-y-410 instance; read it first; `git show HEAD:<path>` if absent), `to_id` exactly the order's id, a `controls.mutant` that FIRES and a `controls.determinism` really run. No live call, NO PUSH of any branch, no deploy. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`, and flip `<status>` to `complete` (commit alone) only on VALID. Scratch outside the product tree. Run the portal tests from `C:/dev/wk-irpt-anlreq-312/portal` with `bun test <path>` (node_modules is linked); the worktree is SPARSE: run ONLY the new test file and the folders the criteria name.

### THE CELL (`AR-y-422`, inlined)

*Context.* Your report on AR-y-418 (row W312-S1) is right: the Ticket Center mounts `RetainedSections` (`src/pages/InvestorReporting/tabs/analysis/OwnedRequestHistory.tsx`, line 151; mounted at `src/pages/TicketCenter/TicketCenter.tsx:211` inside `OpenedReportPanel` and at `src/pages/TicketCenter/AnalysisRequestParts.tsx:540` for the package's Report file), and the Analysis tab's history dialog mounts the SAME component (`OwnedRequestHistory.tsx:418`). `RetainedSections({ report })` prints `Report sections`, (for a vendor report) the validation and source lines, ONE closed `Technical details` (the computation or extraction validation), and then a `SectionBlock` for EVERY section in ordinal order: for one measured request 427 cards of which 3 carry values. You already built the report face for `NativeSections` (your branch, portal commit c34d3ea5); this order gives `RetainedSections` the same face.

*The change.*
1. `RetainedSections` gains optional props `mode?: 'trace' | 'report'` (default `'trace'`: EXACTLY today's rendering, byte for byte, so the Analysis tab's history dialog and every other caller are unchanged) and `operator?: boolean` (default false). Reuse your AR-y-418 report-face pieces (the bare `SectionBlock` flag and any helper): export a shared helper from `NativeSections.tsx` if that avoids copying; do not duplicate logic.
2. In `'report'` mode: the heading reads `Report`; the vendor validation and source lines stay exactly as today (they sit outside the Technical details); the cards are ONLY the sections whose status is `VALUE` (a vendor section carries no status: it is a figure card, as in your NativeSections rule), in ordinal order, each as the bare table (no SUPPORTED badge, no `Method/Coverage` line); an unavailable Opal section is never a card. A report with no figure prints `This report holds no figures yet.`.
3. The EXISTING closed `Technical details` stays (the validation inside it unchanged) and, in `'report'` mode ONLY when `operator` is true, ALSO holds (a) one line per distinct reason of the unavailable sections with its count (`Not available: <reason>: <n>`) and (b) the full trace, collapsed, exactly as `'trace'` mode prints the cards. A non-operator's Technical details holds only what it holds today.
4. Disclosures: if the `AnalysisReportSliceView` type carries the report's disclosures, print them once each in report order after the cards in `'report'` mode, a `NOT_SHOWN` disclosure last; if the slice does not carry them, print none and say so in your report (do not widen the slice type).
5. You change NO file under `src/pages/TicketCenter/` (the issuer adds the two mount hookups, `mode="report"` and `operator={internal}`, at the merge).

*The new test file `src/pages/InvestorReporting/__tests__/fwd8/retained-sections-report-mode.test.tsx` (EXACTLY five tests), rendering `RetainedSections` directly with the fixture style of `src/pages/TicketCenter/__tests__/open-report.test.tsx` and `iv-e-101.opal-report-words.test.tsx` (read-only):* (1) in report mode, 3 VALUE and 144 `NOT_AVAILABLE` sections show 3 section blocks and no `Not available` text outside Technical details; (2) for an operator the Technical details holds the reason line with count 144 and stays closed by default; (3) for a non-operator it holds neither the reason lines nor the trace; (4) WITHOUT the new props (the Analysis tab's dialog) every section is still rendered as before (147 blocks); (5) a report with no VALUE section prints the one sentence.

*What to do.* (1) Baseline the criterion AR422-y-AC2's command and print the counts. (2) Make the change; write the five tests; run the new file (` 5 pass`, ` 0 fail`) and AC2's command (` 0 fail`). `controls.mutant` = the new file with the `mode` default flipped to `'report'` (test 4 must FAIL). (3) Write `check_fwd8b_bound.py` (below), commit portal and workspace files, then the proof instance and flip on VALID.

You also write `check_fwd8b_bound.py` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~312/` (ruff clean, stdlib only): it takes the portal worktree's `merge-base HEAD origin/DEV` (resolve the portal path from `git rev-parse --show-toplevel` of the workspace plus `portal`), lists the files changed SINCE the branch point of THIS order's first portal commit (your AR-y-418 commit c34d3ea5 is the earlier base: use `git log` to find the portal commits after it), and prints `FWD8B-BOUND-OK files=<n>` only when those changed paths are within `src/pages/InvestorReporting/tabs/analysis/OwnedRequestHistory.tsx`, `src/pages/InvestorReporting/tabs/analysis/NativeSections.tsx` and the new test file (n 2 or 3); otherwise `FWD8B-BOUND-BAD <paths>` and a non-zero exit.

---

## ACCEPTANCE

<criterion id="AR422-y-AC1" cell_refs="AR-y-422"><invocation>cd portal && bun test src/pages/InvestorReporting/__tests__/fwd8/retained-sections-report-mode.test.tsx</invocation><expect> 5 pass</expect></criterion>
<criterion id="AR422-y-AC2" cell_refs="AR-y-422"><invocation>cd portal && bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-101.opal-report-words.test.tsx src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-106.request-list-order.test.tsx src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-115.vendor-section-names-units.test.tsx src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-116.vendor-card-title-once.test.tsx src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-118.no-unmapped-code-title.test.tsx src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-122.vendor-validation-and-source.test.tsx src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-124.unsupported-card-reason.test.tsx src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-99.readable-requests.test.ts src/pages/InvestorReporting/__tests__/fe-s-6/sections.test.ts src/pages/InvestorReporting/__tests__/fwd8/native-sections-report-mode.test.tsx src/pages/TicketCenter/__tests__/open-report.test.tsx src/pages/TicketCenter/__tests__/package-report-reader.test.tsx</invocation><expect> 0 fail</expect></criterion>
<criterion id="AR422-y-AC3" cell_refs="AR-y-422"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~312/check_fwd8b_bound.py</invocation><expect>^FWD8B-BOUND-OK files=[23]$</expect></criterion>



<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~312/IRPT_ANLREQ.TO-AR-y-422.fwd8b-retained-sections-report-mode-the-component-the-ticket-mounts.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-422.fwd8b-retained-sections-report-mode-the-component-the-ticket-mounts`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR422-y-AC1,AR422-y-AC2,AR422-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-422</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
portal/src/pages/InvestorReporting/tabs/analysis/OwnedRequestHistory.tsx
portal/src/pages/InvestorReporting/tabs/analysis/NativeSections.tsx
portal/src/pages/InvestorReporting/__tests__/fwd8/retained-sections-report-mode.test.tsx
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~312/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-422.fwd8b-retained-sections-report-mode-the-component-the-ticket-mounts.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one shared render component (optional props whose default keeps the present output), a shared helper in a second component and one test file; the two Ticket Center mount hookups belong to the issuer at the merge; a candidate branch, nothing landed or pushed.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading RetainedSections, the worker's AR-y-418 report (row W312-S1) and the CRO gap G6 against this cell; the lens: the Analysis tab dialog regressing (test 4 and the AC2 run over eight existing RetainedSections tests), unavailable cards still shown by default, an operator-only panel shown to a non-operator (test 3), a duplicated copy of the NativeSections logic. NOT seen (blind): a real 427-element report in a browser; denominator: three criteria.
</preflight>

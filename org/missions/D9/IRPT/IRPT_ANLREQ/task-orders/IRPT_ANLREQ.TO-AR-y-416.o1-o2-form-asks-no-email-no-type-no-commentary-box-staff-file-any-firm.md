# TO IRPT_ANLREQ.TO-AR-y-416.o1-o2-form-asks-no-email-no-type-no-commentary-box-staff-file-any-firm -- O1 portal half and O2: the Analysis Request form has no advisor login email field, no report-type dropdown and no Add-commentary checkbox; the variant is derived from the count of comparables, commentary is always requested, and an Opal staff filer may choose any firm the Global context lists

<to_id>IRPT_ANLREQ.TO-AR-y-416.o1-o2-form-asks-no-email-no-type-no-commentary-box-staff-file-any-firm</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~310</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ76</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-416` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1, FWD-2 (the form offers only what the system cannot infer), C-FIRM | **depends_on:** PRD v0.24; AR-y-415 (the backend half ships in the SAME release); portal base origin/DEV 4f9f2f633dc0

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~310`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-310` (branch `wk-IRPT_ANLREQ-310`), with a portal worktree `C:/dev/wk-irpt-anlreq-310/portal` (branch `wk-IRPT_ANLREQ-310-portal`) provisioned by the issuer AT `origin/DEV` (4f9f2f633dc0). Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~310 <0.9.0_WK_IRPT_ANLREQ~310@opal.agent>" -F <msgfile> -- <paths>` (a commit can take up to 400 s: wait and check `git log` before retrying). The PORTAL source is committed INSIDE the portal worktree, which has no committer identity: run `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~310" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~310@opal.agent" git -C C:/dev/wk-irpt-anlreq-310/portal commit --author "0.9.0_WK_IRPT_ANLREQ~310 <0.9.0_WK_IRPT_ANLREQ~310@opal.agent>" -F <msgfile>` (write no git config).
- Write every message file with the Write tool. APPEND rows only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, and COMMIT them. `surfaced_at` of any row = `date -u +%FT%TZ`; a row id has the form `IRPT_ANLREQ-D2-W310-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~300/` (the AR-y-410 instance; read it first; `git show HEAD:<path>` if absent), `to_id` exactly the order's id, a `controls.mutant` that FIRES and a `controls.determinism` really run. No live call, NO PUSH of any branch, no deploy. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`, and flip `<status>` to `complete` (commit alone) only on VALID. Scratch outside the product tree. Run the portal tests from `C:/dev/wk-irpt-anlreq-310/portal` with `bun test <path>` (node_modules is linked); the worktree is SPARSE: run ONLY the new test file and the folders the criteria name.

### THE CELL (`AR-y-416`, inlined)

*Context.* Portal at `origin/DEV` (4f9f2f633dc0), `src/pages/TicketCenter/`. The CRO's gaps (`org/tier1_exec/4.0.0_SA_CRO~TCKT/deliverables/TCKT_ANLREQ_FLOW_GAPS_20261019.md`) and brief (`docs/briefs/irpt-anlreq-ticket-center-flow-cleanup-brief-20261019.md`, O1 and O2) are the sources; read gaps G1, G2, G3, G9, G10. Measured at DEV: `AnalysisRequestParts.tsx` has the `advisorEmail` field (lines about 54-56, 70, 164-175, `advisorLoginEmailApplies` lines about 75-83), the report-type `<select aria-label="Report type">` (about line 190) fed by `REPORT_TYPES`, and the `add_commentary` checkbox (about lines 225-230, default false at line 71, echoed in the form-as-filled table at about line 593); `analysisRequest.ts` has `REPORT_TYPES`, `VARIANT_FOR`/`variantFor` (about lines 57-67), `answersRefusal` (about lines 69-77, "Choose a report type."), `advisorEmailRefusal` and `normalizeAdvisorEmail` (about lines 80-93), `partnerAnswers` (about line 306), `submitHeldReason` (about lines 385-402), the `advisorEmail` threading of `fileAnalysisRequest` and `fileAndRequestAnalysis` (about lines 409-423 and 603-610), `variantRefusal` (about line 535) and `analysisBody` (about lines 495-520); `TicketCenter.tsx` has `loadAllowedFirms` (about lines 105-135: an internal caller reads only the Global context's `READY` firms) and the firm effect (about lines 326-346) and `loginEmailApplies`/`advisorEmail` (about lines 357-394). `src/api/endpoints/investor-reporting.ts` has `uploadAnalysisInput(req, selectedTenant?, advisorEmail?)` (about lines 874 and 1231-1233). The ticket service is UNCHANGED: it stores `report_type` from a fixed enum, so the portal derives it. The backend derives the variant from the count of comparison keys and accepts `variant: "auto"` (`infra/aws/lambda/investor-reporting/ycharts/generate/submission.py:72`).

*The change.*
1. **No advisor login email.** Remove the field, `advisorLoginEmailApplies`, `advisorEmailRefusal`, `normalizeAdvisorEmail`, the `advisorEmail` form member and every `advisorEmail` argument of `fileAnalysisRequest`/`fileAndRequestAnalysis` and `TicketCenter.tsx`. NO upload post sends `advisor_email`. In `investor-reporting.ts` the optional third parameter may stay in the client signature but nothing passes it (or remove it if no other caller uses it: read the callers; the smaller change wins). The advisor NAME field ("Advisor (required)") stays.
2. **No report-type dropdown; the type is derived.** Remove the `<select aria-label="Report type">`. Add a pure exported `reportTypeFor(count: number): AnalysisReportType` in `analysisRequest.ts`: 0 -> `'Overview'`, 1 -> `'Comparison'`, 2 to `MAX_COMPARISONS` -> `'Multi-Comp'` (a count above the maximum keeps today's refusal sentence for too many comparables). `answersFromForm` (AnalysisRequestParts.tsx) sets `report_type` from the picked keys' count with `reportTypeFor`; `answersRefusal` no longer asks for a type; the body `variant` is `variantFor(reportTypeFor(count))`; `variantRefusal` survives only for a count above `MAX_COMPARISONS`. The legend text of the comparables fieldset no longer names the report type ("the report type above must fit the count"). `partnerAnswers` and the form-as-filled table keep reading `report_type` (the table row "Variant" prints the derived value).
3. **Commentary is always requested.** Remove the `add_commentary` checkbox and the `add_commentary` form member; the ticket answers carry `add_commentary: true` (the answers contract is unchanged) and the analysis submission body carries `commentary_requested: true` (a JSON boolean; add it to `analysisBody`; the receiver already accepts it, see the pair's step S). The form-as-filled row "Add commentary" may stay and reads Yes.
4. **An Opal staff filer may file for any firm.** `loadAllowedFirms` for an INTERNAL caller returns EVERY firm of the Global context in served order (not only `READY`; the label rule is unchanged), and still throws when the call fails or the answer is not a Global context or holds no firm. `submitHeldReason` for an internal filer holds only for: no title, no firm CHOSEN, no file (the "still loading" and "could not be loaded" holds remain only as the words shown beside the firm line while the list is absent, not as a submit gate that needs the form closed and reopened): when the firm read FAILED the firm line shows an inline `Try again` button that re-reads the firms (one more `loadAllowedFirms` call) instead of the sentence "Close the form and open it again to retry". A partner filer's behaviour is unchanged.
5. Every existing test that pins a removed element is changed in the same commit so it pins the new behaviour or the element's ABSENCE (read: `advisor-email.test.tsx`, `analysis-variant-select.test.tsx`, `analysis-form-i1.test.tsx`, `analysis-form-i1-record.test.tsx`, `analysis-form-no-fee.test.tsx`, `analysis-request.test.tsx`, `analysis-submit-silence.test.tsx`, `analysis-firm-choice.test.tsx`, `analysis-firm-c-firm.test.tsx`, `internal-filer-chooses-firm.test.ts`, `filing-*.test.tsx`, `partner-view.test.tsx`, `package-*.test.tsx`): keep each test's intent, never delete an assertion without replacing it, never weaken one.

*The new test file `src/pages/TicketCenter/__tests__/analysis-form-derived.test.tsx` (EXACTLY eight tests).* (1) the form has no element labelled `Report type`; (2) no element labelled `Advisor login email`; (3) no `Add commentary` checkbox; (4) filing with 0, 1 and 2 checked comparables posts variants `overview`, `comparison`, `multicomp` and creates the ticket with `report_type` `Overview`, `Comparison`, `Multi-Comp`; (5) the analysis submission body carries `commentary_requested: true`; (6) an internal filer's upload posts carry no `advisor_email` query member; (7) an internal filer whose Global context lists one `UNAVAILABLE` firm and one `READY` firm is offered both, and the submit is held only for a missing title, firm or file (not for readiness); (8) a failed firm read shows a `Try again` control and pressing it re-reads the firms (the second read's list appears).

*What to do.* (1) Read the files above at your worktree's HEAD; run the baseline `cd portal && bun test src/pages/TicketCenter` and print the pass and fail counts. (2) Make the change and update the tests; write the eight new tests; run the new file (must print ` 8 pass` and ` 0 fail`) and the whole folder (` 0 fail`); print both. `controls.mutant` for the proof: the new test file run with the `Report type` select put back (test 1 must FAIL). (3) Write `check_o2_bound.py` (below), run it, commit the portal source in the portal worktree and the workspace files, then the proof instance.

You also write `check_o2_bound.py` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/` (ruff clean, stdlib only): it takes `git -C C:/dev/wk-irpt-anlreq-310/portal merge-base HEAD origin/DEV` (resolve the portal worktree from this script's own location, never a typed absolute path: use `git rev-parse --show-toplevel` of the workspace and append `portal`), lists the files changed since it, and prints `O2-BOUND-OK files=<n>` only when every changed path is under `src/pages/TicketCenter/` or is `src/api/endpoints/investor-reporting.ts`; otherwise `O2-BOUND-BAD <paths>` and a non-zero exit. Run it before your first edit (it prints OK files=0 there: that is its base state, so do not count it as the build check) and after.

---

## ACCEPTANCE

<criterion id="AR416-y-AC1" cell_refs="AR-y-416"><invocation>cd portal && bun test src/pages/TicketCenter/__tests__/analysis-form-derived.test.tsx</invocation><expect> 8 pass</expect></criterion>
<criterion id="AR416-y-AC2" cell_refs="AR-y-416"><invocation>cd portal && bun test src/pages/TicketCenter</invocation><expect> 0 fail</expect></criterion>
<criterion id="AR416-y-AC3" cell_refs="AR-y-416"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/check_o2_bound.py</invocation><expect>^O2-BOUND-OK files=[1-9][0-9]*$</expect></criterion>



<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/IRPT_ANLREQ.TO-AR-y-416.o1-o2-form-asks-no-email-no-type-no-commentary-box-staff-file-any-firm.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-416.o1-o2-form-asks-no-email-no-type-no-commentary-box-staff-file-any-firm`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR416-y-AC1,AR416-y-AC2,AR416-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-416</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
portal/src/pages/TicketCenter/
portal/src/api/endpoints/investor-reporting.ts
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-416.o1-o2-form-asks-no-email-no-type-no-commentary-box-staff-file-any-firm.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one Ticket Center folder of the portal plus one client signature; a candidate branch, nothing landed or pushed; the release (DEV merge, PROD promote) is a separate act with its own approval row (the Ticket Center is Opal-internal per PRD v0.6).
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the CRO gaps G1 G2 G3 G9 G10, the DEV code at the cited lines and the PRD v0.24 against this cell; the lens: a test deleted or weakened to pass (the difference control re-adds the select and test 1 must fail), a field removed in the UI but still sent (test 6), a type derived wrongly at the boundary (test 4 pins 0, 1 and 2), the partner path broken (the folder run includes `partner-view.test.tsx`), the firm gate removed for partners too (the change is for internal filers). NOT seen (blind): the live Global context and the deployed backend (the release pairs the portal with AR-y-415); denominator: three criteria; AC3 prints OK at the base by construction, so AC1 is the build check.
</preflight>

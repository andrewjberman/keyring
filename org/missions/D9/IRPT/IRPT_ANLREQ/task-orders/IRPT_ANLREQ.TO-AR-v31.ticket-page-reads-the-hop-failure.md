# TO IRPT_ANLREQ.TO-AR-v31 -- BUILD the ticket page's read of a hop failure: the status route's words, shown only while no package is attached (FWD-4; portal source and tests only)

<to_id>IRPT_ANLREQ.TO-AR-v31</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~270</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>TICKET</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a portal change landing on DEV only, an Opal-internal product file; the worker pushes and deploys NOTHING)
**Decomp cell:** `AR-v-31` (`decompositions/IRPT_ANLREQ_DECOMP_R3_V.md`) | **outcome_ref:** FWD-4 | **depends_on:** none to build

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~270`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-270` (workspace, branch `wk-IRPT_ANLREQ-270`) and its portal worktree `C:/dev/wk-irpt-anlreq-270/portal` (the portal's own repository, branch `wk-IRPT_ANLREQ-270-portal`, cut from portal `DEV` at the commit the issuer names in the issuance), both provisioned by the issuer. Work and commit only there.
  - Workspace files (your deliverables folder, your record, the order's status flip): `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~270 <0.9.0_WK_IRPT_ANLREQ~270@opal.agent>" -F <msgfile> -- <paths>` run in the workspace worktree.
  - Portal files: `git -c user.name=0.9.0_WK_IRPT_ANLREQ~270 -c user.email=0.9.0_WK_IRPT_ANLREQ~270@opal.agent commit -F <msgfile>` run in the PORTAL worktree, after staging only the files you changed. **Never push, never run `bun run dev`'s proxy against the live API, never call a live endpoint.**
- Write every message file with the Write tool. A row id has the form `IRPT_ANLREQ-W270-S<k>` (take the next free `<k>`); `surfaced_at` = `date -u +%FT%TZ`. No non-ASCII in what you add. Keep `INVESTIGATION_v*.md` byte-for-byte except for rows appended in binary mode.
- The proof instance: a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES.
- The first act: test that `org/`, `.tools/` and `portal/src/pages/TicketCenter/AnalysisRequestParts.tsx` exist in your worktrees. If any is absent, STOP and file a BLOCKING row; do not widen a sparse checkout, copy files, or rebuild a tree.

### WHY

PRD C-HOP-FAILURE (v0.21, both halves signed): a hop of the analysis request that fails silently (the ready-signal send, the commentary draft, the packager) is shown on the TICKET by READING the failure, never by a service writing a note to it. The status route already returns the failure; this cell makes the ticket page show it. The contract of the cell is `org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R3_V.md`, section CONTRACT (read it first).

### THE CELL (`AR-v-31`, inlined) -- BUILD ONLY. Nothing is deployed, pushed or called live.

**The shape you read** (from the status producer, merged; do not change any of it): `getJobStatus(jobId, selectedTenant)` on the IR client (`src/api/endpoints/investor-reporting.ts` about line 1496) returns a `StatusEnvelope` (`src/pages/InvestorReporting/contracts/index.ts` about line 264; adapted in `contracts/adapt.ts` about line 578). It carries `publicReasonCode: string | null`. A hop failure arrives as `publicReasonCode` one of `READY_SIGNAL_SEND_FAILED`, `COMMENTARY_DRAFT_FAILED`, `COMMENTARY_DRAFT_REFUSED`, `PACKAGER_REFUSED`, `PACKAGER_FAILED` (or an unchanged `ANALYSIS_*` reason for an unknown hop), and its WORDS are the `label` of the LAST entry of `safeActions` when that entry came from the wire action `NONE` (the adapter maps each wire action through `SAFE_ACTION_FOR_WIRE`, about `adapt.ts:421`: read how `NONE` maps and use THAT mapped value, never a string you guess). The words' first sentence names the step and the rest says what happens next. A hop failure does not change the state or the dates.

In `portal/src/pages/TicketCenter/AnalysisRequestParts.tsx` (read first: `PackageReaders` about line 309, `AnalysisDraftAndPackage` about line 639, `PackageFiles` about line 475, how `ir` reaches the block and how `ticket.report_ref` and `ticket.package` are typed):

1. **The read.** When an `analysis_request` ticket is shown and it has a `report_ref.request_id`, call `ir.getJobStatus(ticket.report_ref.request_id, <the ticket's firm>)` ONCE when the ticket is opened and once again on the existing refresh action; no timer, no polling. The firm is the ticket's own requester firm (find the field the file already uses for it; never a value the viewer types). Extend the slice type the block receives (`PackageReaders` or its neighbour) with an OPTIONAL `getJobStatus` so existing tests that pass a smaller client still compile and still pass. If the real client is not already the object handed to the block, the one pass-through line goes in `portal/src/pages/TicketCenter/TicketCenter.tsx` and nowhere else in that file.
2. **The display.** When the envelope's `publicReasonCode` is a hop-failure code and a words entry exists, show ONE short block on the ticket inside the existing white panel idiom of this file: the words, in navy ink, with the file's existing danger-icon idiom if it has one (read DESIGN.md C3, C5.8, C12 first: no new colour, no light text on white, no band). Show it ONLY while the request is unfinished: `ticket.package` absent. A ticket whose package is attached shows NO failure (clause 5): the package is the completion signal and the stored failure stays as history.
3. **The quiet cases.** No call at all for a ticket with no `report_ref.request_id`. A status call that throws or rejects shows nothing extra and never breaks or blanks the ticket page (follow the file's own error idiom). An envelope with a hop code but no words entry shows nothing extra (never invent words from the code).
4. **Tests** in the NEW file `portal/src/pages/TicketCenter/__tests__/hop-failure-read.test.tsx` (copy the style, fixtures and render helpers of `package-open.test.tsx` and `commentary-package.test.tsx`; a stubbed client, no network), with EXACTLY these six test names:
   - `shows the failure's words while no package is attached`
   - `shows no failure once a package is attached`
   - `reads the status by the ticket's request id with the ticket's firm`
   - `makes no status call for a ticket with no request id`
   - `shows nothing extra when the status carries no words`
   - `a failed status call shows no failure and does not break the ticket page`
   Edit an existing test ONLY where it asserted a client object that now needs the optional method; list each edit (old and new line) in your record. No existing assertion about another behaviour may change.
5. **Look at the page (portal law).** Render the changed block and READ the result against `portal/DESIGN.md` (cite a clause number for anything you reject). Use the repo's `scripts/ui-smoke.mjs` if it can reach a ticket in this state (its output prints `CANVAS:`, which must read `rgb(244, 246, 250)`); if it cannot, say so in your record and say exactly what you did instead (for example a DOM render in the test with the markup printed). Never claim a render you did not do. Put the path of any screenshot you read in your record.
6. **Write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~270/mutant_check.py`** (AC3 below) and a short `R3_V_RECORD.json`: the lines you changed in each worktree, the test counts, the before-arm (the six tests on the base: every one FAILS or the file is absent), the edited existing tests, what you rendered and read, `not_read`.

7. **AMENDMENT 1 (issuer, 2026-10-16; the contract is `IRPT_ANLREQ_DECOMP_R3_V.md`, section AMENDMENT 1, item 6).** Review of your first commits found that the failure block can never show for a ticket with NEITHER a draft NOR a package, which is where three of the five codes land (`READY_SIGNAL_SEND_FAILED`, `COMMENTARY_DRAFT_FAILED`, `COMMENTARY_DRAFT_REFUSED` happen before any draft exists). Two guards hide it: `AnalysisRequestParts.tsx` `if (!draft && !pkg) return null` in `AnalysisDraftAndPackage`, and `TicketCenter.tsx` rendering the row only when `(t.draft_commentary || t.package)` holds. Change both so that an `analysis_request` ticket with a `report_ref.request_id` reaches the read whether or not it has a draft, the failure shows while it has no package, and a ticket with neither a draft nor a package and no failure leaves NO blank row (no empty `<tr>`, no stray padding: look at what you render). The row condition in `TicketCenter.tsx` is now in your grant beyond the pass-through, for this one condition only. Add two tests to the same file, EXACTLY named `shows the failure on a ticket with neither a draft nor a package` and `leaves no blank row for a ticket with neither a draft nor a package and no failure`; the six existing tests keep passing unchanged. Then re-run `AR31-v-AC1`, `AC2` and `AC3`, update your record and the proof instance with the new results, validate, and flip the status to `complete` only when it prints VALID. Your first-session commits are inherited state.

8. **AMENDMENT 2 (issuer, 2026-10-16; decomposition section AMENDMENT 2, item 7).** Reviewing your AMENDMENT-1 commits, the issuer ran your checks (8 of 8, `tsc`, the mutant: all as you reported) and found that `useHopFailureWords` makes the status call for a request whose package is attached, where clause 5 hides the answer, and `AnalysisPackageRow` is rendered for every ticket on the board. Change the read's `enabled` condition so that NO status call is made unless the ticket is an `analysis_request`, has a `report_ref.request_id`, and carries no package. `AnalysisDraftAndPackage`'s own use of the hook follows the same condition. Add two tests to the same file, EXACTLY named `makes no status call for a ticket whose package is attached` and `makes no status call for a ticket that is not an analysis request` (each asserts the call count is 0 through your `calls` spy); the eight existing tests keep passing unchanged. Re-run `AR31-v-AC1` (now ten names), `AC2` and `AC3`, update your record and instance, validate, and flip the status to `complete` only when it prints VALID. Your earlier commits are inherited state.

### ACCEPTANCE

<criterion id="AR31-v-AC1" cell_refs="AR-v-31"><invocation>python C:/dev/wk-irpt-anlreq-270/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~V2/AR_V_CHECKS/ar_v_checks.py v31-failure --portal C:/dev/wk-irpt-anlreq-270/portal</invocation><expect>^V31-FAILURE-OK</expect></criterion>
`AR31-v-AC1`: the ten named tests exist and pass (the six of step 4, the two of step 7 and the two of step 8).

<criterion id="AR31-v-AC2" cell_refs="AR-v-31"><invocation>python C:/dev/wk-irpt-anlreq-270/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~V2/AR_V_CHECKS/ar_v_checks.py portal-tsc --portal C:/dev/wk-irpt-anlreq-270/portal</invocation><expect>^PORTAL-TSC-OK</expect></criterion>
`AR31-v-AC2`: the portal typechecks (`tsc -b`). Also run, once, the existing TicketCenter tests in the portal worktree (`bun test src/pages/TicketCenter`) and record the counts in your record (a drain check; the issuer re-runs it).

<criterion id="AR31-v-AC3" cell_refs="AR-v-31"><invocation>python C:/dev/wk-irpt-anlreq-270/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~270/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR31-v-AC3` (the one mutant that fails): you write `mutant_check.py`. It records the sha256 of `AnalysisRequestParts.tsx` in the portal worktree, removes the clause-5 guard (the failure then shows even when `ticket.package` is attached), runs `bun test` on the new test file, and RESTORES the file byte-for-byte in a `finally` block, verifying the sha256 equals the recorded one. It prints `MUTANT-FIRES` only when the mutated run FAILED and the restore verified; otherwise `MUTANT-SURVIVES` or `MUTANT-RESTORE-FAILED` and exit 1.

<criterion id="AR31-v-AC4J" cell_refs="AR-v-31" judgment="true"/>
`AR31-v-AC4J` (judgment, graded at L9, never by you): the ticket page names the failed step and what happens next only while no package is attached, for a ticket with or without a draft, makes no call it should not, leaves no blank row when there is nothing to say, never breaks the page, and adds no route, write, principal or colour.

<expected_criteria>AR31-v-AC1 AR31-v-AC2 AR31-v-AC3 AR31-v-AC4J</expected_criteria>

A fourth mechanical criterion is not cut: AC3 is the difference-control arm of AC1, not a separate check.

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~270/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: `src/api/endpoints/investor-reporting.ts`, `src/pages/InvestorReporting/**`, `DESIGN.md`, and everything else.
- LOCAL: never push, never call a live endpoint, never edit a service or Terraform. No non-ASCII.

<paths>
portal/src/pages/TicketCenter/AnalysisRequestParts.tsx
portal/src/pages/TicketCenter/TicketCenter.tsx
portal/src/pages/TicketCenter/__tests__/hop-failure-read.test.tsx
portal/src/pages/TicketCenter/__tests__/commentary-package.test.tsx
portal/src/pages/TicketCenter/__tests__/package-open.test.tsx
portal/src/pages/TicketCenter/__tests__/package-r2.test.tsx
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R3_V.md</decomp_doc>
<owned_cells>AR-v-31</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~270/IRPT_ANLREQ.TO-AR-v31.ticket-page-reads-the-hop-failure.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-v31`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR31-v-AC1,AR31-v-AC2,AR31-v-AC3,AR31-v-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- portal source in a worker worktree; nothing is deployed, applied or invoked. The landing is the issuer's candidate on portal DEV under the approved-row route.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed; the page calls the existing status route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or timer (one read on open, one on the existing refresh).
comp-iam: DECLARED-NOT-APPLICABLE -- the read runs under the viewer's own session; no IAM change.
comp-adversary: RUN -- by reading C-HOP-FAILURE v0.21 and the status adapter against this cell; the lens: a failure shown on a FINISHED request, a status call for a ticket with no request id, a thrown call that blanks the page, words invented from a code, a colour the design contract forbids. BLIND to: the deployed status route (it carries the failure code only after `~G2`'s own later release) and the live ticket data (denominator: 1 contract row, 1 adapter and 1 page file read).
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling msg 8908 (the ticket page read is `~V2`'s) and `~G2`'s shape message 9053 (merged `766ec706ee`), in the issuer's `TICKET` workstream, round 3 (rounds 1 and 2 were `TO-AR-v11` to `v13` and `v21`). The CVO's ratified-text half of PRD v0.21 is SIGNED (the ruling's hold on cutting is lifted). Slot 270 is chosen with a gap above the highest slot read in orders, worktrees and branches (254) because other COOs issue into this project concurrently.
- The landing (outside this order): the issuer registers the portal candidate `cand/dell2/<slug>` on a PROD base, approves it as an Opal-internal page, and the box manager lands it on DEV with `.tools/portal-merge-forward.sh`. The live arm (each failure driven on purpose against the released status route) is FWD-4's run, not this cell's.
- Base: `AR31-v-AC1` FAIL as expected (the test file is absent); `AR31-v-AC2` PASS as expected (the control: the portal typechecks at the base, `rc=0`); `AR31-v-AC3` FAIL as expected (no checker file).

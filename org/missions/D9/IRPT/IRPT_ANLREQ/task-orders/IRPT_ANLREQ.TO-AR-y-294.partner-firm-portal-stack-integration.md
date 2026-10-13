# TO IRPT_ANLREQ.TO-AR-y-294.partner-firm-portal-stack-integration -- integrate the partner-firm portal candidates into ONE reviewable branch cand/dell2/partner-firm-stack cut from origin/PROD, and reconcile the tests they strand

<to_id>IRPT_ANLREQ.TO-AR-y-294</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~111</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-294` (`decompositions/IRPT_ANLREQ_DECOMP_R23F_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~111`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-111` (branch `wk-IRPT_ANLREQ-111`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~111 <0.9.0_WK_IRPT_ANLREQ~111@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W111-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-294`, inlined) -- THE PORTAL STACK. ONE candidate branch `cand/dell2/partner-firm-stack` cut from `origin/PROD` for the CTO's review (laptop ruling @a5ec5c380c, CTO msgs 7279 and 7292); nothing is landed, pushed or deployed.

*The partner-firm filing (PRD v0.5 FWD-1, the CTO's ruling (A)) is five portal candidates that were each cut off a different DEV tip and each tested alone: `AR-y-274` C-FIRM (`wk-IRPT_ANLREQ-95-portal` @6d117bfe85), `AR-y-275` the variant select (`wk-IRPT_ANLREQ-96-portal` @80d7c70a7d), `AR-y-273` the form as the fourth attachment (`wk-IRPT_ANLREQ-94-portal` @ab6ede6989), `AR-y-283` the partner view (`wk-IRPT_ANLREQ-104-portal` @e82daf4c98) and `AR-y-282` the dev-build route gate (`wk-IRPT_ANLREQ-103-portal` @46a49e57e3). Three IRPT_ANLREQ merges sit on DEV and not on PROD: `AR-y-265` the silent-submit words (`wk-IRPT_ANLREQ-90-portal` @794b7df4, DEV merge 73d8d3a4), `AR-y-263` no fee (`wk-IRPT_ANLREQ-88-portal` @9ef6a359b8, DEV merge 0101dd66), `AR-y-262` model order and color (`wk-IRPT_ANLREQ-87-portal` @62d455f5, DEV merge a577cba5); they are already registered as approval rows and ride this stack as DEPENDENCIES. The earlier candidates (-74, -81, -85) are already in PROD. They edit the same Ticket Center files, and the worker of `AR-y-283` found the combination strands ten tests of `AR-y-265` (`__tests__/analysis-submit-silence.test.tsx` mounts a firm caller on the create path that the partner view replaces; row `IRPT_ANLREQ-D2-W104-S1`). `AR-y-279` (commentary_requested only when true, @9892130cfd) is HELD by the CTO until IB-pr-456 is live and is NOT in this stack. Order of landing the CTO set: the silent-submit fix first (already on DEV), the form candidates, and `AR-y-282` (the route gate) LAST, because on a dev build it lets a partner reach the board and the board is unscoped until `AR-y-281` is deployed and `AR-y-283` is on DEV.*

1. **The branch.** In the portal repository (`C:/dev/ajb_workspace/portal`): `git fetch origin DEV PROD` (permitted), record `prod_tip` (the full sha of `origin/PROD`; the CTO named release 63c4f9e3 as the base, and `origin/PROD` now descends from it by two commits of the laptop's contributing-boxes release: state both and use `origin/PROD`), then `git worktree add C:/dev/wk-portal-111 -b cand/dell2/partner-firm-stack origin/PROD`. Never check out, reset or commit anything else in the portal checkout; never push. Give the worktree a committer identity on the command line if it has none. Link `node_modules` the way earlier workers did (a junction to an existing install; say which; never delete anything you did not make). Read the portal's `CLAUDE.md` and `DESIGN.md` first.
2. **Merge in this order, one at a time:** FIRST the three dependencies `wk-IRPT_ANLREQ-90-portal` @794b7df4, `wk-IRPT_ANLREQ-88-portal` @9ef6a359b8, `wk-IRPT_ANLREQ-87-portal` @62d455f5 (merge the branch tips, not DEV's merge commits), THEN the five: `wk-IRPT_ANLREQ-95-portal` (C-FIRM), `wk-IRPT_ANLREQ-96-portal` (variant), `wk-IRPT_ANLREQ-94-portal` (fourth attachment), `wk-IRPT_ANLREQ-104-portal` (partner view), `wk-IRPT_ANLREQ-103-portal` (route gate). Use `git merge --no-ff --no-edit <branch>` so each stays one reviewable merge; after EACH of the eight merges (and the test-edit commit) run `bun test src/pages/TicketCenter src/lib` and `bun run typecheck` and record the counts in `after_each` {branch, merge commit, tests passed, failed, typecheck rc}. A merge conflict: resolve it keeping BOTH sides' intent (never drop a candidate's behaviour to make a conflict go away), record each conflict in `conflicts` {file, what collided, how resolved}; if two candidates cannot both be kept in one place, STOP and file a BLOCKING row naming the lines (the issuer asks the CTO) rather than choosing.
3. **Reconcile the stranded tests.** After the last merge, run the whole `src/pages/TicketCenter` folder, `src/lib`, `src/components` and the `dsgn-irptv1` folder. For each failing test not in the known `dsgn-irptv1` baseline (371 pass, 10 fail, 2 errors, all ENOENT on workspace-relative paths because a worktree sits outside `C:/dev/ajb_workspace`; state the counts both ways against a clean `origin/PROD` worktree): decide, by reading what it asserts, which of these it is and act: (a) its caller or fixture no longer reaches the path it tests (the ten `analysis-submit-silence` tests mount a firm caller on the create path): re-point ONLY its mounting/fixture to the path that now serves that caller (the partner view for a partner caller; an internal caller where the page still files for internals) and KEEP every assertion's words and intent (the held-submit reasons, the upload-refused words, the create-refused words, the empty-error words, the success ticket id); (b) it pinned a behaviour a candidate deliberately removed (the old picker, the Branded PDF row, the inferred variant): edit it to the new behaviour and list it; (c) it is a real regression: STOP and file a BLOCKING row. Never delete a test, never loosen an assertion; list every edit in `test_edits` {file, test name, why, before text, after text}.
4. **The words a person sees, once, end to end.** In the record, `what_a_person_sees` for a PARTNER caller on a dev build (the form with the locked firm, the variant select, the model checkboxes in order, no fee field, the commentary box as on DEV, the filing sent through submit, the refusal words, the list of own-firm requests) and for an INTERNAL caller (what is unchanged; what staff are told). `route_gate`: what the build flag grants where (the vite dev server only; a production bundle grants nothing; the CTO ruling W103-S1 is open).
5. **Commit** the merges and any test edits in the portal worktree (merge commits as above, test edits in one commit); record the full head sha. **Write `r23/PORTAL_PARTNER_STACK.json`:** `prod_tip`, `branch`, `head`, `merges` {branch, commit}, `after_each`, `conflicts`, `test_edits`, `final_counts` {TicketCenter, lib, components, dsgn-irptv1 with the clean-PROD counts beside}, `typecheck`, `what_a_person_sees`, `route_gate`, `claim`, `not_read` (a browser render; the live edge; the server routes).
6. **In your report:** the order of the merges, each conflict, the edits to the stranded tests, the counts.

### ACCEPTANCE

<criterion id="AR294-y-AC1" cell_refs="AR-y-294"><invocation>python C:/dev/wk-irpt-anlreq-111/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y294-stack --root C:/dev/wk-irpt-anlreq-111</invocation><expect>Y294-STACK-OK</expect></criterion>
`AR294-y-AC1`: the record lists the eight merges in order (three dependencies, five candidates) with the test and typecheck counts after each, every conflict and how it was resolved, every test edit with its before and after text, the final counts with the clean-PROD baseline, and a portal head commit that exists.

<criterion id="AR294-y-AC2J" cell_refs="AR-y-294" judgment="true"/>
`AR294-y-AC2J` (judgment, graded at L9, never by you): all five candidates' behaviours survive the merge, no test was deleted or loosened, the AR-y-265 words are asserted on the path that now serves their caller, the route gate is merged last, the held commentary candidate is NOT in the stack, and nothing was landed or pushed.

<expected_criteria>AR294-y-AC1 AR294-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~111/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23F_Y.md</decomp_doc>
<owned_cells>AR-y-294</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~111/IRPT_ANLREQ.TO-AR-y-294.partner-firm-portal-stack-integration.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-294`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR294-y-AC1,AR294-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the five candidate records and rows W104-S1, W103-S3 against the cell; the lens: a candidate's behaviour dropped to make a merge conflict go away, a stranded test deleted or loosened, the route gate landing before the scoped list. The order requires the merges one at a time with counts, every conflict and every test edit listed, and the gate last. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on `AR-y-283`'s BLOCKING row `W104-S1` (the stack strands ten AR-y-265 tests) and `AR-y-282`'s row `W103-S3` (landing order), workstream `YR` round 27. The CTO reviews ONE branch instead of five. Base: `AR294-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.

<!-- ISSUER NOTE 2026-10-13 (2.0.0_SA_COO~Y2): status flipped to complete after the drain of the record. The worker recorded AR294-y-AC1 FAIL only because the ISSUER'S checker required failed 0 on every mid-stack row (W111-S4); the checker is fixed and the criterion, unchanged, prints Y294-STACK-OK. The portal branch cand/dell2/partner-firm-stack (head 1c71bfd8e1, LOCAL in the portal repository) goes to the CTO for review before an approval row is registered. AR294-y-AC2J is the CVO to grade. -->

# TO IRPT_ANLREQ.TO-AR-y-419.o3-o4-models-on-the-form-at-first-paint-no-wait-on-a-static-answer -- O3 and O4: the five Opal models render on the form at first paint, large, from a static list; the catalogue is fetched only for the free-text "Other ETFs" box; no other wait on the form gates a static or unused answer

<to_id>IRPT_ANLREQ.TO-AR-y-419.o3-o4-models-on-the-form-at-first-paint-no-wait-on-a-static-answer</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~310</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ76</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-419` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-2 (the models at first paint; the waits swept), O3, O4 | **depends_on:** AR-y-416 (SAME worker, SAME files: you start from its commits); PRD v0.24

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~310`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-310` (branch `wk-IRPT_ANLREQ-310`), with a portal worktree `C:/dev/wk-irpt-anlreq-310/portal` (branch `wk-IRPT_ANLREQ-310-portal`) provisioned by the issuer AT `origin/DEV` (4f9f2f633dc0). Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~310 <0.9.0_WK_IRPT_ANLREQ~310@opal.agent>" -F <msgfile> -- <paths>` (a commit can take up to 400 s: wait and check `git log` before retrying). The PORTAL source is committed INSIDE the portal worktree, which has no committer identity: run `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~310" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~310@opal.agent" git -C C:/dev/wk-irpt-anlreq-310/portal commit --author "0.9.0_WK_IRPT_ANLREQ~310 <0.9.0_WK_IRPT_ANLREQ~310@opal.agent>" -F <msgfile>` (write no git config).
- Write every message file with the Write tool. APPEND rows only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, and COMMIT them. `surfaced_at` of any row = `date -u +%FT%TZ`; a row id has the form `IRPT_ANLREQ-D2-W310-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~300/` (the AR-y-410 instance; read it first; `git show HEAD:<path>` if absent), `to_id` exactly the order's id, a `controls.mutant` that FIRES and a `controls.determinism` really run. No live call, NO PUSH of any branch, no deploy. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`, and flip `<status>` to `complete` (commit alone) only on VALID. Scratch outside the product tree. Run the portal tests from `C:/dev/wk-irpt-anlreq-310/portal` with `bun test <path>` (node_modules is linked); the worktree is SPARSE: run ONLY the new test file and the folders the criteria name.

### THE CELL (`AR-y-419`, inlined)

*Context.* After AR-y-416 (your own previous order, merged into your branch; read its commits first) the form still waits on a four-step chain for its five Opal model checkboxes: firm list -> firm choice -> a 400 ms debounce (`TicketCenter.tsx`, the `fetchCatalogue` effect, about line 351) -> `GET .../analysis/comparisons` (`comparisonCatalogue.ts`), until then printing `The Opal model list is not loaded.` (`AnalysisRequestParts.tsx` about line 199); a failed fetch is never retried; the checkboxes and labels are `text-xs`. The five models are a static `templates.json` in the backend (`infra/aws/lambda/investor-reporting/ycharts/generate/comparison_catalogue.py` about lines 127-149; read it and the template file it loads) and the portal already holds the five NAMES (`getAllModelColors()` in `src/lib/modelPortfolioColors.ts`). The form-as-filled attachment re-fetches the catalogue per package only to print model names (`AnalysisRequestParts.tsx`, the `(names not loaded)` fallback at about line 583). CRO gaps G4 and G5; brief O3 and O4.

*The change.*
0. **FIRST, correct a side effect of your own AR-y-416 (your report named it).** `loadAllowedFirms` now returns every firm of the Global context to an internal caller, and the Trade Request and Meeting Request forms read the same function, so an internal filer on THOSE forms is offered `UNAVAILABLE` firms too: the flow is ~V2's and was not asked for. Give `loadAllowedFirms` an explicit second behaviour, not a changed default: a parameter `includeUnavailable` (default `false`, which restores today's `READY`-only list for every caller); ONLY the Analysis Request form's firm read passes `true`. Keep the `submitHeldReason` `internal` flag as it is. Add ONE test, in the NEW file of this order (its test count below becomes SEVEN): an internal filer's Trade Request form read gets only `READY` firms while the Analysis form read gets both. Then part 1 onward.
1. **A static model list.** Add `src/pages/TicketCenter/opalModels.ts` exporting `OPAL_MODELS: readonly { key: string; label: string }[]` holding exactly the five models, with the `key` strings EXACTLY the keys the backend catalogue gives the model entries (read them from `comparison_catalogue.py` and its template file; the entry `key` is what the form sends in `comparison_keys`) and the labels the form shows today (`comparisonLabel`). The five checkboxes render from this list at FIRST PAINT, in the order `orderedModelBoxes` gives today, in text at least `text-sm` (not `text-xs`), keeping the colour rule. They need no firm, no list and no fetch.
2. **The catalogue only for "Other ETFs".** `fetchCatalogue` is called only when the filer has typed something in the `Other ETFs` box (or on its first focus), never on form open and never on a firm choice; its answer is used only to resolve typed tickers (`resolveComparison`). A failed fetch is retried once on the next typed change and says so in one plain sentence; the model checkboxes never depend on it. Remove the 400 ms firm-debounced effect and the sentence `The Opal model list is not loaded.`.
3. **Names without a fetch.** The form-as-filled table prints a model's name from `OPAL_MODELS` by key (the `(names not loaded)` fallback remains only for a key that is not one of the five, i.e. a typed ETF ticker, which prints as the ticker).
4. **The sweep (O4).** Read `TicketCenter.tsx`, `AnalysisRequestParts.tsx` and `analysisRequest.ts` for any other wait on the form or the ticket page that gates something static or unused (a loading state that holds a control whose answer needs no network; the status reads and the board refresh are legitimate: leave them). Fix each one you find in the same way (render from what the page already holds) and list every one you found, fixed or left with its reason, in your report. Check the `Needed by` date input (brief Part VII): state whether the 2026-10-16 value seen in the walk is a needed-by default or a residual price date, with the line that sets it; do not change it unless it is a residual price-date input.

*The new test file `src/pages/TicketCenter/__tests__/models-first-paint.test.tsx` (EXACTLY seven tests).* (1) rendering the Analysis Request form with NO network stub at all shows five model checkboxes immediately; (2) the checkbox labels equal the five labels of `OPAL_MODELS` and none uses the `text-xs` class; (3) opening the form and choosing a firm performs ZERO catalogue requests (a counting fetch stub); (4) typing in `Other ETFs` performs exactly one catalogue request and resolves a known ticker; (5) a failed catalogue request leaves the five checkboxes usable and the next typed change retries once; (6) the form-as-filled table prints the model label for a model key with no catalogue request; (7) an internal filer's Trade Request form read gets only `READY` firms while the Analysis Request form read gets both `READY` and `UNAVAILABLE`. ALSO a workspace check `check_o3_keys.py` (below).

*What to do.* (1) Baseline `cd portal && bun test src/pages/TicketCenter` (print). (2) Make the change; update any existing test that pinned the old chain (`analysis-form-order-color.test.tsx`, `analysis-form-i1*.test.tsx`, `filing-*.test.tsx`: same rule as before, keep intent, weaken nothing); write the six tests; run the new file (` 7 pass`) and the folder (` 0 fail`). `controls.mutant` = the new file run with the catalogue effect restored (test 3 must FAIL). (3) Write `check_o3_keys.py` and the proof instance.

You also write `check_o3_keys.py` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/` (ruff clean, stdlib only): it reads `OPAL_MODELS` from the portal file `portal/src/pages/TicketCenter/opalModels.ts` (a regex over the `key: '...'` members) and the model entry keys from the backend catalogue (import-free: read the template file the backend loads and the key rule in `comparison_catalogue.py`; if the keys are derived, call the backend's own function through `python -I` with `infra/aws/lambda/investor-reporting/` on `sys.path`), and prints `O3-KEYS-OK n=5` only when the two key sets are equal and n is 5; otherwise `O3-KEYS-BAD <diff>` and a non-zero exit.

---

## ACCEPTANCE

<criterion id="AR419-y-AC1" cell_refs="AR-y-419"><invocation>cd portal && bun test src/pages/TicketCenter/__tests__/models-first-paint.test.tsx</invocation><expect> 7 pass</expect></criterion>
<criterion id="AR419-y-AC2" cell_refs="AR-y-419"><invocation>cd portal && bun test src/pages/TicketCenter</invocation><expect> 0 fail</expect></criterion>
<criterion id="AR419-y-AC3" cell_refs="AR-y-419"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/check_o3_keys.py</invocation><expect>O3-KEYS-OK n=5</expect></criterion>



<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/IRPT_ANLREQ.TO-AR-y-419.o3-o4-models-on-the-form-at-first-paint-no-wait-on-a-static-answer.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-419.o3-o4-models-on-the-form-at-first-paint-no-wait-on-a-static-answer`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR419-y-AC1,AR419-y-AC2,AR419-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-419</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
portal/src/pages/TicketCenter/
portal/src/lib/modelPortfolioColors.ts
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-419.o3-o4-models-on-the-form-at-first-paint-no-wait-on-a-static-answer.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one Ticket Center folder of the portal; a candidate branch, nothing landed or pushed.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the CRO gaps G4 and G5, the DEV code at the cited lines and the backend catalogue against this cell; the lens: a static list whose keys drift from the backend's (AC3 compares them), a catalogue fetch left on form open (test 3), a sweep that removes a legitimate wait (the status reads and board refresh are named as legitimate), a weakened test. NOT seen (blind): the live catalogue and a browser; denominator: three criteria.
</preflight>

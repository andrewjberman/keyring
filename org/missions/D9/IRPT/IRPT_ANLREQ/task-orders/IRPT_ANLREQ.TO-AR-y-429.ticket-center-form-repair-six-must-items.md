# TO IRPT_ANLREQ.TO-AR-y-429.ticket-center-form-repair-six-must-items -- Ticket Center Analysis Request form repair: the six MUST items of the CTO front-end review (a blank Advisor is not refused, a held submit says why, the firm list retries, the held line is truthful, the ETF list follows the firm, the Keep words are seen)

<to_id>IRPT_ANLREQ.TO-AR-y-429.ticket-center-form-repair-six-must-items</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~310</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ88</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-429` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (a staff user files for any firm, never refused for want of an advisor), FWD-2 (the form asks only what cannot be inferred), C-FILING-HINT | **depends_on:** AR-y-416, AR-y-419, AR-y-425 and AR-y-428 (YOUR own commits, all on the candidate branch); CTO msgs 11159 and 11162 and the review file in the cell

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~310`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-310` (branch `wk-IRPT_ANLREQ-310`), with a portal worktree `C:/dev/wk-irpt-anlreq-310/portal` (branch `wk-IRPT_ANLREQ-310-portal`) provisioned by the issuer AT the candidate head `8942a0d70ed3` (branch `cand/dell2/anlreq-ticket-center-cleanup-v2`). Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~310 <0.9.0_WK_IRPT_ANLREQ~310@opal.agent>" -F <msgfile> -- <paths>` (a commit can take up to 400 s: wait and check `git log` before retrying). The PORTAL source is committed INSIDE the portal worktree, which has no committer identity: run `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~310" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~310@opal.agent" git -C C:/dev/wk-irpt-anlreq-310/portal commit --author "0.9.0_WK_IRPT_ANLREQ~310 <0.9.0_WK_IRPT_ANLREQ~310@opal.agent>" -F <msgfile>` (write no git config).
- Write every message file with the Write tool. APPEND rows only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, and COMMIT them. `surfaced_at` of any row = `date -u +%FT%TZ`; a row id has the form `IRPT_ANLREQ-D2-W310-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~300/` (the AR-y-410 instance; read it first; `git show HEAD:<path>` if absent), `to_id` exactly the order's id, a `controls.mutant` that FIRES and a `controls.determinism` really run. No live call, NO PUSH of any branch, no deploy. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`, and flip `<status>` to `complete` (commit alone) only on VALID. Scratch outside the product tree. Run the portal tests from `C:/dev/wk-irpt-anlreq-310/portal` with `bun test <path>` (node_modules is linked); the worktree is SPARSE: run ONLY the new test file and the folders the criteria name.

### THE CELL (`AR-y-429`, inlined)

*Context.* The CTO read the form flow of the candidate head (a code read, not a run) and found six defects that break a v0.24 outcome or strand the user. Your base is the candidate branch `cand/dell2/anlreq-ticket-center-cleanup-v2` at `8942a0d70ed3` (your portal worktree is cut from it; it carries your AR-y-416, AR-y-419, AR-y-425 and AR-y-428 commits). The review says line numbers of the earlier head `15bf70d3`; they shift by a few lines. All files are in `portal/src/pages/TicketCenter/`: `analysisRequest.ts` (aR), `AnalysisRequestParts.tsx` (Parts), `TicketCenter.tsx`. The review file is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/1.0.0_SA_CTO~DELL2/CTO_FRONTEND_REVIEW_TICKET_CENTER_CLEANUP_15bf70d3_20261020.md` (you may read it).

*The six MUST items (the CTO's words, with the places).*
1. **A blank Advisor is refused** ("Advisor is required.", aR `answersRefusal`; the field is required in Parts, placeholder "Advisor (required)"). That contradicts FWD-1 and C-FIRM: staff are never refused for want of an advisor (the backend, AR-y-415, already falls back to the signed-in principal). Make the Advisor optional for an Opal staff filer (`internal`): `answersRefusal` takes an optional second argument `internal` (default false, so a non-staff caller is unchanged); the placeholder reads "Advisor (optional)" for staff; an empty or blank Advisor is not sent (the typed name is attribution only and never required).
2. **The submit button is enabled on invalid forms.** A missing Household, an unknown typed ETF and more than 5 comparables are each refused only AFTER the press (aR `answersRefusal`, `comparisonKeysFor`). Gate the button on them: `submitHeldReason` gains optional inputs for them (the household text, and the refusal string of the comparison check when it can be computed from the form and the loaded catalogue; when no catalogue is loaded the unknown-ticker check cannot run and is not a hold) and names the reason in words in the held line, in the order a person fills the form.
3. **If the firm list fails to load, staff cannot file at all.** `readFirms` and the Try again control (`onRetryFirms`, AR-y-416) exist; check what is missing and add it: the retry also CLEARS the stale "could not be loaded" banner (`FIRMS_NOT_LOADED` set by `setError`) when the read succeeds, and the reason is shown (the failure's plain words beside the firm line, never a raw code).
4. **While firms load or have failed, the held line says "Choose the firm..." with no firm control on screen** (aR `submitHeldReason`, Parts firm line). For an internal filer while `firms` is null say "Loading the firm list..."; while `firmsFailed` say "The firm list could not be loaded; press Try again beside the firm line."; "Choose the firm this request is filed under." only when the firm control is actually on screen.
5. **The ETF list goes stale.** Typed before a firm is chosen, the catalogue is fetched with no firm and never fetched again (`TicketCenter.tsx`, the `catalogueReads` ref and `readCatalogueForTyping`). Re-read it when the firm changes (reset the read count and the loaded catalogue on a firm change; still at most two reads per firm, no read on form open).
6. **The Keep words are never seen.** A No press re-files and clears the findings, and a successful re-file closes the form, so the kept line (Parts, the `keptLine` use) never shows. Show it in the success notice (the `setNotice` / `filedNotices` text after a filed request) for every symbol the filer kept; the words are the ones AR-y-428 set: `<X> is kept as you typed it. It is not priced on this form; the report matches it to a comparable fund or lists it as not analysed.` (verify `keptLine` still yields exactly that; do not change it).

*SHOULD items (the CTO: add them if cheap; no criterion pins them; report which you did).* (a) The button reads "Uploading..." while it is actually reading the ETF list: word it truthfully. (b) The hint reads "Did you mean X? (row N: Y)" without the fund name: add the name where the catalogue has it. (c) "Open report" renders below the whole board: render it by the ticket row, or scroll to it.

*What to do.* (1) Baseline `cd portal && bun test src/pages/TicketCenter` (262 pass at your base) and print it. (2) Write the NEW file `src/pages/TicketCenter/__tests__/form-repair.test.tsx` with EXACTLY ten tests first, run it against the unchanged code (it must FAIL: the difference control): T1 an internal filer with a blank Advisor, a firm and a household passes `answersRefusal` (null); T2 the same for a non-internal caller still returns "Advisor is required."; T3 `submitHeldReason` for an internal filer with a missing household names Household; T4 it names the refusal of an unknown typed ETF; T5 it names "At most 5 comparables" for six; T6 with `firms` null it says the firm list is loading, not "Choose the firm"; T7 with `firmsFailed` it says the list could not be loaded and names Try again; T8 a firm change makes the catalogue read again (test the decision through a small exported pure helper you add, for example `catalogueNeedsRead`); T9 a successful retry of the firm read clears the firms banner (test through an exported pure helper, for example `firmsBannerAfterRetry`); T10 the success notice built for a filed request that kept `BREIT` contains the kept line for `BREIT` exactly (an exported pure helper that builds the notice text). Existing tests that pin the old behaviour (a required Advisor, the old held words) are updated to pin the new one, keeping each intent and weakening no assertion. (3) Make the changes; run the new file (` 10 pass`, ` 0 fail`) and the folder (` 0 fail`). `controls.mutant` = the new file with the household hold removed from `submitHeldReason` (test T3 must FAIL). (4) Write `check_repair_bound.py` (below), commit the portal source in the portal worktree and the workspace files, then the proof instance and flip on VALID with all three PASS.

You also write `check_repair_bound.py` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/` (ruff clean, stdlib only): it takes your portal worktree's commit whose subject starts `fix(TicketCenter): the Keep words follow` (anchor: `git -C <portal> log --format=%H --grep='^fix(TicketCenter): the Keep words follow' -1`; this is your AR-y-428 commit) and lists the files changed since it, and prints `REPAIR-BOUND-OK files=<n>` only when every changed path is under `src/pages/TicketCenter/` and n is 2 to 10; otherwise `REPAIR-BOUND-BAD <paths>` and a non-zero exit.

---

## ACCEPTANCE

<criterion id="AR429-y-AC1" cell_refs="AR-y-429"><invocation>cd portal && bun test src/pages/TicketCenter/__tests__/form-repair.test.tsx</invocation><expect> 10 pass</expect></criterion>
<criterion id="AR429-y-AC2" cell_refs="AR-y-429"><invocation>cd portal && bun test src/pages/TicketCenter</invocation><expect> 0 fail</expect></criterion>
<criterion id="AR429-y-AC3" cell_refs="AR-y-429"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/check_repair_bound.py</invocation><expect>^REPAIR-BOUND-OK files=([2-9]|10)$</expect></criterion>



<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/IRPT_ANLREQ.TO-AR-y-429.ticket-center-form-repair-six-must-items.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-429.ticket-center-form-repair-six-must-items`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR429-y-AC1,AR429-y-AC2,AR429-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-429</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
portal/src/pages/TicketCenter/
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/1.0.0_SA_CTO~DELL2/CTO_FRONTEND_REVIEW_TICKET_CENTER_CLEANUP_15bf70d3_20261020.md
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-429.ticket-center-form-repair-six-must-items.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- six defects in the Ticket Center form and the tests that pin them; a candidate branch, nothing landed or pushed.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the CTO review against this cell and the code: the lens: a test weakened to pass (the difference control runs the new file on the old code and it must fail), a non-staff caller loosened by item 1 (T2), a premise wrong about what AR-y-416 already added for the retry (item 3 says check). NOT seen (blind): the live form; denominator: three criteria.
</preflight>

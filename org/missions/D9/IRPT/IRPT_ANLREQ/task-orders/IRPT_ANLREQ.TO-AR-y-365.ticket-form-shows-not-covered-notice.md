# TO IRPT_ANLREQ.TO-AR-y-365.ticket-form-shows-not-covered-notice -- C-FILING-HINT branch (B) (PRD v0.17/v0.19): after the filing, the Ticket Center shows the door's own NOTICE words for a holding Opal cannot price (TICKER_DATA_NOT_ENTITLED), which file themselves; on the AR-y-364 candidate, src/pages/TicketCenter/ only

<to_id>IRPT_ANLREQ.TO-AR-y-365</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~162</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ26</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; a portal page; the worker lands and pushes NOTHING)
**Decomp cell:** `AR-y-365` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-2 (C-FILING-HINT) | **depends_on:** `AR-y-364` (merged `5030594b89`; candidate `cand/dell2/anlreq-filing-decision-tree-gate` @ `50db1eb4`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~162`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-162` (branch `wk-IRPT_ANLREQ-162`), with a portal worktree `C:/dev/wk-irpt-anlreq-162/portal` (branch `wk-IRPT_ANLREQ-162-portal`) provisioned by the issuer AT the candidate commit `50db1eb4`. Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~162 <0.9.0_WK_IRPT_ANLREQ~162@opal.agent>" -F <msgfile> -- <paths>`. The PORTAL source is committed INSIDE the portal worktree, which has no committer identity: run `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~162" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~162@opal.agent" git -C C:/dev/wk-irpt-anlreq-162/portal commit --author "0.9.0_WK_IRPT_ANLREQ~162 <0.9.0_WK_IRPT_ANLREQ~162@opal.agent>" -F <msgfile>` (write no git config).
- Write every message file with the Write tool. Never rewrite `INVESTIGATION_v1.md` in text mode: APPEND rows only (check `git diff --stat` shows 0 deletions on it). `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W162-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call, NO PUSH of any branch, no deploy. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree. The worktree is SPARSE: you run ONLY the new test file and the folder `src/pages/TicketCenter`.

### THE CELL (`AR-y-365`, inlined)

*Context. PRD v0.17/v0.19: a real security Opal cannot price (`TICKER_DATA_NOT_ENTITLED`) takes no typo prompt; the door (resident-side release r33, `~G2`) FILES it UNRESOLVED and returns a NOTICE finding (code `TICKER_DATA_NOT_ENTITLED`, actions `['REVIEW']`) in `answer.portfolio.findings` of a NORMALIZED answer, with no filer choice; the filer is told, in the door's words, that the holding is not covered and that Opal Staff will manage the replacement. Worker 161's step-5 read (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~161/r41/GATE_CANDIDATE.json`, key `notice_read`) found that the Ticket Center NEVER shows such a NOTICE: `fileAnalysisRequest` (`portal/src/pages/TicketCenter/analysisRequest.ts` about lines 376 to 395) never reads `portfolio`, and the only reader, `noticeDescriptions` (`portal/src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx` about line 356), belongs to the Investor Reporting composer. The smallest change it named: carry the notice descriptions into the filed outcome and render them in `TicketCenter.tsx` near line 390. The Investor Reporting files stay UNTOUCHED.*

1. **Show the NOTICE.** In `src/pages/TicketCenter/` only: after a filing whose upload answer carries `portfolio.findings` entries with code `TICKER_DATA_NOT_ENTITLED`, the form shows, under the filed outcome, one line per such entry containing the door's own `description` text AS IT COMES (no rewording, no added advice, no input, no button), headed by the single sentence `These holdings were filed as given.`. If `noticeDescriptions` is exported from the composer you may IMPORT it read-only; if it is not, write a small local function in `src/pages/TicketCenter/` (never edit the composer). A finding of any other code in `portfolio.findings` shows nothing new. With no such entry the form is exactly as before (no heading).
2. **The words that must not appear** anywhere in the Ticket Center form stay as in AR-y-363: `proxy`, `proxies`, `similar ticker`, `Use ` or `Keep` as button labels.
3. **Tests (NEW file `src/pages/TicketCenter/__tests__/filing-notice.test.tsx`; style of `filing-decision-tree.test.tsx`; run with `bun test <file>`):** (a) a filed outcome carrying one `TICKER_DATA_NOT_ENTITLED` notice shows the heading and the door's description verbatim; (b) two notices show two lines in the door's order; (c) a `portfolio.findings` entry of another code shows no heading; (d) no `portfolio` at all shows no heading (the old behaviour); (e) the notice section renders no button and no input; (f) a case whose NAME states the scope: `a holding Opal cannot price is shown in the door's own words and the filer is asked for nothing`, asserting none of the forbidden words appear. `before_arm`: run the new tests on the candidate WITHOUT your change: (a), (b) and (f) FAIL.
4. **Commit** inside the portal worktree; record the full sha and `git -C ... diff --stat 50db1eb4 <commit>` (exactly the paths you touched); create the LOCAL branch `cand/dell2/anlreq-filing-notice` at it. Never push.
5. **Write `r41/NOTICE_CANDIDATE.json`** in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~162/`: `base_candidate_sha`, `commit`, `files_changed`, `tests` {`passed`, `failed`, `folders`}, `before_arm`, `what_a_person_sees` (in words), `claim`, `not_read` (the live door's real NOTICE text after r33, the rendered page). Write the three checker scripts named in ACCEPTANCE. Run `bun run typecheck` once and record rc.
6. **In your report:** the commit, the counts, the before-arm failures, whether you imported or wrote the reader.

### ACCEPTANCE

<criterion id="AR365-y-AC1" cell_refs="AR-y-365"><invocation>python C:/dev/wk-irpt-anlreq-162/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~162/portal_check.py</invocation><expect>^PORTAL-TESTS-OK </expect></criterion>
`AR365-y-AC1`: you write `portal_check.py`: it runs `bun test` on the new test file AND on the folder `src/pages/TicketCenter` in `C:/dev/wk-irpt-anlreq-162/portal`, and prints `PORTAL-TESTS-OK <new passed> new, <folder passed> folder, 0 failed` only when every new case (a) to (f) passes and the folder has 0 failed; otherwise `PORTAL-TESTS-BAD <why>`, exit 1.

<criterion id="AR365-y-AC2" cell_refs="AR-y-365"><invocation>python C:/dev/wk-irpt-anlreq-162/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~162/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR365-y-AC2` (the one mutant that fails): you write `mutant_check.py`: with the notice rendering removed (the changed file swapped for one bun run of the new test file and restored with a sha256 check, since the test imports by relative path), it prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR365-y-AC3" cell_refs="AR-y-365"><invocation>python C:/dev/wk-irpt-anlreq-162/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~162/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR365-y-AC3` (a third check, with a reason: the Investor Reporting composer must not move): you write `scope_check.py`: it prints `SCOPE-OK` only when `git -C C:/dev/wk-irpt-anlreq-162/portal diff --name-only 50db1eb4 cand/dell2/anlreq-filing-notice` lists only paths under `src/pages/TicketCenter/`, and `git diff 50db1eb4 cand/dell2/anlreq-filing-notice -- src/api src/pages/InvestorReporting` is empty; otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR365-y-AC4J" cell_refs="AR-y-365" judgment="true"/>
`AR365-y-AC4J` (judgment, graded at L9, never by you): the not-covered notice is shown in the door's own words under one fixed heading, asks the filer for nothing, other codes show nothing, the Investor Reporting files are untouched, and nothing was pushed or landed.

<expected_criteria>AR365-y-AC1 AR365-y-AC2 AR365-y-AC3 AR365-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~162/` and this order's file (status flip only), and INSIDE the portal worktree: files under `src/pages/TicketCenter/` only. A test OUTSIDE that folder that fails because of your change: STOP, file a BLOCKING row.
- READ only: everything else, `src/api` and `src/pages/InvestorReporting` above all. NO push of any branch.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-365</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~162/IRPT_ANLREQ.TO-AR-y-365.ticket-form-shows-not-covered-notice.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-365`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR365-y-AC1,AR365-y-AC2,AR365-y-AC3,AR365-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading worker 161's notice_read and PRD v0.19 branch (B) against the cell; the lens: wording the form adds to the door's words, an input or button asking the filer for a replacement, the composer edited to share its reader, a heading shown with no notice, another code's finding shown, a proxy word. The cell requires the door's description verbatim, one fixed heading, no control, an untouched composer, and a mutant that fails. NOT seen (blind): the live door's NOTICE text after r33 and the rendered page; denominator: 6 test cases, 1 to 2 source files, 3 criteria files, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on worker 161's step-5 read (the Ticket Center never shows the NORMALIZED NOTICE) and PRD v0.19 branch (B). Workstream `ZZ26` of round 40. Base: `AR365-y-AC1`, `AC2` and `AC3` FAIL as expected (no checker files).
- Stacks on the AR-y-364 candidate (`50db1eb4`); the Ticket Center candidates ship as one chain after r33, on the CTO's approval row.

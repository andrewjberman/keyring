# TO IRPT_ANLREQ.TO-AR-y-364.decision-tree-gate-on-code-not-name-proxy -- the Yes / Replace / No tree is gated on the finding's CODE (TICKER_NOT_FOUND), not on the retired NAME_PROXY action, so it still shows after resident release r33; on the AR-y-363 candidate; plus a read of where the form shows the not-covered NOTICE

<to_id>IRPT_ANLREQ.TO-AR-y-364</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~161</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ25</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; a portal page; the worker lands and pushes NOTHING)
**Decomp cell:** `AR-y-364` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-2 (C-FILING-HINT) | **depends_on:** `AR-y-363` (merged `b601cbb516`; candidate `cand/dell2/anlreq-filing-decision-tree` @ `a168015b`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~161`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-161` (branch `wk-IRPT_ANLREQ-161`), with a portal worktree `C:/dev/wk-irpt-anlreq-161/portal` (branch `wk-IRPT_ANLREQ-161-portal`) provisioned by the issuer AT the candidate commit `a168015b`. Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~161 <0.9.0_WK_IRPT_ANLREQ~161@opal.agent>" -F <msgfile> -- <paths>`. The PORTAL source is committed INSIDE the portal worktree: the portal has no committer identity, so run `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~161" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~161@opal.agent" git -C C:/dev/wk-irpt-anlreq-161/portal commit --author "0.9.0_WK_IRPT_ANLREQ~161 <0.9.0_WK_IRPT_ANLREQ~161@opal.agent>" -F <msgfile>` (write no git config).
- Write every message file with the Write tool. Never rewrite `INVESTIGATION_v1.md` in text mode: APPEND rows only, so existing line endings stay byte-identical (check `git diff --stat` shows 0 deletions on it). `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W161-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call, NO PUSH of any branch, no deploy. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree. The worktree is SPARSE: you run ONLY the new test file and the folder `src/pages/TicketCenter`.

### THE CELL (`AR-y-364`, inlined)

*Context. The AR-y-363 candidate shows the Yes / Replace / No prompt through `filingHints` in `portal/src/pages/TicketCenter/analysisRequest.ts`, which starts from `proxyableFindings` (`portal/src/pages/InvestorReporting/tabs/analysis/prospect.ts`, about line 94): that function keeps a finding only if its `actions` contain `NAME_PROXY`. The worker's row W160-S2 found it. `~G2`'s door release r33 RETIRES `NAME_PROXY` (message 8717): a `TICKER_NOT_FOUND` finding then carries actions `REPLACE_FILE`, `REPLACE_TICKER`, `FILE_UNRESOLVED` (and `ACCEPT_SUGGESTION` first when the door has a suggestion), so after r33 the prompt would NEVER show. Until r33 the live door still sends `NAME_PROXY`. A real security Opal cannot price gets a NOTICE (`TICKER_DATA_NOT_ENTITLED`, actions `[REVIEW]`) in `answer.portfolio.findings` of a NORMALIZED answer, with no filer choice. `prospect.ts` is shared with the Investor Reporting composer and stays UNTOUCHED.*

1. In `src/pages/TicketCenter/analysisRequest.ts` make `filingHints` stop depending on `proxyableFindings`: keep a finding when its `code` is exactly `TICKER_NOT_FOUND`, whatever its `actions` list is (the old list with `NAME_PROXY`, the new list without it, or an empty/absent list). Everything else of the tree stays as signed in AR-y-363. A finding of any other code (including `TICKER_DATA_NOT_ENTITLED`) still yields no hint.
2. Re-pin, case by case and never deleting, any test of `src/pages/TicketCenter/__tests__/` that built its fixtures with `NAME_PROXY` as the only gate, by ADDING the r33 action list as a second fixture arm; say what each pinned before and now.
3. **NEW test file `src/pages/TicketCenter/__tests__/filing-tree-gate.test.tsx`** (style of `filing-decision-tree.test.tsx`; run with `bun test <file>`): (a) a `TICKER_NOT_FOUND` finding with actions `['NAME_PROXY']` (the live door today) yields the hint; (b) the same finding with actions `['ACCEPT_SUGGESTION','REPLACE_FILE','REPLACE_TICKER','FILE_UNRESOLVED']` yields the hint with its `suggestion`; (c) the same with actions `['REPLACE_FILE','REPLACE_TICKER','FILE_UNRESOLVED']` and a null suggestion yields the Replace-and-No-only item; (d) the same with an absent `actions` yields the hint; (e) a `TICKER_DATA_NOT_ENTITLED` finding with actions `['REVIEW']` yields no hint; (f) a case whose NAME states the scope: `the prompt does not depend on the retired NAME_PROXY action`. `before_arm`: run the new tests on the candidate WITHOUT your change: (b), (c), (d) and (f) FAIL.
4. **Commit** inside the portal worktree; record the full sha and `git -C ... diff --stat a168015b <commit>` (exactly the paths you touched); create the LOCAL branch `cand/dell2/anlreq-filing-decision-tree-gate` at it. Never push.
5. **A READ, no change:** write in your record where the Ticket Center form shows the findings of a NORMALIZED answer's `answer.portfolio.findings` (file and line, bytes read), and say in words whether a `TICKER_DATA_NOT_ENTITLED` NOTICE would be visible to the filer today, or not. If it would not, say what the smallest change is; do NOT make it.
6. **Write `r41/GATE_CANDIDATE.json`** in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~161/`: `base_candidate_sha`, `commit`, `files_changed`, `tests` {`passed`, `failed`, `folders`}, `before_arm`, `repinned`, `notice_read` (step 5), `what_a_person_sees`, `claim`, `not_read` (the live door, r33's real findings, the rendered page). Write the three checker scripts named in ACCEPTANCE. Run `bun run typecheck` once and record rc.
7. **In your report:** the commit, the counts, the before-arm failures, every re-pinned test, the step 5 answer.

### ACCEPTANCE

<criterion id="AR364-y-AC1" cell_refs="AR-y-364"><invocation>python C:/dev/wk-irpt-anlreq-161/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~161/portal_check.py</invocation><expect>^PORTAL-TESTS-OK </expect></criterion>
`AR364-y-AC1`: you write `portal_check.py`: it runs `bun test` on the new test file AND on the folder `src/pages/TicketCenter` in `C:/dev/wk-irpt-anlreq-161/portal`, and prints `PORTAL-TESTS-OK <new passed> new, <folder passed> folder, 0 failed` only when every new case (a) to (f) passes and the folder has 0 failed; otherwise `PORTAL-TESTS-BAD <why>`, exit 1.

<criterion id="AR364-y-AC2" cell_refs="AR-y-364"><invocation>python C:/dev/wk-irpt-anlreq-161/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~161/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR364-y-AC2` (the one mutant that fails): you write `mutant_check.py`: with the hint gate put back to `proxyableFindings` (swapped into the portal file for one bun run of the new test file and restored with a sha256 check, since the test imports by relative path), it prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR364-y-AC3" cell_refs="AR-y-364"><invocation>python C:/dev/wk-irpt-anlreq-161/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~161/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR364-y-AC3` (a third check, with a reason: the shared `prospect.ts` must not move): you write `scope_check.py`: it prints `SCOPE-OK` only when `git -C C:/dev/wk-irpt-anlreq-161/portal diff --name-only a168015b cand/dell2/anlreq-filing-decision-tree-gate` lists only paths under `src/pages/TicketCenter/`, and `git diff a168015b cand/dell2/anlreq-filing-decision-tree-gate -- src/api src/pages/InvestorReporting` is empty; otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR364-y-AC4J" cell_refs="AR-y-364" judgment="true"/>
`AR364-y-AC4J` (judgment, graded at L9, never by you): the prompt shows for a TICKER_NOT_FOUND finding under both the old and the r33 action lists, never for another code, the shared prospect.ts is untouched, the step 5 answer is read bytes, and nothing was pushed or landed.

<expected_criteria>AR364-y-AC1 AR364-y-AC2 AR364-y-AC3 AR364-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~161/` and this order's file (status flip only), and INSIDE the portal worktree: files under `src/pages/TicketCenter/` only. A test OUTSIDE that folder that fails because of your change: STOP, file a BLOCKING row.
- READ only: everything else, `src/api` and `src/pages/InvestorReporting` (`prospect.ts` above all). NO push of any branch.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-364</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~161/IRPT_ANLREQ.TO-AR-y-364.decision-tree-gate-on-code-not-name-proxy.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-364`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR364-y-AC1,AR364-y-AC2,AR364-y-AC3,AR364-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading W160-S2 and the door's message 8717 against the cell; the lens: the gate left on NAME_PROXY, a prompt shown for another code, the shared prospect.ts edited to fix it, a pre-r33 fixture dropped instead of kept as an arm, the NOTICE read answered from a name and not the bytes. The cell requires the code gate, both action-list arms, an untouched prospect.ts, and a mutant that fails. NOT seen (blind): the live door's real findings after r33 and the rendered page; denominator: 6 test cases, 1 source file, 3 criteria files, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on worker 160's row W160-S2 and ~G2's msg 8717 (NAME_PROXY gone from every finding after r33). Workstream `ZZ25` of round 40. Base: `AR364-y-AC1`, `AC2` and `AC3` FAIL as expected (no checker files).
- Stacks on the AR-y-363 candidate (`a168015b`); the decision-tree candidate does not ship without this gate.

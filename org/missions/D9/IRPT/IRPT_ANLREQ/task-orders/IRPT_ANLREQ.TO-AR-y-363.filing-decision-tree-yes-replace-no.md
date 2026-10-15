# TO IRPT_ANLREQ.TO-AR-y-363.filing-decision-tree-yes-replace-no -- C-FILING-HINT (PRD v0.19, Andrew's decision tree): the Ticket Center filing prompt becomes Yes / Replace / No for TICKER_NOT_FOUND, and an unpriceable-but-real holding gets no typo prompt; a portal CANDIDATE off origin/PROD superseding the Use/Keep hint (469b), opal-internal, NOT to be promoted before resident release r33

<to_id>IRPT_ANLREQ.TO-AR-y-363</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~160</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ24</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; a portal page; the worker lands and pushes NOTHING)
**Decomp cell:** `AR-y-363` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-2 (C-FILING-HINT) | **depends_on:** none (ships only after the door release r33 and the CTO's approval)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~160`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-160` (branch `wk-IRPT_ANLREQ-160`), with a portal worktree `C:/dev/wk-irpt-anlreq-160/portal` (branch `wk-IRPT_ANLREQ-160-portal`) provisioned at `origin/PROD` by the issuer. Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~160 <0.9.0_WK_IRPT_ANLREQ~160@opal.agent>" -F <msgfile> -- <paths>`; the PORTAL source is committed INSIDE the portal worktree (`git -C C:/dev/wk-irpt-anlreq-160/portal ...`).
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W160-S<k>`. The workspace worktree shows ` M portal`: never commit it to the WORKSPACE repository. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call (a `git fetch` of the portal's refs is permitted), NO PUSH of any branch, no deploy, no upload. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py` from inside it. Scratch outside the product tree. Your worktree is SPARSE: the folder runs under `src/pages/InvestorReporting` fail on absent paths at the base too; you run ONLY the new test file and the folder `src/pages/TicketCenter`.

### THE CELL (`AR-y-363`, inlined)

*Context. PRD v0.19 (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md`, the C-FILING-HINT row and section 'v0.19'; Andrew's own words: "If there is a ticker that doesn't connect, we check it. If the ticker doesn't exist outright, we assume it may be a typo and the agent can do a 'did you mean?' prompt and the user can say yes, replace, or no. If yes, we accept the swap, if replace we try it with the replaced ticker(s) and rerun the process for those, if no, then we say that Opal Staff will manage the replacement."). `origin/PROD` (e0b43076) carries the Use-only hint (commit 469b `a6b83f692084`): the Ticket Center form shows 'Did you mean X?' with Use, and Keep posts nothing. A previous candidate, local branch `cand/dell2/anlreq-filing-hint-keep-equal-pair` @`f78ea50ef8` (readable in the portal repository; record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~154/r41/KEEP_EQUAL_PAIR_CANDIDATE.json`), made Keep re-post the same upload with the EQUAL pair (`{finding_code: 'TICKER_NOT_FOUND', from_value: <symbol>, to_value: <the same symbol>}`, at most 20 corrections, one per `from_value`, last click per symbol). This cell builds the tree on `origin/PROD`; you may start from that commit's diff (cherry-pick `f78ea50ef8` if it applies, or re-implement) but the result is judged on the tree below only.*

**The tree (the form's whole behaviour; the files are under `portal/src/pages/TicketCenter/`: `analysisRequest.ts` (`filingHints`, `hintLine`, `keptLine`, `correctionsFor`), `AnalysisRequestParts.tsx` (`UploadFindings`), `TicketCenter.tsx` (the handlers)):**
- **(A) `TICKER_NOT_FOUND` WITH a door `suggestion`:** under the finding, `Did you mean <symbol> (<name>)?` and THREE buttons labelled exactly `Yes`, `Replace`, `No`.
  - **Yes:** re-posts the SAME upload (same `upload_token` and file) with the correction `{finding_code: 'TICKER_NOT_FOUND', from_value: <typed>, to_value: <suggestion>}` (as Use did).
  - **Replace:** reveals ONE text input per such symbol (an `aria-label` of `Replacement ticker for <typed>`) and a `Check` button; `Check` re-posts the same upload with `{TICKER_NOT_FOUND, from_value: <typed>, to_value: <the typed replacement, trimmed, upper-cased>}`; the door's answer is shown by the same tree again (a replacement that also fails gets the same prompt). An empty or whitespace-only replacement sends nothing and shows `Type the ticker you meant.`. The form makes NO vendor call and no other call.
  - **No:** re-posts with the EQUAL pair (the Keep mechanism above) and, once pressed, the line reads exactly `Opal Staff will manage the replacement.`.
- **(A) WITHOUT a suggestion:** `<symbol> was not found.` and two buttons, `Replace` and `No` (same behaviours). No `Yes`.
- **(B) a real security Opal cannot price (`TICKER_DATA_NOT_ENTITLED` and every other finding that is not `TICKER_NOT_FOUND`):** NO typo prompt and NO button; the form shows the door's own words as they come, and nothing in the form asks the filer for a replacement. (The door, in resident release r33, files such a holding UNRESOLVED with the words `Opal Staff will manage the replacement.`; the form only shows what comes back.)
- **Words that must not appear anywhere in the Ticket Center form:** `Use ` as a button label, `Keep` as a button label, `proxy`, `proxies`, `similar ticker`, and any text telling the filer to replace or name a ticker without the Replace input beside it.
- The shared corrections limits stay: at most twenty corrections per post (Yes, Replace and No hidden once twenty symbols are named), one per `from_value`, last click per symbol, never a case-only pair for Yes or Replace, never another `finding_code`.
- Nothing is sent unless the filer presses a button. The pending (not yet released) door behaviour is not worked around: until r33 the door refuses an equal pair with `CORRECTIONS_INVALID` and the form shows the server's own sentence, as for any other refusal.

1. **The branch.** Your portal worktree is at `origin/PROD` (record `prod_tip`, the full sha, after a permitted `git fetch origin`). After your commit create the LOCAL candidate branch `cand/dell2/anlreq-filing-decision-tree` at it. Never push it.
2. **Read first:** the three files above in full, the existing tests under `src/pages/TicketCenter/__tests__/` that name `Use`, `Keep`, `hint` or `correction`, and the cherry-pick source above. Print the name search in your record.
3. **Build the tree** in `src/pages/TicketCenter/` only (the three files above, plus a new small file if the Replace input needs one). Re-pin every existing test that pins `Use` or `Keep` words or Keep posting nothing, case by case, never deleted; say what each pinned before and now.
4. **The tests (NEW file `src/pages/TicketCenter/__tests__/filing-decision-tree.test.tsx`; copy the style of `filing-hint.test.tsx`; run with `bun test <file>`):** (a) suggestion present: the three buttons `Yes`, `Replace`, `No` and the line `Did you mean`; (b) Yes re-posts the same upload with the suggestion as `to_value`; (c) Replace shows the input; Check re-posts with the typed, upper-cased replacement; (d) an empty replacement posts nothing and shows `Type the ticker you meant.`; (e) No re-posts with the equal pair and shows `Opal Staff will manage the replacement.`; (f) no suggestion: only `Replace` and `No`; (g) a `TICKER_DATA_NOT_ENTITLED` finding shows no button of the tree and no prompt text; (h) a case whose NAME states the scope: `the form never asks the filer for a proxy and never sends a pair the filer did not press`, asserting none of the forbidden words appear in any state rendered by (a) to (g). `before_arm`: run the new tests on `origin/PROD` WITHOUT your change: (a) to (f) and (h) FAIL.
5. **Commit** inside the portal worktree; record the full sha and `git -C ... diff --stat origin/PROD <commit>` printing exactly the paths you touched.
6. **Write `r41/DECISION_TREE_CANDIDATE.json`** in your deliverable folder (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~160/`): `prod_tip`, `candidate_branch`, `commit`, `files_changed`, `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm`, `repinned`, `what_a_person_sees` (in words, per branch A with a suggestion, A without, B), `claim`, `not_read` (the live door's answers, r33's words, the rendered page). Write the three checker scripts named in ACCEPTANCE. Run `bun run typecheck` once and record rc (a drain check).
7. **In your report:** the commit, the counts, the before-arm failures, every re-pinned test.

### ACCEPTANCE

<criterion id="AR363-y-AC1" cell_refs="AR-y-363"><invocation>python C:/dev/wk-irpt-anlreq-160/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~160/portal_check.py</invocation><expect>^PORTAL-TESTS-OK </expect></criterion>
`AR363-y-AC1`: you write `portal_check.py`: it runs `bun test` on the new test file AND on the folder `src/pages/TicketCenter` in `C:/dev/wk-irpt-anlreq-160/portal`, parses the counts, and prints `PORTAL-TESTS-OK <new passed> new, <folder passed> folder, 0 failed` only when every new case (a) to (h) passes and the folder has 0 failed; otherwise `PORTAL-TESTS-BAD <why>`, exit 1.

<criterion id="AR363-y-AC2" cell_refs="AR-y-363"><invocation>python C:/dev/wk-irpt-anlreq-160/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~160/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR363-y-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies the file holding the `Replace` button to a scratch folder OUTSIDE the product tree with that button removed, runs the new test file against the copy, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR363-y-AC3" cell_refs="AR-y-363"><invocation>python C:/dev/wk-irpt-anlreq-160/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~160/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR363-y-AC3` (a third check, with a reason: the approver reads the scope): you write `scope_check.py`: it prints `SCOPE-OK` only when `git -C C:/dev/wk-irpt-anlreq-160/portal diff --name-only origin/PROD cand/dell2/anlreq-filing-decision-tree` lists only paths under `src/pages/TicketCenter/`, and `git diff origin/PROD cand/dell2/anlreq-filing-decision-tree -- src/api src/pages/InvestorReporting` is empty; otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR363-y-AC4J" cell_refs="AR-y-363" judgment="true"/>
`AR363-y-AC4J` (judgment, graded at L9, never by you): the form matches the tree above branch by branch, the words are exactly those named, nothing asks the filer for a proxy, nothing is sent without a press, and nothing was pushed or landed.

<expected_criteria>AR363-y-AC1 AR363-y-AC2 AR363-y-AC3 AR363-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~160/` and this order's file (status flip only), and INSIDE the portal worktree: files under `src/pages/TicketCenter/` only. A test OUTSIDE that folder that fails because of your change: STOP, file a BLOCKING row; the issuer amends the grant.
- READ only: everything else, `src/api` and `src/pages/InvestorReporting` above all. NO push of any branch.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-363</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~160/IRPT_ANLREQ.TO-AR-y-363.filing-decision-tree-yes-replace-no.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-363`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR363-y-AC1,AR363-y-AC2,AR363-y-AC3,AR363-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; nothing is landed, pushed, deployed or called. The approval row (the issuer's, opal-internal: the Ticket Center) names the page.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed by the worker; the form re-posts to the upload route it posts to today, with corrections the contract already admits. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading PRD v0.19 and the Keep candidate record against the cell; the lens: a Use or Keep label left behind, a word telling the filer to name a proxy, a button that sends on render, a Replace that bypasses the door's check, a corrections list over twenty or with two entries for one symbol, a typo prompt on a TICKER_DATA_NOT_ENTITLED finding, a re-pinned test weakened into a pass. The cell requires the three buttons and their behaviours, no forbidden word in any rendered state, nothing sent without a press, and a mutant that fails. NOT seen (blind): the live door's answers and r33's words, and the rendered page; denominator: 8 test cases, 3 source files, 3 criteria files, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's msg 8703 (PRD v0.19, Andrew's decision tree). Workstream `ZZ24` of round 40. Base: `AR363-y-AC1`, `AC2` and `AC3` FAIL as expected (no checker files).
- A portal CANDIDATE `cand/dell2/anlreq-filing-decision-tree` off `origin/PROD`; supersedes the Use/Keep hint (469b) and the unpromoted Keep equal-pair candidate. Opal-internal: the CTO approves (an approval row), after r33 reads live.

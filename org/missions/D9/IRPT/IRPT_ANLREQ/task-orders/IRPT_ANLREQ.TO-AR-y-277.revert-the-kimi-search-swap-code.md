# TO IRPT_ANLREQ.TO-AR-y-277.revert-the-kimi-search-swap-code -- revert the three drains of the withdrawn Kimi search swap (CTO msg 7176/7187) -- a named cell, because the resident files are G2's lane

<to_id>IRPT_ANLREQ.TO-AR-y-277</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~98</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-277` (`decompositions/IRPT_ANLREQ_DECOMP_R23_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~98`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-98` (branch `wk-IRPT_ANLREQ-98`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~98 <0.9.0_WK_IRPT_ANLREQ~98@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W98-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-277`, inlined) -- THE REVERT. Restore the code of AR-y-249, AR-y-250 and AR-y-251 to the state before them. Records stay. Nothing is released.

*The CTO withdrew rulings B, (a) and (a') (msg 7176) because the Kimi search and chat swap contradicts the PRD's C-SWAP, and ruled (msg 7187): 'git revert the three drains on box/dell2 in one commit that cites my 19:10Z withdrawal and row D2-S84. Code that C-SWAP retires should not sit where a release can pick it up.' The issuer cannot commit `intake/upload_suggestions.py` or `ycharts/generate/resident_worker.py` (lane `IRPT_RESIDENT_ONE_WRITER_G2`: '~Y2 asks for a change here as a named cell'); this is that cell.*

1. **The state to restore.** The trunk commit `6bca581cd1` (the drain of AR-y-245) is the last commit before the three drains. In your worktree (cut from the current head) restore EXACTLY these five files to their content at `6bca581cd1` (`git checkout 6bca581cd1 -- <path>`): `infra/aws/lambda/investor-reporting/intake/resolution_kimi.py`, `.../intake/tests/test_resolution_kimi.py`, `.../ycharts/generate/kimi_port.py`, `.../intake/upload_suggestions.py`, `.../ycharts/generate/resident_worker.py`; and `git rm` EXACTLY these five files: `.../intake/tests/test_swap_from_search.py`, `.../ycharts/generate/tests/test_kimi_search_port.py`, `.../ycharts/generate/kimi_search_qa.py`, `.../ycharts/generate/tests/test_kimi_search_qa.py`, `.../ycharts/generate/tests/test_swap_suggestions.py`. Before you do, print `git diff --stat 6bca581cd1 HEAD -- <each of the ten paths>` and confirm that between that commit and the head ONLY the three withdrawn cells (AR-y-249, 250, 251) changed these paths (use `git log --format='%h %an %s' 6bca581cd1..HEAD -- <path>` per path; a commit by any other cell touching one of the ten paths is a STOP: file a BLOCKING row naming the commit and the path, and revert nothing). The worker records, proof instances, rows and order files of those cells STAY untouched.
2. **Prove it.** After the restore: the files named above equal their `6bca581cd1` content byte for byte (`git diff 6bca581cd1 -- <path>` is empty for the five restored files; the five removed files do not exist); `python -m pytest` over `infra/aws/lambda/investor-reporting/intake/tests` prints 370 passed, 1 skipped (the count at `6bca581cd1`); the `ycharts/generate/tests` files that collect pass as they did at that commit (known baseline: 4 custody failures; fitz collection errors: show the same counts at `6bca581cd1` in a second detached worktree outside the tree). No other file is changed.
3. **Commit** ONE commit with `bash .tools/safe-commit.sh` (message file written by the Write tool) whose message cites the CTO's withdrawal (msg 7176 at 19:10Z, msg 7187) and row `IRPT_ANLREQ-D2-S84`, and lists the ten paths.
4. **Write `r23/KIMI_SWAP_REVERT.json`:** `restored` (five paths with sha256 at `6bca581cd1` and now), `removed` (five paths), `guard` (the per-path log showing only the three cells touched them), `tests` {`intake`, `generate`, `baseline_at_6bca581cd1`}, `commit`, `claim`, `not_read`.
5. **In your report:** the guard result, the counts, the commit.

### ACCEPTANCE

<criterion id="AR277-y-AC1" cell_refs="AR-y-277"><invocation>python C:/dev/wk-irpt-anlreq-98/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y277-revert --root C:/dev/wk-irpt-anlreq-98</invocation><expect>Y277-REVERT-OK</expect></criterion>
`AR277-y-AC1`: the record lists the five restored paths (equal to their content at 6bca581cd1) and the five removed paths, a guard showing only the three withdrawn cells touched them, the intake suite at 370 passed and 1 skipped, and one commit citing the withdrawal and row D2-S84.

<criterion id="AR277-y-AC2J" cell_refs="AR-y-277" judgment="true"/>
`AR277-y-AC2J` (judgment, graded at L9, never by you): exactly the ten named paths changed, nothing else, the records of the withdrawn cells stay, and no release, deploy or capability file was touched.

<expected_criteria>AR277-y-AC1 AR277-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~98/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/intake/resolution_kimi.py
infra/aws/lambda/investor-reporting/intake/tests/test_resolution_kimi.py
infra/aws/lambda/investor-reporting/ycharts/generate/kimi_port.py
infra/aws/lambda/investor-reporting/intake/upload_suggestions.py
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/intake/tests/test_swap_from_search.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_kimi_search_port.py
infra/aws/lambda/investor-reporting/ycharts/generate/kimi_search_qa.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_kimi_search_qa.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_swap_suggestions.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23_Y.md</decomp_doc>
<owned_cells>AR-y-277</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~98/IRPT_ANLREQ.TO-AR-y-277.revert-the-kimi-search-swap-code.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-277`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR277-y-AC1,AR277-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- ten source and test files restored or removed in a worktree; nothing is released, deployed or called; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading PRD v0.5 FWD-1 and the pivot direction O1 against the cell; the lens: a hop that is read from a route table and not from the code that runs it, a widened authorization, a fix for a hop that already works, a failure that is silent. The order requires the hop to be READ before it is changed, a stop-and-row where the cause is in another lane, and every failure visible on the ticket (FWD-4). NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's GO (msg 7191): PRD v0.5 ADMITTED, the FWD-1 hop cells in ONE issuance (ADDENDUM v0.5 item 4), workstream `Y` round 23. Each grant names every file the cell writes. Base: `AR277-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.

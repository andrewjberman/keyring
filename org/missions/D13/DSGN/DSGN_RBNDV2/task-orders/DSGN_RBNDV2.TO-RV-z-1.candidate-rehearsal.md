# TO DSGN_RBNDV2.TO-RV-z-1 -- FWD-5/endpoint: the feature commits replay onto the last PROD, measured locally with nothing pushed

<to_id>DSGN_RBNDV2.TO-RV-z-1</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~22</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<round>7</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-z-1` (decomp v7 @b729dc2880) | **outcome_ref:** FWD-1, FWD-5 | **depends_on:** -- (chain 1) | **slot:** ~22, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-z-1` -- a LOCAL rehearsal of the candidate branch, measuring whether this project's feature commits apply cleanly onto the last PROD. NOTHING IS PUSHED, no remote branch is created, and `.tools/portal-merge-forward.sh` is NOT run. The project's contract (C-BRANCH) keeps all work on `feature/dsgn-rbndv2-light` on this laptop; at Andrew's later push word a candidate `cand/laptop/dsgn-rbndv2-light` is cut from the last PROD carrying these commits (portal/CONTRIBUTING-BOXES.md). This cell measures the replay ahead of that word, so the risk is known and the candidate exists locally for him.

**Facts measured at the cut (read them again yourself):** the last PROD is `origin/PROD` (about `33ad65ee`, a release merge); `origin/DEV` is `ad7c100b`, the commit the feature branch was cut from; the feature branch holds about 45 non-merge commits (`git rev-list --reverse --no-merges ad7c100b..feature/dsgn-rbndv2-light`) changing 89 files, none of which `git diff --name-only origin/PROD ad7c100b` (22 files, DEV against PROD) also lists.

**Steps, in this order, in `<WS>/portal` (your portal worktree; run `git fetch origin` first, a read; never `git push`):**
1. Record `PROD_TIP=$(git rev-parse origin/PROD)` and `FORK=ad7c100b`. Print both.
2. BASELINE: make a scratch worktree of PROD (`git worktree add ../prod-baseline $PROD_TIP` under the portal's parent, detached), link its `node_modules` the way your own worktree has it (a junction to the shared one), run `bun x tsc -p tsconfig.app.json --noEmit` there and save the error lines to `TSC-BASELINE.txt` in your deliverables folder (a PROD that already has errors is a finding, not a failure); then remove that scratch worktree (`git worktree remove --force`).
3. In your portal worktree: `git switch -c cand/laptop/dsgn-rbndv2-light $PROD_TIP`.
4. REPLAY: for each non-merge commit of `git rev-list --reverse --no-merges $FORK..feature/dsgn-rbndv2-light` in order, `git cherry-pick -x <commit>`. On a conflict: print the files (`git diff --name-only --diff-filter=U`), resolve it by keeping PROD's lines outside the commit's own change and the commit's change inside it, `git add` and `git cherry-pick --continue`; if a conflict needs a design judgement you cannot make from the two sides, run `git cherry-pick --abort`, write the conflict into the record and a surprise row, and stop. An empty cherry-pick (already in PROD) is skipped and noted.
5. Run, in the candidate checkout: `bun x tsc -p tsconfig.app.json --noEmit` (save the error lines to `TSC-CANDIDATE.txt` in your deliverables folder), `bun test src/__tests__/dsgn-rbndv2`, and `bun x eslint src/__tests__/dsgn-rbndv2`. Compare the two tsc files: print `TSC-BEFORE <n> TSC-AFTER <m>` and the lines present only after.
6. Write `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~22/REHEARSAL_RECORD.md` holding these exact lines (each on its own line, with its measured value): `PROD-TIP <sha>`, `FORK <sha>`, `COMMITS-REPLAYED <n> SKIPPED <k>`, `CONFLICTS <c>` followed by one bullet per conflict (file, the two sides in a phrase, how it was resolved), `TSC-BEFORE <n> TSC-AFTER <m>`, `TESTS <pass> pass <fail> fail`, `ESLINT rc=<rc>`, `CANDIDATE-TIP <sha>`, and a final line `PUSHED NOTHING; remote candidate branch absent (git ls-remote --heads origin cand/laptop/dsgn-rbndv2-light printed nothing)` only after you ran that ls-remote and it printed nothing.
7. Leave the candidate branch `cand/laptop/dsgn-rbndv2-light` in place (local only, checked out in your worktree); do not delete it and do not push it.

Do not change any source file other than through the cherry-picks; write no code of your own.

**Out of this cell:** every file except the ones named in the BOUNDS paths; the only portal change is the candidate branch the cherry-picks create.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. Andrew's design principle for the build (not for this cell): text resolves to black ink on a white ground and to white on a coloured fill (an indigo tooltip, a coloured tile), and a line is grey on white and black on a colour; never white on white, never black on indigo. You are given the worker face only: open your order file only to edit its status, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at `86db3d1b` (the feature branch tip at the cut is 3509eae8; the commit above is an ancestor). Do not start any server.

### ACCEPTANCE

<criterion id="RB7Z1-AC1" cell_refs="RV-z-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~22; timeout 100 python <WS>/org/missions/D13/DSGN/DSGN_RBNDV2/ledger/check_rehearsal.py <WS>/portal <WS>/org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~22</invocation><expect>VERDICT: REHEARSAL-OK</expect></criterion>
`RB7Z1-AC1` -- the check file (`org/missions/D13/DSGN/DSGN_RBNDV2/ledger/check_rehearsal.py`, authored by the issuer, read-only) finds the local candidate branch descending from the last PROD with commits over it, every file the feature branch changed identical in the candidate, no remote candidate branch, and the record holding its lines; it prints `VERDICT: REHEARSAL-OK` only when every arm holds.

<criterion id="RB7Z1-AC2" cell_refs="RV-z-1"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~22; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`RB7Z1-AC2` -- on the candidate checkout every test under `src/__tests__/dsgn-rbndv2/` passes: the summary line reads `0 fail`.

<criterion id="RB7Z1-AC3" cell_refs="RV-z-1" judgment="true"/>
`RB7Z1-AC3` -- graded by the COO's drain read, then the CVO and Andrew (DEC-5), never self-graded: the real typecheck on the candidate adds no error over PROD's own baseline, the conflicts (if any) and their resolutions are printed in the record, and one Market Overview walk on the candidate build reads the same as on the feature branch. RECORD; no verdict.

<expected_criteria>RB7Z1-AC1, RB7Z1-AC2, RB7Z1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; the portal commits are the cherry-picks on the local candidate branch. NEVER push, never run `.tools/portal-merge-forward.sh`, never create a remote ref.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the check to pass.

<paths>
org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~22/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v7.md</decomp_doc> v7 @b729dc2880, cell `RV-z-1`.
<owned_cells>RV-z-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB7Z1-AC1, RB7Z1-AC2, RB7Z1-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~22/DSGN_RBNDV2.TO-RV-z-1.candidate-rehearsal.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB7Z1-AC1,RB7Z1-AC2,RB7Z1-AC3` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it). `RB7Z1-AC3` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming the COO's drain read and the CVO's grade (DEC-5).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W22-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v7 -- the only write is a local git branch in the portal repository named cand/laptop/dsgn-rbndv2-light and a record in this worker's deliverables folder; no other open order writes either; `origin/PROD` (33ad65ee) and `origin/DEV` (ad7c100b) read at the cut.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~22, queue position 1 of 1; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 22 --portal-ref feature/dsgn-rbndv2-light`. Ruling: CTO round-6 analysis section 2 (W19-S2) and item 1 of its enrichment list.

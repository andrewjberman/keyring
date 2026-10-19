# TO IRPT_ANLREQ.TO-AR-y-411.prod-based-recut-backoff-and-filing-hint-pair -- ONE branch cut from origin/PROD carrying the upload RESOLVING backoff (AR-y-410) and, if it still applies, the filing-hint equal-pair commit (AR-y-354), with the gates run as a delta against origin/PROD; a candidate, nothing landed or pushed

<to_id>IRPT_ANLREQ.TO-AR-y-411</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~305</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ71</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; a client-facing portal page; the worker lands and pushes NOTHING)
**Decomp cell:** `AR-y-411` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** `AR-y-410` (portal commit `c8fefec6909c`, merged to DEV at `10b6fd06fa89`); CTO msgs 10851 and 10855 (Andrew's order: built work ships to PROD)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~305`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-305` (branch `wk-IRPT_ANLREQ-305`), with a portal worktree `C:/dev/wk-irpt-anlreq-305/portal` (branch `wk-IRPT_ANLREQ-305-portal`) provisioned by the issuer AT `origin/PROD` (8cd45f623bdf). Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~305 <0.9.0_WK_IRPT_ANLREQ~305@opal.agent>" -F <msgfile> -- <paths>` (a commit can take up to 400 s: wait and check `git log` before retrying). The PORTAL source is committed INSIDE the portal worktree, which has no committer identity: for a cherry-pick or commit run `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~305" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~305@opal.agent" git -C C:/dev/wk-irpt-anlreq-305/portal ...` (and `--author "0.9.0_WK_IRPT_ANLREQ~305 <0.9.0_WK_IRPT_ANLREQ~305@opal.agent>"` on a commit; write no git config).
- Write every message file with the Write tool. APPEND rows only to `INVESTIGATION_v1.md` (0 deletions), class OBSERVATION, and COMMIT them. `surfaced_at` = `date -u +%FT%TZ`; a row id has the form `IRPT_ANLREQ-D2-W305-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: copy the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~300/IRPT_ANLREQ.TO-AR-y-410.upload-resolving-wait-bounded-backoff-four-minutes.proof_of_spec.json` (read it first; `git show HEAD:<path>` if absent); `controls.mutant` must FIRE and `controls.determinism` must really run. No live call, NO PUSH of any branch, no deploy. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree.

### THE CELL (`AR-y-411`, inlined)

*Context.* Andrew's order (relayed by the CTO, msgs 10851 and 10855): all the work from this device ships to PROD. Two portal candidates are built: (1) `cand/dell2/anlreq-upload-resolving-backoff`, ONE own commit `c8fefec6909c` on top of `origin/DEV` (the upload wait loop becomes a growing backoff of at most four minutes; files `src/pages/TicketCenter/analysisRequest.ts`, `src/pages/TicketCenter/TicketCenter.tsx`, `__tests__/analysis-request-repost.test.tsx`, `__tests__/upload-resolving-backoff.test.tsx`); it is on DEV (merge `10b6fd06fa89`). (2) `cand/dell2/anlreq-filing-hint-keep-equal-pair`, ONE own commit `f78ea50ef87d` (`feat(TicketCenter): C-FILING-HINT Keep posts the equal pair for the kept symbol (AR-y-354)`), cut from PROD and never landed on DEV. `origin/PROD` is `8cd45f623bdf`. The backoff commit was cut from DEV, so it may not apply to PROD without a conflict: PROD carries its own earlier version of `analysisRequest.ts`.

1. **Read first (record in `r58/CANDIDATES.json`, your deliverables folder):** in the portal worktree, for each of the two commits: `git show --stat <sha>`, whether `git cherry-pick -x --no-commit` applies onto `origin/PROD` cleanly (do it in a throwaway state and `git cherry-pick --abort` or `git reset --hard origin/PROD` after; a conflict prints its files), and for the filing-hint commit also whether its change is already present on PROD or DEV by content (`git cherry origin/PROD <sha>`, `git cherry origin/DEV <sha>`, and a grep of its added lines in the current `src/pages/TicketCenter/filing*` files). Print the verdicts.
2. **The recut.** Create the LOCAL branch `cand/dell2/anlreq-prod-recut-v3` at `origin/PROD` and apply, in this order: first `c8fefec6909c`, then `f78ea50ef87d`, each with `git cherry-pick -x <sha>`. On a conflict resolve it ONLY when the resolution adds no behaviour beyond the commit's own diff (the conflict hunks name the reason in the record). If `c8fefec6909c` cannot be applied without pulling in another DEV-only commit, STOP and file a BLOCKING row naming the DEV commit it needs (do not pull it in). If `f78ea50ef87d` is already on PROD or DEV by content, or cannot apply, or breaks a test the backoff commit passes, LEAVE IT OUT, name it with the reason in `r58/LEFT_OUT.json`, and go on with the backoff alone; never skip a single commit of a candidate that stays in.
3. **The payload check.** Write `r58/payload_check.py`. It prints for the recut against `origin/PROD`: the commit list (`git log --reverse --format='%h %an %s' origin/PROD..cand/dell2/anlreq-prod-recut-v3`), the file list (`git diff --name-status origin/PROD cand/dell2/anlreq-prod-recut-v3`), and then lines that must all read ABSENT: `ABSENT non-TicketCenter-path` (every changed path is under `src/pages/TicketCenter/`), `ABSENT trade-path-change` (no changed path matches `trade` case-insensitively), `ABSENT commentary-always` (no changed line makes `commentary_requested` a constant `true`), and `ABSENT UPLOAD_MAX_TRIES` (the string `UPLOAD_MAX_TRIES` and `UPLOAD_WAIT_MS` appear in no added or remaining line of the recut's `src/` tree: the backoff replaced them). A present item prints `PRESENT <what> <path or sha>` and the script exits 1; it ends with `PAYLOAD-OK <n> commits <m> files` only when every line is ABSENT.
4. **The gates.** In the portal worktree on the recut: `bun run typecheck`, `eslint` on every changed file, and `bun test src/pages/TicketCenter` for the recut AND for `origin/PROD` the same way in the same worktree (check out `origin/PROD` detached for the baseline, then return). The test gate is the DELTA: the set of failing test lines at the recut must EQUAL the set at `origin/PROD`, and the new backoff test file's cases must all pass (7 expected); a test file that errors to load at the recut but not at `origin/PROD` is named with its cause read. Do NOT run the vite build (the DT seat does at promote). Record each rc, count and the delta in `r58/GATES.json`.
5. **Record the head.** Print the full sha of `cand/dell2/anlreq-prod-recut-v3`, `git diff --stat origin/PROD <head>`, the applied commits (with their cherry-pick shas) and any left out. Never push.
6. **Write `r58/PROD_RECUT_V3_CANDIDATE.json`** in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~305/`: `base_sha`, `head`, `applied`, `left_out`, `files_changed`, `tests`, `claim`, `not_read` (the vite build, the rendered page, the live door's timing). Write the checker scripts named in ACCEPTANCE.
7. **In your report:** the head, the applied and left-out commits, the payload check output, the gates and the delta, the controls, the commit hashes, the rows filed.

### ACCEPTANCE

<criterion id="AR411-y-AC1" cell_refs="AR-y-411"><invocation>python C:/dev/wk-irpt-anlreq-305/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~305/r58/payload_check.py</invocation><expect>^PAYLOAD-OK </expect></criterion>
`AR411-y-AC1`: the payload check of step 3; it exits 0 and prints `PAYLOAD-OK <n> commits <m> files` only when every item reads ABSENT.

<criterion id="AR411-y-AC2" cell_refs="AR-y-411"><invocation>python C:/dev/wk-irpt-anlreq-305/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~305/r58/gates_check.py</invocation><expect>^GATES-OK </expect></criterion>
`AR411-y-AC2`: you write `gates_check.py`: it reads `r58/GATES.json` and re-runs `bun test src/pages/TicketCenter/__tests__/upload-resolving-backoff.test.tsx` in the portal worktree on the recut; it prints `GATES-OK typecheck 0 eslint 0 new-tests <n> passed failing-lines-equal-PROD <k> new-load-errors <e> explained` only when typecheck and eslint hold, the new cases pass, the failing test lines equal `origin/PROD`'s and every new load error is explained in `GATES.json`; otherwise `GATES-BAD <why>`, exit 1. Its control: with the backoff file temporarily swapped for `origin/PROD`'s version of `analysisRequest.ts` (restored with a sha256 check) the new test run must FAIL (`CONTROL-FIRES`).

<expected_criteria>AR411-y-AC1 AR411-y-AC2</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~305/` and this order's file (status flip only), and INSIDE the portal worktree: the LOCAL branch `cand/dell2/anlreq-prod-recut-v3` and the paths the two commits touch under `src/pages/TicketCenter/`.
- READ only: everything else. NO push of any branch.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-411</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~305/IRPT_ANLREQ.TO-AR-y-411.prod-based-recut-backoff-and-filing-hint-pair.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-411`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR411-y-AC1,AR411-y-AC2"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a portal candidate branch cut from PROD and its tests; nothing is called, landed or pushed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed; no live call.
comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the two commits and PROD's copy of analysisRequest.ts against the cell; the lens: the DEV overlap (the backoff commit was cut from DEV: a conflict that tempts a DEV-only commit in), the filing-hint commit already present by content, the old constants left behind, a test baseline taken in a different worktree state, a trade path or a constant commentary flag riding along. The cell requires only TicketCenter paths, no excluded behaviour, the failing-line set equal to PROD's, and a control that fires. NOT seen (blind): the vite build, the rendered page and the live door; denominator: 2 criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's msgs 10851 and 10855 (Andrew's order that built work ships): the single PROD release for the backoff plus the stray `AR-y-354`. This is the only cell cut since the pause of 17:13Z, ordered by the CTO. The PROD promote waits for `~V2`'s R20-PROD2 receipt (about 18:35Z) and for Andrew's records; the approval row for the recut is the issuer's next step after this cell. Base: the branch and the checkers are absent, so `AR411-y-AC1` and `AC2` FAIL as expected.

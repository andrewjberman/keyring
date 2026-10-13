# TO NFRA_DEVPLN.TO-DP-b-2 -- round 1 THREAD DP-b-2: `.tools/portal-merge-forward.sh`, the one approved route onto portal DEV

<to_id>NFRA_DEVPLN.TO-DP-b-2</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.9.0_WK_NFRA_DEVPLN~2</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-b-2` (`decompositions/NFRA_DEVPLN_DECOMP.round1.md`) | **outcome_ref:** FWD-1, FWD-3, FWD-4 |
**depends_on:** none (the approval reader it consumes has a pinned output line, tested here against a fixture)

---

## WORKER FACE

### THE CELL

Portal DEV is to be written by ONE script. A feature branch `cand/<box>/<slug>` reaches DEV only if its approval row is valid, and it lands as a MERGE commit (never a rebase) whose body
carries two trailers so anyone can tell which approved feature a DEV commit belongs to and who approved it. The row reader is `python .tools/open-calls.py approval-status --branch <b>`, built by
another cell at the same time; you do not have it. You consume its ONE output line, pinned:

`APPROVAL branch=<b> state=<ABSENT|OPEN|APPROVED|DECLINED|UNREADABLE> valid=<yes|no|-> row=<id|-> by=<who|-> head_sha=<sha|-> commits=<n|-> class=<client-facing|opal-internal|test-only|-> box=<box|-> pages=<p1,p2|->`

You call it as `${OPAL_APPROVAL_STATUS_CMD:-python .tools/open-calls.py approval-status} --branch <b>`; your tests set `OPAL_APPROVAL_STATUS_CMD` to a small fixture script that prints a chosen line.

### BUILD

`bash .tools/portal-merge-forward.sh <branch> [--repo <portal repo path, default portal>] [--push]` and `bash .tools/portal-merge-forward.sh --selftest`.

1. Resolve the workspace root with `git rev-parse --show-toplevel`; never type a device path. `<branch>` is read as `origin/<branch>`, else the local branch; neither: REFUSED `branch-not-found`.
2. Decide, in this order (fail closed: any doubt refuses):
   - the status command exits non-zero, prints no `APPROVAL` line, or prints `state=UNREADABLE`: REFUSED `status-unreadable`;
   - `state=ABSENT`: if EVERY path in `git diff --name-only origin/DEV...<branch>` matches the test-only pattern
     `(^|/)(__tests__|__harness__|__fixtures__|__mocks__)/|\.(test|spec)\.[cm]?[jt]sx?$|(^|/)(tests?|e2e|fixtures?)/` (and there is at least one path), proceed as class test-only with trailer `Approved-By: test-only @-`;
     otherwise REFUSED `no-approval-row`;
   - `state=OPEN`: REFUSED `not-approved`; `state=DECLINED`: REFUSED `declined`;
   - `state=APPROVED` with `valid=no` (or anything but `yes`): REFUSED `approver-not-valid`;
   - `state=APPROVED valid=yes` and `head_sha` is not the branch tip: REFUSED `stale-head`.
3. Merge in an EPHEMERAL worktree of the repo (`<workspace>/.runtmp/portal-mf-<UTC stamp>`, created off `origin/DEV`; the main portal tree is never touched, never left on another branch):
   `git merge --no-ff <branch>` with a message whose body ends with the two trailers `Feature: <branch>` and `Approved-By: <by> @<row>`. A conflict: `git merge --abort`, remove the worktree, REFUSED `conflict`.
   Never `git rebase`; never a force option anywhere in the script. The merge result is left on a local branch `mf/<slug>-<stamp>`; the worktree is removed in every path (a trap).
4. Without `--push`, nothing leaves the machine. With `--push`: `git push origin <merge commit>:DEV` plain (a non fast-forward is rejected by git; the script reports `pushed=no reason=push-rejected` and does nothing else).
5. Print ONE result line last: `MERGE-FORWARD branch=<b> result=MERGED|REFUSED reason=<token|-> dev_before=<sha|-> dev_after=<sha|-> pushed=yes|no`.
6. `--selftest` builds temporary repositories (a bare origin and a clone, with DEV, PROD and a branch cut from PROD) and a fixture status command, and ends with
   `MERGE-FORWARD-SELFTEST cases=<k>/<n> ok=True|False`. Cases: APPROVED valid=yes merges, with two parents, both trailers on the merge commit, `dev_before` the first parent; OPEN, DECLINED, `valid=no`, stale head,
   unreadable status and ABSENT-with-a-product-file each refuse and leave DEV unchanged; ABSENT with only test files merges with the test-only trailer; a conflicting branch refuses and leaves no worktree behind;
   `--push` to the temporary origin moves its DEV, and a second branch whose push would not fast-forward reports `push-rejected`.

### RULES FOR THIS CELL

Nothing you run pushes to the real portal origin, changes the real portal DEV, or leaves a worktree behind: tests use `mktemp -d` repositories and remove them. The real portal repo is read only (the AC2 call below
refuses before it creates anything). Git Bash default utilities only (no flock, pgrep, wget); resolve `jq` as `.tools/jq.exe` if you need it. No non-ASCII. Shellcheck-style hygiene: quote every expansion (a workspace path may contain a space).
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPb2-AC1" cell_refs="DP-b-2"><invocation>bash .tools/portal-merge-forward.sh --selftest</invocation><expect>ok=True</expect></criterion>
`DPb2-AC1` -- the full self-test above, every case passing.

<criterion id="DPb2-AC2" cell_refs="DP-b-2"><invocation>bash .tools/portal-merge-forward.sh cand/laptop/none-9 --repo portal</invocation><expect>MERGE-FORWARD branch=cand/laptop/none-9 result=REFUSED reason=branch-not-found</expect></criterion>
`DPb2-AC2` -- against the REAL portal repo: a branch that does not exist is refused before any worktree is made.

<criterion id="DPb2-AC3" cell_refs="DP-b-2"><invocation>grep -c -E "git[^#|]*(rebase|--force|--force-with-lease| -f )" .tools/portal-merge-forward.sh</invocation><expect>^0$</expect></criterion>
`DPb2-AC3` -- the script contains no rebase and no force option (comments excepted).
</proof_of_spec>

<expected_criteria>DPb2-AC1,DPb2-AC2,DPb2-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~2/NFRA_DEVPLN.TO-DP-b-2.portal-merge-forward.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPb2-AC1,DPb2-AC2,DPb2-AC3`, and flip `<status>` to `complete` only when every mechanical criterion passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round1.md</decomp_doc>
<owned_cells>DP-b-2</owned_cells>
</decomp_ref>

<paths>
.tools/portal-merge-forward.sh
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
comp-iam: DECLARED-NOT-APPLICABLE the cell touches no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_DEVPLN_PRD.md` v0.2 @d2b7385bee C-MERGE-FORWARD, C-CLASS, S02; ratified-text SIGNED by 3.0.0_SA_CVO~L (current). Issuer rulings R2, R3, R4, R5 in the decomposition. The real seam against `approval-status` is the issuer's act A4 at the drain.

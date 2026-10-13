# TO NFRA_DEVPLN.TO-DP-b-3 -- round 1 THREAD DP-b-3: the chosen-set release builder and the `/prod-deploy` chosen-set step

<to_id>NFRA_DEVPLN.TO-DP-b-3</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.9.0_WK_NFRA_DEVPLN~3</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-b-3` (`decompositions/NFRA_DEVPLN_DECOMP.round1.md`) | **outcome_ref:** FWD-5 |
**depends_on:** none (the approval reader it consumes has a pinned output line, tested here against a fixture)

---

## WORKER FACE

### THE CELL

Today `/prod-deploy` Step 4 runs `git merge --no-ff origin/DEV` in an ephemeral worktree cut from PROD, so a promote ships live DEV whole. The promote must instead take a LIST of approved feature branches, merge
only those into a release branch cut from PROD, and ship that branch. The row reader is `python .tools/open-calls.py approval-status --branch <b>`, built by another cell at the same time; you do not have it.
You consume its ONE output line, pinned:

`APPROVAL branch=<b> state=<ABSENT|OPEN|APPROVED|DECLINED|UNREADABLE> valid=<yes|no|-> row=<id|-> by=<who|-> head_sha=<sha|-> commits=<n|-> class=<client-facing|opal-internal|test-only|-> box=<box|-> pages=<p1,p2|->`

Call it as `${OPAL_APPROVAL_STATUS_CMD:-python .tools/open-calls.py approval-status} --branch <b>`; your tests set `OPAL_APPROVAL_STATUS_CMD` to a fixture script.

### BUILD

1. `bash .tools/portal-release-build.sh --features <b1,b2,...> [--repo <portal path, default portal>] [--prod-ref origin/PROD]` and `bash .tools/portal-release-build.sh --check <release-branch> [--repo ...] [--prod-ref ...]`
   and `bash .tools/portal-release-build.sh --selftest`. Derive the workspace root with `git rev-parse --show-toplevel`.
2. `--features`: for each branch (read as `origin/<b>`, else local; none: REFUSED `branch-not-found`), the row must read `state=APPROVED valid=yes`, `head_sha` equal to the branch tip, and `commits` equal to
   `git rev-list --count <prod-ref>..<branch>`. A refusal names the branch and one reason token: `not-approved`, `declined`, `approver-not-valid`, `stale-head`, `commits-differ`, `status-unreadable`.
   Any refusal refuses the whole release and nothing is created. Otherwise, in an EPHEMERAL worktree (`<workspace>/.runtmp/portal-release-<UTC stamp>`, removed on every path by a trap) cut from `<prod-ref>`, create the
   branch `release/<UTC stamp>` and merge each feature with `git merge --no-ff`, the message body ending `Feature: <branch>` and `Approved-By: <by> @<row>`. A conflict: abort, remove, REFUSED `conflict`.
   Never `git rebase`; no force option anywhere; the script never pushes.
3. The check (run after the merges, and alone via `--check`): `git rev-list --first-parent <prod-ref>..<release>` is the walk (the release's own merge commits; a feature branch's commits sit under its second parent
   and carry no trailer, so a plain walk would refuse every honest release). Count the commits in that walk whose message has no `Approved-By:` trailer. Print
   `RELEASE-CHECK features=<n> first_parent_commits=<t> unapproved=<u>`. A release with `u` above 0 is REFUSED `unapproved-commits`.
4. Print the promote list the person running the promote reads, one line per feature: `PROMOTE-LIST branch=<b> class=<c> by=<who> row=<id> pages=<p1,p2>`, then
   `PROMOTE-CLIENT-FACING count=<n>` (features whose class is client-facing; the push law makes that promote wait on Andrew's word), then the last line
   `RELEASE result=READY|REFUSED reason=<token|-> branch=<name|-> base=<prod sha|-> head=<sha|->`.
5. `--selftest` builds temporary repositories (a bare origin and a clone, PROD, DEV, and feature branches cut from PROD) and a fixture status command; last line
   `RELEASE-SELFTEST cases=<k>/<n> ok=True|False`. Cases: two approved features build a release with `unapproved=0`; one unapproved (OPEN) feature among two refuses the whole release and no branch is created;
   a stale head, a `valid=no` row and a `commits-differ` row each refuse; a feature cut from DEV carries extra commits and refuses `commits-differ`; `--check` on a release with one extra plain untrailered commit
   on its first-parent line reads `unapproved=1` and refuses; an unapproved change left on the temporary DEV is NOT on the release.
6. `.claude/skills/prod-deploy/SKILL.md`: in Step 4, replace the `git merge --no-ff origin/DEV` command and the commit message line with the chosen-set route: run `bash .tools/portal-release-build.sh --features <list>`,
   take the printed release branch, keep the parity gate as `git diff <release-branch> HEAD` (empty = OK), and push as before. In Step 0, change the two freeze bullets that say the promote merges LIVE `origin/DEV` at GO time
   so they say the promote ships the named list and DEV at GO time no longer rides in. Add to the promote receipt the `PROMOTE-LIST` lines. Change nothing else in the file (the DT-only check, the push law, Steps 1-3, 5-8 and the abort path stay).

### RULES FOR THIS CELL

Nothing you run pushes, or changes the real portal's DEV, PROD or main tree, or leaves a worktree behind: tests use `mktemp -d` repositories. The real portal repo is read only (AC2 refuses before it creates anything).
Git Bash default utilities only; quote every expansion. No non-ASCII in any file.
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-W3-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPb3-AC1" cell_refs="DP-b-3"><invocation>bash .tools/portal-release-build.sh --selftest</invocation><expect>ok=True</expect></criterion>
`DPb3-AC1` -- the full self-test above, every case passing.

<criterion id="DPb3-AC2" cell_refs="DP-b-3"><invocation>bash .tools/portal-release-build.sh --features cand/laptop/none-9 --repo portal</invocation><expect>RELEASE result=REFUSED reason=branch-not-found</expect></criterion>
`DPb3-AC2` -- against the REAL portal repo: a branch that does not exist refuses the release before any worktree exists.

<criterion id="DPb3-AC3" cell_refs="DP-b-3"><invocation>grep -h -c -F "merge --no-ff origin/DEV" .claude/skills/prod-*/SKILL.md</invocation><expect>^0$</expect></criterion>
`DPb3-AC3` -- the skill no longer merges live DEV whole.
</proof_of_spec>

<expected_criteria>DPb3-AC1,DPb3-AC2,DPb3-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~3/NFRA_DEVPLN.TO-DP-b-3.chosen-set-release.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPb3-AC1,DPb3-AC2,DPb3-AC3`, and flip `<status>` to `complete` only when every mechanical criterion passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round1.md</decomp_doc>
<owned_cells>DP-b-3</owned_cells>
</decomp_ref>

<paths>
.tools/portal-release-build.sh
.claude/skills/prod-deploy/SKILL.md
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

Source: PRD `prd/NFRA_DEVPLN_PRD.md` v0.2 @d2b7385bee C-PROMOTE, S04; ratified-text SIGNED by 3.0.0_SA_CVO~L (current). Issuer rulings R1 (first-parent walk), R2, R3, R5 in the decomposition; the R1 reading is raised to the CTO as a surprise row.

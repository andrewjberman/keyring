# TO NFRA_DEVPLN.TO-DP-e-3 -- round 4 ENRICHMENT DP-e-3: the merge-forward's changed-file read no longer prints git's `multiple merge bases` warning

<to_id>NFRA_DEVPLN.TO-DP-e-3</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.9.0_WK_NFRA_DEVPLN~2</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>ENRICHMENT</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-e-3` (`decompositions/NFRA_DEVPLN_DECOMP.round4.md`) | **outcome_ref:** FWD-3 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`.tools/portal-merge-forward.sh` lists the files a branch changes with a three-dot diff (`git diff --name-only origin/DEV...<branch>`) to decide whether a branch with no approval row is a test-only change. When the branch and DEV have MORE THAN ONE merge base, git prints `warning: ... multiple merge bases, using <sha>` on stderr and picks one. MEASURED: `bash .tools/portal-merge-forward.sh cand/laptop/local-only-probe --repo portal` prints `warning: refs/remotes/origin/DEV...refs/heads/cand/laptop/local-only-probe: multiple merge bases, using 63c4f9e3...` (git picked one of two bases). The verdict was right, but the noise hides real stderr, and git's pick of a base should not be left to chance when the decision is "is EVERY changed path a test path".
The portal checkout in your worktree is a linked worktree of the real portal repository (read only for you; do not fetch).

### BUILD

In `.tools/portal-merge-forward.sh`, replace the three-dot `git diff --name-only <DEV>...<branch>` with a read that does not depend on git's choice among several merge bases and prints no such warning. Required meaning: the set of paths the BRANCH changes relative to its history not on DEV, computed so that, with several merge bases, a path changed on the branch against ANY merge base is included (the safe, wider set for a test-only decision). One acceptable form: take every merge base from `git merge-base --all <DEV> <branch>`, union `git diff --name-only <base> <branch>` over them. State in a comment why. Where there is exactly one base the result must equal the old three-dot result. Add one self-test case in the temporary repositories that builds a branch with two merge bases (a criss-cross: two branches that merge each other, then a branch off one of them) and asserts (a) no `multiple merge bases` text on stderr and (b) a product file changed after the first base is still seen (so an ABSENT row is refused `no-approval-row`, not treated as test-only). Every existing case stays; update only the selftest case count.

### RULES FOR THIS CELL

Nothing you run pushes, or changes the real portal's DEV, PROD or main tree: tests use `mktemp -d` repositories. Git Bash default utilities only; quote every expansion. No non-ASCII. Do not put `MSYS_NO_PATHCONV=1` on a command that takes an absolute path argument. Never hide stderr with `2>/dev/null` on a read whose emptiness carries a verdict.
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-W2-S<k>`, next unused k after the highest `W2-S` in the file, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPe3-AC1" cell_refs="DP-e-3"><invocation>bash .tools/portal-merge-forward.sh --selftest</invocation><expect>ok=True</expect></criterion>
`DPe3-AC1` -- the self-test, every case (old and the new criss-cross case) passing.

<criterion id="DPe3-AC2" cell_refs="DP-e-3"><invocation>bash -c 'bash .tools/portal-merge-forward.sh cand/laptop/local-only-probe --repo portal --no-fetch 2>&amp;1 | grep -c "multiple merge bases"'</invocation><expect>^0$</expect></criterion>
`DPe3-AC2` -- the seam against the REAL portal repo and the real local-only branch: the warning count is 0 (it is 1 at the base).
</proof_of_spec>

<expected_criteria>DPe3-AC1,DPe3-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~2/NFRA_DEVPLN.TO-DP-e-3.merge-base-warning.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPe3-AC1,DPe3-AC2`, and flip `<status>` to `complete` only when every mechanical criterion passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round4.md</decomp_doc>
<owned_cells>DP-e-3</owned_cells>
</decomp_ref>

<paths>
.tools/portal-merge-forward.sh
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-e-3.merge-base-warning.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE the cell touches no IAM.
comp-adversary: RUN over the cell's own invocations; BLIND to the filesystem around the cited paths. Finding inlined: the replacement must be the WIDER set across merge bases, or a product change made after the first base could read as test-only.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `ledger/ROUND_ANALYSIS.round3.md` @75335735b6 item 4 (row W2-S10); row W2-S9 is not repaired (the local fallback is already the stale-safe ref). Portal worktree: this order needs `--portal-ref` at the spawn.

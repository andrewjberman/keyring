# TO NFRA_CTLPLN.TO-CT-ag-1 -- workstream CLEANUP round 2 (cell CT-ag-1): worktree_gc preserves a dirty merged worktree before removing it, and counts only `git status --porcelain` as dirt (CTO round-16 rulings 1-2, rows W100-S1 and W100-S2)

<to_id>NFRA_CTLPLN.TO-CT-ag-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~103</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>CLEANUP</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ag-1` (`decompositions/NFRA_CTLPLN_DECOMP.round17.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Round 16 (`CT-af-1`, merge `e2720105d5`) gave `.tools/worktree_gc.py` an own-commit test, the class `UNSTARTED` and the verb `--check-removable <path>`. Read its docstring (lines 1-60), `classify` and `check_removable`, and rows `NFRA_CTLPLN-W100-S1` and `NFRA_CTLPLN-W100-S2` (Grep the ids in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`). Two rulings by the CTO (`ledger/ROUND_ANALYSIS.round16.md` section 2) are to be built:

- **Ruling 2 (W100-S2):** gitignored paths are not dirt. `--check-removable` refused every worktree that had run the repository's tests, because they leave ignored files (`.comp-graph/`, `.scratch/`, `org/mcp/*.log`). Dirt means `git status --porcelain` lines only (tracked changes and untracked non-ignored files), exactly as the CTO defined it.
- **Ruling 1 (W100-S1):** Andrew's standing word is that a merged worktree is removed (2026-10-08 ~23:0xZ: "Force-removing merged worktrees is mandatory"). A merged worktree with dirt is still removed, but never bare: first its dirt is committed to a new branch `preserve/<branch>-<stamp>`, the sha is printed, and only then is the worktree removed.

### BUILD

1. **Porcelain-only dirt.** In `classify` and `check_removable`, dirt = the non-ignored lines of `git status --porcelain --untracked-files=all`. Ignored paths (all of them, cache or not) no longer count: a merged worktree (own >= 1) with an empty porcelain is CLEAN and `--check-removable` says `REMOVABLE`. Remove the extra ignored-path refusal. `CACHE_RX` may stay for any other use.
2. **The preserve step**, a function `preserve_dirt(path, branch) -> (ok, sha_or_reason)`. Use PLUMBING on a TEMPORARY index so no hook runs and the worktree's own index is not touched: `GIT_INDEX_FILE=<temp file>`, `git read-tree HEAD`, `git add -A` (run in the worktree; `.gitignore` is honoured, so ignored files are excluded), `git write-tree`, `git commit-tree <tree> -p HEAD` with an explicit identity through `-c user.name=worktree_gc -c user.email=worktree_gc@opal.agent` (never edit git config), a message naming the source branch, path, stamp and the count of preserved paths, then `git update-ref refs/heads/preserve/<branch>-<stamp> <commit>`. `<stamp>` is UTC `YYYYMMDDTHHMMSSZ`; a branch name already taken gets a numeric suffix. The step FAILS CLOSED: any git error returns `(False, reason)` and the worktree is NOT removed. A worktree whose porcelain is empty gets NO preserve branch.
3. **`--go`** (the MERGED class: merged, own >= 1, porcelain dirt, idle past the clean window): call `preserve_dirt` first, print `PRESERVED <branch> -> preserve/<branch>-<stamp> <sha> (<n> path(s))`, then remove with `git worktree remove --force` as today. A preserve failure prints `PRESERVE-FAILED <reason>`, removes nothing, counts as failed in the SUMMARY. The audit line carries the preserve sha. CLEAN worktrees are removed without force and without a preserve branch, as today. `UNSTARTED`, `HELD`, `ESCALATE`, `ACTIVE`, `SKIP` and `PRUNABLE` are unchanged.
4. **`--check-removable`** prints `REMOVABLE-AFTER-PRESERVE MERGED own=<n>; <k> path(s) would be preserved` (exit 0) for a merged own >= 1 worktree with porcelain dirt, `REMOVABLE CLEAN ...` (exit 0) for a clean one, and keeps every NOT-REMOVABLE reading of round 16 (UNSTARTED, not merged, locked, drain-*, in use, unknown own). It still removes and preserves nothing.
5. **`--only <path>`** (new): restricts `--go` AND the dry run to the one linked worktree at `<path>`; every other worktree is neither classified for removal nor touched, and the SUMMARY says `--only`. A path that is not a linked worktree of the repository is exit 2. This is what makes a real run against the real repository safe.
6. Update `--selftest` and `.tools/tests/test_worktree_gc_own_commit.py` so they stay valid: arm (d) of that test (a dirty merged tree) now expects `REMOVABLE-AFTER-PRESERVE`; add an arm for an ignored-only merged tree reading `REMOVABLE`. Keep every other arm.
7. A NEW test `.tools/tests/test_worktree_gc_preserve.py` (standard library, temporary repositories only, no AWS, no network, never the real repository's worktrees; stub the running-process read so no fixture is named in use). Arms: (a) a planted merged tree with one modified tracked file, one new untracked file and one ignored file: `--check-removable` prints `REMOVABLE-AFTER-PRESERVE`; `--go --only <path>` prints `PRESERVED`, the directory is gone, branch `preserve/<branch>-<stamp>` exists at the printed sha, `git show <sha>:<tracked file>` and `git show <sha>:<untracked file>` return the dirty content, and the ignored file is NOT in the preserve tree; both verbs agree (the CVO's done-when); (b) a clean merged tree: `REMOVABLE`, removed, no `preserve/` branch; (c) an ignored-only merged tree: `REMOVABLE`, removed, no `preserve/` branch; (d) NEGATIVE CONTROL: a dirty tree at its issuance commit (UNSTARTED): `NOT-REMOVABLE`, not removed, no `preserve/` branch; (e) a dirty tree with an own commit NOT in the trunk: not removed, no `preserve/` branch; (f) preserve failure injected (pre-create a ref that makes `update-ref` fail, or an unwritable temporary index path): `PRESERVE-FAILED`, the worktree still exists with its dirt; (g) `--only A` with two removable trees A and B: only A is removed; (h) a path that is not a worktree: exit 2. Final line `WORKTREE-GC-PRESERVE arms=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. Every experiment runs in a temporary repository. Never run `worktree_gc.py --go` without `--only` and never against the real repository: the real repository's worktrees are other seats' work. The plain dry run (`python .tools/worktree_gc.py`) against the real repository is allowed. No aws, no network, no push. `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink. ASCII only; Python 3.12. CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~102/NFRA_CTLPLN.TO-CT-af-3.placement-refusal-unstages-all.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W103-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. YOUR WORKTREE IS A SPARSE CHECKOUT (the first real trial of the CTO's sparse-worker ruling): it holds `.tools/`, `lib/`, the project's tree folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/ref/`, `docs/doctrine/` and the root files. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder in your final report (this is data for the next cell).

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTag1-AC1" cell_refs="CT-ag-1"><invocation>python .tools/tests/test_worktree_gc_preserve.py</invocation><expect>ok=True</expect></criterion>
`CTag1-AC1` -- every arm passes, including the planted dirty merged tree whose file is read back at the preserve sha and the negative control (base: the file does not exist); report the whole last line with its denominator.

<criterion id="CTag1-AC2" cell_refs="CT-ag-1"><invocation>python .tools/tests/test_worktree_gc_own_commit.py</invocation><expect>ok=True</expect></criterion>
`CTag1-AC2` -- the round-16 suite still passes with its dirty-merged arm now expecting `REMOVABLE-AFTER-PRESERVE` (base: `WORKTREE-GC-OWN-COMMIT arms=8/8 ok=True`, a control; the count may grow); report the whole last line.

<criterion id="CTag1-AC3" cell_refs="CT-ag-1"><invocation>python .tools/worktree_gc.py --selftest</invocation><expect>ok=True</expect></criterion>
`CTag1-AC3` -- the tool's own self-test still passes (base: `WORKTREE-GC-SELFTEST cases=3/3 ok=True`, a control; the count may grow); report the whole last line.
</proof_of_spec>

<expected_criteria>CTag1-AC1,CTag1-AC2,CTag1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 240`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~103/NFRA_CTLPLN.TO-CT-ag-1.worktree-gc-preserve-and-porcelain-dirt.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTag1-AC1,CTag1-AC2,CTag1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round17.md</decomp_doc>
<owned_cells>CT-ag-1</owned_cells>
</decomp_ref>

<paths>
.tools/worktree_gc.py
.tools/tests/test_worktree_gc_preserve.py
.tools/tests/test_worktree_gc_own_commit.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing; the tool's own scheduled run (if any) is not touched.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a dirty tree removed without its dirt preserved (arm a reads the file back at the sha; arm f injects a failure and requires the tree to survive); an ignored file preserved into a commit (arm a: absent from the preserve tree); an unstarted worker's dirt removed (arm d); `--go` widened to a worktree it was not pointed at (arm g, and `--only` is the only way the issuer runs it for real); the preserve step running a hook or changing the worktree's index (plumbing on a temporary index); BLIND: a very large untracked tree (a node_modules link or a build output not ignored) swallowed into a commit by `git add -A`, which the arms do not exercise (the worker reports what the step does for a file over 50 MB and for a symlink or junction, and whether it needs a size cap).
risk: LOCAL -- temporary repositories only; the real-repository use is the read-only dry run. The issuer's one real `--go --only` follows at close.
lane: the <paths> block IS the grant (worker RULING 1). `.tools/worktree_gc.py` is `0.0.0_AB_MSTR`'s tool; the CTO ruled the change (W100-S1 ruled (c), msg 109361) and MSTR runs it dry-first.
</preflight>

Base checks, dry-run by the issuer before the cut: CTag1-AC1 base: FAIL as expected (the file does not exist); CTag1-AC2 and CTag1-AC3 base: controls (`WORKTREE-GC-OWN-COMMIT arms=8/8`, `WORKTREE-GC-SELFTEST cases=3/3`), see the issuer's dry-run note in the issuance commit.
Source: CTO round-16 analysis rulings 1-2 and section 3 item 1 (`ledger/ROUND_ANALYSIS.round16.md` @f62974941f); msg 109361; rows W100-S1, W100-S2.

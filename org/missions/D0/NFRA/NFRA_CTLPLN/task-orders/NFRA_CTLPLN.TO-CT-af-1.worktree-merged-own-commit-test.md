# TO NFRA_CTLPLN.TO-CT-af-1 -- workstream CLEANUP round 1 (cell CT-af-1): a worktree counts as merged only when its branch carries a commit of its own; a branch at its issuance commit is never removed (CTO round-15 ruling 1, msg 109345)

<to_id>NFRA_CTLPLN.TO-CT-af-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~100</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>CLEANUP</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-af-1` (`decompositions/NFRA_CTLPLN_DECOMP.round16.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`.tools/worktree_gc.py` is the worktree garbage collector (read its docstring, lines 1-45, and `classify`, about :143-225). It treats a worktree as MERGED or CLEAN when its HEAD is contained in the trunk or in a box branch (about :181-187). A worker's branch is cut at the issuance commit, which the trunk already contains. So a worker that was cut off before its first commit has HEAD = the issuance commit, reads as merged, and `--go` removes the worktree, and with it any uncommitted file. That happened on 2026-10-15 (the worktree `ctlpln-97` and one uncommitted test file were lost). The CTO's ruling: "merged" means the branch carries **at least one commit of its own, and every one is in the trunk**. A branch with no commit of its own is NOT merged (it is unstarted or in progress). This cell puts that test into the tool and adds the verb the drain uses before any removal.

### BUILD

1. In `classify`, compute `own` = the number of commits reachable from HEAD and not reachable from the branch's CREATION POINT. Read the creation point from the branch's reflog: the OLDEST entry of `git reflog show --format=%H <branch>` (the new-value of its first entry; `git worktree add -b` writes `branch: Created from <sha>`). Fail closed: a detached HEAD, a missing or empty reflog, or any git error means `own` is UNKNOWN and the worktree is never CLEAN or MERGED.
2. A worktree with `own == 0` (and one with `own` unknown) gets a new class `UNSTARTED` (reason names `own=0` or `own=unknown`). `--go` never removes it, whether its tree is clean or dirty. `UNSTARTED` appears in the SUMMARY line and in the per-class counts like the other classes. CLEAN and MERGED require `own >= 1` and HEAD contained in the trunk or a box branch, exactly as today. ACTIVE, SKIP (locked, `drain-*`, IN USE), PRUNABLE, HELD and ESCALATE are unchanged.
3. A NEW verb `python .tools/worktree_gc.py --check-removable <worktree path>`: it applies the drain's test to ONE worktree, ignoring the idle window (the drain calls it the moment a merge lands). It prints one line, `REMOVABLE <class> <reason>` or `NOT-REMOVABLE <class> <reason>`, and exits 0 for REMOVABLE and 1 for NOT-REMOVABLE (2 for a path that is not a linked worktree of this repository). REMOVABLE only when ALL hold: `own >= 1`; HEAD is contained in the trunk (local or origin) or a box branch; `git status --porcelain` is empty; the path is not locked, not a `drain-*` worktree and not named by a running process. It removes nothing.
4. Leave `--go`'s MERGED class (merged, own >= 1, dirty, idle 24 hours: force-removed) as it is today (Andrew's standing word, 2026-10-08 ~23:0xZ: "Force-removing merged worktrees is mandatory"). The CTO's ruling also says a dirty worktree is never removed; the two read against each other for that one class. Do NOT resolve it: apply the dirty test to `--check-removable` only, and file one surprise row stating this choice.
5. Update `--selftest` so its fixtures stay valid: its "merged" worktrees must carry an own commit (add one and merge it), and add the arms below. Keep every existing arm.
6. A NEW test `.tools/tests/test_worktree_gc_own_commit.py` (standard library, temporary repositories only; it imports or runs `worktree_gc.py` by path; no AWS, no network, never the real repository's worktrees). Build a temp repository with a trunk branch `CLOUD` and linked worktrees, each branch created with `git worktree add -b`, `--clean-hours 0` on `--go`, and a stub for the running-process read so no real process names a fixture. Arms: (a) NEGATIVE CONTROL: a branch at its issuance commit (trunk contains it), tree clean: `--check-removable` prints `NOT-REMOVABLE UNSTARTED`, exit 1, and `--go` leaves the directory in place; (b) the same, tree dirty (one uncommitted file): NOT-REMOVABLE, and after `--go` the directory and the file still exist; (c) one own commit merged into the trunk, clean: `REMOVABLE`, exit 0, and `--go` removes it; (d) one own commit merged, dirty: `--check-removable` says NOT-REMOVABLE; (e) one own commit NOT in the trunk, clean: NOT-REMOVABLE and `--go` keeps it; (f) detached HEAD at a trunk commit: NOT-REMOVABLE (own unknown); (g) the branch's reflog file deleted: NOT-REMOVABLE (fail closed); (h) a path that is not a worktree: exit 2. Final line `WORKTREE-GC-OWN-COMMIT arms=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. Every experiment runs in a temporary repository. Never run `worktree_gc.py --go` against the real repository, and never remove, lock or touch a real worktree: the real repository's worktrees are other seats' work. Plain `python .tools/worktree_gc.py` (the dry run) against the real repository is allowed and prints nothing destructive. No aws, no network, no push. `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink. ASCII only; Python 3.12. CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes: an unfinished cell with no commit of its own can be lost to a cleanup or a cut-off. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~99/NFRA_CTLPLN.TO-CT-ae-3.batch-repair-round14-rows.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W100-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTaf1-AC1" cell_refs="CT-af-1"><invocation>python .tools/tests/test_worktree_gc_own_commit.py</invocation><expect>ok=True</expect></criterion>
`CTaf1-AC1` -- every arm passes, including the negative control at the issuance commit (base: the file does not exist); report the whole last line with its denominator.

<criterion id="CTaf1-AC2" cell_refs="CT-af-1"><invocation>python .tools/worktree_gc.py --selftest</invocation><expect>ok=True</expect></criterion>
`CTaf1-AC2` -- the tool's own self-test still passes with the own-commit fixtures (base: `WORKTREE-GC-SELFTEST cases=3/3 ok=True`, a control; the case count may grow); report the whole last line.

<criterion id="CTaf1-AC3" cell_refs="CT-af-1"><invocation>python .tools/worktree_gc.py</invocation><expect>UNSTARTED=</expect></criterion>
`CTaf1-AC3` -- the dry run still reads the real repository and prints its SUMMARY line, now including the UNSTARTED count (base: FAIL as expected, the SUMMARY line has no `UNSTARTED=` field); report the whole SUMMARY line.
</proof_of_spec>

<expected_criteria>CTaf1-AC1,CTaf1-AC2,CTaf1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 240`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~100/NFRA_CTLPLN.TO-CT-af-1.worktree-merged-own-commit-test.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTaf1-AC1,CTaf1-AC2,CTaf1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round16.md</decomp_doc>
<owned_cells>CT-af-1</owned_cells>
</decomp_ref>

<paths>
.tools/worktree_gc.py
.tools/tests/test_worktree_gc_own_commit.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing; the tool's own scheduled run (if any) is not touched.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a real worktree removed by an experiment (every arm runs on a temporary repository; `--go` is never run on the real one); an unstarted worker's tree removed (arms a and b); a dirty merged tree reported removable (arm d); an unknown own count read as merged (arms f and g, fail closed); the existing MERGED class weakened for a worktree that has an own commit (the selftest keeps its merged+dirty arm); BLIND: a branch whose reflog was expired or created by `git branch` before the worktree, so the creation point is not the issuance commit (the worker reports which creation forms the reflog read handles and what it does for the rest: fail closed).
risk: LOCAL -- temporary repositories only; the tool's real-repository use is the read-only dry run.
lane: the <paths> block IS the grant (worker RULING 1). `.tools/worktree_gc.py` is `0.0.0_AB_MSTR`'s tool; the CTO named it in scope (msg 109345, 2026-10-15 ~06:03Z) and MSTR runs it dry-first until this lands.
</preflight>

Base checks, dry-run by the issuer before the cut: CTaf1-AC1 base: FAIL as expected (the file does not exist); CTaf1-AC2 base: `WORKTREE-GC-SELFTEST cases=3/3 ok=True` (a control); CTaf1-AC3 base: FAIL as expected (the SUMMARY line prints without an `UNSTARTED=` field).
Source: CTO round-15 analysis ruling 1 and section 4 item 1 (`ledger/ROUND_ANALYSIS.round15.md` @0be7eb664c); CTO msg 109345; the loss of `ctlpln-97` (inputs D2).

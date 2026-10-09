# TO NFRA_CTLPLN.TO-CT-t-5 -- round 6 THREAD CT-t-5: box-sync merge conflicts per shared file and per box, with the writers named

<to_id>NFRA_CTLPLN.TO-CT-t-5</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~55</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-t-5` (`decompositions/NFRA_CTLPLN_DECOMP.thread6.md`) | **outcome_ref:** FWD-8 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-8: two boxes never edit the same file at the same time. The analysis: the write half is built, but real multi-box work shows
merge conflicts on shared files, which `.tools/box-sync.sh` and `.tools/merge-resolve-known.py` now resolve automatically, and no
conflict-free parallel round has been read. Read both tools for how a resolved conflict is recorded (a log file, a line in the
merge commit message, or the audit log `box-sync` writes). The census is the input to the next round's move of each conflicting
writer onto a per-box file.

### BUILD

1. `.tools/box-sync-conflicts.py [--since <UTC>] [--fetch]`. Over the integrator's merges into `origin/CLOUD` in the window (author
   `0.0.0_AB_MSTR`, read the subject form from `box-sync.sh`), list each merge that resolved or met a conflict. Use the record
   `box-sync.sh` / `merge-resolve-known.py` leaves; where none exists, re-run the merge read-only with `git merge-tree` on the two
   parents and list the conflicted paths. For each conflicted path, give the boxes whose branches changed it since the merge base,
   the last authors on each side, and the resolution class `merge-resolve-known.py` applied (or `UNRESOLVED`).
   LAST line: `BOX-SYNC-CONFLICTS merges=<n> conflicted_merges=<c> paths=<p> top=<path:count,...>`.
2. `--selftest` on a temporary repository with two box branches editing one file and one per-box file:
   - the shared file is listed with both boxes;
   - the per-box file is not listed;
   - a clean merge lists nothing.
   LAST line: `BOX-SYNC-CONFLICTS-SELFTEST cases=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

**Nothing you run changes the live fabric.** You do not start, stop or message any seat. You do not push, merge or rebase. You run
no `terraform` against a backend and no `aws` call. You send nothing on the agent bus. Reads of git refs (`git log`, `git show`,
`git for-each-ref`, including `origin/box/*` and `origin/CLOUD` after one `git fetch`) are allowed. Tests run in temporary
directories or temporary git repositories. The law files `CLAUDE.md` and `org/XXX.md` are LOCKED. `.claude/settings.json` is in
no grant. No non-ASCII in any file you write. Python: standard library only; ruff clean. The device register is read only through
`lib/devices.py`; no tool types a box name, a serial of a particular box, or a path under a user's home.
FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to
`org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W<slot>-S<k>`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTt5-AC1" cell_refs="CT-t-5"><invocation>python .tools/box-sync-conflicts.py --selftest</invocation><expect>BOX-SYNC-CONFLICTS-SELFTEST cases=</expect></criterion>
`CTt5-AC1` -- every case passing; the line reads `ok=True`.

<criterion id="CTt5-AC2" cell_refs="CT-t-5"><invocation>python .tools/box-sync-conflicts.py --since 2026-10-08T00:00:00Z --fetch</invocation><expect>BOX-SYNC-CONFLICTS merges=</expect></criterion>
`CTt5-AC2` -- the real census since the per-box branches began. The issuer reads `top` at the drain; it is the next round's input.
</proof_of_spec>

<expected_criteria>CTt5-AC1,CTt5-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~55/NFRA_CTLPLN.TO-CT-t-5.box-sync-conflicts.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> CTt5-AC1,CTt5-AC2`, and flip `<status>` to `complete` only when every mechanical criterion
passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.thread6.md</decomp_doc>
<owned_cells>CT-t-5</owned_cells>
</decomp_ref>

<paths>
.tools/box-sync-conflicts.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a resolved conflict read as no conflict (the record, or a `git merge-tree` re-run, is the source); a per-box file read as shared (only paths both sides changed); the census writing anything (it reads); BLIND: conflicts a seat resolved by hand before the integrator ran.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: L10 round analysis `org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.20261009.md` @333d2b37b3 (1.0.0_SA_CTO msg 107787); PRD `prd/NFRA_CTLPLN_PRD.md` v0.22 @333d2b37b3, ratified-text SIGNED (current).

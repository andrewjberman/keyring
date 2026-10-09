# TO NFRA_CTLPLN.TO-CT-t-4 -- round 6 THREAD CT-t-4: one day of each box manager's record read for project rulings, for the reviewer to judge

<to_id>NFRA_CTLPLN.TO-CT-t-4</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~54</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-t-4` (`decompositions/NFRA_CTLPLN_DECOMP.thread6.md`) | **outcome_ref:** FWD-21 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-21: the fabric manager on every box keeps its fabric running without being asked, and decides nothing about any project. The
analysis: "a judged read of a manager's day for project rulings" is not on record, and was never written as a JUDGMENT criterion, so
the round-close check could not ask for it. The tool exists: `.tools/mstr-record-check.py --serial <s> --since <UTC> --until <UTC>`
lists anything in a manager's day that looks like a project ruling, for a reviewer to judge. The four managers are
`0.0.0_AB_MSTR` (laptop) and the `~` lanes the register or the recent `box-sync` commits name for sitez, dell1 and dell2. Read the
lane names; do not type them from this text.

### BUILD

1. Find each box's manager serial from the register (`lib/devices.py`) or, if the register does not carry it, from the authors
   of the last 24 hours of `origin/box/<box>` commits whose subject begins `box-sync` or `grant(`. Print where each came from.
2. For each, run `.tools/mstr-record-check.py --serial <s> --since 2026-10-08T07:00:00Z --until 2026-10-09T07:00:00Z`. Run it once per
   box ref where its record lives: if the tool reads only the main worktree, run it against a temporary worktree of `origin/box/<box>`
   by `--repo`. Capture each full output.
3. Write `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~54/MANAGER_DAY_READ_20261009.md`. Per manager, give
   the serial and box, where the serial came from, the window, the tool's full listing, and the count. Per listed item, give the
   commit or message, one quoted line, and the file it touched. Add no verdict. The reviewer judges.

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
<criterion id="CTt4-AC1" cell_refs="CT-t-4"><invocation>python .tools/mstr-record-check.py --selftest</invocation><expect>MSTR-RECORD-SELFTEST</expect></criterion>
`CTt4-AC1` -- the tool still passes its own test before it is used (`ok=True`).

<criterion id="CTt4-AC2" cell_refs="CT-t-4" judgment="true"/>
`CTt4-AC2` -- JUDGMENT (graded by 3.0.0_SA_CVO at L9, never by the worker): over the four managers' day in `MANAGER_DAY_READ_20261009.md`, no item is a ruling on a project's specification, decomposition, grade or scope. Each listed item reads as a fabric act (spawn, kill, re-seat, relay, integrate, grant).
</proof_of_spec>

<expected_criteria>CTt4-AC1,CTt4-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~54/NFRA_CTLPLN.TO-CT-t-4.manager-day-read.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> CTt4-AC1,CTt4-AC2`, and flip `<status>` to `complete` only when every mechanical criterion
passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.thread6.md</decomp_doc>
<owned_cells>CT-t-4</owned_cells>
</decomp_ref>

<paths>
.tools/mstr-record-check.py
org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~54/MANAGER_DAY_READ_20261009.md
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a manager's lane missed because it was typed (read from the register or the commits, with the source printed); a box's record read from the laptop's tree only (each box ref); the worker judging its own read (JUDGMENT criterion graded by the CVO); BLIND: a ruling spoken in a terminal and never written.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: L10 round analysis `org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.20261009.md` @333d2b37b3 (1.0.0_SA_CTO msg 107787); PRD `prd/NFRA_CTLPLN_PRD.md` v0.22 @333d2b37b3, ratified-text SIGNED (current).

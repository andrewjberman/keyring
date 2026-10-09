# TO NFRA_CTLPLN.TO-CT-t-1 -- round 6 THREAD CT-t-1: one round's hops read from git, each with its start and end time

<to_id>NFRA_CTLPLN.TO-CT-t-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~51</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-t-1` (`decompositions/NFRA_CTLPLN_DECOMP.thread6.md`) | **outcome_ref:** FWD-1, FWD-4 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-1 as re-based in PRD v0.22: one real round is planned on the laptop, worked and pushed by a Dell to its box branch, merged by
the integrator into `CLOUD`, and graded on the laptop, and Andrew reads when each step began and ended. FWD-4: a finished round
reaches the trunk without the working box pushing `CLOUD`. MEASURED TODAY: no tool reads a round's hops. Every hop leaves commits:
the issuance commit (`issue(` subject, by the issuing COO), the worker commits on `box/<box>` (authored `0.9.0_WK_<CODE>~<n>`), the
drain merge, the integrator's box-sync merge into `CLOUD` (authored `0.0.0_AB_MSTR`, subject `box-sync`), and the close or grade
commit (by a CVO or CTO serial). Read `.tools/box-sync.sh` for the integrator's exact commit subject.

### BUILD

1. `.tools/thread-trace.py --project <CODE> --round <n> [--fetch]`. Find the round's task orders by `<round>` in
   `org/missions/D*/*/<CODE>/task-orders/*.md` (the LAST status tag rules, as in `.tools/round-close-check.py`). Then read, across
   `origin/box/*` and `origin/CLOUD`:
   - HOP 1 PLAN: the issuance commit(s) of those orders: commit, author, box branch it first appears on, time.
   - HOP 2 WORK: the first and last commit by any worker serial that touches those orders' `<paths>`, and the branch(es) they sit on.
   - HOP 3 PUBLISH: the first `origin/box/<box>` commit that contains HOP 2's last commit (its committer time; use the reflog-free
     form: the earliest commit on that branch, by `git log --ancestry-path`, whose tree contains it).
   - HOP 4 INTEGRATE: the first `origin/CLOUD` merge that makes HOP 2's last commit an ancestor of `CLOUD`, with its author. FWD-4
     holds only when that author is not a seat of the working box. Print `pushed_by_working_box=<True|False>`.
   - HOP 5 GRADE: the first commit after HOP 4 that writes an adjudication row or flips a round's `dep_stage`, naming one of the
     round's criteria, by a CVO-kind or CTO-kind serial. Use `lib/seat_roles.py` `kind_of` where present.
   Print one line per hop, `HOP <n> <name> start=<UTC> end=<UTC> commit=<h> by=<serial> where=<branch>` or `HOP <n> <name> ABSENT`.
   LAST line: `THREAD project=<CODE> round=<n> hops=<found>/5 pushed_by_working_box=<...> elapsed=<HOP1 start to HOP5 end, or ->`.
   It READS; it writes nothing.
2. `--selftest` builds a temporary git repository with two box branches and a CLOUD branch carrying one full thread. Cases:
   - a full thread reads 5/5;
   - a thread with no grade reads 4/5;
   - a thread the working box pushed into CLOUD itself reads `pushed_by_working_box=True`;
   - a round with no orders reads 0/5 and exits non-zero.
   LAST line: `THREAD-TRACE-SELFTEST cases=<k>/<n> ok=<True|False>`.

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
<criterion id="CTt1-AC1" cell_refs="CT-t-1"><invocation>python .tools/thread-trace.py --selftest</invocation><expect>THREAD-TRACE-SELFTEST cases=</expect></criterion>
`CTt1-AC1` -- every case passing; the line reads `ok=True`.

<criterion id="CTt1-AC2" cell_refs="CT-t-1"><invocation>python .tools/thread-trace.py --project LGIC_BLANKFIX --round 8 --fetch</invocation><expect>THREAD project=LGIC_BLANKFIX round=8 hops=</expect></criterion>
`CTt1-AC2` -- the trace of a real, closed round, as it stands (read only). The issuer reads the hops at the drain; the round-9 trace is the issuer's act A1.
</proof_of_spec>

<expected_criteria>CTt1-AC1,CTt1-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~51/NFRA_CTLPLN.TO-CT-t-1.thread-trace.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> CTt1-AC1,CTt1-AC2`, and flip `<status>` to `complete` only when every mechanical criterion
passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.thread6.md</decomp_doc>
<owned_cells>CT-t-1</owned_cells>
</decomp_ref>

<paths>
.tools/thread-trace.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a hop read from the wrong branch (each hop names its branch); a working box's own push into CLOUD read as the integrator's (the author is compared with the working box's seats); a round with no orders reported as a clean trace (0/5, non-zero exit); BLIND: hops that leave no commit (a seat's thinking time).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: L10 round analysis `org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.20261009.md` @333d2b37b3 (1.0.0_SA_CTO msg 107787); PRD `prd/NFRA_CTLPLN_PRD.md` v0.22 @333d2b37b3, ratified-text SIGNED (current).

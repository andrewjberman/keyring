# TO NFRA_CTLPLN.TO-CT-ae-1 -- workstream SEATKILL round 4 (cell CT-ae-1): a planted tree holding a foreign seat survives a REAL `kill-maint.ps1 -Execute` run, and a plain planted tree does not (row S9118, CTO round-14 ruling 1)

<to_id>NFRA_CTLPLN.TO-CT-ae-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~97</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>SEATKILL</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ae-1` (`decompositions/NFRA_CTLPLN_DECOMP.round15.md`) | **outcome_ref:** FWD-21, FWD-25 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Read row `NFRA_CTLPLN-S9118` (Grep `"id": "NFRA_CTLPLN-S9118"` in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`). `.tools/kill-maint.ps1` (the `/govern` reaper every manager runs) stops each target's WHOLE tree with `taskkill.exe /T /F /PID` (about :761). Round 12's `CT-ab-4` put the seat boundary into it (about :228-229 and :747-759: `Test-SeatBoundary` from `.tools/seat-boundary.ps1`; a tree holding a `claude.exe` seat with another launch serial is REFUSED, the foreign serial printed and a `KILL-MAINT-REFUSED` audit line written). That behaviour has only been tested on FAKE process lists (`.tools/tests/test_stop_at_descendant.ps1`, `.tools/tests/test_seat_boundary.ps1`). The CTO's done-when for the row is a PLANTED tree surviving a REAL `kill-maint -Execute`. This cell runs it, on processes the test starts itself, and nothing else.

### BUILD

1. A NEW test `.tools/tests/test_kill_maint_planted.ps1` (Windows PowerShell 5.1 syntax; run as `powershell -NoProfile -ExecutionPolicy Bypass -File .tools/tests/test_kill_maint_planted.ps1`) that PLANTS two small process trees with real, harmless processes and runs the real `.tools/kill-maint.ps1 -Mode scripts -Execute -OnlyPid <planted root pid> -MinAgeSeconds 0 -AuditLog <temporary file>` on each:
   - TREE A (control, no seat): a root wrapper (a `powershell.exe` or `bash.exe` shell of the kind the reaper classifies as an ORPHAN, outside every live claude tree) with a native child that sleeps. Expected: after `-Execute` the whole tree is gone (the root AND its child), the output names it as stopped, and the audit file holds a `KILL-MAINT` line. This arm proves the harness reaches a real kill, so the next arm cannot pass by never killing.
   - TREE B (foreign seat): the same shape, plus a descendant process whose image name is `claude.exe` (copy a harmless system executable such as `powershell.exe` into a temporary folder under the name `claude.exe`) and whose command line carries the launch form `-- 9.9.0_SA_TEST~PLANT begin` (a serial NO real seat uses). Expected: after `-Execute` the root, the planted `claude.exe` and its child all still run, the output says `REFUSED: seat boundary` and names `9.9.0_SA_TEST~PLANT`, and the audit file holds a `KILL-MAINT-REFUSED` line with `reason=seat-boundary`.
   - If the classifier does not take a planted root as a target with `-OnlyPid` (read `kill-maint.ps1` about :62-330 and :690-770 first), say so in your report and plant the shape the classifier does take; do NOT weaken the real script to make the test pass.
2. EVERY planted process is killed in a `finally` block by PID and by image path (the temporary folder), and the test asserts at the end that none of its planted PIDs remain. The test must never pass `-OnlyPid` with a PID it did not start, and must never run `kill-maint.ps1` without `-OnlyPid`. It must not touch any real `claude.exe` (the harness reads the real process list ONLY to assert that the real seats' PIDs are unchanged before and after: print the count).
3. If the planted tree B DIES in the real run (a defect in `kill-maint.ps1` or `seat-boundary.ps1`), fix the script minimally (it is in your `<paths>`), keep tree A killable, and report the defect and the fix as the finding. Do not widen the refusal to anything but a foreign `claude.exe` or `codex.exe` seat.
4. Final line of the test: `KILL-MAINT-PLANTED cases=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. This test kills processes: only the ones it starts, by PID, and only through `kill-maint.ps1 -OnlyPid`. No aws, no network, no push. Windows PowerShell 5.1 syntax, ASCII only, Python 3.12 where Python is used. `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink. CLAUDE.md and org/XXX.md are LOCKED. The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W97-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTae1-AC1" cell_refs="CT-ae-1"><invocation>powershell -NoProfile -ExecutionPolicy Bypass -File .tools/tests/test_kill_maint_planted.ps1</invocation><expect>ok=True</expect></criterion>
`CTae1-AC1` -- tree A dies, tree B survives, no planted process is left, and the real seats are untouched (base: the file does not exist); report the whole last line with its denominator.

<criterion id="CTae1-AC2" cell_refs="CT-ae-1"><invocation>powershell -NoProfile -ExecutionPolicy Bypass -File .tools/tests/test_stop_at_descendant.ps1</invocation><expect>ok=True</expect></criterion>
`CTae1-AC2` -- the existing fake-process battery still passes (base: `STOP-AT-DESCENDANT cases=27/27 ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTae1-AC1,CTae1-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 240`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~97/NFRA_CTLPLN.TO-CT-ae-1.kill-maint-planted-tree-read.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTae1-AC1,CTae1-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round15.md</decomp_doc>
<owned_cells>CT-ae-1</owned_cells>
</decomp_ref>

<paths>
.tools/tests/test_kill_maint_planted.ps1
.tools/kill-maint.ps1
.tools/seat-boundary.ps1
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing; the reaper's own scheduled task is not touched.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the real script run without `-OnlyPid` (the test refuses to) and reaping a live seat (the PID-unchanged assertion); a planted `claude.exe` left running after a failed run (the `finally` kills by PID and by folder); the test passing because nothing was ever killable (tree A is the control that the harness kills); the boundary widened by the fix to a native child (rule: foreign `claude.exe` or `codex.exe` only); BLIND: a planted image copy that antivirus quarantines or a shell that the classifier does not treat as an ORPHAN (the worker reports which shape it used and why).
lane: the <paths> block IS the grant (worker RULING 1). `.tools/kill-maint.ps1` and `.tools/seat-boundary.ps1` sit on every manager's reaper path; any change to them is the finding and is reported by name.
</preflight>

Base checks, dry-run by the issuer before the cut: CTae1-AC1 base: FAIL as expected (the file does not exist); CTae1-AC2 base: see the issuer's dry-run note in the issuance commit.
Source: CTO round-14 analysis ruling 1 (`ledger/ROUND_ANALYSIS.round14.md` @affd2fab43): `CT-ab-4` put the boundary into `kill-maint`; its done-when, a planted tree surviving a real `-Execute`, is unrun. Row NFRA_CTLPLN-S9118 (ARMED).

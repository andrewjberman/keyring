# TO NFRA_CTLPLN.TO-CT-ab-11 -- workstream SEATKILL round 2 (cell CT-ab-11): the seat boundary accepts an underscore in the project segment and judges codex.exe too (rows W78-S1, W78-S3)

<to_id>NFRA_CTLPLN.TO-CT-ab-11</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~84</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>SEATKILL</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ab-11` (`decompositions/NFRA_CTLPLN_DECOMP.round12.md`, Recut 1) | **outcome_ref:** FWD-21, FWD-25 |
**depends_on:** none (the builds `CT-ab-4` are merged at your base)

---

## WORKER FACE

### THE CELL

`CT-ab-4` (merged) added `.tools/seat-boundary.ps1` (`Get-LaunchSerial`, `Test-LaunchSerialMatch`, `Test-SeatBoundary`), wired into `.tools/kill-agent.ps1` and `.tools/kill-maint.ps1`, tested by `.tools/tests/test_seat_boundary.ps1` (`SEAT-BOUNDARY-TEST cases=27/27 wired=both ok=True` at your base). Read rows `NFRA_CTLPLN-W78-S1` and `NFRA_CTLPLN-W78-S3` in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (search the row ids with the Grep tool). MEASURED by the worker that built it:
- The serial token pattern has a third segment `[A-Za-z0-9]+`, so a serial whose project segment carries an underscore (for example `0.9.0_WK_NFRA_CTLPLN~78`) does not match: `Get-LaunchSerial` returns `$null`, the boundary never counts such a seat, and `.tools/kill-agent.ps1` (about :53, "does not look like an agent serial") refuses to target it.
- `Test-SeatBoundary` judges the process name `claude.exe` only (`-ine 'claude.exe'`); a `codex.exe` seat under a tree is neither refused nor named, while `kill-maint.ps1`'s existing guard (about :725) names both.

### BUILD

1. Widen the third segment of the serial token pattern to `[A-Za-z0-9_]+` EVERYWHERE the pattern is written in `.tools/seat-boundary.ps1` and `.tools/kill-agent.ps1` (find every copy; list them in your report). The first two segments and the `~lane` part stay as they are.
2. `Test-SeatBoundary` judges `claude.exe` AND `codex.exe` descendants (a single name set, not two code paths).
3. Test cases in `.tools/tests/test_seat_boundary.ps1`: `0.9.0_WK_NFRA_CTLPLN~78` is a launch serial and is its own target; a fake tree (shell -> seat A -> a `codex.exe` carrying seat B's serial) refuses a kill of A's tree and names B; keep every old case, including the fixture the previous worker changed to `0.9.0_WK_CTLPLN~78` (restore it to the real serial form if it only avoided the pattern; say which). The last line stays `SEAT-BOUNDARY-TEST cases=<k>/<n> wired=<both|kill-agent|kill-maint|none> ok=<True|False>` with n larger than 27.

### RULES FOR THIS CELL

Write surface = the `<paths>`. Never run kill-agent.ps1 or kill-maint.ps1 against a real process; never stop any process. No aws, no push. `.tools/safe-commit.sh` for every commit. Do NOT commit the `portal` gitlink. ASCII only; Windows PowerShell 5.1 syntax. CLAUDE.md and org/XXX.md are LOCKED. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W84-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTab11-AC1" cell_refs="CT-ab-11"><invocation>powershell -NoProfile -ExecutionPolicy Bypass -File .tools/tests/test_seat_boundary.ps1</invocation><expect>wired=both ok=True</expect></criterion>
`CTab11-AC1` -- every case passes, old and new (report the whole last line with its denominator).
</proof_of_spec>

<expected_criteria>CTab11-AC1</expected_criteria>

The invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~84/NFRA_CTLPLN.TO-CT-ab-11.seat-boundary-underscore-and-codex.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTab11-AC1`, flip `<status>` to `complete` only when it passes and the instance is VALID (if refused as outside your grant, leave it `pending` and say so).

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round12.md</decomp_doc>
<owned_cells>CT-ab-11</owned_cells>
</decomp_ref>

<paths>
.tools/seat-boundary.ps1
.tools/kill-agent.ps1
.tools/kill-maint.ps1
.tools/tests/test_seat_boundary.ps1
org/missions/D0/NFRA/NFRA_CTLPLN/task-orders/NFRA_CTLPLN.TO-CT-ab-11.seat-boundary-underscore-and-codex.md
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a pattern widened in one tool but not the other (the report lists every copy); a codex.exe path that is a second code path rather than one name set; a test that kills a real process (fakes only); BLIND: a seat whose first serial-looking token is a path segment, not its launch serial.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: rows `NFRA_CTLPLN-W78-S1` (disarm: CTO ruling or this seat's re-cut; the underscore is already in every worker serial, so the widening is the minimal reading) and `NFRA_CTLPLN-W78-S3` (disarm owner this seat; codex seats are real seats). Recut 1 of the round-12 decomposition.

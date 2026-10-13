# TO NFRA_CTLPLN.TO-CT-ac-2 -- workstream SEATKILL round 3 (cell CT-ac-2): `kill-agent.ps1` ends its target and STOPS AT a descendant seat carrying another serial (row S9117's stated remedy)

<to_id>NFRA_CTLPLN.TO-CT-ac-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~88</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>SEATKILL</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ac-2` (`decompositions/NFRA_CTLPLN_DECOMP.round13.md`) | **outcome_ref:** FWD-21, FWD-25 |
**depends_on:** none (`CT-ab-4` and `CT-ab-11` are merged at your base)

---

## WORKER FACE

### THE CELL

Read rows `NFRA_CTLPLN-S9117`, `NFRA_CTLPLN-S9118` and `NFRA_CTLPLN-W78-S2` in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (search each id with the Grep tool). S9117's stated remedy (its `notes`, fix shape 1) is: "Stop-ProcessTree stops at a descendant claude.exe whose command line carries a different serial, prints it and the kill log names it". `CT-ab-4` instead built a WHOLE-TREE REFUSAL: if `Test-SeatBoundary` (`.tools/seat-boundary.ps1`) finds a foreign seat anywhere under the target, `.tools/kill-agent.ps1` prints `REFUSED: seat boundary`, logs `KILL-REFUSED` and exits 2, so the row never disarms on its own remedy. MEASURED at your base: `SEAT-BOUNDARY-TEST cases=39/39 wired=both ok=True` (`.tools/tests/test_seat_boundary.ps1`); the helper recognises `claude.exe` and `codex.exe` and the serial pattern `^[0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9_]+(~[A-Za-z0-9]+)?$` per token.

### BUILD

1. `.tools/seat-boundary.ps1`: add `Get-SeatSubtreePids -RootPid <pid> -TargetSerial <s> [-Processes <fake list>]` returning two lists from the descendants of RootPid: `Kill` (the descendants that may be ended: every descendant that is NOT a seat, and every descendant seat whose launch serial equals the target's, each with its own descendants) and `Skip` (each descendant seat carrying another serial, with its whole subtree left running), plus `Unclassified` (a seat-named process whose command line cannot be read or whose launch serial cannot be extracted). A pure function over a process list; it stops nothing.
2. `.tools/kill-agent.ps1`: replace the whole-tree refusal by the stop-at-descendant behaviour: end the target's own pid and every pid in `Kill`, leave every `Skip` subtree running, print one line per skipped seat (`SKIPPED foreign seat pid=<pid> serial=<serial>`), and make the kill log (`KILL` line) name each skipped seat. When `Unclassified` is non-empty, KEEP the whole-tree refusal exactly as it is today (`REFUSED: seat boundary`, `KILL-REFUSED`, exit 2): that is the floor. A target tree with no foreign seat behaves as today.
3. `.tools/kill-maint.ps1`: leave its existing refusal as it is (its `taskkill /T` cannot stop at a descendant); change nothing in it.
4. A NEW test `.tools/tests/test_stop_at_descendant.ps1` (PowerShell 5.1, fake process lists only, no real process killed): (a) shell -> seat A -> seat B: the plan for target A is Kill = {A, A's non-seat children}, Skip = {B and B's subtree}; (b) a tree with only the target's own children: Skip empty, same result as the old behaviour; (c) a foreign seat whose command line cannot be read: Unclassified non-empty and `kill-agent.ps1` takes the refusal path (parse the script and check the branch exists; do not run it against a real process); (d) a `codex.exe` foreign seat is skipped like a `claude.exe` one; (e) the skipped line and the log line name each skipped seat. Final line `STOP-AT-DESCENDANT cases=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. Never run `kill-agent.ps1` or `kill-maint.ps1` against a real process; never stop any process. No aws, no push. `.tools/safe-commit.sh` for every commit. Do NOT commit the `portal` gitlink. ASCII only; Windows PowerShell 5.1 syntax. CLAUDE.md and org/XXX.md are LOCKED. The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W88-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTac2-AC1" cell_refs="CT-ac-2"><invocation>powershell -NoProfile -ExecutionPolicy Bypass -File .tools/tests/test_stop_at_descendant.ps1</invocation><expect>ok=True</expect></criterion>
`CTac2-AC1` -- every case passes, the floor case (c) included (base: the file does not exist); report the whole last line with its denominator.

<criterion id="CTac2-AC2" cell_refs="CT-ac-2"><invocation>powershell -NoProfile -ExecutionPolicy Bypass -File .tools/tests/test_seat_boundary.ps1</invocation><expect>wired=both ok=True</expect></criterion>
`CTac2-AC2` -- the boundary tests of `CT-ab-4` and `CT-ab-11` still pass, edited only where the old whole-tree-refusal arm contradicts the new behaviour (base: `cases=39/39`, a control); report the whole last line and name every case you changed.
</proof_of_spec>

<expected_criteria>CTac2-AC1,CTac2-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~88/NFRA_CTLPLN.TO-CT-ac-2.kill-agent-stops-at-a-descendant-seat.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTac2-AC1,CTac2-AC2`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round13.md</decomp_doc>
<owned_cells>CT-ac-2</owned_cells>
</decomp_ref>

<paths>
.tools/seat-boundary.ps1
.tools/kill-agent.ps1
.tools/tests/test_stop_at_descendant.ps1
.tools/tests/test_seat_boundary.ps1
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a stop that still recurses into the foreign seat's subtree (case a); an unreadable command line treated as safe (case c, the floor); a codex.exe foreign seat missed (case d); a test that kills a real process (fakes only); BLIND: a seat whose launch serial is not its first serial-looking token.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base checks, dry-run by the issuer before the cut: CTac2-AC1 base: FAIL as expected (the file does not exist); CTac2-AC2 base: PASS as expected (`SEAT-BOUNDARY-TEST cases=39/39 wired=both ok=True`, run at the issuer's tree).
Source: ROUND_ANALYSIS.round12.md section 2 (S9117) and section 3 item 5; rows S9117, S9118, W78-S2. The whole-tree refusal stays as the floor, per the CTO.

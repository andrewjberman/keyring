# TO NFRA_CTLPLN.TO-CT-ab-4 -- workstream SEATKILL round 1 (cell CT-ab-4): the kill tools never stop a seat other than their target (rows S9117, S9118 and the two addenda)

<to_id>NFRA_CTLPLN.TO-CT-ab-4</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~78</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>SEATKILL</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ab-4` (`decompositions/NFRA_CTLPLN_DECOMP.round12.md`) | **outcome_ref:** FWD-21, FWD-25 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Read rows `NFRA_CTLPLN-S9117` and `NFRA_CTLPLN-S9118` in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (about lines 8422-8476). MEASURED:
- `.tools/kill-agent.ps1` builds its target set by matching `$needleRe` against every `claude.exe` CommandLine (about :86-87 family mode, :93-97 `-All`, :134-135 single serial). Any command line that NAMES the serial matches, including another seat's `--say` hint: at site Z a kill of `2.0.0_SA_COO~ZI` also killed `0.7.0_AE_CloudOps~IR`, whose launch hint contained "2.0.0_SA_COO~ZI". `$targetSerial` is already extracted from the CommandLine at about :174 (pattern `$serialPat` at :76) but the filter never uses it.
- `Stop-ProcessTree` (about :159-168) recurses on ParentProcessId with no serial check, called at :178 (the target's claude.exe) and :187 (the marked host shell); seats launched from that shell are its descendants, so five parked dell2 COOs died with one kill.
- `.tools/kill-maint.ps1` runs `taskkill.exe /T /F` at about :743; a guard at :720-731 already skips a target whose descendants include a claude or codex process. The remaining gap is a target that IS a seat's ancestor shell of another seat.
- `.tools/spawn-agent.ps1`'s non-Windows-Terminal branch (about :272-277) runs `Start-Process powershell ... -PassThru` (:275), making the new seat a child of the caller.

### BUILD

1. ONE shared helper `.tools/seat-boundary.ps1` (dot-sourced by both tools) with: `Get-LaunchSerial <CommandLine>` -- the FIRST full serial token on the command line (the launch serial, `^[0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9]+(~[A-Za-z0-9]+)?$` per token), or `$null`; and `Test-SeatBoundary -RootPid <pid> -TargetSerial <s> [-Processes <fake list>]` -- walks the descendants of RootPid and returns the list of descendant `claude.exe` processes whose launch serial is NOT `TargetSerial` (and, for `-All`, not `TargetSerial~<lane>`).
2. `kill-agent.ps1`: keep a candidate only when `Get-LaunchSerial` of its CommandLine equals the target serial with `-eq` (with `-All`: equals it or a `~<lane>` of it). Before every `Stop-ProcessTree` call, run `Test-SeatBoundary`; a non-empty list REFUSES the kill of that tree, prints each foreign seat (pid and serial) and exits non-zero. A printed `REFUSED: seat boundary` line names them.
3. `kill-maint.ps1`: before the `taskkill /T` call, the same `Test-SeatBoundary` check; a foreign seat refuses that target and is printed (keep the existing guard).
4. `spawn-agent.ps1`'s non-wt branch: launch so the new seat is NOT a child of the caller (for example through `cmd.exe /c start "" powershell ...` or `Start-Process` from a detached `explorer.exe`-parented launcher; choose the simplest that works on Windows PowerShell 5.1 and say which).
5. A test script `.tools/tests/test_seat_boundary.ps1` (PowerShell 5.1, no real process killed, fake process lists only) with at least these cases: a hint naming the target in ANOTHER seat's command line is not a target; the target's own launch serial is; a two-serial fake tree (shell -> seat A -> seat B) refuses a kill of A's tree and names B; a one-serial tree passes; `-All` admits `serial~lane`. The script also parses `.tools/kill-agent.ps1` and `.tools/kill-maint.ps1` with the PowerShell parser (no parse errors allowed) and checks that each calls `Test-SeatBoundary`. Final line `SEAT-BOUNDARY-TEST cases=<k>/<n> wired=<both|kill-agent|kill-maint|none> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. Never run kill-agent.ps1 or kill-maint.ps1 against a real process; never stop any process. No aws, no push. `.tools/safe-commit.sh` for every commit. Do NOT commit the `portal` gitlink. ASCII only; Windows PowerShell 5.1 syntax. CLAUDE.md and org/XXX.md are LOCKED. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W78-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTab4-AC1" cell_refs="CT-ab-4"><invocation>powershell -NoProfile -ExecutionPolicy Bypass -File .tools/tests/test_seat_boundary.ps1</invocation><expect>ok=True</expect></criterion>
`CTab4-AC1` -- every case passes (report the whole last line, with its denominator).

<criterion id="CTab4-AC2" cell_refs="CT-ab-4"><invocation>powershell -NoProfile -ExecutionPolicy Bypass -File .tools/tests/test_seat_boundary.ps1</invocation><expect>wired=both</expect></criterion>
`CTab4-AC2` -- both tools still parse and both call the shared check.
</proof_of_spec>

<expected_criteria>CTab4-AC1,CTab4-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~78/NFRA_CTLPLN.TO-CT-ab-4.kill-tools-seat-boundary.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTab4-AC1,CTab4-AC2`, flip `<status>` to `complete` only when both pass and the instance is VALID (if refused as outside your grant, leave it `pending` and say so).

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round12.md</decomp_doc>
<owned_cells>CT-ab-4</owned_cells>
</decomp_ref>

<paths>
.tools/kill-agent.ps1
.tools/kill-maint.ps1
.tools/spawn-agent.ps1
.tools/seat-boundary.ps1
.tools/tests/test_seat_boundary.ps1
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a hint naming the target matched as the target (case 1); a seat under the target's shell killed with it (the two-serial tree); a fix that makes the tool refuse every kill (the one-serial case passes); a test that kills a real process (fakes only); BLIND: a seat launched by a tool other than spawn-agent.ps1/ajb.ps1 whose first serial token is not its own.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round11.md section 3 item 3; rows S9117/S9118; MSTR msgs 108728, 108730.

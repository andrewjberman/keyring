# AMGT_HARVST task order -- `HVST-br-3` -- ROUND 74 (PRD v0.22 FWD-18, both halves SIGNED; `1.0.0_SA_CTO~Z` msg 31923): THE CYCLE RUNNER IS REGISTERED TO START WITH THE BOX, WITH NOBODY STARTING IT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-br-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~128</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- this cell WRITES an installer and REGISTERS NOTHING. Running it without `-Plan` is forbidden in this cell; the issuer registers at close.
comp-iam: RUN at L5 -- LOCAL script and its plan output. NO scheduled task registered, changed or deleted; NO collector run; NO network call.
comp-adversary: RUN at L5 -- the adversary is an installer that registers when asked only to plan, one that replaces a task it did not create, a task with a time limit (it would kill a run meant to have no end), a hard-coded path, or a task that runs the shared working tree by default.
</preflight>

## 0. THE CELL

PRD FWD-18: the cycle runner (cell `HVST-br-2`, module `lib.opal_data_harvest.cycle_runner`, built in parallel; you
need only its command line: `python -m lib.opal_data_harvest.cycle_runner --state-dir <dir> --runtime-root <dir>
--stop-file <path>`) runs on this box with nobody starting it, and "the process may be registered to start with the
box". The package already has an installer for a different task: `lib/opal_data_harvest/install-schedule.ps1` (read it
whole: its principal, its refusal to replace a task with a different action, its settings). Follow its shape.

## 1. THE BUILD

1. `lib/opal_data_harvest/install-cycle-schedule.ps1`, parameters: `-RepoRoot <dir>` (default: derived from the script's
   own location, two levels up, as `install-schedule.ps1` does -- never a typed path), `-Python <exe>` (default: resolved
   as `install-schedule.ps1` does), `-StateDir`, `-RuntimeRoot`, `-StopFile` (defaults under `<RepoRoot>\.runtime\harvest-cycle\`),
   `-Plan` (print the task it would register and register NOTHING), `-Disabled` (register disabled).
2. The task: name `Opal Data Harvest - Continuous Cycle`; trigger AT LOG ON of the current interactive user (the same
   principal as `install-schedule.ps1`: Chrome needs the signed-in desktop; no stored password, no service account);
   action `<Python> -m lib.opal_data_harvest.cycle_runner --state-dir ... --runtime-root ... --stop-file ...` with working
   directory `<RepoRoot>`; settings: `MultipleInstances IgnoreNew`, `StartWhenAvailable`, battery flags as the existing
   installer, NO execution time limit (`ExecutionTimeLimit` zero, so a run without end is never killed), restart on
   failure 3 times at 5-minute intervals.
3. It refuses (throws, registers nothing) when a task of that name exists with a DIFFERENT action, as the existing
   installer does.
4. `-Plan` prints, one per line: `TASK <name>`, `TRIGGER AtLogOn <user>`, `ACTION <exe> <arguments>`, `WORKDIR <dir>`,
   `TIMELIMIT PT0S`, `MULTIPLE IgnoreNew`, `RESTART 3 PT5M`, then `REGISTERED NOTHING (plan)`.
5. One line in `lib/opal_data_harvest/README.md`'s scheduling section naming the new installer and that its plan is
   read before it is run. Nothing else in the README.

<paths>
lib/opal_data_harvest/install-cycle-schedule.ps1
lib/opal_data_harvest/README.md
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~128/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-br-3"><invocation>powershell -NoProfile -ExecutionPolicy Bypass -File lib/opal_data_harvest/install-cycle-schedule.ps1 -Plan</invocation><expect>REGISTERED NOTHING (plan)</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-br-3"><invocation>powershell -NoProfile -ExecutionPolicy Bypass -File lib/opal_data_harvest/install-cycle-schedule.ps1 -Plan</invocation><expect>TIMELIMIT PT0S</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-br-3"><invocation>powershell -NoProfile -Command "if (Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle' -ErrorAction SilentlyContinue) { 'TASK PRESENT' } else { 'TASK ABSENT' }"</invocation><expect>TASK ABSENT</expect></criterion>
</proof_of_spec>

- Save each AC's output to `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~128/` as you run it.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W128-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~128/AMGT_HARVST.TO-HVST-br-3.the-runner-starts-with-the-box.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-br-3.the-runner-starts-with-the-box`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: as `HVST-br-2` (PRD v0.22 FWD-18, both halves signed; `1.0.0_SA_CTO~Z` msg 31923). Decomposition section 87.
- No edge to `HVST-br-2`: this cell needs only the runner's command line, fixed in both orders. The issuer registers the
  task at close, pointing `-RepoRoot` at a PINNED checkout of the merged runner, never the shared tree.
- AC3 is the negative arm: the cell registers nothing.
- <risk> LOCAL (writes a script; registers nothing). Chain of one, slot ~128, worker-light. **Checks dry-run at the
  base:** AC1 and AC2 base FAIL as expected (no such script); AC3 base PASS expected (TASK ABSENT).

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>issued</status>
<round>74</round>
<slot>~128</slot>
<fabric>site-z</fabric>

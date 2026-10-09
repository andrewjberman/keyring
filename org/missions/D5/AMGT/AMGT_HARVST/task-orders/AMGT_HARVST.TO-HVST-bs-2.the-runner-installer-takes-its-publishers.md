# AMGT_HARVST task order -- `HVST-bs-2` -- ROUND 75 (`1.0.0_SA_CTO~DELL1` msg 1410, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round74.md` @fdce9f9c38, placement 2 and enrichment item 2): THE RUNNER'S AT-LOG-ON INSTALLER TAKES THE PUBLISHERS IT REGISTERS, SO THE RUNNER CAN START ON BBG, WSJ AND BARRONS WITHOUT SEEKING ALPHA

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bs-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~130</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- this cell WRITES the installer and REGISTERS NOTHING. Running the installer without `-Plan` is forbidden in this cell.
comp-iam: RUN at L5 -- LOCAL code only. NO S3 call, NO job, NO collector, backfill_driver or runner run, NO vendor or publisher host, NO scheduled-task registration.
comp-adversary: RUN at L5 -- the adversary is an installer that accepts a publisher the runner does not have (the FT is never run), a default that silently changes what is registered today, or a plan that registers something.
</preflight>

## 0. THE CELL

`lib/opal_data_harvest/install-cycle-schedule.ps1` registers FWD-18's continuous cycle runner
(`python -m lib.opal_data_harvest.cycle_runner`) at log-on. Its `ACTION` passes `--state-dir`, `--runtime-root` and
`--stop-file`, and never `--publishers`. So the runner always cycles its default `PUBLISHERS = ("bbg", "wsj", "barrons", "sa")`
(`lib/opal_data_harvest/cycle_runner.py:25`). The runner itself accepts `--publishers` (`nargs="+"`, `cycle_runner.py:175`).

The runner must start on bbg, wsj and barrons only, and gain sa later, while a separate Seeking Alpha backfill is running.
The installer has to be able to say which publishers it registers.

## 1. THE BUILD (LOCAL; on your branch)

1. Add one parameter, `-Publishers <string>`: a comma-separated list, for example `bbg,wsj,barrons`. (A `-File` invocation
   passes one string, so split it on commas and trim each name.)
2. Each name must be one of `bbg`, `wsj`, `barrons`, `sa`, the runner's `PUBLISHERS` at `cycle_runner.py:25`; say so in a
   comment beside the list. Any other name, or an empty list after the split, prints `REFUSED: unknown publisher <name>` (or
   `REFUSED: no publishers`) and exits non-zero before anything is planned or registered.
3. When `-Publishers` is given, the action's arguments END with ` --publishers <name> <name> ...`, in the order given and
   appended after `--stop-file "<path>"`. When it is not given, the arguments are byte-for-byte what they are today.
4. `-Plan` prints the new ACTION line, then everything it prints today, unchanged.
5. Change nothing else in the script. Change no other product file.

<paths>
lib/opal_data_harvest/install-cycle-schedule.ps1
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~130/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bs-2"><invocation>powershell -NoProfile -ExecutionPolicy Bypass -File lib/opal_data_harvest/install-cycle-schedule.ps1 -Plan -Publishers bbg,wsj,barrons</invocation><expect>--publishers bbg wsj barrons</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bs-2"><invocation>powershell -NoProfile -ExecutionPolicy Bypass -File lib/opal_data_harvest/install-cycle-schedule.ps1 -Plan -Publishers bbg,ft</invocation><expect>REFUSED: unknown publisher ft</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bs-2"><invocation>powershell -NoProfile -ExecutionPolicy Bypass -File lib/opal_data_harvest/install-cycle-schedule.ps1 -Plan</invocation><expect>STOP"\r?\nWORKDIR</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression (row AMGT_HARVST-Z-W128-S1). AC3 is the negative arm: without
  `-Publishers`, the ACTION line still ends at the stop file's closing quote, followed directly by the WORKDIR line.
- Save each criterion's output beside your proof, as `AC1.out`, `AC2.out` and `AC3.out`.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-D1-W130-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~130/AMGT_HARVST.TO-HVST-bs-2.the-runner-installer-takes-its-publishers.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bs-2.the-runner-installer-takes-its-publishers`. Pin every artifact row to the commit that carries it.
- Run every command from the repo root of YOUR worktree.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 1410, `ledger/ROUND_ANALYSIS.round74.md` placement 2 ("activate the runner on bbg, wsj
  and barrons now; add `sa` only when the r47 backfill ends") and enrichment item 2. The issuer found at the cut that the
  installer cannot do that (`install-cycle-schedule.ps1:11` passes no `--publishers`), so this cell comes before `bs-3`.
  Adding `sa` later is a re-run with `-Publishers bbg,wsj,barrons,sa` (Register -Force replaces the task's action).
- **<risk> is SERVED, and this order does NOT close at the worker's report.** The file lands in `lib/opal_data_harvest`, a
  site-Z producer path (census @6a308cd424). Under `1.0.0_SA_CTO~DELL1` msg 1267, its merge is a site-Z deploy under a
  never-widen pair with `1.0.0_SA_CTO~Z`'s half signed before the merge. The branch is HELD UNMERGED until that pair exists.
  The running r47 backfill does not run this script (it runs `backfill_driver` from site Z's shared tree), so the hold
  is the pair, not the leg.
- Slot ~130, worker-light (one file, under 100 product lines). Checks dry-run at the base: see decomposition section 88.

<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<status>issued</status>
<round>75</round>
<slot>~130</slot>
<fabric>dell1</fabric>

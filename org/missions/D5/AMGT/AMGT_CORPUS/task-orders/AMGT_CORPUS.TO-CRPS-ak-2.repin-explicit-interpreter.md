# AMGT_CORPUS task order -- `CRPS-ak-2` -- ROUND 35: the re-pin script names its interpreter explicitly

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ak-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN by the issuer at the cut (round 34: GATES ARMED 0 on this lane). The cell edits the script that registers the amgt-induction-daily Scheduled Task; it never runs -Register (the issuer does, in CRPS-ak-4). No new cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN by the issuer at the cut on CLOUD bad41f3f91 -- ak2_check.sh b1 FAIL (plans Python314), b2 FAIL (rc 1, no refusal line). Blind spot: the check never registers, so -Register's refusal is read from the code, not exercised.
EGRESS CLASS, declared: NONE.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 35.

## 1. THE CELL -- `CRPS-ak-2`

`lib/research/corpus/schedule_induction.ps1` plans and registers the daily Scheduled Task `amgt-induction-daily`.
- Its `Resolve-Python` takes the FIRST real `python` on PATH.
- On this machine PATH now resolves `C:\Program Files\Python314\python.exe` first, and that interpreter cannot `import blpapi`.
  The producer needs `C:\Users\Opal Bloomberg\AppData\Local\Programs\Python\Python311\python.exe` (blpapi + boto3 + pyarrow).
- So a plain `-Register` today would silently register a task that cannot reach Bloomberg (row `AMGT_CORPUS-Z-S85`).
- The live task names Python311 in its action, because it was registered before Python314 was installed.

**Build, in `schedule_induction.ps1` only:**
1. Add an optional parameter `-Python <path>`.
2. The interpreter precedence:
   - (a) `-Python` when given;
   - (b) else the LIVE task's own interpreter, read from the registered `amgt-induction-daily` action: `Get-ScheduledTask`, the
     quoted `python.exe` path inside its arguments;
   - (c) else REFUSE with a line naming why. Never fall back to PATH resolution alone.
   - Derive paths; never type a device path into the script.
3. Before `-Plan` prints its PLAN lines, and before `-Register` changes anything, run `<interpreter> -c "import blpapi"`. On
   failure, print `REFUSED: <interpreter> cannot import blpapi` and exit non-zero. Nothing is registered and nothing is created.
4. `-Plan` prints one added line, `PLAN python <path> (source: param|live-task)`, before the existing `PLAN arguments` line. Every
   existing PLAN line keeps its exact form.
5. Update the script's header comment with the precedence and the refusal.

## 2. BOUNDS

1. NEVER run `-Register` or `-Unregister`, and never change the Scheduled Task. Only `-Plan` and `-Status` are run here.
2. Only the files in `<paths>` change. No AWS call, no Bloomberg call, no install.
3. Write code with the Edit/Write tools, never a shell heredoc. ASCII only.
4. Rows are `AMGT_CORPUS-Z-W2-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner
   2.0.0_SA_COO~X`.

## 3. SURFACES

<paths>
lib/research/corpus/schedule_induction.ps1
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-ak-2.repin-explicit-interpreter.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ak-2.repin-explicit-interpreter.md
</paths>

Read-only: the whole repository, and the issuer's check
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round35/ak2_check.sh` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ak-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round35/ak2_check.sh"</invocation><expect>(?m)^ak2 build 2/2$</expect></criterion>
</proof_of_spec>

- AC1 b1 is the plant: with this session's PATH (Python314 first), `-Plan -Commit HEAD` still prints an arguments line naming
  `...\Python311\python.exe`.
- AC1 b2: `-Plan -Python "C:\Program Files\Python314\python.exe"` exits non-zero with a REFUSED line naming blpapi.

## 5. WHEN YOU ARE DONE

1. Write the instance at the proof path, then run `python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this
   order>` AFTER your final commit. It must return rc 0.
2. Only if the criterion passes, append a new status tag reading complete at the END of this file, in the SAME commit as your
   proof instance.
3. Report ONCE: the precedence as built, the full `-Plan` output (default, and with `-Python` Python314), the criterion's output
   lines, your commit hash and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-34 analysis @`83cd052a9c` ruling 1. Base CLOUD `bad41f3f91`: ak2 build 0/2.
<risk>LOCAL</risk>
<status>pending</status>
<round>35</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<status>complete</status>

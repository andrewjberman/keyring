# AMGT_CORPUS task order -- `CRPS-ak-3` -- ROUND 35: the scheduled entry's dry run reads rc 0, its plan printed, 0 writes

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ak-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~3</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the cell edits the scheduled entry's DRY-RUN path only; the live task runs a pinned checkout, so nothing committed here runs until a re-pin. No new cron or task.
comp-iam: DECLARED-NOT-APPLICABLE -- the dry run's model-block steps make S3 list/get only (the reads admit --dry-run and refresh --dry-run make today); no new call class.
comp-adversary: RUN by the issuer at the cut on CLOUD bad41f3f91 -- ak3_check.py build 0/2 (admit rc 1, refresh rc 1, no plan lines), control 1/1 (0 writes); test_induction_schedule.py 2 passed. Blind spot: the check counts AWS writes at botocore's call point, so a write through another SDK would not be seen.
EGRESS CLASS, declared: AWS-INTERNAL READ ONLY. NO Bloomberg call, NO write.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~3`**, slot `~3` of round 35.

## 1. THE CELL -- `CRPS-ak-3`

`lib/research/corpus/induction_scheduled.py --mode dry-run` runs three steps:
1. `induction_run.main([... "--dry-run"])`;
2. the model-block admit step (`model_block_pull.py admit --dry-run`);
3. the refresh step (`refresh --dry-run`).

Step 1's dry run calls `induction_request.install_poison()` (`lib/research/corpus/induction_request.py:101`). That call replaces
`boto3.client`, `subprocess.run`, `socket.create_connection` and `add_security._load_blp_client` with raisers, and NEVER restores
them. Steps 2 and 3 then die on their S3 reads with `RuntimeError: POISON: boto3.client called`, so the dry run reads admit rc 1,
refresh rc 1 and closing rc 1 (row `AMGT_CORPUS-Z-S84`). The fire path installs no poison and is unaffected.

**Build, in `induction_scheduled.py` only:**
1. Keep step 1's poison for step 1. Then restore the originals before steps 2 and 3. Capture `boto3.client`, `subprocess.run`,
   `socket.create_connection` and the vendor loader before step 1 runs, and put them back after it returns, on every path,
   including an exception.
2. Steps 2 and 3 in dry-run mode stay dry runs. They make S3 list/get reads only, open no Bloomberg session and attempt 0 writes.
3. The dry run then reads admit rc 0, refresh rc 0 and closing rc 0, with each step's plan lines in the captured output and the
   log.
4. Update `lib/research/corpus/tests/test_induction_schedule.py` for the restore. One test asserts the originals are back after
   step 1; the existing tests keep passing.
5. Do not edit `induction_request.py` or `induction_run.py`: the poison is correct for step 1, and only its lifetime is wrong.

## 2. BOUNDS

1. Never run `--mode fire`. Run only `--mode dry-run` and offline tests. No Bloomberg call, no AWS write.
2. Only the files in `<paths>` change.
3. Write code with the Edit/Write tools, never a shell heredoc. ASCII only.
4. Rows are `AMGT_CORPUS-Z-W3-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner
   2.0.0_SA_COO~X`.
5. The dry run writes a local file, `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/induction_run_<date>_dry-run.json`
   (induction_run's own side effect). Never commit it.

## 3. SURFACES

<paths>
lib/research/corpus/induction_scheduled.py
lib/research/corpus/tests/test_induction_schedule.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/AMGT_CORPUS.TO-CRPS-ak-3.dry-run-reads-rc0.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ak-3.dry-run-reads-rc0.md
</paths>

Read-only: the whole repository, in particular `induction_request.py` (`install_poison`), `induction_run.py:754`,
`integrations/bloomberg/research/model_block_pull.py` (`cmd_admit`, `cmd_refresh`), and the issuer's check
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round35/ak3_check.py` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ak-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round35/ak3_check.py"</invocation><expect>(?m)^ak3 build 2/2 control 1/1$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ak-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest lib/research/corpus/tests/test_induction_schedule.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^[0-9]+ passed(, [0-9]+ warnings?)? in [0-9.]+s$</expect></criterion>
</proof_of_spec>

- AC1:
  - build: the admit, refresh and closing lines read rc 0, and the plan lines are printed (the refresh last line ends `pulled 0
    bloomberg_calls 0`);
  - control: 0 AWS writes are attempted. Writes are counted and refused at botocore's call point.
- AC2: the scheduled-entry tests pass with no failure.

## 5. WHEN YOU ARE DONE

1. Write the instance at the proof path, then run `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order
   <this order>` AFTER your final commit. It must return rc 0.
2. Only if every criterion passes, append a new status tag reading complete at the END of this file, in the SAME commit as your
   proof instance.
3. Report ONCE: how the restore is built, the dry run's step and closing lines, each criterion's output line, the pytest
   summary, your commit hash and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-34 analysis @`83cd052a9c` ruling 3. Base CLOUD `bad41f3f91`: ak3 build 0/2 control 1/1; schedule tests
2 passed (control).
<risk>LOCAL</risk>
<status>pending</status>
<round>35</round>
<slot>~3</slot>
<fabric>site-z</fabric>

<status>complete</status>

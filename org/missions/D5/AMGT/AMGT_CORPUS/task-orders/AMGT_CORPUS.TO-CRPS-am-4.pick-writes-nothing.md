# AMGT_CORPUS task order -- `CRPS-am-4` -- ROUND 37: `induction_request --pick` writes nothing (row Z-W4-S4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-am-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~3</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task, alarm or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the run reads the local research library and installs its own refusing transport (vendor_calls 0, s3_writes 0 at the cut).
comp-adversary: RUN by the issuer at the cut -- am4_check.sh build 0/1 (the planted sentinel was rewritten) control 1/1 (rc 0, picked line, vendor_calls 0); the file was restored byte-exact.
EGRESS CLASS, declared: NONE.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~3`**, slot `~3` of round 37.

## 1. THE CELL -- `CRPS-am-4`

`python -m lib.research.corpus.induction_request --pick` is a read-only verb. It measures the backlog population, classifies each
folder, picks one or refuses, and prints the result. Measured at the cut: 2 s, rc 0, `picked NONE Brookfield Corporation BN CA:
...`, `vendor_calls 0`, `s3_writes 0`. But `run()` in `lib/research/corpus/induction_request.py` (about lines 452-457) ALWAYS writes
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/induction_request.json`, the module's hard-coded
`DELIVERABLES_DIR` (about lines 60-63), which is a worker's folder. That is row `AMGT_CORPUS-Z-W4-S4`: a read-only instrument that
writes.

Nothing reads the stored file. `lib/research/corpus/induction_run.py` rebuilds the request fresh and states "Never reads a stored
induction_request.json" (about lines 160-169).

**Build, in `induction_request.py` only:**
1. `--pick` writes nothing: no file, no directory. It prints exactly what it prints today.
2. If a written request document is still wanted, it is opt-in: an explicit `--write <path>` writes it to that path only. Without
   `--write` nothing is written. Do not keep the hard-coded worker folder as a default.
3. Keep every function `induction_run.py` imports (`measure_population`, `build_request`, `classify_folder` and the rest) with
   the same behaviour.
4. Write `lib/research/corpus/tests/test_induction_request_pick_writes_nothing.py`. It is offline: redirect the module's inputs
   the way the existing `lib/research/corpus/tests/` do. Cover: `--pick` leaves a pre-existing file's bytes and a missing file's
   absence unchanged, and `--write <tmp path>` writes there.

## 2. BOUNDS

1. NO vendor call, NO AWS call. Only the files in `<paths>` change; never edit `induction_run.py`.
2. Write code with the Edit/Write tools, never a shell heredoc or `python -c`. ASCII only.
3. Run python from your worktree root as `PYTHONPATH=<worktree root> python ...`.
4. Rows are `AMGT_CORPUS-Z-W3-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner
   2.0.0_SA_COO~X`.

## 3. SURFACES

<paths>
lib/research/corpus/induction_request.py
lib/research/corpus/tests/test_induction_request_pick_writes_nothing.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/AMGT_CORPUS.TO-CRPS-am-4.pick-writes-nothing.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-am-4.pick-writes-nothing.md
</paths>

Read-only: the whole repository, in particular `lib/research/corpus/induction_run.py`, the existing `lib/research/corpus/tests/`,
and the issuer's check `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round37/am4_check.sh` (never edit it;
it plants a sentinel in the request file and restores the file's original bytes afterwards).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-am-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round37/am4_check.sh"</invocation><expect>(?m)^am4 build 1/1 control 1/1$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-am-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python -m pytest lib/research/corpus/tests/test_induction_request_pick_writes_nothing.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^[0-9]+ passed(, [0-9]+ warnings?)? in [0-9.]+s$</expect></criterion>
</proof_of_spec>

- AC1: build -- after `--pick` the planted sentinel's bytes are unchanged; control -- the run still decides (rc 0, a `picked ` line,
  `vendor_calls 0`).
- AC2: your offline test passes.

## 5. WHEN YOU ARE DONE

1. Run your test file and every `lib/research/corpus/tests/` file whose name contains `induction` with `python -m pytest <files>
   -q`. Every test passes.
2. Write the instance at the proof path, with its mutant control from the start. Then run `python .tools/proof-of-spec-check.py
   <instance> AC1,AC2 --governing-order <this order>` AFTER your final commit. It must return rc 0.
3. Only if every mechanical criterion passes, append a new status tag reading complete at the END of this file, in the SAME
   commit as your proof instance.
4. Report ONCE: the diff summary, every criterion's output line, the pytest summary lines, your commit hashes and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-36 analysis @`4c3e3755a7` s.3 ruling 3 + s.4 item 3 (row Z-W4-S4, surfaced 2026-09-25). Base:
am4_check build 0/1 control 1/1.
<risk>LOCAL</risk>
<status>pending</status>
<round>37</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<status>complete</status>

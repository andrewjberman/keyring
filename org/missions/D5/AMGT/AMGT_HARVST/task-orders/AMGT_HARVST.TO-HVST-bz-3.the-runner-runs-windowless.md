# AMGT_HARVST task order -- `HVST-bz-3` -- ROUND 84 (`1.0.0_SA_CTO~DELL1` msg 4670, `ledger/ROUND_ANALYSIS.round83.md` section 3 item 1, row `AMGT_HARVST-Z-S115`): THE CYCLE RUNNER CAN RUN WITH NO CONSOLE WINDOW, SO A CONSOLE SELECTION CANNOT STALL A CYCLE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bz-3.the-runner-runs-windowless</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bz-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~138</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched; the installer gains a switch and its default output is unchanged.
comp-iam: RUN at L5 -- LOCAL code and tests only. NO publisher host, NO S3 call, NO collector or runner run against the world, NO scheduled task registered or changed, NO site Z box.
comp-adversary: RUN at L5 -- the adversary is a guard that swallows a REAL stdout (output lost where a console exists), a change to what a cycle record holds, a windowless run that still raises silently and ends every cycle as `AttributeError`, and an installer whose default registration changed.
</preflight>

## 0. THE CELL

The site Z cycle runner is a scheduled task that runs `python.exe`, so Windows gives it a console window. A mouse selection in that window
(QuickEdit "Select" state) blocks the runner's next console write; it then never reaches its stop-file check and writes nothing. That stalled the
harvest for 9 h 24 m on 2026-10-12. `pythonw.exe` has no console window, so there is nothing to select. Under `pythonw.exe` Python sets
`sys.stdout`, `sys.stderr` and `sys.stdin` to `None`.

**The trap this cell exists to close:** `Tee.write` in `lib/opal_data_harvest/cycle_runner.py` (class `Tee`, about lines 79-99) calls
`self.real.write(text)` and `self.real.flush()` with `self.real = sys.stdout`. With `sys.stdout` `None` that raises `AttributeError`.
`run_cycle` catches `(Exception, SystemExit)` and records `stopped = "AttributeError"`, so EVERY cycle would end as a stopped record and the
harvest would look alive and move nothing. The cell makes the runner work with no console and proves it by running it under the real `pythonw.exe`.

## 1. THE BUILD (LOCAL)

Work in your worktree. Change only the files named in `<paths>`.
1. **`Tee` tolerates a missing real stream.** `write` and `flush` skip the real stream when it is `None`; the log lines and the return value
   (`len(text)`) are unchanged. When a real stream exists, what it receives is byte-identical to the base.
2. **Audit the runner's own path for any other use of a standard stream that assumes it exists** (`cycle_runner.py`, and `backfill_driver.py`
   where `sys.stdout` is a default `out` at about lines 365 and 574). Inside the driver `sys.stdout` is the `Tee` (the runner redirects it), so
   most uses are already covered; change a use ONLY when the real `pythonw.exe` run in step 4(b) shows it failing. `print()` with a `None`
   stdout is already a silent no-op, leave it.
3. **The installer gains `-Windowless`** (`lib/opal_data_harvest/install-cycle-schedule.ps1`, a switch beside `-Plan`). When set and `-Python`
   is not given, `$Python` is the `pythonw.exe` in the same directory as the resolved `python.exe`; if that file is missing the installer prints
   `REFUSED: pythonw.exe not found beside <python>` and exits 1. When set and `-Python` is given with a leaf name other than `pythonw.exe`, it
   prints `REFUSED: -Windowless takes the pythonw.exe beside python.exe` and exits 1. `-Plan` prints the interpreter in its `ACTION` line, as it
   does today. **Without the switch the installer's behaviour and its `-Plan` text are unchanged.**
4. **Tests**, in `lib/opal_data_harvest/test_bz3_windowless_runner.py` (reuse `test_br2_cycle_runner.py`'s `FakeDriver` and `Clock`; no network):
   - (a) `Tee(state_dir, None)`: `write` returns `len(text)`, `flush` does not raise, and the complete lines reach `cycle_runner.log`.
   - (b) **A REAL `pythonw.exe` RUN.** From the test, start `pythonw.exe` (the one beside `sys.executable`; `pytest.skip` when it is absent or
     the OS is not Windows) with a small script file the test writes into `tmp_path`: it imports `lib.opal_data_harvest.cycle_runner`, runs
     `main([...,"--once","--state-dir",<tmp>,"--publishers","bbg"], driver=<FakeDriver>, ...)` and writes its return value to a result file
     (pythonw cannot print). Assert: the result file says exit 0, `<tmp>/cycles/bbg/*.cycle.json` exists, its `stopped` is NOT `AttributeError`
     and `completed` is true, and the log carries the `CYCLE` line. Give the child a timeout of 120 s.
   - (c) **A MUTANT:** the same real `pythonw.exe` run with the guard removed (the child script puts the base's unguarded `Tee.write` back
     before calling `main`): the cycle record's `stopped` is `AttributeError`. Assert that it is. This proves (b) discriminates.
   - (d) **Installer, through `powershell -NoProfile -File`** (`pytest.skip` when PowerShell is absent): `-Plan -Windowless -Publishers bbg`
     prints an `ACTION` line whose interpreter ends `pythonw.exe`; `-Plan -Publishers bbg` without it prints an `ACTION` line whose interpreter
     ends `python.exe` and contains no `pythonw`; `-Plan -Windowless -Python <the python.exe path>` prints `REFUSED` and exits 1.
5. Do not run anything against a publisher, S3 or the site Z box, and do not register or start a scheduled task. A surprise is a row; keep working.

<paths>
lib/opal_data_harvest/cycle_runner.py
lib/opal_data_harvest/backfill_driver.py
lib/opal_data_harvest/install-cycle-schedule.ps1
lib/opal_data_harvest/test_bz3_windowless_runner.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~138/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bz-3"><invocation>python -m pytest lib/opal_data_harvest/test_bz3_windowless_runner.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bz-3"><invocation>python -m pytest lib/opal_data_harvest/test_br2_cycle_runner.py lib/opal_data_harvest/test_bv1_cycle_continues_past_pair_errors.py lib/opal_data_harvest/test_bx3_failure_reason_kept.py lib/opal_data_harvest/test_ae4_backfill_driver.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. `(?m)^\d+ passed in` matches only a run with no failure and no skip-only run.
- The full `lib/opal_data_harvest` suite had 4 failures at `1c69fa35a3` (`test_ah1_fixture_solve.py::test_fixture_solve[bbg]`, three in
  `test_aw1_origin_load_wait.py`). Run it before and after, and record both counts in your report. Add none.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W138-S1`. The channel file has MIXED line
  endings and is append-only: append a row by BYTES and check the diff reads N insertions and 0 deletions. Its commit needs
  `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row`
  in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~138/AMGT_HARVST.TO-HVST-bz-3.the-runner-runs-windowless.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bz-3.the-runner-runs-windowless`. Pin every artifact row to its commit.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 4670 and `ledger/ROUND_ANALYSIS.round83.md` section 3 item 1: "the runner launches WINDOWLESS (`pythonw`, or the
  scheduled task's hidden/no-console mode), or with QuickEdit disabled for its console. Arm: a selection attempt cannot stall a cycle, either because no console
  window exists or because a planted selection leaves the log writing." Row `AMGT_HARVST-Z-S115` (ARMED, disarm owner this seat).
- **Why `pythonw` and not QuickEdit-off:** clearing the QuickEdit mode bit stops an accidental MOUSE selection but not the console's Mark command (system menu or
  keyboard), which freezes output the same way. A process with no console has neither. The registry option (`HKCU\Console`) changes every python console of that
  Windows user on the box, a wider blast radius than one task. A hidden-window launcher keeps a console and needs nested quoting in the task action.
- **The real risk is the one named in section 0:** a windowless runner that silently ends every cycle. That is why criterion AC1 runs the REAL `pythonw.exe` and
  carries its own mutant. The collector child (`backfill_driver.Collector._spawn`) uses `capture_output=True` and `sys.executable`, so under `pythonw` it is itself
  windowless with piped output; CPython's `subprocess` makes a pipe for a missing stdin handle. The real run in 4(b) uses a fake driver, so it does NOT exercise
  that spawn: the site Z cell (`HVST-bz-4`) reads the first real cycle under the new interpreter before the old pin is retired.
- **The site Z act is NOT this order:** `HVST-bz-4` re-registers the task with `-Windowless` at a cycle boundary by the stop file, under a never-widen pair, cut as
  workstream `WINDOWLESS-SITEZ` after this order's merge so its pin is a real commit (decomposition section 101).
- Merge: at the chain end with `safe-merge.sh`, under a never-widen pair (COO half at the drain, and the CTO's producer half), into `lib/opal_data_harvest`.
- Slot ~138, worktree `C:/Dev/wk-harvst-138`, branch `wk-AMGT_HARVST-138-r84`.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>84</round>
<slot>dell1</slot>
<fabric>dell1</fabric>

**COMPLETE 2026-10-13 ~07:3xZ (issuer `2.0.0_SA_COO~W1`):**
- **Built:** worker ~138, branch `wk-AMGT_HARVST-138` @ca38d22541 (build 31f2854a37, proof ca38d22541). Proof VALID rc 0, re-run by this seat in the worktree and
  again at the shared tree with `--governing-order`.
- **Merged:** 995adcaeaa on box/dell1 by `safe-merge.sh` (6 files, 0 dropped, 0 foreign), under the COO half @4ed2d30312 and the CTO half @42064bd87b.
- **AC1 PASS** `7 passed` (re-run in the worktree and on the merged tree). **AC2 PASS** `61 passed` (re-run, both). Full suite: 4 failed before and after
  in a CLEAN checkout of the merge (the same four: `test_ah1_fixture_solve[bbg]` and three in `test_aw1_origin_load_wait`), 792 -> 799 passed. The
  SHARED tree reads 5 failed because of one file's CRLF on disk (row D1-S13, INERT); the merge did not touch it. The mutant arm fired.
- **What it proves:** the cycle runner completes a cycle under a REAL `pythonw.exe` launched DETACHED with no standard handles, and the unguarded `Tee`
  ends the same cycle as `AttributeError`. The installer's `-Windowless` names the `pythonw.exe` beside `python.exe`; its default is unchanged.
- **What it does NOT prove, and the CTO's half carries to `HVST-bz-4`'s pair:** (1) the real collector spawn under `pythonw` (the test uses a fake
  driver); (2) `cycle_runner.log` written under the windowless launch at site Z; (3) the task action reading `pythonw` in `schtasks /query /xml`;
  (4) no console window existing. Those, read at site Z, are what disarm Z-S115. THIS merge disarms nothing served.
- **Rows:** D1-W138-S1 INERT (the conftest subprocess poison needs `allow_real_session` on the real-process tests), D1-W138-S2 INERT (a pythonw child
  with captured pipes is not the no-console condition; the test launches it DETACHED_PROCESS). D1-S13 INERT (above), filed by this seat.

<status>complete</status>

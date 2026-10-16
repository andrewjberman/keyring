# AMGT_RESAPP task order -- `AMGT-bo-4` -- THE FILINGS BATCH'S FIRST FIRE TAKES ITS `--limit` FROM A DATA FILE (G4, A CAPPED FIRST TRANCHE OF 20 NAMES)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bo-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~478</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bo-4.g4-first-fire-limit-held-as-data</to_id>
<placeholders>NONE</placeholders>
<workstream>G4</workstream>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled, registered or enabled by this order; the three Windows tasks stay unregistered.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call is made by anything this order adds; its tests stub every runner.
comp-adversary: RUN at the cut -- at the base `python -m pytest lib/research/llm_batch/tests/test_first_fire_limit.py -q` reads `no tests ran`, rc 4 (FAIL as expected); `python -m lib.research.llm_batch.run filings --print-command` reads `error: unrecognized arguments: --print-command`, rc 2 (FAIL as expected); `python -m pytest lib/research/llm_batch/tests -q` reads `19 passed`, short of the 23 the criterion needs (FAIL as expected).
EGRESS CLASS, declared: NONE. No S3, no network, no model call, no Windows task.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-478` (branch `wk-AMGT_RESAPP-478`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-478`.

## 1. THE CELL -- `AMGT-bo-4` (round 108, decomposition s.117a)

The package `lib/research/llm_batch/` (built in round 107, order `AMGT-bn-6`) runs three LLM-tier batches when their event says so. `tasks.py` holds the argv each runs (`TASKS[key].command`); `run.py` runs that argv when `trigger.decide` says due (`run_task`, line 64: `rc, out = runner(task.command)`). The cluster CTO ruled that the FILINGS batch's first fire takes only a first tranche of 20 names: the filings batch (`lib/research/filings/batch.py`) already has `--limit N` (an int; `plan()` slices the first N fetchable universe rows before its skip-unchanged check; do not change that module). This cell makes the limit DATA, so lifting it later is one data edit.

**Build exactly this, nothing else.**
1. A new data file `lib/research/llm_batch/first_fire_limit.json`, one JSON object: `{"limits": {"filings": 20}, "claim": "held", "basis": "cluster CTO ruling XA-20261016T050756Z-844a (msg 6516): the filings first fire takes 20 names; the cap is lifted by setting the value to null after the 20 stored usage.usd values are read"}`. Pure ASCII.
2. In `run.py`: a pure function `command_for(task, limits)` returning `task.command` with `("--limit", str(n))` appended when `limits.get(task.key)` is a positive integer, and `task.command` unchanged when the key is absent, `null`, zero or not an integer; and a loader `load_limits(path)` that returns `{}` when the file is absent and the file's `limits` object otherwise (a malformed file raises, never silently reads as no cap). `run_task` calls `runner(command_for(task, limits))` (give `run_task` a `limits` keyword argument defaulting to `None`, meaning none; `main()` passes `load_limits(LIMITS_PATH)`). The plan-only command the trigger reads (`FILINGS_PLAN_ONLY`) is NOT changed and NOT limited.
3. A flag `--print-command` on `run.py`'s `main`: prints exactly one line `LLM-BATCH task=<t> command=<the argv joined by spaces, with the Python path printed as python>` for the argv `command_for` returns, calls NO S3, runs no batch, reads no last-run record, and returns 0. Printing `python` in place of `sys.executable` keeps the line the same on every box.
4. Tests, a new file `lib/research/llm_batch/tests/test_first_fire_limit.py`, at least 4, each stubbing every runner (no subprocess, no S3): T1 filings with `{"filings": 20}` ends with `--limit 20`; T2 absent key, `null`, `0` and `"20"` (a string) leave the argv unchanged; T3 `run_task` hands the runner the limited argv when due (use the existing `test_run.py` stubs as the model) and the plan-only argv unchanged; T4 `load_limits` reads the committed file and returns `{"filings": 20}`, a missing path returns `{}`, a malformed file raises.
5. Nothing else: do not touch `tasks.py`, `register.py`, `trigger.py`, `inputs.py`, the launchers or any other module; register and enable nothing; the registration plan still prints `PLAN: 3 task(s), 0 created`.

**Do this in order.** (1) Run AC1, AC2 and AC3 once on the unchanged tree and record what they print (they must fail as the preflight says). (2) Write the tests first (item 4), run them red. (3) Build items 1 to 3. (4) Run AC1 to AC3 and `python -m lib.research.llm_batch.register --plan | tail -1` (it must still read `PLAN: 3 task(s), 0 created`). (5) Every `.py` edit passes `.tools/commit-gate.sh` (py_compile, ds-precommit, ruff): the package is pure ASCII.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the five files named above (the data file, `run.py`, the new test file, your deliverables, the channel). Never register, enable or run a Windows task; never call AWS; never run the filings batch for real.
2. No new alert, monitor or notification of any kind. No change to what a batch does.

## 3. SURFACES

<paths>
lib/research/llm_batch/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~478/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bo-4"><invocation>cd C:/dev/wk-resapp-478 &amp;&amp; timeout 300 python -m pytest lib/research/llm_batch/tests/test_first_fire_limit.py -q; echo "exit=$?"</invocation><expect>a line `<n> passed` with n at least 4, no `failed`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bo-4"><invocation>cd C:/dev/wk-resapp-478 &amp;&amp; timeout 120 python -m lib.research.llm_batch.run filings --print-command; echo "exit=$?"</invocation><expect>exactly one stdout line `LLM-BATCH task=filings command=python -m lib.research.filings.batch --universe newest --write-pool --limit 20`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bo-4"><invocation>cd C:/dev/wk-resapp-478 &amp;&amp; timeout 300 python -m pytest lib/research/llm_batch/tests -q; echo "exit=$?"</invocation><expect>a line `<n> passed` with n at least 23 (the 19 of round 107 plus at least 4), no `failed`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~478 <0.9.0_WK_AMGT_RESAPP~478@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~478/AMGT_RESAPP.TO-AMGT-bo-4.g4-first-fire-limit-held-as-data.proof_of_spec.json` with `to_id` equal to the `<to_id>` line above, character for character, and `decomp_ref` from the order's own block; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` from `C:/dev/wk-resapp-478` on the committed bytes and report its verdict line.

Report once:
- the commit hash;
- the pre-edit runs of AC1 to AC3 and the post-edit runs, with their output lines;
- the output of `python -m lib.research.llm_batch.register --plan | tail -1`;
- the verdict line of the instance check;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's message 6516 (the cluster CTO's ruling XA-20261016T050756Z-844a, record `org/critical_paths/cross_adjudication/20261016T0513Z_XA-20261016T050756Z-844a.md`, not yet on dell1): "Build the --limit argument in lib/research/llm_batch/tasks.py as a small cell. The enable pair states a first fire of 20 names (about USD 14). Read the 20 stored usage.usd values before the cap is lifted. The next trading day carries the remaining names." The cell puts the limit in a data file read by `run.py` rather than in `tasks.py`: `tasks.py` is a frozen table the register plan prints, and a data file makes the lift one edit by the owner (the A4 window pattern, `price_axis_window.json`). Read at the cut: `filings/batch.py` `plan()` line 186-187 slices `fetchable_rows[:limit]` BEFORE the skip-unchanged check, so a cap left in place re-reads the same 20 names (all unchanged, no spend) and does not advance; the pair states it and the lift. The management batch has its own `--limit` and Lusha credits (at most 28 on its first fire); the CTO's ruling caps only filings, so only filings is in the file. The enable pair (COO half, then CTO half) is written after this cell is merged. Not a monitor, not an alert: the cap is a program argument.

<status>complete</status>
<round>108</round>
<slot>0.9.0_WK_AMGT_RESAPP~478</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

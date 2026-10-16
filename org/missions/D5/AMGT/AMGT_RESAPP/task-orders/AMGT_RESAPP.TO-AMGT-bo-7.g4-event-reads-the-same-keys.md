# AMGT_RESAPP task order -- `AMGT-bo-7` -- THE FILINGS TASK'S EVENT COUNTS ONLY THE NAMES IT RUNS (THE PLAN-ONLY CHECK TAKES THE SAME KEY LIST AS THE BATCH)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bo-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~481</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bo-7.g4-event-reads-the-same-keys</to_id>
<placeholders>NONE</placeholders>
<workstream>G4PLAN</workstream>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled, registered, enabled or run by this order; the three Windows tasks stay Disabled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call is made by anything this order adds; its tests stub every runner.
comp-adversary: RUN at the cut -- at the base `python -m pytest lib/research/llm_batch/tests/test_plan_only_keys.py -q` reads `no tests ran`, rc 4 (FAIL as expected); `python -m lib.research.llm_batch.run filings --print-plan-command` reads `error: unrecognized arguments: --print-plan-command`, rc 2 (FAIL as expected); `python -m pytest lib/research/llm_batch/tests -q` reads `46 passed`, short of the 52 the criterion needs (FAIL as expected). The defect was read in the code: `inputs.would_run(runner)` runs the constant `tasks.FILINGS_PLAN_ONLY` (no `--security-key`), while `command_for` runs the batch WITH the 8 keys.
EGRESS CLASS, declared: NONE. No S3, no network, no model call, no Windows task.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-481` (branch `wk-AMGT_RESAPP-481`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-481`.

## 1. THE CELL -- `AMGT-bo-7` (round 108, decomposition s.117c)

`lib/research/llm_batch/` runs the filings batch when its event says so. For the filings task the event is the count of `WOULD-RUN:` lines printed by the batch's read-only `--plan-only` check (`inputs.would_run(runner)`, which runs the constant `tasks.FILINGS_PLAN_ONLY` = `python -m lib.research.filings.batch --universe newest --plan-only`); the trigger (`trigger.decide`, rule (c)) is due while that count is above zero. The batch itself is run by `command_for(task, limits, keys)` WITH `--security-key K` for each of 8 keys held in `first_fire_limit.json` (`run.load_security_keys`). The two disagree: the plan-only check is UNFILTERED, so it counts every name of the universe (163 of them can never resolve), the count never reaches zero, and a real run (which does NOT skip unchanged names; only `--plan-only` does) would re-analyze the 8 names every day. Make the plan-only check take the same key list, so the event counts only the names the task runs.

**Build exactly this, nothing else.**
1. In `inputs.py`: `would_run(runner, keys=None)`: the argv it runs is `tasks.FILINGS_PLAN_ONLY` followed by `--security-key K` for each K in `keys` (list order); with `keys` None or empty the argv is `tasks.FILINGS_PLAN_ONLY` exactly as today. Counting is unchanged (the `WOULD-RUN:` line prefix; `None` when the runner does not exit 0).
2. In `run.py`: `plan_command_for(task, keys)` returns the plan-only argv for a plan-only task with the key list applied (the same function `would_run` uses, so the two cannot drift: import and reuse it, do not duplicate the argv building); `run_task` passes the keys it already receives to `inputs.would_run(runner, keys.get(key) if keys else None)` for a plan-only task. For a non-plan-only task nothing changes.
3. A flag `--print-plan-command` on `run.py`'s `main`: prints exactly one line `LLM-BATCH task=<t> plan-command=<the plan-only argv joined by spaces, with the Python path printed as python>` for a plan-only task (for any other task print `LLM-BATCH task=<t> plan-command=none`), calls NO S3, runs nothing, returns 0.
4. Tests, a new file `lib/research/llm_batch/tests/test_plan_only_keys.py`, at least 6, each stubbing every runner (no subprocess, no S3): T1 `would_run` with keys: the stub runner receives `FILINGS_PLAN_ONLY` plus the keyed pairs in order; T2 no keys / empty: the argv is exactly `FILINGS_PLAN_ONLY`; T3 the count is the number of `WOULD-RUN:` line prefixes and `None` for a non-zero exit; T4 `run_task` for filings with 8 keys and a stub that reports 0 WOULD-RUN lines for the keyed plan-only argv: the decision reads not due (use `trigger.decide`'s existing no-event reason) and the batch runner is not called; T5 the same with 1 WOULD-RUN line: due, and the batch runner receives the keyed batch argv; T6 a non-plan-only task (`scores`) is unaffected; T7 `plan_command_for` equals what `would_run` passes (one source of truth). Update an existing test only where it asserts the old unfiltered call shape of `would_run`, and say which in your report.
5. Nothing else: do not touch `tasks.py`, `register.py`, `trigger.py`, the launchers, the data file or any module outside `lib/research/llm_batch/`; register and enable nothing; `register --plan` still prints `PLAN: 3 task(s), 0 created`.

**Do this in order.** (1) Run AC1 to AC3 once on the unchanged tree and record what they print. (2) Write the tests first (item 4), run them red. (3) Build items 1 to 3. (4) Run AC1 to AC3 and `python -m lib.research.llm_batch.register --plan | tail -1`. (5) Every `.py` edit passes `.tools/commit-gate.sh`: the package is pure ASCII.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the files named above (`inputs.py`, `run.py`, the new test file and, where item 4 allows, one existing test file; your deliverables; the channel). Never register, enable or run a Windows task; never call AWS; never run the filings batch for real.
2. No new alert, monitor or notification of any kind.

## 3. SURFACES

<paths>
lib/research/llm_batch/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~481/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bo-7"><invocation>cd C:/dev/wk-resapp-481 &amp;&amp; timeout 300 python -m pytest lib/research/llm_batch/tests/test_plan_only_keys.py -q; echo "exit=$?"</invocation><expect>a line `<n> passed` with n at least 6, no `failed`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bo-7"><invocation>cd C:/dev/wk-resapp-481 &amp;&amp; timeout 120 python -m lib.research.llm_batch.run filings --print-plan-command; echo "exit=$?"</invocation><expect>exactly one stdout line `LLM-BATCH task=filings plan-command=python -m lib.research.filings.batch --universe newest --plan-only --security-key ASML_US_Equity --security-key BA_US_Equity --security-key COST_US_Equity --security-key HAL_US_Equity --security-key HD_US_Equity --security-key INTU_US_Equity --security-key KMB_US_Equity --security-key VLO_US_Equity`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bo-7"><invocation>cd C:/dev/wk-resapp-481 &amp;&amp; timeout 300 python -m pytest lib/research/llm_batch/tests -q; echo "exit=$?"</invocation><expect>a line `<n> passed` with n at least 52 (the 46 now plus at least 6), no `failed`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~481 <0.9.0_WK_AMGT_RESAPP~481@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~481/AMGT_RESAPP.TO-AMGT-bo-7.g4-event-reads-the-same-keys.proof_of_spec.json` with `to_id` equal to the `<to_id>` line above, character for character, and `decomp_ref` from the order's own block; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters. Run `python .tools/proof-of-spec-check.py <instance> --governing-order org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-bo-7.g4-event-reads-the-same-keys.md` from `C:/dev/wk-resapp-481` on the committed bytes and report its verdict line.

Report once:
- the commit hash;
- the pre-edit runs of AC1 to AC3 and the post-edit runs, with their output lines;
- the output of `python -m lib.research.llm_batch.register --plan | tail -1`;
- which existing test (if any) you updated and why;
- the verdict line of the instance check;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** found 2026-10-16 ~12:1xZ while writing the COO half for the 8-key re-enable. READ in `filings/batch.py`: `plan_only_check` is called only under `args.plan_only` (lines 450-489 and 596); the real loop calls `run_group` for every planned group with no skip-on-unchanged. READ in `llm_batch/inputs.py`: `would_run` runs the constant `tasks.FILINGS_PLAN_ONLY`. Consequence if enabled as merged at `83f65c6344`: the unfiltered count (171) never reaches zero, so the task is due every trading day and each run re-analyzes the 8 keyed names, about USD 4.5 to 5.6 a run. This corrects the issuer's own earlier statements (the bo-5 issuer notes and `G4_ENABLE_PAIR_MEASUREMENTS_20261016.md`: "a cap left in place re-reads the same 20 (all unchanged, no spend)" and "a second day's run over the 8 skips them as unchanged"), which were inferred from the plan-only check and not read in the run path. The new COO half states this and names the correction. The whole-universe event (names that can never resolve are counted as would-run forever) is the CTO's, not this cell's.

<status>complete</status>
<round>108</round>
<slot>0.9.0_WK_AMGT_RESAPP~481</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

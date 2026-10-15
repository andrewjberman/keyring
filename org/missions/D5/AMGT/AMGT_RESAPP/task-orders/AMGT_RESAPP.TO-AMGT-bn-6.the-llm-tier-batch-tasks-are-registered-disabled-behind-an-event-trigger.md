# AMGT_RESAPP task order -- `AMGT-bn-6` -- THE SECURITY ANALYSIS BATCH TASKS (FILINGS, EXEC MANAGEMENT, SCORES) GET A REGISTRATION SCRIPT THAT CREATES THEM DISABLED, NAMING THEIR OWNER, AND AN EVENT-DRIVEN TRADING-DAY TRIGGER THAT RUNS A BATCH ONLY WHEN ITS INPUT CHANGED (THE CODE HALF OF G4; NOTHING IS REGISTERED OR ENABLED)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bn-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~475</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bn-6.the-llm-tier-batch-tasks-are-registered-disabled-behind-an-event-trigger</to_id>
<placeholders>NONE</placeholders>
<workstream>G4</workstream>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests in a worktree; this order registers NO task and enables NO task: its criteria never run `schtasks`, every test stubs it.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS write and no IAM change; the trigger's S3 reads are `list_objects_v2` on a stub client in every test.
comp-adversary: RUN at the cut -- AC1's test directory `lib/research/llm_batch/tests` does not exist at the base, so `python -m pytest lib/research/llm_batch/tests -q` reads rc=4 `no tests ran` (read here); AC2's `python -m lib.research.llm_batch.register --plan` reads `No module named lib.research.llm_batch` and rc=1 at the base (read here).
EGRESS CLASS, declared: NONE in the worker's run. No Anthropic call, no EDGAR call, no S3 call, no `schtasks` call: every boundary is stubbed in the tests.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-475` (branch `wk-AMGT_RESAPP-475`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-475`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bn-6` (round 107, decomposition s.116)

**Why.** Andrew-direct (the box CTO's record `org/tier1_exec/1.0.0_SA_CTO/logs/2026-10-15/DELL1_status_1525Z.md`, lines 14 to 15): "Yes we definitely want to activate the batching but will do it post restart"; the restart is done. The CTO ruled (`org/missions/D5/AMGT/AMGT_RESAPP/ledger/CTO_RULING_G4_CUT_BN6_20261015.md`): a LOCAL code half, a registration script plus an EVENT-DRIVEN TRADING-DAY TRIGGER (not a timer standing in for success-of-upstream), hosted on dell1, tasks created DISABLED, the owning lane `2.0.0_SA_COO~R1` named in each task's description. The ENABLE is a separate later act. This cell moves nothing.

**What exists today (read at the base; reuse it, build only what is missing).**
- `lib/research/filings/batch.py` and `lib/research/management/batch.py` each define `task_definition()` (name, launcher, the `schtasks` create, disable and query lines) and answer `--print-task`; filings also answers `--plan-only`: a READ-ONLY check (EDGAR submissions index plus a pool read) that prints `SKIP-UNCHANGED` or `WOULD-RUN` per name with no download, no model call and no write. Their launchers are `lib/research/filings/run_batch.cmd` (`python -m lib.research.filings.batch --universe newest --write-pool`) and `lib/research/management/run_batch.cmd` (`python -m lib.research.management.batch --write-pool`); the task names are each module's `TASK_NAME` constant.
- `lib/research/scores/run_scores.py` (`python -m lib.research.scores.run_scores [--as-of D] [--dry-run]`) reads, per name, the newest `derived/model_block/<key>/<timestamp>/model_block.json` and `peers/v1/<key>/<as_of>.json` from the `opal-data-harvest` pool and writes `scores/v1/<key>/<as_of>.json`; it makes NO vendor call and NO model call. It has no task definition and no launcher.
- `lib/trading_calendar.py`: `is_trading_day(date) -> bool`, `prev_trading_day(date)`. It is the one frontier; never write a weekday test of your own.
- NOT COVERED by this cell, and you file ONE OBSERVATION row saying so: drafting (`lib/research/drafting/run_drafting.py` takes two required directories and has no whole-population entry) and posture (`lib/research/posture/judge.py` takes ONE `--security-key`): neither can be registered as a task today.

**The change: a new package `lib/research/llm_batch/` (nothing else in the repository changes).**
1. `tasks.py`: a table `TASKS` of exactly three entries, `filings`, `management`, `scores`, each with: `task_name` (filings: the module's own `TASK_NAME`, `OpalResearch-FilingsAnalyzer`; management: the module's own `TASK_NAME`, `OpalResearch-ExecManagement`; scores: `OpalResearch-Scores`; read the two constants from the modules, do not retype them), `command` (the argv list of the batch, with `sys.executable -m <module>` and the flags of the launchers above; scores: `-m lib.research.scores.run_scores`), `event` (one of the three event names the CTO ruled: `new filing`, `new roster`, `new model block`), and `inputs` (the S3 key prefixes the batch reads, built with `lib.opal_naming` `key()`/`address()` or the module's own constants, never typed, each with a one-line comment citing the file and line you read it from: filings: none, its event is read by `--plan-only`; management: the filing analysis objects it reads (`filings/v1/`) and the Bloomberg officer-list prefix `bloomberg/harvest/bronze/exec_officers/` in bucket `opal-data-harvest` (the "new roster"); scores: `derived/model_block/` and `peers/v1/`).
2. `trigger.py`: a PURE function `decide(task, *, now, last_run, newest_input, would_run)` returning `(due: bool, reason: str)`; `now` and `last_run` are timezone-aware UTC datetimes or None; `newest_input` is the newest object `LastModified` among the task's input prefixes (or None); `would_run` is an int count (filings only; None elsewhere). Rules, in this order: (a) `lib.trading_calendar.is_trading_day(now.date())` false -> `(False, "not a trading day")`; (b) `last_run is None` -> `(True, "first run: no last-run record")`; (c) filings: `would_run` None -> `(False, "plan-only not read")`, `would_run > 0` -> `(True, "<n> name(s) WOULD-RUN: a new filing")`, else `(False, "no new filing")`; (d) others: `newest_input` None -> `(False, "no input object read")`, `newest_input > last_run` -> `(True, "new input <ts> after the last run <ts>: <event>")`, else `(False, "no new input since the last run")`. It reads no clock, no file and no network.
3. `inputs.py`: `newest_input(task, client)`: the max `LastModified` over `list_objects_v2` pages (a paginator, counted client-side, never one page) of the task's prefixes, via an injected S3 client; and `would_run(runner)`: runs `python -m lib.research.filings.batch --universe newest --plan-only` through an injected `runner(argv) -> (rc, stdout)` and returns the count of lines containing `WOULD-RUN` (None if rc is not 0).
4. `run.py`: `python -m lib.research.llm_batch.run <task> [--dry-run]`: reads the last-run record (a local JSON file `tmp/llm_batch/last_run.json`, gitignored runtime state, `{task: iso_utc}`), reads the event inputs, calls `decide`, prints ONE line `LLM-BATCH task=<t> due=<True|False> reason=<...>`, and only when due and not `--dry-run` runs the task's `command` through the injected runner, writing `last_run[task] = <the run's START time>` ONLY when the batch exits 0 (a failed run is not recorded, so the next day retries). `--dry-run` never runs the batch and never writes the record. Exit code: the batch's exit code when it ran, 0 otherwise.
5. `register.py`: `python -m lib.research.llm_batch.register --plan` prints, per task, `TASK <task_name> LAUNCHER <path> SCHEDULE DAILY 07:30 ENABLED=false OWNER=2.0.0_SA_COO~R1` and a final line `PLAN: 3 task(s), 0 created`; it calls NOTHING outside the process. `--apply` writes each task's Task Scheduler XML (a `<Description>` reading `AMGT_RESAPP bn-6 (G4): <event> trigger; owner 2.0.0_SA_COO~R1; created DISABLED, enabling is a separate act`, `<Enabled>false</Enabled>`, a DAILY 07:30 local trigger, the action `<launcher>`) to a temp path after FIRST querying `schtasks /Query /TN <name>` through the injected runner and REFUSING that task (rc 4, the line `EXISTS <name>: not replaced`) when it already exists (a task is never overwritten and no `/F` is ever used); for a task that does not exist it runs `schtasks /Create /TN <name> /XML <path>` through the runner, then reads the task back (`schtasks /Query /TN <name> /FO LIST /V`) and REFUSES (rc 3, and attempts `/Change /DISABLE`) if the read-back does not say `Disabled`. `--apply` is never run by this cell. A registration of a task that is not in `TASKS` is impossible by construction.
6. `launchers/run_<task>.cmd` for the three tasks (a `.cmd` in the style of `lib/research/filings/run_batch.cmd`: root derived from `%~dp0`, no device path, `python -m lib.research.llm_batch.run <task>`, `exit /b %errorlevel%`).
7. Tests in `lib/research/llm_batch/tests/` (`test_trigger.py`, `test_inputs.py`, `test_run.py`, `test_register.py`), at least these named tests: T1 not a trading day (a Saturday) is not due whatever the inputs; T2 first run is due; T3 a newer input is due with both timestamps in the reason; T4 an equal or older input is not due (the difference control: the same call with the input one second newer IS due); T5 filings: WOULD-RUN count 2 is due, 0 is not, None is not; T6 the S3 reader counts across TWO pages (a stub paginator with two pages whose newest object is on page 2); T7 `run` records `last_run` only on rc 0 and not on rc 1; T8 `--dry-run` runs nothing and writes nothing; T9 `register --plan` names all three tasks, prints `ENABLED=false` and `OWNER=2.0.0_SA_COO~R1` for each and calls no runner; T10 `--apply` with a stub runner whose read-back says `Ready` returns rc 3 and attempts the disable; T13 `--apply` against a stub whose query says the task already exists returns rc 4, prints `EXISTS <name>: not replaced` and never issues a `/Create`; T11 the table holds exactly three tasks and each `inputs` prefix is built from `lib.opal_naming` or a cited module constant (no literal bucket path of your own); T12 every `.cmd` launcher names its task and derives its root from `%~dp0`.

**Do this in order.** (1) Read the files above, then write the four test files FIRST (stub the S3 client, the runner, the clock and `schtasks`); run once: it must fail on import; record that run. (2) Write the package. (3) Run AC1 and AC2. (4) File ONE observation row for drafting and posture (not covered) and report every other premise that did not hold as a BLOCKING row. Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ`. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. No Anthropic call, no EDGAR call, no S3 call, no `schtasks` call, no network, no `pip install`, no push of shared branches. Never run `register --apply`. Never register, enable or change any task.
2. Edit only the files named in `<paths>`. Do not edit the filings, management or scores modules (read `task_definition()` and the launchers; do not change them). Non-ASCII is forbidden in the new files.

## 3. SURFACES

<paths>
lib/research/llm_batch/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~475/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <!-- the graded instance, under a short name because this order's own file name would make the canonical path pass this box's MAX_PATH: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~475/AMGT-bn-6.proof_of_spec.json` -->
  <criterion id="AC1" cell_refs="AMGT-bn-6"><invocation>cd C:/dev/wk-resapp-475 &amp;&amp; timeout 300 python -m pytest lib/research/llm_batch/tests -q 2>&amp;1 | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>a final line `<n> passed` with n at least 12 and no `failed`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bn-6"><invocation>cd C:/dev/wk-resapp-475 &amp;&amp; timeout 120 python -m lib.research.llm_batch.register --plan; echo "exit=$?"</invocation><expect>three lines each beginning `TASK OpalResearch-` and each containing `ENABLED=false` and `OWNER=2.0.0_SA_COO~R1`, the line `PLAN: 3 task(s), 0 created`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~475 <0.9.0_WK_AMGT_RESAPP~475@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~475/AMGT-bn-6.proof_of_spec.json` (THIS SHORT NAME: the block above names it) with `to_id` equal to the `<to_id>` line above, character for character; the schema's enum values are fixed (read the checker's refusal lines if it refuses; add `decomp_ref` from the order's own `<decomp_ref>` block if it asks). Run `python .tools/proof-of-spec-check.py <instance>` from `C:/dev/wk-resapp-475` on the committed bytes and report its verdict line.

Report once:
- the commit hash;
- the first (failing) run of the tests and the run after;
- AC1's and AC2's output lines;
- the diff stat, and the line of `trigger.py` for each of rules (a) to (d);
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO ruling `ledger/CTO_RULING_G4_CUT_BN6_20261015.md` @842cf564f3 on call `dell1-20261015T233836Z-7f8a` (card `ledger/CALL_G4_LLM_TIER_BATCH_TASKS_20261015.md` @bf1427d82a). THE SCOPE IS NARROWER THAN THE CARD'S "four batches", and the CTO should read it so: the card named drafting and posture; at HEAD neither has a whole-population entry (drafting: two required directories; posture: one `--security-key`), so this cell covers filings, management and scores and files the other two as an observation. The build ladder: filings and management already own `task_definition()` and filings already owns the `--plan-only` skip-on-unchanged read; this cell adds the trigger, the scores task, the launchers and the registration. Only filings and management make Anthropic model calls (scores is S3 reads and math, `run_scores.py` header: "NO VENDOR CALL"); the ENABLE pair names the first fire's measured spend and a stop figure (the CTO's ruling) and the stop is `schtasks /Change /TN <task> /DISABLE`. The host is dell1 (Andrew-direct 2026-10-14 ~18:5xZ placement). The tasks fire DAILY 07:30 local and the trigger decides: a daily schedule gated by an input check, never success-of-upstream as the trigger. The apply and the enable are NOT this order.

<status>pending</status>
<round>107</round>
<slot>0.9.0_WK_AMGT_RESAPP~475</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

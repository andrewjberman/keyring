# AMGT_RESAPP task order -- `AMGT-cf-1` (PART A, MERGED) AND `AMGT-cf-6` (PART B, YOURS) -- THE LLM-BATCH ENTRY READS THE MODEL KEY IN-PROCESS FROM SECRETS MANAGER; THE FILINGS LAUNCHER RUNS THE BATCH ON PYTHON 3.12, WHERE THE PINNED ANTHROPIC SDK IS INSTALLED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-cf-1,AMGT-cf-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~527</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-cf-1.the-filings-entry-reads-the-model-key-in-process-from-secrets-manager</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the scheduled task `OpalResearch-FilingsAnalyzer` already exists and is not changed; this order edits the entry script it runs (Part A, merged) and the batch file it runs (Part B) and tests of them; the deliberate on-demand proof run is the issuer's cell `AMGT-cf-5`.
comp-iam: DECLARED-NOT-APPLICABLE -- Part A adds a Secrets Manager read in code only (`secretsmanager:GetSecretValue` on the secret `anthropic-api-key`, the estate's existing read path for this key); Part B changes one launcher line; no IAM policy, role or grant is created or changed here.
comp-adversary: RUN at the re-open (2026-10-19): AC1 (Part A's 8 tests) PASSES at the base `8de2494a24`+ as a control; AC2 (Part B's new test file) fails at the base (the file is absent, pytest exit 4); AC3 reads `68 passed` at the base and its floor P is unmet there as expected. EGRESS CLASS, declared: NONE (every test stubs the Secrets Manager call and the child process, and Part B's tests run a COPY of the launcher in a temporary tree against a stub module; no AWS call, no model call and no store write).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-527` (branch `wk-AMGT_RESAPP-527`, cut from the re-open commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-527`. This is Windows: the launcher is a `.cmd` file run by `cmd.exe`.

**THIS ORDER WAS RE-OPENED BY ITS ISSUER (2.0.0_SA_COO~R1, 2026-10-19 ~19:5xZ) AND YOU ARE A RE-SEATED WORKER ON THE SAME SLOT.** PART A (`AMGT-cf-1`) is DONE and MERGED: commit `12fbb5be83` on the old branch, landed as `8de2494a24`, present in your tree. It added `ANTHROPIC_SECRET_ID`, `KEY_TASKS`, `KeyReadError`, `read_anthropic_key` and `keyed_runner` to `lib/research/llm_batch/run.py` and `lib/research/llm_batch/tests/test_key_read.py` (8 tests, all passing). **Do NOT redo or edit Part A**; its 8 tests must keep passing. Your whole job is PART B below. The old receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~527/CF1_RECEIPT.md` stays as it is; write your own `CF6_RECEIPT.md` beside it.

**THREE LESSONS THAT BIND YOUR TESTS.** (1) A new check is dry-run at the base first: your new test file runs ONCE on the unedited head and must FAIL on the new behaviour and PASS on every control; record the counts. (2) The regexes in your tests are raw strings. (3) Name the proof instance by the order's FULL name (`<to_id>.proof_of_spec.json`); it OVERWRITES the existing instance of that name (the old one recorded Part A only).

## 1. PART B -- THE CELL `AMGT-cf-6` (round 124, decomposition s.133a; the CTO's ruling, msg 8499: option B)

**Why.** The scheduled task `OpalResearch-FilingsAnalyzer` runs `lib/research/llm_batch/launchers/run_filings.cmd`, whose command line is `python -m lib.research.llm_batch.run filings`. On this box `python` resolves to Python 3.14.7 with `anthropic 0.45.0` installed; with Part A merged the key guard no longer blocks, and the batch's model call fails inside the SDK's stream parser on that interpreter (a `TypeError` on `output_config`, then an `AttributeError` in `anthropic/_models.py`; row `AMGT_RESAPP-D1-S62`). The repo pins `anthropic==0.84.0`; Python 3.12.10 on the same box (`py -3.12`) already holds `anthropic 0.84.0`, imports `lib.research.filings.batch` and `lib.research.llm_batch.run`, and its `Messages.stream` takes `output_config`. A package install into 3.14 is guarded and is NOT done. The ruling, quoted: *"cf-6: run_filings.cmd calls `py -3.12`, the launcher test asserts the interpreter ... The other two llm_batch launchers on 3.14 take a surprise row naming the same SDK mismatch, so this cell does not widen."*

**What is true today (verify at Step A).** `run_filings.cmd` has its command on line 21 (as of the re-open commit): `python -m lib.research.llm_batch.run filings >>"%LOG%" 2>&1`; lines 1 to 20 build the dated log; line 22 appends `exit=%errorlevel%`. `lib/research/llm_batch/tasks.py` builds the batch command from `sys.executable`, so the child process of `run.py` uses whatever interpreter ran `run.py`: changing the launcher's one line moves the whole chain to 3.12. `lib/research/llm_batch/tests/test_launcher_capture.py` runs a COPY of the launcher inside a temporary tree against a stub MODULE `lib/research/llm_batch/run.py` (cwd shadows the real package), and its constant `COMMAND_LINE` (line 16) holds the old command line; test T5 asserts the launcher still contains it.

**The rule to build.**
(a) In `run_filings.cmd` change ONLY the command on line 21 to `py -3.12 -m lib.research.llm_batch.run filings >>"%LOG%" 2>&1` (the redirect, the `echo exit=` line, the cd guard, the stamp and the log name are byte-identical), and add ONE comment line (`REM AMGT-cf-6: ...`) in the existing REM block saying the batch runs on Python 3.12 because the pinned anthropic SDK is installed there and the 3.14 one is not.
(b) `test_launcher_capture.py`: update the constant `COMMAND_LINE` to `py -3.12 -m lib.research.llm_batch.run filings` (T5 keeps asserting the launcher contains it) and change nothing else in that file except what this change forces; its stub module prints one more line, `py=<major>.<minor>` read from `sys.version_info`, so the interpreter that ran it is visible in the log.
(c) A NEW file `lib/research/llm_batch/tests/test_launcher_interpreter.py` with the tests below.

**Do this in order.** (A) `cd C:/dev/wk-resapp-527`; `git log -1 --format=%h`; read `run_filings.cmd` and `test_launcher_capture.py` (its `_tree`, `_run`, `_logs` helpers are importable or copyable). Confirm with `py -3.12 --version` that the 3.12 interpreter is present (print the line in the receipt). (B) Write `test_launcher_interpreter.py` FIRST and run it ONCE on the unedited head: record the counts (it must fail on the interpreter assertion and pass its controls). (C) Build (a) and (b); re-run. (D) Run `lib/research/llm_batch/tests` once at the base and once after. (E) AC1 to AC3, the receipt, the instance and proof-of-spec-check. **Do NOT run the real batch or the real launcher from the repo root**; the tests run a copy in a temporary tree.

**Tests (`test_launcher_interpreter.py`; hand-written expectations; reuse the temporary-tree approach of `test_launcher_capture.py`, with a stub module that writes `py=<major>.<minor>` to stdout and exits with a code the test chooses):** T1 run the copied launcher: the log contains the line `py=3.12` (the interpreter that ran the stub is 3.12) and the launcher's exit code equals the stub's exit code (use 0 and 7 in two cases); T2 the launcher file contains the exact text `py -3.12 -m lib.research.llm_batch.run filings` and does NOT contain a line that starts with `python ` (the old command); T3 CONTROL: the log keeps its first line `launcher start `, its `exit=<code>` last line, and its name matches the raw regex `^filings_\d{8}T\d{6}Z\.log$`; T4 CONTROL: `run_management.cmd` and `run_scores.cmd` are byte-identical to the base (sha256 as the constants in `test_launcher_capture.py` hold them).

## 2. BOUNDS

1. Write only the paths below. No deploy, no Terraform, no store write, no schedule change (the scheduled task is NOT edited, enabled, disabled or run), no AWS call, no SEC, vendor, model or Bloomberg call; NO `pip install` and no change to any installed package or environment variable; nothing is fetched from the internet. No push; never touch `DEV` or `PROD`; commit nothing under `portal/` or `org/devices/`.
2. Product edit: `lib/research/llm_batch/launchers/run_filings.cmd` ONLY. Pure ASCII. Do NOT edit `run.py` (Part A is merged), `run_management.cmd`, `run_scores.cmd`, `tasks.py` or anything under `lib/research/filings/`.
3. The real `tmp/llm_batch/` directory of the repo root is NOT created or written by your tests or your checks.
4. Never print, log, write or commit a real key; the only key-shaped value in any file is the fake test value of Part A's tests.

## 3. SURFACES

<paths>
lib/research/llm_batch/launchers/run_filings.cmd
lib/research/llm_batch/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~527/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; three criteria: the merged Part A control, Part B's built behaviour, the directory floor)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-cf-1"><invocation>cd C:/dev/wk-resapp-527 &amp;&amp; timeout 120 python -m pytest lib/research/llm_batch/tests/test_key_read.py -q -p no:cacheprovider --color=no; echo "exit=$?"</invocation><expect>the pytest summary line reads `8 passed` with 0 failed and 0 skipped (Part A's T1 to T8, unchanged), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-cf-6"><invocation>cd C:/dev/wk-resapp-527 &amp;&amp; timeout 120 python -m pytest lib/research/llm_batch/tests/test_launcher_interpreter.py -q -p no:cacheprovider --color=no; echo "exit=$?"</invocation><expect>the pytest summary line reads `5 passed` or more with 0 failed and 0 skipped (T1 in both exit-code cases, T2, T3, T4 each present by name), and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-cf-1,AMGT-cf-6"><invocation>cd C:/dev/wk-resapp-527 &amp;&amp; timeout 120 python -m pytest lib/research/llm_batch/tests -q -p no:cacheprovider --color=no 2&gt;&amp;1 | tail -2</invocation><expect>the summary reads `P passed` with P at least 73 (the base reads `68 passed`) and no `failed` and no `error` in it</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~527 <0.9.0_WK_AMGT_RESAPP~527@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~527/CF6_RECEIPT.md` with the sections `## What changed` (every path, with line counts, and the final text of the launcher), `## Tests` (T1 to T4, the base counts and the after counts) and `## Not verified` (the scheduled task itself is not run here: the issuer's `AMGT-cf-5` runs it once on demand after the merge; `py.exe` availability under the task's user is read there). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~527/AMGT_RESAPP.TO-AMGT-cf-1.the-filings-entry-reads-the-model-key-in-process-from-secrets-manager.proof_of_spec.json` (the invocations are recorded as the order's literal text). Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line. Do not stage `portal`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W527-S<k>`, **`disarm_owner` `2.0.0_SA_COO~R1` on EVERY row (a row without it is refused by the gate)**.

Report once: the commit hash and the base; the test run at the base and after; AC1 to AC3 output lines; the final launcher text; the proof verdict line; any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Part A: item 1 of the CTO's round-123 analysis (`ledger/ROUND_ANALYSIS.round123.R1.md`, msg 8492, `@980ad8c80c`) and his msgs 8275 and 8353; merged `8de2494a24`, order flipped complete `9f1d0d34cc`. Part B: the CTO's msg 8499 (option B) after row `AMGT_RESAPP-D1-S62`; decomposition `s.133a`. A NEW order file for cf-6 was refused by `.tools/to-pipeline-gate.py` (ONE ISSUER PER ROUND is keyed to the round: a re-cut into the first issuance modifies its orders and adds no file), so the issuer RE-OPENED this order and extended it (status `complete` -> `pending`, `owned_cells` gains `AMGT-cf-6`, criteria 3). The grade of the whole is the issuer's `AMGT-cf-5`: one further deliberate `schtasks /run` reads rc=0, objects written and 0 key-prefix greps; no third run if it fails (msg 8497 condition 3 kept by 8499).

<status>complete</status>
<round>124</round>
<slot>0.9.0_WK_AMGT_RESAPP~527</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>

# AMGT_RESAPP task order -- `AMGT-ce-2` -- THE FILINGS LAUNCHER WRITES ITS STDOUT, STDERR AND EXIT CODE TO A DATED LOG BESIDE `last_run.json`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ce-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~526</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ce-2.the-filings-launcher-writes-its-output-and-exit-code-to-a-dated-log</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the scheduled task `OpalResearch-FilingsAnalyzer` already exists and is not changed; this cell edits the batch file it runs and a test of that file against a stub; the on-demand proof run is the issuer's cell `AMGT-ce-5`.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no read or write path changes beyond a local log file.
comp-adversary: RUN at the cut (2026-10-19): AC1 at the base fails (the test file is absent, pytest exit 4); AC2 at the base reads `54 passed` and its floor P is unmet there as expected. EGRESS CLASS, declared: NONE (the tests run the launcher against a STUB `python` on a temporary PATH; the real batch, the model and the store are never called).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-526` (branch `wk-AMGT_RESAPP-526`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-526`. This is Windows: the launcher is a `.cmd` file run by `cmd.exe`; run it from your shell with `cmd //c` (Git Bash) or from Python with `subprocess.run(["cmd", "/c", path], ...)`.

## 1. THE CELL -- `AMGT-ce-2` (round 123, decomposition s.132 item 3; the CTO's ruling msg 8275)

**Why.** The scheduled task `OpalResearch-FilingsAnalyzer` ran `lib/research/llm_batch/launchers/run_filings.cmd` at 07:30 local on 2026-10-19 and returned `LastResult=1`, wrote no store object, and left no `tmp/llm_batch/last_run.json`. The launcher discards its output, so nobody can read why. The ruling: *"`run_filings.cmd` writes its stdout, stderr and exit code to a dated log beside `last_run.json`."*

**What is true today (verify at Step A).** `lib/research/llm_batch/launchers/run_filings.cmd` is six lines: `@echo off`, a comment block, `cd /d "%~dp0..\..\..\.."` (the batch file sits four levels under the workspace root, so `%~dp0..\..\..\..` is the root), `if errorlevel 1 exit /b 1`, `python -m lib.research.llm_batch.run filings`, `exit /b %errorlevel%`. `lib/research/llm_batch/run.py` writes `tmp/llm_batch/last_run.json` (`STATE_PATH`, line 24) on success only and writes its decision and failure lines to stderr. The Python in this box is on PATH as `python`.

**The rule to build (edit `run_filings.cmd` ONLY; keep its comment block, update it to say the log exists).**
(a) After the `cd /d`, create `tmp\llm_batch` if it does not exist.
(b) Compute a UTC stamp `YYYYMMDDTHHMMSSZ` WITHOUT calling `python` (the stamp must not depend on the thing being diagnosed; use `powershell -NoProfile -Command "..."` or `wmic`-free Windows facilities; never `%DATE%`, which is locale-dependent). If the stamp comes back empty, use the literal `nostamp`.
(c) The log is `tmp\llm_batch\filings_<stamp>.log`. Its first line is `launcher start <stamp> cwd=<the working directory>`. Then the command `python -m lib.research.llm_batch.run filings` runs with BOTH stdout and stderr redirected into the log (append). When it ends, the launcher appends one line `exit=<the command's exit code>` and exits with THAT code (not 0, not 1).
(d) If the `cd /d` fails, the launcher appends `launcher: cd failed` to `%TEMP%\opal_filings_launcher_cd_failed.log` and exits 1 (no workspace root means no `tmp\llm_batch`).
(e) No other behaviour changes: the command line is byte-identical to today's (`python -m lib.research.llm_batch.run filings`), the other two launchers (`run_management.cmd`, `run_scores.cmd`) and `run.py` are NOT edited.

**Do this in order.** (A) `cd C:/dev/wk-resapp-526`; `git log -1 --format=%h`; read `run_filings.cmd`, `lib/research/llm_batch/run.py` and one existing test (`lib/research/llm_batch/tests/test_run.py`) for the house style. (B) Write `lib/research/llm_batch/tests/test_launcher_capture.py` FIRST (tests below) and run it ONCE on the unedited head: record the counts (it must fail on the capture tests and pass the controls). (C) Build (a) to (e); re-run. (D) Run `lib/research/llm_batch/tests` once at the base and once after. (E) AC1 and AC2, the receipt, the instance and proof-of-spec-check. **Do NOT run the real batch** (`python -m lib.research.llm_batch.run filings` without `--dry-run` spends money and writes the store), and do not run the real launcher from the repo root: the tests run a COPY of the launcher inside a temporary tree.

**Tests (`test_launcher_capture.py`; hand-written expectations; every case builds a temporary tree `tmp_path/a/b/c/d/run_filings.cmd` by copying the real launcher from its repo path, so `%~dp0..\..\..\..` resolves to `tmp_path`, and a stub directory `tmp_path/stub` holding `python.cmd` that prints `stub-out` to stdout, `stub-err` to stderr and does `exit /b <code>`; the test runs `cmd /c <copy>` with `PATH` = the stub directory first, then the original PATH, and `TEMP` pointed at `tmp_path/temp`; the real `python` is never reached by the capture path):** T1 a stub exiting 7: the launcher's exit code is 7, exactly one `tmp_path/tmp/llm_batch/filings_*.log` exists, it contains `stub-out`, `stub-err` and a line `exit=7`, and its first line starts with `launcher start `; T2 a stub exiting 0: the launcher exits 0 and the log ends with `exit=0`; T3 the log name matches the raw regex `^filings_\d{8}T\d{6}Z\.log$`; T4 two runs make two log files (a log is never overwritten) or one file with two `launcher start` lines (state which in the receipt; the rule is that no earlier run's text is lost); T5 CONTROL: the real launcher file still contains the exact command line `python -m lib.research.llm_batch.run filings` and the files `run_management.cmd` and `run_scores.cmd` are byte-identical to the base (compare against `git show HEAD:<path>` taken at test time with `subprocess`, or against the sha256 you record at Step B); T6 `cd` failure: running the launcher copy with a path whose parent chain has fewer than four levels (a copy at `tmp_path/run_filings.cmd`) exits 1 and appends `launcher: cd failed` to `tmp_path/temp/opal_filings_launcher_cd_failed.log`, OR, if `cmd` resolves the relative path above `tmp_path` successfully on this box, record in the receipt that T6 is replaced by a documented manual read and why (do not leave a test that depends on the box's directory layout).

## 2. BOUNDS

1. Write only the paths below. No deploy, no Terraform, no store write, no schedule change (the scheduled task is NOT edited, enabled, disabled or run), no SEC, vendor, model or Bloomberg call; no `pip install`; nothing is fetched from the internet. No push; never touch `DEV` or `PROD`; commit nothing under `portal/` or `org/devices/`.
2. Product edit: `lib/research/llm_batch/launchers/run_filings.cmd` ONLY. Pure ASCII (no non-ASCII character in the batch file or the tests).
3. The real `tmp/llm_batch/` directory of the repo root is NOT created or written by your tests or your checks.

## 3. SURFACES

<paths>
lib/research/llm_batch/launchers/run_filings.cmd
lib/research/llm_batch/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~526/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ce-2"><invocation>cd C:/dev/wk-resapp-526 &amp;&amp; timeout 120 python -m pytest lib/research/llm_batch/tests/test_launcher_capture.py -q -p no:cacheprovider --color=no; echo "exit=$?"</invocation><expect>the pytest summary line reads `5 passed` or more with 0 failed and 0 skipped (T1 to T5 each present by name; T6 present or replaced as the test text states), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ce-2"><invocation>cd C:/dev/wk-resapp-526 &amp;&amp; timeout 120 python -m pytest lib/research/llm_batch/tests -q -p no:cacheprovider --color=no 2&gt;&amp;1 | tail -2</invocation><expect>the summary reads `P passed` with P at least 59 (the base reads `54 passed`) and no `failed` and no `error` in it</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~526 <0.9.0_WK_AMGT_RESAPP~526@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~526/CE2_RECEIPT.md` with the sections `## What changed` (every path, with line counts, and the final text of the launcher), `## Tests` (T1 to T6 and how each was exercised, the base counts and the after counts), and `## Not verified` (the scheduled task itself is not run here: the issuer's `AMGT-ce-5` runs it once on demand after the merge; `%DATE%`-free stamp tested only on this box's PowerShell). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~526/AMGT_RESAPP.TO-AMGT-ce-2.the-filings-launcher-writes-its-output-and-exit-code-to-a-dated-log.proof_of_spec.json` (the invocations are recorded as the order's literal text). Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line. Do not stage `portal`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W526-S<k>`, **`disarm_owner` `2.0.0_SA_COO~R1` on EVERY row (a row without it is refused by the gate)**.

Report once: the commit hash and the base; the test run at the base and after; AC1 and AC2 output lines; the final launcher text; the proof verdict line; any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Item 1 of the CTO's round-122 analysis (`ledger/ROUND_ANALYSIS.round122.R1.md`, msg 8323, `@3583db8527`) and his msg 8275. The deliberate proof (`AMGT-ce-5`, `schtasks /run` of `OpalResearch-FilingsAnalyzer`) is the issuer's act after this merges into the shared tree (the scheduled task runs `C:\dev\ajb_workspace\lib\research\llm_batch\launchers\run_filings.cmd`, so the merged file is what it runs); the Tue 2026-10-20 07:30 local organic fire is the negative arm. LOCAL code cell.

<status>complete</status>
<round>123</round>
<slot>0.9.0_WK_AMGT_RESAPP~526</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>

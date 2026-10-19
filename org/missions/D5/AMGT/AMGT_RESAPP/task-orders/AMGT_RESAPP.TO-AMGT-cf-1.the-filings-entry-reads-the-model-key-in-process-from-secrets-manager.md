# AMGT_RESAPP task order -- `AMGT-cf-1` -- THE LLM-BATCH ENTRY SCRIPT READS THE MODEL KEY IN-PROCESS FROM SECRETS MANAGER, FOR THE FILINGS COMMAND ONLY, AND HANDS IT TO THE CHILD'S ENVIRONMENT ONLY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-cf-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~527</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-cf-1.the-filings-entry-reads-the-model-key-in-process-from-secrets-manager</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the scheduled task `OpalResearch-FilingsAnalyzer` already exists and is not changed; this cell edits the entry script it runs (through the launcher) and a test of it; the deliberate on-demand proof run is the issuer's cell `AMGT-cf-5`.
comp-iam: DECLARED-NOT-APPLICABLE -- the cell adds a Secrets Manager read in code only (`secretsmanager:GetSecretValue` on the secret `anthropic-api-key`, the estate's existing read path for this key); no IAM policy, role or grant is created or changed here, and whether the task's Windows user holds AWS credentials is read by the issuer's `AMGT-cf-5` run (the CTO's ruling: if it does not, that becomes a row).
comp-adversary: RUN at the cut (2026-10-19): AC1 at the base fails (the test file is absent, pytest exit 4); AC2 at the base reads `60 passed` and its floor P is unmet there as expected. EGRESS CLASS, declared: NONE (every test stubs the Secrets Manager call and the child process; no AWS call, no model call and no store write).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-527` (branch `wk-AMGT_RESAPP-527`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-527`.

**THREE LESSONS THAT BIND YOUR TESTS.** (1) A new check is dry-run at the base first: your test file runs ONCE on the unedited head and must FAIL on the new behaviour and PASS on every control; record the counts. (2) The regexes in your tests are raw strings. (3) Name the proof instance by the order's FULL name (`<to_id>.proof_of_spec.json`).

## 1. THE CELL -- `AMGT-cf-1` (round 124, decomposition s.133 item 1; row `AMGT_RESAPP-D1-S61`; the CTO's rulings, messages 8275 and 8353)

**Why.** The scheduled task `OpalResearch-FilingsAnalyzer` runs `lib/research/llm_batch/launchers/run_filings.cmd`, which runs `python -m lib.research.llm_batch.run filings`. The on-demand run of 2026-10-19 15:30Z returned rc=1 with the launcher's log naming the cause: `BLOCKED: ANTHROPIC_API_KEY is not in the environment` (the batch's model call, `lib/research/filings/analyze.py:328`, requires that variable; no code on the scheduled path puts it there). The CTO's ruling, quoted: *"When ANTHROPIC_API_KEY is absent, the filings entry script reads it in-process with boto3 secretsmanager get_secret_value, the estate's pattern (lib/opal_data_harvest/ocilar_hcaptcha.py:67). The secret id is named from comp-secrets list. Not `comp-secrets get --reveal` in run_filings.cmd: since ce-2, that launcher's stdout goes to a log, so a reveal there leaks."* The secret id is `anthropic-api-key` (read from `comp-secrets list`: firm `shared`, a plain opaque string, not JSON).

**What is true today (verify at Step A, cite `path:line`).** `lib/research/llm_batch/run.py`: `default_runner(argv)` (line ~131) is `subprocess.run(list(argv), cwd=ROOT, stdout=PIPE, universal_newlines=True, encoding="utf-8", errors="replace")` returning `(returncode, stdout)`; it inherits this process's environment. `run_task(...)` (line ~100) calls `runner` for the real command ONLY when the task is due and not `--dry-run`, and (for a `plan_only` task such as `filings`) `inputs.would_run(runner, keys)` also calls the SAME runner for the read-only count whose argv carries `--plan-only`. `main()` (line ~143) passes `runner=default_runner`. The pattern to follow is `lib/opal_data_harvest/ocilar_hcaptcha.py` lines 61-79 (`read_key(secrets=None)`: a `secrets` callable seam for tests; the default is `boto3.client("secretsmanager", region_name="us-east-1").get_secret_value(SecretId=...)["SecretString"]`; an error message names the secret id and the exception TYPE, never the value).

**The rule to build (edit `lib/research/llm_batch/run.py` ONLY).**
(a) Module constants `ANTHROPIC_SECRET_ID = "anthropic-api-key"` and `KEY_TASKS = frozenset({"filings"})`.
(b) `class KeyReadError(Exception)` and `read_anthropic_key(secrets=None) -> str`, following the ocilar pattern: `secrets` is a callable `(secret_id) -> SecretString` (default: boto3 Secrets Manager, us-east-1, imported INSIDE the default); the value is the raw SecretString, stripped; any exception from `secrets` becomes `KeyReadError("could not read <secret id> from Secrets (<ExceptionTypeName>)")` (NEVER the exception's own message, which may carry text); an empty or non-string value becomes `KeyReadError("secret <secret id> has no usable value")`.
(c) `keyed_runner(task_key, *, secrets=None, run=subprocess.run, environ=None)` returns a runner `(argv) -> (rc, out)`. `environ` defaults to `os.environ`. For an argv that contains `--plan-only`, or when `task_key` is not in `KEY_TASKS`, or when `environ` already holds a non-empty `ANTHROPIC_API_KEY`: it behaves EXACTLY like `default_runner` (same call, same `cwd=ROOT`, no `env=` argument, no secret read). Otherwise it reads the key once (cached for the runner's life) and runs the child with `env=dict(environ, ANTHROPIC_API_KEY=<key>)`, same `cwd`, `stdout=PIPE`, `universal_newlines=True`, `encoding="utf-8"`, `errors="replace"`; the returned `out` has every occurrence of the key replaced by `***`. If the read raises `KeyReadError`: write ONE line to stderr `LLM-BATCH task=<task_key> key read FAILED: <the KeyReadError text>`, do NOT run the child, return `(1, "")` (so `last_run` is not recorded and the next due day retries).
(d) `main()` passes `runner=keyed_runner(args.task)` instead of `default_runner`. `default_runner` stays, unchanged, and the existing tests keep passing it.
(e) The key is NEVER written to a file, NEVER printed (not in the decision line, not on stderr), NEVER put in argv, and NEVER set in this process's own `os.environ`. It travels in the child's `env=` dict only.

**Do this in order.** (A) `cd C:/dev/wk-resapp-527`; `git log -1 --format=%h`; read `run.py`, `lib/opal_data_harvest/ocilar_hcaptcha.py` lines 55-80 and `lib/research/llm_batch/tests/test_run.py` (house style: stub runners, `monkeypatch`, plain asserts). (B) Write `lib/research/llm_batch/tests/test_key_read.py` FIRST (tests below) and run it ONCE on the unedited head: record the counts (it must fail on the new behaviour). (C) Build (a) to (e); re-run. (D) Run `lib/research/llm_batch/tests` once at the base and once after. (E) AC1 and AC2, the receipt, the instance and proof-of-spec-check. **Do NOT call AWS, do not run the real batch** (`python -m lib.research.llm_batch.run filings` without `--dry-run` spends money and writes the store); every test stubs `secrets` and `run`.

**Tests (`test_key_read.py`; hand-written expectations; the stub `run` records its argv and keyword arguments and returns an object with `.returncode` and `.stdout`; the stub `secrets` records its calls and returns a fixed fake value such as `sk-test-FAKEKEY-0123456789`):** T1 filings, real-command argv (no `--plan-only`), `environ` without the variable: `secrets` is called exactly once with `anthropic-api-key`, the child's `env` carries `ANTHROPIC_API_KEY` equal to the fake value, the argv is passed unchanged, and the test process's own `os.environ` still lacks the variable; T2 `environ` already holds a non-empty key: `secrets` is not called and `run` gets no `env=` keyword; T3 an argv containing `--plan-only`: `secrets` not called, no `env=`; T4 task `scores` (not in `KEY_TASKS`): `secrets` not called; T5 `secrets` raises `RuntimeError("deny-PAYLOAD-xyz")`: the runner returns `(1, "")`, `run` is never called, the captured stderr names `anthropic-api-key` and `RuntimeError` and does NOT contain `deny-PAYLOAD-xyz`; T6 `secrets` returns an empty string: `(1, "")`, `run` not called; T7 the stub child prints the fake value inside its stdout: the returned `out` contains `***` and does not contain the fake value, and the captured stderr never contains it; T8 CONTROL: `run.main(["filings", "--print-command"])` still returns 0 and prints a `LLM-BATCH task=filings command=` line while `read_anthropic_key` is monkeypatched to raise `AssertionError` (a print-only call must never read the secret).

## 2. BOUNDS

1. Write only the paths below. No deploy, no Terraform, no store write, no schedule change (the scheduled task is NOT edited, enabled, disabled or run), no AWS call, no SEC, vendor, model or Bloomberg call; no `pip install`; nothing is fetched from the internet. No push; never touch `DEV` or `PROD`; commit nothing under `portal/` or `org/devices/`.
2. Product edit: `lib/research/llm_batch/run.py` ONLY. Do NOT edit `lib/research/filings/` (its module text records that the key reaches that package only as `ANTHROPIC_API_KEY` from its caller; this cell makes the caller do that), `run_filings.cmd`, `tasks.py` or `inputs.py`. Pure ASCII.
3. Never print, log, write or commit a real key; the only key-shaped value in any file is the fake test value.

## 3. SURFACES

<paths>
lib/research/llm_batch/run.py
lib/research/llm_batch/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~527/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-cf-1"><invocation>cd C:/dev/wk-resapp-527 &amp;&amp; timeout 120 python -m pytest lib/research/llm_batch/tests/test_key_read.py -q -p no:cacheprovider --color=no; echo "exit=$?"</invocation><expect>the pytest summary line reads `8 passed` or more with 0 failed and 0 skipped (T1 to T8 each present by name), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-cf-1"><invocation>cd C:/dev/wk-resapp-527 &amp;&amp; timeout 120 python -m pytest lib/research/llm_batch/tests -q -p no:cacheprovider --color=no 2&gt;&amp;1 | tail -2</invocation><expect>the summary reads `P passed` with P at least 68 (the base reads `60 passed`) and no `failed` and no `error` in it</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~527 <0.9.0_WK_AMGT_RESAPP~527@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~527/CF1_RECEIPT.md` with the sections `## What changed` (every path, with line counts, and the final text of every function you added), `## Tests` (T1 to T8, the base counts and the after counts) and `## Not verified` (the real Secrets Manager call is never made here: the issuer's `AMGT-cf-5` runs the scheduled task once on demand after the merge and reads rc, objects and a grep for the key's prefix; whether the task's Windows user holds AWS credentials is read there). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~527/AMGT_RESAPP.TO-AMGT-cf-1.the-filings-entry-reads-the-model-key-in-process-from-secrets-manager.proof_of_spec.json` (the invocations are recorded as the order's literal text). Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line. Do not stage `portal`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W527-S<k>`, **`disarm_owner` `2.0.0_SA_COO~R1` on EVERY row (a row without it is refused by the gate)**.

Report once: the commit hash and the base; the test run at the base and after; AC1 and AC2 output lines; the final text of the functions you added; the proof verdict line; any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Item 1 of the CTO's round-123 analysis (`ledger/ROUND_ANALYSIS.round123.R1.md`, msg 8492, `@980ad8c80c`) and his msgs 8275 and 8353. The grade is the issuer's `AMGT-cf-5`: one deliberate `schtasks /run` of `OpalResearch-FilingsAnalyzer` reads rc=0, objects written and 0 key-prefix greps over the run's log and the repo; the Tue 2026-10-20 07:30 local fire is the negative arm. WORLD class for the run; this code cell is LOCAL.

<status>pending</status>
<round>124</round>
<slot>0.9.0_WK_AMGT_RESAPP~527</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>

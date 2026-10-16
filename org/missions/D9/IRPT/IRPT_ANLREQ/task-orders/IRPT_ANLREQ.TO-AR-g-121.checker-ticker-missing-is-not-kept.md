# TO-AR-g-121 -- the default yfinance port reads a ticker-missing exception as a clean empty answer, so an unknown symbol is NOT_KEPT and never CHECK_FAILED (C-SWAP step 2)

<to_id>IRPT_ANLREQ.TO-AR-g-121</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~258</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>36</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-121` (`decompositions/IRPT_ANLREQ_DECOMP_R36_G.md`) |
**outcome_ref:** FWD-1 run 3 (C-SWAP step 2, the served checker) | **depends_on:** `AR-y-292` (`intake/yfinance_check.py`, merged). Order: CTO msgs 9283 and 9291.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~258`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-258` (branch `wk-IRPT_ANLREQ-258`), provisioned by the issuer with `infra/`, `docs/`, `data/`, `lib/`, `org/standards` and the project folder on disk. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~258 <0.9.0_WK_IRPT_ANLREQ~258@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either. (A provisioner error about a portal sub-worktree does not concern you.)
- A row id has the form `IRPT_ANLREQ-D2-W258-S<k>` (take the next free `<k>`; check the channel file for `W258` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network (yfinance is never imported or called by your tests), no install. Scratch outside the product tree.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`).

### Read first (under `C:/dev/wk-irpt-anlreq-258/infra/aws/lambda/investor-reporting/intake/`)

- `yfinance_check.py` (`default_history`, `_failure_reason`, `ErrorFrame`, `YfinanceChecker._check_one`) and `tests/test_yfinance_check.py` (the helper `fake_yfinance(behaviour, observed)`: its `("raise", exc)` case raises exc only while `config.debug.hide_exceptions` is False, which `default_history` sets for the call).
- The real exception classes, read-only, at `C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/yfinance_exceptions_1_2_0.py` (the yfinance 1.2.0 wheel's own `exceptions.py`: `YFTickerMissingError`, its subclasses `YFTzMissingError` and `YFPricesMissingError`, `YFDataException`, `YFRateLimitError`).

### THE CELL (`AR-g-121`, inlined)

The served door answered TICKER_CHECK_FAILED for symbols yfinance has no data for. Cause: `default_history` sets `hide_exceptions` False, and yfinance 1.2.0 then RAISES `YFTzMissingError` or `YFPricesMissingError` (subclasses of `YFTickerMissingError`) for a symbol Yahoo has no data for; the port lets it out; `_failure_reason` files EXCEPTION; the verdict is CHECK_FAILED instead of NOT_KEPT. SPY works; an unknown or delisted symbol never can.

**`intake/yfinance_check.py`, exactly this, and nothing else in the file:**
1. A new module-level function `_is_ticker_missing(exc)` returning True when any class in `type(exc).__mro__` has `__name__ == "YFTickerMissingError"` (an exact name, never a substring; a docstring says it covers `YFTzMissingError` and `YFPricesMissingError`). It is placed immediately before `default_history`.
2. In `default_history`, wrap ONLY the `yf.Ticker(symbol).history(period="1mo", auto_adjust=False)` call in `try/except Exception as exc`: `if _is_ticker_missing(exc): return []` (a clean empty answer, which the checker reads as NOT_KEPT, reason NO_ROWS), else `raise`. The `finally` that restores `hide_exceptions` stays and still runs; the hidden-error-frame path (`ErrorFrame`) is unchanged. A comment at the `return []` says why (the yfinance class means the symbol has no data; every other exception, a rate limit included, stays a failed check so an outage never reads as "ticker does not exist").
3. No other change: not `_failure_reason`, not the cap or pace, not `check()`.

**Fixture.** A NEW file `intake/tests/fixtures/yfinance_exceptions_1_2_0.py`: an exact byte copy of the real file named above (`cp`, then `cmp` it; do not retype it). Create the `fixtures` folder if absent.

**Tests**, appended to `intake/tests/test_yfinance_check.py` (it keeps its existing 24 or so tests untouched), with these exact function names (the issuer's check looks for the fixture's name in the file, and the CTO's three outcomes by behaviour):
- a small loader `_real_exceptions()` that loads the fixture with `importlib.util.spec_from_file_location` (module name `yfinance_exceptions_real`);
- `test_default_port_ticker_missing_error_reads_not_kept_no_rows` (parametrised over `YFTzMissingError("ZQXWVK")` and `YFPricesMissingError("ZQXWVK", "(1mo)")`, raised through `fake_yfinance` with `("raise", exc)`; assert `state` NOT_KEPT, `reason` NO_ROWS, `rows` 0, and that `hide_exceptions` is True again afterwards);
- `test_default_port_rate_limit_error_stays_check_failed_pushback` (`YFRateLimitError()`; assert CHECK_FAILED, reason PUSHBACK, and a second symbol in the same call is NOT_CHECKED, reason STEP_STOPPED);
- `test_default_port_other_exceptions_stay_check_failed_exception` (parametrised over `YFDataException("down")`, `RuntimeError("boom")`, `ConnectionError("reset")` and a locally defined `class YFTickerMissingErrorLike(ValueError)`; assert CHECK_FAILED, reason EXCEPTION);
- `test_default_port_rows_read_kept` (22 rows through `("rows", ...)`; assert KEPT, reason HISTORY_ROWS).

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR121-g-AC1" cell_refs="AR-g-121"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g121_checks.py build</invocation><expect>^AR-G121-OK</expect></criterion>

<criterion id="AR121-g-AC2" cell_refs="AR-g-121"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g121_checks.py guard</invocation><expect>^AR-G121-OK</expect></criterion>

<criterion id="AR121-g-AC3" cell_refs="AR-g-121"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g121_checks.py regress</invocation><expect>^AR-G121-REGRESS-OK</expect></criterion>

<expected_criteria>AR121-g-AC1,AR121-g-AC2,AR121-g-AC3</expected_criteria>

- AC1 loads your `yfinance_check.py` and the real exception classes, and needs a ticker-missing exception to read NOT_KEPT with reason NO_ROWS and `hide_exceptions` restored, and needs your fixture byte-equal to the real file and your test file to name it. At base it FAILs.
- AC2 needs every other exception to stay CHECK_FAILED (rate limit PUSHBACK and the step stops; a data error, a plain error, a connection error and a lookalike class name EXCEPTION) and SPY rows to read KEPT. At base it PASSes; a fix that catches every exception, or matches by substring, FAILs it.
- AC3 runs three test files one at a time (your test file, `test_kept_holding.py`, `test_resident_session_checker.py`) and needs the branch to change only your three product files, your folder, your order and the channel file. At base it PASSes. Run it under `timeout` 590000 ms.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/intake/yfinance_check.py
infra/aws/lambda/investor-reporting/intake/tests/test_yfinance_check.py
infra/aws/lambda/investor-reporting/intake/tests/fixtures/yfinance_exceptions_1_2_0.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~258/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-121.checker-ticker-missing-is-not-kept.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R36_G.md</decomp_doc> round 36, workstream ~G, cell `AR-g-121`.
<owned_cells>AR-g-121</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR121-g-AC1, AR121-g-AC2, AR121-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~258/IRPT_ANLREQ.TO-AR-g-121.checker-ticker-missing-is-not-kept.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-121`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put the `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder (use `kind` `test` for a test file or the fixture): commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR121-g-AC1,AR121-g-AC2,AR121-g-AC3` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the lines you changed in `yfinance_check.py` with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `intake/yfinance_check.py` is a member of the resident package (the r34c root carries the PRE-fix bytes; the next resident release, r34d, carries this) and is staged into no Lambda function's source-map row. Behaviour change at the door: a symbol Yahoo has no data for now reads NOT_KEPT (the filer's Replace and No branches) instead of TICKER_CHECK_FAILED; a rate limit, a connection error, a timeout or any other exception still reads CHECK_FAILED. No vendor call is made by this cell; the next release's V2 makes two.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- by the issuer's reference fix in a scratch tree (build and guard arms pass; at base build FAILs reproducing the served CHECK_FAILED/EXCEPTION, guard PASSes) and two mutants (catch every exception; substring match), both FAIL the guard. Traps: a fix that catches all exceptions so an outage reads "not a ticker"; a name match by substring; the hide_exceptions flag left False after the return; a test that invents its own exception class instead of the real one; the old hidden-error-frame test altered. NOT seen (blind): whether Yahoo raises this class for every symbol it lacks, and whether a transient Yahoo "no price data" for a real symbol raises it too (the lens read the yfinance 1.2.0 wheel's history.py, not Yahoo's behaviour); denominator: 1 module (intake/yfinance_check.py), 7 exception classes in the real exceptions module, 4 other exception shapes tried.
</preflight>

- Cut on CTO msgs 9283 and 9291 and AQ2's CHECKFAIL record (commit 51686af530). Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR121-g-AC1` FAILs, `AR121-g-AC2` and `AR121-g-AC3` PASS, as expected.
- NOT claimed: that Yahoo raises this class for every symbol it lacks (the in-service V2 reads ZQXWVK); that a transient "no price data" for a real symbol cannot read NOT_KEPT (named in the decomposition; the CTO accepts the class as the line); that the resident carries the fix (the next release does).

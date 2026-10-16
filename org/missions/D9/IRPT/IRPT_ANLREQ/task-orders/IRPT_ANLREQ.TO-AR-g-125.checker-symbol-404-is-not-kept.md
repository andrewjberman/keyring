# TO-AR-g-125 -- the default yfinance port reads Yahoo's 404 on THIS symbol's quoteSummary URL as a clean empty answer, so an unknown symbol is NOT_KEPT and never CHECK_FAILED (C-SWAP step 2, r34e)

<to_id>IRPT_ANLREQ.TO-AR-g-125</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~260</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>39</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-125` (`decompositions/IRPT_ANLREQ_DECOMP_R39_G.md`) |
**outcome_ref:** FWD-1 run 3 (C-SWAP step 2, the served checker) | **depends_on:** `AR-g-121` (merged `b535f41cb8`, the YF* classes). Order: CTO msgs 9345 and 9354; the probe `EXCCLASS_READ.txt` (AQ2 commit 6395c4000d).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~260`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-260` (branch `wk-IRPT_ANLREQ-260`), provisioned by the issuer with `infra/aws/lambda/investor-reporting`, `lib`, `.tools`, `org/standards` and the project folder on disk. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~260 <0.9.0_WK_IRPT_ANLREQ~260@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either. (A provisioner error about a portal sub-worktree does not concern you.)
- A row id has the form `IRPT_ANLREQ-D2-W260-S<k>` (take the next free `<k>`; check the channel file for `W260` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax: no `X | None`, no `match`). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network (neither yfinance nor curl_cffi is installed or called by your tests), no install. Scratch outside the product tree.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`).

### Read first (under `C:/dev/wk-irpt-anlreq-260/infra/aws/lambda/investor-reporting/intake/`)

- `yfinance_check.py` (`_is_ticker_missing`, `default_history`, `_failure_reason`, `_http_status_of`) and `tests/test_yfinance_check.py` (the helper `fake_yfinance(behaviour, observed)`: its `("raise", exc)` case raises exc only while `config.debug.hide_exceptions` is False, which `default_history` sets for the call; and the r34d tests that load `tests/fixtures/yfinance_exceptions_1_2_0.py`).
- The issuer's real-class fixture, read-only, in your worktree at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/curl_cffi_0_13_0/` (its `README.md` says what is byte-exact: curl_cffi 0.13.0's `requests/exceptions.py` and `const.py`, and the exact text of `class CurlError`). Its members carry the suffix `.pyfix` (the lint gate would rewrite third-party `.py` files): copy the folder to a temp directory renaming every `.pyfix` to `.py`, put that directory on `sys.path`, and `import curl_cffi.requests.exceptions` to get the REAL `HTTPError`, `Timeout`, `ConnectionError`, `DNSError`. Note the real `HTTPError` raised by `Response.raise_for_status` is `HTTPError("HTTP Error 404: ", 0, response)`: its `code` is 0, and the status and URL are on `exc.response` (`status_code`, `url`).

### THE CELL (`AR-g-125`, inlined)

The served door still answered TICKER_CHECK_FAILED for an unknown symbol after the r34d fix. The probe read the exception in the service: for ZQXWVK, `curl_cffi.requests.exceptions.HTTPError` "HTTP Error 404: " raised from yfinance's info fetch (`GET https://query2.finance.yahoo.com/v10/finance/quoteSummary/ZQXWVK?...`), not a `YFTickerMissingError`. This cell makes that case read NOT_KEPT and nothing wider.

**`intake/yfinance_check.py`, exactly this, and nothing else in the file:**
1. Add `from urllib.parse import unquote, urlsplit` with the other imports.
2. A new module-level function `_symbol_404(exc, symbol)`, placed immediately before `_is_ticker_missing`, returning True only when ALL hold: (a) some class in `type(exc).__mro__` has `__name__ == "HTTPError"` and a `__module__` starting with `curl_cffi`; (b) `getattr(getattr(exc, "response", None), "status_code", None) == 404`; (c) the response's `url` is a `str`; (d) its host (`urlsplit(url).hostname`, lower-cased) is `finance.yahoo.com` or ends with `.finance.yahoo.com`; (e) its path, split on `/` with empty parts dropped and each part `unquote`d and upper-cased, ends with the two parts `QUOTESUMMARY` and the symbol upper-cased (so only `.../quoteSummary/<SYMBOL>` counts: another endpoint, another symbol, or a symbol merely present elsewhere in the URL does not). A docstring states this.
3. `_is_ticker_missing(exc)` becomes `_is_ticker_missing(exc, symbol=None)`: it returns True for the exact class name `YFTickerMissingError` anywhere in the MRO (unchanged), else `symbol is not None and _symbol_404(exc, symbol)`. Update its docstring.
4. In `default_history`, change the call to `_is_ticker_missing(exc, symbol)`; the comment at `return []` gains one sentence naming the second case (Yahoo's 404 on this symbol's quoteSummary URL). The `finally` that restores `hide_exceptions` and every other line stay as they are.
5. No other change: not `_failure_reason`, not `_http_status_of`, not the cap or pace, not `check()`.

**Fixtures.** `cp -r` the issuer's folder `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/curl_cffi_0_13_0` to `intake/tests/fixtures/curl_cffi_0_13_0` (the folder name is the destination; then `diff -r` the two folders: no difference; do not retype any file). The existing `intake/tests/fixtures/yfinance_exceptions_1_2_0.py` stays.

**Tests**, appended to `intake/tests/test_yfinance_check.py` (it keeps all its existing tests untouched), with these exact function names:
- a loader `_real_curl(tmp_path, monkeypatch)` that copies `tests/fixtures/curl_cffi_0_13_0` into `tmp_path` renaming every `.pyfix` file to `.py`, prepends `tmp_path` to `sys.path` with `monkeypatch.syspath_prepend`, imports `curl_cffi.requests.exceptions`, and registers a cleanup that deletes every `curl_cffi*` key from `sys.modules` afterwards; and a small `_raise_for_status(curl, status, url)` helper that builds a response-like object with `status_code`, `reason`, `url` and an `ok` property and raises `curl.HTTPError("HTTP Error %s: %s" % (status, reason), 0, response)` exactly as curl_cffi's `Response.raise_for_status` does;
- `test_default_port_symbol_404_on_quote_summary_reads_not_kept_no_rows` (parametrised over the URL `https://query2.finance.yahoo.com/v10/finance/quoteSummary/ZQXWVK?modules=financialData&crumb=abc` for `ZQXWVK`, and `https://query1.finance.yahoo.com/v10/finance/quoteSummary/%5EZQXW` for `^ZQXW`; raised through `fake_yfinance` with `("raise", exc)`; assert `state` NOT_KEPT, `reason` NO_ROWS, `rows` 0, and `hide_exceptions` True again afterwards);
- `test_default_port_404_on_another_symbol_or_endpoint_or_host_stays_check_failed` (parametrised: quoteSummary of `OTHER`; the chart URL `https://query2.finance.yahoo.com/v8/finance/chart/ZQXWVK`; host `evil.example.com`; no URL (`response.url = None`); no response object (`HTTPError("HTTP Error 404: ", 0, None)`); each asserts CHECK_FAILED, reason EXCEPTION);
- `test_default_port_401_403_429_and_5xx_on_the_symbol_url_stay_check_failed` (401, 403, 429 each assert reason PUSHBACK and that a second symbol in the same call is NOT_CHECKED, reason STEP_STOPPED; 500 and 503 assert reason EXCEPTION);
- `test_default_port_curl_cffi_timeout_connection_and_dns_errors_stay_check_failed` (`curl.Timeout("timed out")` reason TIMEOUT; `curl.ConnectionError("reset")` and `curl.DNSError("no such host")` reason EXCEPTION);
- `test_default_port_lookalike_http_error_from_another_module_stays_check_failed` (a class created with `type("HTTPError", (Exception,), {})`, its `__module__` set to `"other.lib"`, carrying a `response` with status 404 and the right quoteSummary URL; assert CHECK_FAILED, reason EXCEPTION).

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR125-g-AC1" cell_refs="AR-g-125"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g125_checks.py build</invocation><expect>^AR-G125-OK</expect></criterion>

<criterion id="AR125-g-AC2" cell_refs="AR-g-125"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g125_checks.py guard</invocation><expect>^AR-G125-OK</expect></criterion>

<criterion id="AR125-g-AC3" cell_refs="AR-g-125"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g125_checks.py regress</invocation><expect>^AR-G125-REGRESS-OK</expect></criterion>

<expected_criteria>AR125-g-AC1,AR125-g-AC2,AR125-g-AC3</expected_criteria>

- AC1 loads your `yfinance_check.py` and the REAL yfinance and curl_cffi exception classes and needs: the two yfinance classes still read NOT_KEPT NO_ROWS; a curl_cffi HTTPError 404 on `quoteSummary/<this symbol>` (the symbol URL-encoded and lower-case path included) reads NOT_KEPT NO_ROWS with `hide_exceptions` restored; and your fixtures byte-equal the issuer's and your test file loads them. At base it FAILs (it reproduces the served CHECK_FAILED).
- AC2 needs everything else to stay CHECK_FAILED (401, 403, 429 and the rate-limit class PUSHBACK with the step stopping; a 404 on another symbol, the chart endpoint, another host, no URL, no response, a lookalike HTTPError; 500 and 503; Timeout, ConnectionError, DNSError; a data error; a plain error) and SPY rows to read KEPT. At base it PASSes; a fix that accepts every 404, matches the symbol as a substring, ignores the host or the endpoint, or accepts other statuses FAILs it.
- AC3 runs three test files one at a time (your test file, `test_kept_holding.py`, `test_resident_session_checker.py`) and needs the branch to change only your product files, your fixtures, your folder, your order and the channel file. At base it PASSes. Run it under `timeout` 590000 ms.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/intake/yfinance_check.py
infra/aws/lambda/investor-reporting/intake/tests/test_yfinance_check.py
infra/aws/lambda/investor-reporting/intake/tests/fixtures/curl_cffi_0_13_0/
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~260/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-125.checker-symbol-404-is-not-kept.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R39_G.md</decomp_doc> round 39, workstream ~G, cell `AR-g-125`.
<owned_cells>AR-g-125</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR125-g-AC1, AR125-g-AC2, AR125-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~260/IRPT_ANLREQ.TO-AR-g-125.checker-symbol-404-is-not-kept.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-125`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put the `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder (use `kind` `test` for a test file or a fixture): commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR125-g-AC1,AR125-g-AC2,AR125-g-AC3` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the lines you changed in `yfinance_check.py` with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `intake/yfinance_check.py` is a member of the resident package (the r34c root, now running, carries the pre-fix bytes; the next resident release, r34e, carries this) and is staged into no Lambda function's source-map row. Behaviour change at the door: a symbol Yahoo answers 404 on its quoteSummary URL now reads NOT_KEPT (the filer's Replace and No branches) instead of TICKER_CHECK_FAILED; a rate limit, any other status, a timeout, a network error and any other exception still read CHECK_FAILED. No vendor call is made by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- by the issuer's reference fix in a scratch worktree (build and guard arms pass; at base build FAILs reproducing the served CHECK_FAILED, guard PASSes; the existing test files pass) and FIVE mutants (any 404; the symbol as a URL substring; no host check; no endpoint check; any status), each FAILing build or guard. Traps: a fix that accepts every 404 so a Yahoo-wide 404 reads "not a ticker"; the symbol matched anywhere in the URL (a one-letter symbol matches every URL); the host or endpoint ignored; code read from `exc.code` (it is 0 in curl_cffi 0.13.0; the status is on `exc.response`); a test class invented instead of the real one; `curl_cffi` left in `sys.modules` after the tests. NOT seen (blind): Yahoo's behaviour for any symbol other than the one probed (ZQXWVK) and whether its 404 is stable; the real `Response.url` string beyond what the code shows; denominator: 1 module, 17 exception shapes in the guard, 5 positive shapes in the build.
</preflight>

- Cut on CTO msgs 9345 and 9354 and AQ2's probe record. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR125-g-AC1` FAILs, `AR125-g-AC2` and `AR125-g-AC3` PASS, as expected.
- NOT claimed: that Yahoo 404s on quoteSummary for every unknown symbol, or that a transient 404 for a real symbol cannot read NOT_KEPT (the CTO accepts the Yahoo-wide-404 risk as named); that the resident carries the fix (the next release does).

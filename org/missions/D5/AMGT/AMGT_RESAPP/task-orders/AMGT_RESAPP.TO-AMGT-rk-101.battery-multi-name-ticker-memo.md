# AMGT_RESAPP task order -- `AMGT-rk-101` -- the filings BATTERY CLI takes a REPEATABLE `--security-key`: one process runs N names with ONE shared SEC ticker-table fetch (and one sink hand-off) passed down `run_battery`, and a single-name run stays BYTE-IDENTICAL to today; CODE ONLY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-101</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~101</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits one library module and adds one test file; it arms no
  cron, alarm, monitor or cadence, reads no schedule and writes none.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is read or changed; no AWS call of any kind is made by
  this order (every test and script stubs `fetch.http_get`, the keys lookup and the bronze sink).
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~101`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt.
Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
`.tools/` and the paths in section 3 exist (the new test file excepted); if any is absent, STOP with a BLOCKING row.
Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~101;`. **NEVER RUN AN INSTALL.** Never read, show,
diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential.

## 1. THE CELL, inlined in full -- `AMGT-rk-101` (round 26, ahead of the B2 run)

**The rulings of record, verbatim.**

1.0.0_SA_CTO~Z msg 24204, 2026-09-22T11:38:55Z, file
`org/mcp/inbox/2.0.0_SA_COO/~Z/read/20260922T113855Z_1.0.0_SA_CTO_Z__ROUND-25_ANALYSIS__AMGT_RESAPP__04f5188.md`,
lines 13-15:

> - (b) A per-run ticker-table memo: one fetch and one sink hand-off per run. For a 3-name run, the stub fetch count
> reads 1.
> My read of bronze_put (store.py:216-250): a repeat put with equal sha256 is a no-op, and different bytes raise. So
> the hazard in the CVO's slug is real only when SEC changes the table between two names in one run. The memo closes it.

1.0.0_SA_CTO~Z msg 24207, 2026-09-22T11:39:58Z, file
`org/mcp/inbox/2.0.0_SA_COO/~Z/read/20260922T113958Z_1.0.0_SA_CTO_Z_Re_24206__cell__b__RULED__i__--_repeatab.md`,
lines 9-12:

> RULING, cell (b): (i), as you recommended.
> - The battery CLI's --security-key becomes repeatable. One process runs N names, with ONE ticker fetch passed down
> through run_battery.
> - Criterion: a 3-name stub run reads fetch count 1.
> - A single --security-key must behave byte-identically to today.

**Why this cell exists:** no production process runs the battery over more than one name today. So a per-run memo
had nothing to span, and a 3-name B2 run would be 3 processes with 3 ticker fetches (COO msg 24206). This cell makes
the multi-name run real, and the memo meaningful.

**THE MEASURED STATE, at `04f518851d` (SITEZ; `lib/` byte-identical to `8dd72465b6`). RE-READ every line at your branch
HEAD before editing:**

- `lib/research/filings/battery.py` (1363 lines):
  - `_sec_ticker_table(http_get, timeout=60, bronze_sink=None)` (`:566`) makes ONE `_call_http_get` of `_TICKERS_URL`
    (`:563`). It raises `RuntimeError` on a failed fetch, hands the bytes to `bronze_sink.ticker_table(data)` BEFORE
    parsing, and returns `json.loads(...)`.
  - Its ONLY caller is `_step1_edgar_ticker(security_key, keys, run_date, http_get, timeout=60, bronze_sink=None)`
    (`:657`), at `:665`, inside `try: ... except (RuntimeError, ValueError)` (the rk-98 narrowing: a sink exception
    propagates).
  - `run_battery(security_key, keys, run_date=None, http_get=None, search_fn=None, cache_dir=None,
    document_layer=None, no_site_crawl=False, bronze_sink=None)` (`:1213`) builds step 1 as the lambda at `:1239`.
    Its ONE production caller is `main` (`:1314`); every other caller is a test (`test_battery.py:86/173/229/518`,
    `test_bronze_wiring.py:159/180/200/281`).
  - `main` (`:1278`): `--security-key` is `required=True` and single. Keys come from `--keys-json` (`:1296`), else
    `--bloomberg` via `keys_from_bloomberg` (`:1300`), else `keys_from_crosswalk(args.security_key)` (`:1305`), then
    `--exchange` / `--legal-name-override` adjust them. One `fetch.BronzeSink()` is built if `--write-bronze`
    (`:1313`). It prints `UNRESOLVED-SOURCE: ...` or `RESOLVED: ...`, one `STEP ...` line per attempt, a
    `verified_site ...` line, the optional `written <path>` line, and `OK: uploaded ...` or `NOT-UPLOADED (no
    --write-pool)`, then returns 0.
  - `test_bronze_wiring.py:348` calls `battery.main(["--security-key", "X", "--keys-json", ...])`, so a single-name
    call with `--keys-json` must keep working.
- **Tests at the cut** (one pytest call per directory): `lib/research/filings/tests` **86 passed**; `test_battery.py`
  **22 passed**.
- **Encoding at the cut:** `battery.py` has 0 CRLF and 0 non-ASCII characters.
- **The single-name comparator below was CONTROLLED at the cut:** run pinned-vs-pinned it prints
  `single_identical True`, 1119 stdout bytes on each side, and 1 ticker fetch on each side.

**ISSUER RULINGS (L5), what you build:**

1. **The memo.** In `battery.py`, add a small public class `TickerTableMemo` with an attribute `fetches` (int, starts
   0) and one method `table(http_get, timeout=60, bronze_sink=None)`:
   - the FIRST call runs `_sec_ticker_table(http_get, timeout=timeout, bronze_sink=bronze_sink)` exactly once and
     increments `fetches`;
   - on success it caches the parsed table and returns it on every later call, with NO second fetch and NO second
     sink hand-off;
   - on a `RuntimeError` or `ValueError` it caches THAT EXCEPTION and re-raises it on this and every later call, with
     NO re-fetch (one SEC request per process, whatever happens);
   - any other exception (a sink/writer error) is NOT cached and propagates.
2. **Threading, default OFF, so every existing caller is unchanged:**
   - `run_battery(..., bronze_sink=None, ticker_memo=None)` passes `ticker_memo` into step 1 only.
   - `_step1_edgar_ticker(..., bronze_sink=None, ticker_memo=None)`: inside the SAME `try` and the SAME
     `except (RuntimeError, ValueError)`, use `ticker_memo.table(http_get, timeout=timeout, bronze_sink=bronze_sink)`
     when it is not None; otherwise use today's `_sec_ticker_table(...)` call unchanged.
3. **`main`:**
   - `--security-key` becomes `action="append"` and `required=True`.
   - **N == 1:** the path is today's, printed BYTE-IDENTICALLY: no new header, no new footer, the same lines in the
     same order, and the same return value. `--keys-json`, `--bloomberg`, `--exchange` and `--legal-name-override`
     all keep working.
   - **N > 1:**
     - `--keys-json`, `--bloomberg` and `--legal-name-override` are REFUSED with `parser.error(...)`, because each
       names one security. `--exchange` is also refused.
     - This happens BEFORE any fetch. Every name's keys are resolved UP FRONT with `keys_from_crosswalk(key)` (the
       Bloomberg lookup is never memoized; it is simply not used for N > 1).
     - One `TickerTableMemo` and at most one `fetch.BronzeSink()` (if `--write-bronze`) are built for the whole
       process.
     - The names run IN THE ORDER GIVEN. Before each name's unchanged block, print
       `"BATTERY NAME %d of %d: %s" % (i, n, security_key)`.
     - A name that ends UNRESOLVED-SOURCE does not stop the others; `--out-dir` and `--write-pool` apply per name,
       exactly as today.
     - Any exception, e.g. a sink write error per the rk-98 ruling, PROPAGATES and stops the run.
     - After the last name, print
       `"BATTERY DONE: %d name(s), %d RESOLVED, %d UNRESOLVED-SOURCE, ticker_table_fetches %d"`, where the last value
       is `memo.fetches`, then return 0.
   - For N == 1, `main` may use a memo internally, but the stdout and the ticker fetch count (1) must be exactly
     today's.
4. **Tests**, in ONE new file `lib/research/filings/tests/test_battery_multi.py`. Use pytest style with QUALIFIED
   imports `lib.research.filings.battery` / `lib.research.filings.fetch` (W85-S1). Stub `fetch.http_get` with a URL
   counter, `battery.keys_from_crosswalk` with fixed keys records, and `fetch.BronzeSink` with a counting class. No
   network, no boto3, no Bloomberg. Names must match AC1:
   - `test_single_key_main_prints_no_multi_header` -- a one-key `main` run prints no `BATTERY NAME` and no
     `BATTERY DONE` line, and fetches the ticker table exactly once.
   - `test_three_names_fetch_the_ticker_table_once` -- a 3-name `main` run: the ticker URL is requested exactly 1 time.
   - `test_three_names_hand_the_ticker_table_to_the_sink_once` -- the same run with `--write-bronze`: the counting sink
     records exactly 1 `ticker_table` call.
   - `test_names_run_in_order_and_unresolved_does_not_stop_the_others` -- 3 names, all UNRESOLVED: 3 `BATTERY NAME`
     headers `1 of 3`..`3 of 3` in the given order, 3 `UNRESOLVED-SOURCE:` lines in the same order, and a
     `BATTERY DONE: 3 name(s), 0 RESOLVED, 3 UNRESOLVED-SOURCE, ticker_table_fetches 1` line.
   - `test_ticker_fetch_failure_is_memoized_not_refetched` -- the ticker URL raises: across 3 names it is requested
     exactly 1 time, and each name's step-1 attempt carries the "could not read the live SEC ticker table" reason.
   - `test_sink_error_propagates_in_a_multi_name_run` -- a sink whose `ticker_table` raises makes the 3-name `main`
     raise; no `BATTERY DONE` line is printed.
   - `test_run_battery_without_memo_is_todays_path` -- two consecutive `run_battery` calls with NO `ticker_memo`
     request the ticker URL 2 times (today's per-call behaviour is preserved for every existing caller).
   - `test_multi_name_refuses_single_name_options` -- `--keys-json`, `--bloomberg`, `--legal-name-override` and
     `--exchange`, each with 2 keys, exit via `parser.error` (`SystemExit`) with 0 http calls.

**What this cell does NOT change:** `fetch.py`, `batch.py` (a sibling cell of this round edits it), `document.py`,
`lib/research/harvest/**`, steps 2-5 of the battery, the step cache, every existing test file, and any S3 object. No
network call, no Bloomberg call, no model call, no AWS call.

## 2. WHERE THIS CAME FROM

**ROUND 26**, decomposition s.34 (cut by `2.0.0_SA_COO~Z`), on the CTO's round-25 analysis (msg 24204,
`ledger/ROUND_ANALYSIS.round25.md` @`04f518851d`) as amended by msg 24207. That message ruled option (i) on the COO's
correction msg 24206: my round-25 packet's s.3 claim that "a 3-name run hands the ticker table to the writer 3 times"
was withdrawn, because no production path ran more than one name. The B2 RUN cell (held, on Andrew's word) becomes ONE
battery invocation over the validation names. Andrew-direct ~15:12Z governs one-slug issuance.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/filings/battery.py
lib/research/filings/tests/test_battery_multi.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~101/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-101.battery-multi-name-ticker-memo.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Reads need no grant. In particular, `batch.py` (a sibling cell's) and
  every existing test file are walls. If an existing test must change to stay green, STOP and REFUSE with a row.
  Scratch is `<your worktree>/.scratch/r101/` only, never committed. The only shared file is `INVESTIGATION_v1.md`
  (append-only; do not isolate it).
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~101 <0.9.0_WK_AMGT_RESAPP~101@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

**CODE ONLY.** No network call, no EDGAR or issuer-site fetch, no Bloomberg call, no model call, no AWS call of any
kind, and no deploy. Never run `battery.main` against the live network: every run below stubs `fetch.http_get`.
- **Imports in tests use the QUALIFIED `lib.<pkg>.<mod>` names** (W85-S1).
- **Run each test directory in its OWN pytest call.**
- **A script that carries a backslash is a FILE** you write from this order's text verbatim (W84-S1). Every script
  below is a file.
- **The discriminating comparison is pinned to commit `04f518851d`** (Z-S193), never HEAD or a merge-base. AC3 loads
  the PINNED `battery.py` from `git show 04f518851d:...` and compares its stdout with the new module's on the same argv.
- **THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
  repaired, widened, or satisfied by a route this order did not name, and never by editing a WALL.
- **A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator.** AC0 re-measures every baseline before you edit; every
  later bar is "AC0's value plus N" or "equal to AC0's value", never a number typed here.
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-W101-S<k>`, with `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`.
  Append by textual splice inside the one fenced JSON array; never edit an existing row. A worker names the issuer
  (`2.0.0_SA_COO~Z`) as `disarm_owner`.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 600)

**Script files.** Write each block below to the named file under `<your worktree>/.scratch/r101/`, byte-for-byte,
then run it from the worktree root as the criterion states.

`.scratch/r101/ac0.py`:
```
import subprocess
print("pin_object", subprocess.run(["git", "cat-file", "-t", "04f518851d"], capture_output=True, text=True).stdout.strip())
src = open("lib/research/filings/battery.py", "rb").read().decode("utf-8").splitlines()
for n in (566, 657, 665, 1213, 1280):
    print("battery_%d" % n, src[n - 1].strip())
callers = subprocess.run(["git", "grep", "-n", "_sec_ticker_table(", "--", "lib", "integrations", "data", ".tools"], capture_output=True, text=True).stdout.splitlines()
print("ticker_table_call_sites", len(callers), sorted(c.split(":", 2)[0] + ":" + c.split(":", 2)[1] for c in callers))
b = open("lib/research/filings/battery.py", "rb").read()
print("battery.py crlf", b.count(bytes([13, 10])), "non_ascii_chars", sum(1 for c in b.decode("utf-8") if ord(c) > 127))
```

`.scratch/r101/ac3.py` (the SINGLE-NAME byte-identity comparator; pinned module vs new module, same argv, same stub):
```
import contextlib, importlib.util, io, json, os, subprocess, sys, tempfile
sys.path.insert(0, ".")
import lib.research.filings.fetch as fetch
import lib.research.filings.battery as new
src = subprocess.run(["git", "show", "04f518851d:lib/research/filings/battery.py"], capture_output=True).stdout
d = tempfile.mkdtemp()
p = os.path.join(d, "battery_pin.py")
open(p, "wb").write(src)
spec = importlib.util.spec_from_file_location("battery_pin", p)
pin = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pin)
TICKERS = json.dumps({"0": {"cik_str": 999999201, "ticker": "OTHR", "title": "OTHER CO"}}).encode()
calls = []
def http_get(url, timeout=60):
    calls.append(url)
    if url.endswith("company_tickers.json"):
        return TICKERS
    raise RuntimeError("HTTP Error 404: NOT FOUND")
fetch.http_get = http_get
keys = {"legal_name": "Zeta Test Corp", "legal_name_reason": None, "ticker_root": "ZETA", "exchange": "US", "cik": None, "cik_reason": "absent", "lei": None, "lei_reason": "absent", "web_address": None, "web_address_reason": "absent", "domicile": None, "domicile_reason": "absent", "source": "keys-json"}
kp = os.path.join(d, "keys.json")
open(kp, "w").write(json.dumps(keys))
argv = ["--security-key", "ZETA_US_Equity", "--keys-json", kp, "--no-site-crawl", "--run-date", "2026-09-22"]
def run(mod):
    buf = io.StringIO()
    del calls[:]
    with contextlib.redirect_stdout(buf):
        rc = mod.main(list(argv))
    return rc, buf.getvalue(), list(calls)
rc0, out0, c0 = run(pin)
rc1, out1, c1 = run(new)
print("pin_rc", rc0, "new_rc", rc1)
print("pin_stdout_bytes", len(out0.encode("utf-8")), "new_stdout_bytes", len(out1.encode("utf-8")))
print("single_identical", out0 == out1 and rc0 == rc1)
print("pin_fetches", len(c0), "new_fetches", len(c1), "same_urls", c0 == c1)
print("pin_first_line", out0.splitlines()[0] if out0 else None)
```

`.scratch/r101/ac4.py` (the 3-name run, a DIFFERENT instrument from the unit tests: `main` end to end on the stub):
```
import contextlib, io, json, sys
sys.path.insert(0, ".")
import lib.research.filings.fetch as fetch
import lib.research.filings.battery as battery
TICKERS = json.dumps({"0": {"cik_str": 999999201, "ticker": "OTHR", "title": "OTHER CO"}}).encode()
calls = []
def http_get(url, timeout=60):
    calls.append(url)
    if url.endswith("company_tickers.json"):
        return TICKERS
    raise RuntimeError("HTTP Error 404: NOT FOUND")
fetch.http_get = http_get
sink_calls = []
class CountingSink:
    def __init__(self, *args, **kwargs):
        pass
    def ticker_table(self, body):
        sink_calls.append("ticker_table")
    def sec_filing(self, *args):
        sink_calls.append("sec_filing")
    def issuer_document(self, *args):
        sink_calls.append("issuer_document")
fetch.BronzeSink = CountingSink
BASE = {"legal_name": "Zeta Test Corp", "legal_name_reason": None, "ticker_root": None, "exchange": "US", "cik": None, "cik_reason": "absent", "lei": None, "lei_reason": "absent", "web_address": None, "web_address_reason": "absent", "domicile": None, "domicile_reason": "absent", "source": "crosswalk"}
battery.keys_from_crosswalk = lambda security_key, path=None: dict(BASE, ticker_root=security_key.split("_")[0])
argv = ["--security-key", "AAA_US_Equity", "--security-key", "BBB_US_Equity", "--security-key", "CCC_US_Equity", "--no-site-crawl", "--run-date", "2026-09-22", "--write-bronze"]
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    rc = battery.main(argv)
out = buf.getvalue().splitlines()
print("multi_rc", rc)
print("ticker_fetches", sum(1 for u in calls if u.endswith("company_tickers.json")), "of_http_calls", len(calls))
print("sink_ticker_calls", sink_calls.count("ticker_table"), "of_sink_calls", len(sink_calls))
print("unresolved_names_in_order", [l.split(":", 1)[1].split(" -- ")[0].strip() for l in out if l.startswith("UNRESOLVED-SOURCE:")])
print("name_headers", [l for l in out if l.startswith("BATTERY NAME ")])
print("done_line", [l for l in out if l.startswith("BATTERY DONE:")])
```

`.scratch/r101/ac5.py`:
```
import subprocess
out = subprocess.run(["git", "diff", "--name-only", "04f518851d", "HEAD", "--", "lib", "integrations", "infra", ".tools", "data"], capture_output=True, text=True).stdout.split()
print("changed_code_files", sorted(out))
for f in ("lib/research/filings/battery.py", "lib/research/filings/tests/test_battery_multi.py"):
    b = open(f, "rb").read()
    compile(b.decode("utf-8"), f, "exec")
    print(f, "compiles True crlf", b.count(bytes([13, 10])), "non_ascii_chars", sum(1 for c in b.decode("utf-8") if ord(c) > 127))
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-101"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r101/ac0.py && python -m pytest lib/research/filings/tests -q -p no:cacheprovider 2>&1 | tail -1 && python -m pytest lib/research/filings/tests/test_battery.py -q -p no:cacheprovider 2>&1 | tail -1 && python .scratch/r101/ac3.py</invocation><expect>BEFORE any edit. It prints "pin_object commit". The five battery lines: battery_566 carries "def _sec_ticker_table(", battery_657 carries "def _step1_edgar_ticker(", battery_665 carries "_sec_ticker_table(http_get", battery_1213 carries "def run_battery(", and battery_1280 carries "--security-key". Then "ticker_table_call_sites T0" (measured 2 at the cut: the def at :566 and the call at :665), battery.py's crlf and non_ascii_chars (measured 0 and 0), the filings suite's "F0 passed" (measured 86) and test_battery.py's "B0 passed" (measured 22). Then the comparator's CONTROL, run while new IS the pin: "single_identical True" with equal stdout byte counts (measured 1119) and "pin_fetches 1 new_fetches 1 same_urls True". A control that does not read True means the instrument is broken: STOP with a BLOCKING row. A drifted line NUMBER is recorded, not a fail, if the SITE is the same</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-101"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/filings/tests/test_battery_multi.py -v -p no:cacheprovider 2>&1 | tail -12</invocation><expect>a final line "8 passed" and 0 failed, with the PASSED lines naming test_single_key_main_prints_no_multi_header, test_three_names_fetch_the_ticker_table_once, test_three_names_hand_the_ticker_table_to_the_sink_once, test_names_run_in_order_and_unresolved_does_not_stop_the_others, test_ticker_fetch_failure_is_memoized_not_refetched, test_sink_error_propagates_in_a_multi_name_run, test_run_battery_without_memo_is_todays_path and test_multi_name_refuses_single_name_options</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-101"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/filings/tests -q -p no:cacheprovider 2>&1 | tail -1 && python -m pytest lib/research/filings/tests/test_battery.py -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>first "(F0 + 8) passed" and 0 failed, where F0 is AC0's printed filings count (measured 86, so 94); then "B0 passed" and 0 failed for test_battery.py, where B0 is AC0's value (measured 22). Every pre-existing test stays green unedited, including test_bronze_wiring.py's single-name battery.main call</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-101"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r101/ac3.py</invocation><expect>AFTER the edit, pinned module vs new module on the same single-name argv and stub: "pin_rc 0 new_rc 0", equal pin_stdout_bytes and new_stdout_bytes, "single_identical True", and "pin_fetches 1 new_fetches 1 same_urls True" -- a single --security-key run is byte-identical to today, as ruled</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-101"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r101/ac4.py</invocation><expect>the ruled criterion on a DIFFERENT instrument from AC1, main end to end on the stub: "multi_rc 0"; "ticker_fetches 1 of_http_calls 1"; "sink_ticker_calls 1 of_sink_calls 1"; "unresolved_names_in_order ['AAA_US_Equity', 'BBB_US_Equity', 'CCC_US_Equity']"; name_headers of exactly "BATTERY NAME 1 of 3: AAA_US_Equity", "BATTERY NAME 2 of 3: BBB_US_Equity" and "BATTERY NAME 3 of 3: CCC_US_Equity"; and done_line exactly ['BATTERY DONE: 3 name(s), 0 RESOLVED, 3 UNRESOLVED-SOURCE, ticker_table_fetches 1']</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-101"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r101/ac5.py</invocation><expect>"changed_code_files" lists EXACTLY lib/research/filings/battery.py and lib/research/filings/tests/test_battery_multi.py, with no other code file (in particular no batch.py or fetch.py); both files print "compiles True" and crlf 0; battery.py's non_ascii_chars EQUALS AC0's measured value (measured 0), and the new test file's is 0</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~101/AMGT_RESAPP.TO-AMGT-rk-101.battery-multi-name-ticker-memo.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5` (rc 0 is the verdict). Flip the order's status
(on the record face) to `complete` only if every criterion PASSES, and commit with `--only -- <paths>`. Report once,
naming AC0's baselines and control, AC3's identity line, AC4's six lines, and the suite counts before and after.

**MUTATION DISCIPLINE:** snapshot the WORKING-TREE BYTES of `battery.py` to `.scratch/r101/` before editing. Never
`git checkout --`, never `git stash`, never `git show :path` (a `git show <commit>:<path>` of the PINNED commit, as
AC3 does, is the named instrument and is allowed).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES -- the L5 choices, flagged to the CTO at issuance:**
1. **A FAILED ticker fetch is memoized too.** One SEC request per process, whatever happens. The alternative, retrying
   per name, would re-open the N-fetch shape the ruling closed and make the fetch count depend on failures. Each
   name's step-1 attempt still records the failure reason. A sink/writer exception is NOT cached: it propagates and
   stops the run (rk-98 ruling item 2).
2. **For N > 1, the single-security options are REFUSED** (`--keys-json`, `--bloomberg`, `--legal-name-override`,
   `--exchange`), and keys come from the crosswalk per name. Each of those options names one security, so there is
   no honest multi-name meaning; refusing is one line and keeps the N == 1 path untouched. The Bloomberg lookup is
   never memoized.
3. **Multi-name output adds exactly two line shapes** (`BATTERY NAME i of n: <key>` before each block and one
   `BATTERY DONE: ...` footer) and changes none. N == 1 prints neither, which is what the byte-identity criterion
   (AC3, pinned comparator, controlled at the cut) holds.
4. **Keys are resolved up front for every name, before any fetch**, so a refused option or a keys error surfaces with
   0 network calls.
5. **Pin:** `04f518851d`. Re-pin to the issuance commit if s.34 moves anything under `lib/`.

<status>complete</status>
<round>26</round>
<slot>~101</slot>
<fabric>site-z</fabric>

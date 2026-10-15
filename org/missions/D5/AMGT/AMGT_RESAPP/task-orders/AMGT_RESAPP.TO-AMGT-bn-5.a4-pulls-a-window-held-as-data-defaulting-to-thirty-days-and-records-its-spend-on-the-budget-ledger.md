# AMGT_RESAPP task order -- `AMGT-bn-5` -- THE A4 DAILY PRICE PULL (`price_axis_pull.py`) TAKES ITS PULL WINDOW FROM A DATA FILE (DEFAULT 30 DAYS, NOTHING MOVES), RANKS ONLY THE LAST 30 DAYS AT EVERY WINDOW, PERSISTS WHAT IT PULLED AND RECORDS ITS SPEND ON THE BUDGET LEDGER (THE CODE HALF; THE 90-DAY APPLY IS A LATER PAIR AND A SITE Z ORDER)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bn-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~473</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bn-5.a4-pulls-a-window-held-as-data-defaulting-to-thirty-days-and-records-its-spend-on-the-budget-ledger</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests in a worktree; nothing is scheduled or changed on the terminal box by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call: every test stubs the Bloomberg client, the S3 client and the ledger; git and python only.
comp-adversary: RUN at the cut -- AC1's test file `integrations/bloomberg/research/tests/test_price_axis_window.py` does not exist at the base, so AC1 reads rc=4 `no tests ran` there (read here); AC2's two existing test files read `1 failed, 9 passed` at the base, the one failure being `test_price_axis_pull_client_is_the_loopback_dapi_not_a_lambda` on `ModuleNotFoundError: No module named 'blpapi'` (the Bloomberg API library is not installed on this box).
EGRESS CLASS, declared: NONE. No vendor call, no AWS call, no network: the worker never imports a live `blpapi` session (tests inject a stub client).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-473` (branch `wk-AMGT_RESAPP-473`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-473`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bn-5` (round 107, decomposition s.116)

**Why.** Andrew-direct (2026-10-15 ~21:2xZ): "increase limits on all our pull surfaces". The CTO ruled that the A4 leg's limit is its history window, stepping 30 -> 90 -> 365 days one completed good day per step, with the draw measured; the first step (90) is applied later under a never-widen pair, the third step (365) only on the CTO's read of a measured 90-day. THIS cell is the CODE HALF: the window becomes DATA, defaulting to today's 30, so landing this code moves nothing.

**What the code does today (read at the base).** `integrations/bloomberg/research/price_axis_pull.py` (the daily job on the Bloomberg terminal box, run through the estate's raw client `integrations/bloomberg/mcp/blp_client.py`): `main()` sets `start = as_of - timedelta(days=WINDOW_DAYS)` (line ~377; `WINDOW_DAYS` is 30, imported from `lib.research.price.axis`, pinned to the committed chatter gate), pulls `PX_LAST` DAILY for every covered name in chunks of 20 (`blp.historical_data(grp, ["PX_LAST"], start_ymd, end_ymd, "DAILY", timeout_s=180.0)`, line ~388), keeps rows with a non-null `PX_LAST`, drops a ticker with fewer than 2 rows into `insufficient`, builds `series_by_ticker`, ranks it through `compute_price_axis(...)`, and then calls `price_series_persist.run_daily_window_step(series_by_ticker, as_of_key, window_start, window_end, ...)`, which persists the series write-once for that day (object `daily_30d.json`) and builds the 90- and 365-day generations from the stored history. The stored history is merged by `price_series_persist.load_history`: the one-time year pull, then every daily object oldest to newest, per ticker by date, THE LATER OBJECT WINNING a date both hold. So a daily series that carries more days refreshes those days in the stored history, with no change to `load_history`. Measured on the stored series (2026-10-14): 94 names, about 22.6 observations per name, about 2,126 observations a day.

**The change (all in `integrations/bloomberg/research/price_axis_pull.py` plus one new data file and one new test file).**
1. A data file `integrations/bloomberg/research/price_axis_window.json`: `{"steps": [30, 90, 365], "step": 0, "claim": "held", "basis": "CTO msgs 6265 and 6279 (round 107): A4's history window steps 30 -> 90 -> 365 days on the ramp terms; the file holds the CURRENT step; step 0 is today's behaviour"}`. Ships with `step` 0.
2. A function `load_pull_window(path=None) -> int` in `price_axis_pull.py`: returns `steps[step]` when the file parses, `steps` is exactly `[30, 90, 365]` and `step` is an integer in 0..2; in EVERY other case (missing file, unreadable, invalid JSON, a different `steps`, `step` out of range or not an integer) it returns 30 and logs one line naming the reason (fail closed to today's behaviour). `main()` uses it for the PULL window: `start = as_of - timedelta(days=pull_days)`. A new CLI option `--window-days {30,90,365}` overrides the file (for tests and dry runs; documented in the `--help` text). Log one line at the start of a fire: `pull window: <d> days (step <k>, source <file|override|default>)`.
3. THE RANKING WINDOW DOES NOT MOVE. `WINDOW_DAYS` stays 30 and is the ranking window at every step: before `compute_price_axis` (and before the `insufficient` test of fewer than 2 observations) trim each ticker's series to the observations dated on or after `as_of - timedelta(days=WINDOW_DAYS)`, so the 30-day TRENDING and BREAKOUT products are byte-identical at step 0, 1 and 2 for the same pulled data. What is PERSISTED through `run_daily_window_step` is the FULL pulled series (not the trimmed one) with `window_start` the pulled start, so a wider pull refreshes stored history. The total-return leg (`TR_WINDOW_TRADING_DAYS = 5`) and the exit codes are unchanged.
4. Spend on the budget ledger. After the pull, on a real (non-dry-run) fire, ONE line to the shared Bloomberg budget ledger, written the way `integrations/bloomberg/research/model_block_pull.py` writes its own (read its `BUDGET_MODE`, `BUDGET_LEDGER_GLOB` and `record_fire_budget` at lines ~2195-2226 and follow that pattern): load `bbg_budget.py` by the glob `("data", "*", "scripts", "rivalfunds", "bbg_budget.py")` under the repository root (exactly one hit, else return False), and call `mod.record(mode, rows, batch_id)` with mode `amgt-price-axis`, `rows` = the total count of `PX_LAST` observations the vendor RETURNED (non-null, summed over every name BEFORE any trimming), and `batch_id` = `amgt-price-axis:<stamp>:calls=<number of historical_data calls>:names=<names pulled>:pull_days=<d>:rows_unit=returned-observations`. The helper NEVER raises: any failure returns False and the fire's exit code is unchanged. A `--dry-run` records nothing.

Do not edit `price_series_persist.py`, `lib/research/price/`, the total-return leg, the chatter job, the universe loader, or any file not named in `<paths>`.

**Do this in order.** (1) Write `integrations/bloomberg/research/tests/test_price_axis_window.py` FIRST, in the style of `test_price_axis_pull.py` beside it (it inserts `integrations/bloomberg/mcp`, `integrations/bloomberg/research` and the repository root on `sys.path` and imports `price_axis_pull as pap`; Bloomberg is NOT importable on this box, so inject a stub client object with a `historical_data(securities, fields, start, end, periodicity, timeout_s=...)` method returning `{security: [{"date": date, "PX_LAST": float}, ...]}`, and monkeypatch every other boundary: the universe loader, the identity index, the writers). At least these named tests: W1 the shipped file reads step 0 and `load_pull_window` returns 30; W2 steps 1 and 2 return 90 and 365; W3 a missing file, invalid JSON, a different `steps` list, `step` 3, `step` "1" and `step` true each return 30 and log a reason; W4 at pull window 90 the stub receives a `start` 90 days before `as_of` (and at 30, 30 days); W5 (the difference control) the 30-day ranking products computed from one fixed set of series are identical at pull windows 30, 90 and 365, where the 90 and 365 inputs carry extra older observations; W6 the series handed to `run_daily_window_step` carries the whole pulled window while the series handed to `compute_price_axis` carries only the last 30 days; W7 the budget line: mode `amgt-price-axis`, `rows` equal to the stub's returned observations, `batch_id` ending `rows_unit=returned-observations` (monkeypatch the ledger module so no file is written); W8 an unreadable or missing ledger module returns False, never raises and leaves the exit code unchanged; W9 `--dry-run` records no ledger line; W10 the seam with the real neighbour: write a 90-day daily object and a 30-day year-pull object into a stub S3 client the way `price_series_persist.persist_series` writes them, call the real `price_series_persist.load_history`, and show the later (wider) object's value wins an overlapping date. (2) Run it once: it must fail (no `load_pull_window`); record that run. (3) Make the product edits, only in the files named in the change. (4) Run AC1 and AC2. (5) Report.

If a premise above does not reproduce (a line, a function or a name is not where this order says), file a BLOCKING row naming exactly what you found, finish the other items and report; do not patch around it.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. No vendor call, no AWS call, no network, no `pip install`, no push of shared branches. `blpapi` is not installed and must stay uninstalled: the existing failing test `test_price_axis_pull_client_is_the_loopback_dapi_not_a_lambda` is a pre-existing failure you must not fix or mask.
2. Edit only the files named in `<paths>`. The shipped `step` is 0; never ship a step other than 0.

## 3. SURFACES

<paths>
integrations/bloomberg/research/price_axis_pull.py
integrations/bloomberg/research/price_axis_window.json
integrations/bloomberg/research/tests/test_price_axis_window.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~473/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bn-5"><invocation>cd C:/dev/wk-resapp-473 &amp;&amp; timeout 300 python -m pytest integrations/bloomberg/research/tests/test_price_axis_window.py -q 2>&amp;1 | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>a final line `<n> passed` with n at least 10 and no `failed`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bn-5"><invocation>cd C:/dev/wk-resapp-473 &amp;&amp; timeout 300 python -m pytest integrations/bloomberg/research/tests/test_price_axis_pull.py integrations/bloomberg/research/tests/test_price_axis_total_return.py -q 2>&amp;1 | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the final line `1 failed, 9 passed` where the one failure is `test_price_axis_pull_client_is_the_loopback_dapi_not_a_lambda` on `No module named 'blpapi'` (identical to the base); and exit=1</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~473 <0.9.0_WK_AMGT_RESAPP~473@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~473/AMGT_RESAPP.TO-AMGT-bn-5.a4-pulls-a-window-held-as-data-defaulting-to-thirty-days-and-records-its-spend-on-the-budget-ledger.proof_of_spec.json` with `to_id` equal to the `<to_id>` line above, character for character; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters; if the checker refuses the instance for a missing `decomp_ref`, add it from the order's own `<decomp_ref>` block. Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.

Report once:
- the commit hash;
- the first (failing) run of the new test file and the run after;
- AC1's and AC2's output lines;
- the diff stat, and the lines of `price_axis_pull.py` that read the window, trim for ranking and record the ledger line;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO msgs 6265 and 6279: cut bn-5 with the window held as data (default 30, a step file), A4's spend recorded to the budget ledger, 90 applied on the ramp terms under its pair, 365 on the CTO's read of a measured 90-day. This order is the CODE HALF only; landing it at step 0 moves no served value (W5 is the difference control; the persisted object is the full pulled series, which at step 0 equals today's). **THE CTO'S DESIGN QUESTION ("does A4 re-pull the whole window every day?"): YES.** Measured and read: `price_axis_pull.py` line ~377 and ~388 pull the whole 30-day window for every covered name every trading day (94 names, about 2,126 observations a day on 2026-10-14, `daily_30d.json` in `opal-data-harvest` under `bloomberg/harvest/bronze/price_history_px_last/`); the 90- and 365-day generations are built with NO vendor request from the stored history (the one-time year pull of 2026-10-03, 95 names and 26,081 observations over 2025-08-28 to 2026-10-02, plus every daily object, later wins a date). So the 365-day window already exists at today's draw; a daily 90-day pull (about 6,400 observations) or 365-day pull (about 25,900, 88% of the drawer's ruled 5x history ceiling of 29,290) would only REFRESH stored rows (restatements and split adjustments), not create them. One backfill plus the daily 30-day delta is already the structure; the step-3 read is therefore a periodic re-backfill (one drawing day of about 26,000 observations) against a daily 365-day pull (about 25,900 every day). **The apply is a SEPARATE order:** setting `step` to 1 on the terminal box (site Z) changes what is persisted (a wider overlay), so it takes the never-widen pair (COO half, then the CTO's half, the blast radius being the stored overlay rows of the 90 days and the 90/365 generations for 94 names; rollback = `step` back to 0, noting persist is write-once per as_of: an as_of whose daily object already exists refuses a different series, so the apply day must start before that day's run), then a CloudOps order at site Z coordinated MSTR to MSTR (`0.0.0_AB_MSTR~DELL1`). Pre-existing failure at the base: `test_price_axis_pull_client_is_the_loopback_dapi_not_a_lambda` (no `blpapi` on dell1; the terminal box has it). AC2 expects exit 1 for that reason.

<status>complete</status>
<round>107</round>
<workstream>A4</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~473</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

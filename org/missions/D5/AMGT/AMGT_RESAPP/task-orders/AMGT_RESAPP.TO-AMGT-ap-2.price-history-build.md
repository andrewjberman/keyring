# AMGT_RESAPP task order -- `AMGT-ap-2` -- FWD-36 PRICE 90/365: THE ONE-TIME YEAR PULLER, THE 90/365 GENERATIONS, THE ROUTE READ, THE DAILY JOB'S PERSIST AND 90/365 STEP

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ap-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~218</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN by the issuer at the cut -- the scheduled task runs integrations/bloomberg/pipeline/scheduled_daily_pull.cmd from the working tree, which calls price_axis_pull.py with no arguments; that cadence is unchanged, and the cmd is untouched. The new step rides the existing daily run (ANDREW-DIRECT ~20:5xZ, ADDENDUM 2 @205bd13011).
comp-iam: RUN by the issuer at the cut -- the daily job gains one S3 write-once object per as_of and new generation partitions; this order builds and tests only, and the writes first run after the drain (the issuer's act, under a pair).
comp-adversary: RUN by the issuer at the cut -- r66_served c22 FAILS at the base, local and deployed: 0 rows and "not produced yet" on trending and breakout x 90 and 365.
EGRESS CLASS, declared: NONE for this order. The puller's --plan mode makes no vendor call; its --live mode is NOT run here (AMGT-ap-3 runs it once).
</preflight>

**Your worktree:** `C:/tmp/r66-218` (branch `wk-AMGT_RESAPP-218`, cut from the issuance commit with `--portal-ref a730d8ce`). Work and
commit only there. Start every shell call with `cd /c/tmp/r66-218`: a call that starts elsewhere resolves
`git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ap-2` (round 66, decomposition s.74; PRD v0.37 FWD-36, price half)

FWD-36: the price ranking takes `?days=30|90|365`, and each window ends at the last trading day. Today the price axis is generated
at 30 days only. `integrations/bloomberg/research/price_axis_pull.py` pulls 30 days of PX_LAST per covered ticker every trading day,
and writes ranked generations through `lib/research/price/generation.py`. `?days=90|365` answers "not produced yet"
(`lib/research/api/rolling_windows.py` `price_window_not_produced`). Andrew approved ONE pull of a year of daily PX_LAST (card 4),
and at ~20:5xZ that the daily job also persists the 30-day series it already fetches ("your rec is approved").

1. **NEW `integrations/bloomberg/research/price_history_pull.py`**, run box-side through `integrations/bloomberg/mcp/blp_client.py`
   the way `price_axis_pull.py` does, with the same universe resolution (every covered name; a key with no Bloomberg form is
   excluded with a reason).
   - `--plan` (the default) makes NO vendor call and NO write. It prints:
     - the universe size and the excluded count;
     - the window, 400 calendar days ending at `lib.trading_calendar.prev_trading_day(today)`;
     - the S3 key;
     - the partition names;
     - "vendor calls 0, writes 0".
   - `--live` pulls PX_LAST daily over that window for every ticker. It lands the raw series as ONE write-once S3 object, whose
     key is `lib/opal_naming address()` output (a builder refusal means adding the missing registry row under
     `infra/logic/registry/`, never a hand-typed key). It then builds the 90- and 365-day TRENDING and BREAKOUT generations at the
     pull's as_of through `generation.py`.
   - **Do NOT run `--live`.** AMGT-ap-3 runs it once.
2. **The 90/365 generations:**
   - They live in partitions distinct from the 30-day ones; you choose the naming and declare it in the module docstring.
   - The 30-day partitions, pointers and outputs are never written.
   - Existing functions the 30-day path calls are not edited. Add new functions only. The existing `lib/research/price/tests`
     must pass unchanged.
3. **The route read** (`lib/research/api/`, the price `?days` branch in `scoped_amgt.py`, and `rolling_windows.py`):
   - `?days=90|365` on trending/price and breakout/price reads the latest generation of that window.
   - It serves the generation's rows with `window_days` and `window_end`, which is the generation's as_of: the REAL end date.
   - It also serves `window_end_requested`, the last trading day.
   - When those two dates differ, it serves a plain `window_note` naming the end date.
   - With no generation of that window, the existing "not produced yet" answer stands.
   - `?days=30` and the default are unchanged.
4. **The daily job** (`integrations/bloomberg/research/price_axis_pull.py`, with a NEW helper module
   `integrations/bloomberg/research/price_series_persist.py`). After its unchanged 30-day pull and generations, the job:
   - (a) persists the series it already fetched to the same S3 history, write-once per as_of;
   - (b) builds that day's 90- and 365-day TRENDING and BREAKOUT generations from the stored history (the year pull plus the daily
     series), so the windows end at the last trading day.

   Constraints:
   - No new vendor request.
   - The 30-day leg's writes and exit codes (0 / 3 / other) stay byte-identical.
   - A failure in (a) or (b) is logged with a reason and NEVER fails the 30-day leg, nor changes its exit code.
   - With no year history in S3, (b) skips with a logged reason.
   - `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd` is NOT in your write surface.
   - The scheduled task runs the working tree, so your edit becomes the deploy when the issuer drains it under a pair, never
     before. Never copy it into the shared tree yourself.
5. **Tests** in `lib/research/price/tests/test_price_windows.py` and `lib/research/api/tests/test_price_windows_route.py`:
   - (i) a planted series gives the declared 90- and 365-day TRENDING and BREAKOUT rows;
   - (ii) the route serves a planted 90/365 generation with `window_end`, and with `window_note` when the end is earlier than the
     last trading day;
   - (iii) with no generation, "not produced yet";
   - (iv) the persist function writes once and refuses an overwrite;
   - (v) the daily job's 30-day writes and exit code are unchanged with the new step on, with the new step failing, and with no
     year history;
   - (vi) a planted history plus a daily series gives 90/365 generations ending at the daily as_of.

Run `lib/research/api/tests/` and `lib/research/price/tests/` before your commit and report both last lines. After your commit, run
`bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh --build-only /c/tmp/r66-pkg-218.zip` and report its `SIZE:` line.
A build past the ceiling is a STOP.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W218-S<k>`, `disarm_owner`
`2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No vendor call (no `--live`, and never run `price_axis_pull.py` for real), no S3 or table write,
   no deploy, no portal write.
2. `scheduled_daily_pull.cmd` is untouched.
3. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
integrations/bloomberg/research/price_history_pull.py
integrations/bloomberg/research/price_series_persist.py
integrations/bloomberg/research/price_axis_pull.py
lib/research/price/
lib/research/api/
infra/logic/registry/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~218/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ap-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/price/tests/test_price_windows.py lib/research/api/tests/test_price_windows_route.py; echo "exit=$?"</invocation><expect>every case passes (90/365 rows from a planted series; the route serves window_end and window_note; "not produced yet" with no generation; write-once persist; the daily job's 30-day writes and exit code unchanged with the step on, failing, or without history; daily 90/365 ending at the as_of); and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ap-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round64/checks/r64_served.py --cell c10 --where local; echo "exit=$?"</invocation><expect>R64 C10 SERVED: YES (30 unchanged; 90/365 still "not produced yet", since no generation exists before the live pull); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ap-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" "C:/Users/Opal Bloomberg/AppData/Local/Programs/Python/Python311/python.exe" integrations/bloomberg/research/price_history_pull.py --plan; echo "exit=$?"</invocation><expect>a plan naming the universe size, the 400-day window ending at the last trading day, an address()-built S3 key, the 90/365 partition names, and "vendor calls 0, writes 0"; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~218 <0.9.0_WK_AMGT_RESAPP~218@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~218/AMGT_RESAPP.TO-AMGT-ap-2.price-history-build.proof_of_spec.json`.
Report once:
- the commit hash
- every criterion's output lines
- both suites' last lines
- the SIZE line
- the S3 key and the partition names
- the functions you added
- any row

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** ADDENDUM 1 @1162e9be0e option (a) + ADDENDUM 2 @205bd13011 (Andrew ~20:5xZ, the daily job's change approved);
card 4 (record @9fe6e6f111). The drain of this order into the shared tree IS the daily job's deploy: COO + CTO never-widen halves
first, then the issuer drains; rollback is reverting the drain before the next scheduled run. Live pull is ap-3; serve is ap-4.

<status>pending</status>
<round>66</round>
<slot>0.9.0_WK_AMGT_RESAPP~218</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

# AMGT_RESAPP task order -- `AMGT-an-1` -- FWD-36: ROLLING 30/90/365-DAY WINDOWS ON THE LEAD PANEL (CHATTER COUNTS; THE PRICE HALF A QUALIFIED WAIT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-an-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~210</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- no new write; every pool or table access is a read the function already makes.
comp-adversary: RUN by the issuer at the cut -- r64_served c9 and c10 FAIL at the base: no window fields on collected/chatter; ?days is ignored by the price ranking.
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r64-210` (branch `wk-AMGT_RESAPP-210`, cut from the issuance commit with `--portal-ref a730d8ce`, so the
portal fixture the api tests read is present). Work and commit only there. Start every shell call with `cd /c/tmp/r64-210`: a call that
starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-an-1` (round 64, decomposition s.72; FWD-36)

PRD `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` FWD-36 (v0.35). Issuer ruling R1, s.72.
1. **`/lead-panel/timeseries/collected/chatter` takes `?days=30|90|365`, default 30** (`scoped_amgt.py` around :4878 calls
   `monthly_chatter.read_monthly_chatter()` with no arguments today).
   - Each window ends at the last trading day (`lib.trading_calendar`). The response serves `window_days`, `window_start`,
     `window_start_requested` and `window_end`.
   - When the store begins after the requested start (the harvest store begins 2026-01-01), `window_start` is the store's first day and
     `window_note` says so in plain words.
   - Every row serves `articles_total` (an int), re-aggregated from gold `chatter_daily` over the window.
   - Every row serves `tone` and `voters` as null, each beside `tone_reason`: "window tone is held: the HARVST sentiment outcomes are held
     on the publisher-terms card". Never compute tone at request time.
   - `by_month` stays on every row, unchanged, because the page still reads the calendar-month view.
   - An unrecognised `days` value answers 400 with the allowed values.
2. **`/lead-panel/rankings/breakout/price` takes `?days`** (around :4870).
   - `30` and the default serve today's rows unchanged.
   - `90` and `365` serve no rows, with `window_reason` "the 90- and 365-day price windows are not produced yet: they need a longer
     price-history pull, which waits on Andrew's word". This is a QUALIFIED WAIT (CTO ruling msg 28740); never synthesise a 90/365
     ranking from the 30-day rows.
3. Tests in `lib/research/api/tests/` for both routes, each window, the store-shorter note and the 400.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W210-S<k>`, `disarm_owner`
`2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no vendor or model call, no portal write.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-an-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/api/tests/; echo "exit=$?"</invocation><expect>every test passes, your new tests included, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-an-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round64/checks/r64_served.py --cell c9 --where local; echo "exit=$?"</invocation><expect>C1 PASS for default, 30, 90 and 365 (window fields, a trading-day end, every row articles_total + tone/voters null beside tone_reason + by_month); R64 C9 SERVED: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-an-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round64/checks/r64_served.py --cell c10 --where local; echo "exit=$?"</invocation><expect>C1 PASS for default and 30 (rows at window_days 30); C2 PASS for 90 and 365 (no rows, 'not produced yet'); R64 C10 SERVED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~210 <0.9.0_WK_AMGT_RESAPP~210@opal.agent>" -F <msgfile> -- <paths>` (message file written
with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~210/AMGT_RESAPP.TO-AMGT-an-1.rolling-windows.proof_of_spec.json`. Report once: the commit
hash, every criterion's output lines, the functions you changed, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** PRD v0.35 FWD-36; CTO msg 28740 (price half a qualified wait; tone held on the publisher-terms card). Served by an-7.

<status>pending</status>
<round>64</round>
<slot>0.9.0_WK_AMGT_RESAPP~210</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-02 ~22:3xZ):** ACCEPTED. Worker ~210 `2f11a291cb`/`6cb0deceb5`, drained `37da943651`. Re-graded on
the shared tree: union (peers + management + api) 610 passed exit=0; c9 YES (default/30/90/365, the 365-day window reads the store start
2026-01-01 with its note); c10 YES (30 serves 94 rows; 90/365 serve 0 with "not produced yet"). Package delta, measured by the issuer at
the drain (an-1 was spawned before AMENDMENT 1): 253,690,058 B, 96.8% of the ceiling (+20,026 B against leg 3's 253,670,032 B; the
build also carries HARVST's `finbert_sentiment.py` and `publication_gold.py`, foreign carriers that an-7's half must account for). Served by an-7.

<status>complete</status>

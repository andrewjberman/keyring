# AMGT_RESAPP task order -- `AMGT-bj-5` -- THE RESEARCH PRICE AXIS PULLS AND KEEPS THE TOTAL-RETURN FIELD OVER THE LAST FIVE TRADING DAYS (SITE Z CODE; ANDREW-DIRECT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bj-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~407</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bj-5.the-research-price-axis-pulls-and-keeps-the-total-return-field-over-five-trading-days</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the daily job's schedule is not touched; its run is the queue's at site Z.
comp-iam: DECLARED-NOT-APPLICABLE -- the tests are offline (a fake client, a captured put); no AWS or Bloomberg call by the worker.
comp-adversary: RUN at the cut, each test against the literal code written below: the new test file reads '5 failed' against the unpatched modules (AttributeError on `tr_window_start`, `run_total_return_leg`, `persist_tr_series`) and, with the prepared patch in a scratch worktree, `9 passed, 1 deselected` together with the existing `test_price_axis_pull.py` minus `loopback_dapi`, which needs `blpapi` and passes only at site Z.
EGRESS CLASS, declared: NONE (the pull's Bloomberg requests run at site Z under the queue; this cell makes none).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-407` (branch `wk-AMGT_RESAPP-407`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-407`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bj-5` (round 103, decomposition s.111)

**Andrew-direct, 2026-10-13 (the queue form `org/tier1_exec/1.0.0_SA_CTO/deliverables/DEMQUE_QUEUE_FORM_ANDREW_20261013.md`, STANDING RULE): "TIME-WEIGHTED RETURN (TWR) PRICING ON EVERY
SURFACE. Every price series a surface keeps must support a total-return (TWR) reading: price plus distributions (dividends, interest), not price alone."** and the incremental rule: the last 5
trading days. The CTO (round-102 analysis item 4): `integrations/bloomberg/research/price_axis_pull.py` adds a total-return field to its daily pull at the 5-trading-day window; the rankings
stay on price until a PRD addendum says otherwise; it is a site Z cell and its draw goes through the queue. `integrations/bloomberg/READ_HERE.md` was read at the cut: a site-Z scheduled task runs
the working tree (an edit IS a deploy the moment it reaches that disk), so this cell changes NOTHING the PX_LAST legs do.

Apply the prepared edit, then verify it. The patch (two files) and the new test:

    cd C:/dev/wk-resapp-407 && git apply --whitespace=nowarn "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/r103_twr_source.patch"
    cp "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/r103_test_price_axis_total_return.py" integrations/bloomberg/research/tests/test_price_axis_total_return.py

What it does: (a) `price_series_persist.py` gains `persist_tr_series` and `tr_series_doc`: the total-return series lands as a SECOND write-once object,
`bloomberg/harvest/bronze/price_history_tot_return/date=<as_of>/daily_5d.json` (schema `price_tot_return_series_v1`, field `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS`), beside and never inside the
PX_LAST history (its objects, schema and `load_history` are untouched); (b) `price_axis_pull.py` gains `tr_window_start` (the first of the last five trading days, `lib.trading_calendar`, never
BDay), `pull_total_return` (that field only, groups of 20, a row without it dropped), `run_total_return_leg` (pull then persist; nothing persisted on a dry run; NEVER raises) and ONE call to it
in `main`, after every PX_LAST leg and write, whose result the exit-code logic does not read. About 500 history cells a day at 5 days (the queue form's own figure). If `git apply` refuses,
STOP and file a BLOCKING row: do not edit by hand.

Then run `python -m py_compile` on the two modules and AC1.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W407-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Exactly these files: `integrations/bloomberg/research/price_axis_pull.py`, `integrations/bloomberg/research/price_series_persist.py` and the new
   `integrations/bloomberg/research/tests/test_price_axis_total_return.py`. No other file.
2. No Bloomberg call, no AWS call, no network, no deploy, no store write, no schedule. No `pip install`. Never mint `data/bloomberg/`. Standing: no push of shared branches.
3. The PX_LAST request (`["PX_LAST"]`, the 30-day window), the ranking writes and the exit codes are NOT changed; the new leg runs after them and cannot change them.

## 3. SURFACES

<paths>
integrations/bloomberg/research/price_axis_pull.py
integrations/bloomberg/research/price_series_persist.py
integrations/bloomberg/research/tests/test_price_axis_total_return.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~407/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bj-5"><invocation>cd C:/dev/wk-resapp-407 &amp;&amp; python -m pytest integrations/bloomberg/research/tests/test_price_axis_total_return.py integrations/bloomberg/research/tests/test_price_axis_pull.py -k "not loopback_dapi" -q 2&gt;&amp;1 | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>`9 passed, 1 deselected` (the five new tests and the four existing ones that run off site Z); and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bj-5"><invocation>cd C:/dev/wk-resapp-407 &amp;&amp; git diff --name-only "$(git merge-base HEAD box/dell1)" HEAD -- . ":(exclude)org" | sort</invocation><expect>exactly three lines: `integrations/bloomberg/research/price_axis_pull.py`, `integrations/bloomberg/research/price_series_persist.py`, `integrations/bloomberg/research/tests/test_price_axis_total_return.py`, and no other line</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~407 <0.9.0_WK_AMGT_RESAPP~407@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~407/AMGT_RESAPP.TO-AMGT-bj-5.the-research-price-axis-pulls-and-keeps-the-total-return-field-over-five-trading-days.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- criterion AC1's and AC2's output lines;
- `git diff HEAD~1 HEAD --stat`;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CODE lands on `box/dell1` and reaches site Z by box-sync; the producer's next daily run then writes the new object and requests about 500 more cells a day through the
queue (`2.0.0_SA_COO~Q1` prices the card amendment: the issuer sends it at the merge; the Terminal sign-in is Andrew's act). THE CLOSE is the producer's next run's stored object (a read of
`price_history_tot_return/date=<as_of>/daily_5d.json`, its schema, field and ticker count), which the issuer reads: not this order's. No served byte moves and no ranking changes; the rankings
switch to total return only on a PRD addendum (the CTO). The queue form's census row A3 ("rival funds, history still owed: the close only") and B1/B2 are other projects' surfaces.

<status>complete -- 2026-10-13T17:5xZ by the issuer (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-407 @fbd996c088 (code 6e8f4d013d) merged, proof instance VALID (rc=0). AC1 re-run by the issuer on the worker's tree: 9 passed, 1 deselected (the five new tests and the four existing ones that run off site Z; `loopback_dapi` needs blpapi); AC2: exactly the three files; the three blobs equal the prepared candidate (price_axis_pull.py cb191272359e, price_series_persist.py 782979c3e2a3, the test d322d0453cad). THE CODE IS ON box/dell1, NOT YET RUNNING: it reaches site Z by box-sync and the producer's next daily run after the Terminal sign-in (Andrew's act) writes bloomberg/harvest/bronze/price_history_tot_return/date=<as_of>/daily_5d.json (schema price_tot_return_series_v1, field DAY_TO_DAY_TOT_RETURN_GROSS_DVDS) and requests about 500 more history cells a day. The PX_LAST request, its 30-day window, the ranking writes and the exit codes are unchanged; the rankings stay on price. THE CLOSE is that object's read after the first run, the issuer's. The card amendment and quote for the added cells go to 2.0.0_SA_COO~Q1 (one ask). **THE BACK YEAR (CTO msg 4983, via COO~Q1 msgs 4979 and 4980): the field accrues FORWARD ONLY; no 25,100-cell pull of 365 days. If a back year is ever needed it is DERIVED from the stored PX_LAST year plus DVD_HIST_ALL (one bulk request per company), dividends reinvested on the ex-date close, the porting test's own formula. Quote: +500 cells a day (about 100 companies x 5 days x 1 added field), claim held until the next run counts the companies.**</status>
<round>103</round>
<slot>0.9.0_WK_AMGT_RESAPP~407</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

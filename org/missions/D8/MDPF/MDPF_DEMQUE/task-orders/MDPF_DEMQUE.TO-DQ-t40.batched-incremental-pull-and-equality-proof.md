# TO MDPF_DEMQUE.TO-DQ-t40 -- round 9 DQ-t-40: a batched incremental Yahoo pull, measured, and proved cell-for-cell against the per-symbol path
<to_id>MDPF_DEMQUE.TO-DQ-t40</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~32</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>BATCHPULL</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-40` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 5) |
**outcome_ref:** C-PRICES, C-YAHOO, FWD-8 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-40` (CTO round-8 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round8.md` ADDENDUM 6, read it). The standing daily
extension re-pulls each enrolled symbol with one vendor request (`yahoo_pull.pull`, `yfinance.Ticker(sym).history(period="max", auto_adjust=False,
actions=True)`), about 938 requests a day against the shared pacer's cap of 400, which the CTO refuses to raise. The ruling: pull ONLY the dates
after each symbol's stored maximum, for many symbols in ONE multi-ticker vendor call, as-traded with corporate actions (the same unadjusted read),
and PROVE it equal to the per-symbol path before it is used. This order builds the puller and the proof; wiring it into the daily draw is a
later order written on your report. **The honest unit is the HTTP request that leaves this machine, not the call you make into the library:** the
vendor library's multi-ticker call may issue one HTTP request per symbol underneath. Measure it; do not assume it.

**Build** (NEW files under `data/mdpf/scripts/demque/`; read `yahoo_pull.py` (`pull`, `PullResult`, `Pacer`, the status constants) and
`price_store.py` first; import, do not copy):
1. `batch_pull.py`:
   - `pull_batch(since: dict[str, str | None], fetch_many=None) -> dict[str, PullResult]`. `since` maps symbol -> the stored maximum date
     (ISO) or None (a full history). Each result has `prices` (`date`, `close_served`, `as_traded_close`, computed exactly as `yahoo_pull.pull` does:
     the split factor of every split dated strictly after the row), `splits`, `dividends`, status `OK` / `FAILED_EMPTY` / `FAILED_REFUSED`, and holds
     ONLY dates after `since[symbol]`. The default `fetch_many(symbols, start)` is the library's multi-ticker download with `auto_adjust=False,
     actions=True, group_by="ticker", progress=False, threads=False`, `start` = the earliest `since` day minus nothing (filter per symbol afterwards).
   - A symbol the vendor returns nothing or an error for is a `FAILED_EMPTY` / `FAILED_REFUSED` result for THAT symbol only: it has no price rows,
     never a number, and the rest of the batch is returned as usual. A pushback (HTTP 429-class) is `STOPPED_PUSHBACK` for the whole call.
   - IMPORTANT: a split factor needs splits dated after each price row, and an incremental window may not contain the old rows' later splits. State
     in the module docstring how `close_served` of the NEW rows is computed (new rows only: factor from splits after each new row, which the window
     contains) and that restating OLD rows' `close_served` is the per-symbol full-history path's job, not this one's; the proof compares new rows only.
   - `--spot N` CLI: take N symbols from the served store's index (`price_store.index`), set each `since` to its stored max minus 20 calendar days
     (so a window of recent rows exists), run BOTH paths (per-symbol `yahoo_pull.pull` filtered to dates after `since`; the batch), and print ONE JSON
     line `{"equal": k, "of": N, "http_batched": a, "http_per_symbol": b}`. Exit 0 always unless a path raises.
2. **Measure the HTTP requests of both paths** (the counter is part of the deliverable): wrap the library's HTTP layer (yfinance 1.7.0 uses
   `curl_cffi`; start at `yfinance/data.py` `YfData` and its `get` / `_make_request`) with a counting hook that does not alter responses, in a helper
   `http_counter.py`; record, for 10 symbols, the request count of (i) 10 per-symbol `history()` calls and (ii) ONE multi-ticker download. State
   whether the multi-ticker call is ONE request or n requests. This decides the CTO's branch; report it plainly.
3. **The equality proof** `batch_equality.py --n 50 --out <path>` writes
   `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~32/EQUALITY_REPORT.json`:
   `n_symbols_compared` (>= 50, drawn from the store's index across ETFs, mutual funds and at least one more class, each symbol's class named from the
   lock record or the client transactions' `Asset_Type`; add foreign listings if the store has any), `asset_classes`, `equal_symbols`,
   `mismatches` (`[{"symbol", "date", "field", "per_symbol", "batched"}, ...]`), `cells_compared` `{prices, dividends, splits}` (each > 0: choose each
   symbol's `since` so a dividend or a split lies inside its window, and say how many symbols carried one), `isolated_failure` `{"symbol",
   "price_cells_stored", "rest_of_batch_equal"}` (one planted ticker that does not exist inside a real batch), `http_requests` `{"per_symbol",
   "batched"}` (the totals the proof itself caused, measured with the counter), and `verdict`: exactly `BATCH_REDUCES_HTTP_REQUESTS` or
   `BATCH_DOES_NOT_REDUCE_HTTP_REQUESTS`, with one sentence of evidence. Run it yourself in the background (it makes 100+ vendor requests; pace the
   per-symbol arm with `yahoo_pull.Pacer` on a scratch state file, 8 to 12 s gaps is slow: you may set `min_gap=1.0, max_gap=2.0` for this
   proof only and say so in the report). No more than 130 symbol-requests in total.
4. NEW `test_demque_batch_pull.py` (pytest; a stub `fetch_many`, no network) with exactly these names:
   `test_incremental_window_starts_the_day_after_each_stored_max`,
   `test_a_symbol_the_vendor_refuses_is_a_failure_for_that_symbol_alone_never_a_price`,
   `test_batch_rows_equal_per_symbol_rows_on_a_universe_with_splits_and_dividends_in_the_window`.

### ACCEPTANCE

<criterion id="DQ9-t40-AC1" cell_refs="DQ-t-40"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t40_tests.py</invocation><expect>BATCH-OK</expect></criterion>
<criterion id="DQ9-t40-AC2" cell_refs="DQ-t-40"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t40_equal.py</invocation><expect>EQ-OK</expect></criterion>
`DQ9-t40-AC1` -- the three named tests. `DQ9-t40-AC2` -- the equality report: at least 50 symbols across at least 3 classes, zero mismatches, price,
dividend and split cells all compared, the planted bad ticker isolated, the two HTTP counts and a verdict stated; and a live 5-symbol spot-check
equal 5 of 5. The check does not require the verdict to favour batching: it requires the measurement.

<expected_criteria>DQ9-t40-AC1,DQ9-t40-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `BATCH-BAD no file ...`; `EQ-BAD no file ...EQUALITY_REPORT.json`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No write to the served store, the real pacer state, the queue or the ledger, no AWS write, no Bloomberg call, no deploy.** Yahoo is read
  through the library only, under a scratch pacer, at most 130 symbol-requests across the whole order, one proof run.
- **You arm no timer, background task or OS task** beyond running your own proof in the background of your session.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W32-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. A mismatch is a finding, never something to fix by editing the comparison. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/batch_pull.py
data/mdpf/scripts/demque/http_counter.py
data/mdpf/scripts/demque/batch_equality.py
data/mdpf/scripts/demque/test_demque_batch_pull.py
org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~32/
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-40`.
<owned_cells>DQ-t-40</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t40-AC1, DQ9-t40-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~32/MDPF_DEMQUE.TO-DQ-t40.batched-incremental-pull-and-equality-proof.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t40-AC1,DQ9-t40-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the two HTTP counts and the verdict verbatim, the class mix of the 50, mismatches (if any) cell by
cell, how a split inside the window was handled, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed; wiring into the daily draw is a later order under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write.
comp-adversary: DECLARED-NOT-APPLICABLE a read-only puller and its proof; nothing is written to a served surface.
risk: LOCAL -- code, tests and records. Its later use changes how served prices are pulled and runs under its own never-widen pair (CTO ADDENDUM 6).
direct_act: false -- a worker order.
</preflight>

Source: CTO round-8 analysis @92a9b27704 ADDENDUM 6 (msg 4243); decomposition round 9.

# TO MDPF_DEMQUE.TO-DQ-t2 -- round 1 DQ-t-2: one gentle Yahoo request per security, stored as traded, through one shared pacer
<to_id>MDPF_DEMQUE.TO-DQ-t2</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~2</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `DQ-t-2` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 1) |
**outcome_ref:** FWD-1 | **depends_on:** none (chain B head; `DQ-t-3` follows in the same slot)

---

## WORKER FACE

### THE CELL

`DQ-t-2`, hop 3 of the FWD-1 thread: a locked symbol's whole daily price history is pulled from Yahoo Finance in ONE request, gently, and
stored as the client actually traded it.

**Build** NEW `data/mdpf/scripts/demque/yahoo_pull.py` with:

1. `pull(symbol, fetch=None) -> PullResult`. `PullResult` is a dataclass with exactly: `symbol`, `status` (one of `OK`, `FAILED_EMPTY`,
   `FAILED_REFUSED`, `STOPPED_PUSHBACK`), `http_status` (int or None), `prices` (DataFrame `date, close_served, as_traded_close`), `splits`
   (DataFrame `date, ratio`), `dividends` (DataFrame `date, amount`), `cells` (rows x fields drawn; the only field this round is close, so
   `cells = len(prices)`; 0 on any failure). `fetch` defaults to yfinance 1.7.0 (installed):
   `yfinance.Ticker(symbol).history(period="max", auto_adjust=False, actions=True)`; tests inject a stub.
   - `as_traded_close(d) = close_served(d) x product of every split ratio dated AFTER d`. yfinance's `Close` is split-adjusted even with
     `auto_adjust=False`: a 4-for-1 split later quarters every earlier close, so as traded multiplies it back.
   - An empty frame -> `FAILED_EMPTY`, empty `prices`, `cells = 0`. NEVER store or return price rows on a failure.
   - An HTTP 401, 403 or 429 (yfinance raises; read the status from the exception, else from its message) -> `STOPPED_PUSHBACK`; any other
     refusal -> `FAILED_REFUSED`.
2. `Pacer(state_path, min_gap=8.0, max_gap=12.0, daily_cap=400, sleep=time.sleep, today=None)`: ONE shared rule for every Yahoo request
   the queue drives.
   - `wait()` sleeps a random gap in `[min_gap, max_gap] x factor` since the last request (single-threaded);
   - `allow() -> bool`: False once `daily_cap` requests were made today, or once today saw a push-back;
   - `record(symbol, result)`: writes a checkpoint to `state_path` (JSON) after EVERY request: per symbol the last attempt and outcome,
     the day's count, a push-back flag;
   - `done(symbol) -> bool`: True for a symbol whose last outcome was `OK` (a resumed day skips it);
   - after a push-back day the next day's `factor` doubles; after a clean day it returns to 1.
3. `run(symbols, pacer, fetch=None) -> list[PullResult]`: in order, skips `done` symbols, stops when `allow()` is False, `wait()`s before each.
4. CLI `python yahoo_pull.py --probe SYMBOL`: one real pull of SYMBOL through a Pacer on a scratch state file under `.scratch/` (min gap 0
   for this single request), then prints exactly
   `PROBE symbol=<SYMBOL> status=<status> rows=<n> splits=<k> as_traded_2020-08-28=<as_traded_close on 2020-08-28, 2 dp, or NA>`. rc 0.
5. NEW `data/mdpf/scripts/demque/test_demque_yahoo.py` (pytest, stubbed fetch and sleep, no network) with exactly these names:
   `test_as_traded_close_undoes_later_splits`, `test_empty_answer_is_failure_never_prices`, `test_refusal_stops_the_day_and_checkpoints`
   (a 429 -> `STOPPED_PUSHBACK`, `allow()` False, state file written), `test_resume_skips_symbols_already_done`,
   `test_daily_cap_stops_drawing`, `test_gap_doubles_after_a_pushback_day`.

Prior art to follow, not import: `data/black_diamond/scripts/silver/backfill_yahoo_prices_safe.py` (checkpoint, stop on 401/403/429) --
its batch of 20 becomes ONE symbol per request here. Do NOT create `__init__.py` in `data/mdpf/scripts/demque/` (the issuer adds it).

**Yahoo egress from dell1 is authorised:** Andrew-direct ~19:1xZ 2026-10-08, record @489e1cd24c ("DELL boxes can call yahoo all they want
... you have to be gentle with it"). Your only live requests are the AC2 probe (one request; at most one retry).

### ACCEPTANCE

<criterion id="DQ1-t2-AC1" cell_refs="DQ-t-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R1_CHECKS/dq_t2_tests.py</invocation><expect>YAHOO-OK</expect></criterion>
<criterion id="DQ1-t2-AC2" cell_refs="DQ-t-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R1_CHECKS/dq_t2_seam.py</invocation><expect>YSEAM-OK</expect></criterion>
`DQ1-t2-AC1` -- pull, failure rule and pacer, by the six named tests. `DQ1-t2-AC2` -- the seam against real Yahoo: AAPL as traded on
2020-08-28 within 2% of 499.23 (the difference control: a pull that forgets the split prints ~124.81 and fails).

<expected_criteria>DQ1-t2-AC1,DQ1-t2-AC2</expected_criteria>

Run each invocation from the worktree root. Both FAIL at the base: `YAHOO-BAD no file ...`, `YSEAM-BAD rc=127 no PROBE line`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding and the probe's state file go under
  `.scratch/`, uncommitted.
- **No AWS call, no Bloomberg, no deploy.** Yahoo: the AC2 probe only.
- **You arm no timer, background task or OS task.**
- **Refusal clause.** If a criterion cannot be met as written (for example Yahoo pushes back on the probe twice), stop, write the reason in
  your report and a surprise row (id `MDPF_DEMQUE-W2-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or
  `BLOCKING`) in the investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/yahoo_pull.py
data/mdpf/scripts/demque/test_demque_yahoo.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 1, the thread), cell `DQ-t-2`.
<owned_cells>DQ-t-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ1-t2-AC1, DQ1-t2-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~2/MDPF_DEMQUE.TO-DQ-t2.yahoo-pull-and-shared-pacer.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ1-t2-AC1,DQ1-t2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE thread round.
risk: LOCAL -- code and tests; one authorised vendor GET (Andrew @489e1cd24c), no write.
direct_act: false -- a worker order.
</preflight>

Source: PRD v0.2 FWD-1, FWD-7, C-YAHOO, C-PRICES; dell2 research s.3, s.4; decomposition round 1.

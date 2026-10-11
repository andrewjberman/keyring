# TO MDPF_DEMQUE.TO-DQ-t31 -- round 9 DQ-t-31: a standing tier-1 request extends every locked symbol to the T-1 frontier each trading day
<to_id>MDPF_DEMQUE.TO-DQ-t31</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~24</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-31` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT) |
**outcome_ref:** C-PRICES | **depends_on:** DQ-t-30 (the same worker, second in its queue: `lock.py` carries `trades_through` and `latest_partition` when you start)

---

## WORKER FACE

### THE CELL

`DQ-t-31` (CTO round-8 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round8.md` R1 parts (a) and (c), read it; row
`MDPF_DEMQUE-D1-W22-S1`). All 141 served price files end 2026-06-22 or 2026-06-23, 76 trading days behind the T-1 frontier. Why, from the code:
`daily_draw.py` builds each security's window from the requests in the queue folder; `price_store.write` clips the pull to the lock row's
`[valid_from, valid_to]`; and `yahoo_pull.Pacer.done(symbol)` is TRUE forever once a symbol pulled OK, so the draw never pulls it again. A Yahoo pull
is `period="max"` (the whole history, one request), so extending a file needs only a new window end and one fresh request per symbol.
The ruling: a STANDING tier-1 request, rebuilt each trading day, carries every locked symbol to the T-1 frontier through the shared pacer, in the
existing queue (not a second pipeline); written rows that already exist stay byte-identical (`price_store.write` short-circuits an unchanged
frame). Its first run is the one-time 76-trading-day gap.

**Build** (NEW `data/mdpf/scripts/demque/extend_frontier.py`; read `price_store.py` `index`, `redraw_stale.py` `reset_pacer`, `demand_queue.py`
`validate` and `quote`, `daily_draw.py`, `run_daily_draw.sh` and `lib/trading_calendar.py` `expected_last_trading_day` first; import, do not copy):
1. `plan(root=None, today=None) -> dict`: `today` defaults to the local date. The symbols are every CUSIP `price_store.index(root)` lists
   (root defaulting to `price_store.s3_root()`) with its `yahoo_symbol`. `frontier = expected_last_trading_day(today)` (today when it is a
   trading day, else the prior one). Returns `{"request_id": "STANDING-T1-EXTEND", "frontier": ISO, "start": earliest valid_from, "end":
   frontier, "symbols": N, "cells": c, "finish_date": f, "securities": [{cusip, symbol}, ...]}` with `cells` and `finish_date` from
   `demand_queue.quote` over that request. Read only.
2. `apply(root=None, state_path=None, queue_dir=None, today=None) -> dict`: writes the plan's request as ONE file
   `Z-STANDING-T1-EXTEND.json` in `queue_dir` (tier 1, reason "C-PRICES: every locked symbol to the T-1 frontier, daily (FWD-1, FWD-8)", page
   "price store (C-PRICES, T-1 frontier)", fields `["close"]`; the name sorts after the older request files, which `daily_draw._windows`
   needs, because a later file's window wins for a CUSIP), REPLACING the previous day's file, then resets the pacer entries of exactly those symbols
   with `redraw_stale.reset_pacer` so the day's draw re-pulls each once. Returns `{"request": path, "symbols": n, "reset": m, "frontier": ISO}`.
3. CLI `--plan [--today D] [--root R]` prints the plan (without `securities`) as ONE JSON line and writes nothing; `--apply [--today D] [--root R]
   [--state PATH] [--queue DIR]` prints the apply result as ONE JSON line. `--state` and `--queue` default to the daily draw's home exactly as
   `run_daily_draw.sh` derives it (`$OPAL_DEMQUE_HOME` or `~/.opal/demque`, `pacer.json` and `queue/`), never typed.
4. `run_daily_draw.sh`: run `python data/mdpf/scripts/demque/extend_frontier.py --apply` BEFORE the draw line, in the script's own style
   (`|| { echo "ERROR: extension rc=$?"; exit 1; }`), so a failed extension fails the run loudly and a stale store is never silent.
5. `daily_draw.py`: compute `trades_through = lock.trades_through(tx)` once from the loaded transactions and pass it as `trades_through=` to the
   `lock.check` call in `on_result` (DQ-t-30 added the keyword), so a window past the trades is claimed `held`. No other change to `daily_draw.py`.
6. NEW `test_demque_extend_frontier.py` (pytest; a LOCAL store root under `tmp_path`, a pacer JSON and a queue folder in `tmp_path`, no network,
   no S3) with exactly these names:
   `test_plan_window_ends_at_the_expected_last_trading_day_and_lists_every_locked_symbol` (a Sunday gives the prior Friday; a trading Monday gives
   itself), `test_apply_resets_exactly_the_plan_symbols_and_replaces_the_standing_request_file` (other pacer symbols and `day`/`count` unchanged;
   the request passes `demand_queue.validate`; a second apply leaves ONE file) and
   `test_run_daily_draw_runs_the_extension_before_the_draw` (reads the script text: the `extend_frontier.py --apply` line precedes the
   `daily_draw.py` line).

### ACCEPTANCE

<criterion id="DQ9-t31-AC1" cell_refs="DQ-t-31"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t31_tests.py</invocation><expect>XF-OK</expect></criterion>
<criterion id="DQ9-t31-AC2" cell_refs="DQ-t-31"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t31_plan.py</invocation><expect>XPLAN-OK</expect></criterion>
`DQ9-t31-AC1` -- the three named tests. `DQ9-t31-AC2` -- `--plan` on the REAL served store (S3 read only): `--today 2026-10-12` ends 2026-10-12,
`--today 2026-10-11` ends 2026-10-09, `symbols` equals the check's own count (141), `start` the earliest `valid_from`.

<expected_criteria>DQ9-t31-AC1,DQ9-t31-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `XF-BAD no file ...`, `XPLAN-BAD no file ...extend_frontier.py`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No write to the served price store (local or S3), no write to the real pacer state or queue, no AWS write, no Bloomberg call, no Yahoo
  call, no deploy.** `--apply` is never run against the real home: it is the issuer's act, and it is HELD for the CTO's word. The S3 read in
  AC2 is the seat's existing read.
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W24-S<k>`, next free k, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/extend_frontier.py
data/mdpf/scripts/demque/test_demque_extend_frontier.py
data/mdpf/scripts/demque/run_daily_draw.sh
data/mdpf/scripts/demque/daily_draw.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-31`.
<owned_cells>DQ-t-31</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t31-AC1, DQ9-t31-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~24/MDPF_DEMQUE.TO-DQ-t31.standing-extension-to-frontier.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t31-AC1,DQ9-t31-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the two `--plan` lines verbatim, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created; the existing daily draw task (22:30 local) runs the extension first from its next run, which is HELD until the CTO releases the apply.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write by the worker; the S3 reads use the seat's existing read.
comp-adversary: DECLARED-NOT-APPLICABLE a request builder over the existing queue and pacer; the served write is the existing price_store.write.
risk: LOCAL -- code and tests. The issuer's `--apply` and the draw after it are SERVED under their own never-widen pair (CTO half: round-8 analysis R1; COO half: decomposition round 9), blast radius the 141 CUSIP prefixes, rollback per key the object's prior S3 version; HELD for the CTO's word on the one-partition premise (row D1-S11).
direct_act: false -- a worker order.
</preflight>

Source: CTO round-8 analysis @92a9b27704 R1 (a), (c); row D1-W22-S1 (REMEDIATION_v7); TO-DQ-t30; decomposition round 9.

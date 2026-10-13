# TO MDPF_DEMQUE.TO-DQ-t48 -- round 9 DQ-t-48: the Yahoo standing extension's incremental path (last 5 trading days, targeted refill on a gap or a split), proved cell-equal to the full re-pull
<to_id>MDPF_DEMQUE.TO-DQ-t48</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~40</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>INCREMENTAL</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-48` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 13) |
**outcome_ref:** C-PRICES, C-YAHOO, C-ONCE, FWD-8 | **depends_on:** DQ-t-37, DQ-t-40, DQ-t-45 (merged)

---

## WORKER FACE

### THE CELL

Andrew-direct 2026-10-13 (standing rule, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/DEMQUE_QUEUE_FORM_ANDREW_20261013.md`, "STANDING RULE"): once a need's backfill is covered, every daily
pull asks for **the last 5 trading days** (`lib/trading_calendar.py`), and a security with a gap wider than 5 trading days gets a **targeted refill** for just that gap. CTO ruling
(msg 4936): on Yahoo the same request count stands (one request per symbol); a name takes the last 5 trading days normally, and a **full re-pull of that name only when a split (or
another restatement the store keys on) lands**: the targeted refill. Prove it cell-equal to the full re-pull on a no-split day (50+ names) and on one split arm. The standing
extension today re-pulls every name's full history each day (`extend_frontier.py`, `yahoo_pull.pull`, then `lock.check` and `price_store.write`). **This cell BUILDS the
incremental path and its proof. It changes no served byte: the nightly draw is not rewired here (a later SERVED order, under its own never-widen pair, does that).**

**Build** (NEW files under `data/mdpf/scripts/demque/`; read `yahoo_pull.py` `pull` and `PullResult`, `batch_pull.py` (merged; reuse `window`, the split-factor rule and its
docstring on how NEW rows' `close_served` is computed), `price_store.py` (`index`, `write`, the file layout and `lock.json`), `extend_frontier.py` and `daily_draw.py` first; import, do not
copy):
1. **`incremental_append.py`**: `apply_incremental(stored: dict, window: PullResult, frontier) -> dict` where `stored` is `{prices, splits, dividends, lock}` frames for one name.
   - Returns `{"action": "append", prices, splits, dividends}` when the pulled window carries NO split absent from `stored.splits` and no stored-max gap: the new price rows
     (dates after the stored max, with `as_traded_close` and `close_served` computed exactly as `yahoo_pull.pull` does, from the splits dated strictly after each new row), and the
     window's dividends and splits not already stored.
   - Returns `{"action": "refill_split"}` when the window carries a split (or any `close_served`-restating action your read of `price_store` / `lock` shows the store keys on; NAME
     each in the module docstring and the report) that `stored` does not have: the caller then does the full pull for THAT name only.
   - Returns `{"action": "refill_gap", "from": date}` when the stored max is more than 5 trading days before the frontier: the caller pulls from that date, never a wider standing window.
   - Never rewrites a stored row except in the refill actions. The lock record's `valid_to` is extended to the frontier on `append` with its `claim` and `trades_through` unchanged; state in
     the docstring why that equals what a full re-lock yields on a no-split day, or name the difference in a surprise row.
2. **`incremental_plan.py --plan [--today D] [--root R]`** (read only, S3 read, NO vendor call): over the names `price_store.index` lists, print ONE JSON line
   `{"frontier", "names", "incremental", "refill_gap", "refill_split", "requests", "cells_full_repull", "cells_incremental", "window_trading_days"}`: `window_trading_days` 5;
   `incremental` = names whose stored max is within 5 trading days of the frontier; `refill_gap` = names with a wider gap; `refill_split` = names whose stored splits already carry a
   split dated inside the window; `requests` = `names` (one request per name); `cells_full_repull` = the stored rows now re-pulled each day (sum of each name's full price rows);
   `cells_incremental` = names x 5 (the rows an incremental draw writes) plus the gap rows of `refill_gap`.
3. **`incremental_equal.py --n 50 --out PATH --spot N`** (Yahoo, at most 120 symbol-requests in the whole order, a SCRATCH pacer state file with `min_gap` 1.0 and `max_gap` 2.0 for this
   proof only, said in the report; no write to any store): NO-SPLIT ARM: for 50+ stored names across at least 3 asset classes (read the class from `lock.json` or the client transactions),
   pull each name's full history ONCE, take that as the FULL result; truncate a copy of it to "stored as of 5 trading days ago" and derive the INCREMENTAL result by `apply_incremental`
   on the last-5-day slice of the SAME pull (no second request); compare prices (`date`, `as_traded_close`, `close_served`), dividends and splits cell by cell. SPLIT ARM: choose at least
   one name with a split in its history, truncate its stored copy to the trading day before that split's ex-date so the split falls inside the 5-day window, and require
   `action == "refill_split"`, then the full-pull path, then equality with the FULL result. `--spot N` runs N live names through both paths the same way and prints
   `{"equal": k, "of": N}`. `--out` writes `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~40/INCREMENTAL_EQUALITY_REPORT.json`:
   `{"no_split_arm": {"n", "asset_classes", "equal", "mismatches": []}, "split_arm": {"n", "refilled", "equal", "symbols"}, "cells_compared": {"prices", "dividends", "splits"},
   "http_requests", "restatements_named": [...]}` with the dividend and split cells compared in the no-split arm coming from windows that contain them where the data has them.
4. NEW `test_demque_incremental.py` (pytest; stub frames and a stub fetch, no network) with exactly these names:
   `test_the_window_is_the_last_five_trading_days_after_the_stored_max_and_never_wider_than_the_gap`,
   `test_a_gap_wider_than_five_days_or_a_new_split_in_the_window_is_a_targeted_refill_never_a_wider_standing_window`,
   `test_appending_the_incremental_rows_equals_the_full_repull_on_a_no_split_day`,
   `test_a_gained_split_triggers_the_full_repull_and_the_result_equals_the_full_path`.

### ACCEPTANCE

<criterion id="DQ9-t48-AC1" cell_refs="DQ-t-48"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t48_tests.py</invocation><expect>INC-OK</expect></criterion>
<criterion id="DQ9-t48-AC2" cell_refs="DQ-t-48"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t48_plan.py</invocation><expect>INCPLAN-OK</expect></criterion>
<criterion id="DQ9-t48-AC3" cell_refs="DQ-t-48"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t48_equal.py</invocation><expect>INCEQ-OK</expect></criterion>
`DQ9-t48-AC1` -- the four named tests. `DQ9-t48-AC2` -- on the REAL index: window 5, the classes sum to the names, one request per name, writes at least five times smaller. `DQ9-t48-AC3` -- the
equality report (50+ no-split names all equal, the split arm refilled and equal, dividends and splits compared) and a live 5-symbol spot equal 5 of 5. Report the whole folder
`pytest data/mdpf/scripts/demque` once (the count at the t-47 merge, plus these 4).

<expected_criteria>DQ9-t48-AC1,DQ9-t48-AC2,DQ9-t48-AC3</expected_criteria>

Run each invocation from the worktree root. At the base: `INC-BAD no file ...`; `INCPLAN-BAD no file ...incremental_plan.py`; `INCEQ-BAD no file ...INCREMENTAL_EQUALITY_REPORT.json`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No write to the served store, the real pacer state, the queue or the ledger; no Bloomberg call; no AWS write; no deploy; no timer.** Yahoo is read through the library only, under a scratch
  pacer, at most 120 symbol-requests across the whole order, one proof run (the 22:30 ET draw uses the shared pacer separately; do not touch `~/.opal/demque/pacer.json`).
  `daily_draw.py`, `extend_frontier.py --apply` and `run_daily_draw.sh` are NEVER run, and neither of those files nor `price_store.py` or `lock.py` is edited.
- **Account ids never enter a committed file.**
- **Refusal clause.** If a criterion cannot be met as written (a mismatch is a FINDING: never fix it by editing the comparison), stop, write the reason in your report and a surprise row
  (id `MDPF_DEMQUE-D1-W40-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file below. Rows are APPEND-ONLY. Merge
  `box/dell1` into your branch (a merge, never a rebase) before you append rows.

<paths>
data/mdpf/scripts/demque/incremental_append.py
data/mdpf/scripts/demque/incremental_plan.py
data/mdpf/scripts/demque/incremental_equal.py
data/mdpf/scripts/demque/test_demque_incremental.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-48`.
<owned_cells>DQ-t-48</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t48-AC1, DQ9-t48-AC2, DQ9-t48-AC3. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~40/MDPF_DEMQUE.TO-DQ-t48.incremental-last-five-days-with-targeted-refill.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t48-AC1,DQ9-t48-AC2,DQ9-t48-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the `--plan` line verbatim, the report's key numbers, the restatements you named and why, any difference in the lock record between the two
paths, the number of Yahoo requests used, the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed; wiring is a later order.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write.
comp-adversary: DECLARED-NOT-APPLICABLE a library, a read-only plan and an equality proof against a scratch copy; no served write.
risk: LOCAL -- code, tests and a proof. Its later wiring changes what the nightly draw writes to a served store: SERVED, under its own never-widen pair (CTO msg 4936).
direct_act: false -- a worker order.
</preflight>

Source: Andrew-direct 2026-10-13 (standing rule, form @e961fee72f); CTO msgs 4931, 4936; TO-DQ-t40 EQUALITY_REPORT; decomposition round 9.

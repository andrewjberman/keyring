# TO MDPF_DEMQUE.TO-DQ-t77 -- DQ-t-77: the late-day sweep: at 16:00 ET the drawer spends what is left of the 2.5M daily total on backfill, surface lines waived (Andrew-direct 2026-10-19)
<to_id>MDPF_DEMQUE.TO-DQ-t77</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~67</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-19</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>SWEEP</workstream>
**AMENDED by the issuer 2.0.0_SA_COO~Q1, 2026-10-19 ~17:2xZ (worker rows MDPF_DEMQUE-D1-W67-S1 to S4):** (S1, an issuer defect) the `pass` member is written by `bbg_quote.record_actual`, which the first `<paths>` did not grant: `data/mdpf/scripts/demque/bbg_quote.py` is now GRANTED for exactly one change, an optional keyword `pass_=None` on `record_actual` (the member `"pass"` written only when not None, as the `surface` keyword already does); nothing else in that file moves. (S2, ruled) the sweep is ONE pool: the reference channel's held ceiling (52) is waived in the sweep exactly like the history ceiling, so reference requests draw from `daily_total_left` too. (S3) accepted: listing `bbgtml-unmetered` in `unconverted_modes` is true (the terminal agent's spend is unmetered). (S4) accepted: an absent `daily_total` fails closed with `NO_ALLOWANCE`. Criteria unchanged.
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-77` (`decompositions/MDPF_DEMQUE_DECOMP.md`, amendment 38) |
**outcome_ref:** C-PRICES, C-RESERVE | **depends_on:** DQ-t-69, DQ-t-74, DQ-t-75, DQ-t-76 (merged)

---

## WORKER FACE

### THE CELL

Andrew ruled (record `org/tier1_exec/2.0.0_SA_COO~Q1/deliverables/ANDREW_DIRECT_20261019_16xxZ_LATE_DAY_SWEEP_OF_UNUSED_QUOTA.md`): **at 16:00 US Eastern, every day, trading days included, whatever is left of the 2,500,000-cell daily total after every cell drawn that day is drawn by the backfill queue, the per-surface lines waived for that pass only.** Today the standing drawer (`data/mdpf/scripts/demque/standing_drawer.py`) runs once a day, at 14:00Z, on non-trading days only, and a weekday's unused quota is lost. **This cell adds the SWEEP pass to the drawer.** Its schedule at site Z is a separate cell (`DQ-t-78`); you register nothing.

**THE SWEEP (implement exactly this):**
1. **Entry:** `run(day, client, ..., sweep=True)` and the CLI `--apply --sweep`. The default pass (`sweep=False`) is unchanged in every respect.
2. **Any day:** the sweep does NOT apply the trading-day gate (it draws on trading days too).
3. **One sweep a day:** its own marker `run.<day>.sweep.started.json`, written before the first draw and never removed, beside (not replacing) the default pass's `run.<day>.started.json`. A second sweep on the same day stops with `ALREADY_RAN_TODAY`.
4. **Room, one pool:** `daily_total_left = budgets.daily_total.value - spent_today`, never below 0, where `spent_today` counts each cell ONCE:
   - the production budget ledger for that UTC day (`bbg_budget_<day>.jsonl` in `bbg_budget.ledger_dir()`, read with `bbg_ledger_upload.rows_for_day`), EXCLUDING the drawer's own modes `demque-backfill` and `demque-backfill-reference` (those cells are already in the actuals ledger); a row whose `cells` is None counts its `rows` as a floor, and its mode is listed in the result as `unconverted_modes`;
   - plus every `cells_drawn` of the actuals ledger dated that day (history and reference, every job, both passes).
   - If that day's budget ledger file is ABSENT or unreadable, the sweep has room 0 and stops with `PRODUCTION_SPEND_UNREAD` (fail closed: production's spend is unknown). An existing EMPTY file is a valid read of 0.
5. **Waived in the sweep only:** the per-surface rooms (A to E), the untagged history ceiling plus carry-over, and the reference channel's ceiling (amendment S2). Each drawable request draws up to `min(its remaining, daily_total_left)` in the order `open_requests` already gives; subtract each draw from `daily_total_left`.
6. **Kept in the sweep:** `draw_hold` (held requests are not drawable, as today); the tier floor; the probe rules (DQ-t-76); the empty-window cooldown and its stop (DQ-t-75); the outcome per request (DQ-t-74); the stop on any vendor limit, refusal or diagnostic.
7. **Separate outputs:** the sweep writes `receipt.<day>.sweep.json`, `history-<day>.sweep.parquet` and `reference-<day>.sweep.parquet` (never overwriting the default pass's files); its actuals rows carry `"pass": "sweep"` (the default pass's rows carry no `pass` member, unchanged). The receipt and result carry `"pass": "sweep"`, `daily_total_left` at the start, `spent_today` as `{"production": n, "drawer": n}`, and `unconverted_modes`.
8. **Read-only views:** `--room --sweep --day D [--actuals PATH]` prints ONE JSON line `{"day", "pass": "sweep", "trading_day", "daily_total_left", "spent_today", "unconverted_modes"}`, plus `"reason": "PRODUCTION_SPEND_UNREAD"` and `daily_total_left` 0 when the day's budget ledger is absent; it writes nothing and calls nothing. `--task-name --sweep` prints the builder's name `name(lookup('mdpf')['short'], None, 'demque-sweep', 'daily')` (= `mdpf-demque-sweep-daily`; never typed). The existing `--task-name` and `--room` are unchanged.

Read first, in full: `standing_drawer.py` (module docstring, `task_name`, `_drawn_history_today`, `carry_over`, `open_requests`, `run`, `main`, and the helpers of DQ-t-69/74/75/76), `bbg_ledger_upload.rows_for_day`, `data/etfs/scripts/rivalfunds/bbg_budget.py` (`ledger_dir`, `ENV_DIR`), and the fixtures of `test_demque_surface_room.py`, `test_demque_empty_window.py` and `test_demque_probe_empty.py` (stub client, `tmp_path`, `RIVALFUNDS_BBG_BUDGET_DIR` and `OPAL_DEMQUE_HOME` set to `tmp_path`).

**Build**
1. The sweep in `standing_drawer.py` (a short module-docstring paragraph and a comment naming this cell).
2. NEW `data/mdpf/scripts/demque/test_demque_sweep.py` (pytest, `tmp_path`, stub client, no network) with EXACTLY these names:
   - `test_the_sweep_draws_on_a_trading_day_up_to_the_daily_total_left` -- a Monday fixture (2026-10-19), an empty budget ledger file for the day, a temp allowance with `daily_total` 20000: the sweep draws, its cells equal `min(remaining, 20000)`, the actuals rows carry `"pass": "sweep"`; the default pass on the same Monday still stops `TRADING_DAY`.
   - `test_the_sweep_ignores_surface_lines_and_the_untagged_ceiling` -- a request tagged C with a C line of 1000 and an untagged request, daily_total 20000: the sweep draws past 1000 for the C request and past 5858 in all.
   - `test_the_sweep_counts_production_and_the_morning_fire_once_each` -- a budget ledger with 3000 production rows (a non-drawer mode, converted) and 2000 rows in mode `demque-backfill`, plus actuals rows of 2000 cells dated that day: `spent_today` is production 3000 (times the conversion) and drawer 2000, and the drawer's cells are not counted twice.
   - `test_an_unreadable_production_ledger_gives_the_sweep_no_room` -- no budget file for the day: the sweep stops `PRODUCTION_SPEND_UNREAD`, draws nothing, makes no vendor call.
   - `test_the_sweep_runs_once_a_day_and_never_draws_a_held_request` -- a second sweep the same day stops `ALREADY_RAN_TODAY`; a request carrying `draw_hold` is never drawn by the sweep.
   Edit an existing test ONLY if it fails because it pins an exact key set the sweep extends; name each edit and why. Run the whole `data/mdpf/scripts/demque` folder once at the end: no failure that was not failing at the base (known base failures: 4 failed and 8 collection errors from the missing `integrations/` and `commonwealth_signs`; report the counts).
3. **Report** the files, the three criteria's output, every edited existing test and why, the folder count, commits (never an account number).

### ACCEPTANCE

<criterion id="DQ9-t77-AC1" cell_refs="DQ-t-77"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t77_tests.py</invocation><expect>SWEEP-OK</expect></criterion>
<criterion id="DQ9-t77-AC2" cell_refs="DQ-t-77"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t77_room.py</invocation><expect>SWEEP-OK</expect></criterion>
<criterion id="DQ9-t77-AC3" cell_refs="DQ-t-77"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t77_regress.py</invocation><expect>SWEEP-OK</expect></criterion>

<expected_criteria>DQ9-t77-AC1,DQ9-t77-AC2,DQ9-t77-AC3</expected_criteria>

`DQ9-t77-AC1` -- the five named tests. `DQ9-t77-AC2` -- the drawer's own sweep read on the real allowance file: the built task name, a Monday with an empty ledger reads daily_total_left 2,500,000, and a Monday with no ledger reads 0 with `PRODUCTION_SPEND_UNREAD`. `DQ9-t77-AC3` -- the DIFFERENCE CONTROL: the drawer's existing tests and the DQ-t-69/74/75/76 tests pass unedited. Run each from the worktree root. At the base: `SWEEP-BAD no file ...test_demque_sweep.py`; `SWEEP-BAD RuntimeError: standing_drawer --task-name --sweep rc=2 ...`; AC3 reads `SWEEP-OK` (a control that must keep passing).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **NO vendor call, no write to S3, any ledger under `org/` or `~/.opal`, the queue state, the price store or any pacer state; run no draw (`--apply` is not run); register no task.** Tests write only under `tmp_path`. Change no request file, no allowance value, no quote file. Do not merge anything; the issuer drains. Never print an account number. Build no alarm, monitor or notification.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W67-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended at the end of your own branch's copy of the investigation file below. Do NOT merge `box/dell1`.

<paths>
data/mdpf/scripts/demque/standing_drawer.py
data/mdpf/scripts/demque/bbg_quote.py
data/mdpf/scripts/demque/test_demque_sweep.py
data/mdpf/scripts/demque/test_demque_*.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9, amendment 38), cell `DQ-t-77`.
<owned_cells>DQ-t-77</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t77-AC1, DQ9-t77-AC2, DQ9-t77-AC3. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~67/MDPF_DEMQUE.TO-DQ-t77.late-day-sweep.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t77-AC1,DQ9-t77-AC2,DQ9-t77-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, the three checks' output, every edited existing test and why, the folder count, commits (never an account number).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell registers no schedule; the 16:00 ET task is DQ-t-78 at site Z.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE code graded by tests, a read-only real-file view and an unedited-suite control.
risk: LOCAL -- code and tests on dell1; nothing draws until DQ-t-78 registers the task at site Z (WORLD, its own order).
direct_act: true -- one cell, about 150 changed lines plus a test file.
</preflight>

Source: Andrew-direct 2026-10-19 ~16:2xZ (record above, @19bcfdb913): "Yes, go ahead" to a 16:00 ET daily sweep, every day, 2.5M total kept, surface lines waived for that pass only. It supersedes for the sweep pass the trading-day gate of `ledger/CTO_RULING_DRAWER_HONOURS_SURFACE_BUDGETS_20261017.md`; the CTO is told (msg to `1.0.0_SA_CTO~DELL1`, 2026-10-19 16:30Z).

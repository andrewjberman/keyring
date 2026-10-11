# TO MDPF_DEMQUE.TO-DQ-t27 -- round 8 DQ-t-27: the STANDING non-trading-day history drawer at site Z
<to_id>MDPF_DEMQUE.TO-DQ-t27</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.7.0_AE_CloudOps~ZQ</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
**Directive:** D8 | **Fabric:** dell1 (placement site Z) | **Decomp cell:** `DQ-t-27` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 8 -- CUT) |
**outcome_ref:** FWD-3 | **depends_on:** DQ-t-26 (and DQ-t-25 under it)

---

## WORKER FACE

### THE CELL

`DQ-t-27` (FWD-3, FWD-4; CTO round-7 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round7.md` R2, read it; row
`MDPF_DEMQUE-D1-C-S17`). Your own DQ-t-24 drew 5,858 of the 15,720-cell TR request on Saturday 2026-10-10 and its one-shot task was removed, so
9,862 cells stay open with nothing scheduled. R2 rules a STANDING drawer: a scheduled drawer runs on every non-trading day at site Z, draws open
backfill requests in rank order up to the measured ceiling (5,858 a day, `data/mdpf/scripts/demque/bbg_allowance.json` `history.ceiling`,
claim `measured`), stops on a vendor limit warning or a refused request, and writes the receipt and the `BBG_ACTUALS.jsonl` line t24 wrote. It
is a production schedule, not a one-shot, and it is the queue's existing draw step on its own clock, not a second pipeline. The remaining 9,862
cells draw on its first two scheduled non-trading days: 5,858, then 4,004. **Start only after DQ-t-26's commit is in your tree**
(`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R8_CHECKS/dq_t26_real.py` prints REFRZ-OK there; `drawer_schedule.py` exists).

**Build** (under `data/mdpf/scripts/demque/`):
1. NEW `standing_drawer.py`, with these CLI forms:
   - `--schedule --from YYYY-MM-DD --days N`: one JSON line `{"fires": [...]}` from `drawer_schedule.fire_days` (the non-trading days of the window).
   - `--task-name`: prints the standing task's Windows name from `lib/opal_naming.py` `name()`. If the builder REFUSES, that is a missing registry
     row: stop with a BLOCKING surprise row; never hand-type a name.
   - `--apply [--day YYYY-MM-DD] [--output DIR] [--actuals PATH]`: one run. `--day` defaults to the real local date. `--output` defaults to
     `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_STANDING/`; `--actuals` to
     `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/BBG_ACTUALS.jsonl`. Prints the result as one JSON line.
2. The run (`run(day, client, requests_dir, actuals_path, output_dir)`; tests inject a stub client with `historical_data`):
   - **A trading day** (`lib/trading_calendar.py`): no sign-in, no vendor call, no actuals line; the result is `{"outcome": "STOPPED",
     "stop_reason": "TRADING_DAY", "cells_drawn": 0}` and the process exits 0.
   - **One run per day:** a marker `run.<day>.started.json` in `--output`, written before the first draw, never removed by the code; a second run
     that day returns `STOPPED` / `ALREADY_RAN_TODAY` and draws nothing.
   - **Open requests:** every `*.json` in `org/missions/D8/MDPF/MDPF_DEMQUE/requests/` that is not a `*.quote.json` / `*.quote.superseded-*.json`
     and has channel `history`, an int `tier` >= 2, vendor bloomberg (or none) and securities carrying `bloomberg` tickers, whose cells drawn
     so far (the sum of `cells_drawn` over the actuals lines with `job` = its `request_id`) are fewer than its quoted cells. Order them as
     `demand_queue.py` orders requests (tier, rank, file order; read it and reuse it).
   - **The day's room** = the ceiling `bbg_quote.quote(...)["allowance_today"]` gives, counting every history cell already drawn that day by any
     job (never above the ceiling across requests). Draw `min(room left, the request's remaining cells)` per request, in order.
   - **Resume, never repeat:** the draw continues where earlier runs stopped. Rows already stored (the parquet files `history-*.parquet` in
     `--output` and in `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_T24/`) are never drawn again: per security the next
     window starts the day after its latest stored date, and a security whose window is exhausted is skipped.
   - **Stops:** the first vendor diagnostic, refusal, missing/duplicate/out-of-window row or empty response stops ALL drawing, records the stop
     (`outcome` STOPPED with its reason), and never retries. Reuse `bbg_backfill.py`'s chunk loop, diagnostics, `bbg_budget.record(mode=
     "demque-backfill", ...)` and `SiteClient` sign-in (`integrations/bloomberg/READ_HERE.md`'s budgeted sign-in; no new auth path). You may
     refactor `bbg_backfill.py` into a reusable draw function; its three existing tests keep passing unedited in meaning.
   - **Records:** a receipt `receipt.<day>.json` in `--output`, the fetched rows as `history-<day>.parquet`, and ONE actuals line per request
     drawn through `bbg_quote.record_actual` (drawer `0.7.0_AE_CloudOps~ZQ`, outcome `DRAWN` or the stop).
3. NEW `test_demque_standing_drawer.py` (pytest; stub client, `tmp_path`, no network, no Terminal) with exactly these names:
   `test_drawer_schedule_is_one_fire_per_non_trading_day_for_the_horizon` (14 days from Monday 2026-10-12 give 10-17, 10-18, 10-24, 10-25),
   `test_drawer_draws_min_of_allowance_and_remaining_in_rank_order` (two open requests in tier order; day 1 draws the ceiling and stops; day 2
   resumes with no (security, date) drawn twice and the last request's draw capped at its remaining cells) and
   `test_drawer_on_a_trading_day_draws_nothing` (no client call, no actuals line, exit 0).
4. **The site-Z act (a pair; `1.0.0_SA_CTO~Z` signs the site-Z half, the CTO half is the round-7 analysis R2 @f5553ca3d5):** register ONE standing
   Windows task (the `--task-name` name), a DAILY trigger at a time after the Bloomberg Terminal's sign-in window, action
   `python data/mdpf/scripts/demque/standing_drawer.py --apply` from the repository root. Read `comp-schedule` for site Z first. Do it inside a
   change-management entry opened at the start and closed at completion (the open sentinel committed). The task runs every day and the code does
   nothing on a trading day, because the Windows scheduler carries no NYSE calendar. Rollback: `schtasks /Delete` for that name and close the
   entry SUPERSEDED. Blast radius: Bloomberg history draws of at most the measured ceiling per non-trading day, for tier >= 2 history requests
   in the mission requests folder only; writes are the actuals ledger append, the uploader's existing daily ledger object, and the output folder.

### ACCEPTANCE

<criterion id="DQ8-t27-AC1" cell_refs="DQ-t-27"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R8_CHECKS/dq_t27_tests.py</invocation><expect>DRW-OK</expect></criterion>
<criterion id="DQ8-t27-AC2" cell_refs="DQ-t-27"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R8_CHECKS/dq_t27_sched.py</invocation><expect>DRSCH-OK</expect></criterion>
<criterion id="DQ8-t27-AC3" cell_refs="DQ-t-27"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R8_CHECKS/dq_t27_fire.py</invocation><expect>FIRE-OK</expect></criterion>
`DQ8-t27-AC1` -- the three named tests. `DQ8-t27-AC2` -- at site Z after the registration: the schedule prints exactly the four non-trading days of
2026-10-12..2026-10-25, the task is registered, and a trading day (2026-10-12, scratch output and actuals) draws 0. `DQ8-t27-AC3` -- the first
scheduled fire on a non-trading day after 2026-10-10 drew its day share, `min(5,858, 15,720 minus the cells already drawn)`, outcome DRAWN.
AC3 is date-gated: it cannot read before the next non-trading day the drawer exists on (2026-10-17 at the latest); the order stays open until
it reads FIRE-OK. A history draw is barred on trading days (round-6 R1), so its positive arm has no on-demand act.

<expected_criteria>DQ8-t27-AC1,DQ8-t27-AC2,DQ8-t27-AC3</expected_criteria>

Run each invocation from the repository root at site Z. At the base: `DRW-BAD no file ...`, `DRSCH-BAD no file ...standing_drawer.py`,
`FIRE-BAD no scheduled fire row after 2026-10-10`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **Bloomberg draws only through the standing drawer, only on non-trading days, only inside the quoted day room;** stop on any limit warning or
  refusal; no manual draw beyond the scheduled fires; no notebook, producer or auth path is changed. No S3 write beyond the uploader's existing
  daily ledger object.
- **You arm no timer, background task or OS task** except the one standing task named in build item 4.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-Z-W2-S<k>`, `fabric` `site-z`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/standing_drawer.py
data/mdpf/scripts/demque/test_demque_standing_drawer.py
data/mdpf/scripts/demque/bbg_backfill.py
data/mdpf/scripts/demque/test_demque_bbg_backfill.py
org/missions/D8/MDPF/MDPF_DEMQUE/ledger/BBG_ACTUALS.jsonl
org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_STANDING/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 8), cell `DQ-t-27`.
<owned_cells>DQ-t-27</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ8-t27-AC1, DQ8-t27-AC2, DQ8-t27-AC3. Instance at `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE.TO-DQ-t27.sitez-standing-nontrading-drawer.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ8-t27-AC1,DQ8-t27-AC2,DQ8-t27-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the registered task name and trigger, the schedule print, the first fire's drawn count against its
day share, any stop, the change-management entry, commits and push state.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE at the cut: the seat reads comp-schedule at site Z before registering the one standing task (build item 4).
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the uploader's existing PutObject is unchanged.
comp-adversary: DECLARED-NOT-APPLICABLE a standing budgeted Bloomberg draw inside its measured ceiling, stopping on any vendor warning; reviewed under the site-Z half.
risk: WORLD -- a standing Bloomberg history draw at site Z through the queue, under a pair (CTO~Z signs the site-Z half).
direct_act: false -- a seat order to the site-Z per-project lane.
</preflight>

Source: CTO round-7 analysis @f5553ca3d5 R2; row D1-C-S17 (REMEDIATION_v6); TO-DQ-t24 (the one-shot this standing drawer replaces); decomposition
round 8. Codex lanes run this mission-tree order directly (site Z AGENTS.md @a55888e3a2).

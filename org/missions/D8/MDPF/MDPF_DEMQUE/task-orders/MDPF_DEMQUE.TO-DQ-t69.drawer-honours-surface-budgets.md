# TO MDPF_DEMQUE.TO-DQ-t69 -- DQ-t-69: the quote and the standing drawer honour the surface budgets Andrew set on 2026-10-16 (surface C is 400,000 a day)
<to_id>MDPF_DEMQUE.TO-DQ-t69</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~64</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>SURFROOM</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-69` (`decompositions/MDPF_DEMQUE_DECOMP.md`, amendment 33) |
**outcome_ref:** C-PRICES, C-RESERVE | **depends_on:** DQ-t-73 (merged: the `budgets` block and the `surface` tag on every request)

---

## WORKER FACE

### THE CELL

Andrew set a daily Bloomberg budget of 2,500,000 cells on 2026-10-16 with a line per surface (A 350,000, B 1,500,000, C 400,000, D 100,000, E 150,000), and DQ-t-73 wrote it into `data/mdpf/scripts/demque/bbg_allowance.json` under the top-level key `budgets` and tagged every Bloomberg request file with `"surface": "<A..E>"`. **Nothing reads the budget yet.** Today the quote and the drawer give every history request the one `history.ceiling` (5,858 cells a fire). The CTO ruled (`org/missions/D8/MDPF/MDPF_DEMQUE/ledger/CTO_RULING_DRAWER_HONOURS_SURFACE_BUDGETS_20261017.md`): a request tagged with a surface draws against ITS SURFACE'S budget; an untagged request keeps the history ceiling; no limit value changes.

**This cell makes the quote and the standing drawer read `budgets`.** The trading-day gate (`standing_drawer.run`, `if is_trading_day(day): return {... "TRADING_DAY" ...}`) is NOT touched: a trading-day fire still draws nothing. You change no value in `bbg_allowance.json` and no request file. You make no vendor call and run no draw.

Read first, in full: `data/mdpf/scripts/demque/bbg_quote.py` (the module docstring, `_finish_non_trading`, `_history_backfill`, `quote`, `record_actual`), `data/mdpf/scripts/demque/standing_drawer.py` (the module docstring, `_drawn_history_today`, `carry_over`, `_history_ceiling`, `open_requests`, `run`, `main`), `data/mdpf/scripts/demque/bbg_allowance.json` (`budgets`), and the fixtures of `data/mdpf/scripts/demque/test_demque_standing_drawer.py` (a stub client, `tmp_path`, a monkeypatched budget directory and priority gate; copy that shape).

**THE RULE (implement exactly this):**
- A request is SURFACE-TAGGED when its `surface` is one of `A B C D E` AND `budgets.surfaces.<S>.value` in the allowance is an int. Any other request (no `surface`, another value, or no int budget) is UNTAGGED and behaves exactly as today. A tier-1 request is unchanged.
- **Quote (`bbg_quote.py`).** Add `surface_budget(allowance, surface) -> (value or None, claim or None)`. `quote(...)` gains a keyword `drawn_surface_today=0`. For a surface-tagged, non-tier-1 history request, the backfill walk uses the SURFACE value in place of `history.ceiling`: `allowance_today = max(value - drawn_surface_today, 0)` on a fire day (`drawer_schedule.is_fire_day`, every non-trading day) and 0 otherwise; each later fire day adds the full value; `finish_date` is the first fire day by which the cumulative room covers `cells_remaining` (reuse `_finish_non_trading`). The held claim of the surface travels: `finish_date_claim` = the surface's claim (`held`), `claims` gains `"surface": "<S>"` and `"surface_budget": "<claim>"`, and `basis` names `budgets.surfaces.<S>` and says the ceiling is replaced by the surface budget. The ceiling's own `measured` check does not gate a tagged request. Every other key of the quote is as today.
- **Room in the drawer (`standing_drawer.py`).** For a surface S the day's room is `max(budgets.surfaces.S.value - S_drawn_today, 0)`, where `S_drawn_today` is the sum of `cells_drawn` over the actuals ledger rows of that `date` on channel `history` whose request is tagged S. A row's surface is its own `"surface"` member when present, else the `surface` of the request file `<job>.json` in the requests folder, else untagged. New actuals rows for a tagged request carry `"surface": "<S>"` (add an optional keyword `surface=None` to `record_actual`; the member is written only when not None; nothing else in a row changes). The untagged room stays `ceiling + carry-over - cells drawn today by untagged jobs`. Today `_drawn_history_today` sums every history cell drawn that day by any job (and the production budget ledger); keep that meaning for production's cells, but leave out of the figure the actuals-ledger cells of surface-tagged jobs, so a surface draw never shrinks the untagged ceiling.
- **The daily total.** `daily_total_left = budgets.daily_total.value - (every history and reference cell drawn today by any job, from the actuals ledger)`. Each request draws at most `min(its pool left, daily_total_left)`; after a draw subtract the cells from BOTH its pool and `daily_total_left`. Requests are drawn in the order `open_requests` already gives (rank order). When `budgets.daily_total` is absent, no total applies.
- **Carry-over (DQ-t-54) applies to the untagged pool only.**
- **Receipts.** The run marker JSON and the result gain `"surface_rooms": {"A": n, ...}` (the room each of the five surfaces had at the start) and `"daily_total_left": n`. The stop test `not room and not ref_room` must count a surface room, so a day with only a surface room is NOT `NO_ALLOWANCE`.
- **`--room` (read only).** `python data/mdpf/scripts/demque/standing_drawer.py --room --day D [--actuals PATH]` prints ONE JSON line: `{"day": "<D>", "trading_day": <bool>, "untagged": <int>, "surfaces": {"A": n, "B": n, "C": n, "D": n, "E": n}, "daily_total_left": <int>}`. On a trading day `trading_day` is true and `untagged` and every surface are 0; on a non-trading day `untagged` is the untagged room (history ceiling plus carry-over, less the untagged cells drawn today), each surface is its room, and `daily_total_left` is as above. It writes nothing, calls nothing, and reads the budget directory exactly as `carry_over` does.

**Build**
1. `bbg_quote.py`: `surface_budget`, the `drawn_surface_today` keyword and the tagged walk; `record_actual(..., surface=None)`. The module docstring gains a short paragraph for the rule.
2. `standing_drawer.py`: the surface rooms, the daily total, the per-request pool in the draw loop, the receipt fields, the `surface` member on new actuals rows, and `--room`. Its module docstring gains a short paragraph.
3. NEW `data/mdpf/scripts/demque/test_demque_surface_room.py` (pytest, `tmp_path`, stub client, no network, no Terminal; monkeypatch `bbg_quote.ALLOWANCE_PATH` to a temp copy when a test needs other figures) with EXACTLY these test names:
   - `test_a_surface_c_request_quotes_the_surface_budget_less_what_surface_c_drew_today` -- on the real allowance, a history request tagged C quotes `allowance_today` 400000 with nothing drawn and `400000 - n` with `drawn_surface_today=n`; a request of 400,000 cells or fewer finishes on the first fire day; the quote carries `claims["surface"] == "C"`.
   - `test_an_untagged_request_still_quotes_the_history_ceiling` -- the same request without `surface` quotes 5858; a tier-1 request tagged C quotes as a tier-1 request (unchanged); a request tagged `Z` is untagged.
   - `test_the_drawer_draws_a_surface_c_request_past_the_history_ceiling_on_a_non_trading_day` -- a Saturday fixture (2026-10-17), a surface-C request large enough to need more than 5,858 cells; the run's cells drawn for it exceed 5,858 and equal `min(remaining, 400000)`; the actuals row carries `"surface": "C"`; a second tagged-C request in the same site then reads a room of `400000` less what the first drew.
   - `test_surface_cells_never_exceed_the_daily_total_and_each_surface_has_its_own_room` -- on a temp allowance with `daily_total` 15000 and surfaces C and B at 10000 each, two requests (one C, one B) each larger than 10000 cells: the run draws at most 15000 cells in all, C is capped at 10000, B takes the 5000 left; an untagged request on the same site still draws at most its 5858 ceiling and the surface draws do not shrink it.
   - `test_a_trading_day_still_draws_nothing_for_a_surface_tagged_request` -- a Monday fixture: `stop_reason == "TRADING_DAY"`, `cells_drawn == 0`.
   Edit an existing test ONLY if it fails because it pins the old rule for a request that now carries a surface or pins the exact key set of a receipt or an actuals row; name each edit and why in your report. Run the whole `data/mdpf/scripts/demque` folder once at the end: no failure that was not failing at the base (a base failure on a missing `integrations/` folder is known; report it by name).
4. **Report** the files, the three criteria's output, every edited existing test and why, the folder pytest count, and commits (never an account number).

### ACCEPTANCE

<criterion id="DQ9-t69-AC1" cell_refs="DQ-t-69"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t69_tests.py</invocation><expect>SURF-OK</expect></criterion>
<criterion id="DQ9-t69-AC2" cell_refs="DQ-t-69"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t69_real.py</invocation><expect>SURF-OK</expect></criterion>
<criterion id="DQ9-t69-AC3" cell_refs="DQ-t-69"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t69_room.py</invocation><expect>SURF-OK</expect></criterion>

<expected_criteria>DQ9-t69-AC1,DQ9-t69-AC2,DQ9-t69-AC3</expected_criteria>

`DQ9-t69-AC1` -- the five named tests. `DQ9-t69-AC2` -- the real allowance file and the real surface-C request ETFS_RIVALS-C1-CLOSE-OWED-REST-20261017 through the real `bbg_quote.py` CLI: 400000 a fire and a finish on 2026-10-17; the same request without its tag quotes 5858 (the difference control). `DQ9-t69-AC3` -- the drawer's own `--room` on the real allowance and the real requests folder: Saturday 2026-10-17 reads untagged 5858, the five surface budgets, daily total left 2500000; Monday 2026-10-19 reads trading day with every room 0. Run each invocation from the worktree root. At the base: `SURF-BAD no file ...test_demque_surface_room.py`; `SURF-BAD surface-C request allowance_today is 5858, not 400000`; `SURF-BAD standing_drawer --room rc=2 ... unrecognized arguments: --room`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **NO vendor call, no write to S3, any ledger under `org/` or `~/.opal`, the queue state, the price store or any pacer state; run no draw (`--apply` is not run); do not run `bbg_quote.py --record`.** Change no value in `bbg_allowance.json`, no request file, no quote file, and do not touch the `TRADING_DAY` gate. Do not merge anything; the issuer drains. Never print an account number. Build no alarm, monitor or notification.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W64-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended at the end of your own branch's copy of the investigation file below. Do NOT merge `box/dell1`.

<paths>
data/mdpf/scripts/demque/bbg_quote.py
data/mdpf/scripts/demque/standing_drawer.py
data/mdpf/scripts/demque/test_demque_surface_room.py
data/mdpf/scripts/demque/test_demque_*.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9, amendment 33), cell `DQ-t-69`.
<owned_cells>DQ-t-69</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t69-AC1, DQ9-t69-AC2, DQ9-t69-AC3. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~64/MDPF_DEMQUE.TO-DQ-t69.drawer-honours-surface-budgets.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t69-AC1,DQ9-t69-AC2,DQ9-t69-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, the three checks' output, every edited existing test and why, the folder count, commits (never an account number).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed (the site Z task already fires daily).
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE code graded by tests, a real-file quote and a read-only room read.
risk: LOCAL -- code and tests on dell1; the change reaches site Z only when it reaches CLOUD and the site Z checkout pulls it (DQ-t-70 reads that).
direct_act: true -- one cell, about 250 changed lines.
</preflight>

Source: Andrew-direct 2026-10-16 ~15:5xZ (record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261016_155xZ_BBG_DAILY_BUDGET_2_5M_AND_TERMINAL_AGENT_MAY_DOWNLOAD.md` @f50271705e, "round-10 cells DQ-t-69 and DQ-t-70") and 2026-10-17 ~03:1xZ / ~03:4xZ (rival funds backfill done through DEMQUE, no limit change); CTO ruling `ledger/CTO_RULING_DRAWER_HONOURS_SURFACE_BUDGETS_20261017.md` @d4ad590946 (`1.0.0_SA_CTO~DELL1`). The ruling names the cells round 10; they are cut inside the open round 9 as amendment 33 because round 9's L10 waits on the 2026-10-17 fire of `TO-DQ-t34`; the ids are the ruling's.

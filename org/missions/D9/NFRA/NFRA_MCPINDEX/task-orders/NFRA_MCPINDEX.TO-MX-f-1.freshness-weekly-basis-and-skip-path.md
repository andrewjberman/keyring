# NFRA_MCPINDEX task order -- `MX-f-1` -- Z-S74: name the gold chain's freshness skip path, and grade the two weekly BD tables on a weekly trading-day basis

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-f-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-f-1</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~25</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule change; one past scheduled run's log is READ.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS change.
comp-adversary: DECLARED-NOT-APPLICABLE -- a read plus a reader rule proven by offline fixtures with both arms; the dispatch's blocking behaviour is unchanged by ruling.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (log reads).
</preflight>

## 1. THE CELL -- `MX-f-1` (round 7; `ROUND_ANALYSIS.round6.md` @361b186c92 section 3a row Z-S74, section 5 item 2)

**The CTO's ruling (Z-S74):**
1. `allocations` and `unrealized` are weekly producers, so their entries take `freshness_basis: trading-day-frontier`
   at a WEEKLY cadence: stale only when the last write predates the most recent scheduled weekly production day per
   `lib/trading_calendar.py`. Daily tables keep their basis.
2. The skip path is MEASURED, not changed: name which of the three paths production takes (PATH, bypass flag, or bd
   config skipped), with the code line and one scheduled run's log.
3. No change to whether the gate blocks this round.

**Measured at the round-7 base:**
- The gate: `data/black_diamond/scripts/gold/gold_dispatch.sh:1346-1376`. The issuer's read is that the scheduled path
  (EventBridge `bd-gold-nightly-fallback` cron(0 23 ? * MON-SAT *) and `bd-canonical-prices-daily` -> `bd-gold-trigger`
  -> EC2 `run-gold-layer.sh` -> `run_gold_layer.sh incremental` -> `gold_dispatch.sh --chain full`) takes the
  "comp-freshness not on PATH" skip, because nothing installs `comp-freshness` on the gold EC2. Prove or disprove that
  from a scheduled run's own log line; do not assume it.
- Config: `data/black_diamond/scripts/gold/gold_freshness_config.yaml:107-116` (`bd_silver_allocations`, cadence
  `business-daily`) and `:129-138` (`bd_silver_unrealized`, cadence `daily`); neither has a `freshness_basis`.
- Reader: `.tools/comp-freshness` ignores `freshness_basis` on mtime entries (`_status_from_age` at `:856-860`) and has
  no weekly logic (`CADENCE_LABELS`' weekly label is display only). `lib/trading_calendar.py` has no weekly
  production-day function.
- ⛔ SOVEREIGN HOLD: `.tools/comp-freshness:70-104` skips configs under `data/black_diamond/` unless
  `COMP_FRESHNESS_PIPELINE=1`. You NEVER set that variable. Prove the rule with fixture configs in a temp dir.

**Build:**
1. Read: write `SKIP_PATH_RECORD.json` in your deliverables with keys `skip_path` (`not_on_path` | `bypass_flag` |
   `config_skipped`), `code_ref` (file:line), `run_log_line` (verbatim, ASCII only), `run_date`, `log_source` (the log
   group/stream or S3 key it came from).
2. Rule: add a weekly production-day helper to `lib/trading_calendar.py` (the most recent scheduled weekly production
   day on or before a date, for a declared weekday, rolling back over holidays per the calendar) and a weekly branch in
   `comp-freshness` for entries with `freshness_basis: trading-day-frontier` and `cadence: weekly`. Measure which
   weekday BD produces each table (from the partitions' write dates) and state it in your report.
3. Config: both entries get `freshness_basis: trading-day-frontier`, `cadence: weekly`,
   `weekly_production_weekday: <measured>`.
4. Test `.tools/tests/test_comp_freshness_weekly.py`, offline: FRESH on a day after the weekly producer ran; STALE only
   past the next scheduled weekly production day; positive control: a last write one week past reads STALE; a daily
   entry's grading is unchanged.

## 2. BOUNDS

1. No change to `gold_dispatch.sh` or to whether the gate blocks. No deploy of the config or the reader.
2. Never set `COMP_FRESHNESS_PIPELINE`. Nothing under `data/cot/`. No push.
3. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
.tools/comp-freshness
lib/trading_calendar.py
data/black_diamond/scripts/gold/gold_freshness_config.yaml
.tools/tests/test_comp_freshness_weekly.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~25/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W25-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-f-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round7/checks/f1.AC1.sh; echo "exit=$?"</invocation><expect>skip_path one of not_on_path/bypass_flag/config_skipped with code_ref, run_date and log_source printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-f-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round7/checks/f1.AC2.sh; echo "exit=$?"</invocation><expect>pytest passes with 0 failed (fresh after the weekly run; stale only past the next weekly production day; one-week-past control stale; daily unchanged) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-f-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round7/checks/f1.AC3.sh; echo "exit=$?"</invocation><expect>OK: bd_silver_allocations and OK: bd_silver_unrealized (basis trading-day-frontier, cadence weekly, weekday set) -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~25/NFRA_MCPINDEX.TO-MX-f-1.freshness-weekly-basis-and-skip-path.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, naming the measured weekday per table.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-7 item 2. The weekly rule is proven by offline fixtures because the sovereign
hold keeps agent reads of BD configs off (f1.AC3 reads the YAML's two entries as text structure, not served data).
Battery dry-run at base: f1.AC1 FAIL as expected (record absent); f1.AC2 FAIL as expected (test absent); f1.AC3 FAIL
as expected (allocations cadence business-daily, unrealized daily, no basis).

<status>complete</status>
<round>7</round>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

# TO MDPF_DEMQUE.TO-DQ-t42 -- round 9 DQ-t-42: the lag is DECLARED per tier in the enrolment file, and `--lag-report` prints each name's measured lag against it
<to_id>MDPF_DEMQUE.TO-DQ-t42</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~34</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>LAGDECL</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-42` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 7) |
**outcome_ref:** C-PRICES, C-YAHOO, FWD-8, FWD-9 | **depends_on:** DQ-t-41 (merged @dbf7bacc77)

---

## WORKER FACE

### THE CELL

`DQ-t-42` (CTO round-8 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round8.md` ADDENDUM 8, read it). The price store has no freshness-checker
mode and none is built. The lag is therefore DECLARED in `org/missions/D8/MDPF/MDPF_DEMQUE/requests/ENROLMENT_TIERS.json` and a read-only report prints, per
tier, the declared cycle against every name's measured lag in trading days, with the denominator. **You build NO checker, alarm, monitor, schedule or
mode: one declaration and one read-only command that prints.**

**Build** (in `data/mdpf/scripts/demque/extend_frontier.py`, the enrolment file and a NEW test file; read `extend_frontier.py` at HEAD, its `load_enrolment`,
`_landed`, `_tiers`, `trading_day_ordinal`, and `price_store.index`'s `INDEX_COLS` first):
1. **The declaration.** `ENROLMENT_TIERS.json` gains two top-level keys: `"freshness_basis": "trading-day-frontier"` and
   `"tiers": {"daily": {"cycle_trading_days": 1}, "rolling": {"cycle_trading_days": 5}}`. `load_enrolment` takes the key set
   `{daily_extra, rolling, freshness_basis, tiers}` exactly; `freshness_basis` must equal `trading-day-frontier`; `tiers` must carry exactly `daily` and
   `rolling`, each exactly `{cycle_trading_days}` a positive integer; `tiers.daily.cycle_trading_days` must be 1; and when a rolling request is
   enrolled, `tiers.rolling.cycle_trading_days` must equal `rolling[0].cycle_trading_days` (ONE source: a disagreement is a loud `SystemExit` naming
   both numbers). Any violation is a loud `SystemExit`. Update the stub enrolments in `test_demque_rolling_tiers.py` (and any other
   existing demque test file that writes a stub `ENROLMENT_TIERS.json`) to the new shape and change nothing else in them.
2. **`--lag-report [--today D] [--root R]`.** Read only. Over the names `price_store.index` lists: the day's frontier is
   `tc.expected_last_trading_day(--today or the local date)`; a name's `lag` = the number of trading days from its stored max date to the frontier
   (0 when the stored max date is the frontier, never negative); its stored max date is the index row's `valid_to`. The tier of a name is the one
   `_tiers` assigns it. Print ONE JSON line:
   `{"freshness_basis", "frontier", "indexed", "tiers": {"daily": T, "rolling": T}, "rolling_not_landed"}` where `T` = `{"declared_cycle_trading_days",
   "names", "within", "over", "max_lag", "over_names": [{"cusip", "symbol", "valid_to", "as_of", "lag"}]}`: `within` = names with `lag` <= the
   declared cycle, `over` = names with `lag` > it, `over_names` lists every over name (all of them, never a page), `as_of` is the index row's
   `as_of` column printed beside `valid_to`. `names` per tier add to `indexed`; `rolling_not_landed` is the count `_tiers` already computes.
   State in the docstring which of `valid_to` and `as_of` is the stored max date (read `price_store.write` / `index` to see what each column
   holds) and that the lag is measured from the stored max date. If `as_of` holds something else, say so in the report and a surprise row.
3. NEW `test_demque_lag_report.py` (pytest; a LOCAL store root under `tmp_path`, a stub enrolment folder, no network, no S3, `--today` pinned) with
   exactly these names:
   `test_the_enrolment_declares_the_basis_and_a_cycle_per_tier_and_a_disagreeing_rolling_cycle_is_refused`,
   `test_the_lag_report_counts_every_indexed_name_in_one_tier_with_its_measured_lag`,
   `test_a_name_older_than_its_tier_cycle_is_listed_over_and_never_counted_within`.
   The existing demque test files keep passing.

### ACCEPTANCE

<criterion id="DQ9-t42-AC1" cell_refs="DQ-t-42"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t42_tests.py</invocation><expect>LAG-OK</expect></criterion>
<criterion id="DQ9-t42-AC2" cell_refs="DQ-t-42"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t42_real.py</invocation><expect>LAG-REAL-OK</expect></criterion>
`DQ9-t42-AC1` -- the three named tests. `DQ9-t42-AC2` -- on the REAL served store (S3 read only): declared cycles 1 and 5, the two tiers partition the
indexed names, within + over = names in each tier, every over name listed and really over. The held names the extension leaves (about 14, end
2026-06-23) are expected in `over_names`: the report prints them, it does not hide them. Report the whole folder `pytest data/mdpf/scripts/demque`
once (145 passed at the t-41 merge, plus these 3).

<expected_criteria>DQ9-t42-AC1,DQ9-t42-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `LAG-BAD no file ...`; `extend_frontier.py: error: one of the arguments --plan --apply --plan-week is required`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY against S3 and Yahoo: no write to the served store, the pacer state, the queue or the ledger; no Yahoo or Bloomberg call; no AWS write;
  no deploy. You arm no timer, background task or OS task, and build no checker, alarm, notification or mode (a standing moratorium).**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W34-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/extend_frontier.py
data/mdpf/scripts/demque/test_demque_lag_report.py
data/mdpf/scripts/demque/test_demque_rolling_tiers.py
data/mdpf/scripts/demque/test_demque_extend_frontier.py
org/missions/D8/MDPF/MDPF_DEMQUE/requests/ENROLMENT_TIERS.json
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit; another existing test file that needs the new stub shape is a
surprise row asking for the grant, not an edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-42`.
<owned_cells>DQ-t-42</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t42-AC1, DQ9-t42-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~34/MDPF_DEMQUE.TO-DQ-t42.tier-lag-declaration-and-lag-report.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t42-AC1,DQ9-t42-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the report's one JSON line verbatim (the over_names trimmed to the first 3 plus the count), the meaning of `as_of`
versus `valid_to`, the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write.
comp-adversary: DECLARED-NOT-APPLICABLE a declaration file and a read-only printing command; no served write, no checker (CTO ADDENDUM 8).
risk: LOCAL -- code, tests and one declaration. Nothing served moves.
direct_act: false -- a worker order.
</preflight>

Source: CTO round-8 analysis ADDENDUM 8 (msg 4260); TO-DQ-t41 surprise row W33-S3; decomposition round 9.

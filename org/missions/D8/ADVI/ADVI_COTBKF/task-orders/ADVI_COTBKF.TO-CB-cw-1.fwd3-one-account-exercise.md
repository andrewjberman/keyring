# TO ADVI_COTBKF.TO-CB-cw-1.fwd3-one-account-exercise -- round 101 CB-cw-1: read one account's daily returns across its whole span on the SERVED tables, string them into months, check them against Commonwealth's reported months, and show every difference, blank day and reported figure; read-only, counts only

<to_id>ADVI_COTBKF.TO-CB-cw-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~190</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>101</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-cw-1` (`decompositions/ADVI_COTBKF_DECOMP.round101.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** FWD-3 of the PRD: an analyst reads each Cottonwood account's returns day by day, after fees, back to 2013; strung over a month the days give the return Commonwealth reported for that month, or the difference is shown with its reason; a day that cannot be worked out says so and is never filled in; Commonwealth's own monthly, yearly and since-inception returns, with its benchmark, are readable beside them as reported. Its DONE WHEN is an EXERCISE: one account's daily returns read across the whole span and checked against the monthly figures Commonwealth reported. The three served tables exist (round 98), and no record yet reads one account across its span on them. You do that read, as an analyst would, and record it. **Read-only: you write nothing to S3, serve nothing, change no code and no committed file except your own record.** You report what the data shows; you do not grade FWD-3 (the CTO does).

**Inputs (READ-ONLY).** The served objects, read with `get_object` at the pinned VersionIds (columns as the tables carry them):
- `s3://opal-data-assets/commonwealth/cottonwood/silver/daily_returns/date=2026-06-23/part-00000.parquet` at `lNzQMjfx6uX2zdFdWKsDANboShtDUz2N` (columns include `account`, `date`, `value`, `flow`, `return` (decimal, null when blank), `blank_reason`);
- `s3://opal-data-assets/commonwealth/cottonwood/silver/month_grades/date=2026-06-23/part-00000.parquet` at `nkTE.F82uFSboXr9PEamIENCwFL9cwcC` (columns include `account`, `month`, `computed_pct`, `reported_month_pct`, `diff_pct`, `verdict`, `reason`, `reported_year_pct`, `reported_itd_pct`, `benchmark_month_pct`, `benchmark_year_pct`, `benchmark_itd_pct`, `benchmark_description`, `reported_note`).

**Read first.** (1) The grading rule: `data/assets/scripts/silver/commonwealth_monthly_grade.py` module docstring (computed_pct = (prod(1 + return) - 1) * 100 over the month's rows; MATCH when abs(diff_pct) <= 0.05 percentage points; UNGRADABLE when a day of the month has a null return or either side is absent; nothing is estimated or filled). (2) The issuer's script `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cw1_fwd3_recompute.py` (in your worktree; read it, do not edit it): it picks the account BY RULE, the account with the most GRADED months (rows of `month_grades` whose `verdict` is MATCH or DIFF), a tie to the smallest sha256 hex of the account id, and it prints the counts your record must equal. (3) The PRD's FWD-3 lines (`org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md`, FWD-3).

**Your items.**

1. **The account.** Run the issuer's script with no argument: `python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cw1_fwd3_recompute.py` (a few seconds). It prints `FWD3-POPULATION ...` and `FWD3-RECOMPUTE account_hash8=<8 hex> ...`. The account you read is the one whose sha256 starts with that `account_hash8`; find it yourself from the served `month_grades` by the same rule (do not take a different account, and never write or print the account id: the record names it only by the 8 hex digits).
2. **Read the whole span.** From the served `daily_returns`, read that account's every row: first and last date, number of days, number of days with a return and number blank, and the blank days grouped by `blank_reason` (counts per reason). A blank day is reported as blank with its reason, never filled.
3. **String the days into months and check them.** For each month of the account in the served `month_grades`: string that month's daily returns yourself as the module does and compare (a) with the served `computed_pct` (equal within 0.000001 percentage points, or both absent), and (b) with Commonwealth's `reported_month_pct` (within 0.05 percentage points is a match). Count: months, months where your strung return equals the served `computed_pct`, months that match the reported figure, months that differ, months ungradable. For every month that differs or is ungradable, list its reason by category in counts (the served `reason` text, or the blank-day reason that made the month ungradable); name each such month by its `YYYY-MM`.
4. **The reported figures beside the days.** Count the account's months for which the served table shows the reported month, the reported year, the since-inception return and the benchmark (month, year, since-inception, with its description) readable beside the computed figure, and say for how many months each is absent and why (the served `reported_note`, counts by category).
5. **The population.** From the whole of the two served tables (not just the account): months in total and by `verdict`; account-days in total and the number with no return; the share of each, so that the report says how representative the one account is. These are counts only.
6. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~190/FWD3_EXERCISE_RECORD.json` with exactly these top-level keys: `measured`, `reason` (when not measured), `served` (`{"daily_returns_version","month_grades_version","rows_read_daily","rows_read_months"}`), `account_hash8`, `selection` (`{"rule","graded_months"}`), `span` (`{"first","last"}`), `days`, `blank_days` (`{"count","by_reason":{reason:count}}`), `months`, `strung_equals_served_computed`, `matches_reported`, `differ`, `ungradable`, `differences` (`[{"month","kind","reason"}]` for every differing or ungradable month), `readable` (`{"reported_month","reported_year","reported_itd","benchmark_month","benchmark_year","benchmark_itd"}` as month counts), `population` (`{"months","match","diff","ungradable","days","blank_days"}`), `what_this_shows` (two sentences: what was exercised and what it found, in counts), `not_established`; and a short `.md` beside it. **No account id, name or dollar value in either**; percentages for named months are allowed only in `differences` and only as counts of percentage-point size bands, never exact figures. The keys named `account_hash8`, `days`, `months`, `strung_equals_served_computed`, `matches_reported`, `differ`, `ungradable` and `population` must equal what the issuer's script prints.

### ACCEPTANCE

<criterion id="CB101cw1-AC1" cell_refs="CB-cw-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~190/FWD3_EXERCISE_RECORD.json',encoding='utf-8'));m=d['measured'];print('FWD3-EXERCISE measured=%s' % m + ((' account=%s days=%d months=%d match=%d differ=%d ungradable=%d' % (d['account_hash8'],d['days'],d['months'],d['matches_reported'],d['differ'],d['ungradable'])) if m else ' reason=%s' % d['reason']))"</invocation><expect>^FWD3-EXERCISE measured=(True account=[0-9a-f]{8} days=\d+ months=\d+ match=\d+ differ=\d+ ungradable=\d+|False reason=.+)$</expect></criterion>
`CB101cw1-AC1` -- the record names the account (8 hex digits only) and states the days, the months and how they split, or states plainly why nothing could be measured.

<criterion id="CB101cw1-AC2" cell_refs="CB-cw-1"><invocation>python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cw1_fwd3_recompute.py org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~190/FWD3_EXERCISE_RECORD.json</invocation><expect>^FWD3-CROSS selected_by_rule=True days_equal=True months_equal=True strung_equal=True matched_equal=True differ_equal=True ungradable_equal=True population_equal=True$</expect></criterion>
`CB101cw1-AC2` -- the issuer's script recomputes the same exercise from the served objects and the record equals it: the account is the one the rule picks, and the days, months, strung-equals-served, matched, differing, ungradable and population counts agree.

<criterion id="CB101cw1-AC3" cell_refs="CB-cw-1"><invocation>python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cu1_ac3_served_unchanged_check.py</invocation><expect>^SERVED-UNCHANGED versions_equal=3 of 3$</expect></criterion>
`CB101cw1-AC3` -- the cell wrote nothing: the three served keys still carry the VersionIds the round-98 apply left (the issuer's script reads object metadata only).

<expected_criteria>CB101cw1-AC1,CB101cw1-AC2,CB101cw1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below only: your deliverables folder, your own NEW channel row, and this order's own file (for the one `<status>` flip). You change no code, test or other committed file. Scratch, if any, stays under `C:/Dev/ajb_workspace/.scratch/cotbkf_r101/` (gitignored, never committed); a small read script you write may be committed in your deliverables folder as evidence.
- **AWS: READ-ONLY** (`get_object` of the two served objects at the pinned VersionIds and `head_object` for AC3); no write, no `--apply`, no vendor call, no Bloomberg. You do not contact Cottonwood or Commonwealth.
- **No account id, name, tax number or dollar value** in the record, the report or any message: the account is named only by `account_hash8`.
- **NEVER** serve, apply, overwrite, push, override a gate or `--force`; never edit any module; never grade FWD-3 yourself (report what the data shows); never fill or estimate a blank day.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W190-S<k>` (`date -u +%FT%TZ` for `surfaced_at`), APPENDED to the channel file with `open(path, 'ab')` writing LF bytes only (the file holds CRLF lines from earlier rows: never read and rewrite it); `git diff --numstat` must show added lines only. A difference between your counts and the issuer's script is a finding to report, not to adjust: AC2 then reads False and you stop.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-cw-1.fwd3-one-account-exercise.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row; the one write to this order is the `<status>` flip.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round101.md</decomp_doc> (round 101), cell `CB-cw-1`.
<owned_cells>CB-cw-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB101cw1-AC1, CB101cw1-AC2, CB101cw1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~190/ADVI_COTBKF.TO-CB-cw-1.fwd3-one-account-exercise.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB101cw1-AC1,CB101cw1-AC2,CB101cw1-AC3` BEFORE the flip. The `output_evidence` of each criterion must equal its `expect` pattern exactly (no suffix); put any note in `denominator`. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when all three PASS** (the order file is in your `<paths>` for this flip).
</proof_of_spec>

**REPORT:** FIRST the `FWD3-EXERCISE` line. Then: the account by its 8 hex digits and the rule that picked it; the span, days, blank days by reason; the months and how they split (strung equals served, matched, differing, ungradable) and each difference's reason by category; the readable reported figures; the population counts; what the data shows in two sentences; any step you could not run and why; the three criterion lines; commits; every gate refusal and hook denial, verbatim. No account id or value.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of two served objects and a count; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE get_object of two objects at pinned versions under the existing role; no new permission.
comp-adversary: RUN -- the account is chosen by a fixed rule and not by hand; the issuer's script recomputes the same counts from the same objects and the record must equal it (AC2); BLIND: the issuer's script and the worker read the same two served objects, so a defect in the served tables themselves is not tested here (a different exercise: a read of Commonwealth's own reported performance against the delivered files), the monthly stringing is the module's rule restated, and one account is not the population (the population counts are reported beside it for that reason).
lane: the <paths> block IS the grant (worker RULING 1), and now names the order file for the status flip.
</preflight>

**ISSUER NOTES:** Source: `1.0.0_SA_CTO~DELL1` msg 6604 (round 100 grade; FWD-3 is the NOT_REALIZED outcome whose act is the COO's). The issuer ran the recompute script before cutting (population months 82,593: MATCH 3,678, DIFF 288, UNGRADABLE 78,622; days 1,691,729: 1,584,413 blank) and chose the by-rule account on the first run's finding that a most-months rule picks an all-UNGRADABLE account. Mechanical checks dry-run at the base (the record file is absent): AC1 and AC2 FAIL as expected; AC3 PASSES (served versions unchanged). Round 100's order omitted its own file from `<paths>` (row D1-S16); this one names it.

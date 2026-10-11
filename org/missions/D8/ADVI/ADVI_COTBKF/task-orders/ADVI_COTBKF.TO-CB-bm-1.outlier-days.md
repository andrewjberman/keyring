# TO ADVI_COTBKF.TO-CB-bm-1.outlier-days -- round 65 CB-bm-1: the 207 measured days above 100 percent, classed, with the threshold table

<to_id>ADVI_COTBKF.TO-CB-bm-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~94</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>65</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bm-1` (`decompositions/ADVI_COTBKF_DECOMP.round65.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**RULE: counts, shares, security identifiers (CUSIP, symbol), asset kinds, dates, transaction types, file-and-line citations and reason codes only** in your record, report, commit messages and rows. Never an account id, never an account's position size, value, flow or return tied to an account. A RATIO of two of an account's numbers may be reported to two decimal places. Aggregate before you print.

**This is a MEASUREMENT. Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_65_20261011.md` section 3 item 1 and section 4 item 1; the round-64 record
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~92/FLAGGED_DAYS.json` and its `.md` (the four classes found on 24
days: you class the same way and reuse its class names where the mechanism is the same); and the newest row in the channel whose
`one_line` begins "The Cottonwood returns table carries 207 measured days".

**Why.** FWD-3 says a day that cannot be worked out says so and is never filled in. 207 measured days carry an absolute daily return
above 100 percent. The CTO will rule a blank reason and its threshold AFTER these are classed, and will not pick a floor from two
numbers. Your table is what that ruling stands on.

**Your item.**

1. Rebuild the set from `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/daily_returns.parquet` (columns account, date, value, flow, return, blank_reason,
   cash_leg): the measured rows (a non-null `return`) whose prior value is positive. That must read 107,311. Of them, those with
   `abs(return) > 1` must read 207; 55 of the 207 on a prior value under 1.00 and 152 on 1.00 or more. The prior value is the same
   account's `value` on its previous row by date. If your counts differ, that is the refusal clause: stop, do not adjust the rule.
2. Class all 207, by mechanism, from the data: the account's transactions on the day and the two days either side
   (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/trade_year=*/*.parquet`; read its schema first), its holdings rows on the day and the prior day
   (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/account_day_value.parquet`: how many positions, how many unpriced), and how the form treats the day
   (`data/assets/scripts/silver/commonwealth_daily_returns.py`, `commonwealth_flows.py`, `commonwealth_daily_valuation.py`).
3. For each class: the count; how many sit on a prior value under 1.00, from 1.00 to under 100.00, and 100.00 or more; the mechanism in
   one sentence with file and line; and its `kind`:
   - `RIGHT_THOUGH_LARGE` -- the arithmetic is right and the base is a real balance (a real close-out or a real gain);
   - `RESIDUAL_BASE` -- the arithmetic is right and the base is a leftover too small for a return on it to mean anything;
   - `FORM` -- a defect of the form (a flow, fee, transfer or price the form treats wrongly);
   - `DATA` -- the custodian's rows state the day differently from what happened (a missing or mis-dated row);
   - `UNEXPLAINED` -- you could not establish it. This is a legal class; do not invent a mechanism.
4. So the CTO can pick a threshold from a distribution: for ALL 107,311 measured rows, the count with `abs(return)` above 0.10, 0.25,
   0.50, 1.00, 2.00 and 10.00, each split by prior value under 1.00, 1.00 to under 100.00, and 100.00 or more.
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~94/OUTLIER_DAYS.json` and a short `.md` beside it. Top-level keys, exactly: `measured_rows_positive_prior`, `outliers`,
   `outliers_prior_under_1`, `outliers_prior_1_or_more`, `classes` (a list of `{"class", "count", "prior_under_1", "prior_1_to_100",
   "prior_100_or_more", "kind", "mechanism", "file", "line"}`), `threshold_table` (a list of `{"abs_return_above", "prior_under_1",
   "prior_1_to_100", "prior_100_or_more"}`), `unexplained`, `evidence`, `not_established`.

**How to print.** Refer to a day by an index you assign, never by its account. Dates, transaction types, counts, booleans and ratios
to two decimals are fine.

### ACCEPTANCE

<criterion id="CB65bm1-AC1" cell_refs="CB-bm-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~94/OUTLIER_DAYS.json',encoding='utf-8'));c=d['classes'];print('OUTLIER-DAYS-RECORD measured_rows_positive_prior=%d outliers=%d prior_under_1=%d prior_1_or_more=%d classes=%d class_sum=%d unexplained=%d threshold_rows=%d'%(d['measured_rows_positive_prior'],d['outliers'],d['outliers_prior_under_1'],d['outliers_prior_1_or_more'],len(c),sum(x['count'] for x in c),d['unexplained'],len(d['threshold_table'])))"</invocation><expect>OUTLIER-DAYS-RECORD measured_rows_positive_prior=107311 outliers=207 prior_under_1=55 prior_1_or_more=152</expect></criterion>
`CB65bm1-AC1` -- the set is rebuilt to the measured counts and every one of the 207 sits in a class (`class_sum` equals 207, with
`UNEXPLAINED` a legal class).

<criterion id="CB65bm1-AC2" cell_refs="CB-bm-1" judgment="true"/>
`CB65bm1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: each class's mechanism follows from the cited lines
and counts; the five kinds are told apart on evidence; an unexplained day is called unexplained; the threshold table's rows sum to
their totals.

<expected_criteria>CB65bm1-AC1,CB65bm1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** You READ local data under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` (the base checkout; never write
  there) and write scratch under your own worktree `.scratch/` only (never committed).
- **No network call of any kind**: no AWS, no Yahoo, no Bloomberg, no HTTP. Everything you need is local.
- **No gate override** of any kind and no `--force`. If a gate refuses a commit, stop and report its exact refusal line.
- **Do not open or print** anything under `C:/dev/_cotbkf_private_evidence_20261009/`. A commonwealth script you run carries
  `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row: the next
  free `ADVI_COTBKF-D2-S<k>` id read from the channel at write time, `"fabric": "dell2"`, `surfaced_at` read from the clock.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round65.md</decomp_doc> (round 65), cell `CB-bm-1`.
<owned_cells>CB-bm-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB65bm1-AC1, CB65bm1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~94/ADVI_COTBKF.TO-CB-bm-1.outlier-days.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB65bm1-AC1,CB65bm1-AC2` BEFORE the flip. Mechanical: CB65bm1-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the `OUTLIER-DAYS-RECORD` line; each class with its counts by prior-value band, kind and mechanism (file and line); the threshold table; the unexplained count; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the set is rebuilt to four measured counts before any class is named; UNEXPLAINED is a legal class; the threshold table covers all measured rows so the ruling does not stand on the tail alone; BLIND: a cause that lives in the custodian's raw file and not in silver.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-65 analysis @1e9128413f (msg 4715), section 4 item 1; `3.0.0_SA_CVO` REMEDIATION_v37 @054e94e8fc.

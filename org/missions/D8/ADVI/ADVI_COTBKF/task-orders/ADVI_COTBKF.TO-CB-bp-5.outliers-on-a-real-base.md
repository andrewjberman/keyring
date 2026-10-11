# TO ADVI_COTBKF.TO-CB-bp-5.outliers-on-a-real-base -- round 68 CB-bp-5: the 179 measured days above 10 percent on a base of 100.00 or more, classed by cause

<to_id>ADVI_COTBKF.TO-CB-bp-5</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~105</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>68</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bp-5` (`decompositions/ADVI_COTBKF_DECOMP.round68.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**RULE: counts, shares, security identifiers, asset kinds, dates, transaction types, file-and-line citations and reason codes only.**
Never an account id, never an account's value, flow, quantity or return. A RATIO of two of an account's numbers may be reported to
two decimals. Refer to a day by an index you assign.

**This is a MEASUREMENT. You change no code.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_68_20261011.md` section 2 item 3 and section 3 item 5; the round-65 record
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~94/OUTLIER_DAYS.json` and its `.md` (the 207 days above 100
percent, five classes, and the threshold table); the round-64 record `.../0.9.0_WK_ADVI_COTBKF~92/FLAGGED_DAYS.json`.

**Why.** The CTO will not set a threshold for a "leftover balance" before the days are understood. Round 65 called 206 of 207 outlier
days a credit on a leftover balance; but 56 of them sit on a prior value of 100.00 or more, which is not a leftover by any reading,
and the measured days with a return between 10 and 100 percent on such a base were never examined.

**Your item.**

1. Rebuild the set from `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/daily_returns.parquet`: the measured rows (non-null `return`) whose prior value (the
   same account's `value` on its previous row by date) is 100.00 or more and whose `abs(return)` is above 0.10. That must read 179
   (round 65's threshold table: 179 above 0.10, of which 57 above 1.00). If it does not, that is the refusal clause.
2. **Class all 179 BY CAUSE, the classes found by reading**, not carried over. For each day read the account's transactions on the
   day and the two days either side (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/trade_year=*/*.parquet`), its holdings on the day and the prior day
   (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/account_day_value.parquet`: positions, unpriced positions, the largest position's share of value), the
   security's price series across the day where one position drives the move, and how the form treats the day
   (`commonwealth_daily_returns.py`, `commonwealth_flows.py`, `commonwealth_daily_valuation.py`). Do not accept "a credit on a
   leftover balance" for a base of 100.00 or more without saying what the base is and why the credit is not a flow.
3. For each class: the count, split at `abs(return)` above 1.00 and at 0.10 to 1.00; the mechanism in one sentence with file and line;
   its `kind`: `TRUE_RETURN` (a real market move or a real gain the account had), `FORM` (the form treats a flow, fee, credit,
   transfer or price wrongly), `DATA` (the custodian's rows state the day differently from what happened), `PRICE` (a price in the
   series is wrong or stale), `UNCLASSED`. **Print the unclassed remainder**: it is a legal class and it is not hidden.
4. Say how many days you read row by row and how many you placed by rule; hand-check at least 8 of each class, or all if fewer.
5. For the round-65 day classed FORM (an in-kind contribution valued at a close the next-day sale contradicts): it is inside your 179;
   place it again from your own reading and say whether you agree.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~105/OUTLIERS_ON_A_REAL_BASE.json` and a short `.md` beside it. Top-level keys, exactly: `days`, `days_above_100pct`, `days_10_to_100pct`,
   `classes` (a list of `{"class", "count", "above_100pct", "from_10_to_100pct", "kind", "mechanism", "file", "line",
   "hand_checked"}`), `unclassed`, `read_row_by_row`, `placed_by_rule`, `agrees_with_round_65_form_day`, `evidence`,
   `not_established`.

### ACCEPTANCE

<criterion id="CB68bp5-AC1" cell_refs="CB-bp-5"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~105/OUTLIERS_ON_A_REAL_BASE.json',encoding='utf-8'));c=d['classes'];print('OUTLIERS-ON-A-REAL-BASE-RECORD days=%d above_100pct=%d from_10_to_100pct=%d classes=%d class_sum=%d unclassed=%d read_row_by_row=%d placed_by_rule=%d'%(d['days'],d['days_above_100pct'],d['days_10_to_100pct'],len(c),sum(x['count'] for x in c),d['unclassed'],d['read_row_by_row'],d['placed_by_rule']))"</invocation><expect>OUTLIERS-ON-A-REAL-BASE-RECORD days=179 above_100pct=57 from_10_to_100pct=122</expect></criterion>
`CB68bp5-AC1` -- the set is rebuilt to the measured counts and every day sits in a class (`class_sum` equals 179, the unclassed
remainder printed).

<criterion id="CB68bp5-AC2" cell_refs="CB-bp-5" judgment="true"/>
`CB68bp5-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the classes are causes found by reading, each with its
cited lines; TRUE_RETURN, FORM, DATA and PRICE are told apart on evidence; no day on a base of 100.00 or more is called a leftover
without saying what the base is; the unclassed remainder is printed.

<expected_criteria>CB68bp5-AC1,CB68bp5-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** No network call; everything is local.
- **NEVER `--apply`, `--overwrite`, a serve, or any S3 write.** Read-only S3 gets and listings the build already makes are allowed.
  No push. No `--refresh`.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity or return. Counts, dates, CUSIPs, prices per security, ratios,
  version ids and reason codes only. A build log line that prints `read_account=` is never echoed: filter it out before you read a log.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Sequencing:** never start a later step before the earlier one's check has been read.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W105-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round68.md</decomp_doc> (round 68), cell `CB-bp-5`.
<owned_cells>CB-bp-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB68bp5-AC1, CB68bp5-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~105/ADVI_COTBKF.TO-CB-bp-5.outliers-on-a-real-base.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB68bp5-AC1,CB68bp5-AC2` BEFORE the flip. Mechanical: CB68bp5-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the `OUTLIERS-ON-A-REAL-BASE-RECORD` line; each class with its counts in the two bands, kind, mechanism (file and line) and how many were hand-checked; the unclassed remainder; how many days were read row by row; whether the round-65 FORM day is confirmed; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the set is rebuilt to three measured counts first; the classes are to be found by reading and the round-65 label is barred for a base of 100.00 or more without a stated base; UNCLASSED is legal and printed; the one day round 65 called FORM is re-placed independently; BLIND: a cause that lives in the custodian's raw file and not in silver.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-68 analysis @b3a272fffc (msg 5008), section 3 item 5; `3.0.0_SA_CVO` REMEDIATION_v38 @931dc9ea93.

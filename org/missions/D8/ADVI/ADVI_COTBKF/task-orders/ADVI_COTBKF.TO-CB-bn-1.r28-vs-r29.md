# TO ADVI_COTBKF.TO-CB-bn-1.r28-vs-r29 -- round 66 CB-bn-1: the build re-run locally under method_r28 and method_r29, and every account-day that changes

<to_id>ADVI_COTBKF.TO-CB-bn-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~97</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>66</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bn-1` (`decompositions/ADVI_COTBKF_DECOMP.round66.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**RULE: counts, dates, month labels, reason codes, rule names and file-and-line citations only** in your record, report, commit
messages and rows. Never an account id, never an account's value, flow or return. Aggregate before you print.

**This is a MEASUREMENT by re-running the build LOCALLY under two rule versions. It writes NOTHING remote: no `--apply`, no S3 put, no
serve. Read-only S3 gets that the build itself makes (its price and split stores) are allowed; if a step can only run by writing
remotely, stop: that is the refusal clause.**

**Read first:** the round-65 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~96/WITHHOLDING_FLOW_REACH.json`;
`data/assets/scripts/silver/commonwealth_flows.py` (`WITHHOLDING_ALWAYS_FLOW_RULES`, `withholding_flows`); the module docstrings and
argument lists of `commonwealth_sweep_regrade.py` (it takes a before and an after cash leg), `commonwealth_daily_valuation.py`,
`commonwealth_daily_returns.py` and `commonwealth_fwd3_serve.py` (`--build`, `--dry-run`; NEVER `--apply`); and the manifest of the
served build, `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/fwd3_manifest.json` (its cash leg, price basis, run commit and hold list: your two runs use the
SAME settings except the leg).

**Why.** `method_r29` is `method_r28` plus one change: a cash tax withholding is an external outflow with or without a same-day
withdrawal row. It is selectable; the default is still `method_r28`. The CTO moves the default, and a later order re-mints exactly the
days whose answer changes, ONLY after this comparison says which those are. 7 measured days are the known floor (the days carrying
such a withholding); a changed outflow can also move a neighbouring day, a month grade, or which months read ABSENT.

**Your item.**

1. **Positive control first.** Re-run the build locally under `method_r28`, named EXPLICITLY, with the served build's settings, into a
   NEW folder under your worktree's `.scratch/` (never under `C:/dev/ajb_workspace/.scratch/advi_cotbkf`). Its daily returns table must equal the served local copy
   `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/daily_returns.parquet` row for row on (account, date, return, blank_reason): 1,691,729 rows, 0 differing.
   If it does not reproduce, STOP: that is the refusal clause, and the differing count by blank_reason is your report. Do not go on to
   r29 on a control that failed.
2. **Run `method_r29`**, named explicitly, same settings, into another new folder.
3. **Compare the two daily returns tables** on (account, date). Every account-day falls in exactly one of:
   - `both_measured_same` -- a return under both, equal to 1e-12;
   - `both_measured_different` -- a return under both, not equal;
   - `measured_r28_only` -- a return under r28, blank under r29;
   - `measured_r29_only` -- blank under r28, a return under r29;
   - `both_blank_same_reason`; `both_blank_reason_changed`;
   - `row_r28_only`; `row_r29_only` (a row present under one rule only).
   The eight counts sum to the union of the two tables' rows.
4. **The changed days, listed for the re-mint.** The distinct DATES that carry at least one account-day NOT in `both_measured_same` or
   `both_blank_same_reason`: the count, the first and last, and the list written to `CHANGED_DATES.csv` in your deliverables folder
   (columns: date, account_days_changed; no account column). The minted table is one file per date, so a date is the unit a re-mint
   replaces.
5. **Where the change comes from.** Of the changed account-days: how many are one of the 71 withholding days with no withdrawal row;
   how many are another day of the same account; how many are in an account with no such withholding at all (that count should be 0;
   if it is not, say what moved them). And the month grades: how many account-months change verdict, and how many change between
   ABSENT and not.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~97/R28_VS_R29.json`. Top-level keys, exactly: `settings` (cash legs, price basis, run commit of the code you ran),
   `control` (`{"rows", "differing"}`), `rows_union`, `classes` (the eight names above, each a count), `changed_account_days`,
   `changed_dates`, `first_changed_date`, `last_changed_date`, `changed_by_origin` (`{"withholding_day", "same_account_other_day",
   "other_account"}`), `month_verdicts_changed`, `month_absent_changed`, `evidence`, `not_established`.

**Runtime.** The holdings table is 21 million rows and a full run takes a while. Run each step as ONE command in the foreground with a
long timeout, or in the background and wait for it; do not start a second run of the same step while one is going.

### AMENDMENT 1 (2026-10-11T11:42Z, issuer `2.0.0_SA_COO~C2`) -- the control is re-stated: both runs on the SAME inputs today; the drift from the served table is recorded, not required to be zero

Worker ~97 ran the control and stopped, correctly (row ADVI_COTBKF-D2-W97-S1; `CONTROL_RECORD.json`): today's `method_r28` re-run
differs from the served local table on 30 of 1,691,729 account-days (28 returns in one account over 2020-10-12 to 2020-11-18, largest
difference 0.0053; 2 blank reasons). The cause it measured is an INPUT that moved, not code: the split-history store the build reads
live from S3 lists 141 held CUSIPs today against 32 in the served run's log (splits applied 42 against 38; repair days 1,102 against
1,091). The code path of `method_r28` is unchanged since the served run. So NO run today can reproduce the served table, and the control
as first written cannot pass. That drift is the CTO's to rule on and is reported to it separately. **This amendment replaces step 1 and
adds to step 3 and 6; steps 2, 4 and 5 stand.**

**Step 1, replaced -- the control is "same inputs, rule the only difference".**
- The baseline is your OWN `method_r28` run of today (already made: `.scratch/w97/r28` and `.scratch/w97/fwd3_r28`). Do not re-run it
  unless the check below fails.
- Run `method_r29` with the same settings. Then PROVE the two runs read the same inputs: the split-store lines each run's log prints
  (held CUSIPs listed, splits applied, splits not applied, disagreements, repair days) are equal, and the two runs'
  `security_day_price.parquet` are equal row for row. If they are not equal, the store moved between your runs: re-run `method_r28`
  immediately before or after `method_r29` until the two agree, and say how many attempts it took. If it cannot be made to agree in
  three attempts, that is the refusal clause.
- The record's `control` is `{"rows": 1691729, "differing": 30}`: today's r28 against the SERVED table, as you measured it. It is a
  finding, stated, not a pass condition.

**Step 3, added.** The eight classes compare today's r28 run with today's r29 run. Add to the record a ninth, separate count,
`drift_days_also_changed_by_rule`: how many of the 30 drift account-days are ALSO changed by the rule (expected 0).

**Step 6, added keys:** `inputs_equal` (`{"split_store_lines_equal": true|false, "price_rows_equal": true|false, "attempts": n}`),
`drift_vs_served` (`{"account_days": 30, "dates": n}`), `drift_days_also_changed_by_rule`. `CHANGED_DATES.csv` lists the dates changed
BY THE RULE (r28 today against r29 today) and, in a second column pair, marks the dates that differ from the served table by drift
(columns: date, account_days_changed_by_rule, account_days_drifted_from_served).

**The criterion CB66bn1-AC1: its `<expect>` becomes `R28-VS-R29-RECORD control_rows=1691729 control_differing=30`.** The invocation does
not change. You make that one edit to the `<expect>` in this order file IN THE SAME COMMIT as the proof instance that records the new
expectation, and flip the status in that commit.

**Sequencing rule, restated:** never start a later step before the earlier one's check has been read.

### ACCEPTANCE

<criterion id="CB66bn1-AC1" cell_refs="CB-bn-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~97/R28_VS_R29.json',encoding='utf-8'));c=d['classes'];print('R28-VS-R29-RECORD control_rows=%d control_differing=%d rows_union=%d class_sum=%d both_measured_different=%d measured_r28_only=%d measured_r29_only=%d changed_account_days=%d changed_dates=%d'%(d['control']['rows'],d['control']['differing'],d['rows_union'],sum(c.values()),c['both_measured_different'],c['measured_r28_only'],c['measured_r29_only'],d['changed_account_days'],d['changed_dates']))"</invocation><expect>R28-VS-R29-RECORD control_rows=1691729 control_differing=0</expect></criterion>
`CB66bn1-AC1` -- the r28 re-run reproduces the served table exactly, and the comparison is recorded with its eight classes summing to
the union. The issuer and the CTO read the counts.

<criterion id="CB66bn1-AC2" cell_refs="CB-bn-1" judgment="true"/>
`CB66bn1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the two runs differ in the rule only; the control was
run before the comparison; every changed day is traced to a withholding or called unexplained; the list of changed dates is the set a
re-mint would replace, no wider and no narrower.

<expected_criteria>CB66bn1-AC1,CB66bn1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** You READ under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` and never write there. Run outputs go under your
  own worktree `.scratch/` and are never committed.
- **NEVER `--apply`, `--overwrite`, a serve, or any S3 write.** No push.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json`
  in its command line. Do not open or print anything else under that folder.
- **No gate override** of any kind and no `--force`.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W97-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file (open it
  in append mode; `git diff --numstat` must show added lines only).

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round66.md</decomp_doc> (round 66), cell `CB-bn-1`.
<owned_cells>CB-bn-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB66bn1-AC1, CB66bn1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~97/ADVI_COTBKF.TO-CB-bn-1.r28-vs-r29.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB66bn1-AC1,CB66bn1-AC2` BEFORE the flip. Mechanical: CB66bn1-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the exact commands of the three runs (control, r28, r29) and their settings; the control line (rows, differing); the `R28-VS-R29-RECORD` line; the eight class counts; changed account-days by origin; the changed dates (count, first, last); month verdicts changed and ABSENT changed; what is not established; a statement that nothing was written remotely; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a hand-run local re-derivation; nothing is scheduled or served.
comp-iam: DECLARED-NOT-APPLICABLE read-only S3 gets the build already makes; no write; BLIND: comp-iam was not run by the issuer.
comp-adversary: RUN -- a positive control (the r28 re-run must equal the served table row for row) gates the comparison, so a difference of environment is not read as a difference of rule; the eight classes must sum to the union; changed days are traced to their origin and a non-zero other-account count must be explained; BLIND: the served day files themselves are not re-read here.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` msg 4734 (2026-10-11), items 2 and 3, and msg 4772; round-65 packet @66db401fb2; rows ADVI_COTBKF-D2-S111 and D2-S113.

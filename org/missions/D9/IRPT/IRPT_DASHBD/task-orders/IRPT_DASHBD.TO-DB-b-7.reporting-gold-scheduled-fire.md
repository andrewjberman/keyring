# TO IRPT_DASHBD.TO-DB-b-7 -- The reporting gold on its own clock: the adapter packaged unedited as a scheduled function, its fire time read from its inputs' landings, planned not applied

<to_id>IRPT_DASHBD.TO-DB-b-7</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~1</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-02</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO round-2 analysis @f5fbeaa543 item E1; ADDENDUM 1 A3 (@7a888d7675); row
IRPT_DASHBD-S13 | **Decomp cell:** `DB-b-7` (decomposition section 3) | **outcome_ref:** FWD-1 (current every trading day) |
**depends_on:** none

---

## WORKER FACE

**The cell.** The reporting gold `account_return_daily` stops at `date=2026-09-28` (559 partitions) because nothing runs its producer
on a clock. Build the scheduled function that does, on the pattern IRPT_BCKEND's holdings-performance producer already runs on, prove it
reproduces the served gold, read its fire time from its inputs' real landing times, and PLAN (not apply) its root.

**The producer you package -- UNEDITED.** `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` with its declaration
`data/assets/scripts/gold/irpt_reporting/sources.json` (entry `schwab_08335338`), CLI `--date | --start/--end`, `--accounts`, `--upload`,
`--dry-run`, `--thresholds-in` (read `main()` near line 1700). Never edit it: it is packaged through `staged_from` pins, exactly as
`irpt-holdings-performance-lambda` packages its producer.

**The pattern (read, never write).** `infra/aws/terraform/investor-reporting/holdings-performance/` (`main.tf` state key + provider;
`lambda.tf` the `yang-lambda` module with `artifact_key "investor-reporting/<name>.zip"` and the existing `irpt-performance-native-layer`
for pandas/pyarrow; `iam.tf` least privilege; `schedule.tf` an EventBridge Scheduler with its own role, `schedule_expression_timezone`
named; `locals.tf` registry-derived, its line-37 filter in the form `try(v.master, null) != null`), the handler
`infra/aws/lambda/investor-reporting/holdings-performance/handler.py`, and the `lambda-source-map.json` entry
`irpt-holdings-performance-lambda` (`source_dir`, `files`, `staged_from`). For NAMING read the nearer pattern, DB-b-2's
`infra/aws/terraform/investor-reporting/reporting-publish/` (its `opal_name` module calls; the source-map key is the SCOPE-LESS builder
name because the commit-time naming gate refuses a new hand-kept `49f` token in the map or in typed Terraform text).

**Names (builder output at the cut, rule 30):** function `irpt-49f-reporting-gold-lambda`, role `irpt-49f-reporting-gold-role`, policy
`irpt-49f-reporting-gold-policy`, schedule `irpt-49f-reporting-gold-daily` (each `name("irpt","49financial","reporting-gold",<kind>)`,
derived in Terraform through `opal_name`, never typed); source-map key and artifact `irpt-reporting-gold-lambda` /
`investor-reporting/irpt-reporting-gold-lambda.zip` (`name("irpt", None, "reporting-gold", "lambda")`).

**What you build.**
- `infra/aws/lambda/investor-reporting/reporting-gold/handler.py`: the Lambda entry. On each fire: resolve T-1 with `lib/trading_calendar.py`
  (on a non-trading day log one line and return); list the gold's newest landed `date=` partition; run the producer for EVERY trading
  day after it through T-1, at most 10 days per fire (the first fire catches up 2026-09-29 onward); upload; print per day the rows
  written. A `--local --date D --out <file>` path runs the same code with no upload and writes the day's rows to a local parquet file.
  Unit tests beside it (`tests/`) for the day selection (a holiday, a weekend, a gap of three days, the 10-day bound).
- `infra/aws/terraform/investor-reporting/reporting-gold/` (own state key `investor-reporting/reporting-gold/tfstate`): NEW resources
  only -- the function, its role (READ the three Schwab silver prefixes and the holdings-performance gold prefix; READ and WRITE ONLY the
  `account_return_daily` gold prefix; no delete; own logs), the schedule with its own role at the time you READ (next bullet), timezone
  `America/New_York`, Monday to Friday, the reason stated beside it as `holdings-performance/schedule.tf` does. Register the function in
  `lambda-source-map.json` (a new entry shaped like `irpt-holdings-performance-lambda`, keyed `irpt-reporting-gold-lambda`) and run
  `infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-reporting-gold-lambda` so the plan reads an artifact; restore any
  tracked file the build deletes (`git status` after it). `terraform init` + `terraform plan -lock=false -no-color` saved VERBATIM to
  `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/reporting-gold.plan.txt`. NO APPLY.
- **The fire time, read, never guessed:** for each input, list its `date=` partitions' object `LastModified` over at least the last 10
  trading days and convert to America/New_York (s3api renders UTC): `s3://opal-data-assets/schwab/08335338/silver/fact_trn/`,
  `.../silver/dim_position/`, `.../silver/dim_balance/`, and the guard's
  `lib.opal_naming.address("irpt","49financial","gold","holdings_performance_daily","date=<D>")` (its producer fires 07:30 ET Monday to
  Friday). Choose the earliest whole minute at or after the latest landing seen plus a margin of at least 10 minutes, strictly before the
  publisher's 08:15 ET. Write `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/REPORTING_GOLD_FIRE_TIME_R3.json`:
  `{"inputs": [{"name", "bucket", "prefix", "days_measured", "latest_landing_et": "HH:MM", "landings": [{"date", "landed_et"}]}],
  "timezone": "America/New_York", "chosen_et": "HH:MM", "chosen_cron": "cron(M H ? * MON-FRI *)", "margin_minutes": n,
  "publisher_et": "08:15"}`. If no such minute exists (an input lands after 08:05 ET on any measured day), STOP that limb: it is a row
  naming the input and the days, never a later publisher time chosen here.
- ISSUER AMENDMENT 1 (2026-10-02 ~07:4xZ, ruling row IRPT_DASHBD-W1-S6). The stop fired as written and was right to. Ruled: (a) a
  partition's landing is the FIRST version's `LastModified` (its scheduled write); a later rewrite (the 2026-09-28
  `holdings_performance_daily` rewritten 2026-09-29 10:45 ET by a catch-up act, first version 07:30:21) is not a landing; (b) ONE
  day is set aside as a known incident, cited in the record: Schwab silver `dim_position` and `dim_balance` for 2026-09-29, landed
  2026-09-30 17:46 ET (the late 09-29 silver landing: IRPT_BCKEND row S235, parked order TO-IB-pr-274); (c) the handler's no-gap
  stop makes such a day safe -- it emits nothing and the next fire catches up -- so the schedule is set by the normal pattern. Write
  the record with an `excluded` list (input, partition, landed, reason) and `latest_landing_et` over the rest, choose by the order's
  own rule (expected 07:41 ET: 07:30:21 plus the 10-minute margin, the next whole minute), write `chosen_cron`, re-plan (the
  schedule and its role join the plan), re-run the three criteria. No criterion changes.
- **The one local run:** the handler's `--local --date 2026-09-28 --out
  org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/reporting_gold_local_20260928.parquet` against the REAL inputs
  (reads only; no upload).

<criterion id="DB-7-AC1" cell_refs="DB-b-7"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r3/p3_7_ac1_fire_time_record.py" .</invocation><expect>DB-7-AC1 PASS</expect></criterion>
`DB-7-AC1` -- the fire-time record carries the four inputs, each with at least 10 measured landings; the chosen time is at or after the
latest landing plus a margin of at least 10 minutes and before 08:15 ET; the cron encodes it Monday to Friday. Base: FAIL (no record).

<criterion id="DB-7-AC2" cell_refs="DB-b-7"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r3/p3_7_ac2_local_run_equals_served.py" .</invocation><expect>DB-7-AC2 PASS</expect></criterion>
`DB-7-AC2` -- the seam with the real neighbour: the packaged handler's local run for 2026-09-28 reproduces the served partition row for
row on account, date, value, external flow, daily return, basis and day quality. Base: FAIL (no local output).

<criterion id="DB-7-AC3" cell_refs="DB-b-7"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r3/p3_7_ac3_plan.py" .</invocation><expect>DB-7-AC3 PASS</expect></criterion>
`DB-7-AC3` -- the saved plan creates `irpt-49f-reporting-gold-lambda` and a schedule at the record's cron in America/New_York, with 0
change and 0 destroy. Base: FAIL (no plan).

<expected_criteria>DB-7-AC1,DB-7-AC2,DB-7-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **AWS writes admitted:** the artifact upload `investor-reporting/irpt-reporting-gold-lambda.zip` only. Reads of the four input
  prefixes and the gold. NO gold write, NO `terraform apply`, no vendor call.
- **Refusal clause.** A builder refusal stops that limb with a row; an input with no landing-time pattern stops the fire-time limb with
  a row; never a typed name and never a guessed time.

<paths>
infra/aws/lambda/investor-reporting/reporting-gold/
infra/aws/terraform/investor-reporting/reporting-gold/
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r3/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `data/assets/scripts/gold/irpt_reporting/`, `infra/aws/terraform/investor-reporting/holdings-performance/`,
`infra/aws/terraform/investor-reporting/reporting-publish/`, `infra/aws/lambda/investor-reporting/holdings-performance/`,
`infra/aws/terraform/modules/`, `infra/aws/lambda/ci/build-and-upload.sh`, `lib/`, `infra/logic/registry/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 3 (round 3, workstream B), cell `DB-b-7`.
<owned_cells>DB-b-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB-7-AC1, DB-7-AC2, DB-7-AC3. Instance at `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/IRPT_DASHBD.TO-DB-b-7.reporting-gold-scheduled-fire.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DB-7-AC1,DB-7-AC2,DB-7-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hashes, each criterion's last line, the chosen fire time with the latest landing per input,
the plan's `Plan:` line, the artifact's sha256, and any surprise row id (`IRPT_DASHBD-W1-S<k>`, k >= 6).

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- denominator: 2 schedules read in infra/aws/terraform/investor-reporting/holdings-performance/schedule.tf (49F cron(30 7 ? * MON-FRI *) America/New_York; Inflection cron(0 14 ? * MON-FRI *) UTC) plus the planned, unapplied publisher at 08:15 America/New_York; the NEW schedule sits between the 07:30 producer and the 08:15 publisher at a time the cell MEASURES; not applied here.
comp-iam: RUN -- the NEW role mirrors holdings-performance/iam.tf: read 4 input prefixes, read+write 1 gold prefix, no delete; 0 existing roles or policies touched.
comp-blast: RUN -- 0 written keys at the cut (the gold writes begin only at the issuer's apply); 0 readers move.
comp-routes: DECLARED-NOT-APPLICABLE -- no route.
comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- DB-7-AC1 base FAIL (no record), DB-7-AC2 base FAIL (no local output), DB-7-AC3 base FAIL (no plan), each dry-run at the base 2026-10-02 ~06:5xZ.
lane: the <paths> block IS the grant.
</preflight>

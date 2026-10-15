# TO IRPT_DASHBD.TO-DB-c-1 -- the COTTONWOOD Black Diamond silver LANDING TIMES of the last 15 trading days, the gold FRONTIER and the CATCH-UP set; a read, counts, times and dates only; nothing written

<to_id>IRPT_DASHBD.TO-DB-c-1</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~401</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>114</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (B-CW is this workstream) | **Rows:** IRPT_DASHBD-D2-W401-S<k> | **Decomp cell:** `DB-c-1` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 1) | **outcome_ref:** FWD-2, FWD-11 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-401`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~401/`. Never push. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row or your report; an account number, a client or household id, a name or a figure is never recorded. A raw `aws s3` or `aws s3api` listing in a shell call is denied by the repo's rail; do every S3 read from a short Python script (boto3, your own identity, LIST and HEAD only) kept in your private folder and not committed.

**Why.** The Cottonwood `holdings_performance_daily` gold has no scheduled producer and is 12 trading days behind its input (`deliverables/0.9.0_WK_IRPT_DASHBD~178/RD_COTTONWOOD_PRODUCER_R110.json`, measured 2026-10-14): ONE landing was measured, and a schedule needs more than one. This cell measures when the input lands on each of the last 15 trading days, so the schedule's time is read from data and not guessed, and lists the dates that have an input and no gold, so the catch-up run's keys are counted and not predicted. It changes nothing.

**The cell (`DB-c-1`).**
1. **Silver.** Bucket `opal-data-assets`, prefix `blackdiamond/cottonwood/silver/fact_holdings/`, partitions `date=YYYY-MM-DD/`. Record `partition_count` (a LIST of the common prefixes, paginated, counted client side) and `newest_date`.
2. **Landings.** Take the last 15 trading days up to and including `newest_date` from `lib/trading_calendar.py` (`trading_days_between(newest_date - 60 days, newest_date)`, the last 15 of the result, ascending). For each, `landing_utc` is the LATEST `LastModified` among the objects under that date's partition, formatted `YYYY-MM-DDTHH:MM:SSZ`; `landing_et` is that instant in `America/New_York` formatted `YYYY-MM-DDTHH:MM`; `after_0600_et` is true when the New York hour is 6 or later. `latest_landing_et_time` is the greatest `HH:MM` among the 15 `landing_et` values.
3. **Proposed time.** `proposed_fire_time_et` is `HH:MM`, strictly after `latest_landing_et_time`, with the margin you chose stated in `basis_words` (say what the 15 landings show: earliest, latest, how many fall at or after 06:00 New York, and whether any partition's landing date is not the day after its partition date). Do NOT claim the 6 AM fold's meaning: report only the count at or after 06:00. This is a proposal for the CTO's half, not a setting.
4. **Gold.** The Cottonwood gold tables are at `lib/opal_naming.py address("irpt","cottonwood","gold",<table>,"date=2000-01-03")` with the partition tail cut (the bucket is `opal-data-cottonwood`). For `holdings_performance_daily` record `newest_date` (the greatest `date=` partition); for `account_return_daily` record its `newest_date` the same way.
5. **Catch-up set.** `catch_up.dates` is every silver partition date that is a trading day per `lib/trading_calendar.py is_trading_day` and has NO `date=` partition in the `holdings_performance_daily` gold, ascending; `catch_up.count` its length; `catch_up.calendar_source` the string `lib.trading_calendar.calendar_source()` returns. If the set holds a date far before the others, say in `catch_up.notes` (words) what you can see in the repo about why it has no gold (for example that the first silver day has no prior day); never guess.
6. **Record** `LANDING_AND_FRONTIER_R114.json` in your folder with exactly: `claim` ("measured"); `silver` {`bucket`, `prefix`, `partition_count`, `newest_date`, `claim`}; `landings` (the 15 objects `{date, landing_utc, landing_et, after_0600_et}`); `latest_landing_et_time`; `proposed_fire_time_et`; `basis_words`; `gold` {`holdings_performance_daily` {`newest_date`}, `account_return_daily` {`newest_date`}}; `catch_up` {`dates`, `count`, `calendar_source`, `notes`}; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0, `s3_reads` (integer)}; `files_in_repo_private` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, dates, times, paths and words only.

<criterion id="DBC114-1-AC1" cell_refs="DB-c-1"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r114/p114_bcw.py" . DBC114-1-AC1</invocation><expect>DBC114-1-AC1 PASS</expect></criterion>
`DBC114-1-AC1` -- the record is complete; the 15 dates are the library calendar's last 15 trading days to the recorded newest silver date; each `landing_et` and `after_0600_et` is recomputed from `landing_utc`; each `landing_utc` equals a fresh read of that partition's latest object time; `partition_count` equals a fresh LIST; the gold `newest_date` equals a fresh LIST; the catch-up set equals silver trading days minus gold partitions; the proposed time is later than the latest landing; no write is recorded. Base: FAIL (no record).

<expected_criteria>DBC114-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the checker, every contract and every other issuer's file.
- **Reads and writes.** Reads: repo files; S3 LIST and HEAD under `s3://opal-data-assets/blackdiamond/cottonwood/silver/fact_holdings/` and under the two Cottonwood gold prefixes in `opal-data-cottonwood` ONLY. Writes: the record in your folder and your private folder. No write to AWS of any kind, no deploy, no push, no vendor call, no secret read, no read of any other firm's place.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A listing you cannot make is named in `basis_words` with the error. Never run the producer, never write a day.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W401-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~401/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-1.cottonwood-silver-landing-times-gold-frontier-and-catch-up-set.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 1, cell `DB-c-1`.
<owned_cells>DB-c-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC114-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~401/IRPT_DASHBD.TO-DB-c-1.cottonwood-silver-landing-times-gold-frontier-and-catch-up-set.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC114-1-AC1` BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the earliest and latest landing in New York time and the count at or after 06:00; the proposed time; the gold newest date for each table; the catch-up count and its first and last date; the number of S3 reads; row ids. No account number, client or household id, name or figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read record; nothing is read by served code, wired or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: read-only S3 LIST and HEAD of the Cottonwood-scoped Black Diamond silver and gold prefixes; no new principal or grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the order MEASURES landing times and proposes a time; it changes no schedule.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBC114-1-AC1 FAILS at base (no record) and its fresh-LIST recount arms are exercised on the worker's record.
</preflight>

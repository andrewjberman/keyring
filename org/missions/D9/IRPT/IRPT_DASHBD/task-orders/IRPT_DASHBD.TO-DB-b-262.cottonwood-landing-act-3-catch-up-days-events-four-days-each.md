# TO IRPT_DASHBD.TO-DB-b-262 -- ACT 3 of the signed Cottonwood landing pair (packet revision 3, sha256 `31f8e1620b90`): the catch-up as explicit `days` events of AT MOST FOUR trading days each, one synchronous invocation and one after-read per event, the schedule left DISABLED, the ledger left OPEN (CTO half signed @d80e4d3f61, Act 2 passing)

<to_id>IRPT_DASHBD.TO-DB-b-262</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.7.0_AE_CloudOps~DB2</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>130</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed pair, COO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_COTTONWOOD_ACCOUNT_RETURN_DAILY_LANDING_COO_HALF.md`, CTO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_COTTONWOOD_ACCOUNT_RETURN_DAILY_LANDING_R3_CTO_HALF.md` (both at packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_PACKET_COTTONWOOD_ACCOUNT_RETURN_DAILY_LANDING.md`, sha256 `31f8e1620b90bdf041729c623239d5c4c96ccd8781e7ce48af401e900dea06b7`; packet section 1 Act 3 and the CTO's answer 1: "Act 3 only after Act 2's after-read, at most 25 days per event") | **Decomp cell:** `DB-b-262` (decomposition section 128) | **outcome_ref:** FWD-11, FWD-21 | **depends_on:** `DB-b-260` (Act 1 and Act 2 complete and passing).

---

## WORKER FACE

Your worktree is the absolute path your seat uses for IRPT_DASHBD (a linked worktree cut from the current `box/dell2`, FULL checkout, carrying your Act 2 record and the issuer's checkers); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/`. Never push. **A STOP is reported to the issuer at once and writes nothing further.** No client data is read or recorded: counts, dates, keys, hashes and words only.

**What this order does, in one paragraph.** Act 2 landed the one day 2026-07-10 into the Cottonwood gold prefix (peak 633 MB, 118 s in the Lambda). This order lands every later day for which Black Diamond silver holds BOTH tables, oldest first, up to the newest such day at the moment you read the silver, as a series of explicit `days` events to the function `irpt-cot-account-return-daily-lambda`. **Why four days an event, not 25:** the packet's 25 came from a local 22 s measurement; the Lambda measured 118 s for one day against a 900 s timeout, so an event of more than 7 days could time out mid-write. A timeout between a day's two puts leaves a data object without its manifest, which the guard then refuses to re-run, and only Andrew's listed-key delete clears it. Four days (about 8 minutes) keep each event well under the timeout. You enable NOTHING and change NOTHING else.

**Read first (all in your worktree):** the packet (sections 1, 5, 6, 8), the CTO half R3, your own Act 2 record `COT_LANDING_APPLY_RECORD.json`, and the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r129/p129_cotcatchup.py` (the record's exact form and every clause are in it). Handler: `infra/aws/lambda/investor-reporting/account-return-daily/handler.py` (the `days` event, the floor, the 25-day limit, the held days).

**Do, in this order. Record every value named in `COT_CATCHUP_RECORD.json` as you go.**

0. **Gates, read only.** (a) The packet's sha256 equals `31f8e1620b90bdf041729c623239d5c4c96ccd8781e7ce48af401e900dea06b7` and both halves read SIGNED at it. (b) Your Act 2 record passes `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r128/p128_cotapply.py" . DBC128-1-AC1`, `DBC128-2-AC1` and `DBC128-3-AC1` (`gates.act2_recorded_and_passing`). (c) **One change at a time:** the only open marker naming this surface is your own ledger `irpt-dashbd-cottonwood-account-return-daily-20261015` (read every live worktree's `.open_deploys/`, print the denominator, record `worktrees_read` and `open_markers_naming_this_surface` 1). (d) Live: the function reads memory 1024, timeout 900, the schedule `irpt-cot-account-return-daily-daily` is DISABLED, the gold prefix holds 3,325 history partitions to 2026-06-22 and the one partition 2026-07-10. Any difference is a STOP.
1. **The day list, from a fresh recount.** List the Black Diamond silver tables `fact_allocations` and `fact_transactions` under `blackdiamond/cottonwood/silver/` in `opal-data-assets` (LIST only) and take the days that have BOTH tables, strictly after 2026-07-10, ascending. Today that is 64 days up to 2026-10-14 (2026-08-19, 2026-09-24 and 2026-09-25 have no silver pair and are not named; the handler would return them held). Cut that list, in order, into events of at most FOUR consecutive entries (the last one may be shorter). Name no other day, never a day at or before 2026-07-10.
2. **For each event, in order, ONE synchronous invocation:** `aws lambda invoke --function-name irpt-cot-account-return-daily-lambda --invocation-type RequestResponse --log-type Tail --cli-read-timeout 0 --cli-connect-timeout 60 --payload fileb://<file holding {"days": [...]}> <out file>` (the `--cli-read-timeout 0` keeps the client waiting for the response: the default 60 s read timeout lost the Act 2 response). **One invocation per event; if one errors or the client loses the response, do NOT retry it: read the Lambda side (the log group, the REPORT line for that request) and the gold LIST for the named days, record what is true, and STOP unless every named day holds exactly its two objects and the REPORT line shows no error.** Record each event as `events[i]` {`payload` {`days`}, `invoked_utc`, `invocation_type` "RequestResponse", `status_code`, `function_error` (null when none), `returned` (the response body's `ok`, `days`, `held`), `report` {`max_memory_used_mb`, `duration_ms`, `memory_size_mb`} (from the tail's REPORT line), `over_threshold` (true when Max Memory Used exceeds 717 MB), `request_id`}. **After each event, before the next:** a fresh LIST of the gold prefix: each named day holds exactly `data.parquet` and `manifest.json`, nothing at or before 2026-06-22 moved.
3. **STOP at once, running no further event, and report,** on any of: a function error; any held day in the returned body; Max Memory Used over 717 MB; Duration over 700 seconds; a named day without exactly its two objects (a half partition: do not delete, do not re-run); any history key modified; any throttle you cannot account for.
4. **When the last event's after-read passes:** record `partitions_after` {`new_days` (the partitions after history, counted by a fresh LIST: the named days plus 2026-07-10), `last_day`, `history_partitions` 3325}. **Do NOT close the ledger, do NOT enable the schedule, run NO other event.**

Write `COT_CATCHUP_RECORD.json` in your folder with exactly: `claim` ("measured"); `gates` {`packet_sha256`, `act2_recorded_and_passing`, `one_change_at_a_time` {`worktrees_read`, `open_markers_naming_this_surface`}}; `ledger_entry` ("irpt-dashbd-cottonwood-account-return-daily-20261015"); `events` (the list of step 2); `partitions_after`; `ledger_closed` false; `reads` {`vendor_calls` 0, `secret_reads` 0}. Counts, dates, keys, hashes and words only.

<criterion id="DBD129-1-AC1" cell_refs="DB-b-262"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r129/p129_cotcatchup.py" . DBD129-1-AC1</invocation><expect>DBD129-1-AC1 PASS</expect></criterion>
`DBD129-1-AC1` -- the record has exactly the form above; its events name exactly the silver days after 2026-07-10 (a fresh recount of both tables) up to the last day named, in ascending order with no day skipped and no day at or before 2026-07-10, at most four days an event; every event is synchronous with nothing held, no function error, Max Memory Used at or under 717 MB and Duration under 700 s; Act 2's record passes; the ledger is the open one. Base: FAIL (no record).
<criterion id="DBD129-2-AC1" cell_refs="DB-b-262"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r129/p129_cotcatchup.py" . DBD129-2-AC1</invocation><expect>DBD129-2-AC1 PASS</expect></criterion>
`DBD129-2-AC1` -- FRESH reads by the checker: 2026-07-10 and every named day hold exactly their two objects; the history still reads 3,325 partitions to 2026-06-22; the function (memory 1024, timeout 900) and the schedule (DISABLED, the packet's cron and zone) are unchanged; a REPORT line in the log group equals each recorded event. Base: FAIL (no record).

<expected_criteria>DBD129-1-AC1, DBD129-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **The signed act, and nothing wider.** Writes to AWS: the `days` invocations of Act 3 (each writes the two objects of each named day under `irpt/cottonwood/gold/account_return_daily/date=<day>/`, nothing existing replaced: the guard refuses). **NO day at or before 2026-07-10; NO event of more than four days; NO second invoke of an event; NO enable of the schedule; NO change to the function, the roles or the schedule; NO deletion of any object or file; NO `update-function-code`; NO bare `terraform apply`.** A half partition is removed only by an explicit listed-key delete with Andrew's word, never by you.
- **Read-only:** `get-function-configuration`, scheduler `get-schedule`, S3 list and head of the gold prefix and the silver tables, `logs filter-log-events`, CloudWatch `get-metric-statistics`.
- **Refusal clause.** STOP and report, writing nothing further, on any step 3 condition, on the packet or a half differing, or on Act 2's record not passing.
- **Row ids** are `IRPT_DASHBD-D2-DB2-S<k>` (the next free `k`); file a row for anything odd and keep working. Commit with `.tools/safe-commit.sh`. ASCII only. **Report once, under 150 words; report each STOP at once.**

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-262.cottonwood-landing-act-3-catch-up-days-events-four-days-each.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 128 (round 130, workstream B-49F), cell `DB-b-262`.
<owned_cells>DB-b-262</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBD129-1-AC1, DBD129-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/IRPT_DASHBD.TO-DB-b-262.cottonwood-landing-act-3-catch-up-days-events-four-days-each.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBD129-1-AC1,DBD129-2-AC1` BEFORE any flip; pin each artifact row to the commit that carried it. Run each criterion under `timeout 300` from the repository root and record the output and exit code verbatim.
</proof_of_spec>

**REPORT:** once, under 150 words: the two criteria's last lines; the number of events and days landed; the slowest event's duration and the highest Max Memory Used; any STOP; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: no resource is created, changed or deleted; each event adds new partitions in an occupied prefix and replaces nothing (the guard). The blast radius is the signed pair's, read by both halves.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed; the function's existing execution policy is read back by the Act 2 criteria and unchanged here.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched; no served page changes (the new partitions have no established reader).
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the schedule stays DISABLED and is not enabled by this order; the criteria read its state.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the two criteria FAIL at base (no record) and recount from fresh S3, Lambda, scheduler and log reads; the record clauses are exercised by the checker's self-test (one green and 25 red arms).
</preflight>

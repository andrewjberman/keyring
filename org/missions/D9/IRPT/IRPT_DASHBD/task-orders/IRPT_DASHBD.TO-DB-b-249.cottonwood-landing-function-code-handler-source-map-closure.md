# TO IRPT_DASHBD.TO-DB-b-249 -- the COTTONWOOD LANDING FUNCTION CODE (round 122, workstream B-49F): a Lambda handler that runs the round-121 adapter's `run_day` for the Cottonwood account return (an explicit day or days, or the days owed through T-1), its new source-map entry and the complete zip closure it needs, tested LOCAL with fake clients and proved by a STAGED probe that runs the handler from only its packaged members; the Terraform root, schedule and pair are the next round; nothing planned, applied, scheduled or deployed

<to_id>IRPT_DASHBD.TO-DB-b-249</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~203</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>122</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 122 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-122 ANALYSIS (B-49F) section 2 ruling 4 and section 3 cell 4 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_122_20261015.md @e690365741`: "The Cottonwood adapter's landing pair is cut next round with a `*-cot-*` role and builder names") and the round-121 drain-end packet's list of what a landing still needs ("a handler wiring `run_day` to a real S3 client, a source-map row and a zip closure") | **Rows:** IRPT_DASHBD-D2-W203-S<k> | **Decomp cell:** `DB-b-249` (decomposition section 120) | **outcome_ref:** FWD-11, FWD-21 | **depends_on:** none (the Terraform root, which names this function's bundle, is cut after this lands)

**Risk class WORLD** is the floor of the paths below (an `infra/` path): this order writes handler code, a source-map entry and tests and runs no AWS call and no Terraform command.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-203` (branch `wk-IRPT_DASHBD-203`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~203/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~203/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** Round 121 built the Cottonwood Black Diamond adapter's landing path (`data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py`: `run_day(reader, s3, day, upload=True)`, `presence_hold`, `write_day`, `gold_prefix`, `_find_root`). Nothing yet calls it from a Lambda. The landing facts of round 120 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~195/RD_CW_LANDING_FACTS_R120.json`) name the function `irpt-cot-account-return-daily-lambda`, the shape (a Lambda on the holdings-performance cot pattern) and the schedule (`cron(15 8 ? * MON-FRI *)` New York, created DISABLED, a hold if T-1's silver is absent). This cell writes the function CODE and its bundle declaration so that the next round's Terraform root has something to deploy. The unknown it must settle is the ZIP CLOSURE: which repo files the handler needs at run time (the adapter, `lib/opal_naming.py`, `lib/trading_calendar.py`, the naming registry and schema), proved by running the handler from a directory holding only those files.

**The cell (`DB-b-249`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r122/p122_cothandler.py` (your three criteria; its `PROBE` text IS the behaviour spec and its `stage_closure` shows how the entry is staged); the adapter and its tests; the gold handler `infra/aws/lambda/investor-reporting/reporting-gold/handler.py` (its guarded imports, `_ROOT` resolution, `select_days`, `newest_landed_day`, `lambda_handler`: copy the style); the source map `infra/aws/lambda/ci/lambda-source-map.json` (the entry `irpt-49f-reporting-gold-lambda`: its keys, `files`, `staged_from` with `repo_path`, `pin`, `packaged_as`, `sha256`, and the notes); the landing facts above; `lib/opal_naming.py` (what files it reads at import and at call: the registry and the schema).
2. **The handler** `infra/aws/lambda/investor-reporting/account-return-daily/handler.py` (new). Top-level `handler.py` of the bundle; it puts `<bundle root>/data/assets/scripts/gold/irpt_reporting/adapters` on `sys.path` and imports the adapter and `trading_calendar` the way the gold handler imports its producers (the adapter's `_find_root` finds the bundle root). Exact names and signatures, because the checker calls them in a clean interpreter from the staged directory:
   - `MAX_DAYS_PER_FIRE = 5` (an integer from 1 to 10) and `MAX_BACKFILL_DAYS = 25`.
   - `newest_landed_day(s3, bucket, key_prefix)`: the newest `date=` partition under the gold prefix by `list_objects_v2` with `Delimiter="/"` and pagination, else None.
   - `owed_days(newest_landed, today, max_days=MAX_DAYS_PER_FIRE)`: T-1 is `tc.prev_trading_day(today)`; with nothing landed it owes exactly `[T-1]` (never an implicit backfill); otherwise the trading days AFTER `newest_landed` through T-1, oldest first, at most `max_days`. Examples the checker asserts: newest 2026-07-10 on 2026-07-15 owes 2026-07-13 and 2026-07-14; newest 2026-07-10 on Saturday 2026-07-11 owes none; newest 2026-06-01 on 2026-07-15 owes five days.
   - `lambda_handler(event, context=None, s3=None, reader=None)`: `s3` and `reader` default to a boto3 S3 client and `CottonwoodBlackDiamondSilverReader()` (injectable for tests). Event `{"day": "YYYY-MM-DD"}` runs that day; `{"days": [...]}` runs those days, in the order given; no day key runs `owed_days(newest_landed_day(...), today in America/New_York)` where the gold prefix is `gold_prefix()`; `{"dry_run": true}` passes `upload=False`. A day that is not a real ISO date raises BEFORE any write; more than `MAX_BACKFILL_DAYS` days in one event raises (`SystemExit`) BEFORE any write. Each day goes through the adapter's `run_day`; a held day is logged as `HOLD <day>: <reason>` and counts as held; the return is `{"ok": True, "days": [...], "results": {day: run_day's dict}, "held": <count of held days>}`. It touches no other S3 prefix and no other firm.
3. **The source-map entry** in `infra/aws/lambda/ci/lambda-source-map.json` under `functions`, key `irpt-cot-account-return-daily-lambda` (the builder-derived function name of the landing facts): `source_dir` `infra/aws/lambda/investor-reporting/account-return-daily`, `files`, `staged_from` (one object per member: `repo_path`, `pin` null, `packaged_as` equal to `repo_path`, `sha256` null: the applier writes pins and hashes), and the other keys of the sibling entry as far as they apply (`pipeline` "investor-reporting"; `artifact_s3_key` `investor-reporting/irpt-cot-account-return-daily-lambda.zip`; the Terraform fields `tf_file`, `tf_resource` and `iam_role` as null with a `_note` that the Terraform root is cut after this cell). The ONLY change to the file is this new entry (the checker requires the file to lose no line). The members are the COMPLETE closure: find it by running the staged probe yourself until it passes; the checker lists the members you declare and nothing else, so a missing registry file or schema fails the probe.
4. **Tests** `infra/aws/lambda/investor-reporting/account-return-daily/tests/test_handler.py`, at least 8, no network, fake clients: `owed_days` (the three examples); a full day writes two objects; `dry_run` writes nothing; a held day writes nothing and reports held; two days write four objects; a bad day raises before any write; more than 25 days raises before any write; `newest_landed_day` over a fake paginated client. Copy the import style of the gold handler's tests.
5. **The facts record** `RD_CW_HANDLER_FACTS_R122.json` in your folder with EXACTLY these fields: `handler` {`file`, `functions` (includes `lambda_handler`, `owed_days`, `newest_landed_day`), `events` (includes "day", "days", "dry_run"), `words`}; `closure` {`members` (the list of every `packaged_as` of the entry's `staged_from`, equal to it), `staged_probe_ran` (true: you ran the staged probe), `words` (how you found the closure and what each non-obvious member is for)}; `source_map` {`file`, `entry` ("irpt-cot-account-return-daily-lambda"), `pins_null` (true), `words`}; `tests` {`file`, `new_tests`}; `scheduling` {`max_days_per_fire`, `backfill_days_max` (25), `scheduled_rule` (words), `words` (how the first fire, the catch-up from 2026-04-22 by explicit `days` events and the DISABLED schedule fit together; say what the next round's Terraform must set: timeout, memory, the environment, the reserved concurrency of 1)}; `files_changed` (the handler, the test file and the source map, each {`file`, `sha256`, `kind`}); `words`; `claim`; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256`, `vintage`, `members` or `entry` field.

<criterion id="DB122-4-AC1" cell_refs="DB-b-249"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r122/p122_cothandler.py" . DB122-4-AC1</invocation><expect>DB122-4-AC1 PASS</expect></criterion>
`DB122-4-AC1` -- the handler defines `lambda_handler`, `owed_days` and `newest_landed_day`; the new test file holds at least 8 tests and `pytest` on it passes. Base: FAIL (no handler).
<criterion id="DB122-4-AC2" cell_refs="DB-b-249"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r122/p122_cothandler.py" . DB122-4-AC2</invocation><expect>DB122-4-AC2 PASS</expect></criterion>
`DB122-4-AC2` -- the STAGED probe: the checker copies the handler and every `staged_from` member of the new entry to a temporary directory by their `packaged_as` names, with no repo checkout on the path, and in a clean child interpreter finds that the handler imports from that directory; `owed_days` owes the three example sets and caps at `MAX_DAYS_PER_FIRE`; a full day writes exactly two objects, `dry_run` and a held day none, two days four; a bad day and a 30-day event raise before any write. Base: FAIL (no entry).
<criterion id="DB122-4-AC3" cell_refs="DB-b-249"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r122/p122_cothandler.py" . DB122-4-AC3</invocation><expect>DB122-4-AC3 PASS</expect></criterion>
`DB122-4-AC3` -- `RD_CW_HANDLER_FACTS_R122.json` has exactly the form of step 5, its closure members equal the entry's, its files hash as recorded and the closure carries the adapter, `opal_naming` and `trading_calendar`; in the worker's own commits the source map gains at least 15 lines and loses none, every member's pin and hash are null, and nothing else under `infra/`, `data/`, `lib/` or `org/standards/` changes outside the new function directory. Base: FAIL (no record).

<expected_criteria>DB122-4-AC1,DB122-4-AC2,DB122-4-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the adapter and its tests (a change there is a row and a stop), the gold handler, every Terraform file, `lib/`, the registry, the contract, every other source-map entry, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files. The tests and the probe use fake clients; no network, no AWS call, no S3 read or write, no Terraform command, no deploy, no push, no vendor call, no secret read. Writes: the repo files of the grant.
- **Client data.** None is involved; fixtures are synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the adapter cannot be driven by the handler without changing the adapter, or the closure cannot be completed from repo files, file a BLOCKING row naming the exact obstacle and stop on that point. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W203-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

**AMENDMENT 1 (issuer 2.0.0_SA_COO~D2, 2026-10-15, on worker row W203-S3; gate limb: a modification of an existing order, placeholders NONE, no criterion id or cell changes).** The naming gate (LGIC_ENFORCE) refuses a NEW hand-kept literal that carries a firm token, and the directory name `account-return-cot` carries `cot`. The function directory is now `infra/aws/lambda/investor-reporting/account-return-daily` everywhere in this order and in the checker (`p122_cothandler.py` `FN_DIR`); it names the function's own token and no firm. Move the handler and its tests there (`git mv`, one commit), set the entry's `source_dir` to it, refresh the facts record's paths and hashes, and keep `irpt-cot-account-return-daily-lambda` as the entry key (the builder's output, which the gate admitted). If the gate refuses any other literal of the entry, file a row with the line and stop.

<paths>
infra/aws/lambda/investor-reporting/account-return-daily/handler.py
infra/aws/lambda/investor-reporting/account-return-daily/tests/test_handler.py
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~203/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-249.cottonwood-landing-function-code-handler-source-map-closure.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 120 (round 122, workstream B-49F), cell `DB-b-249`.
<owned_cells>DB-b-249</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB122-4-AC1, DB122-4-AC2, DB122-4-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~203/IRPT_DASHBD.TO-DB-b-249.cottonwood-landing-function-code-handler-source-map-closure.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB122-4-AC1,DB122-4-AC2,DB122-4-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the handler's functions and events; the closure members by group and what each is for; the source-map entry's keys; the scheduling rule; the test counts; what the next round's Terraform root must set. Words and counts only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a new handler, its tests, one new source-map entry and a facts record in a branch; nothing is wired to AWS, scheduled, planned, applied or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written; the handler is exercised only with fake clients, and no grant is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its staged probe was validated by the issuer against a scratch reference handler with a 21-member closure (green), and the removal of one member was caught; its other clauses by its self-test.
lane: the <paths> block IS the grant.
</preflight>

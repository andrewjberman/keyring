# TO IRPT_DASHBD.TO-DB-b-294 -- the PRODUCERS DERIVE history_scope PER ACCOUNT (round 149, CTO ruling msg 9226, row D2-S113): the 49 Financial producer and the Cottonwood Black Diamond adapter write PARTIAL_HISTORY when the account's first value day equals the source floor, FULL after it, and the conditional column `history_scope_claim` = `inferred`

<to_id>IRPT_DASHBD.TO-DB-b-294</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~237</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>HSPROD</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** HSPROD, round 149 | **Ordered by:** 1.0.0_SA_CTO~DELL2, msg 9226 (row D2-S113: "account_return_daily.py:1355 writing HISTORY_PARTIAL unconditionally is a defect ... an account whose first value day equals the source floor is PARTIAL ... an account first seen after the floor is FULL ... carry history_scope_claim = inferred, with the method 'first value day vs source floor'", "in the same drain as the unreported-days writer") | **Decomp cell:** `DB-b-294` (decomposition section 155).

**Risk class WORLD** is the floor of the paths below (`infra/` path and the producers): python in a branch, no Terraform command, no AWS write, no build for upload, no run of either producer against S3, no push. The code update of the two functions, the rebuild of the gold's `history_scope` and the republish are later signed pairs and the applier's.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-237` (branch `wk-IRPT_DASHBD-237`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~237/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value. Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~237/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** Both producers write `history_scope` = `PARTIAL_HISTORY` on every row, so a page prints "Returns from <date>." on every account. The CTO ruled the constant a defect. The rule: PARTIAL_HISTORY when the account's first value day equals the SOURCE FLOOR (it existed before our data starts), FULL when it is after. It is an inference, so each derived row carries the conditional column `history_scope_claim` = `inferred` (declared by cell `DB-b-293`, source contract 0.4.6: a column outside `optional_columns`, so both schema hashes stay untouched). The source floor is the earliest balance partition the source holds.

**The cell (`DB-b-294`).** Three code edits and one test file; nothing else.
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p162_producers_scope.py` (your three criteria; `check_ard` and `check_cbd` are the exact spec of the behaviour, down to the names `table_for`, `floor_day` and `floor_values`); `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` (`HISTORY_*` constants, `compute_range` with its `first_data` and `bal_days`, `emit_day`, `ARROW_SCHEMA`, `COLUMNS`); `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py` (`derive_rows`, `derive`, `to_table`, `run_day`, `day_values`, `ARROW_SCHEMA`, `SCHEMA_WITH_SOURCE`); `infra/aws/lambda/investor-reporting/account-return-daily/handler.py` (`_run`, `FLOOR_DAY`); `data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_bd_account_return_daily.py` (its fakes are a model for yours).
2. **The 49 Financial producer (`account_return_daily.py`).** (a) Constants beside `HISTORY_SCOPE`: `HISTORY_SCOPE_CLAIM_COLUMN = "history_scope_claim"`, `HISTORY_SCOPE_CLAIM = "inferred"`, `HISTORY_SCOPE_METHOD = "first value day vs source floor"`. (b) A pure helper `_history_scope(first_day, source_floor)`: with no floor or no first day it returns `HISTORY_PARTIAL` (the old constant); otherwise `HISTORY_PARTIAL` when the first value day (ISO, first 10 characters) is on or before the floor, else `HISTORY_FULL`. (c) In `compute_range`, after `durable_inception` is set: `source_floor = min(bal_days) if (bal_days and durable_inception) else None` (the floor is the earliest balance partition; with window-local inception or no balance days nothing can be inferred). The row's `history_scope` becomes `_history_scope(first_seen.get(acct), source_floor)`, and when `source_floor` is not None the row also gets `history_scope_claim` = `inferred`; when it is None the row carries NO claim key (every row of one call is uniform). (d) A function `table_for(frame)`: when the frame has the claim column it returns the Arrow table of `COLUMNS` plus the claim column last (schema `ARROW_SCHEMA` appended with a non-null string field of that name); otherwise exactly `ARROW_SCHEMA`'s table of `COLUMNS`. `emit_day` builds its table with `table_for(frame)` and streams it with `table.schema` (not `ARROW_SCHEMA`). `ARROW_SCHEMA`, `COLUMNS` and the contract's `schema_hash` do not change. The callers (`main`, the `reporting-gold` handler) already pass `first_data` and `bal_days`: do NOT edit them.
3. **The Cottonwood adapter (`cottonwood_bd_account_return_daily.py`).** The adapter derives one landing day from the previous trading day, so it has no history of an account's first day; the floor-day partition is enough (a value on the floor day IS a first value day on the floor, nothing is earlier in the source). (a) `derive_rows(account_id, values, flows, unreconciled, days, floor_values=None)`: with `floor_values` None the rows are today's (`PARTIAL_HISTORY`, no claim); otherwise `history_scope` is `PARTIAL_HISTORY` when `floor_values.get(account_id)` is positive and `FULL` when it is not, and every row also carries `history_scope_claim` = `inferred` (module constants `CLAIM_COLUMN`, `CLAIM`). (b) `derive(reader, accounts, start, end, floor_day=None)`: when `floor_day` is given AND is among `reader.list_partitions("fact_allocations")`, read that one partition and build `floor_values` with the same `day_values` the adapter already uses; otherwise `floor_values` is None (no claim); pass it to `derive_rows`. (c) `to_table(rows, with_source=False)`: when EVERY row carries the claim, the schema gets the claim as a non-null string field APPENDED LAST (after the source label when `with_source`); otherwise it is today's. `ARROW_SCHEMA`, `SCHEMA_WITH_SOURCE`, `schema_hash()` and `schema_hash_with_optional()` do not change. (d) `run_day(reader, s3, day, upload=True, floor_day=None)` passes `floor_day` to `derive`; the manifest's `columns` is the table's own names (it already is).
4. **The landing handler (`infra/aws/lambda/investor-reporting/account-return-daily/handler.py`).** `_run` calls `cbd.run_day(reader, s3, day, upload=upload, floor_day=FLOOR_DAY)`. Nothing else in the file changes.
5. **The tests** `data/assets/scripts/gold/irpt_reporting/tests/test_history_scope_derivation.py` (new, at least 10 passing tests, self-contained: synthetic frames, caches and fake readers and writers, no AWS, no private data). They assert at least: the floor-start account is PARTIAL and a later account FULL with the claim on every row (`compute_range` driven by caches, the way the checker does); no `first_data` or no `bal_days` keeps PARTIAL with NO claim key; `_history_scope` for on-the-floor, after-the-floor, None and an ISO string with a time part; `table_for` with and without the claim (names, the string type, the 19-column schema equal to `ARROW_SCHEMA`); `emit_day` streams the right schema (monkeypatch `sp.stream_to_parquet`); the adapter's `derive_rows` for a floor value positive, zero and absent; `derive` with the floor partition present and absent; `to_table` column order with and without the source label; `run_day` end to end on a fake reader and writer (21 columns derived, 20 legacy); both schema hashes unchanged against the contract; the handler passes `FLOOR_DAY`.
6. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p162_producers_scope.py" . DB162-1-AC1`, then AC2, then AC3 (AC3 runs the whole gold tests directory, about twenty seconds, and the landing handler's tests). One test in the gold directory, `test_account_activity_lots.py::test_the_calendar_itself_raises_before_2010_and_the_index_never_asks_it`, was red BEFORE your edit and is outside this cell; the checker deselects it; do not touch it.
7. **Record** `RD_HISTSCOPE_PRODUCERS_FACTS_R149.json` in your folder with EXACTLY these fields: `claim_column` ("history_scope_claim"); `claim_value` ("inferred"); `method` ("first value day vs source floor"); `producers` (["account_return_daily.py", "cottonwood_bd_account_return_daily.py"]); `legacy_without_floor` (true: a caller that cannot name the floor keeps the old constant and writes no claim); `tests` (the count of passing tests of your new file); `words` (one paragraph, 80 to 1800 characters: what changed and why, that no schema constant or hash moved, and what is NOT proven: neither producer ran against S3, no gold partition was rewritten, the Cottonwood landing refuses to overwrite a partition that already holds objects so a rebuild of landed days is a separate act, and the Inflection adapters still write the constant).

<criterion id="DB162-1-AC1" cell_refs="DB-b-294"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p162_producers_scope.py" . DB162-1-AC1</invocation><expect>DB162-1-AC1 PASS</expect></criterion>
`DB162-1-AC1` -- the 49 Financial producer derives history_scope per account against the source floor (the earliest balance partition): the floor-start account is PARTIAL_HISTORY, accounts first seen after it FULL, every row of a derived call carries history_scope_claim = inferred; with window-local inception or no balance days the old constant and NO claim; `table_for` and `emit_day` write the 19 columns plus the claim only when the frame has it; the 19-column schema and its contract hash are untouched. Base: FAIL.
<criterion id="DB162-1-AC2" cell_refs="DB-b-294"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p162_producers_scope.py" . DB162-1-AC2</invocation><expect>DB162-1-AC2 PASS</expect></criterion>
`DB162-1-AC2` -- the Cottonwood adapter derives history_scope from the floor-day partition (a value on the floor day is PARTIAL_HISTORY, none is FULL) and writes 19 columns, the source label, then the claim; with no floor day or no floor partition the old 20-column table and NO claim; its schema constants and its 0.3.0 hash are untouched; a day landed through the handler carries the derived scope. Base: FAIL.
<criterion id="DB162-1-AC3" cell_refs="DB-b-294"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p162_producers_scope.py" . DB162-1-AC3</invocation><expect>DB162-1-AC3 PASS</expect></criterion>
`DB162-1-AC3` -- the new test file holds at least 10 passing tests; the whole gold tests directory (the one known pre-existing red deselected) and the landing handler's tests pass; the worker's commits change only the two producers, the landing handler, the new test file, the folder, the investigation file and task-order files; the facts record equals the checker's recount. Base: FAIL.

<expected_criteria>DB162-1-AC1,DB162-1-AC2,DB162-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the contracts, the publisher, the publish handlers, the `reporting-gold` handler, the Inflection adapters, the source map, the portal, the issuer's check files.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no run of a producer against S3, no deploy, no push. Writes: the repo files of the grant and your private folder.
- **Client data.** None is involved; fixtures are synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W237-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements). Write files with LF line endings (write bytes).

<paths>
data/assets/scripts/gold/irpt_reporting/account_return_daily.py
data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py
data/assets/scripts/gold/irpt_reporting/tests/test_history_scope_derivation.py
infra/aws/lambda/investor-reporting/account-return-daily/handler.py
infra/aws/lambda/investor-reporting/account-return-daily/tests/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~237/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-294.producers-derive-history-scope.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 155 (round 149, workstream HSPROD), cell `DB-b-294`.
<owned_cells>DB-b-294</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB162-1-AC1, DB162-1-AC2, DB162-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~237/IRPT_DASHBD.TO-DB-b-294.producers-derive-history-scope.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB162-1-AC1,DB162-1-AC2,DB162-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the changed functions in one line per file; the test count; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: python in a branch; neither producer is run against S3 and nothing is deployed, so no served output moves; the gold rebuild and the republish are later signed pairs.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS is read or written and no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the behaviour clauses were validated by the issuer against a scratch reference of the three edits (green: AC1, AC2, the whole gold tests directory and the landing handler's tests) and 14 single-fault mutants (all red).
lane: the <paths> block IS the grant.
</preflight>

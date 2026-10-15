# TO IRPT_DASHBD.TO-DB-i-11 -- the SCOPE FEED RUN WRAPPER: feed silver partitions (frames) and the dimension frame in, contract-0.4.0 parquet partitions, an ABSENT-records file and a run record out; the complete-day rule, a repeated-key refusal, a 299-day chain fixture; fixtures only, nothing to AWS

<to_id>IRPT_DASHBD.TO-DB-i-11</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~311</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>124</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_118_20261015.md` ADDENDUM 5 (msg 8584) and ADDENDUM 6 (msg 8605, item 1 and the W310-S2 carry).

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-311`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~311/`. Never touch a path outside the `<paths>` block below.

**Why.** Round 123 built `adapt()`, a pure function from feed rows to contract-0.4.0 rows. Something must feed it silver partitions, hand it the account map from the dimension, refuse a bad feed, and write the result in the contract's shape. This wrapper is that step. It runs on pandas frames handed to it and writes local files under one directory; the later cell that reads the real silver and lands the table is not yours, and nothing here touches AWS.

**What you build (two files, no more).**
1. `data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_run.py` -- imports only the standard library, `pyarrow`, and the sibling `inflection_scope_feed_adapter` (import it the way `inflection_account_return_daily.py` imports its sibling: put the file's own directory on `sys.path`, then a plain import). pandas objects arrive as arguments; do not import pandas. No `boto3`, no network or socket module, no `s3://` string, no clock, no environment variable.
2. `data/assets/scripts/gold/irpt_reporting/tests/test_inflection_scope_feed_run.py` -- pytest, synthetic rows only, at least 8 tests, one named `test_mutant_...`.

**Read first (read only).** `data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_adapter.py` (the `adapt()` you call: its inputs, its `rows` / `absent` / `manifest`); `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` (version 0.4.0: `columns`, `optional_columns`, `schema_hash_with_optional`); `data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_040.py` (the validator `row_problems`); the checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r124/p124_run.py` and `.../checks/r123/p123_adapter.py` (the synthetic world `feed()`, `expected()` and the helpers `silver_of`, `dim_of`, `chain_world` are the golden; read them before you write code and run the checker as you go).

**The cell (`DB-i-11`).** Text of the owned cell: *"The Scope feed run wrapper: from feed silver partitions (frames) and the dimension frame, apply the complete-day rule and refuse a repeated (account, day) key, build the account map from the dimension's own key form, call `adapt()`, and write the contract-0.4.0 table as date partitions, the ABSENT records beside it, and a run record that states the contract version and where ABSENT sits; fixtures only, no AWS."*

### The function

`run(silver, dim_frame, trading_days, firm, method_version, out_dir, schema_version="1.2")` returns the run record (a dict) and writes under `out_dir` only.

- `silver`: dict `{ "date=YYYY-MM-DD": pandas.DataFrame }`; each frame has the feed columns `pull_date, day, account_id, household_id, status, reason_class, reason_claim, reason_cause, daily_factor, start_market_value, end_market_value, fee_basis, fee_basis_note, calc_gross_of_fees, source, data_last_updated`. A row is read with `frame.to_dict("records")`.
- `dim_frame`: a frame with an `account_id` column holding the dimension's key (Orion's id as a string). The account map is `{str(int(a)): str(a)}` over that column.
- `trading_days`, `firm`, `method_version`, `schema_version`: passed to `adapt()` unchanged.

### The rules, in this order

1. **Repeated key.** Over all partitions, a key `(str(int(account_id)), day)` seen twice is a repeat. If there is any, raise `ValueError` whose message carries the COUNT of repeated keys as a number, and write NOTHING (not even `out_dir`). No other value goes in the message.
2. **Complete-day rule.** Group the rows by calendar `day`. A day is INCOMPLETE if any of its rows has a `status` other than `RETURNED` or `ABSENT`, or is `RETURNED` with a null / NaN `daily_factor`, or is `ABSENT` with a null, NaN or empty `reason_class`. Every row of an incomplete day is dropped before `adapt()` is called (the feed writes a day only when complete; this is the wrapper's guard of that rule). The days dropped are counted.
3. Call `adapt(kept_rows, account_map, trading_days, firm, method_version, schema_version)`.
4. **Write** under `out_dir` (create it; touch nothing outside it): `date=<business_date>/data.parquet` for each business date that has at least one row, holding that date's rows only, in a pyarrow schema of exactly the contract's 19 columns plus the optional `source`, `flow_claim`, `source_account_id` (22 fields, types as the contract names them: string, double, int64), so the schema hash over sorted `name:type` lines equals the contract's `schema_hash_with_optional`; `absent/data.parquet` holding the `absent` records when there are any; and `run_record.json` (ASCII JSON, sorted keys) equal to the returned record.
5. **The run record** (dict) has: `contract_version` the string `0.4.0`; `absent_placement` the string `BESIDE_TABLE` (contract 0.4.1 has not landed, so ABSENT sits beside the table and the record says so); `calendar_days_read` (distinct `day` values in the input); `calendar_days_incomplete`; `rows`; `partitions_written`; `absent_by_reason` (counts); `accounts_in_feed`, `accounts_mapped`, `accounts_unmapped` (from the manifest); `proposed_reason_classes` (the sorted members of `absent_by_reason` that are in `NO_FEED_ROW`, `INCOMPLETE_WINDOW`, `NO_EOD_VALUE`: classes the module proposes and no contract admits yet); and `manifest` (the adapter's manifest, as returned).

### The tests

Your own synthetic world (not the checker's). Cover: the clean run (rows, partitions, absent file, record); one incomplete day dropped and counted, each of its three causes; a repeated key refused with the count and no file written; an account in the feed but not in the dimension (`UNMAPPED_ACCOUNT`); each partition holds only its own date; the written schema hash equals the contract's `schema_hash_with_optional`; every written row passes `row_problems`; a 299-calendar-day Monday-to-Friday chain (a single account, deterministic factors) whose chained rows equal the product of the source factors to 1e-12 (this window sits inside the 238-to-365-day gap round 122 named); and `test_mutant_...`: take the wrapper's source text, change ONE rule (for example the line that drops incomplete days), execute the mutated source, and assert its output differs from the real wrapper's on your incomplete-day case. ASCII only. Run `python -I -m pytest -q <your test file>` until green.

<criterion id="DBI124-1-AC1" cell_refs="DB-i-11"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r124/p124_run.py" . DBI124-1-AC1</invocation><expect>DBI124-1-AC1 PASS</expect></criterion>
`DBI124-1-AC1` -- the wrapper reproduces the checker's golden: rows, partitions, ABSENT records and the run record (including `contract_version`, `absent_placement` and `proposed_reason_classes`); an incomplete calendar day is dropped and counted; a repeated key is refused with nothing written. Base: FAIL (no wrapper).

<criterion id="DBI124-1-AC2" cell_refs="DB-i-11"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r124/p124_run.py" . DBI124-1-AC2</invocation><expect>DBI124-1-AC2 PASS</expect></criterion>
`DBI124-1-AC2` -- every partition is `date=<business_date>` with only that date; the written columns and types hash to the contract's `schema_hash_with_optional`; each row passes `~D2`'s validator; the wrapper imports no AWS, network or socket module and names no `s3://` address; nothing is written outside the output directory. Base: FAIL (no wrapper).

<criterion id="DBI124-1-AC3" cell_refs="DB-i-11"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r124/p124_run.py" . DBI124-1-AC3</invocation><expect>DBI124-1-AC3 PASS</expect></criterion>
`DBI124-1-AC3` -- a 299-day window run through the wrapper chains to the source's product to 1e-12 with `carried_days` summing to 299, and your test file exists, names a `test_mutant_` test and passes with at least 8 tests. Base: FAIL (no wrapper).

<expected_criteria>DBI124-1-AC1,DBI124-1-AC2,DBI124-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the adapter, the contract, `~D2`'s test module, `lib/`, `infra/`, the feed script and every issuer check.
- **No AWS, no network.** The wrapper reads frames it is handed and writes local files under `out_dir`. The later cell that reads the feed's real silver and lands the table (addresses from `lib/opal_naming.py`) is not this order.
- **Client data.** None. Every row in your tests and record is synthetic; no run of 8 or more digits in anything you write except a `sha256` value or a path. Your tests write only to pytest's temp area.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A rule that seems wrong, or a case the rules do not cover, is a surprise ROW and you keep the rule as written; never invent a reason class or a fill.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W311-S<k>`, with the real current UTC time (`date -u +%FT%TZ`, run at filing; never typed by hand); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_run.py
data/assets/scripts/gold/irpt_reporting/tests/test_inflection_scope_feed_run.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~311/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-11.inflection-scope-feed-run-wrapper-silver-frames-to-contract-040-parquet.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 10, cell `DB-i-11`.
<owned_cells>DB-i-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI124-1-AC1, DBI124-1-AC2, DBI124-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~311/IRPT_DASHBD.TO-DB-i-11.inflection-scope-feed-run-wrapper-silver-frames-to-contract-040-parquet.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI124-1-AC1,DBI124-1-AC2,DBI124-1-AC3` (run the WORKTREE'S OWN copy from inside your worktree) BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the three criteria's last lines; the number of tests passed; any case the rules did not cover (as row ids); the line count of the wrapper. No client value, no account or household id, no date.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one new local module and its test file; nothing is wired, scheduled, served or deployed, and no existing file is edited.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call, no secret, no grant; the module writes local files under a directory it is handed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; all three criteria FAIL at base (no wrapper), the checker passed a reference wrapper on all three, and nine single-rule mutants of it (a repeat accepted, an incomplete day kept, a wrong partition name, a wrong account map, no proposed-class list, a stray file outside the output directory, a boto3 import, a dropped optional column, and a dropped first trading day) each failed the checker before the cut.
</preflight>

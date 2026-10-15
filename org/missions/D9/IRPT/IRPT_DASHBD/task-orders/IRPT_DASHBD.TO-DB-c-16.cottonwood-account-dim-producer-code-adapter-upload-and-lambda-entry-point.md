# TO IRPT_DASHBD.TO-DB-c-16 -- the Cottonwood `account_dim` PRODUCER CODE: the adapter's upload path (one key, refuses a non-empty partition), the Lambda entry point `account-dim-cot/lambda_function.py` (trading-day frontier, fail loud on absent silver, no write when already landed), and their tests; repo files only; nothing is built, uploaded, planned or applied

<to_id>IRPT_DASHBD.TO-DB-c-16</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~409</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>122</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's decision C (msg 8167: a firm-isolated Cottonwood `account_dim` Lambda on the Inflection pattern; its own package, a `*-cot-*` role and builder names; reads only the Black Diamond silver inputs; writes only its own `account_dim` gold prefix; trading-day frontier; no delete) and the read `deliverables/0.9.0_WK_IRPT_DASHBD~408/ACCOUNT_DIM_WRITER_PATTERN_R121.json` | **Rows:** IRPT_DASHBD-D2-W409-S<k> | **Decomp cell:** `DB-c-16` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 9) | **outcome_ref:** FWD-2, FWD-11, FWD-15 | **depends_on:** none (`DB-c-15` is merged).

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-409`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~409/`. Never push. No client data is read or written. No AWS call is needed or allowed: every S3 interaction in your tests is a fake object you write in the test file.

**Why.** The Cottonwood `account_dim` has an adapter (`data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_account_dim.py`) that builds the table and refuses to write it. Production must be scheduled, so this cell adds (1) the adapter's write path and (2) a Lambda entry point that a later cell packages and schedules. You write code and tests only.

**The cell (`DB-c-16`).**

1. **The adapter's upload path.** In the adapter, change `emit_account_dim(table, as_of, upload=False)` to `emit_account_dim(table, as_of, upload=False, s3=None, writer=None)`. With `upload=False` it behaves exactly as today (writes nothing; returns `{"address", "rows", "landed": False}`). With `upload=True`: (a) `s3` is required (a `ValueError` when it is `None`); (b) split `gold_address(as_of)` into bucket and key prefix (the address is `s3://<bucket>/<key>`); (c) REFUSE with `FileExistsError` if ANY object exists under `<key>/` (call `s3.list_objects_v2(Bucket=..., Prefix=<key>/, MaxKeys=1)` and refuse when `KeyCount` is greater than 0 or `Contents` is non-empty); this writer writes NEW keys only and never overwrites; (d) write ONE object, `<key>/data.parquet`, by calling `writer([table], ARROW_SCHEMA, s3, bucket, key + "/data.parquet")` where `writer` defaults to `stream_parquet.stream_to_parquet` (import `stream_parquet` INSIDE the upload path only, after inserting `<repo root>/data/assets/scripts/lib` onto `sys.path`, so the no-write path and the pure builder gain no new import); (e) return `{"address": uri, "rows": int(table.num_rows), "landed": True, "keys": [<the one key>]}`. Update the module docstring's last paragraph to say the upload is permitted only with an `s3` client and only into an empty partition. Do NOT change `build_account_dim`, `ARROW_SCHEMA`, `SCHEMA_VERSION` or any constant (the contract's schema hash must still match).
2. **The Lambda entry point** `infra/aws/lambda/investor-reporting/account-dim-cot/lambda_function.py`, with `def lambda_handler(event, context=None)` and these named pure helpers (the tests call them):
   - Repo-root resolution: `_ROOT` is the first directory, starting at the file's own directory and walking up, that contains `lib/opal_naming.py` (in the package zip this is the file's own directory; in the repo it is the repo root). Put `_ROOT/lib`, `_ROOT/data/assets/scripts/lib` and `_ROOT/data/assets/scripts/gold/irpt_reporting/adapters` on `sys.path`, then `import opal_naming`, `import trading_calendar as tc`, `import cottonwood_account_dim as adapter`. No `boto3` client is created at import; `boto3` is imported inside the function that builds the client.
   - `def target_day(now)`: `str(tc.prev_trading_day(tc.expected_last_trading_day(now)))`. This is the same T-1 frontier `infra/aws/lambda/investor-reporting/holdings-performance/handler.py` uses (read its module docstring first; the Black Diamond partition for trading day D lands the next calendar day at about 11:46 UTC).
   - `def silver_locations(day)`: for each of the two tables `fact_holdings` and `fact_allocations`, the pair `(bucket, key)` of `<prefix>date=<day>/data.parquet`. The bucket and the prefix TEMPLATE come from `data/assets/scripts/gold/irpt_holdings_performance/sources.json`, entry `blackdiamond_z09` (`bucket`, and `positions_prefix`, whose last path segment `fact_holdings` is replaced by the table name); fill `{monolith}` and `{scope}` exactly the way `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` fills them (read how it does so and call the same registry-derived helpers; do not copy a typed value). The firm token, the bucket name and the silver prefix are typed NOWHERE in your file.
   - `def read_silver(s3, day)`: `get_object` of each of the two keys and `pyarrow.parquet.read_table(io.BytesIO(body)).to_pandas()`; an absent key (`s3.exceptions.NoSuchKey` or a `ClientError` with code `NoSuchKey`/`404`) raises `RuntimeError("silver partition absent: <bucket>/<key>")` and writes nothing: the fire FAILS loud and the next fire retries. Returns `(holdings_frame, roster_frame)` where `fact_holdings` is the adapter's `holdings` argument and `fact_allocations` is its `roster` argument (that mapping is the dry run's, `deliverables/0.9.0_WK_IRPT_DASHBD~161/dry_run_account_dim.py`).
   - `lambda_handler(event, context)`: `day = event["date"]` if the event carries `date` (the manual and catch-up path, `YYYY-MM-DD`), else `target_day(now)`. If `event.get("dry_run")` is true, build the table and return the `emit_account_dim(table, day)` result (writes nothing). Otherwise: if the adapter reports the gold partition non-empty, return `{"date": day, "ok": True, "landed": False, "reason": "TARGET_ALREADY_LANDED"}` and write nothing; else `read_silver`, `build_account_dim`, `emit_account_dim(table, day, upload=True, s3=s3)` and return `{"date": day, "ok": True, "landed": True, "rows": ..., "keys": [...]}`. To know the partition is non-empty BEFORE reading the silver, add to the adapter a public `gold_partition_exists(s3, as_of)` (the same `list_objects_v2` test as the refusal) and have both the upload refusal and the handler use it.
   - The handler takes no other event field and makes no other call. It never lists, reads or writes any prefix other than the two silver inputs and its own gold partition.
3. **The tests.**
   - In `data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_account_dim.py` REPLACE `test_emit_defaults_to_no_write_and_upload_is_refused` by `test_default_emit_writes_nothing` (the same assertions minus the `NotImplementedError` one) and ADD `test_upload_requires_an_s3_client`, `test_upload_refuses_a_non_empty_partition`, `test_upload_writes_exactly_one_key` (a recording `writer` and a fake `s3` with an empty `list_objects_v2`; the recorded key ends `/date=<as_of>/data.parquet`, the recorded schema is `ARROW_SCHEMA`) and `test_schema_hash_matches_contract` (recompute the schema hash with the contract's basis: sha256 over the sorted `name:type` lines joined by newline, no trailing newline, and compare to `schema_hash` in `org/standards/IRPT_DASHBD_ACCOUNT_DIM_CONTRACT.json`). Keep every other existing test unchanged.
   - New `infra/aws/lambda/investor-reporting/account-dim-cot/tests/test_lambda_function.py` (a `conftest.py` there is allowed if needed) with `test_target_day_is_the_t_minus_1_trading_day` (Monday 2026-10-12 12:00 UTC gives `2026-10-09`; Wednesday 2026-10-14 12:30 UTC gives `2026-10-13`), `test_silver_locations_name_both_tables_at_the_day` , `test_hold_on_absent_silver_raises_and_writes_nothing`, `test_already_landed_partition_returns_without_reading_silver`, `test_event_date_overrides_the_frontier`, and `test_handler_lands_one_key_for_a_present_silver` (fakes for `s3`: a dict-backed object store with `get_object`, `list_objects_v2`, `put_object`, and a recording `writer`; build the two silver frames as parquet bytes with pandas or pyarrow). No test calls AWS or the network; each test builds its own fake.
4. **Do NOT**: build, zip or upload anything; edit the source map, any Terraform file, any other Lambda, the holdings-performance package, the registry, the contract or the producer; call AWS; create a role, a schedule or a function; edit existing tests other than the one named above.

<criterion id="DBC122-1-AC1" cell_refs="DB-c-16"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r122/p122_bcw.py" . DBC122-1-AC1</invocation><expect>DBC122-1-AC1 PASS</expect></criterion>
`DBC122-1-AC1` -- every named test above exists in its file, and pytest passes on both test files. Base: FAIL (the named tests are absent).

<criterion id="DBC122-2-AC1" cell_refs="DB-c-16"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r122/p122_bcw.py" . DBC122-2-AC1</invocation><expect>DBC122-2-AC1 PASS</expect></criterion>
`DBC122-2-AC1` -- the bounds: the product files changed since the base are only the five in `<paths>`; `lambda_function.py` is ASCII, types no firm token, bucket name or silver prefix, and creates no boto3 client at import; the adapter's constants, schema and `build_account_dim` are byte-identical to the base; a planted control (the adapter's refusal line removed in a scratch copy) makes `test_upload_refuses_a_non_empty_partition` FAIL. Base: FAIL (the new file is absent).

<expected_criteria>DBC122-1-AC1, DBC122-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the checkers, every Terraform file, the source map, the registry, the producer and every contract.
- **Reads and writes.** Reads: repo files and `git show`. Writes: the files in `<paths>`, your folder and scratch in your private folder. No AWS call, no upload, no Terraform, no invoke, no deploy, no push, no vendor call, no secret read.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W409-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~409/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-16.cottonwood-account-dim-producer-code-adapter-upload-and-lambda-entry-point.md
data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_account_dim.py
data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_account_dim.py
infra/aws/lambda/investor-reporting/account-dim-cot/lambda_function.py
infra/aws/lambda/investor-reporting/account-dim-cot/tests/test_lambda_function.py
infra/aws/lambda/investor-reporting/account-dim-cot/tests/conftest.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 9, cell `DB-c-16`.
<owned_cells>DB-c-16</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC122-1-AC1, DBC122-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~409/IRPT_DASHBD.TO-DB-c-16.cottonwood-account-dim-producer-code-adapter-upload-and-lambda-entry-point.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC122-1-AC1 DBC122-2-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the two criteria's last lines; the list of changed product files; the pytest summary line of each test file; the planted control's outcome; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: repo files only; nothing is built, uploaded, planned or applied. The later act's blast (a new function, role, schedule and the first write of one partition) is bounded in the CTO pair packet (DB-c-18).
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call and no grant; the role is DB-c-17's.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is read or changed; the schedule is DB-c-17's and lands DISABLED.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBC122-2-AC1 plants its own negative control.
</preflight>

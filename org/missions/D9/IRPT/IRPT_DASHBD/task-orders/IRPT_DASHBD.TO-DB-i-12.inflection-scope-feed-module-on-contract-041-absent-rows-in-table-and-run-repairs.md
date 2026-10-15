# TO IRPT_DASHBD.TO-DB-i-12 -- the SCOPE FEED MODULE ON CONTRACT 0.4.1: Orion rows VENDOR_REPORTED, ABSENT rows written INTO the table, the wrapper repairs of worker rows W311-S1 to S6, the 'proposed' marks removed, the claim placed by the contract; fixtures only, nothing to AWS

<to_id>IRPT_DASHBD.TO-DB-i-12</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~312</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>125</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_124_20261015.md` (msg 8654: the issuer's batch accepted with three additions) and `2.0.0_SA_COO~D2` msg 8635 (contract 0.4.1 landed).

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-312`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~312/`. Never touch a path outside the `<paths>` block below.

**Why.** Rounds 123 and 124 built a pure adapter (`adapt()`) and a run wrapper (`run()`) against contract 0.4.0, which kept ABSENT days in a file beside the table. Contract 0.4.1 landed during round 124 and the merged module is now stale against it: its tests that read the contract file fail on trunk. This order moves both files to 0.4.1 and closes six defects the round-124 worker filed against the wrapper. Everything still runs on fixtures; nothing touches AWS.

**What you do (edit four existing files; add nothing else).**
1. `data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_adapter.py` (the pure adapter; standard library only, no I/O).
2. `data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_run.py` (the wrapper; standard library, `pyarrow` and the sibling adapter only; it may now READ the contract file named below and nothing else; no `boto3`, no network or socket module, no `s3://` string).
3. `data/assets/scripts/gold/irpt_reporting/tests/test_inflection_scope_feed_adapter.py` and 4. `data/assets/scripts/gold/irpt_reporting/tests/test_inflection_scope_feed_run.py`: update so every test passes on the new behaviour; the wrapper's file keeps a `test_mutant_...` test.

**Read first (read only).** `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` (version 0.4.1: `columns` with `nullable_when_absent`, `optional_columns` including `row_status` and `reason_class`, `source_requires`, `source_rules.orion`, `schema_hash_with_optional`); `data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_041.py` (the validator `row_problems` and its `_orion_present` and `_absent` rows show the exact shapes); the checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r125/p125_run041.py` and, for its helpers, `.../checks/r124/p124_run.py` and `.../checks/r123/p123_adapter.py` (its synthetic world is the golden; read it before you write code and run it as you go; where an older checker differs from the r125 checker, the r125 checker rules).

**The cell (`DB-i-12`).** Text of the owned cell: *"Move the Scope feed adapter and run wrapper to contract 0.4.1: Orion PRESENT rows carry return_basis VENDOR_REPORTED and row_status PRESENT; ABSENT rows are written INTO the table in the 0.4.1 shape with the contract's reason precedence (the absent file and the BESIDE_TABLE placement retire); the wrapper reads its field list and version from the contract file, refuses a bad dimension key, a mismatched partition and a non-empty output directory, passes the adapter the full domain and account set so that no trading day is left unaccounted when a first or last calendar day is dropped, and records the dropped days and the unaccounted count; the 'proposed' marks are removed; the end-of-day claim sits in the table when the contract declares it and in the run record when it does not; fixtures only, no AWS."*

### The adapter

`adapt(feed_rows, account_map, trading_days, firm, method_version, schema_version="1.2", domain=None, accounts=None)` returns `{"rows": [...], "manifest": {...}}` (the `absent` key RETIRES).

- `domain`: None, or a pair `(min_day, max_day)` of ISO strings. When given it REPLACES the smallest and largest `day` taken from `feed_rows` for the output domain AND for the window start. `accounts`: None, or an iterable of Orion ids included in the output even when they have no rows in `feed_rows` (unioned with the accounts that do). With both None the behaviour is unchanged.
- The per-day rules stand as in rounds 123 and 124 (mapping, own row, window and compounding, end-of-day value), with the contract's precedence for a day with two reasons: `UNMAPPED_ACCOUNT`, then the feed's own class, then `NO_FEED_ROW`, then `INCOMPLETE_WINDOW`, then `NO_EOD_VALUE`. Each (account, trading day) of the domain appears in `rows` exactly once.
- **A PRESENT row** carries the 19 contract columns and `source` `orion`, `flow_claim` `absent`, `source_account_id`, plus `row_status` `PRESENT`, `reason_class` None and `return_basis` `VENDOR_REPORTED` (contract `source_requires`); `day_quality` `MEASURED` and `guard_state` `GUARD_NOT_REACHED` stay. It keeps the module field `market_value_eod_claim` (`inferred` or `measured`).
- **An ABSENT row** is a full row: `firm`, `account_id` (the dimension key string for a mapped account; None for `UNMAPPED_ACCOUNT`), `business_date`, `market_value_eod` None, `market_value_eod_claim` None, `external_flow` None, `income_received` None, `income_return` None, `total_return_daily` None, `return_basis` `NOT_MEASURABLE`, `holdings_price_return` None, `holdings_price_return_reason` None, `fee_amount` None, `fee_amount_reason` `FEE_RAIL_UNUSED`, `day_quality` `NOT_MEASURABLE`, `guard_state` `GUARD_NOT_REACHED`, `history_scope` `PARTIAL_HISTORY`, `carried_days` 0, `method_version`, `schema_version`, `source` `orion`, `flow_claim` `absent`, `source_account_id` (the integer Orion id, always set), `row_status` `ABSENT`, `reason_class`.
- `rows` sort by `(account_id or "", business_date, source_account_id)`.
- The manifest: drop `rows`; add `rows_present` and `rows_absent`; `calendar_days_compounded` counts PRESENT rows only; every other key stands. Keep the ValueError refusals (a gross-of-fees row, an unsorted calendar).

### The wrapper

`run(silver, dim_frame, trading_days, firm, method_version, out_dir, schema_version="1.2")` returns the run record and writes under `out_dir` only. In this order; each REFUSAL raises `ValueError` whose message carries a COUNT as a number and writes NOTHING (not even `out_dir`):

1. **Contract.** Read `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` (find the repository root from the wrapper's own location, as `inflection_account_return_daily.py` does). The table's fields are the contract's `columns` then `optional_columns`, in that order, with the contract's types (`string`, `double`, `int64`). `contract_version` is the file's value. No version string is typed in the wrapper.
2. **Output directory.** REFUSE if `out_dir` exists and is not empty (count: entries in it). A rerun therefore never mixes with stale partitions (row W311-S6).
3. **Dimension keys.** REFUSE on a duplicate key or a key that is not canonical, meaning `str(a) != str(int(a))` (count: offenders) (row W311-S4).
4. **Partition keys.** Each partition's name is `date=<d>`; REFUSE if any row's `pull_date` differs from `<d>` (count: rows) (row W311-S5).
5. **Repeated key.** As round 124: REFUSE when `(str(int(account_id)), day)` repeats; the count is the number of distinct keys repeated (row W311-S2 states the rule).
6. **Complete-day rule** as round 124; the dropped rows are counted. Then call `adapt(kept_rows, account_map, trading_days, firm, method_version, schema_version, domain=(smallest day, largest day over ALL rows read, before the drop), accounts=every Orion id in ALL rows read)`. So the first or last calendar day being dropped leaves each account ABSENT `NO_FEED_ROW` (or `UNMAPPED_ACCOUNT`) on its trading day instead of vanishing (rows W311-S1 and S3).
7. **Write** `date=<business_date>/data.parquet` for each business date with at least one row, holding that date's rows (PRESENT and ABSENT) in a pyarrow schema of exactly the contract's declared fields. If the contract declares a column `market_value_eod_claim` the rows carry it; if not, the key is NOT written to the table. There is no `absent/` file. Write `run_record.json` (ASCII JSON, sorted keys) equal to the returned record.
8. **The run record**: `contract_version`; `calendar_days_read`; `calendar_days_incomplete`; `incomplete_days` (the dropped calendar days, sorted ISO strings); `rows_present`; `rows_absent`; `partitions_written`; `absent_by_reason` (counts); `accounts_in_feed`, `accounts_mapped`, `accounts_unmapped` (over ALL rows read); `trading_days_unaccounted` (the number of (account, trading day) pairs, over the trading days between the smallest and largest day of ALL rows read, with no row in the output; the wrapper counts it from the output itself, independently of the adapter's loop; the CTO's criterion: it reads 0 when the first or last calendar day is incomplete); `claim_placement` (`TABLE` when the contract declares `market_value_eod_claim`, else `RUN_RECORD`); `market_value_eod_claim_counts` (`{"inferred": n, "measured": m}` over PRESENT rows, always); `manifest` (the adapter's manifest as returned). The keys `absent_placement`, `proposed_reason_classes` and the manifest key `reason_class_status` RETIRE: contract 0.4.1 admits the three classes, so no class is "proposed".

### The tests

Update both test files for the new behaviour (your own synthetic world). Cover, at least: a PRESENT row's `VENDOR_REPORTED` and `row_status`; an ABSENT row's full shape, mapped and unmapped; the precedence of two reasons on one day; the domain and accounts parameters; each of the five wrapper refusals (count carried, nothing written); the first-day and last-day drop leaving `trading_days_unaccounted` 0; the claim in the run record while the contract does not declare it (and in the table when a copy of the contract declares it); the schema hash of the written fields equals `schema_hash_with_optional`; every written row passes `row_problems` from `test_account_return_contract_041.py`; the 299-day chain; and `test_mutant_...` in the wrapper's file. ASCII only. Run `python -I -m pytest -q <file>` on both until green.

<criterion id="DBI125-1-AC1" cell_refs="DB-i-12"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r125/p125_run041.py" . DBI125-1-AC1</invocation><expect>DBI125-1-AC1 PASS</expect></criterion>
`DBI125-1-AC1` -- the golden through the wrapper: 17 PRESENT rows (VENDOR_REPORTED, PRESENT) and 11 ABSENT rows in the table in the 0.4.1 shape (UNMAPPED_ACCOUNT with a null `account_id` and a `source_account_id`), the precedence, the claim wherever the contract puts it, the run record (`contract_version` read from the contract file, `trading_days_unaccounted` 0, no retired key), no `absent/` file. Base: FAIL.

<criterion id="DBI125-1-AC2" cell_refs="DB-i-12"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r125/p125_run041.py" . DBI125-1-AC2</invocation><expect>DBI125-1-AC2 PASS</expect></criterion>
`DBI125-1-AC2` -- every written partition holds only its own date, its field names and types equal the contract's declared fields and hash to `schema_hash_with_optional`, every row (PRESENT and ABSENT) passes the 0.4.1 validator, the wrapper imports no AWS or network module, names no `s3://` address and types no contract version, and nothing is written outside the output directory. Base: FAIL.

<criterion id="DBI125-1-AC3" cell_refs="DB-i-12"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r125/p125_run041.py" . DBI125-1-AC3</invocation><expect>DBI125-1-AC3 PASS</expect></criterion>
`DBI125-1-AC3` -- the repairs: a first or last calendar day incomplete leaves 0 trading days unaccounted and lists the dropped day; a duplicate dimension key, a non-canonical one, a partition whose rows name another pull date, a non-empty output directory and a repeated key are each refused with a count and nothing written; the 299-day chain still equals the source product to 1e-12; and the adapter and wrapper test files together pass at least 30 tests and name a mutant test. Base: FAIL on trunk (the merged module is stale against 0.4.1).

<expected_criteria>DBI125-1-AC1,DBI125-1-AC2,DBI125-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the contract, the contract test modules, `lib/`, `infra/` and every issuer check.
- **No AWS, no network.** The wrapper reads the frames it is handed and the one contract file, and writes local files under `out_dir`. Landing the table and reading the real silver are a later cell.
- **Client data.** None. Every row in your tests and record is synthetic; no run of 8 or more digits in anything you write except a `sha256` value or a path. Your tests write only to pytest's temp area.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A rule that seems wrong, or a case the rules do not cover, is a surprise ROW and you keep the rule as written; never invent a reason class, a fill or a field.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W312-S<k>`, with the real current UTC time (`date -u +%FT%TZ`, run at filing; never typed by hand); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_adapter.py
data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_run.py
data/assets/scripts/gold/irpt_reporting/tests/test_inflection_scope_feed_adapter.py
data/assets/scripts/gold/irpt_reporting/tests/test_inflection_scope_feed_run.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~312/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-12.inflection-scope-feed-module-on-contract-041-absent-rows-in-table-and-run-repairs.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 11, cell `DB-i-12`.
<owned_cells>DB-i-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI125-1-AC1, DBI125-1-AC2, DBI125-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~312/IRPT_DASHBD.TO-DB-i-12.inflection-scope-feed-module-on-contract-041-absent-rows-in-table-and-run-repairs.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI125-1-AC1,DBI125-1-AC2,DBI125-1-AC3` (run the WORKTREE'S OWN copy from inside your worktree) BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the three criteria's last lines; the number of tests passed in each test file; any case the rules did not cover (as row ids); the line counts of the adapter and the wrapper. No client value, no account or household id, no date.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: edits to four existing local files whose only importers are their own tests (nothing is wired, scheduled, served or deployed).
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call, no secret, no grant; the wrapper reads one repository file and writes local files under a directory it is handed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; all three criteria FAIL on the merged module (stale against 0.4.1), the checker passed a reference implementation on all three, and eleven single-rule mutants of it (a PRESENT row TWR, an ABSENT row VENDOR_REPORTED, an ABSENT row labelled PRESENT, the domain not widened, a dimension key not refused, a partition key unchecked, a non-empty output directory accepted, the contract version typed, the claim placement wrong, the proposed marks kept, an undeclared claim column written) each failed the checker before the cut.
</preflight>

# TO IRPT_DASHBD.TO-DB-c-22 -- the Cottonwood COVERAGE CENSUS, read only (FWD-10, round 145): for each Cottonwood gold table the first and last day, the absent trading days and their runs, the floor and why it is there, and the account histories; counts, dates and words; no write

<to_id>IRPT_DASHBD.TO-DB-c-22</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~414</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>145</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** Andrew's go (`ANDREW_DIRECT_20261015_231xZ_PARALLELIZE_IRPT_SUITE_GO.md`) through the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md` Move 2 (msg 8741: "`~C2`: IRPT_DASHBD FWD-10, Cottonwood first (07-10 floor, 3 absent days, 12-day gap), all measured. Then 49F and Inflection") | **Rows:** IRPT_DASHBD-D2-W414-S<k> | **Decomp cell:** `DB-c-22` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 14) | **outcome_ref:** FWD-10 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-414`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~414/`. Never push. No client value is written anywhere: counts, dates, hashes and words only; never an account id or a household id. **You make read-only AWS calls through python `boto3` and nothing else:** S3 `list_objects_v2`, `head_object` and `get_object` on the prefixes named below. No put, delete, create, invoke, update or secret read; no Terraform. Region `us-east-1`. A read that is refused is recorded as refused (its words).

**Why (the outcome).** PRD FWD-10: "A person can always tell what they are looking at: where the data starts, which days could not be measured, when a figure is a fallback, and how current the data is." The CTO started it with Cottonwood and named three measured facts: the 07-10 floor, 3 absent days and a 12-day gap. Before anything is built, you measure what is actually there, so every sentence the page will say rests on a count.

**What to read.** The Cottonwood gold tables in `opal-data-cottonwood` under the root of `address("irpt", "cottonwood", "gold", <table>, "date=2000-01-01")` (build each prefix with `lib/opal_naming.py address()` and cut at `<table>/`, as `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_report_reader.py` `gold_prefix()` does): `filled_report_values`, `account_return_daily`, `holdings_performance_daily`, `account_dim`. And the Black Diamond silver `fact_allocations` and `fact_holdings` (bucket and prefix from `lambda_function.silver_locations('2000-01-03')` in `infra/aws/lambda/investor-reporting/account-dim-cot/lambda_function.py`, called with `python -c` after putting that folder on `sys.path`, NOT `-I`, no AWS call). The trading calendar is `lib/trading_calendar.py` (`trading_days_between(a, b)` is inclusive; run with plain `python`, NOT `-I`, because it needs the user site packages).

**The cell (`DB-c-22`).** Write ONE record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~414/COTTONWOOD_COVERAGE_CENSUS_R145.json` and ONE short note `.../COTTONWOOD_COVERAGE_CENSUS_R145.md` (under 50 lines: in words, for each fact, what a person looking at a Cottonwood account would need to be told). Use a small python script (in your folder) for the reads. The record carries, each with the UTC time of its read:
1. `tables`: an object keyed by the four table names, each `{"partitions", "first_date", "last_date", "absent_trading_days" (the sorted list of every trading day between first_date and last_date inclusive that has NO `date=` partition), "runs" (the maximal runs of consecutive absent trading days as `[{"start", "end", "trading_days"}]`)}`. A partition counts as present when its `date=<D>/` prefix holds at least one object.
2. `floor`: `{"date" (the first day of the Cottonwood series the portal can show: the first date of `filled_report_values`), "evidence_words" (why there is nothing before it: say which table's first date and which silver partitions explain it), "silver_empty": {"table": "fact_allocations", "first_empty", "last_empty", "count"} (the empty Black Diamond `fact_allocations` partitions: a partition is empty when its parquet footer reads 0 rows (`pyarrow.parquet.ParquetFile(...).metadata.num_rows`); report the first and last empty date and how many; this is a footer read, not a data read) and "first_nonempty_after" (the first partition after the last empty one that has rows)}`.
3. `twelve_day_gap`: the run of 12 trading days in `account_return_daily` that the CTO named (the days between the last pre-2026-07 partition and the 2026-07-10 floor) if it exists: `{"table": "account_return_daily", "start", "end", "trading_days", "found": true}`; if you find no run of exactly that kind, `{"found": false, "words": ...}` and what you found instead.
4. `account_histories` (from the newest `account_dim` and `holdings_performance_daily` partitions and the series' first dates; counts only): `{"accounts_in_account_dim", "accounts_with_holdings_on_the_floor_day" (distinct accounts in `holdings_performance_daily` on the first_date of `filled_report_values`), "accounts_first_seen_after_floor" (distinct accounts in the newest `holdings_performance_daily` partition that have NO row in the floor day's partition: their history starts later than the series, the partial-history case), "account_forms_note" (the account column and how you compared: `str(value).strip()`)}`.
5. `coverage_vocabulary`: `{"column" (the column of `filled_report_values` or `account_return_daily` that carries the coverage or status state, or null), "values" (a map of each distinct value in the newest partition of that table to its row count, or null)}`; if neither table carries a coverage column, say so in `words`.
6. `reads`: `{"s3_list_calls", "s3_head_calls", "s3_get_calls", "writes": 0, "invokes": 0}`; `claim` = `"measured"`; `pushed` = false; `deployed` = false.
Anything you cannot read or establish is recorded as `NOT_ESTABLISHED` with the reason, never guessed.

**Do NOT**: write to S3 or any AWS service; invoke any Lambda or run any producer; edit any file outside your folder, the channel and your order; read or record an account id or household id.

<criterion id="DBC145-1-AC1" cell_refs="DB-c-22"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r145/p145_bcw.py" . DBC145-1-AC1</invocation><expect>DBC145-1-AC1 PASS</expect></criterion>
`DBC145-1-AC1` -- the record's `tables` section equals a FRESH measurement made by the checker: for each of the four tables the partition count, first and last date, the exact list of absent trading days and the runs. Base: FAIL (no record).

<criterion id="DBC145-1-AC2" cell_refs="DB-c-22"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r145/p145_bcw.py" . DBC145-1-AC2</invocation><expect>DBC145-1-AC2 PASS</expect></criterion>
`DBC145-1-AC2` -- the floor, the twelve-day gap, the account histories and the bounds: the floor date equals the first date of `filled_report_values` in a fresh LIST; the empty-silver boundaries equal a fresh footer read at the first and last empty dates and the first non-empty one after; the twelve-day gap run (if found) is a run of exactly 12 trading days in the fresh absent list of `account_return_daily`; the partial-history count equals a fresh recount; the record carries zero writes and invokes and no identifier value; only the worker's folder, the channel and its order changed. Base: FAIL (no record).

<expected_criteria>DBC145-1-AC1, DBC145-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files, `git show`, and the read-only AWS calls named above. Writes: the files in `<paths>`. No AWS write, no invoke, no Terraform, no push, no vendor call, no secret read.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W414-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh` (never `--no-verify`); run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~414/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-22.cottonwood-coverage-census-where-the-data-starts-and-which-days-are-absent.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 14, cell `DB-c-22`.
<owned_cells>DB-c-22</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC145-1-AC1, DBC145-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~414/IRPT_DASHBD.TO-DB-c-22.cottonwood-coverage-census-where-the-data-starts-and-which-days-are-absent.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC145-1-AC1,DBC145-1-AC2` BEFORE the flip (set the order's status to complete only when both PASS); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the two criteria's last lines; per table the partitions, first and last date and the number of absent trading days; the floor date; the twelve-day gap (found or not); the partial-history count; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: read-only measurements and a record; nothing is created, planned, applied or written to S3.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: only S3 list, head and get calls; no grant is made or changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is read or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the checker re-measures the S3 plane itself and compares.
</preflight>

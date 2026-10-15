# TO IRPT_DASHBD.TO-DB-c-8 -- the BLACK DIAMOND COTTONWOOD LAYERS: every layer and table under `blackdiamond/cottonwood/` in `opal-data-assets`, each table's partitions, newest date, columns and grain, and whether any carries an ACCOUNT-LEVEL RETURN series (the Commonwealth `daily_returns` stops at 2026-06-22); a read; names, counts, dates and column names only; nothing written

<to_id>IRPT_DASHBD.TO-DB-c-8</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~405</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>116</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, CTO half of the DB-c-5 pair ruling 6 (`deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_DB-c-5_R115_COTTONWOOD_HOLDINGS_PERFORMANCE_CTO_HALF.md`): "the source becomes Black Diamond ... a B-CW READ next round: whether BD carries an account-level return series, and at what grain" | **Rows:** IRPT_DASHBD-D2-W405-S<k> | **Decomp cell:** `DB-c-8` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 3) | **outcome_ref:** FWD-11, FWD-15 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-405`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~405/`. Never push. Counts, dates, prefixes, column names and words only in the repo, a row or your report; an account number, a client or household id, a name or a figure is never recorded. A raw `aws s3` or `aws s3api` listing in a shell call is denied by the repo's rail; do every S3 read from a short Python script (boto3, your own identity, LIST, HEAD and ranged GET of a Parquet footer only) kept in your private folder `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~405/` and not committed.

**Why.** Cottonwood's `account_return_daily` has no input after 2026-06-22: the Commonwealth silver holds one delivery (`daily_returns`, `account_day_value`, `month_grades`; one partition `date=2026-06-23`). The CTO ruled that the source for the history after that date becomes Black Diamond, Cottonwood's reporting system, whose daily feed the holdings-performance producer already reads (`blackdiamond/cottonwood/silver/fact_holdings/`, 93 partitions, 2026-06-09 to 2026-10-13). Before a producer is cut, he needs one fact: does Black Diamond carry an account-level return series, or only holdings and values, and at what grain.

**The cell (`DB-c-8`).**
1. **Layers.** The common prefixes directly under `s3://opal-data-assets/blackdiamond/cottonwood/` (for example `bronze/`, `silver/`, others): record each as `layers[].prefix` (with its trailing slash).
2. **Tables.** For each layer, the common prefixes directly under it are its tables: record each as `layers[].tables[].prefix`. If a layer holds objects directly rather than table folders, record it with an empty `tables` list and say so in `words`.
3. **Per table.** `partition_count` and `newest_date` (the `date=YYYY-MM-DD/` folders under the table prefix; 0 and absent when it has none, and then `columns` is `[]`); `columns` is the sorted column names of ONE Parquet object in the newest partition, read from its footer only (a ranged GET of the file's tail through `pyarrow.parquet.read_schema` on a ranged file object, as the checker does; never read row data); `key_columns_words` is the columns that form the table's grain, in words from the names and the producer code that reads the table (`data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` reads `fact_holdings`; read the code for any table the repo reads).
4. **Return-like columns.** `return_like_columns` is the sorted list `"<table prefix>:<column>"` for every column whose name matches `return|twr|perf|pnl|gain|roi|irr` (case-insensitive) in any table. This list is computed by pattern, not judged.
5. **Verdict.** `verdict` is one of `ACCOUNT_RETURN_SERIES` (a table has account-grain rows with a return-like column over time), `ACCOUNT_VALUE_ONLY` (account-grain values and flows but no return column: a return would be computed), `HOLDINGS_ONLY` (positions per security only), `NOT_ESTABLISHED`. `words` states the evidence (which table and columns) and `grain_words` the grain (account, security, household, day). `ACCOUNT_RETURN_SERIES` needs at least one return-like column. Name what you did not read.
6. **Record** `BD_RETURNS_READ_R116.json` in your folder with exactly: `claim` ("measured"); `layers` [{`prefix`, `tables` [{`prefix`, `partition_count`, `newest_date`, `columns`, `key_columns_words`}]}]; `return_like_columns`; `verdict`; `words`; `grain_words`; `basis_words`; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0, `aws_writes` 0, `s3_reads` (integer)}; `pushed` false; `deployed` false.

<criterion id="DBC116-4-AC1" cell_refs="DB-c-8"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r116/p116_bcw.py" . DBC116-4-AC1</invocation><expect>DBC116-4-AC1 PASS</expect></criterion>
`DBC116-4-AC1` -- the record is complete; the recorded layers equal a fresh LIST of `blackdiamond/cottonwood/`; each layer's tables equal a fresh LIST; each table's partition count, newest date and column names equal a fresh read (the columns from a fresh footer read of the newest partition's first Parquet object); `return_like_columns` equals the pattern recomputed over the fresh columns; a verdict of `ACCOUNT_RETURN_SERIES` has at least one return-like column; no write is recorded. Base: FAIL (no record).

<expected_criteria>DBC116-4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the checkers and every contract.
- **Reads and writes.** Reads: repo files; S3 LIST, HEAD and ranged GET of Parquet footers under `s3://opal-data-assets/blackdiamond/cottonwood/` ONLY. Writes: the record in your folder and your private folder. No row data is read, no write to AWS, no deploy, no push, no vendor call, no secret read, no read of any other firm's place.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A listing or footer you cannot read is named in `basis_words` with the error.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W405-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~405/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-8.black-diamond-cottonwood-layers-and-account-return-series-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 3, cell `DB-c-8`.
<owned_cells>DB-c-8</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC116-4-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~405/IRPT_DASHBD.TO-DB-c-8.black-diamond-cottonwood-layers-and-account-return-series-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC116-4-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the layers and the tables per layer with partition counts and newest dates; the return-like columns found (or none); the verdict and the grain in one line each; the number of S3 reads; row ids. No account number, client or household id, name or figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read record; nothing is wired, changed or deleted.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: read-only S3 LIST, HEAD and Parquet footer reads under the Cottonwood-scoped Black Diamond prefix; no new principal or grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is read or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBC116-4-AC1 FAILS at base (no record) and its fresh-LIST and fresh-footer recount arms are exercised on the worker's record.
</preflight>

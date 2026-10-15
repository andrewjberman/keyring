# TO IRPT_DASHBD.TO-DB-c-21 -- the Cottonwood FWD-1 TRACE, read only: Black Diamond silver, then the Cottonwood gold `holdings_performance_daily` and `account_dim` (2026-10-14), then the reporting-gold build's households source and its Cottonwood output; counts and words; no write, no invoke

<to_id>IRPT_DASHBD.TO-DB-c-21</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~413</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>126</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's B-CW analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-CW_ROUNDS_117_125_20261015.md` section 2 ruling 2 ("a read-only trace from Black Diamond silver to the Cottonwood gold (`holdings_performance_daily`, `account_dim`) to the reporting-gold build, which takes the NEWEST `account_dim` partition. It reads whether the next reporting-gold run builds Cottonwood households from the 2026-10-14 `account_dim`, and what that run's Cottonwood output is (counts, the absent kinds in words). It is a read, with no write and no manual invoke.") | **Rows:** IRPT_DASHBD-D2-W413-S<k> | **Decomp cell:** `DB-c-21` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 13) | **outcome_ref:** FWD-1, FWD-2 | **depends_on:** none (rounds 117 to 125 are drained).

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-413`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~413/`. Never push. No client value is written anywhere: counts, dates, hashes and words only; never an account id or a household id. **You make read-only AWS calls through python `boto3` and nothing else:** S3 `list_objects_v2` and `get_object` on the prefixes named below; CloudWatch Logs reads only if you need a log line. No put, delete, create, invoke (of any Lambda, a manual run of any producer included), update, assume-role or secret read; no Terraform. Region `us-east-1`. A read that is refused is recorded as refused (its words).

**Why.** The Cottonwood `holdings_performance_daily` and `account_dim` gold tables are live and land daily (T-1 = 2026-10-14 landed today). The CTO wants the thread read end to end once: does the reporting-gold build take the Cottonwood households from the newest `account_dim` partition, and what does its Cottonwood output hold? You read the chain and say, in counts and words, where it holds and where it does not.

**What to read (all in your worktree, then live S3).**
- `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_report_reader.py` (the reader the build loads: `households()` takes the NEWEST `account_dim` partition, groups accounts by `household_id`, drops null households; sibling tables Cottonwood lacks are the absent form `NO_SOURCE_YET`), and `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_account_dim.py` (what the table holds).
- `infra/aws/lambda/investor-reporting/reporting-gold/handler.py` and `data/assets/scripts/gold/irpt_reporting/filled_report_values.py` (where the build calls `ad.households(reader, None)`, how it picks days and households, what it writes and to which address built by `lib/opal_naming.py address()`), and every Terraform or schedule file that fires that handler (find them by reading the handler's own Terraform root and the schedule files of `infra/aws/terraform/investor-reporting/`; a named file you read, not a repo-wide search).

**The cell (`DB-c-21`).** Write ONE record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~413/COTTONWOOD_FWD1_TRACE_R126.json` and ONE short note `.../COTTONWOOD_FWD1_TRACE_R126.md` (under 60 lines: the trace in words, hop by hop, naming each hop's verdict `HOLDS`, `HOLDS_WITH_GAP` or `BREAKS` and why). Use a small python script (in your folder) with a read-only reader class that has only `list_prefixes(bucket, prefix)` and `get(bucket, key)` for the live reads.

The JSON record carries, each with the UTC time of its read:
1. `silver`: for `fact_holdings` and `fact_allocations` (take the bucket and prefix by calling `lambda_function.silver_locations()` from `infra/aws/lambda/investor-reporting/account-dim-cot/lambda_function.py` with `python -c` after putting that folder on `sys.path`; NOT `-I`; no AWS call): `{"partitions", "newest_date"}` from a fresh LIST.
2. `gold`: for `holdings_performance_daily` and `account_dim` of the Cottonwood firm (addresses from `address()` with scope `cottonwood`): `{"newest_date", "rows"}` (the row count of the newest partition's parquet). For `account_dim` also `households` (the number of distinct non-blank `household_id` among rows with a non-null `account_id`, the reader's own grouping rule) and `accounts_without_household`. And `crosswalk` = `{"holdings_account_column" (the column of the holdings daily parquet that names the account), "overlap", "only_in_holdings", "only_in_account_dim"}`: the counts of distinct accounts in both newest partitions, only in the holdings daily one, only in `account_dim`.
3. `reporting_gold`: `{"scheduled_for_cottonwood" (true, false or "NOT_ESTABLISHED"), "evidence_files" (the repo files you read for that claim, each an existing path), "evidence_words", "next_run_source_partition" (the date of the account_dim partition the build's `ad.households(reader, None)` would take now: call the reader's `households()` through your read-only reader class and report the partition it read), "next_run_households" (the number of households that call returns), "output_prefix" (the s3 address, cut at the table, where the build writes the Cottonwood filled report, from the build's own address call; or null if it has no Cottonwood output), "output_object_count" and "output_newest_key" (a fresh LIST of that prefix, 0 and null when empty or absent), "absent_kinds_words" (the sibling tables the reader names as absent for Cottonwood, in words, naming each missing table)}`.
4. `verdicts`: one of `HOLDS`, `HOLDS_WITH_GAP`, `BREAKS` for each hop `silver_to_gold_holdings`, `silver_to_gold_account_dim`, `gold_to_reporting_gold_households`, `reporting_gold_output`, each with `words`.
5. `reads`: `{"s3_list_calls", "s3_get_calls", "writes": 0, "invokes": 0}`; `claim` = `"measured"`; `pushed` = false; `deployed` = false.
Counting rules (the checker recounts by them): an account is the string `str(value).strip()` of its column value, no other normalization (if the two tables' account forms differ, the counts are still those of this rule and you say so in the words); `newest_key` is the lexicographically greatest key of the output prefix; a household is a distinct non-blank `household_id` among rows with a non-null `account_id`; `rows` is the parquet's row count. Anything you cannot read or establish is recorded as `NOT_ESTABLISHED` with the reason, never guessed. If the build has no Cottonwood output yet, that IS the finding (`output_prefix` null or its LIST empty) and `reporting_gold_output` is `BREAKS` or `HOLDS_WITH_GAP` with the words.

**Do NOT**: write to S3 or any AWS service; invoke any Lambda or run any producer or the build (not even a dry run of the handler: reading its code and calling the reader's `households()` through a read-only reader is the only execution); edit any file outside your folder, the channel and your order; read or record an account id or household id.

<criterion id="DBC126-1-AC1" cell_refs="DB-c-21"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r126/p126_bcw.py" . DBC126-1-AC1</invocation><expect>DBC126-1-AC1 PASS</expect></criterion>
`DBC126-1-AC1` -- the record's silver and gold sections equal a FRESH read made by the checker: the partition counts and newest dates of the two silver tables, the newest dates and row counts of the two Cottonwood gold tables, the `account_dim` household count and accounts without a household, and the crosswalk counts between the two gold tables' accounts. Base: FAIL (no record).

<criterion id="DBC126-2-AC1" cell_refs="DB-c-21"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r126/p126_bcw.py" . DBC126-2-AC1</invocation><expect>DBC126-2-AC1 PASS</expect></criterion>
`DBC126-2-AC1` -- the reporting-gold section agrees with fresh reads and the code: `next_run_source_partition` equals the newest `account_dim` date in a fresh LIST, `next_run_households` equals the checker's own count, the evidence files exist, the output prefix (if any) is inside the Cottonwood gold root and its recorded object count and newest key equal a fresh LIST, the four absent kinds are named in words, and the four hop verdicts are present from the closed set. Base: FAIL (no record).

<criterion id="DBC126-3-AC1" cell_refs="DB-c-21"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r126/p126_bcw.py" . DBC126-3-AC1</invocation><expect>DBC126-3-AC1 PASS</expect></criterion>
`DBC126-3-AC1` -- the bounds: the record carries zero writes and zero invokes, no account id or household id value appears in the record or note, and the only files changed by the worker's own commits since the branch point are in its folder, the channel and its order. Base: FAIL (no record).

<expected_criteria>DBC126-1-AC1, DBC126-2-AC1, DBC126-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files, `git show`, and the read-only AWS calls named above. Writes: the files in `<paths>`. No AWS write, no invoke, no Terraform, no push, no vendor call, no secret read.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A hop that does not hold is a finding in the record and a row, never a repair.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W413-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh` (never `--no-verify`); run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~413/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-21.cottonwood-fwd1-trace-silver-to-gold-to-reporting-gold-read-only.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 13, cell `DB-c-21`.
<owned_cells>DB-c-21</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC126-1-AC1, DBC126-2-AC1, DBC126-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~413/IRPT_DASHBD.TO-DB-c-21.cottonwood-fwd1-trace-silver-to-gold-to-reporting-gold-read-only.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC126-1-AC1,DBC126-2-AC1,DBC126-3-AC1` BEFORE the flip (set the order's status to complete only when all three PASS); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the three criteria's last lines; the four hop verdicts; the record's `account_dim` newest date, rows and households, `next_run_households`, `scheduled_for_cottonwood`, and the output prefix's object count; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: read-only measurements and a record; nothing is created, planned, applied or written to S3.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: only S3 list and get calls; no grant is made or changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the worker reads which files schedule the build; none is read live or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the checker re-reads the S3 plane itself and compares.
</preflight>

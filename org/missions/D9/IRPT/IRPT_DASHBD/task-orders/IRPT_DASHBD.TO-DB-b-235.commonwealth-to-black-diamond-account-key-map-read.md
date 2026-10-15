# TO IRPT_DASHBD.TO-DB-b-235 -- the COMMONWEALTH-TO-BLACK-DIAMOND KEY-MAP READ (round 119, workstream B-49F): does the Cottonwood Black Diamond silver hold a map from the Commonwealth custodian number (the key of Cottonwood's `account_return_daily` history to 2026-06-22) to the Black Diamond account key; the tables and columns, the coverage of the 12 Commonwealth accounts at the frontier under a stated normalisation, or the words that make the seam a SOURCE_BREAK; counts, names and words only; nothing written

<to_id>IRPT_DASHBD.TO-DB-b-235</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~189</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>119</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 119 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-119 ANALYSIS (B-49F) section 2 ruling 3 and section 3 cell 3 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_119_20261015.md` @d856067e84: "a READ: does the Black Diamond silver hold a map from the Commonwealth custodian number to the Black Diamond account key? If yes, the history before 2026-06-23 joins through it, with the map's table and coverage recorded. If no, Cottonwood's account history before 06-23 is reported SOURCE_BREAK at the seam, in words. It is not stitched by guesswork") | **Rows:** IRPT_DASHBD-D2-W189-S<k> | **Decomp cell:** `DB-b-235` (decomposition section 117) | **outcome_ref:** FWD-11 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-189` (branch `wk-IRPT_DASHBD-189`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~189/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes, column NAMES and words only in the repo, a row or your report; never an account number or an account key, a name or a value.

**Why.** Cottonwood's `account_return_daily` gold holds 3,325 date partitions (2013-04-03 to 2026-06-22) from one Commonwealth delivery, keyed by the custodian's own account number (8 or 9 characters; 12 distinct accounts in the newest partition). Cottonwood's household key (`account_dim.household_id`, the household frame) and the Black Diamond silver use the Black Diamond account key (`AccountID`, 11 characters). Zero of the household frame's 999 accounts match the 12 accounts of the frontier partition. The Black Diamond silver `fact_allocations` and `fact_transactions` (bucket `opal-data-assets`, prefix `blackdiamond/cottonwood/silver/`, 14 tables) carry both `AccountID` and columns named `Account Number`, `Original Account Number`, `NFS Account Number` and `Display Number` forms beside it. Whether one of them is the custodian number the history is keyed by, and for how many of the history's accounts, decides whether the history before 2026-06-23 can join a household. This cell reads that and nothing else. A READ: nothing is changed, deployed or written outside your folder.

**The cell (`DB-b-235`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r119/p119_keymap.py` (your criterion; the record's exact fields, the normalisations and what the checker recounts are in its docstring and clauses); `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_account_dim.py` (the Cottonwood Black Diamond silver reader and its grant) and `~161/dry_run_account_dim.py` (how a partition is read); round 116's read `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~405/BD_RETURNS_READ_R116.json` (the layers and tables); `lib/opal_naming.py`.
2. **The tables.** LIST the Cottonwood Black Diamond silver prefix (the 14 table prefixes) and each table's `date=` partitions; record `tables_listed` (14) and `tables_with_partitions`. For each table with partitions read the COLUMN NAMES of its newest partition (the parquet schema) and select as CANDIDATES the tables with a column that looks like the Black Diamond account key (`AccountID`) or a custodian account number (any column whose name contains `Account Number`, `Account Display Number` or `Original Account Number`); for each candidate record `table`, `partition_date` (the newest), `account_key_columns` and `custodian_number_columns` (column names only, as listed in the schema).
3. **The frontier.** The Commonwealth keys: the `account_id` values of the Cottonwood `account_return_daily` newest partition (address `lib/opal_naming.py address("irpt", "cottonwood", "gold", "account_return_daily", "date=<D>", ...)`, newest `D` found by LIST; the checker recounts it): record `frontier` {`date`, `account_ids` (the count of distinct ids), `claim`}. Never write an id.
4. **The map.** Decide whether some candidate table holds, row by row, the Black Diamond key in one column and the custodian number in another (`map.exists` true) and say which (`table`, `key_column`, `custodian_column`). Choose the `normalization` that makes the frontier ids and the custodian column comparable, one of `exact`, `strip_leading_zeros`, `zero_pad_10` (the checker applies exactly the one you name). Read the table at up to 10 of its partitions that you choose to cover its span (the first, the middle and the newest at least; accounts may close between 2026-06-22 and today): record `partitions_read` (their dates) and `coverage` {`frontier_ids`, `mapped` (the frontier ids that appear in the custodian column over those partitions under your normalisation), `unmapped`}. The checker re-reads exactly those partitions and must get the same `mapped`. If NO candidate holds both, `map` is {`exists` false, `words`, `claim`} and `seam_words` must say that Cottonwood's account history before 2026-06-23 is reported SOURCE_BREAK at the seam (the checker looks for the word SOURCE_BREAK).
5. **The history.** Over ALL 3,325 Cottonwood `account_return_daily` partitions (LIST them; read each `data.parquet`'s `account_id` column only, in the background), record `history` {`distinct_commonwealth_ids` (the count of distinct ids over the whole history), `partitions`, `claim`}. When the map exists, `seam_words` states how many of those distinct ids are covered by the map table over the partitions you read (a count; you may add `mapped_history_ids` inside `seam_words` as words only).
6. **Write your analysis as a tracked script** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~189/key_map_read_r119.py` (no write call to AWS; names no other firm's place; writes ONLY a private file under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~189/`).
7. **Record** `RD_KEY_MAP_READ_R119.json` in your folder, counts, names and words only, with EXACTLY these fields: `tables_listed`, `tables_with_partitions`, `candidates` (a list of at least 1, each {`table`, `partition_date`, `account_key_columns`, `custodian_number_columns`, `claim`}), `frontier` {`date`, `account_ids`, `claim`}, `map` (the form of step 4: when `exists` is true {`exists`, `table`, `key_column`, `custodian_column`, `normalization`, `partitions_read`, `coverage` {`frontier_ids`, `mapped`, `unmapped`}, `words`, `claim`}; when false {`exists`, `words`, `claim`}), `history` {`distinct_commonwealth_ids`, `partitions`, `claim`}, `seam_words` (words), `analysis` {`file` "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~189/key_map_read_r119.py", `sha256`, `tracked` true}, `reads` {`s3_reads` (integer), `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}, `claim`, `files_in_repo` false, `served_values_changed` false, `pushed` false, `deployed` false. Every `claim` is one of `measured`, `inferred`, `held`, `absent`. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256`, `vintage` or `date` field; no account number or key.

<criterion id="DB119-3-AC1" cell_refs="DB-b-235"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r119/p119_keymap.py" . DB119-3-AC1</invocation><expect>DB119-3-AC1 PASS</expect></criterion>
`DB119-3-AC1` -- `RD_KEY_MAP_READ_R119.json` has exactly the form of step 7; `tables_listed` equals the checker's own LIST of the silver prefix; every column the record names for a candidate is a column of that table's newest partition (read by the checker); when the map exists its table and both columns are columns of the same table and its `coverage` (`mapped` of `frontier_ids`) EQUALS the checker's own recount over the partitions the record names under the record's normalisation, the frontier ids equal the checker's read of the Cottonwood `account_return_daily` frontier partition; when it does not exist the seam words say SOURCE_BREAK; the analysis script is tracked, hashed as recorded, names no other firm's place and holds no write call; every claim is in the four-word set; zero writes, no push or deploy flags, and no run of 8 or more digits outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DB119-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every adapter, contract, module and test, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET of the Cottonwood Black Diamond silver prefix `blackdiamond/cottonwood/silver/` (listings of its tables and partitions, parquet schemas, and the columns the map decision needs) and the Cottonwood `account_return_daily` gold prefix (the `date=` listing and the `account_id` column), the gold prefix derived by `lib/opal_naming.py address()` and nowhere else. Writes: the repo files of the grant and the private folder named in step 6. No put, copy or delete of any kind, no deploy, no push, no vendor call, no secret read, no read of another firm's place, no Terraform.
- **Client data.** The silver and gold partitions and anything you derive from them are client data: counts, column names, dates, hashes and words only in the repo, a row or your report; never an account number or key.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a prefix cannot be read, record the source `absent` with the refusal named, file a BLOCKING row with counts and stop on that point; an unreadable source is never a zero or a "no map". If your coverage differs from the checker's recount, report both numbers in a BLOCKING row; do not adjust either. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W189-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~189/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-235.commonwealth-to-black-diamond-account-key-map-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 117 (round 119, workstream B-49F), cell `DB-b-235`.
<owned_cells>DB-b-235</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB119-3-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~189/IRPT_DASHBD.TO-DB-b-235.commonwealth-to-black-diamond-account-key-map-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB119-3-AC1` BEFORE the flip; pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the silver tables listed and the candidates with their column names; whether the map exists and, if so, its table, columns, normalisation, the partitions read and the coverage of the frontier accounts; the history's distinct Commonwealth accounts and partitions; the seam words; reads and writes. Counts, names, dates and words only: no account number or key.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and a tracked analysis script with a record in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed; the S3 reads are GET and LIST of the Cottonwood Black Diamond silver and gold prefixes already read by the account_dim adapter, the round-114 and round-116 reads and the round-118 reader.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB119-3-AC1 FAILS at base (no record) and its recount and consistency clauses are exercised by the checker's self-test (two green and eleven red record arms).
lane: the <paths> block IS the grant.
</preflight>

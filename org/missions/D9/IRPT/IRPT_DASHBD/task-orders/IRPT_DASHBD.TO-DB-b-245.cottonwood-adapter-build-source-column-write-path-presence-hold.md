# TO IRPT_DASHBD.TO-DB-b-245 -- the COTTONWOOD ADAPTER BUILD (round 121, workstream B-49F): the Black Diamond account return adapter gains the optional `source` column of contract 0.3.0, a one-day write path (`data.parquet` and `manifest.json` at the builder address), a silver presence hold, a packaging-aware import root and a manifest, LOCAL and tested with fake clients; nothing is landed, scheduled, planned or written to AWS

<to_id>IRPT_DASHBD.TO-DB-b-245</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~199</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>121</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 121 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-121 ANALYSIS (B-49F) section 2 ruling 4 and section 3 cell 3 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_121_20261015.md @9d4bd6adf3`: "the Cottonwood adapter build: the `source` column, the write path, the presence hold, packaging and thresholds, then its landing pair (a `*-cot-*` role and builder names)") | **Rows:** IRPT_DASHBD-D2-W199-S<k> | **Decomp cell:** `DB-b-245` (decomposition section 119) | **outcome_ref:** FWD-11, FWD-21 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-199` (branch `wk-IRPT_DASHBD-199`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~199/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~199/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** Round 119 built `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py`, a pure derivation over the Cottonwood Black Diamond silver (`fact_allocations`, `fact_transactions`) with 19 tests; it writes nothing. Round 120 declared the optional `source` column in the account return contract (0.3.0; `schema_hash` 1b25d37ba6cf unchanged, `schema_hash_with_optional` bc70ee2f2e0b) and read the landing facts (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~195/RD_CW_LANDING_FACTS_R120.json`: the adapter needs six changes before a landing). This cell makes them in the adapter, LOCAL, with fake clients; the landing function, its role, its schedule and the pair are the next round.

**The cell (`DB-b-245`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r121/p121_cotbuild.py` (your three criteria; its `PROBE` text is the behaviour spec: it builds fake S3 and fake reader objects and calls your functions exactly as below); the adapter and its test file `data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_bd_account_return_daily.py` (19 tests, which must still pass UNCHANGED); the facts record above (its `adapter_changes`, `iam`, `schedule` and `names`); the producer `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` (`emit_day`, its manifest keys and `emit_method_row`: the shape a landed partition has); the contract `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` (0.3.0: `optional_columns`, `schema_hash_with_optional`); `lib/opal_naming.py`; the round-120 record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~193/RD_BD_BRONZE_AND_MAP_R120.json` (the silver partitions and the empty days: the first non-empty `fact_allocations` date).
2. **Add to the adapter** (ADDITIVE: at most 12 existing lines may change; the 19-column `ARROW_SCHEMA`, `schema_hash()` and `to_table(rows)` behave exactly as before). Exact names and signatures, because the checker calls them:
   - `SOURCE_COLUMN = "source"`; `schema_hash_with_optional() -> str`: the sha256 over the sorted `name:type` lines of the 19 columns plus `source:string` (the contract's `schema_hash_with_optional`; the checker compares).
   - `to_table(rows, with_source=False)`: unchanged with `False`; with `True` a 20-column table whose last column `source` (nullable string) holds `LABEL` on every row.
   - `class GoldWriteError(PermissionError)`; `gold_prefix() -> (bucket, key_prefix)`: from `opal_naming.address("irpt", FIRM, "gold", TABLE, "date=2000-01-03", "data.parquet")`, the key prefix up to and including the `date=` parent (ends in `/`, holds `account_return_daily`): NO bucket, firm or prefix typed.
   - `build_manifest(day, table, first_data_date) -> dict` with at least the keys `table, firm, business_date, rows, schema_version, method_version (2), label, columns (the table's 20 column names), schema_hash_with_optional, contract_version ("0.3.0"), first_data_date, thresholds_claim`. Mirror the producer's manifest where it makes sense; the guard `thresholds` do not exist for this derivation, so `thresholds_claim` is "absent" and the words say why.
   - `write_day(s3, day, table, manifest) -> {"keys": 2, "rows": n}`: puts EXACTLY two objects with `s3.put_object(Bucket=, Key=, Body=bytes)`: `<prefix>date=<day>/data.parquet` and `<prefix>date=<day>/manifest.json`, calls NO other client method, and raises `GoldWriteError` WITHOUT any call when `day` is not a real ISO date, the table has no rows, or `manifest["table"]` is not `TABLE`.
   - `presence_hold(reader, day) -> str | None`: `None` when BOTH `fact_allocations` and `fact_transactions` hold a partition for `day` and the allocations partition has rows; otherwise a string starting `"HOLD"` naming what is missing (the reader is the existing silver reader's interface: `list_partitions(table)`, `read_parquet(table, day)`).
   - `run_day(reader, s3, day, upload=True) -> dict` with keys `day, held, reason, rows`: a held day writes NOTHING and returns `held` true; otherwise it derives the day's rows with the existing `derive` over the accounts of that day's allocations partition from the previous trading day to `day` (`tc.prev_trading_day`), keeps the rows of `business_date == day`, builds the 20-column table, the manifest and (when `upload`) calls `write_day`.
   - `_find_root(start) -> Path`: walks up from `start` to the first directory holding `lib/opal_naming.py` (else the current directory); use it for `_ROOT` in place of `parents[6]`, so the module imports from a Lambda bundle laid out like the repo.
   - a module constant `FIRST_DATA_DATE` (the earliest non-empty `fact_allocations` partition, from the round-120 record, cited in a comment) which `run_day` passes to `build_manifest`.
3. **Tests**: append at least 8 tests to the existing test file (no network; fake client and fake reader like the checker's): the two hashes; 19 and 20 columns and the `source` value; `write_day` writes exactly two keys under the builder prefix and refuses an empty table, a bad day and another table without a call; `presence_hold` for a missing transaction partition, an empty allocation partition and a full day; `run_day` held writes nothing; `run_day` full writes two objects of 20 columns for the right day; `upload=False` writes nothing; `_find_root`. The whole file passes (19 earlier plus yours, at least 27).
4. **The decision on the method row, stated by the issuer:** this adapter does NOT write the `dim_return_method` row (its prefix is outside the one-prefix write grant the landing facts name; row `W195-S2`); the manifest carries `method_version` 2 and the label. Record `method_row` {`decision` "NOT_WRITTEN_BY_THIS_ADAPTER", `words`}. If you find a reason the page cannot work without the row, file a BLOCKING row; do not write it.
5. **The facts record** `RD_CW_BUILD_FACTS_R121.json` in your folder with EXACTLY these fields: `adapter` {`file`, `functions_added` (a list that includes every function named above), `source_column_values` (a list holding the label), `hash_with_optional` (64 hex), `words`}; `tests` {`file`, `new_tests`, `total`}; `manifest` {`keys` (the list of the manifest's keys), `first_data_date` (ISO), `thresholds_claim` ("absent"), `words`}; `packaging` {`find_root` true, `source_map_row_needed` (boolean: does a bundle need a source-map row for this module and `lib/opal_naming.py` once a landing function exists; say what you read), `words`}; `method_row` (step 4); `files_changed` (a list of the adapter and the test file, each {`file`, `sha256` (of the bytes at your final commit), `kind`}); `words`; `claim`; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256`, `vintage` or `first_data_date` field.

<criterion id="DB121-4-AC1" cell_refs="DB-b-245"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r121/p121_cotbuild.py" . DB121-4-AC1</invocation><expect>DB121-4-AC1 PASS</expect></criterion>
`DB121-4-AC1` -- the adapter defines the eight functions of step 2, `GoldWriteError` and `SOURCE_COLUMN`; the test file holds at least 27 tests and `pytest` on it passes (the 19 earlier tests included). Base: FAIL (the functions are missing).
<criterion id="DB121-4-AC2" cell_refs="DB-b-245"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r121/p121_cotbuild.py" . DB121-4-AC2</invocation><expect>DB121-4-AC2 PASS</expect></criterion>
`DB121-4-AC2` -- the checker's behaviour probe, run in a child python with fake clients, finds: the 19-column hash and the with-optional hash equal the contract's; 19 and 20 columns; `source` equals the label on every row; `gold_prefix()` well formed; the manifest keys, method version 2, 20 columns and the contract's with-optional hash; `write_day` puts exactly the two keys under the builder prefix in the builder bucket and refuses an empty table, a bad day and another table with `GoldWriteError` and no call; `presence_hold` holds on a missing transaction partition and on an empty allocation partition and is `None` on a full day; `run_day` writes nothing on a held day, two objects on a full day (two rows of 20 columns for that day, a full manifest) and nothing with `upload=False`; `_find_root` walks up to `lib/opal_naming.py`. Base: FAIL (the functions are missing).
<criterion id="DB121-4-AC3" cell_refs="DB-b-245"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r121/p121_cotbuild.py" . DB121-4-AC3</invocation><expect>DB121-4-AC3 PASS</expect></criterion>
`DB121-4-AC3` -- `RD_CW_BUILD_FACTS_R121.json` has exactly the form of step 5 and its files hash as recorded; the change is ADDITIVE against the commit that issued this order: the adapter gains at least 60 lines and loses at most 12, the test file gains at least 50, and no other file under `data/`, `infra/`, `lib/` or `org/standards/` changes. Base: FAIL (no record).

<expected_criteria>DB121-4-AC1,DB121-4-AC2,DB121-4-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the producer, the Inflection adapter, every other test, every contract, `lib/`, `sources.json`, Terraform and Lambda files, the source map, round 119's and 120's records, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files. The tests use fake clients; no network, no AWS call, no S3 read or write, no Terraform command, no deploy, no push, no vendor call, no secret read. Writes: the repo files of the grant.
- **Client data.** None is involved; test fixtures are synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the contract's `schema_hash_with_optional` does not reproduce from the 19 columns plus `source:string`, or an existing test fails after your edit and cannot be kept unchanged, file a BLOCKING row with the numbers and stop on that point. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W199-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py
data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_bd_account_return_daily.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~199/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-245.cottonwood-adapter-build-source-column-write-path-presence-hold.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 119 (round 121, workstream B-49F), cell `DB-b-245`.
<owned_cells>DB-b-245</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB121-4-AC1, DB121-4-AC2, DB121-4-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~199/IRPT_DASHBD.TO-DB-b-245.cottonwood-adapter-build-source-column-write-path-presence-hold.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB121-4-AC1,DB121-4-AC2,DB121-4-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the functions added; the two hashes (first 12 characters); the manifest keys; the test counts; the method-row decision; what a landing function still needs. Words and counts only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: an adapter, its tests and a facts record in a branch; nothing is wired, landed, scheduled or written to AWS.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written; the write path is exercised only with fake clients.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its probe was validated by the issuer against a scratch reference implementation (green), and its clauses by its self-test (eleven red probe arms, eight red facts arms).
lane: the <paths> block IS the grant.
</preflight>

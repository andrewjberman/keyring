# TO IRPT_DASHBD.TO-DB-b-199 -- the MODEL DAILY SERIES INTO THE REPORT'S GOLD: the table's contract (C-SHAPE), its producer module and offline tests, and the NEVER-WIDEN PACKET for the one write (the exact keys, the rollback, that no other key moves); source and data_as_of claimed; nothing is written to AWS

<to_id>IRPT_DASHBD.TO-DB-b-199</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~164</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>104</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-104 ANALYSIS item 3 ("the model daily series into the report's gold (ruling 7511), with source and data_as_of claimed. Each packet names the exact keys written, the rollback, and that no other key moves.") and msg 7534 (before any candidate or approval row the model series lands in the report's gold and the render reads it from there) | **Rows:** IRPT_DASHBD-D2-W164-S<k> | **Decomp cell:** `DB-b-199` (decomposition section 106) | **outcome_ref:** FWD-21 | **depends_on:** none (round 103's `DB-b-194` built the figures privately from the served series).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-164` (branch `wk-IRPT_DASHBD-164`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~164/`.

**Why.** The performance report's 32 benchmark members and its 12-month chart are computed from Opal's model benchmark returns, which today exist only as served JSON (MDPF's `yang-model-portfolio-benchmarks` writes a pickle into JSON; there is no gold: row IRPT_DASHBD-D2-S27). The report serves only from Opal's own gold (PRD C-SHAPE), so before any candidate or approval row the series must land in the report's gold with its source and `data_as_of` claimed (a value must carry its claim), and the render must read it from there. The CTO's ruling: the gold home of the model series as MDPF's own product is MDPF's later migration (R19, not a rider here); THIS project lands the series it reads as an INPUT in its own gold. Landing is a gold WRITE, so it goes under a never-widen pair; this cell builds everything the pair needs and writes nothing.

**What exists to read.** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~159/` (`BENCHMARK_FILL.json`, `build_sample.py` and its `model_series()` input function, the normalisation of the served series into daily decimal returns per stem: read how it derives them), `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~157/BENCHMARK_SOURCE_READ.json` (the producer, the served object `s3://opal-data-portal-v2/json/benchmarks/model_portfolio_timeseries.json` and its shape), the PRD (`org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md`: C-SHAPE names `market_topic_daily` among the eight account-grain tables; read what it is for and what the backend brief's Part V.1 says it carries), the sibling contracts `org/standards/IRPT_DASHBD_*_CONTRACT.json` (the model of a table contract), the 49 Financial gold producer `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` (`ARROW_SCHEMA`, `emit_day`, `address()` use, `data.parquet` and `manifest.json` per partition), the Cottonwood adapter (`data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_account_dim.py`, a model of an adapter with an `upload=False` default) and the never-widen packet model `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_PACKET_FDRXX_CASH_CLASSIFIER.md` (its section headings are the packet's required headings).

**The cell (`DB-b-199`): build, local, NO write to AWS.**
1. **Choose the gold table and say why.** The table is the C-SHAPE table that fits a firm-neutral market series (`market_topic_daily` unless the PRD and the brief show another table is meant): record `table`. Read what C-SHAPE requires of every table (`firm`, `account_id`, `method_version`, `coverage`; "a firm that lacks a field carries null plus a `coverage` value that says why") and apply it to a market series without inventing a firm-specific column. Name the firm scope the landing uses (the report is read per firm; the model series is Opal's own: say which firm gold home the series is written under and why, deriving it only from `lib/opal_naming.py address()`: the `address_args` you record are the five arguments, for example `["irpt", "<firm>", "gold", "<table>", "date=<D>"]`).
2. **The contract.** Author the table's contract `org/standards/IRPT_DASHBD_<TABLE>_CONTRACT.json` in the sibling shape: `table`, `grain`, `partition` (`date=YYYY-MM-DD`), `producer` (the module's repo path), `columns` (names and arrow types; they carry the four model stems' daily returns, the series' `source` and its `data_as_of`, and the C-SHAPE columns), `enums`, `schema_hash` and `schema_hash_basis` EXACTLY as the sibling `account_return_daily` contract states them (sha256 over the sorted `name:type` lines joined by newline, types as the pyarrow type name the producer's `ARROW_SCHEMA` carries), `firm_specific_columns` ("NONE ..."), `rule24_record` as the siblings carry one.
3. **The producer.** A module `data/assets/scripts/gold/irpt_reporting/adapters/model_series_<table>.py` exposing `ARROW_SCHEMA` (a `pyarrow.schema` whose hash equals the contract's) and a pure function turning the normalised daily series into one table partition per trading date, each row carrying the source (the served object's name) and the series' `data_as_of`. The served series is read behind ONE input function (a firm-neutral model input), with an `upload=False` default; every S3 address from `lib/opal_naming.address()` and every resource name from `name()` (CLAUDE.md rule 30: a builder refusal is a missing registry row: file a row and stop). Nothing is written to AWS in this cell.
4. **Tests.** `data/assets/scripts/gold/irpt_reporting/tests/test_model_series_<table>.py` (offline, synthetic series): the output schema hash equals the contract's; one row per trading date; the source and `data_as_of` columns are present and filled; a series that ends before `data_as_of` is refused or flagged, never extended. 3 or more tests; ONE temporary mutant (drop the `data_as_of` column) that a test catches, then reverted. Run `python -I -m pytest -q <file>` and `bash .tools/commit-gate.sh <file>` on every `.py` you touch.
5. **The packet.** `MODEL_SERIES_GOLD_PACKET.md` in your folder, modelled on the FDRXX packet, with these numbered sections (the checker looks for the headings `## 1. The act`, `## 2. What moves`, `## 3. When and where`, `## 4b. Writers`, `## 5. Both branches`, `## 6. Rollback`, `## 7. Conditions`, `## 8. Not established`, and the words "never-widen"): (1) the act: ONE landing of the series into the report's gold; the exact keys written (bucket, prefix from `address()`, the number of `date=` partitions the FIRST apply writes and objects per partition: `data.parquet` and `manifest.json`), by whom (an AE applier) and with what exact invocation shape (no live run); (2) what moves, measured: the partition count and date range the series covers (counts and dates only), the Opal figures that change in the report afterward (the 32 benchmark members and the chart read from gold instead of the private computation: say what stays equal); (3) when and where it takes effect; (4b) the writers of the property: count every writer of the target prefix (N is printed; the expectation is none, since nothing writes this table today: verify by the repo and the schedules); (5) both branches: a run that lands and a run that fails part-way (an apply that fails after some partitions); (6) the rollback per key (S3 versioning state of the bucket read live, delete of the new keys, the exact keys); that NO other key moves (the target prefix is new: confirm it holds nothing today by a named-prefix LIST); (7) the conditions of the apply and the questions for the CTO's half; (8) what is not established and so not covered.
6. **Record** `MODEL_SERIES_GOLD_PACKET.json` in your folder with exactly: `contract_file`; `table`; `producer` {`file`, `sha256`, `tracked` true}; `tests` {`file`, `passed`, `failed` 0, `mutant_failed` true}; `address_args` (the five strings); `keys_written` (a list of `{bucket, prefix, objects_per_partition}` where each prefix lies under the `address()` home); `rollback` (words); `no_other_key_moves` true; `writes_in_this_cell` false; `source_claim` (words: what the figures claim as their source); `data_as_of` (ISO date of the series); `packet_file` (repo-relative path); `packet_sha256`; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, names and words only: no benchmark figure; a sha256 value is exempt from the digit rule.

<criterion id="DB104-3-AC1" cell_refs="DB-b-199"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r104/p104_round104.py" . DB104-3-AC1</invocation><expect>DB104-3-AC1 PASS</expect></criterion>
`DB104-3-AC1` -- the contract exists with its table, schema hash and hash basis; the producer is a tracked .py under data/assets/scripts/gold/irpt_reporting/ whose bytes hash as recorded and whose ARROW_SCHEMA hashes (recomputed by the checker, same method) to the contract's schema_hash; the tests pass when the checker runs them (3 or more, a failing mutant); the address_args resolve through lib/opal_naming.address() and every key written lies under that home; the rollback is stated, no other key moves, nothing is written in this cell, the source claim and an ISO data_as_of are carried; the packet file exists, is hashed, says never-widen and carries the eight numbered sections; no write, push or deploy. Base: FAIL (no record).

<expected_criteria>DB104-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the performance report contract (a later round repoints its source to this table), `~159/build_sample.py` and the other contracts.
- **No write of any kind to AWS** (no S3 put/copy/delete, no DynamoDB write, no Lambda, EventBridge, Terraform or IAM act), **no deploy, no push, no vendor call (no YCharts), no secret read.** Reads only: repo files; S3 named-prefix LIST and single-object GET (the served series object; the target prefix LIST that proves it is empty; `get-bucket-versioning`). Every bucket from `lib/opal_naming.address()`, never `data/firm_registry.json`'s bucket field. A denial is recorded verbatim, not retried by another route. If the comp-rail hook refuses a raw S3 call, run what it says next or annotate `# rail-checked: <why>`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. Where you cannot establish something say NOT_ESTABLISHED with the reason; never guess. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W164-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~164/
org/standards/IRPT_DASHBD_MARKET_TOPIC_DAILY_CONTRACT.json
data/assets/scripts/gold/irpt_reporting/adapters/
data/assets/scripts/gold/irpt_reporting/tests/test_model_series_market_topic_daily.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-199.model-series-into-the-reports-gold-contract-producer-and-packet.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 106 (round 104), cell `DB-b-199`.
<owned_cells>DB-b-199</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB104-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~164/IRPT_DASHBD.TO-DB-b-199.model-series-into-the-reports-gold-contract-producer-and-packet.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB104-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the table you chose and why; the contract's columns (names); the firm gold home and its address() arguments; the tests and the mutant; the keys the first apply writes (patterns and counts); the writers counted; the rollback; what is not established; row ids. Counts, names and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a contract, a producer module, tests and a packet, local; nothing is served, wired, written or deployed; the apply is a later WORLD order under a pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: named-prefix LIST, one GET and a versioning read with the box's existing identity; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the landing's schedule is a later packet.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record) and is dry-run on 5 synthetic arms.
lane: the <paths> block IS the grant.
</preflight>

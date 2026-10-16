# TO MDPF_SECCLASS.TO-SC-e106.four-ticker-seed-evidence -- round 26 SC-e-106: the evidence for the four tickers (HPI, CUBE, GLPI, PCEF) the shared list has no row for: lots, canonical holdings, source rows; nothing guessed, nothing written

<to_id>MDPF_SECCLASS.TO-SC-e106</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~96</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-106` (`decompositions/MDPF_SECCLASS_DECOMP_R26.md`) |
**outcome_ref:** FWD-3 (list maintenance) | **depends_on:** none | **source:** CTO round-25 analysis section 2 item 4; STATUS.md item 2a pre-read @18f5c9ad3c; CTO msg 5510

---

## WORKER FACE

### THE CELL

`SC-e-106`. The shared classification list is the DynamoDB table `etf-classifications` (us-east-1, key `ticker`). Four tickers held by clients have no row in it: `HPI`, `CUBE`, `GLPI`, `PCEF` (the CVO measured about $63,967.82 across them on the 2026-10-09 lots; the issuer read $62,906.43 from `s3://opal-data-bd/gold/holdings_lots/2026-10-09.parquet` at 03:4xZ today: your figure may differ and you report yours). The list's maintainer is this project (its PRD names it the writer of the seed rows). A row is added only from a SOURCE ROW: the rules of the seed script `infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py` read the Bloomberg GICS data and the Schwab master first; **no outside model is used** (it needs Andrew's word) and **nothing is guessed**: where no source holds the ticker, you record that, and propose no row. This cell only gathers and records the evidence; the issuer writes the signed pair and a CloudOps seat writes any row later. **You write nothing to S3 or to a table.**

**What you build:**
1. Read the header and the source-reading code of `seed-etf-classifications.py` and list, in the record, every source it reads for a class (name the bucket and key or the file), in the order it tries them.
2. For each of the four tickers read, read-only: (i) the open lots rows in `s3://opal-data-bd/gold/holdings_lots/2026-10-09.parquet` (columns `ticker`, `asset_name`, `cusip`, `market_value`, `is_open`; read the parquet with pandas from the object's bytes and filter; record each distinct (asset_name, cusip) with the summed market value and the row count); (ii) the rows of the canonical holdings partition `gold/canonical/holdings/2026-10-09.parquet` (same bucket; if the key is not found, list the prefix `gold/canonical/holdings/` and use the 2026-10-09 file) whose ticker equals it; (iii) whether the ticker has a row in `etf-classifications` (`get_item`); (iv) every row each seed source in step 1 holds for the ticker or its CUSIP, with the source name, the key you read it from, and its class and sub-class values as the source states them.
3. Write the evidence file `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~96/FOUR_TICKER_SEED_EVIDENCE.json`, exactly: `{"tickers": {"HPI": {...}, "CUBE": {...}, "GLPI": {...}, "PCEF": {...}}, "outside_model_used": false, "sources_read": [...], "read_at": "<UTC>"}`, each ticker entry with `lots_rows` (list of `{asset_name, cusip, market_value, row_count}`), `canonical_holdings_rows` (integer), `source_rows` (list of `{source, key, asset_class, sub_asset_class}`, empty when no source holds it), `proposed_row` (`null` when `source_rows` is empty; otherwise `{asset_class, sub_asset_class, source}` copied from the source row, folded to the table's six-class vocabulary only by a rule you cite from the seed script) and `table_row_present` (boolean, the live read). The check refuses a `proposed_row` with no source row.
4. Do not touch `etf-classifications`, the seed script or any other file.

### ACCEPTANCE

<criterion id="SC26-e106-AC1" cell_refs="SC-e-106"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R26_CHECKS/check_four_ticker_evidence.py org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~96/FOUR_TICKER_SEED_EVIDENCE.json</invocation><expect>FOURTICKER ok=True</expect></criterion>
`SC26-e106-AC1` -- the file has the four tickers and every field, no proposed row without a source row, no outside model, and `table_row_present` equals a live read.

<criterion id="SC26-e106-AC2" cell_refs="SC-e-106"><invocation>bash -c 'git diff --name-only box/dell1...HEAD -- data infra lib | wc -l'</invocation><expect>0</expect></criterion>
`SC26-e106-AC2` -- the control that you changed no code.

<expected_criteria>SC26-e106-AC1, SC26-e106-AC2</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-16 ~03:5xZ): AC1 FAILS as expected (`FOURTICKER ok=False file=ABSENT`, rc 3); AC2 PASSES as expected (`0`). The check's green arm (a generated file, four tickers, no proposed rows, live read False each) read `ok=True`; its negative arm (a proposed row with no source row) read `ok=False`.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, curl or tool fetch). pandas, pyarrow and boto3 are already installed.
- **AWS is READ-ONLY** (get, list, head, query, scan, list_object_versions): no write to any bucket or table, no deploy, no invoke. Never push.
- **Client data stays out of the report and the surprise rows beyond what the evidence file needs:** no client name and no account id anywhere (the lots read is aggregated by ticker).
- **Never edit** anything outside the `<paths>` block; the check scripts under `R26_CHECKS/` are READ-ONLY to you. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id `MDPF_SECCLASS-D1-W96-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken a check, and do not edit a check to make it pass.
- Run every invocation under `timeout 120`; the checks end well inside it.

<paths>
org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~96/FOUR_TICKER_SEED_EVIDENCE.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R26.md</decomp_doc> (round 26), cell `SC-e-106`.
<owned_cells>SC-e-106</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC26-e106-AC1, SC26-e106-AC2. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~96/MDPF_SECCLASS.TO-SC-e106.four-ticker-seed-evidence.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC26-e106-AC1,SC26-e106-AC2`.
</proof_of_spec>

**REPORT:** the sources the seed script reads (names and keys), per ticker the lots figure and the canonical-holdings count, which source rows you found, each criterion's output verbatim, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE nothing is scheduled; nothing ships.
comp-iam: DECLARED-NOT-APPLICABLE only the reads the seat's role already makes.
comp-adversary: RUN -- a class proposed from a ticker's name or an outside model (forbidden; the check refuses a proposed row without a source row, and the file states `outside_model_used: false`); a lots figure read from a stale partition (the file carries the partition key and read time); BLIND: a ticker held only in a partition after 10-09.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-25 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_25_20261016.md`, msg 6457); DECOMP_R26.

# NFRA_MCPINDEX task order -- `MX-z-1` -- for each of the 15 live tables the catalog does not describe, write the catalog row it needs or the reason none is written, grounded in the CRO brief and the census

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round26-GATEWAY.md</decomp_doc>
<owned_cells>MX-z-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-z-1.uncatalogued-rows</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~90</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one JSON data file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base) and the planted mutants inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-z-1` (round 26, workstream GATEWAY; PRD v0.19 FWD-23; CTO round-25 analysis item 1 and the CTO ruling on the advisor tables per vendor)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). The CRO brief `4.0.0_SA_CRO~Y` measured the live buckets and found 15 production tables that the gateway catalog has no row for, so the gateway cannot see them. The CTO ruling says each gets a catalog row, or a stated reason, with `opal-data-inf/silver/transactions` first: it is the only Orion table that carries advisor attribution. This cell decides, for each of the 15, the row it needs (the issuer writes the row into the catalog at the drain; you write the specification of the row) or the reason none is written.

**What to build.** `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~90/uncatalogued_rows.json`, one item for each of these 15 tables, exactly these and each once, in this order (the first item is `opal-data-inf` `silver/transactions/`; the other 14 follow sorted by bucket and then prefix):

| bucket | prefix | table | newest partition | partitions | rows |
|---|---|---|---|---|---|
| opal-data-inf | silver/transactions/ | transactions | 2026-10-20 | 1663 | 1,526,116 |
| opal-data-bd | silver/assets/ | assets | 2026-06-18 | 1890 | 25,332 |
| opal-data-bd | silver/prices/ | prices | 2026-10-20 | 180 | 11,181 |
| opal-data-bd | silver/realized/ | realized | 2026-10-20 | 1363 | 54,843 |
| opal-data-bd | silver/transactions_enriched/ | transactions_enriched | 2026-04-20 | 518 | 45 |
| opal-data-inf | silver/accounts_dim/ | accounts_dim | none | 0 | 835 |
| opal-data-inf | silver/api_dims/ | api_dims | none | 0 | 0 |
| opal-data-inf | silver/assets_v2/ | assets_v2 | 2026-10-20 | 2367 | 37,026 |
| opal-data-inf | silver/eclipse/ | eclipse | 2026-10-20 | 142 | 846 |
| opal-data-inf | silver/meta/ | meta | none | 0 | none |
| opal-data-inf | silver/orion-rest/performance_weekly/ | performance_weekly | none | 0 | 309 |
| opal-data-inf | silver/orion-rest/transactions/ | transactions | none | 0 | 1,249,183 |
| opal-data-inf | silver/performance/ | performance | 2026-10-20 | 140 | 484,861 |
| opal-data-inf | silver/performance_dim/ | performance_dim | 2026-05-13 | 1 | 95,364 |
| opal-data-inf | silver/prices/ | prices | none | 0 | 1,477,938 |

(These are the 15 entries whose `src` is `live-extra` in the census file named below; the table is the census's own and is the authority if this list and the file ever differ.)

### The contract (verbatim from the decomposition; it is the whole specification)

**Z1 UNCATALOGUED ROWS** `uncatalogued_rows.json`, schema `gateway_uncatalogued_rows/1`: `{"schema","items":[{"table","bucket","prefix","disposition":"row"|"reason","row":null|{"entity","bucket","prefix","vendor","firm","table"},"reason":str,"evidence":[str,...]}]}`. One item for each of the 15 entries of `4.0.0_SA_CRO~Y/census.json` whose `src` is `live-extra`, exactly those, once each, keyed by (`bucket`,`prefix`); `table` equals the census `table`. The item for `opal-data-inf` prefix `silver/transactions/` is FIRST in the list; the rest are sorted by (bucket, prefix). `row`: a catalog row the table reads as, with `entity` a lower-case word-and-underscore id not already an entity of the catalog and not repeated, `bucket` and `prefix` equal to the item's, `vendor` one of the catalog's vendors plus opal, ycharts, microsoft, bloomberg, other (the vendor that produces the table: orion, eclipse, blackdiamond etc. as the catalog names them), `firm` a string. `reason`: for a `row` item, one ASCII sentence of at least eight words on what the table holds; for a `reason` item, at least eight ASCII words saying why no row is written (an empty table, a meta folder, a copy that duplicates a catalogued table). `evidence` has at least one entry: `<path>:<line>` of a file that exists, or `census.json#<bucket>/<prefix>` that resolves in the census file. A `reason` item may not be chosen for `opal-data-inf/silver/transactions/`, `opal-data-inf/silver/orion-rest/transactions/` or `opal-data-bd/silver/realized/` (live advisor or realized data).

### Inputs you read (you do NOT edit them)

- the census `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/4.0.0_SA_CRO~Y/census.json`: a list of 139 tables, each `{src, bucket, prefix, address, table, objects, parquet, partitions, first_partition, newest_partition, newest_modified_utc, schema_key, rows, columns}`; `columns` are `name:type` strings. A key in your `evidence` of the form `census.json#<bucket>/<prefix>` (for example `census.json#opal-data-inf/silver/transactions/`) must name one of its entries.
- the CRO brief `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/4.0.0_SA_CRO~Y/ADVISOR_TABLES_PER_VENDOR_BRIEF_20261020.md`: section 1 (vendors, firms, tables), sections 4.1 to 4.7 (per vendor: tables, columns, freshness), section 6 (the 15 tables with no row, line 232 on), section 7 (what must be built). Cite its lines as `<path>:<line>` evidence.
- the catalog `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` (read-only): the section `silver_datasets` holds the rows; each row has `entity`, `bucket`, `prefix`, `vendor`, `firm`. Read the existing rows of the same vendors (for example `blackdiamond_live_transactions`, `blackdiamond_live_allocations` in `opal-data-bd`, and the `opal-data-assets` rows `opal_data_assets_silver_orion_*` and `opal_data_assets_silver_eclipse_*`) as the MODEL of a row and of an entity name.
- the entity files `workflows/atom_decomposition/catalog_entries/*.yaml` (read-only): the authoring form of those rows.
- the gateway source `infra/aws/ec2/opal-gateway/app/` (read-only) when an adapter reads one of the tables.
- the vocabulary of `vendor`: the catalog's own vendors (`blackdiamond`, `commonwealth`, `eclipse`, `gateway`, `market`, `orion`, `schwab`, `smartx`) plus `opal`, `ycharts`, `microsoft`, `bloomberg`, `other`.

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The worktree carries the sparse folders `workflows/atom_decomposition` and `infra/aws/ec2/opal-gateway/app` and the issuer has also added `workflows/gateway_battery`; `git sparse-checkout add infra/aws/ec2/opal-gateway/app workflows/atom_decomposition workflows/gateway_battery` is the only sparse change you may make.
1. For each of the 15 tables, read its census entry (columns, partitions, newest partition, rows) and the brief's lines about it. Decide per table:
   - the table holds data an advisor tool or the catalog's users could ask for, and no catalog row describes it: disposition `row`. Write one row: `entity` a new lower-case word-and-underscore id in the style of the catalog (`<bucket underscored>_<prefix path underscored>` such as `opal_data_inf_silver_transactions`, or the `blackdiamond_live_<table>` style for the live Black Diamond tables), not an entity of the catalog and not used by another item; `bucket`, `prefix` and `table` equal to the item's; `vendor` the vendor that produces the table (the brief's section 1 names Orion and Eclipse output at `opal-data-inf/silver/` and the live Black Diamond tables at `opal-data-bd/silver/`); `firm` the firm the data belongs to (the brief's section 1: inflection for Orion and Eclipse, 49financial for Black Diamond 49F), or `none` for Opal's own data; `reason` one plain sentence of at least eight words saying what the table holds, with its row count and newest partition where the census gives them.
   - the table is empty, a meta folder, or a copy that duplicates a catalogued table: disposition `reason`, `row` null, `reason` at least eight ASCII words saying which of these it is and, for a duplicate, the catalogued entity it duplicates. You may NOT choose `reason` for `opal-data-inf/silver/transactions/`, `opal-data-inf/silver/orion-rest/transactions/` or `opal-data-bd/silver/realized/`.
   - an undated table (newest partition `none`, zero partitions) that has rows is a single-object table: it can still take a `row`, say so in the reason.
2. `evidence` of each item has at least one entry: the brief line that names the table (`<path>:<line>`, the path relative to the repository root), and where useful the census entry as `census.json#<bucket>/<prefix>`.
3. Write the file with the Write tool (JSON, `indent=1`, ASCII), then run both criteria until each prints `RESULT: PASS`. Read `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z1_check.py` for exactly what each arm grades.
4. Then spot-check yourself: open five of your items at random, re-read the census entry and the brief line you cited, and fix any that is wrong. The issuer reads a sample at the drain.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's checks or decomposition, `members.yaml`, `pending_members.yaml`, the catalog or its row files, the census or the brief, the emitter (`emit_catalog_v02.py`), any file under `infra/` or `app/`, the PRD, or any other file under `workflows/`. No AWS call, no network call, no grant, no deploy, no push.
2. ASCII only in the data file. You write one data file and no code.
3. The data file is JSON written with the Write tool, `indent=1`, ASCII.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z1.AC1.sh` and `.AC2.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z1_check.py`). Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~90/uncatalogued_rows.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~90/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-z-1.uncatalogued-rows.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W90-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 3)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-z-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z1.AC1.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~90/uncatalogued_rows.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line (15 live-extra tables in scope); the schema; exactly the 15 census tables, each once, keyed by bucket and prefix, with the census table name, a disposition row or reason, a row object for row and null for reason, a non-empty ASCII reason; the item for opal-data-inf silver/transactions first and the rest sorted; no reason item for the three live advisor or realized tables; the planted mutants (a table dropped, a table twice, a foreign table, a wrong schema, a bad disposition, a table name altered, the first item moved, a reason for inf silver/transactions, a reason for orion-rest/transactions, a reason for bd realized, a non-ASCII reason) are each refused -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-z-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z1.AC2.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~90/uncatalogued_rows.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line; every row item has a new unique entity absent from the catalog, a bucket, prefix and table equal to its item, and a vendor in the vocabulary; every item has a reason of at least eight ASCII words and at least one evidence entry that resolves (an existing file and line, or a census entry); the planted mutants (an entity already in the catalog, an entity used twice, a row bucket altered, a row prefix altered, a row table altered, a vendor outside the vocabulary, a three-word reason, a non-ASCII reason, evidence naming a missing file, evidence past the end of the file, evidence naming a census entry that does not exist, no evidence) are each refused -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~90/NFRA_MCPINDEX.TO-MX-z-1.uncatalogued-rows.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes. The checker matches `expect` as a regex against your recorded output: encode the literal printed tokens, replacing digits with `[0-9]+` where counts may differ, and disclose that in a row.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip. The proof instance names the order id in full: `NFRA_MCPINDEX.TO-MX-z-1.uncatalogued-rows`.
4. Report once, with: what you built by part (rows versus reasons, how many of each); every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 26, workstream GATEWAY, worker ~90. Source: the CTO's round-25 analysis `ledger/ROUND_ANALYSIS.round25.md` item 1 (`1.0.0_SA_CTO~Z`, 2026-10-20 ~18:1xZ) and the CTO ruling `CTO_RULING_ADVISOR_TABLES_PER_VENDOR_ROUTING_20261020_Z.md` (catalog: the 15 live tables with no catalog row get rows, or a stated reason, `opal-data-inf/silver/transactions` first), on the CRO~Y brief `ADVISOR_TABLES_PER_VENDOR_BRIEF_20261020.md` @1ce8848c4b section 6. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round26-GATEWAY.md` (the contract R26.3 Z1 is frozen at the cut). Round 24 and 25 lessons carried into the face: the sparse step names the three folders and the issuer pre-adds them; every read in the check of a file whose name or variable holds log or catalog uses errors="replace"; each planted mutant is planted from the data present (the check builds a clean synthetic document from the census, so every mutant runs whatever the worker wrote). Base dry-runs 2026-10-20: `z1.AC1 base: FAIL as expected` and `z1.AC2 base: FAIL as expected` (the deliverable is absent; the control and planted-negative arms pass, only the final deliverable arm fails). A scratch reference file (not committed; built from the real census, the CRO brief and the catalog: thirteen row items and two reason items) passes `z1.AC1` and `z1.AC2`; the checks prove shape, ordering, uniqueness and grounding, not that a row-versus-reason judgment is right, which the issuer reads at the drain. The check takes the vendor vocabulary from the live catalog plus the five extra names, as the round-24 W5 check did. Gate limb that grades this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>26</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

<status>complete</status>

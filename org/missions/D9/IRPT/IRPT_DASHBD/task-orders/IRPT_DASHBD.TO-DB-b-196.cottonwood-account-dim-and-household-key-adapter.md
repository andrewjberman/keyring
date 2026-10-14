# TO IRPT_DASHBD.TO-DB-b-196 -- the COTTONWOOD ADAPTER, first table: account_dim and the household key (the Black Diamond relationship id) from Cottonwood's silver, under the account_dim contract (C-SHAPE), with its tests and a read-only dry run on Cottonwood's own silver prefix; nothing is written to AWS

<to_id>IRPT_DASHBD.TO-DB-b-196</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~161</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>103</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-102 ANALYSIS item 4 (and msg 7490: "the Cottonwood adapter from its silver: account_dim, plus the household key (BD relationship id) into the household dimension") | **Rows:** IRPT_DASHBD-D2-W161-S<k> | **Decomp cell:** `DB-b-196` (decomposition section 105) | **outcome_ref:** FWD-21, FWD-2 | **depends_on:** none.

**The issuer's grant decision (stated, as the CTO's analysis asks).** This cell READS Cottonwood's silver in the shared bucket `opal-data-assets` under the prefix `blackdiamond/cottonwood/` and under NO other prefix (never another firm's: `blackdiamond/49financial/`, `schwab/`, any other firm's key). That is Cottonwood's own data under its own key prefix. The rest of the bucket is out of bounds.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-161` (branch `wk-IRPT_DASHBD-161`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~161/`.

**Why.** FWD-21 wants the same default performance report for a household at 49 Financial, Cottonwood and Inflection. Every firm's gold has the same shape (PRD clause C-SHAPE: eight account-grain tables, one contract file per table named `org/standards/IRPT_DASHBD_<TABLE>_CONTRACT.json`, every table carries `firm`, `account_id`, `method_version`, `coverage`, no firm-specific column; the conformance check is the schema hash). Firm knowledge lives in ONE adapter per firm (C-ADAPTERS: Cottonwood from Black Diamond holdings, transactions, realized/unrealized; vendor column names appear ONLY inside the adapter). Cottonwood's gold today holds `account_return_daily` (schema equal to its contract) but none of the other seven tables; the previous round's read is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~155/FIRM_READINESS.json`. `account_dim` is the first table of the Cottonwood adapter: one row per account with its identity, its household key and its dates.

**The cell (`DB-b-196`): build, local, with NO write to AWS.**
1. **Read first.** The PRD `org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md` (C-SHAPE, C-ADAPTERS, C-METHOD, C-TIEOUT, the S03/S13 rows and the backend brief's Part V.1/V.2 it cites: find the brief from the PRD header's `brief_ref`; what `account_dim` carries and the closed vocabulary for `coverage`), `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` (the model of a table contract: `columns`, `enums`, `schema_hash`, `schema_hash_basis`, `firm_specific_columns`), the 49 Financial producer for the neutral parts (`data/assets/scripts/gold/irpt_reporting/account_return_daily.py`: `ARROW_SCHEMA`, `emit_day`, how it builds addresses with `lib/opal_naming.py address()`), and the earlier Cottonwood attempt (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~48/`: `adapter_returns.py`, `adapter_source.json`). Read Cottonwood's silver code and docs: `data/cot/scripts/gold/runners_cot/runner_common.py` (the silver root `blackdiamond/cottonwood/silver/` in `opal-data-assets`, `collapse_relationship_grain()`), `runners_cot/a00_dim_account.py` and `a01_dim_relationship.py` (an account and a relationship dimension already exist in code: reuse their derivation, do not re-derive a second way). Display column names (`Market Value`, `Relationship ID`, `AccountID`) appear ONLY inside the adapter.
2. **The contract.** Author `org/standards/IRPT_DASHBD_ACCOUNT_DIM_CONTRACT.json` in the round-1 shape of the sibling contracts: `table` "account_dim", `grain`, `partition`, `producer` (the adapter's repo path), `columns` (every column with its name and arrow type; they include `firm`, `account_id`, `method_version`, `coverage` and the account-dimension columns the PRD/brief names, including the household key column), `enums` (coverage vocabulary), `schema_hash` and `schema_hash_basis` EXACTLY as the account_return_daily contract states them (sha256 over the sorted `name:type` lines joined by newline, types as the pyarrow type name the producer's `ARROW_SCHEMA` carries), `firm_specific_columns` ("NONE ..."), `rule24_record` as the siblings carry one. A firm that lacks a field carries null plus a `coverage` value that says why.
3. **The adapter.** A new module `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_account_dim.py` (create the directory) exposing `ARROW_SCHEMA` (a `pyarrow.schema` whose hash equals the contract's) and a pure function that turns the silver frames into the `account_dim` table (no AWS call inside the pure function). Every S3 ADDRESS comes from `lib/opal_naming.address()` and every resource name from `name()` (CLAUDE.md rule 30): the adapter reads silver by the addresses the silver runners already use and computes its target as `address("irpt", "cottonwood", "gold", "account_dim", "date=<D>")`, which resolves to `s3://opal-data-cottonwood/irpt/cottonwood/gold/account_dim/date=<D>`; a builder REFUSAL is a missing registry row: file a row and stop, never hand-type an address. The adapter's `emit` path must have an `upload=False` default and writes nothing in this cell. Cottonwood and Black Diamond column names appear only in this file.
4. **Tests.** A test file `data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_account_dim.py` (offline, synthetic silver frames, no AWS) with 3 or more tests: the adapter output's schema hash equals the contract's `schema_hash`; one row per account; the household key comes from the relationship id and a relationship with several accounts yields one key shared by those rows; a missing field yields null plus a coverage value, never a guess. ONE temporary mutant (drop the household key) that a test catches, then reverted. Run them under `python -I -m pytest -q <file>` and `bash .tools/commit-gate.sh <file>` on every `.py` you touch.
5. **A read-only dry run on the real silver.** Run the adapter's pure function over Cottonwood's REAL silver read by S3 GET and LIST of the prefixes it needs under `blackdiamond/cottonwood/silver/` in `opal-data-assets` ONLY (name every prefix you read in the record), writing the result ONLY to the private folder `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~161/` (never the repo, never S3). Record counts only: `accounts` (rows), `relationship_ids` (distinct household keys), `null_counts` (per column), and the computed `target_address` (never written). If the silver you need is not in that prefix, record what is missing and stop: do not read another prefix.
6. **Record** `COTTONWOOD_ACCOUNT_DIM.json` in your folder with exactly: `adapter` {`file`, `sha256`, `tracked` true}; `firm_branches_outside_adapter` 0 (a needed branch anywhere else is a FINDING row, not a branch); `tests` {`file`, `passed`, `failed` 0, `mutant_failed` true}; `dry_run` {`prefixes_read` (a list of `{bucket: "opal-data-assets", prefix: "blackdiamond/cottonwood/..."}`), `accounts`, `relationship_ids`, `null_counts`, `target_address`}; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts and words only: no account number, no client name, no run of eight or more digits (an address or prefix value is not exempt: write bucket and prefix without date partitions).

<criterion id="DB103-4-AC1" cell_refs="DB-b-196"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r103/p103_round103.py" . DB103-4-AC1</invocation><expect>DB103-4-AC1 PASS</expect></criterion>
`DB103-4-AC1` -- the account_dim contract exists with its columns (including firm, account_id, method_version and coverage), a schema hash and the hash basis; the adapter is a tracked .py under data/assets/scripts/gold/irpt_reporting/ whose bytes hash as recorded and mentions Cottonwood, and whose ARROW_SCHEMA hashes (recomputed by the checker, same method) to the contract's schema_hash; the adapter's tests pass when the checker runs them, 3 or more, with a failing mutant; the dry run read only prefixes under blackdiamond/cottonwood/ of opal-data-assets, found accounts and relationship ids above 0, counted nulls and computed the address() gold target s3://opal-data-cottonwood/irpt/cottonwood/gold/account_dim/...; no write, push or deploy; no run of 8 or more digits. Base: FAIL (no record).

<expected_criteria>DB103-4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the other contracts and the 49 Financial producer.
- **No write of any kind to AWS** (no S3 put/copy/delete, no DynamoDB write, no Lambda, Terraform or IAM act), **no deploy, no push, no vendor call, no secret read.** Reads only: repo files; S3 GET and LIST of `s3://opal-data-assets/blackdiamond/cottonwood/...` and nothing else (the issuer's grant above); never another firm's data (CLAUDE.md cross-firm rule). Landing `account_dim` in Cottonwood's gold is a LATER round under a never-widen pair. A denial is recorded verbatim, not retried by another route. If the comp-rail hook refuses a raw S3 call, run what it says next or annotate `# rail-checked: <why>`.
- **Client data.** The silver is client data: counts only in the repo, a row or your report; any dry-run output stays in the private folder.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A column the PRD names that Cottonwood's silver does not carry is null plus a coverage value, and a row. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W161-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~161/
org/standards/IRPT_DASHBD_ACCOUNT_DIM_CONTRACT.json
data/assets/scripts/gold/irpt_reporting/adapters/
data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_account_dim.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-196.cottonwood-account-dim-and-household-key-adapter.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 105 (round 103), cell `DB-b-196`.
<owned_cells>DB-b-196</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB103-4-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~161/IRPT_DASHBD.TO-DB-b-196.cottonwood-account-dim-and-household-key-adapter.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB103-4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the contract's columns (names) and the coverage vocabulary; the adapter and where the household key comes from; the tests and the mutant; the dry run's counts (accounts, relationship ids, null counts) and the prefixes read; the address() target; any column the silver lacks; row ids. Counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a contract, an adapter module and tests, local; nothing is served, wired, written or deployed; the later apply is its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 GET and LIST of one firm's own silver prefix with the box's existing identity; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record) and is dry-run on 8 synthetic arms.
lane: the <paths> block IS the grant.
</preflight>

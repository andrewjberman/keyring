# TO IRPT_DASHBD.TO-DB-b-211 -- the INFLECTION ADAPTER'S FIRST TABLES: `account_dim` and the household key, read from Inflection's own silver under its own key prefixes only, with the counts of accounts and households and the schema hash equal to the gold contract's; a private dry-run table; nothing written to S3

<to_id>IRPT_DASHBD.TO-DB-b-211</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~171</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>108</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-108 ANALYSIS section 3 cell 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_108_20261014.md`) | **Rows:** IRPT_DASHBD-D2-W171-S<k> | **Decomp cell:** `DB-b-211` (decomposition section 110) | **outcome_ref:** FWD-2 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-171` (branch `wk-IRPT_DASHBD-171`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~171/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, hashes and words only in the repo, a row or your report; an account's number, name or figure is never recorded.

**Why.** The 49 Financial default report is complete except for its disclosure gate, so the next firm is Inflection (Cottonwood's silver stops at 2026-06-23 and its input is another project's). The reporting project reaches a second firm through an ADAPTER: firm knowledge lives only in the adapter, every table is built to the gold contract, and the same schema hash proves it (PRD C-ADAPTERS, C-SHAPE). Round 103 built Cottonwood's `account_dim` adapter and found the household key; Inflection's source is different: its holdings and activity come from Orion and Eclipse, in the monolith bucket under the `inflection/` key prefix.

**The grant of the S3 reads (BY PREFIX).** You may LIST and GET under `s3://opal-data-assets/orion/inflection/` and `s3://opal-data-assets/eclipse/inflection/` and nowhere else. The Orion master prefix `s3://opal-data-assets/orion/4698/` is another place and is NOT granted; no other firm's bucket or prefix is read, named or written (the cross-firm rule). No put, copy or delete of any kind. A denial is recorded verbatim, not retried by another route.

**The cell (`DB-b-211`).**
1. **Read first.** Round 103's pattern: `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_account_dim.py` and its tests `data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_account_dim.py` (read-only; copy the SHAPE, not its firm knowledge); the gold contract `org/standards/IRPT_DASHBD_ACCOUNT_DIM_CONTRACT.json` (its columns, coverage vocabulary and `schema_hash`: the adapter must produce exactly this schema); the PRD sections C-ADAPTERS, C-SHAPE and C-COVERAGE in `org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md`; the previous packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~165/ACCOUNT_DIM_GOLD_PACKET.md` (what an account_dim packet states); the registry row `lib/opal_naming.lookup("inflection")` (firm key `inflection`, gold bucket `opal-data-inflection`); and the issuer's check file `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r108/p108_round108.py` (your criterion: read `check_dim`).
2. **Discover Inflection's silver (reads only).** LIST then GET the newest partition of the tables under `s3://opal-data-assets/orion/inflection/silver/` (`fact_assets`, `fact_performance`, `fact_positions`, `fact_transactions`) and `s3://opal-data-assets/eclipse/inflection/silver/` (`fact_model_composition`, `fact_models`, `fact_portfolios_full`, `fact_portfolios_simple`), and their `meta/`, as far as you need to find where an ACCOUNT's identity, its custodian, type and registration, and a HOUSEHOLD key live. Record in `household_key_source` (words) which column you took as the household key and why, and which account-dimension fields Inflection's silver does not carry (`absent_fields`, as Cottonwood's `NOT_CARRIED`).
3. **The adapter.** Create `data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_dim.py` with the SAME `ARROW_SCHEMA` as the gold contract (so `schema_hash` equals the contract's), `FIRM` taken from `opal_naming.lookup("inflection")["key"]` (never typed), a PURE `build_account_dim(...)` over silver frames (no AWS call), a GET-only reader helper limited to the two granted prefixes (a class with no put, copy or delete method), and `emit_account_dim(table, as_of)` that computes the gold address with `lib/opal_naming.address()` and WRITES NOTHING (upload defaults to False and `upload=True` raises `NotImplementedError`). The module names no other firm and holds no write-call name (`put_object`, `upload_file`, `copy_object`, `delete_object`...); every `s3://` literal in it sits under a granted prefix.
4. **Tests.** Create `data/assets/scripts/gold/irpt_reporting/tests/test_inflection_account_dim.py`: at least 6 offline tests on synthetic frames (one row per account; the household key; an account with no household key; the absent fields null and listed; the schema hash equals the contract's; `emit_account_dim(upload=True)` refuses; the module names no foreign place), run with `python -I -m pytest -q <file>`; ONE temporary mutant (for example drop the household key) that a test catches, then reverted.
5. **The dry run (reads only).** Run the adapter against the live silver and write the resulting table to the PRIVATE file `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~171/ACCOUNT_DIM_DRY_RUN.parquet` (one row per account). The table's own schema hash must equal the contract's; the checker recounts accounts and households from this file.
6. **Record** `ACCOUNT_DIM_R108.json` in your folder with exactly: `module` {`file`, `sha256`, `tracked` true}; `tests` {`file`, `passed`, `failed` 0, `mutant_failed` true}; `schema_hash` (the contract's, equal to the adapter's); `source_prefixes` (the list of the granted prefixes you actually read, each as `s3://...`); `dry_run` {`path`, `sha256`}; `accounts` (integer); `households` (integer); `household_key_source` (words); `absent_fields` (a list of field names); `coverage_words` (one plain sentence: what coverage an Inflection account carries until its lots and history are shown, and why); `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0, `s3_reads` (integer)}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, paths, hashes and words only: no account number, name or figure; no run of 8 or more digits except in a `sha256` value or a `path`, `file` or `key` field.

<criterion id="DB108-1-AC1" cell_refs="DB-b-211"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r108/p108_round108.py" . DB108-1-AC1</invocation><expect>DB108-1-AC1 PASS</expect></criterion>
`DB108-1-AC1` -- the adapter is a tracked file hashed as recorded; it names no other firm's bucket, prefix or master id, holds no write-call name, and every `s3://` literal sits under `s3://opal-data-assets/orion/inflection/` or `s3://opal-data-assets/eclipse/inflection/`; its test file has 6 or more passing tests and passes when the checker runs it, with a failing mutant; the adapter's `ARROW_SCHEMA` hash equals the gold contract's `schema_hash` and the record says so; every `source_prefixes` entry is a granted prefix; the private dry-run table exists outside the repo, is hashed as recorded, its own schema hash equals the contract's, it holds one row per account with firm `inflection`, and `accounts` and `households` equal the checker's recount from it; `household_key_source`, `absent_fields` and `coverage_words` are present; nothing is written; no push or deploy. Base: FAIL (no record).

<expected_criteria>DB108-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including `cottonwood_account_dim.py`, every contract under `org/standards/` (if the gold contract's schema cannot hold Inflection's accounts, file a row naming the field and STOP: the contract is not yours to change), every portal file and the issuer's check files.
- **Reads and writes.** Reads: repo files and the S3 LIST and GET of the two granted prefixes named above (and `lib/opal_naming` registry rows). Writes: the repo files of the grant and the private folder named above. No write to AWS of any kind, no deploy, no push, no vendor call, no secret read, no read of any other firm's place.
- **Client data.** The silver and the dry-run table are client data: counts and hashes only in the repo, a row or your report.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If Inflection's silver carries no household key at all, say so in `household_key_source`, produce the table with the household column null and `household_id_reason` stating it, and file a row: do not invent a key. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W171-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~171/
data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_dim.py
data/assets/scripts/gold/irpt_reporting/tests/test_inflection_account_dim.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-211.inflection-adapter-account-dim-household-key-dry-run.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 110 (round 108), cell `DB-b-211`.
<owned_cells>DB-b-211</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB108-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~171/IRPT_DASHBD.TO-DB-b-211.inflection-adapter-account-dim-household-key-dry-run.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB108-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; where in Inflection's silver you found the account identity and the household key and which column you took; the counts of accounts and households; which account-dimension fields Inflection's silver does not carry; the schema hash equality; the prefixes you read and the number of S3 reads; the coverage words; row ids. Counts and words only; no account number, name or figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a new adapter module, its tests and a private dry-run table; nothing is read by served code, wired or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: read-only S3 LIST and GET of two Inflection-scoped prefixes of the monolith bucket the estate's other adapters already read; no new principal or grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB108-1-AC1 FAILS at base (no record) and the checker's cross-firm, write-call and schema-hash helpers are exercised by its 6-arm self-test (one arm reproduces the gold contract's schema hash from the Cottonwood adapter).
lane: the <paths> block IS the grant.
</preflight>

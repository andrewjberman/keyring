# TO IRPT_DASHBD.TO-DB-f-1401 -- the FWD-5 GROUND READ WITH SOURCE READS, three firms: for each of the brief's 14 `account_transaction` columns and each firm, the live column of the firm's transaction silver that supplies it, or the computation from live columns, or ABSENT with every searched column printed; one record per firm, bound to the issuer's live schema census; a read of the census, code and tracked records, nothing written

<to_id>IRPT_DASHBD.TO-DB-f-1401</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~1401</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>128</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the round-126 analysis for F-SHIP (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_126_20261016.md`, msg 9133: "The round-126 records' `absent` claims are VOID wherever the CVO's read shows the field ... Round 127 repeats the ground read WITH source reads (`s3_reads > 0`, partitions and rows counted, each target's source column named). Only a target with no source column after that read is `absent`, with the columns searched printed ... a ground-read criterion requires a source read count above zero"). The cell is numbered round 128 because round 127 was already issued. | **Rows:** IRPT_DASHBD-D2-W1401-S<k> | **Decomp cell:** `DB-f-1401` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R128_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-1401` (branch `wk-IRPT_DASHBD-1401`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1401/`. The folders `data/assets/scripts/gold/irpt_reporting`, `data/inf`, `docs/briefs` and `org/standards` are materialized (if one is missing, run `git sparse-checkout add <folder>`: not a grant to edit). Never push; never commit the workspace `portal` gitlink. You read NO source yourself (no AWS, no network, no vendor call, no secret read): the live source read is the ISSUER's, already done and recorded, and you work from it. No real client, household or account id, no client figure and no security name in the repo, a row or your report.

**Why.** The round-123 and round-126 ground reads said `absent` for fields from the CODE alone, reading no source (`s3_reads 0`). The CVO and the issuer then read the sources: Cottonwood's transaction table has 73 columns (not 5), Inflection's 36, 49 Financial's 140 (not 14). The `absent` claims are void wherever the live schema shows a field. The issuer's census is `deliverables/2.0.0_SA_COO~F2/R128_LIVE_SOURCE_CENSUS_3FIRMS.json`: per firm the table, the partitions read (572 / 125 / 154), the row count, the FULL column list with types, and the code values of the type columns. This cell maps the brief's 14 columns onto those live columns.

**The cell (`DB-f-1401`).** Do steps 1 to 3 for each of `49financial`, `cottonwood`, `inflection`.
1. **The 14 targets, in this order** (brief line 78, `docs/briefs/reporting-dashboard-backend-brief-20260930.md`): `trade_date`, `settle_date`, `action`, `txn_type`, `symbol`, `asset_name`, `units`, `price`, `amount`, `fee`, `custodian`, `flow_class`, `source_txn_id`, `coverage`. For each, read the census's column list for the firm (names only; the census holds no values of the other columns, and you read no source) and decide ONE of:
   - **sourced:** `source` is the live column name exactly as the census spells it, `from_columns` is `[]`, `claim` is `measured` when the column IS the field (a trade date column for `trade_date`), or `inferred` with a `method` when the column needs a reading (a transaction type column read as `txn_type` through the ratified mapping), `searched_columns` is null;
   - **computed:** `source` is null, `from_columns` lists the live columns it is computed from (for example a fee total from several fee columns; `custodian` from the custodian column or the entry's constant; `action` from the type table; `flow_class` from the per-code rule; `coverage` from the mapping), `claim` is `inferred` and `method` says how (the CTO's round-123 ruling: a computed field is `inferred` with a method, never `absent`);
   - **absent:** only when NO live column could feed it: `source` null, `from_columns` `[]`, `claim` `absent`, `searched_columns` the firm's FULL live column list exactly as the census prints it, and `words` saying what you looked for.
   Use code and tracked records to understand what a column MEANS (the column names are the vendor's; `sources.json`, the adapters and `account_return_daily.py` say how each is used). A column whose meaning you cannot establish from a file is `inferred` with the reason in `method`, never `measured`. Print every denominator you cite.
2. **Known facts from the CVO's and the issuer's reads (the checker holds them):** Cottonwood's table carries a settle date, a symbol, units, a price and a custodian, so none of those is absent for Cottonwood; Inflection's `settle_date` and `fee` are truly absent (its 36 columns hold neither); a firm's transaction table with several fee columns (49 Financial has more than one) supplies `fee` as a computed total, and a column holding a per-transaction identifier (`TransactionID` for Cottonwood, `id` for Inflection, a cashiering identifier for 49 Financial) supplies `source_txn_id`; decide each on the live names, do not copy this sentence.
3. **Record** `RD_FWD5_GROUND_49FINANCIAL_R128.json`, `RD_FWD5_GROUND_COTTONWOOD_R128.json` and `RD_FWD5_GROUND_INFLECTION_R128.json` in your folder, each with EXACTLY these top-level fields: `as_of` (ISO date), `firm`, `source_reads` ({`census`: the census path, `partitions_read`, `rows`, `column_count`: copied from the census's section for the firm}), `targets` (the 14 objects in the brief's order, each {`target`, `source` (string or null), `from_columns` (list), `claim`, `method` (string or null), `words`, `searched_columns` (list or null)}), `absent_count`, `computed_count` (the number of targets with a null source and claim `inferred`), `worker_reads` {`s3_reads` 0, `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}, and the false flags `files_in_repo`, `served_values_changed`, `pushed`, `deployed`. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `vintage`, `uri`, `rows`, `partitions_read` or `census` field.

<criterion id="DBF128-1-AC1" cell_refs="DB-f-1401"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r128/p128_ground3.py" . DBF128-1-AC1</invocation><expect>DBF128-1-AC1 PASS</expect></criterion>
`DBF128-1-AC1` -- the three records have exactly the form of step 3; each `source_reads` equals the census's counts for the firm and the census read above zero partitions; for each firm the 14 targets are the brief's columns in order; every `source` and every `from_columns` entry is a column of the firm's live schema; a computed target is `inferred` with a method; an `absent` target prints the full searched column list; the counts equal the checker's; Cottonwood's trade date, settle date, symbol, units, price and custodian are not absent and Inflection's settle date and fee are; `worker_reads` is all zero, the flags false, ASCII, no digit run outside the exempt fields. Base: FAIL (no records).

<expected_criteria>DBF128-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the census, the earlier records (rounds 120, 123, 126), the contract and producer in flight, the brief, every code file and the issuer's checker.
- **No source read by you,** no AWS, no network. The contract `org/standards/IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json` and the producer are NOT edited here: the issuer amends them from your records.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A column whose meaning you cannot establish is `inferred` with the reason, never `measured`, and never a reason to say `absent`.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W1401-S<k>` (D2 is the device coordinate, never F2), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1401/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-1401.fwd5-ground-read-with-source-reads-three-firms-live-schema.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R128_F.md</decomp_doc> round 128, workstream ~F2 (F-SHIP), cell `DB-f-1401`.
<owned_cells>DB-f-1401</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF128-1-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1401/IRPT_DASHBD.TO-DB-f-1401.fwd5-ground-read-with-source-reads-three-firms-live-schema.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF128-1-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; per firm how many of the 14 targets are sourced, computed and absent, and which; for 49 Financial the fee columns and the identifier column you used; anything off-task (as row ids). No real id, no client figure, no security name.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: three records in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call by the worker and no grant is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF128-1-AC1 FAILS at base (no records) and the checker's helpers are exercised by its self-test (10 arms).
lane: the <paths> block IS the grant.
</preflight>

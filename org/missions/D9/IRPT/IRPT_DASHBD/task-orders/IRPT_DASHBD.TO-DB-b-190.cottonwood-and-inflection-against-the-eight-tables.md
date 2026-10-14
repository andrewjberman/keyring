# TO IRPT_DASHBD.TO-DB-b-190 -- READ what Cottonwood and Inflection hold against the eight C-SHAPE gold tables the default performance report needs, which of it is gold IRPT_BCKEND already builds, and what each firm's adapter would take; read only

<to_id>IRPT_DASHBD.TO-DB-b-190</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~155</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>101</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msgs 7451 and 7465 (ENRICHMENT item 3, narrowed to a read: "it also names the gold IRPT_BCKEND already builds for Cottonwood and Inflection (the IR holdings inputs: Cottonwood serves 19/19 columns, Inflection 17/19) as candidate adapter inputs. An adapter reuses that gold and never re-pulls beside it (no shadow pipeline).") | **Rows:** IRPT_DASHBD-D2-W155-S<k> | **Decomp cell:** `DB-b-190` (decomposition section 103) | **outcome_ref:** FWD-21, FWD-2 | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-155` (branch `wk-IRPT_DASHBD-155`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~155/`.

**Why.** FWD-21 wants the same default performance report for a household at 49 Financial, at Cottonwood and at Inflection. The report is built from eight account-grain gold tables whose shape is the same for every firm (PRD C-SHAPE: `account_return_daily`, `account_class_daily`, `account_activity_daily`, `account_transaction`, `account_lot_realized`, `account_lot_unrealized_daily`, `account_dim`, `market_topic_daily`; one contract file per table under `org/standards/IRPT_DASHBD_<TABLE>_CONTRACT.json`, list the ones that exist). Firm knowledge lives in one adapter per firm (PRD C-ADAPTERS: Inflection from Orion positions, `accounts_v2` and the transactions by the ratified `orion_cashflow_taxonomy.yaml`, lots `NO_LOTS` until Eclipse tax lots are shown populated; Cottonwood from Black Diamond holdings, transactions, `fact_realized`/`fact_unrealized`). The issuer read the buckets: `s3://opal-data-49financial/irpt/49financial/` exists; **`s3://opal-data-cot/irpt/` and `s3://opal-data-inf/irpt/` list EMPTY**, so no C-SHAPE table exists yet for Cottonwood or Inflection and the household sample builder has nothing to read for them. Separately, IRPT_BCKEND (another project) already builds gold for these two firms for the Investor Reporting holdings page (the CTO: Cottonwood serves 19 of 19 holdings columns, Inflection 17 of 19). An adapter must REUSE that gold and never re-pull the same vendor data beside it (a shadow pipeline is an Andrew veto).

**The cell (`DB-b-190`): a READ. Nothing is changed, deployed or written.**
1. **Re-read the two prefixes** (`aws s3 ls s3://opal-data-cot/irpt/` and `s3://opal-data-inf/irpt/`, with a `# rail-checked: one named bucket, one prefix, top-level listing` annotation if the rail asks) and state `irpt_prefix_exists` for each (expected false).
2. **Find what each firm holds that a report could be built from.** Start from `data/firm_registry.json` (each firm's `bucket`, `kind`, sources), `infra/aws/lambda/investor-reporting/` and `data/assets/scripts/gold/investor_reporting/` (the holdings snapshot builder and its inputs for these two firms: read `holdings_snapshot.py`'s `firm_bucket_map` and what it reads per firm), `comp-estate --resource <substr>` and `comp-pipescript io <script>` (enumerate before you list S3), and the PRD's C-ADAPTERS and S13 rows (`org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md`; read the sections that name the adapters, the tie-out oracles and the backend brief's Part V). List each firm's existing GOLD or silver inputs as `existing_gold_inputs`: `{what, address (an S3 prefix or table name), columns_served (an integer: the count of columns it carries that the report's tables need; use the IR holdings column counts where that is the input)}`. Read S3 by LIST of prefixes and parquet SCHEMA and partition names only; no figure, no account number.
3. **Table by table.** For each of the eight tables and each firm: `{table, source_exists (bool: a source for it exists in the firm's existing data), candidate_source (the existing gold or silver input an adapter would read, in words and address), gap_in_words (what is missing: a column, history, a taxonomy, a tax-lot source), reuses_existing_gold (bool: the candidate is gold IRPT_BCKEND already builds, so the adapter reads it and pulls nothing new)}`.
4. **Per firm:** `readiness` ("READY" if every table that the report needs has a source an adapter can read today, else "BLOCKED"), `blockers` (words), `household_dimension` (where a household's accounts are grouped for this firm: the ADVI household crosswalk's coverage of the firm, or none), `shadow_pull_proposed` false (an adapter reading an input beside the existing gold is not allowed; if the only route is a new pull, say so in `blockers` and still keep this false).
5. **Say it in words.** `recommendation` (one to three sentences: which firm's adapter is closest, and what the first adapter order would build) and `adapter_order_proposal` (the smallest first order: the table, the firm, the input, the criterion).
6. **Record** `FIRM_READINESS.json` in your folder with exactly: `firms` (two entries, firms `cottonwood` with bucket `opal-data-cot` and `inflection` with bucket `opal-data-inf`, each `{firm, bucket, irpt_prefix_exists, tables (eight entries), existing_gold_inputs, readiness, blockers, household_dimension, shadow_pull_proposed}`); `recommendation`; `adapter_order_proposal`; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, addresses and words only: no figure, no account number, no run of eight or more digits (an address under a key named `address` is NOT exempt: write bucket and prefix without date partitions).

<criterion id="DB101-4-AC1" cell_refs="DB-b-190"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r101/p101_round101.py" . DB101-4-AC1</invocation><expect>DB101-4-AC1 PASS</expect></criterion>
`DB101-4-AC1` -- the record holds exactly the two firms with their buckets and the irpt prefix empty (the issuer's own read); each firm lists the eight C-SHAPE tables with source_exists, a candidate source, a gap in words and whether it reuses existing gold; each names the existing gold inputs with columns served, a readiness, blockers and its household dimension; no shadow pull is proposed; a recommendation and a first adapter order are stated; no write, push or deploy; no run of 8 or more digits. Base: FAIL (no record).

<expected_criteria>DB101-4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No write of any kind to AWS** (no S3 put/copy/delete, no DynamoDB write, no Lambda, Terraform or IAM act), **no deploy, no push, no vendor call, no secret read, no Bloomberg call.** Reads only: repo files; S3 LIST and GET of partition names and parquet schemas with the box's existing identity. A denial is recorded verbatim, not retried by another route. Never read another firm's data to answer for a firm (each firm's own bucket only).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. Where you cannot establish a source, say `source_exists` false and say why in the gap; never guess. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W155-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~155/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-190.cottonwood-and-inflection-against-the-eight-tables.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 103 (round 101), cell `DB-b-190`.
<owned_cells>DB-b-190</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB101-4-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~155/IRPT_DASHBD.TO-DB-b-190.cottonwood-and-inflection-against-the-eight-tables.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB101-4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; per firm the readiness, the tables with a source and the tables without (counts of 8), the existing gold inputs and their columns served, and the blockers; the recommendation and the first adapter order; any row ids. Counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read; nothing is changed, deployed or written.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: repo reads and S3 LIST/GET of schemas with the box's existing identity; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record) and is dry-run on 5 synthetic arms.
lane: the <paths> block IS the grant.
</preflight>

# NFRA_MCPINDEX task order -- `MX-s-15` -- Schwab `dim_transaction` declared beside the three `dim_*` tables: one master, one date

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-s-15</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~19</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; a dataset declaration in an existing integration.
comp-iam: RUN -- 2026-09-30 ~08:4xZ by the issuer: `comp-iam role opal-gateway-role` shows sts:AssumeRole under the schwab ExternalId condition; `comp-iam role gateway-schwab-read-role` returns no match (its TF index does not resolve the reader role by name), so the APPLIED plane was read directly: simulate-principal-policy on gateway-schwab-read-role -> dim_position allowed, dim_transaction explicitDeny. This cell adds the two dim_transaction prefixes to the reader role's list; NOT applied here -- the apply is MX-r-6 under never-widen halves.
comp-adversary: DECLARED-NOT-APPLICABLE -- the three dim_* tables are the pattern.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 reads).
</preflight>

## 1. THE CELL -- `MX-s-15` (round 5; `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/REINSTATE_RULINGS_20260930.md` @4e598ab7be, ruling B4)

**Why.** The Schwab integration answers positions, balances and assets (`dim_position`, `dim_balance`, `dim_asset`)
but not transactions. `dim_transaction` is already in S3 for both masters and is declared nowhere the gateway reads.

**Facts at the cut (issuer-measured 2026-09-30 ~08:1xZ):**
- The three tables are hard-coded on 6 surfaces: `app/integrations/schwab/datasets.json`, `app/integrations/schwab/query.py`
  (`DATASET_SCHEMAS` and `DATASET_GRAINS`), `app/data_entitlement.py:72` `DATASETS`, `app/schwab_audit.py:71` `_DATASETS`,
  and `infra/aws/terraform/opal-gateway/schwab_reader_iam.tf` `schwab_data_prefixes` (:63-70).
- The live reader role `gateway-schwab-read-role` is `allowed` s3:GetObject on `schwab/08242234/silver/dim_position/...`
  and `explicitDeny` on `.../dim_transaction/...` (`aws iam simulate-principal-policy`).
- Definition: `data/assets/scripts/silver/schwab_projections.py:55` (TRN section 1); 39 pinned + 5 provenance columns
  are described in `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~3/analysis-schwab.result.md:320-343`.
  That record saw object names `{master}_dim_transaction.parquet` (:343); the dims read `date=.../data.parquet`. Settle the
  real key form by a live listing before you write a schema.

**The act:**
1. List `s3://opal-data-assets/schwab/{08242234,08335338}/silver/dim_transaction/` (newest partitions) and read one
   object's schema. Record key form, columns and newest date in `SCHEMA_MX-s-15.md`.
2. Declare `dim_transaction` on all 6 surfaces, beside the three tables and in their form. The schema carries the
   columns a transaction question needs (account_ref, business/trade date, cusip, ticker, the transaction type code,
   quantity, net amount), each typed from the source like the others. Declare the unique grain in `DATASET_GRAINS`. If
   the data has no unique grain, declare `None` so paging refuses, and file a row.
3. **One master, one date.** A query reads exactly one master and one date partition, as the dims do. It never sums across
   masters; the dataset's `datasets.json` note says so.
4. **Entitlement, recorded, never changed.** Read how an existing principal's Schwab grant resolves a dataset. State in
   `ENTITLEMENT_MX-s-15.md` whether an existing grant covers `dim_transaction` automatically once it is declared. The
   release halves at MX-r-6 read it. No identity, grant or sign-in path is created or changed (ruling B2).
5. Tests in `tests/test_schwab_transactions.py` with exactly these names: `test_mx_s15_dataset_registered`,
   `test_mx_s15_grain_declared`, `test_mx_s15_entitled_like_dims`, `test_mx_s15_reads_one_master_one_date`. Move only
   the pins in existing `tests/test_schwab_*.py` files that the new dataset moves. Run AC1 and AC2, and commit.

## 2. BOUNDS

1. Nothing is deployed and nothing is applied; `terraform` runs `validate` at most. The release is MX-r-6.
2. No identity, grant or sign-in change. The existing guards stay exactly as they are.
3. Nothing under `data/cot/`. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/schwab/
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/schwab_audit.py
infra/aws/ec2/opal-gateway/tests/test_schwab_transactions.py
infra/aws/ec2/opal-gateway/tests/test_schwab_catalog.py
infra/aws/ec2/opal-gateway/tests/test_schwab_query.py
infra/aws/ec2/opal-gateway/tests/test_schwab_semantics.py
infra/aws/ec2/opal-gateway/tests/test_schwab_wiring.py
infra/aws/terraform/opal-gateway/schwab_reader_iam.tf
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~19/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W19-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-s-15" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/checks/s15.AC1.sh; echo "exit=$?"</invocation><expect>dim_transaction declared on 6 of 6 surfaces -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-s-15" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/checks/s15.AC2.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 4 of 4; failed/error tests 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~19/NFRA_MCPINDEX.TO-MX-s-15.schwab-transactions-table.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Reinstatement ruling B4 and round-5 order item 2. Dry-run at base: s15.AC1 FAIL
(0 of 6), s15.AC2 FAIL (file absent). Chain head of MX-r-6.

<status>complete -- issuer-graded on CLOUD after the drain @46587d5134 by 2.0.0_SA_COO~MI, 2026-09-30 ~10:0xZ: s15.AC1 PASS (6 of 6 surfaces), s15.AC2 PASS (4 of 4 named tests, 0 failed), instance VALID. Key form date=YYYY-MM-DD/data.parquet, newest 2026-09-28 on both masters; grain None (paging refuses). Existing grants do NOT cover dim_transaction (ENTITLEMENT_MX-s-15.md). Row Z-W19-S2 (BLOCKING: the OPLGTW contract and tests/acceptance) is ruled by Z-S63 into MX-r-6 A1. Was: pending.</status>
<round>5</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

# NFRA_MCPINDEX task order -- `MX-s-6` -- the scheduled Black Diamond asset conversion writes the compacted `silver/bd_assets.parquet`, and the cusip bridge is rebuilt from it (row Z-S15)

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context for this order ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-s-6</owned_cells>
</decomp_ref>
<issued_to>0.4.0_DS_ClientPlatform~D</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the existing trigger bd-asset-dim-pipeline-trigger is read, never changed; the builder's own schedule stays a later ask.
comp-iam: DECLARED-NOT-APPLICABLE -- the converter's existing identity writes the same bucket.
comp-adversary: DECLARED-NOT-APPLICABLE -- a data-completeness repair.
EGRESS CLASS, declared: Opal's own AWS only.
</preflight>

## 1. THE CELL -- `MX-s-6` (supplementary; 0.7.0_AE_CloudOps~I's row NFRA_MCPINDEX-Z-S15, ruled by the issuer)

**Measured by 0.7.0_AE_CloudOps~I under MX-s-4 (row Z-S15; read it in the project channel):**
- `data/*/scripts/silver/convert_assets_to_silver.py` writes the compacted `silver/bd_assets.parquet` ONLY under
  `--backfill`, not "unless `--no-compacted`".
- The scheduled SSM path passes `--latest`, so no scheduled run has ever written the compacted file.
- The file is frozen at 2026-04-14. Fixing the Black Diamond login (MX-s-4, AE) restores the date partitions but leaves
  it frozen.
- The cusip bridge `silver/bd_assets_dim.parquet` is built from that compacted file (your MX-s-2 result).

Do, as the DS lane (CLAUDE.md rule 13: DS owns these silver scripts and their QA deploy):
1. Make the scheduled path write the compacted file: fix the condition in the converter, with a test that plants a
   `--latest` run and sees the compacted write. Deploy through `.tools/safe-deploy.sh`.
2. After MX-s-4's login fix lands and one real scheduled or ad-hoc run has converted current dates, confirm the
   compacted file is rewritten. Then rebuild the bridge once with `build_bd_assets_dim.py`, and print the asset_id count
   and how many of the 791 formerly missing ids it now carries.
   **AMENDED A1 (2.0.0_SA_COO~O, 2026-09-28 ~06:1xZ):** step 2's input is now MX-s-9's REST bronze, not MX-s-4's
   login (MX-s-4 closed on step 2 by its A5; the pull moved to MX-s-9, complete). Convert
   `s3://opal-data-bd/blackdiamond/49financial/bronze/assets_dim_rest/2026-09-28/assets_dim_rest.parquet` into the
   compacted `silver/bd_assets.parquet`. UNION it with the frozen 2026-04-14 dim, latest-wins per `asset_id` (per the
   CTO's design @1973056c51). Print both counts; MX-s-9 measured 12,141 total, 1,204 pull-only and 9 frozen-only.
   `asset_super_class` comes from dim 7 (not absent). Then rebuild the bridge as step 2 says. The criteria are
   unchanged. If the naming gate refuses a new file carrying an existing `_bd`-suffixed column, file a BLOCKING row
   citing row Z-S33 (its disarm is 1.0.0_SA_CTO~O's). Never build the literal by concatenation.
   **AMENDED A2 (2.0.0_SA_COO~O, 2026-09-28 ~06:2xZ), SUPERSEDING A1, on the seat's row Z-S34 (@b0fdb8fa33):** A1 named
   the WRONG artifact. `silver/bd_assets.parquet` is TRANSACTION grain (3,449,107 rows, asset_id not unique) and is fed
   by the transaction feed. The MX-s-9 pull is ASSET grain and must NOT be written into it. Step 2 is now DIM-ONLY:
   - write `silver/bd_assets_dim.parquet` = the frozen 2026-04-14 dim UNION the MX-s-9 pull, latest-wins per
     `asset_id` (12,141 rows);
   - keep all 22 columns;
   - for the 1,204 pull-only assets, the transaction-derived columns (txn_count, the seen-dates) are NULL, carrying
     the claim `absent`, never inferred;
   - print both counts and how many of the 791 formerly missing ids it now carries.
   AC1 (s4.AC2, `silver/bd_assets.parquet` rewritten) LEAVES this order, because it is gated on the transaction feed,
   not on this pull. MX-s-6 is graded on AC2 (s4.AC3, the dim rewritten) alone. `silver/bd_assets.parquet` is not
   touched.
   **AMENDED A3 (2.0.0_SA_COO~O, 2026-09-28 ~06:5xZ), on 1.0.0_SA_CTO~O's Z-S37 ruling @86b1b3b5b4:** the builder's commit
   is gated on `coerce_silver_ids()`, whose only home was inf's tree. Two paths join `<paths>`:
   - `lib/silver_ids.py` (new) holds `coerce_silver_ids` and `DEFAULT_SILVER_ID_COLS`, moved BYTE-IDENTICAL from
     `data/inf/scripts/silver/_orion_api_silver_lib.py`;
   - that inf module keeps its public names by re-exporting them from `lib.silver_ids`. Change nothing else in it; its
     existing tests must pass unchanged. Print their result.
   `build_bd_assets_dim.py` imports from `lib.silver_ids` only. A cross-firm import, a copy of the helper and a gate
   exemption are all REFUSED by that ruling. The criteria are unchanged.
3. Do not touch served gold. The `holdings_lots` correction is MX-s-2's, under its own sign-off, and only after this
   bridge is current.

## 2. BOUNDS

1. Silver only, plus the one bridge rebuild. No served key moves.
2. Standing: no push. REFUSE a criterion you cannot meet as written, and report the refusal with its measurement.

## 3. SURFACES

<paths>
data/black_diamond/scripts/silver/
data/assets/scripts/silver/
data/black_diamond/tests/
data/assets/tests/
lib/silver_ids.py
data/inf/scripts/silver/_orion_api_silver_lib.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.4.0_DS_ClientPlatform~D/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows: `NFRA_MCPINDEX-Z-S<k>` (site-Z; take the next free k). A disarm carries a TERMINAL disposition
(DISMISSED_WITH_REASON plus dismissal_reason).

## 4. PROOF OF SPEC (literal; run from the workspace root after step 2)

<proof_of_spec>
  <criterion id="AC2" cell_refs="MX-s-6"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s4.AC3.sh; echo "exit=$?"</invocation><expect>silver/bd_assets_dim.parquet after issue=yes -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance to
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.4.0_DS_ClientPlatform~D/NFRA_MCPINDEX.TO-MX-s-6.bd-assets-compaction.proof_of_spec.json`.
Report once to `2.0.0_SA_COO~O`:
- the condition fix and its deploy;
- the compacted file's new LastModified;
- the bridge's asset_id count and how many of the 791 it now carries;
- any row.

<!-- ===================== RECORD FACE ===================== -->

# pipeline-override: supplementary repair on the issuer's ruling of row NFRA_MCPINDEX-Z-S15 (filed by 0.7.0_AE_CloudOps~I under MX-s-4): the compaction and bridge rebuild are DS-owned silver acts (rule 13), moved out of the AE order MX-s-4 (amended the same commit); same issuer, the DS lane already seated for NFRA_MCPINDEX.

**ISSUER NOTES:** AC1 and AC2 reuse s4.AC2.sh and s4.AC3.sh (dry-run at base 2026-09-26 ~05:4xZ: FAIL, both files
LastModified 2026-04-14). Its step 2 depends on MX-s-4's login fix (AE). The issue timestamp in s4_read.py is 06:00Z;
a write after this order's issue also satisfies it.

<status>pending</status>
<direct_act>true</direct_act>
<slot>~D</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

<status>complete</status>
<!-- flipped by the issuer 2026-09-28T07:3xZ. Seat commits 9fb05bc6c1 (the builder ported onto lib.silver_ids, the
     inf re-export, the result and the proof) and 4d7188efca; lib/silver_ids.py landed by 1.0.0_SA_CTO~O @88e4e69e69.
     Re-graded on CLOUD: AC2 (s4.AC3) PASS, silver/bd_assets_dim.parquet LastModified 2026-09-28T06:22:06Z, after issue.
     Instance VALID. The dim holds 12,141 rows / 22 cols, asset_id unique; 805 of 805 formerly missing ids are carried (MX-s-2's
     791 grew by 14 trading-day ids). Inf re-export: 6 real callers import, 0 failed. Inf tests: 17 passed, 1 failed. The one
     failure was confirmed by the issuer as pre-existing and environmental: test_silver_write_empty_dim_guard (unchanged
     since 92e654c522, 2026-07-13) dies with FileNotFoundError walking untracked .runtmp/portal-promote-20260820T183300Z
     node_modules on an over-long Windows path. Not caused by this change. -->

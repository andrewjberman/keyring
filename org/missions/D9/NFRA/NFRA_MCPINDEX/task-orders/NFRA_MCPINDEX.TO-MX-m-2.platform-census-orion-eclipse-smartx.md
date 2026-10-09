# NFRA_MCPINDEX task order -- `MX-m-2` -- FWD-4 measure before build: what Orion, Eclipse and SmartX serve today, and whether the catalog knows it

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-m-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-m-2</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~26</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- read-only.
comp-iam: DECLARED-NOT-APPLICABLE -- read-only S3 listing and catalog read.
comp-adversary: DECLARED-NOT-APPLICABLE -- a census; no build.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `MX-m-2` (round 7; `ROUND_ANALYSIS.round6.md` @361b186c92 section 5 item 4)

**The CTO's item:** for Orion, Eclipse and SmartX, a census of served silver data and catalog rows. For each: dataset
keys, newest partition and as-of, the row count, and whether a catalog row exists. Tools are cut in round 8 only where
data is served (no tool over absent data). Denominator printed per platform.

**Where to look (issuer's fact read; verify, never assume complete):**
- Orion: `s3://opal-data-inf/silver/api_dims/...`, `silver/transactions/`, `silver/aum_snapshot/`, `silver/accounts_dim/`.
- Eclipse: `s3://opal-data-inf/silver/eclipse/{date}/...`.
- SmartX: `s3://opal-data-smartx-v2/` (no silver tier found; a consolidated path is marked DEAD in the repo).
- Catalog: the gateway catalog's `silver_datasets` rows (`gateway_query_catalog` is the served reader; the repo's
  emitted catalog under `workflows/atom_decomposition/` is the source). None of the three had a row at the issuer's read.
- Find every dataset prefix by LISTING the bucket's top-level and silver prefixes first (`aws s3api list-objects-v2
  --delimiter /`, paginated client-side), and print that listing's count as the domain before you choose datasets.

**Write** `PLATFORM_CENSUS_round7.json` in your deliverables:
`{"orion": {"denominator": N, "domain_listing": [...], "datasets": [{"key", "newest_partition", "as_of", "rows",
"catalog_row"}]}, "eclipse": {...}, "smartx": {...}}`. `rows` is read from the newest partition (parquet metadata via
`pyarrow` on a downloaded copy in your scratch, or `null` with a `rows_claim: absent` reason). `as_of` is the
partition's own date field where the data carries one, else the S3 LastModified, with `as_of_claim` naming which.
A platform with no served silver data has `datasets: []`, `denominator: 0` and a `finding` line saying where you
looked. Record keys, dates and counts only: no row content.

## 2. BOUNDS

1. Read-only. No write to any bucket, no catalog change, no tool built.
2. Each firm's data is listed under its own bucket; nothing is copied between buckets. No push.
3. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~26/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W26-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1</expected_criteria>
  <criterion id="AC1" cell_refs="MX-m-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round7/checks/m2.AC1.sh; echo "exit=$?"</invocation><expect>OK: orion, OK: eclipse, OK: smartx, each with datasets == denominator and every dataset carrying key/newest_partition/as_of/rows/catalog_row -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~26/NFRA_MCPINDEX.TO-MX-m-2.platform-census-orion-eclipse-smartx.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once: per platform, the denominator and which datasets are
served and fresh enough to carry a round-8 tool.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-7 item 4 (FWD-4). Battery dry-run at base: m2.AC1 FAIL as expected (record
absent).

**ISSUER GRADE (2.0.0_SA_COO~MI, 2026-10-06).** Drained @2234389ca8 (worker 3f8588f71b). m2.AC1 re-run by the issuer
on CLOUD after the drain: orion 24/24, eclipse 8/8, smartx 13/13, RESULT: PASS, exit=0. Rows Z-W26-S1 (SmartX silver
lives in `opal-data-assets`) and Z-W26-S2 (Orion/Eclipse duplicated there) carry to the round-7 slug.

<status>complete</status>
<round>7</round>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

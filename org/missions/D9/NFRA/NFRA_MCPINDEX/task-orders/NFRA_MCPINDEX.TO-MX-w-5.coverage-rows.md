# NFRA_MCPINDEX task order -- `MX-w-5` -- decide, for each of the 36 tools still refused as member (b), a new catalog row it reads or a (c) reason, grounded in the traced source sets

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round24-GATEWAY.md</decomp_doc>
<owned_cells>MX-w-5</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-w-5.coverage-rows</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~81</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one JSON data file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base) and the planted mutants inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-w-5` (round 24, workstream GATEWAY; PRD v0.19 FWD-23 coverage; CTO round-23 analysis, item 5)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). FWD-23 asks that every tool of the gateway census is indexed by the catalog. After round 23 the coverage gate over the 14 channels still refuses 36 tools as member (b): each reads data that no catalog row describes yet, and each has a named owner. This cell decides, for each of the 36, either the catalog row it reads (the issuer writes the row into the catalog at the drain; you write the specification of the row) or a (c) reason (the tool reads no data a catalog row can describe).

**What to build.** `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~81/coverage_rows.json`, one item for each of these 36 tools, exactly these and each once:

- opal-data-assets (5, owner `NFRA_OPLGTW`): `client_get_allocation`, `client_get_fees`, `client_get_holdings`, `client_get_transactions`, `client_resolve_account`
- opal-data-etfs (18, owner `NFRA_OPLGTW`): `etfs_compare_peers`, `etfs_get_coverage`, `etfs_get_fund_bloomberg_characteristics`, `etfs_get_fund_flows`, `etfs_get_fund_holdings`, `etfs_get_fund_nav_history`, `etfs_get_fund_snapshot`, `etfs_get_fund_trades`, `etfs_get_monthly_report`, `etfs_get_new_securities`, `etfs_get_ownership_rollup`, `etfs_get_partner_ownership`, `etfs_get_peer_group_members`, `etfs_get_research_notes`, `etfs_get_rival_fund_holdings`, `etfs_get_rival_page_status`, `etfs_get_security_reference`, `etfs_who_holds`
- opal-data-harvest (3): `harvest_get_published_analysis` (owner `NFRA_OPLGTW`), `harvest_list` and `harvest_read` (owner `AMGT_HARVST`)
- opal-data-mdpf (1, owner `NFRA_OPLGTW`): `mdpf_get_model_composition`
- opal-data-portal-v2 (8, owner `NFRA_OPLGTW`): `mdpf_get_category_views`, `portal_get_cma_assumptions`, `portal_get_correlations`, `portal_get_etf_returns`, `portal_get_factor_tilts`, `portal_get_model_portfolio_timeseries`, `portal_get_peer_performance`, `portal_get_trending`
- dynamodb (1, owner `NFRA_OPLGTW`): `mdpf_get_security_classification`

### The contract (verbatim from the decomposition; it is the whole specification)

**W5 COVERAGE ROWS** `coverage_rows.json`, schema `gateway_coverage_rows/1`: `{"schema","items":[{"tool","owner","disposition":"row"|"c","row":null|{"entity","bucket","prefix","vendor","firm"},"reason":str,"cite":"<path>:<line>"}]}`. One item for each refusal of `COVERAGE_after_apply_20261019.json` (36 tools, class tool_member_b), exactly those; `owner` equals the refusal's `detail`. `row`: a catalog row the tool reads, `entity` unique (not an entity of the catalog and not repeated), `bucket` and `prefix` overlapping an `s3` source of the tool's source set, `vendor` one of the catalog's vendors plus opal, ycharts, microsoft, bloomberg, other; `firm` a string. `c`: the tool reads no data a row can describe, `reason` and an existing `cite`.

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/evidence/COVERAGE_after_apply_20261019.json`: `refusals[]` with `class` tool_member_b, `channel`, `subject` (the tool) and `detail` (the owner).
- the source sets, one file per channel group, each `source_sets/1` with `tools[]` of `{tool, vendors, sources:[{kind, bucket, prefix, vendor, cite}]}`:
  - `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~71/source_sets_assets.json`
  - `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~72/source_sets_etfs.json`
  - `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~73/source_sets_portal.json`
  - `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~74/source_sets_harvest.json`
- the catalog `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` (read-only): sections `silver_datasets`, `portal_datasets` and `harvest_datasets` are the rows, each with `entity`, `bucket`, `prefix` (portal rows name the object in their text), `vendor`, `firm`; read the existing rows of each channel as the MODEL of a row, and read `channels:` for the artifact keys.
- the gateway source under `infra/aws/ec2/opal-gateway/app/` (read-only) for the lines a source cites.

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The worktree carries the sparse folders `workflows/atom_decomposition` and `infra/aws/ec2/opal-gateway/app`; `git sparse-checkout add <folder>` is the only sparse change you may make.
1. For each of the 36 tools, read its `sources` in the source sets and the existing catalog rows whose `bucket` equals a source bucket. A source is already DESCRIBED when a catalog row has the same bucket and the same prefix (or, for a portal object, names the same key). Decide per tool:
   - some `s3` source of the tool is NOT described by any row: disposition `row`, one row for that object family (the deepest prefix the source cites): `entity` a new lower-case word-and-underscore name in the style of the catalog (`<bucket-short>_<last path parts>`), not an entity of the catalog and not used by another item; `bucket` and `prefix` of the source (overlap is graded: one prefix starts with the other); `vendor` the source's vendor; `firm` the firm the data belongs to, or `none` for Opal's own data; `reason` one plain sentence (at least eight words) saying what the row describes; `cite` the source's `cite`.
   - every `s3` source of the tool is already described by a row, or the tool browses prefixes its caller chooses, or the tool reads a store, integration or graph source and no S3 object: disposition `c`, `row` null, `reason` at least eight ASCII words saying why no new row describes it (name the existing entity when a row already describes the data: the tool then needs a link to that row, which the issuer applies; a new row would duplicate it), `cite` an existing `<path>:<line>` (the source's own cite is the first choice).
   - two tools that read the same undescribed object share ONE row: the first tool in the list order takes `row`; the others take `c` and name that entity in the reason.
2. `owner` of each item is the refusal's `detail` (34 are `NFRA_OPLGTW`; `harvest_list` and `harvest_read` are `AMGT_HARVST`).
3. Write the file with the Write tool (JSON, `indent=1`, ASCII), then run both criteria until each prints `RESULT: PASS`. Read `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w5_check.py` for exactly what each arm grades.
4. Then spot-check yourself: open five of your items at random, re-read the cited line and the catalog rows you compared, and fix any that is wrong. The issuer reads a sample at the drain.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's checks or decomposition, `members.yaml`, `pending_members.yaml`, the catalog or its row files, the source-set files, the emitter (`emit_catalog_v02.py`), any file under `infra/` or `app/`, the PRD, or any other file under `workflows/`. No AWS call, no network call, no grant, no deploy, no push.
2. ASCII only in the data file. You write one data file and no code.
3. The data file is JSON written with the Write tool, `indent=1`, ASCII.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w5.AC1.sh` and `.AC2.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w5_check.py`). Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~81/coverage_rows.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~81/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-w-5.coverage-rows.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W81-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 3)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-w-5" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w5.AC1.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~81/coverage_rows.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line (36 tools in scope); the schema; exactly the 36 refused tools, each once, each with the owner of its refusal, a disposition row or c, a non-empty ASCII reason and a cite; the planted mutants (a tool dropped, a tool twice, a wrong owner, a foreign tool, a wrong schema, a bad disposition, a non-ASCII reason) are each refused -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-w-5" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w5.AC2.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~81/coverage_rows.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line; every row item has a new unique entity, a bucket and prefix that overlap an s3 source of the tool, and a vendor in the vocabulary; every c item has a reason of at least eight ASCII words and a cite that resolves to an existing file and line; the planted mutants (an entity already in the catalog, a bucket no source names, a vendor outside the vocabulary, two items with one entity, a three-word reason, a cite to a missing file, a cite past the end of the file) are each refused -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~81/NFRA_MCPINDEX.TO-MX-w-5.coverage-rows.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built by part (rows versus c, how many of each); every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 24, workstream GATEWAY, worker ~81. Source: the CTO's round-23 analysis `ledger/ROUND_ANALYSIS.round23.md` item 5 (`1.0.0_SA_CTO~Z`, 2026-10-20 ~12:3xZ) and PRD v0.19 @7c42c0c743. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round24-GATEWAY.md` (the contract R24.3 W5 is frozen at the cut). Base dry-runs 2026-10-20: `w5.AC1 base: FAIL as expected` and `w5.AC2 base: FAIL as expected` (the deliverable is absent). A scratch reference file (not committed; two rows, thirty-four (c) items, built from the real refusal file, source sets and catalog) passes `w5.AC1` (9 of 9 arms) and `w5.AC2` (9 of 9 arms); the checks prove shape, owner, uniqueness and grounding in the traced sources, not that a (c) judgment is right, which the issuer reads at the drain. CONTRACT SILENCE the issuer resolved on the face (step 1): a tool whose data already has a catalog row takes `c` and names that row, because a second row for the same object would duplicate it and the fix is the tool-to-row link the issuer applies; a literal reading of the contract's (c) ("reads no data a row can describe") does not cover that case. Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>24</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

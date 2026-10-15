# NFRA_OPLGTW task order -- `OG-gp-1` -- G3/G4 remainder: the portal-v2 and mdpf catalog rows with no tool

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gp-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gp-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~109</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and offline tests plus one read-only probe; no deploy, no schedule. The release is a later applier order.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell changes no IAM; the vendor read roles and their never-widen asks belong to the release order that carries it. The probe reads with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling @4356f15f16 (msg 34516, 2026-10-15) on PRD v3.6/v3.7, Andrew's question on why opal-data-assets has no tools, and the CRO's G2 census.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-gp-1` (decomposition addendum R3-T.72, workstream G3G5-REMAINDER, FWD-22)

The CTO's ruling @4356f15f16 names the 25 portal-v2 rows and 7 mdpf rows with no tool. The G3 build (eight portal tools, OG-pt-1..3, live) and `mdpf_get_category_views` (OG-pt-5, live) and the older `mdpf_get_*` tools (account distribution, aggregate AUA, AUM metrics, model benchmarks) already cover some of them: the catalog's `read_tool` moves only after a tool deploys, so a covered row can still read empty.

**Step 1 -- CLASSIFY every assigned catalog row (read only, before any build).** The assigned rows are the 32 DATA_CATALOG v0.5 table rows of these buckets whose `read_tool` is empty:
  - `opal_data_portal_v2_platinum_advi_49financial_perfrp`
  - `opal_data_portal_v2_platinum_advi_49financial_twins`
  - `opal_data_portal_v2_platinum_etfs_positioning_data`
  - `opal_data_portal_v2_platinum_mdpf_account_distribution`
  - `opal_data_portal_v2_platinum_mdpf_aggregate_aua_timeseries`
  - `opal_data_portal_v2_platinum_mdpf_aum_metrics`
  - `opal_data_portal_v2_platinum_mdpf_cottonwood_account_units`
  - `opal_data_portal_v2_platinum_mdpf_manifests_and_archive`
  - `opal_data_portal_v2_platinum_mdpf_non_model_assets`
  - `opal_data_portal_v2_served_benchmark_returns`
  - `opal_data_portal_v2_served_cma_assumptions`
  - `opal_data_portal_v2_served_cma_views`
  - `opal_data_portal_v2_served_correlation_data`
  - `opal_data_portal_v2_served_etf_returns`
  - `opal_data_portal_v2_served_factor_tilts`
  - `opal_data_portal_v2_served_keyword_history`
  - `opal_data_portal_v2_served_market_all_returns_legacy`
  - `opal_data_portal_v2_served_model_portfolio_benchmarks`
  - `opal_data_portal_v2_served_model_portfolio_timeseries`
  - `opal_data_portal_v2_served_model_portfolios_views`
  - `opal_data_portal_v2_served_peer_performance`
  - `opal_data_portal_v2_served_portfolios_legacy`
  - `opal_data_portal_v2_served_sentiment_singletons`
  - `opal_data_portal_v2_served_smartx_model_performance`
  - `opal_data_portal_v2_served_trending_latest`
  - `opal_data_mdpf_feeds_etf_net_assets`
  - `opal_data_mdpf_feeds_model_aua_positions_49financial`
  - `opal_data_mdpf_feeds_model_aua_positions_inflection`
  - `opal_data_mdpf_feeds_model_composition`
  - `opal_data_mdpf_feeds_non_model_aua`
  - `opal_data_mdpf_feeds_partner_held_etf_49financial`
  - `opal_data_mdpf_gold_ai_classified_securities`
For EACH row decide, by reading the tool modules on your head (`app/*.py`; the entity constants and key templates they read) and the spec files named below, exactly ONE class: `COVERED` (a deployed or merged tool already reads that row's data: name the tool; the catalog lags the release, `NFRA_MCPINDEX`'s cell follows each release), `BUILT` (you build a typed tool for it in this cell: name it), or `DEFERRED` (not built this round, with the one-line reason: client-derived data needing its own role, a frozen or empty source, or the CRO spec marks it not for tools). Write `W/CLASSIFICATION.json` = `{"rows": {"<entity>": {"class": "COVERED|BUILT|DEFERRED", "tool": "<name or null>", "reason": "<one line>"}, ...}}` with EVERY assigned row exactly once (the issuer's AC2 recomputes the assigned set from the catalog and requires the keys to be equal to it).
**Step 2 -- BUILD** one typed tool per `BUILT` row family in `portal_served` (a family: the CRO spec's tool proposals; one tool may read several rows of one table family), on the seam below. Do not rebuild a `COVERED` row. Read the spec: `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G3_portal_v2.md`, `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G4_mdpf_delta.md` (the CRO's tool proposals and the overlap finding: all four mdpf gold tables equal the portal-v2 leaf for leaf, so mdpf is ranked only where portal-v2 does not carry it). A tool takes ONE firm per call where its data is firm-derived and never returns a total that adds firm slices.
**Step 3 -- PROBE** (`W/probe_built.py`, a script you write and run; the issuer re-runs it as AC2): for EACH `BUILT` tool, against the REAL bucket with the box's credentials (`INTERNAL_READER_ROLE_ARN` unset) and an Opal stand-in principal, call the tool, assert the envelope is complete and the body is non-empty (or carries a stated `absent_reason`), call it again as a non-Opal principal and assert the refusal with zero reads, and print ONE line per tool: `probe built: <tool> answered True; non_opal_refused True; reads_on_refusal 0`. Print no object content.

### The seam you build on (ALREADY ON YOUR HEAD)

`app/typed_scope.py` (OG-gt-6) over `app/harvest_typed.py`: `Scope(name, bucket, served_prefixes, client, max_bytes)`, `admit_scope(scope, tool, ref, *extra)` (principal present; Opal user, else `typed_opal_only`; call it FIRST, before any S3 call), `list_keys`, `newest_part`, `read_parquet(scope, key, columns, filters)`, `read_json`, and the re-exports `envelope`, `project`, `refusal`, `audit_ok`, `TypedOverCap`. A tool module NEVER imports `get_current_principal` or holds a boto3 client at module scope. `app/etfs_funds.py` and `app/etfs_rivals.py` (merged) are the closest models of a module on this seam: mirror their top (catalog helper by `entity`, served prefixes computed from rows, lazily created client) and never edit them.
KEYS COME FROM THE CATALOG (CTO ruling msg 34173): the gateway CODE types NO S3 bucket, prefix or key literal (the commit-time naming limb refuses legacy layouts and graded tool names ending in `_group`). Each bucket and key template is read at call time from the table's DATA_CATALOG row (`app/integrations/portal_index/integration.py` `runtime_catalog()`; catalog v0.5 is live). A row not found or retired is an `absent_reason` with zero reads. Do NOT write `app/refs/DATA_CATALOG.yaml`. Every tool answers with the envelope (`as_of`, `source_keys`, `denominator`, `absent_reason`), projected to 50 KB (narrow wide rows to the columns a reader asks about and name the dropped columns once in `columns_dropped`).

### Tests, named (a recording fake, in-memory rows and a synthetic catalog fixture with the same shape; an Opal stand-in principal)

- `test_oggp1_ac01`: the classification file names every assigned row exactly once and no `COVERED` row names a tool that is absent from `app/tools.py`/the merged modules.
- `test_oggp1_ac02`: each BUILT portal tool reads ONLY the key template of its catalog row (a synthetic row), reads the newest object, returns the envelope with `as_of` from the object's own date, and answers `absent_reason` (zero reads) for a missing or retired row.
- `test_oggp1_ac03`: each BUILT tool refuses a non-Opal and an absent principal with ZERO reads and an over-cap object `harvest_over_cap`.
- `test_oggp1_ac04`: no BUILT tool name ends in `_group` or `_role`, and `SERVED_PREFIXES` is computed from the rows (a function) for the release's grant generator.

## 2. BOUNDS

- Code, tests and your probe only. No release, no deploy, no IAM or Terraform change, no write to any bucket, no grant written.
- `app/tools.py`, `app/data_entitlement.py`, `app/destructive_ops.py` and the pinned-count tests are NOT yours: the issuer registers every tool and re-pins the counts at the merge, in one commit. Name the registrations you expect in your report.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name, a full email address, an account number or an amount, or any object's content, into a report, a row or a log (counts and booleans only); write the catalog file; override a gate. Tool names must not end in `_group` or `_role` (the naming gate refuses them).
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/portal_served.py
infra/aws/ec2/opal-gateway/tests/test_og_gp1.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~109/CLASSIFICATION.json
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G3_portal_v2.md
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G4_mdpf_delta.md
infra/aws/ec2/opal-gateway/app/typed_scope.py
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/app/internal_role.py
infra/aws/ec2/opal-gateway/app/integrations/portal_index/integration.py
lib/trading_calendar.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~109/`. Rows: id `NFRA_OPLGTW-Z-W109-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gp-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gp1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 4 of 4; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gp-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gp1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)classification: assigned 32 of 32, covered \d+, built \d+, deferred \d+; set equal True; built tools defined (\d+) of \1.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the named tests pass. `AC2`: every assigned row is classified exactly once (the keys equal the catalog's assigned set) and every BUILT tool answers an enveloped read of the real bucket and refuses a non-Opal principal with zero reads.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gp-1.classified-remainder.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once. Your report names the tool registrations and the pinned-count moves you expect the issuer to make at the merge.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G3G5-REMAINDER (decomposition addendum R3-T.72). CTO ruling @4356f15f16 (msg 34516): G2 and the G3/G5 remainders are BUILD cells, they do not wait on a release slot; they rejoin the release queue after OG-ap-22, ahead of OG-ap-17. Each vendor adapter needs its own prefix-conditioned read role and never-widen ask at its release; client data never reads through `gateway-global-internal-reader-role` (PRD v3.2).
- The hookup (registrations, lists, pins) belongs to no cell (CUT BY WRITE SET): the issuer cuts one hookup order per merged batch.
- Pre-cut: AC1 and AC2 base FAIL as expected (module, tests and probe or record absent).

<status>complete</status>
<round>37</round>
<workstream>G3G5-REMAINDER</workstream>
<slot>~109</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

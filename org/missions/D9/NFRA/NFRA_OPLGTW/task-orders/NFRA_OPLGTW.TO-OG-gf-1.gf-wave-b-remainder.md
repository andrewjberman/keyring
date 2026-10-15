# NFRA_OPLGTW task order -- `OG-gf-1` -- G5 wave B: the etfs catalog rows with no tool (the rival-funds rows are OG-ap-22's)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gf-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gf-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~110</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and offline tests plus one read-only probe; no deploy, no schedule. The release is a later applier order.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell changes no IAM; the vendor read roles and their never-widen asks belong to the release order that carries it. The probe reads with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling @4356f15f16 (msg 34516, 2026-10-15) on PRD v3.6/v3.7, Andrew's question on why opal-data-assets has no tools, and the CRO's G2 census.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-gf-1` (decomposition addendum R3-T.72, workstream G3G5-REMAINDER, FWD-22)

The CTO's ruling names the 29 etfs rows with no tool; 14 of them are the rival-funds rows the ten tools of OG-ap-22 (staged) already read, so THIS cell's assigned set is the other 15.

**Step 1 -- CLASSIFY every assigned catalog row (read only, before any build).** The assigned rows are the 15 DATA_CATALOG v0.5 table rows of these buckets whose `read_tool` is empty:
  - `opal_data_etfs_config_etf_universe`
  - `opal_data_etfs_gold_mdpf_new_securities`
  - `opal_data_etfs_silver_bbg_characteristics`
  - `opal_data_etfs_silver_bbg_constituents_issuer_fill`
  - `opal_data_etfs_silver_bbg_derived_geo_allocation`
  - `opal_data_etfs_silver_bbg_derived_sector_allocation`
  - `opal_data_etfs_silver_bbg_derived_summary`
  - `opal_data_etfs_silver_bbg_fund_daily`
  - `opal_data_etfs_silver_bbg_history_topup`
  - `opal_data_etfs_silver_bloomberg_etf_holdings`
  - `opal_data_etfs_silver_bloomberg_history_gaps`
  - `opal_data_etfs_silver_etf_history_csv`
  - `opal_data_etfs_silver_issuer_site_holdings`
  - `opal_data_etfs_silver_netassets`
  - `opal_data_etfs_silver_snapshots`
For EACH row decide, by reading the tool modules on your head (`app/*.py`; the entity constants and key templates they read) and the spec files named below, exactly ONE class: `COVERED` (a deployed or merged tool already reads that row's data: name the tool; the catalog lags the release, `NFRA_MCPINDEX`'s cell follows each release), `BUILT` (you build a typed tool for it in this cell: name it), or `DEFERRED` (not built this round, with the one-line reason: client-derived data needing its own role, a frozen or empty source, or the CRO spec marks it not for tools). Write `W/CLASSIFICATION.json` = `{"rows": {"<entity>": {"class": "COVERED|BUILT|DEFERRED", "tool": "<name or null>", "reason": "<one line>"}, ...}}` with EVERY assigned row exactly once (the issuer's AC2 recomputes the assigned set from the catalog and requires the keys to be equal to it).
**Step 2 -- BUILD** one typed tool per `BUILT` row family in `etfs_silver` (a family: the CRO spec's tool proposals; one tool may read several rows of one table family), on the seam below. Do not rebuild a `COVERED` row. Read the spec: `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G5_etfs.md` (the CRO's tool proposals and the `etfs_get_positioning` extension) and `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G5r_rivalfunds_spec.md`. A tool takes ONE firm per call where its data is firm-derived and never returns a total that adds firm slices.
**Step 3 -- PROBE** (`W/probe_built.py`, a script you write and run; the issuer re-runs it as AC2): for EACH `BUILT` tool, against the REAL bucket with the box's credentials (`INTERNAL_READER_ROLE_ARN` unset) and an Opal stand-in principal, call the tool, assert the envelope is complete and the body is non-empty (or carries a stated `absent_reason`), call it again as a non-Opal principal and assert the refusal with zero reads, and print ONE line per tool: `probe built: <tool> answered True; non_opal_refused True; reads_on_refusal 0`. Print no object content.

### The seam you build on (ALREADY ON YOUR HEAD)

`app/typed_scope.py` (OG-gt-6) over `app/harvest_typed.py`: `Scope(name, bucket, served_prefixes, client, max_bytes)`, `admit_scope(scope, tool, ref, *extra)` (principal present; Opal user, else `typed_opal_only`; call it FIRST, before any S3 call), `list_keys`, `newest_part`, `read_parquet(scope, key, columns, filters)`, `read_json`, and the re-exports `envelope`, `project`, `refusal`, `audit_ok`, `TypedOverCap`. A tool module NEVER imports `get_current_principal` or holds a boto3 client at module scope. `app/etfs_funds.py` and `app/etfs_rivals.py` (merged) are the closest models of a module on this seam: mirror their top (catalog helper by `entity`, served prefixes computed from rows, lazily created client) and never edit them.
KEYS COME FROM THE CATALOG (CTO ruling msg 34173): the gateway CODE types NO S3 bucket, prefix or key literal (the commit-time naming limb refuses legacy layouts and graded tool names ending in `_group`). Each bucket and key template is read at call time from the table's DATA_CATALOG row (`app/integrations/portal_index/integration.py` `runtime_catalog()`; catalog v0.5 is live). A row not found or retired is an `absent_reason` with zero reads. Do NOT write `app/refs/DATA_CATALOG.yaml`. Every tool answers with the envelope (`as_of`, `source_keys`, `denominator`, `absent_reason`), projected to 50 KB (narrow wide rows to the columns a reader asks about and name the dropped columns once in `columns_dropped`).

### Tests, named (a recording fake, in-memory rows and a synthetic catalog fixture with the same shape; an Opal stand-in principal)

- `test_oggf1_ac01`: the classification file names every assigned row exactly once and no `COVERED` row names a tool that is absent from the merged modules.
- `test_oggf1_ac02`: each BUILT etfs tool reads the NEWEST part per date partition only (a fake with a re-run of different values: the answer equals the newer), names its weight unit and passes `claim` through where the row has one.
- `test_oggf1_ac03`: each BUILT tool refuses a non-Opal and an absent principal with ZERO reads, an over-cap object `harvest_over_cap`, and answers `absent_reason` for a missing or retired row.
- `test_oggf1_ac04`: WITHDRAWN by A1 (the `etfs_get_positioning` extension is not in this cell).

## 2. BOUNDS

- Code, tests and your probe only. No release, no deploy, no IAM or Terraform change, no write to any bucket, no grant written.
- `app/tools.py`, `app/data_entitlement.py`, `app/destructive_ops.py` and the pinned-count tests are NOT yours: the issuer registers every tool and re-pins the counts at the merge, in one commit. Name the registrations you expect in your report.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name, a full email address, an account number or an amount, or any object's content, into a report, a row or a log (counts and booleans only); write the catalog file; override a gate. Tool names must not end in `_group` or `_role` (the naming gate refuses them).
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/etfs_silver.py
infra/aws/ec2/opal-gateway/tests/test_og_gf1.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~110/CLASSIFICATION.json
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G5_etfs.md
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G5r_rivalfunds_spec.md
infra/aws/ec2/opal-gateway/app/typed_scope.py
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/app/internal_role.py
infra/aws/ec2/opal-gateway/app/integrations/portal_index/integration.py
lib/trading_calendar.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~110/`. Rows: id `NFRA_OPLGTW-Z-W110-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gf-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gf1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gf-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gf1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)classification: assigned 15 of 15, covered \d+, built \d+, deferred \d+; set equal True; built tools defined (\d+) of \1.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the named tests pass. `AC2`: every assigned row is classified exactly once (the keys equal the catalog's assigned set) and every BUILT tool answers an enveloped read of the real bucket and refuses a non-Opal principal with zero reads.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gf-1.classified-remainder.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once. Your report names the tool registrations and the pinned-count moves you expect the issuer to make at the merge.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G3G5-REMAINDER (decomposition addendum R3-T.72). CTO ruling @4356f15f16 (msg 34516): G2 and the G3/G5 remainders are BUILD cells, they do not wait on a release slot; they rejoin the release queue after OG-ap-22, ahead of OG-ap-17. Each vendor adapter needs its own prefix-conditioned read role and never-widen ask at its release; client data never reads through `gateway-global-internal-reader-role` (PRD v3.2).
- The hookup (registrations, lists, pins) belongs to no cell (CUT BY WRITE SET): the issuer cuts one hookup order per merged batch.
- Pre-cut: AC1 and AC2 base FAIL as expected (module, tests and probe or record absent).

- A1 (issuer, 2026-10-15 ~19:2xZ, worker rows Z-W110-S1..S4, all read): the first seat finished the three tools and its classification (15 of 15; covered 0, built 6 rows over 3 tools, deferred 9) and refused one criterion, rightly. Rulings: (1) `test_oggf1_ac04` and the `etfs_get_positioning` extension are WITHDRAWN from this cell: that tool is registered inside `app/integrations/portal_index/integration.py` (NFRA_MCPINDEX's file, not in this order's `<paths>`), and by Andrew's split the indexing and tooling work is `2.0.0_SA_COO~MI`'s; the issuer routes the extension to that seat by message. gf1.AC1 now reads 3 of 3. (2) RENAME `etfs_get_fund_bloomberg_profile` to `etfs_get_fund_bloomberg_characteristics`: the naming gate types a name ending `_profile` as an instance profile and REFUSES it (row Z-W110 note on `INSTANCE_PROFILE`); do the rename in `app/etfs_silver.py`, `tests/test_og_gf1.py`, `W/CLASSIFICATION.json` and `W/probe_built.py` with a whole-word replace and print the count per file; no BUILT tool name may end in `_group`, `_role` or `_profile`. (3) S1: the AC2 check now counts DISTINCT tools among the BUILT rows, not rows: one probe line per BUILT TOOL (3), as the order says. (4) S3: the cone now holds `tests/`. (5) S4: noted; the snapshot tool is `etfs_get_fund_snapshot`. The first seat's commit `2c4d7a0684` is inherited state: re-record the proof instance from the real outputs after the rename. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>complete</status>
<round>37</round>
<workstream>G3G5-REMAINDER</workstream>
<slot>~110</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

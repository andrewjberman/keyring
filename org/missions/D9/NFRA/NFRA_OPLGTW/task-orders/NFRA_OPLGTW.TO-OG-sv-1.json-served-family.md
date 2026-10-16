# NFRA_OPLGTW task order -- `OG-sv-1` -- the json-served tool family: typed reads of the portal-v2 `json/*` objects that no tool reads (PRD v3.13)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-sv-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-sv-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~113</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and offline tests plus one read-only probe; no deploy, no schedule. The release is the later applier order OG-ap-23.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change. The gateway role already holds GetObject on `opal-data-portal-v2/json/*` (`infra/aws/terraform/opal-gateway/queryv0-iam.tf` line 34), and every row below lives under `json/`. The probe reads with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's cross-adjudication ruling XA-20261016T024917Z-cdcc and PRD v3.13 (corrected: no new IAM), on MCPINDEX's census of catalog rows with no tool.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-sv-1` (decomposition addendum R3-T.76, workstream JSON-SERVED, FWD-22)

Seven catalog rows of bucket `opal-data-portal-v2` are read by portal pages only; no gateway tool reads them. Their `read_tool` is empty. Build ONE module `app/portal_json_served.py` (ONE tool per row, on the typed-scope seam below) and decide each row at build time by its OWN freshness.

The seven rows (entity; catalog `prefix`; catalog-measured lag in trading days at the issuer's cut):
  - `opal_data_portal_v2_served_correlation_data`; `json/correlations/correlation_data.json`; lag 0
  - `opal_data_portal_v2_served_etf_returns`; `json/benchmarks/etf_returns.json`; lag 0
  - `opal_data_portal_v2_served_factor_tilts`; `json/factor-tilts/` (a prefix holding several objects: read the catalog row to see which); lag 0
  - `opal_data_portal_v2_served_model_portfolio_timeseries`; `json/benchmarks/model_portfolio_timeseries.json`; lag 0
  - `opal_data_portal_v2_served_model_portfolios_views`; `json/model_portfolios/views/`; lag 93 -- RULED OUT (stale), do not build
  - `opal_data_portal_v2_served_peer_performance`; `json/peers/peer_performance.json`; a MONTHLY object, lag 9 trading days -- it is stale only if its as-of month-end is earlier than the most recent completed month-end
  - `opal_data_portal_v2_served_trending_latest`; `json/trending/latest.json`; lag 0

**Step 1 -- MEASURE (read only).** For each of the seven, read the object's own as-of date from the real bucket (a `head_object`/small `get_object`, box credentials, no content printed) and compute the lag against the trading-day frontier with `lib/trading_calendar.py`. Write `W/SV1_ROWS.json` = `{"rows": {"<entity>": {"class": "BUILT|RULED_OUT", "tool": "<name or null>", "lag_trading_days": <n>, "reason": "<one line>"}, ...}}` with EVERY one of the seven exactly once. A RULED_OUT row's `reason` must carry its measured number (for example "as-of 2026-06-30, 93 trading days behind T-1"). `model_portfolios_views` is RULED_OUT. A row you measure as stale (by the rule above) is RULED_OUT with that measurement; every other row is BUILT.
**Step 2 -- BUILD** one typed tool per BUILT row in `app/portal_json_served.py`, named `portal_get_correlations`, `portal_get_etf_returns`, `portal_get_factor_tilts`, `portal_get_model_portfolio_timeseries`, `portal_get_peer_performance`, `portal_get_trending` (build only those whose row is BUILT; no name may end in `_group` or `_role`). Each tool takes no required argument except where the object holds several parts (then one `part` argument whose accepted values are read from the catalog row or the object listing, never typed), reads ONLY its catalog row's `bucket` + `prefix`, and answers the envelope (`as_of` = the object's OWN date, `source_keys`, `denominator`, `absent_reason`, `freshness` stating the lag in trading days), projected to 50 KB (name any dropped columns once in `columns_dropped`). Opal principals only (the rows are `opal-internal-only`).
**Step 3 -- PROBE** (`W/probe_sv1.py`, a script you write and run; the issuer re-runs it as AC2): for EACH BUILT tool, against the REAL bucket with the box's credentials (`INTERNAL_READER_ROLE_ARN` unset) and an Opal stand-in principal, call the tool, assert the envelope is complete and the body is non-empty (or carries a stated `absent_reason`), call it again as a non-Opal principal and assert the refusal with zero reads, and print ONE line per tool: `probe sv: <tool> answered True as_of <YYYY-MM-DD> non_opal_refused True reads_on_refusal 0`. Print no object content.

### The seam you build on (ALREADY ON YOUR HEAD)

`app/typed_scope.py` over `app/harvest_typed.py`: `Scope(name, bucket, served_prefixes, client, max_bytes)`, `admit_scope(scope, tool, ref, *extra)` (principal present; Opal user, else `typed_opal_only`; call it FIRST, before any S3 call), `list_keys`, `newest_part`, `read_parquet`, `read_json`, and the re-exports `envelope`, `project`, `refusal`, `audit_ok`, `TypedOverCap`. A tool module NEVER imports `get_current_principal` or holds a boto3 client at module scope. `app/portal_served.py` (merged, `mdpf_get_model_composition`) is the closest model: mirror its top (catalog helper by `entity`, served prefixes computed from rows, lazily created client, the principal read through the `harvest_read` module attribute) and NEVER edit it. `app/portal_models.py` and `app/portal_macro.py` read other `json/*` objects of the same bucket and show the JSON read path.
KEYS COME FROM THE CATALOG (CTO ruling msg 34173): the gateway code types NO S3 bucket, prefix or key literal. Each bucket and prefix is read at call time from the table's DATA_CATALOG row (`app/integrations/portal_index/integration.py` `runtime_catalog()`). A row that is absent, several, or retired is an `absent_reason` with zero reads. Do NOT write `app/refs/DATA_CATALOG.yaml` (another seat is editing it). Expose a `served_prefixes()` function computed from the rows. Each tool states its freshness in trading days.

### Tests, named (a recording fake S3, in-memory objects and a synthetic catalog fixture of the same shape; an Opal stand-in principal) in `tests/test_og_sv1.py`

- `test_ogsv1_ac01`: `W/SV1_ROWS.json` names exactly the seven entities once, `model_portfolios_views` is RULED_OUT with a numeric reason, and every BUILT row names a tool defined in the module.
- `test_ogsv1_ac02`: each BUILT tool reads ONLY its synthetic row's `bucket` + `prefix` (the fake records every key), returns the envelope with `as_of` from the object's own date.
- `test_ogsv1_ac03`: each tool answers `absent_reason` with ZERO reads for a missing row, a retired row and two rows of one entity.
- `test_ogsv1_ac04`: each tool refuses a non-Opal and an absent principal with ZERO reads.
- `test_ogsv1_ac05`: an object over the cap answers `harvest_over_cap`; the answer carries `freshness` in trading days and a stale object (more than one trading day behind T-1; for the monthly object, an earlier month-end than the latest completed one) says so.
- `test_ogsv1_ac06`: no tool name ends in `_group` or `_role`; `served_prefixes()` is computed from the rows and returns exactly the prefixes of the BUILT rows.

## 2. BOUNDS

- Code, tests and your probe only. No release, no deploy, no IAM or Terraform change, no write to any bucket, no grant written.
- `app/tools.py`, `app/data_entitlement.py`, `app/destructive_ops.py` and the pinned-count tests are NOT yours: the issuer registers every tool and re-pins the counts at the merge, in one commit. Name the registrations you expect in your report.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name, a full email address, an account number or an amount, or any object's content, into a report, a row or a log (counts and booleans only); override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/portal_json_served.py
infra/aws/ec2/opal-gateway/tests/test_og_sv1.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~113/SV1_ROWS.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~113/probe_sv1.py
infra/aws/ec2/opal-gateway/app/portal_served.py
infra/aws/ec2/opal-gateway/app/portal_models.py
infra/aws/ec2/opal-gateway/app/portal_macro.py
infra/aws/ec2/opal-gateway/app/typed_scope.py
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/app/internal_role.py
infra/aws/ec2/opal-gateway/app/integrations/portal_index/integration.py
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
infra/aws/terraform/opal-gateway/queryv0-iam.tf
lib/trading_calendar.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~113/`. Of the paths above you WRITE only the first four and the investigation file (append rows); the rest you only read. Rows: id `NFRA_OPLGTW-Z-W113-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-sv-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/sv1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 6 of 6; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-sv-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/sv1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)rows: wanted 7 of 7, built \d+, ruled out \d+; set equal True; views ruled out True; ruled-out reasons carry a measurement True; built tools defined (\d+) of \1.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the six named offline tests pass. `AC2`: the seven rows are decided exactly once, the stale one is ruled out with its number, every BUILT tool exists, and each answered a read of the real bucket and refused a non-Opal principal with zero reads.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-sv-1.json-served-family.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once. Your report names the tool registrations and the pinned-count moves you expect the issuer to make, and the lag you measured for each row.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream JSON-SERVED (decomposition addendum R3-T.76). Origin: MCPINDEX msg 34654 (11 RESEARCH rows with no tool), call sitez-20261016T023921Z-035e, cross-adjudication XA-20261016T024917Z-cdcc, PRD v3.13 @def417d2be with item 2 (a new IAM ask) withdrawn @7656f484ab: the catalog prefixes are all under `json/`, already granted by queryv0-iam.tf:34. `opal-harvest-security-metrics` is NOT built here (it goes to dell1 AMGT_HARVST).
- The tool registrations, the pins and the import line are the ISSUER's hookup at the merge (a one-line batch), then they ride `OG-ap-23`.
- Pre-cut: AC1 and AC2 base FAIL as expected (module, tests, record and probe absent).

<status>complete</status>
<round>37</round>
<workstream>JSON-SERVED</workstream>
<slot>~113</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

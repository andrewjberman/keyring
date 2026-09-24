# INF (Inflection / Orion) Performance -- the live path, design card

Author `2.0.0_SA_COO~P`, 2026-09-24 ~21:0xZ. Goal criterion 1 for Inflection: the same one-account path Cottonwood
serves (bd_selected + one-use plan + retained report). Every line below is measured unless it says `[to build]` or
`[to confirm]`.

## What exists

| Piece | State | Where |
|---|---|---|
| Route | host `api.cloud.orionadvisor.com`, token path `/api/v1/Security/Token`, `scope` = `/api/v1/Reporting/Scope`, secret name `orion/credentials` | `performance/tenants.py:166-172` |
| Credential in use by the estate | `s3://opal-data-inf/orion/jwt/current.json` (`{"jwt": ...}`, sent as `Authorization: Session <jwt>`), re-written twice a day: 09:51Z and 21:01Z on 09-21..09-24 (S3 version LastModified, value never read) | `data/inf/manual_api/probe_positions_mv_daily.py:62-91` |
| Response parser | `orion_adapter.adapt` over one Scope response: summary DECIMAL_FRACTION, compact breakdown PERCENT, linked factors reproduce the summary to 1.2e-13 | `performance/orion_adapter.py` |
| Account mapping | the raw account key IS the Orion id: `accounts_v2.account_id` (`_ids/raw_keys.json`, inflection); the canonical id is `opaque_account("inflection", account_id)` | `_ids/raw_keys.json`; the COT analogue `cot_account_mapping.py:45-89` |
| Request grammar | ONE captured Scope request (orionpt2.har, 2026-09-10T13:42:09Z, 2354-byte answer): `{entity, entityIds[], asOfDate, clientPerformanceInclude, accountManagementOverrides[], flags, calculations:[{$type: context-scope, contextChange:{reportCategoryId, performanceOption{$type: performance, calculationMethod: TWR, ...}, comparisonOption}, calculations:[{id, $type: grouping, grouping, calculations:[{id, $type: activity, contextChange:{dateRange{$type: date-range, startDate, endDate, startDateMethod}, activityOption}}...]}]}]}` | `%USERPROFILE%\Downloads\orionpt2.har` (not in the repo; carries a session and client ids) |
| The daily/compact performance request | NOT on disk: the CRO recon tool (sha256 bb5e4a73..) that sent it at 13:57Z is absent; only its response is kept (`performance/fixtures/orion_daily.json`, scrubbed) | `docs/briefs/sources/INVESTOR_REPORTING_PERFORMANCE_EVIDENCE_20260910.json` |
| Estate performance data | `opal-data-inf/bronze/orion-api/*/performance_dim.csv` is STALE since 2026-04-28 (its own docstring), so it is not a source | `infra/aws/lambda/inf-pipeline/inf-performance-daily/pull_inflection_performance_dim.py:17` |

## What to build

1. `performance/inf_selected.py` [to build], the bd_selected twin:
   - `requests_for(mapping, account, start, end)` builds ONE Scope body: entity Account, entityIds [orion id], the
     captured context-scope, one `grouping` Account, with calculations `performance` (id `Period`) and the compact
     `performance-breakdown` (`returnStyle.cumulative = false`) over the window.
   - `calculate` does the same identity checks as COT: exactly one Account group, `groupEntityId` == the mapped id,
     summary vs linked-factor agreement, and the provider data window inside the requested one, published as actual
     dates (dd1811bbaa's rule).
2. `inf_account_mapping` [to build]: scan `opal-data-inf silver/api_dims/accounts_v2` at the directory's as-of and
   match `opaque_account`. It is P's module in `performance/` (the gold `investor_reporting/` directory is ~M's).
3. The one-use gate is generalized from `firm == COT` to a per-firm plan (same claim row, same digest rule) [to build].
   The transport reads the JWT object by name, with no fallback. A new IAM read on
   `opal-data-inf/orion/jwt/current.json` goes through a ledgered plan.
4. `COMPOSED_FIRMS` gains Inflection only after (1)-(3) pass offline against `fixtures/orion_daily.json`.

## What only a live call can settle [to confirm]

The exact field names of the performance and breakdown calculations in the REQUEST are reconstructed, not
captured. The first worded use is therefore also the grammar's proof. A 4xx spends that use with a named refusal.
To avoid that, the builder can be diffed first against a fresh browser HAR of Orion's Performance screen for one
account. That is Andrew's capture, and costs no vendor use by a seat.

## Asks this card implies (none sent yet)

- Andrew: one per-use word for an INF account (card 2 shape), after (1)-(4) land.
- Optional, cheaper: one Orion Performance-screen HAR for a single account, to pin the request grammar before the use.

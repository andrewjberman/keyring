# Brief: Pre-Stage Client Detail at Pipeline Time

**Date:** 2026-02-25
**From:** Systems Architect
**To:** DevOps / Data Scientist
**Reference:** `portal/docs/features/advisor_intelligence/ARCHITECTURE.md`

---

## Problem

`bd-client-detail` Lambda OOMs at 2048 MB loading `gold/account_performance.parquet`
(~350 MB compressed, ~10M rows). It loads the entire file, filters to one
`relationship_id` in memory, then discards 99.9% of the data. This is the wrong
architecture — the Lambda should never touch the full dataset.

## Solution

Pre-generate per-client `ClientDetailResponse` JSON at pipeline time. The data is
already in memory inside `bd-portal-advisor-publisher` (6144 MB, loads the same
parquets). Extend that publisher to write one JSON per client alongside the
per-advisor `book.json` files it already produces.

After this change, `bd-client-detail` becomes a thin auth gate + S3 read:
```
auth check (role == admin) → s3.get_object(f'gold/clients/{relationship_id}.json') → return
```

No parquet loading. No pandas. Could run at 256 MB / 5s timeout.

## S3 Key Structure

```
opal-data-bd/
  gold/
    clients/
      {relationship_id}.json       ← NEW: full ClientDetailResponse
    advisors/
      {advisor_id}/book.json       ← existing (bd-portal-advisor-publisher)
    account_performance.parquet    ← existing (EC2 gold layer)
    ...
```

## What `gold/clients/{relationship_id}.json` Contains

Exact same `ClientDetailResponse` shape that `bd-client-detail` currently builds
on the fly. Every field, same structure, same keys:

```
{
  generated_at, data_as_of, firm_id, client_key, client_name,
  headline:     { total_aua, account_count, ... }
  tax:          { taxable, qualified_aua, cost_basis_by_year[], top_gain_positions[], open_lots[], ... }
  income_fees:  { ... }                          (zeroed — BD doesn't carry this)
  portfolio:    { unique_holdings, ... }          (partial — no asset class taxonomy)
  engagement:   { net_flows_ttm, avg_relationship_years, ... }
  accounts:     [ { account_id, tax_status, total_aua, nna, ... } ]
}
```

Full schema: see `bd-client-detail/lambda_function.py` response builders.

## Where to Add the Generation Logic

**Extend `bd-portal-advisor-publisher`**, not `bd-portal-publisher`.

Rationale:
- advisor-publisher already loads all three required parquets at 6144 MB
  (account_performance, client_tax_liability, client_dimension)
- It already iterates per-architect and has `rel_ids` per advisor
- It does NOT currently load `holdings_lots` — this is the one addition needed

The generation loop fits naturally after the existing `build_advisor_books()`:

```python
# Existing: per-advisor books
build_advisor_books(acct, tax, cdim, latest_date, today)

# New: per-client detail JSONs
build_client_details(acct, tax, lots, cdim, latest_date, today)
```

### Data sources needed per client

| Section           | Source                    | Already loaded? |
|-------------------|--------------------------|-----------------|
| headline          | account_performance      | Yes             |
| tax (standard)    | account_performance      | Yes             |
| tax (yang fields) | client_tax_liability     | Yes             |
| tax (open_lots)   | holdings_lots (latest)   | **No — add**    |
| engagement        | account_performance + client_dimension | Yes |
| accounts          | account_performance      | Yes             |

**One new parquet load:** `gold/holdings_lots/{latest_snapshot}.parquet` (~5 MB).
This is small and won't affect the 6144 MB memory budget.

### Client count estimate

~100-200 unique `relationship_id` values in the latest snapshot (49 Financial).
Each JSON is ~5-30 KB depending on lot count. Total S3 writes: ~200 PUTs per
pipeline run. Negligible cost and latency.

## Changes to `bd-client-detail` Lambda

Replace the parquet-loading logic with a single S3 GET:

```python
def lambda_handler(event, context):
    # Auth check (already added in bd-v2.2.0)
    auth_context = event.get('requestContext', {}).get('authorizer', {})
    role = auth_context.get('role', '')
    if role != 'admin':
        return _err(403, 'Forbidden')

    relationship_id = _extract_client_key(event)
    if not relationship_id:
        return _err(400, 'Missing clientKey')

    # Read pre-generated JSON (replaces all parquet loading)
    try:
        resp = s3.get_object(
            Bucket=INPUT_BUCKET,
            Key=f'gold/clients/{relationship_id}.json'
        )
        body = resp['Body'].read().decode('utf-8')
    except s3.exceptions.NoSuchKey:
        return _err(403, 'Forbidden')  # 403 not 404 (invariant #3)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Cache-Control': 'no-store, no-cache, must-revalidate',
            'Pragma': 'no-cache',
        },
        'body': body,
    }
```

After this change:
- Remove pandas/pyarrow layer dependency from bd-client-detail
- Reduce memory to 256 MB, timeout to 10s
- Remove all response builder functions (`_build_headline`, `_build_tax`, etc.)

## Terraform Changes

```hcl
module "bd_client_detail" {
  # ...
  memory_size   = 256       # was 2048
  timeout       = 10        # was 30
  layers        = []        # was [local.pandas_layer] — no longer needed
}
```

## Phase 1 Compatibility

When `user` role goes live, the auth check in `bd-client-detail` expands to:

```python
if role == 'user':
    bd_architect = auth_context.get('bd_architect_name', '')
    # Check if this client is in the advisor's book
    # Option A: read the advisor's book.json (already pre-generated)
    # and verify relationship_id is in the client list
    book_key = f'gold/advisors/{_advisor_id(bd_architect)}/book.json'
    book = json.loads(s3.get_object(Bucket=INPUT_BUCKET, Key=book_key)['Body'].read())
    client_keys = {c['client_key'] for c in book.get('clients', [])}
    if relationship_id not in client_keys:
        return _err(403, 'Forbidden')
```

The book membership check uses the pre-generated `book.json` (already has a
`clients[]` array with `client_key` values). No parquet loading needed for
the auth check either.

## Execution Order

1. Add `holdings_lots` loading to `bd-portal-advisor-publisher`
2. Add `build_client_details()` function — generates per-client JSONs
3. Build + upload updated advisor-publisher artifact
4. Rewrite `bd-client-detail` to S3 GET (remove parquet logic)
5. Build + upload updated client-detail artifact
6. Terraform apply (advisor-publisher code update + client-detail memory/layer change)
7. Trigger pipeline run (or wait for daily) — generates `gold/clients/*.json`
8. Verify: curl client detail endpoint with admin JWT → 200, fresh data, fast response
9. Tag bd-v2.3.0

## Files to Modify

| File | Change |
|------|--------|
| `infra/aws/lambda/bd-pipeline/bd-portal-advisor-publisher/lambda_function.py` | Add holdings_lots load + `build_client_details()` |
| `infra/aws/lambda/bd-pipeline/bd-client-detail/lambda_function.py` | Replace parquet logic with S3 GET |
| `infra/aws/terraform/bd-pipeline/lambdas.tf` | bd-client-detail: memory 256, timeout 10, remove layer |
| `infra/aws/lambda/ci/lambda-source-map.json` | Verify both functions listed |

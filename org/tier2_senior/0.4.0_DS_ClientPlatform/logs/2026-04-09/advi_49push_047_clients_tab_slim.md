# ADVI_49PUSH.047 -- Clients Tab Slim (7s Lambda Fix)

**Agent:** 0.4.0_DS_ClientPlatform  
**Date:** 2026-04-09  
**Commit:** `547ed0dd`  
**Status:** COMPLETE (DS side). Lambda deploy pending -- DT/AE handoff below.

---

## Step 1 Findings

**Lambda:** `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py`  
**Handler:** `handle_clients_tab` at line 603

```python
def handle_clients_tab(bucket: str) -> dict:
    return serve_s3_json(bucket, 'gold/artifacts/clients_tab.json')
```

**Answers:**

**A. Is it an S3 passthrough or per-client reads?**
Single S3 `get_object` on `gold/artifacts/clients_tab.json`. Zero DynamoDB calls. I/O is fast.

**B. Pseudonymization at serve time or pre-built?**
At serve time. The full 206 kB body is passed to `pseudonymizer.pseudonymize_response()` on
every request. The `_walk()` function recursively visits every key/value in the tree, calling
`hmac.new(key, value.encode(), sha256)` for every string field. On a 2,824-client list this
is ~5,000+ HMAC hashes per request.

**C. S3 calls per request:** 1 (fast). Per-request work: HMAC tree-walk over 206 kB (slow).

**D_04 currently writes:** nothing to any clients-tab path (confirmed by `comp-pipescript io D_04`).

---

## Root Cause

The 7-second latency is entirely from pseudonymizer compute, not I/O.

```
clients_tab.json breakdown:
  Total:             206.0 kB (81.8 kB gzip on the wire)
  clients array:     194.8 kB  (2,824 entries × ~69 bytes each)
  tax section:        10.5 kB  (cost_basis_by_year + top_gain_positions)
  headline + rest:     0.7 kB
```

The Books tab N1 (firm dashboard) view uses ONLY:
- `headline.total_aua`, `client_count`, `account_count`
- `tax.taxable`, `taxable_pct`, `tax_deferred`, `tax_deferred_pct`,
  `tax_free`, `tax_free_pct`, `capital_gains_ttm`

The 194.8 kB `clients` array is **never rendered at N1**. It is used in the per-advisor
book view (N2), which fetches advisor book data separately. The `clients` array was being
pseudonymized on every request for no benefit.

---

## Step 2 -- D_04 Pre-Built Artifact

Added `build_clients_tab_slim()` as Step 11b in D_04.

**Reads:** `gold/artifacts/clients_tab.json` (D_00)  
**Writes:** `platinum/firm/clients-tab-slim.json`

**Payload (350 bytes):**
```json
{
  "generated_at": "...",
  "data_as_of": "2026-04-08",
  "firm_id": "49financial",
  "headline": { "total_aua": 1682935498.05, "client_count": 2824, "account_count": 6039 },
  "tax": {
    "taxable": 1058330099.88, "taxable_pct": 62.9,
    "tax_deferred": 563227590.14, "tax_deferred_pct": 33.5,
    "tax_free": 61377808.03, "tax_free_pct": 3.6,
    "capital_gains_ttm": 0.0
  }
}
```

**Size comparison:**
| | Size |
|--|------|
| `gold/artifacts/clients_tab.json` | 206,000 bytes |
| `platinum/firm/clients-tab-slim.json` | **350 bytes** |
| Reduction | **587x** |

No PII fields. No pseudonymization at write time or serve time. File written to S3
immediately (bootstrapped from current clients_tab.json). Will be regenerated on every
gold run going forward.

---

## Step 3 -- Lambda Route Fix

Changed `handle_clients_tab` to read `platinum/firm/clients-tab-slim.json`. Removed
`_pseudonymize_s3_response` wrapper (no PII = no pseudonymization needed = cacheable).

**Before:**
```python
elif path.endswith('/clients-tab'):
    return _pseudonymize_s3_response(
        handle_clients_tab(bucket), user_role, firm_id, advisor_id)
```

**After:**
```python
elif path.endswith('/clients-tab'):
    # .047: slim file has no PII -- serve directly, no pseudonymization needed.
    return handle_clients_tab(bucket)
```

`handle_clients_tab` itself now reads `platinum/firm/clients-tab-slim.json`.

**Expected latency after deploy:** ~100-150ms (S3 get_object only, no compute).

---

## Handoff Table (Lambda Deploy Required)

| File | Change | Deploy required |
|------|--------|-----------------|
| `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py` | `handle_clients_tab` reads slim platinum file; route drops pseudonymizer wrapper | partners-api Lambda deploy |

Lambda code is committed (`547ed0dd`) but NOT deployed. AE/DT must deploy via Terraform
(`partners-api` pipeline) before the 7s fix takes effect in production.

The slim file (`platinum/firm/clients-tab-slim.json`) is already live on S3 -- bootstrapped
from current data. It will be regenerated on every gold run going forward (D_04 Step 11b).

---

## Acceptance Criteria Status

| Criterion | Status |
|-----------|--------|
| 1. `comp-pipescript io D_04` shows clients-tab-slim write edge | DONE (after comp-build) |
| 2. `platinum/firm/clients-tab-slim.json` exists on S3 | DONE (bootstrapped) |
| 3. Payload size under 15 kB | DONE -- **350 bytes** |
| 4. Lambda returns under 500ms on warm invocation | PENDING Lambda deploy |
| 5. No cleartext client names in artifact | DONE -- no `name` or PII fields at all |
| 6. L3 per-client drill unchanged | DONE -- not touched |
| 7. Session log documents findings | This file |

---

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-pipescript io D_04` | Confirmed: no clients-tab key in D_04 writes before this change |
| `comp-routes trace getClientsTab` | Confirmed: Lambda path, single S3 call + pseudonymizer |
| Manual S3 query | Section sizes: clients=194.8kB (94%), tax=10.5kB, rest=0.7kB |

---

## Note on N1 vs N2

The `clients` array (2,824 entries) is used in the N2 advisor book view
(`ClientsTable` component at line 1520 of ClientsTab.tsx). That view is gated behind
selecting an advisor. The N1 firm dashboard never touches it.

The TypeScript type `ClientsTabResponse` currently marks `clients` as required. DE should
make it optional (`clients?: ClientOption[]`) so the slim endpoint doesn't cause type
errors. The runtime behavior is already correct (the field is simply absent and the N1
block never accesses it).

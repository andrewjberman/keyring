# SIGN-OFF (1.0.0_SA_CTO half) -- Holdings L0 CATEGORY shape (IB-mr-202) and source vendor keys (IB-mr-203), one re-mint

**Requests @`542b519e98` (2.0.0_SA_COO~M msg 102598):**
- `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_L0_CATEGORIES_20260929.md`, blob `091c951203ff...`
- `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_VENDOR_KEYS_20260929.md`, blob `e6174fe01fc0...`

**Signed:** 1.0.0_SA_CTO, 2026-09-29 ~05:1xZ. The COO half is signed with its release order, which this half adopts.

## Signed, as the requests read them

- **The act:** one re-mint of the three Holdings packages under its own ledger; the next publication serves the new
  shape. No Terraform, IAM or schedule change.
- **Measured on the local candidate (business date 2026-09-25):** SECURITY dollar totals bit-identical at all three
  firms; `accounts_l0_sum_mismatch` 0 and `accounts_with_non_category_child` 0 at all three; node counts unchanged at
  49F (152,280) and INF (32,405); COT 17,633 -> 17,637 (+4) as its 464 MODEL_WRAPPER nodes become CATEGORY nodes,
  with the assigned strategy kept on the ACCOUNT (464 of 938). `source_vendor_keys`: 49F schwab+smartx, INF
  eclipse+orion, COT blackdiamond -- registry keys, no hand-kept map (ruling on UIC-14).
- Implements this seat's rulings 102475 (producer-served L0 totals) and UIC-14 (the snapshot names its vendors).

## Readers counted, and the order that binds the re-mint

1. The deployed handlers' contract copy gains `CATEGORY`, `source_vendor_keys` and `assigned_strategy` ADDITIVELY
   and is deployed first (2.0.0_SA_COO~P).
2. The portal reads `CATEGORY` (wire union, `NODE_KIND_FOR_WIRE`, `HoldingsNode['kind']`) on portal PROD
   (2.0.0_SA_COO~D; PROD promotion by its own route).
3. Then the re-mint; at the next publication the served page is read: the handler accepts the document, the AD-01
   card shows Models / SMAs / Client with producer-served amounts, the COT account shows its assigned strategy.

No interim where a category row renders as a security row is accepted. **Rollback per key:** re-put the prior
packages (members-sha256 in the ledger) and repoint each firm's served index to its prior revision.

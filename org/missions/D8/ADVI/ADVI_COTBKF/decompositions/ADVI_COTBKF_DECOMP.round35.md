# ADVI_COTBKF decomposition -- ROUND 35 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~11:2xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s ADDENDUM 9.1 @3093730512 (msg 3188), which places this cell in "round 34 or 35".
- Round 34's issuance is closed to new files (one issuance per round; to-pipeline-gate refused an added order at ~11:2xZ), so it is
  round 35.
- Round 34 stays open: CB-ah-2 is running and CB-ah-3 is held. This round's cell is disjoint from both.

**Reading:** CB-ah-1 classed `cross_firm` (@248cb44fa0; row W61-S1 BLOCKING). The generated `_CROSS_FIRM_FOREIGN_BUCKETS` already bars
`data/cot/` from `opal-data-bd`, so this is CONTAMINATED DATA, not live code.
- Cell 1 is a read-only provenance trace of how 49F's constants entered `opal-data-cot`.
- The three bonds stay held from the rebuild (COO half @0071b97a83).
- Their deletion is Andrew's act, listed with keys and versions once the trace names them.

**Rule 24.** Domain: ADDENDUM 9.1's one new item -> one cell.

## Measured constraints (issuer, ~11:1xZ)

1. `s3://opal-data-cot/silver/prices/canonical_prices.parquet` has ONE object version (LastModified 2026-06-09T20:42:16Z). There is no
   version history to bisect.
2. The rows carry 49F's constants exactly (1.0188 / 0.9804 / 0.9037), from
   `data/black_diamond/scripts/silver/scoped_price_exceptions.json`.
3. `data/cot/scripts/gold/build_canonical_prices_v2.py:22-24` states that cot does not run the inject. The cot run config sets
   `BD_S3_BUCKET=opal-data-cot` (`infra/aws/terraform/cot-pipeline/ssm.tf:233`, `data/cot/scripts/gold/gold_dispatch.sh:62`).

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-ai-1` | read-only provenance trace of the `bd_txn_price` rows in `opal-data-cot`: keys, versions, writer metadata, first write, route, delete list for Andrew | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~63` |

**Fan-out:** `1 of 1 chains, cap 8`.

# ADVI_COTBKF decomposition -- ROUND 37 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~13:2xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s ruling on row W64-S1, inside the CB-aj-2 CTO half @a614350d84 (msg 3346).

The source order for the three bonds (05613L3H2, 95000U2D4, 651639AX4):
1. Cottonwood's OWN custodian-reported price, from the cot tree, carrying the basis `custodian_reported`;
2. otherwise the bond stays UNPRICED, with reason `NO_FIRM_OWNED_SOURCE`.

Never another firm's price, and never a non-bond-specific proxy. The ruling names "one measurement cell in the next round". This is it.
Round 36's CB-aj-2 (the 38-key rewrite) is applying on the applier, and this cell is disjoint from it.

**Rule 24.** Domain: one item -> one cell.

## Measured constraints (issuer)

1. The bonds enter the cot accounts as transactions. Round 35 found the original problem was a mis-routed Yahoo EQUITY ticker
   (49F's exceptions file `reason` field). Cottonwood's own custodian data (Commonwealth / cot silver transactions and holdings) may
   carry a per-unit price or market value for each bond. That is unmeasured.
2. Cot-tree data lives in `opal-data-cot`. This project's Commonwealth delivery is read by the chain in
   `data/assets/scripts/silver/` (`commonwealth_transactions.py`, `commonwealth_daily_holdings.py`).

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-ak-1` | read-only: does Cottonwood's own data carry a custodian-reported price for the three bonds, by date; class per bond | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~65` |

**Fan-out:** `1 of 1 chains, cap 8`. A hit re-enters a bond as its own delta, under its own pair, in a later cell.

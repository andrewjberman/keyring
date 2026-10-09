# ADVI_COTBKF decomposition -- ROUND 47 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~15:2xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `2.0.0_SA_COO~D2`'s msg 3564, which releases the hold of IRPT_DASHBD ADDENDUM 13.2 @304cb81ef6. IRPT_DASHBD.TO-DB-b-102 is
drained @e18a26ad12. `build_manifest`, the row frame and the method row now take `method_version` from the firm's `sources.json`
entry:
- row 2 is `custodian_reported` (Schwab carries 2 explicitly);
- row 3 is `positions_based`;
- a firm with no entry writes `absent`;
- a positions-based entry naming 2 is refused.

The Cottonwood entry must declare `method_version` 3 before CB-al-2 (round 38, held) runs under its own pair.

**Rule 24.** Domain: one item -> one LOCAL cell: declare `method_version` 3 on the `_commonwealth_delivery` entry and rebuild through
the changed producer. CB-al-2 is released by amendment on this cell's rebuilt manifests, under its pair.

## Measured constraints (issuer, ~15:2xZ)

1. `sources.json` at HEAD (it carries @e18a26ad12):
   - `_commonwealth_delivery` = `{registry_key: z09, valuation_source: positions_x_as_traded_close, fee_treatment: net_of_fees,
     price_basis: as_traded}`, with no `method_version`;
   - `schwab_08335338.method_version` = 2.
2. IRPT_DASHBD's record: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~77/METHOD_FROM_SOURCE.json`
   (rule-24: `METHOD_ROW_RULE24.md`).

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-au-1` | add `method_version: 3` to the `_commonwealth_delivery` entry (the one key); rebuild Cottonwood `account_return_daily` locally through the changed producer; every manifest and row reads `method_version` 3; IRPT_DASHBD's tests green | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~74` |

**Fan-out:** `1 of 1 chains, cap 8`. Round 38's CB-al-2 follows on this drain.

# ADVI_COTBKF decomposition -- ROUND 60 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11 ~05:5xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** the CTO half of the CB-al-2 pair, `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R59_ARD_COTTONWOOD_MINT_CTO_HALF.md`
@1013274c3f (msg 4211), SIGNED on seven conditions. Two of them name reads the adapter cannot make today.
- **Condition 2:** before `--apply`, the applier shows the exact day `manifest.json` the producer will write: `method_version` 3,
  the row-3 method sentence, `valuation_source` `positions_x_as_traded_close`, `fee_treatment` `net_of_fees`, `price_basis`
  `as_traded`; the custodian method's text anywhere in it is a STOP; "if the tool cannot show it without writing, STOP". The adapter
  has no such mode (issuer read of `main` at 6e4419bcd7).
- **Condition 3:** `--verify-served` reads each served `manifest.json` back for those five fields, 3,325 of 3,325. `verify_served`
  reads `data.parquet`, the sidecar and the method row only (issuer read of the function at 6e4419bcd7).

**Rule 24.** Domain: the conditions of the signed pair the tool cannot yet meet -> one cell. Conditions 1, 4, 5, 6 and 7 need no
code: 1 is a CLI read by the applier, 4 the tool already does, 5 to 7 are the applier's and the ledger's.

## Measured constraints (issuer)

1. **The pair pins the adapter at @84ef9e0972.** This cell changes the adapter, so the pin moves: the issuer re-states the pin to the
   CTO after the drain (a read-only mode and a wider read-back; `apply_days` is not touched).
2. **No S3 write and no deploy.** The new read-back is exercised on faked S3. The show mode makes no S3 call at all.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bh-1` | a no-write mode shows the day manifest the producer will write and refuses on the custodian method's text; `--verify-served` reads the five method fields of every served day manifest | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~87` |

**Fan-out:** `1 of 1 chains, cap 8`. DIRECT-ACT cell (one cell, under 300 product lines, LOCAL): its close is the one real run by
the issuer.

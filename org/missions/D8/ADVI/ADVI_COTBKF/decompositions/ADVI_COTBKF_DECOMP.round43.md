# ADVI_COTBKF decomposition -- ROUND 43 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~14:3xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:**
- `1.0.0_SA_CTO~DELL2`'s IRPT_DASHBD ADDENDUM 13.1 @49293e07e9 (msg 3414) and COTBKF ADDENDUM 13 (round 38 waits only on that cell);
- `2.0.0_SA_COO~D2`'s msg 3452: IRPT_DASHBD.TO-DB-b-96 is drained @ce9f482be0.

The returns manifest now reads `valuation_source`, `fee_treatment` and `price_basis` from the source's entry in
`data/assets/scripts/gold/irpt_reporting/sources.json`. A source without them writes `absent`. `sources.json` declares no Cottonwood
channel, so CB-al-2 needs one.

**Rule 24.** Domain: one item -> one cell: the Cottonwood channel entry, the adapter re-pointed to it with `return_basis=TWR`, and a
local rebuild. CB-al-2 (round 38, held) is released by amendment on this cell's rebuilt manifest, under its pair.

## Measured constraints (issuer, ~14:3xZ)

1. `sources.json` doc: "one entry per custody channel ... A new firm channel is a new entry here, never a code branch." Its
   `_no_firm_token_comment`: no firm token appears in the file; the entry resolves its firm through `lookup(registry_key)`.
   - An existing entry (`schwab_08335338`) carries `valuation_source=custodian_reported`, `fee_treatment=gross_of_advisory_fees` and
     `price_basis=custodian_closing_price`, plus about 60 keys for the custodian compute path.
2. **Hazard to rule out IN the cell:** the producer's own declared-source iteration (`declared_sources`, `account_return_daily.py`
   :291) and IRPT_DASHBD's scheduled handler (`infra/aws/lambda/investor-reporting/reporting-gold/handler.py`) must not treat a
   Cottonwood entry as a custodian channel to COMPUTE. Cottonwood rows come from ADVI_COTBKF's adapter, not from the producer's
   compute path.
   - The deployed Lambda packages `sources.json` via its `staged_from` pins, so a repo edit does not reach production until
     IRPT_DASHBD redeploys. The cell still proves the producer's code path is safe with the entry present.
3. **Values per ~D2:** `valuation_source=positions_x_as_traded_close`, `fee_treatment=net_of_fees`, `price_basis=as_traded`. The cell
   checks them against the producer's admitted vocabularies.
4. **The file is IRPT_DASHBD's.** Adding a firm channel is its declared extension point, and ~D2 named this entry as CB-al-2's need. The
   edit is confined to adding the one entry.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-aq-1` | add the Cottonwood channel entry to `sources.json` (method fields; no firm token; producer compute path proven safe); adapter `return_basis=TWR` from the entry; local rebuild with the manifest read back | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~70` |

**Fan-out:** `1 of 1 chains, cap 8`. Round 38's CB-al-2 follows on this cell's drain.

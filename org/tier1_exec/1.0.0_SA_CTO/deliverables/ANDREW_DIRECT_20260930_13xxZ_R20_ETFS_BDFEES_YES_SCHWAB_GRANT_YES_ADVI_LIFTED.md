# ANDREW-DIRECT 2026-09-30 ~13:0xZ -- R20 yes (ETF + BD fees), Schwab grant widening yes, platinum/advi hold lifted

**Where:** the 1.0.0_SA_CTO~O terminal, site Z. He was answering three items this seat listed as acts only he can do
(tick logs 29, 32 and 35).

**His words, VERBATIM:**
> "yes thats fine on naming exception. Regarding schwab, sure. advi tool, what not yet are you referring to? but yeah
> certainly whatever needs to be lifted should be lifted"

## What each answer covers (no wider, no narrower)

1. **"yes thats fine on naming exception"** is his CLAUDE.md rule 30 / `infra/logic/02_DOCTRINE.md` R20
   acknowledgement of ONE declared departure covering the two served legacy keys put to him:
   - (a) `opal-data-portal-v2` `platinum/etfs/positioning_data.json`, read at NFRA_MCPINDEX MX-t-10's new sites (the
     catalog row, the emitter and the ETF tool). This is ruling B3 of `REINSTATE_RULINGS_20260930.md`.
   - (b) `opal-data-bd` `silver/fees/` (scope `49financial`), read by MX-t-13 (`blackdiamond_list_fees`) and its reader
     role, released by MX-r-7.
   - The departure is READ-ONLY, at those keys, where the data lives today. It does not move either key and does not
     authorize any write. Its end condition: when the owning migration moves a key onto the builder grammar, that key's
     departure ends. For (b) that is ADVI_FIRMBKTS. For (a) no migration owns `platinum/etfs` yet (Z-W15-S5).
2. **"Regarding schwab, sure"** authorizes widening ONE existing Opal principal's Schwab grant to add `dim_transaction`,
   through the grant admin tool.
   - It makes FWD-3's transaction half reachable, and r6.J1's transaction question can then be answered rather than
     refused.
   - It lifts ruling B2 for that one grant only. No new identity, no new principal, and no other grant change.
3. **"whatever needs to be lifted should be lifted"** lifts the hold he set on `platinum/advi`: "platinum/etfs YES,
   platinum/advi NOT YET", relayed at MX-t-11's supersession @a120fec68b and cited to `DATA_CATALOG.yaml:32` "WIDENING
   IS ANDREW-ONLY".
   - That hold kept the `advi` catalog row and tool, MX-t-12 (formerly MX-t-11), from being built.
   - It is now his widening word for `platinum/advi`, and MX-t-12 may proceed under its own order.
   - The MX-t-8 authority's advi limit (`platinum/advi/49financial/` only, because the firm scope is the key segment,
     C7) is unchanged.

## Routing

- To 2.0.0_SA_COO~MI (NFRA_MCPINDEX issuer): items 1-3.
- The R20 register entry goes in `infra/logic/06_CONFORMANCE_LEDGER.md` section 6, which is 4.0.0_SA_CRO's lane.
- The naming gate grades NEW literals before any waiver (`.tools/naming-gate.py:1413`, `:1444-1446`) and reads no R20
  entry. So this acknowledgement lands in the code only once the gate honours a register entry. That is gate owner laptop
  1.0.0_SA_CTO's (LGIC_ENFORCE) edit, and it is asked the same turn.

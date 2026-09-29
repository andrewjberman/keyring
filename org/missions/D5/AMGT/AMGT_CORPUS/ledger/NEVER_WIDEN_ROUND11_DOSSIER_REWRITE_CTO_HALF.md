# NEVER-WIDEN -- CTO HALF -- AMGT_CORPUS round 11, the dossier rewrite at `/4` -- `1.0.0_SA_CTO~Z`, 2026-09-29 ~08:4xZ

**Against:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND11_DOSSIER_REWRITE.md` @`bfa1821ac8` (msg 26513, READ-acked), code at
`b274848977`. Ruling it implements: `ROUND_ANALYSIS.round10.md` @`8b54c2b4fd` ruling 2.

## VERDICT: REFUSED AS IT STANDS -- one carve-out first (SHOP_CN), then re-sign

The COO half is right that my round-10 ruling, applied literally, moves SHOP_CN (`$` on a CAD listing) to CAD, and BZLFY_US
(`$` on a USD listing, newly read) to USD. **I refuse the SHOP_CN move, and I amend my own ruling.**

**Why, measured by this seat:**
- SHOP_CN's served Base: Price 2026E `127.70` with Return 2026E `-26.4%`, so the pack's own current price is 127.70 / 0.736 =
  **~173.5**. The served `PX_LAST` today is **206.0** (the listing's CAD, vintage 2026-09-29T02:47:03Z), and Shopify reports in USD.
  173.5 is consistent with EITHER reading, depending on how the price moved since the pack was written. **The payload cannot
  decide it.**
- The round-10 L9 (`ADJUDICATION_v13`) named exactly this as the hazard its ruling closed: "`$127.70` on SHOP_CN can no longer be read
  as CAD". Setting CAD re-opens it on an undecidable read.
- By contrast, a bare `$` on a USD listing (CPA, SPOT, UNVGY, BZLFY) is USD on every reading of the pack. For SPOT, 450.64 / 0.827 =
  ~545 against a USD `PX_LAST` of 511.38, the same order and direction as the pack's age implies.

**THE AMENDED RULE (it replaces round-10 ruling 2's scope):** a currency is set only where the symbol's ISO set, intersected with the
listing's currency, is exactly one, **AND the symbol is not a bare `$` on a non-USD dollar listing** (CAD, AUD, NZD, HKD, SGD, and any
other `$`-currency). There the currency stays `null` with its own reason: *"a bare `$` on a non-USD dollar listing: the pack may state
the reporting currency"*. A bare `$` on a USD listing sets USD. Every other symbol (e.g. `€` on EUR, `¥` on JPY) keeps the
intersection rule.

## WHAT RE-SIGNS THIS HALF
1. CRPS-m-1 amended with the carve-out (the issuer amends its own order; no further ruling is needed), with a criterion arm on
   SHOP_CN `null` with the new reason and a planted USD-listing `$` reading USD.
2. The COO half re-measured at the amended code: expected currency moves **4** (CPA, SPOT, UNVGY, BZLFY -> USD), served moves 6
   (positional), changed names **9 of 95** (BZLFY counted once), `currency_set 5` (not 6) in the after-state line 3.
3. This seat then re-runs the per-name expected-moves read itself, and signs on equality.

**Accepted now, so the re-sign reads only the delta:** the one-writer census; the blast radius (95 new objects, no delete, no
overwrite); the six positional moves (placed 6, ambiguous 0; blank 2030E as `null`, never arithmetic); the rollback (`METHOD_VERSION`
back to `/3`); the three stop limbs; and the reader note that RESAPP must render a `null` year as a blank cell.

Signed as REFUSED-PENDING-CARVE-OUT: `1.0.0_SA_CTO~Z`, 2026-09-29.

# NEVER-WIDEN -- CTO HALF -- AMGT_CORPUS round 10, the /3 dossier rewrite (chain A: the case unit carries its claim)

`1.0.0_SA_CTO~Z`, 2026-09-29 ~06:1xZ. **SIGNED.** Pairs with `2.0.0_SA_COO~X`'s half
`deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND10_DOSSIER_REWRITE.md` @`1323991818`. Authority: this seat's round-9 analysis ruling 1
(@`abfad1355c`).

## 1. MEASURED BY THIS SEAT, READ-ONLY, AT HEAD `c7e619aabb`

- `dossier --pick-census`: `dossier_pick names 95 current_method_available 0 stale_pick 0` -- every name takes branch 1, so 95
  puts are the expected count.
- `dossier --case-census`: `names 95 slots 285 body 84 heading_only 0 absent 201 sum 285 ordering_held 28 ordering_violated 0
  ordering_na 67 unit_carried 10 currency_set 1 currency_null 27` -- equal to the COO half's before-state line; the case VALUES
  do not move (body 84, as round 9).
- **The currency rule reads as ruled:** only ML_FP (`€` on a EUR listing) sets a currency; AZN_LN (`£` on a GBp listing)
  and SHOP_CN (`$` on a CAD listing) read null. 8035_JP and V_US read ABSENT on all three cases, as the six-table reason says.

## 2. THE RADIUS I SIGN

The COO half's act (95 puts under `research-dossier/`, no delete, no overwrite), its readers (AMGT_RESAPP's scoped API, waiting on
exactly `unit_as_written` / `currency` / `currency_basis`), its stop limbs, and its same-day rollback by reverting
`METHOD_VERSION` to `/2` (the round-9 CTO half read that fallback in `read_dossier`, `dossier.py:1038-1052`).

Signed: `1.0.0_SA_CTO~Z`, 2026-09-29.

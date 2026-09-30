# NEVER-WIDEN -- CTO HALF -- AMGT_CORPUS round 9, the dossier rewrite (`CRPS-k-1`'s served act)

`1.0.0_SA_CTO~Z`, 2026-09-29 ~02:0xZ. **SIGNED.** Pairs with `2.0.0_SA_COO~X`'s half
`deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND9_DOSSIER_REWRITE.md` @`b98e09953e`. Authority for the rule: this seat's
round-8 analysis s.2 ruling 1 (@`40ff643781`), the table-aware case rule.

## 1. WHAT I MEASURED, READ-ONLY, AT HEAD `53a1c3fd73` (code at the k-1 drain `19458b6130`)

- `dossier --pick-census`: `dossier_pick names 95 current_method_available 0 stale_pick 0` -- every name takes the COO
  half's branch 1 (stored method differs), so 95 puts are the expected count.
- `dossier --case-census`: `names 95 slots 285 body 84 heading_only 0 absent 201 sum 285 ordering_held 28
  ordering_violated 0 ordering_na 67 unit_carried 10` -- byte-equal to the COO half's after-state line 3. 84 = 28 readable
  tables x 3 cases; 34 tables less the 6 unreadable on the 3k count (served ABSENT with the reason, rows Z-W1-S11/S12).
- **The rollback is real without an S3 write:** `read_dossier` (`dossier.py:1038-1052`) picks among objects carrying the
  CURRENT `METHOD_VERSION` when any exists, else among all. Reverting the constant to `/1` therefore excludes the new
  `/2` objects and serves the pre-act `/1` objects, all still stored.

## 2. THE RADIUS I SIGN

The COO half's act (`dossier --write --workers 10`, 95 names, stored gold and extractions only, no vendor call), its
radius (95 new objects under `amgt/harvest/gold/research-dossier/`, no delete, no overwrite), its readers (the dossier's
`cases` has no downstream reader; the page reads the model block's cases), its three stop limbs and its same-day rollback.

## 3. BOUND, STATED

This half signs the WRITE. It does not grade whether each served case reads as the team's own case -- that is `k-1` AC3,
the round's judgment, graded by `3.0.0_SA_CVO~Z` at L9 on the served objects this act writes (names in more than one
currency, AZN's pound sign among them).

Signed: `1.0.0_SA_CTO~Z`, 2026-09-29.

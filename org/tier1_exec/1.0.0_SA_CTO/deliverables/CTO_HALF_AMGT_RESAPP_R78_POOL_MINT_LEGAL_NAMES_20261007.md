# CTO never-widen half -- AMGT_RESAPP round 78, issuer act 1: the pool mint that carries the legal names

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~17:2xZ. **Ask:** `2.0.0_SA_COO~Z` msg 31210.
**COO half:** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/NEVER_WIDEN_HALF_COO_POOL_MINT_LEGAL_NAMES.md`
@f147438d17 (SIGNED), read whole.

## VERDICT: SIGNED. The condition is ruled: the AMGT_CORPUS task is pinned to a commit that holds bb-7 before its next fire. "Best-effort" is not accepted.

## What this seat read at signing

| read | result |
|---|---|
| the served pool, `s3api list-object-versions` on `opal-data-harvest`, `crosswalk/v1/2026-10-07.json` | 2 versions. Latest `Y6Tisihmmlm1lCHOO61ci9b726FLXBAI`, 748,500 B, 13:22:15Z; one older, 745,570 B, 13:15:52Z. Equal to the COO half's base. |
| does AMGT_CORPUS's CURRENT pin hold bb-7 (`git merge-base --is-ancestor 5b498e903a 662cd2b11d`) | NO |
| does AMGT_CORPUS's NEW pin hold bb-7 (`... 057e716da8`), the pin this seat signed at 16:3xZ | **NO.** `057e716da8` was authored 11:37 local and bb-7 merged at 12:28 local. Control: HEAD holds bb-7. |

Not read by this seat: the dry run, `r78_bb7.py`, the in-memory measurement of the older code dropping the names.

## The ruling on the condition

The COO half measured that a mint from code older than bb-7 writes 243 records with 0 names, exits 0, and passes the old schema.
That is a silent revert of a served field. Both of AMGT_CORPUS's pins are older than bb-7, including the one signed today for
tomorrow's 13:00Z fire. So:

1. **`2.0.0_SA_COO~X` re-pins to a commit that holds BOTH `057e716da8` and `5b498e903a`,** with `model_block_pull.py` and
   `field_map.json` equal to `057e716da8`'s. Its own half already allows "a descendant whose two files equal it".
2. This widens that pin's closure again (`crosswalk.py` and `add_security.py` at bb-7). Condition C1 of
   `ledger/NEVER_WIDEN_ROUND40_AP10M_CTO_HALF.md` (the 96 keys equal, key by key) is run on the new pin and covers it. That half
   is amended by an addendum of this date.
3. **After the 2026-10-08 13:00Z fire, whoever reads it also runs `r78_bb7.py --crit AC1`:** 211 of 243 served records carry a
   name, or the count that the day's registrations explain.
   - (a) the count holds: nothing more.
   - (b) it reads 0 or falls: an older writer ran. `2.0.0_SA_COO~Z` re-mints from HEAD the same hour and names the writer.

## Both branches of the mint itself

Accepted as the COO half states them (A, B, C), with the rollback by copy of VersionId `Y6Tisihm...`; no delete.

## Not covered

- A laptop-side run on an older checkout: the same hazard, outside this fabric. `0.0.0_AB_MSTR~Z` is asked to tell the laptop
  that any pool write from a checkout older than `5b498e903a` drops the names.
- bb-18, which is what makes name search read the names. The 32 folder-only records.

-- 1.0.0_SA_CTO~Z

# ADVI_COTBKF decomposition -- ROUND 15 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-07 ~16:2xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-14 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_14_20261007.md` @47ea1968e7 (msg 859): E1, the
near-match page regenerated from the served crosswalk (row D2-S25: 21 -> 22 at the re-apply). After it, the lane waits on MDPF_SECHIST's
price load or the C-RESTRICTED apply.

**Rule 24.** Domain: E1. One cell.

## Measured constraints

1. The served crosswalk (re-applied @ad6d5be150, crosswalk.parquet VersionId wv5z6zeRnWQrPGfO3UcmrxlIaz3ozzLZ) carries per account its
   `score` and `candidates`; the near-match band is `[NEAR_MIN, MIN_SHARE)` = [0.65, 0.80) (`commonwealth_crosswalk.py:70,79`).
2. The per-position detail of a near match is computed during a crosswalk run (`write_near_matches`, `:627-637`), not stored in the table.
3. The page put toward Andrew (`deliverables/0.9.0_WK_ADVI_COTBKF~14/near_matches.{csv,md}`, round 4) lists 21.

## The cell

| cell | what | serves | risk | slot |
|---|---|---|---|---|
| `CB-o-1` | the near-match page regenerated: the list read from the SERVED crosswalk's near-match band (count + VersionId printed), each entry's position detail from the crosswalk's own generator over a local run on the same inputs, the two counts required equal; the entry that newly joined, with its score change, named | FWD-8 (D2-S25) | LOCAL | `0.9.0_WK_ADVI_COTBKF~31` |

**Write set:** `data/assets/scripts/analysis/commonwealth_near_match_page.py` (new) + its test; the deliverables folder; the channel.
**Fan-out:** `1 of 1 chains, cap 8`.

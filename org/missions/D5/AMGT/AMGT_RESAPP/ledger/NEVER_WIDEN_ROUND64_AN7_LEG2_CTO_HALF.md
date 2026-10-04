# AMGT_RESAPP round 64 -- `AMGT-an-7` LEG 2 never-widen pair, CTO half (trending-price `?days`, build 43711514cc)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-03 ~01:4xZ.
**COO half:** `deliverables/2.0.0_SA_COO~Z/round64/NEVER_WIDEN_HALF_COO_AN7_LEG2.md` @e25430f320 (msg 28862).
**Executor:** `0.7.0_AE_CloudOps~A`, under the an-7 order section 7 (AMENDMENT 2).

## What I read

- **The act:** one upload plus one code-only `safe-apply` at 43711514cc (or a descendant with an equal content diff). Memory stays
  1769. It begins only after leg 1's V1 closes.
- **The base and rollback:** CodeSha256 `kSeyeO0v...` (leg 1, LastModified 00:16:16Z, recorded in the leg-1 NEVER-2 entry) and
  VersionId `40smkxDeOsBar9woKz_p5ICvkoUonv9y`.
- **The repair** (`scoped_amgt.py:5317`, read at HEAD): the price-window branch now matches `breakout` OR `trending`. `?days=30`
  (DEFAULT_DAYS) falls through to `read_rankings` unchanged. Any other valid value returns `price_window_not_produced` (0 rows and a
  reason). A bad value answers 400. That is the producer's own rule, read in code, and it is the qualified wait PRD v0.35 places on
  price 90/365. `test_rolling_windows.py`, run by this seat at HEAD, gives 11 passed.
- **CONTENT-DIFF 355 / 352 identical / 3 changed / 0 added / 0 removed:**
  - `scoped_amgt.py`: the one-word widening above.
  - `publication_gold.py`: HARVST al-2 (`GOLD_MENTION_SCHEMA`, `_latest_articles_for_keys`, `build_mention`'s keyword). The routes reach
    `publication_gold` only through `_day_of` and `_latest_gold_snapshot_rows_cached` (`scoped_amgt.py:4264-5202`, read). Neither
    function changed.
  - `finbert_sentiment.py`: HARVST al-2 and am-1. It is reached only lazily inside `build_mention`, a producer that no route calls.
  - The other harvest files that changed between 9eb6c885eb and 43711514cc (`window_tone.py`, `lib/opal_data_harvest/*`) are not in the
    355-file package. That is consistent with leg 1's list, where they never appeared.
- **Drift:** HEAD equals 43711514cc on all four files (`git diff --stat` is empty).
- **Writers of the served property** (trending/price under `?days`): 1, this function.

## Both branches

| check | if the act holds | if it does not |
|---|---|---|
| c10 | YES on both movements: trending and breakout 90/365 give 0 rows with "not produced yet"; 30 gives today's rows | ROLLBACK |
| c9, c11-c14; r63 c3/c4/c5/c7/c8 | unchanged YES | any move means ROLLBACK |
| covered keys' overlay, thesis, peers, timeline, collected/chatter | 200 | a non-200 means ROLLBACK |

## Conditions

1. **Leg 1's V1 is closed first**, including the import-graph proof my leg-1 half required (no route module reaches
   `finbert_sentiment`). Leg 2 ships the same file again, so that proof carries over.
2. **The build-time content diff equals the three files above,** or STOP. The live base is re-read before the build, and a moved base
   is a STOP.
3. **Post-act reads on the DEPLOYED function:** CodeSha256 off `kSeyeO0v...`, memory 1769, and c10 printed for both rankings with the
   row counts at 30/90/365.
4. **NEVER-2:** one entry, opened before the upload and closed after the reads.
5. **After this act, DSGN round 30's FWD-26 price presets read a served window,** so COO~D can stop treating `?days` as ignored.

**CTO HALF: SIGNED** for an-7 leg 2: one upload plus one code-only `safe-apply` at 43711514cc (or a descendant with an equal content
diff), memory unchanged at 1769, with the VersionId `40smkxDe...` rollback.

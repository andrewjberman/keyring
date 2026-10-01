# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 25, `HVST-o-4` (the sa silver `article` rebuild) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~05:0xZ

**Against:** `deliverables/2.0.0_SA_COO_H/round25/NEVER_WIDEN_HALF_COO_O4.md` @`7776cd3492` (msg 26918, READ-acked; read to EOF,
4,761 B).
**Rulings it serves:** round-24 ruling 3 (the tie-break, then the paired rebuild) and the round-24 analysis FWD-2 row.

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT

- **Prefixes from the builder:** `seeking-alpha/harvest/silver/article/` and `seeking-alpha/harvest/bronze/article/`.
- **Counts by `aws s3 ls --recursive | wc -l`:** silver parts **35**, bronze article objects **52**. Both equal the COO half's
  before-state.
- **The DEPLOYED reader, not just the merged one.** The COO half cites `_TIMELINE_SILVER_COLUMNS`, which arrives with `n-6` and is
  not yet deployed. This seat read the deployed build's source instead:
  - `opal-amgt-scoped-api` `pVa+sgzj` is built from `50cc86edd6`.
  - Its `_timeline_article_loader` (`scoped_amgt.py:4237-4258` at `50cc86edd6`) takes ONLY `title` and `published_precision` from
    each silver article.
  - The 5 MOVED rows differ only in `links`, `type` and `meta`. So **no deployed response can move**, under the old reader or
    the new one.
  - The 6 NEW keys are in no served mention snapshot.

## 2. CONDITIONS

1. **Sequencing against `o-5`.** `o-4` does not start until `o-5`'s run 2 and its AC1/AC2 are recorded, because `o-5`'s pair
   holds the sa root as a no-write control. An `o-4` write before that record voids `o-5`'s control. The COO half says the same.
2. **Code at the act.** `git diff --stat 3886894d16 HEAD -- lib/opal_data_harvest/silver_from_bronze.py
   lib/research/harvest/store.py` is printed before the act. Any change to `article_rows`, `silver_append` or `supersedes` is a
   STOP and a re-sign.
3. **The act-start gate** (`o-4.signing.py` without `--signing`) reads equal to the signing snapshot, or STOP.
4. **After the act:** `o-4.AC1.py` and `o-4.AC2.py` pass. That means exactly 11 rows in 3 new parts; served keys 46 -> 52; the
   41 others unchanged; a re-run writes 0.
5. **The `retrieval_mode` ASSUMED `backfill` on the 6 NEW rows** is carried as a labelled assumption on those rows (the `n-2`
   rule). It is never promoted to measured.

## 3. ROLLBACK

The COO half stands: forward only. Deleting a part is Andrew's act. The exposure is 11 silver rows in one table, read by no served
response until a mention rebuild, which is its own pair.

## 4. NOT COVERED

- any other table or source;
- any bronze write;
- any mention or gold rebuild;
- a second run.

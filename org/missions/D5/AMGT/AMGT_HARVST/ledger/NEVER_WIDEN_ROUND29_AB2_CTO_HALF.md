# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 29, `HVST-ab-2` (the `article_security_mention` rebuild for the 11 bbg story ids) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~13:1xZ

**Against:** `deliverables/2.0.0_SA_COO_H/round29/NEVER_WIDEN_HALF_COO_AB2.md` @`9548acfffb` (msg 27164, READ-acked; read to EOF,
5,699 B).
**Ruling it serves:** `ROUND_ANALYSIS.round28.md` ruling 2 @`c907537920`.

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT

- **Before-state on S3:** `article_security_mention` has 7 parts. The newest is `part-20260930T062354Z`, with 358 rows and
  `mention_count` null on 0. This equals the COO half.
- **The predecessor-code diff, by an independent closure:**
  - an AST walk from `publication_gold.py` (absolute and relative imports) reaches 7 files;
  - `01e5499ae7..HEAD` changed **2** of them: `publication_gold.py` and `lib/research/identity/crosswalk.py`.
  - The COO half's three-file diff names only the first.
  - `crosswalk.py`'s change is ONE added comment line (z-4's slash-safe marker), with no code, so the builder's behaviour is
    unchanged.
  - `publication_gold.py`'s change is `q-5` (the daily schema column), and the mention path is untouched. **The half's claim that
    only the silver input moved holds.**
- **The serializing dry run is the right instrument** (the aa-3 lesson): the real `write_gold` against a capturing client, 1 put,
  379 rows, 44,376 B, reproduced twice.
- **The page window is stated rather than predicted** (`Z-S46`): 2 in-window pairs reach `/timeline/day`, and the 9 pre-floor pairs
  are kept in gold and reach no page. Accepted.

## 2. CONDITIONS

1. **The act-start gate** (`ab-2.signing.py` without `--signing`) reads equal on the parts, the rows and the bytes, and
   `git diff --name-only 9548acfffb HEAD` over the 7-file closure is empty, or STOP.
2. **After the act:** `ab-2.AC1.py` and `ab-2.AC2.py` pass.
   - 379 rows: 358 kept byte-identical, 21 new on the 11 story ids;
   - 0 pairs on the 11 empty hash-keyed rows;
   - the 2 in-window pairs are listed on `/timeline/day` (992_HK 2026-08-13 and 2026-09-01), and the 9 are named.
3. **No overlap** with any other round-29 WORLD act: `ab-3`'s backfill batch runs after this act's after-reads pass.

## 3. ROLLBACK

The COO half stands: forward only; the prior 7 parts stay. A delete is Andrew's act.

## 4. NOT COVERED

- `chatter_daily`, which is not rebuilt, so the `/timeline` series does not move;
- the 9 pre-floor pairs' removal;
- any collection.

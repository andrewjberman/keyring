# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 26, `HVST-p-1` (the `article_security_mention` gold rebuild) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~06:2xZ

**Against:** `deliverables/2.0.0_SA_COO_H/round26/NEVER_WIDEN_HALF_COO_P1.md` @`5b407d86a1` (msg 26953, READ-acked; read to EOF,
4,150 B).

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT, including the READ path (the round-25 analysis ruling 1 and the `zz-8` post-act lesson)

- **The writes:** the COO half names the command that reaches the put (`build-mention` -> `build_mention` -> `write_gold`, ONE
  `put_object` with `IfNoneMatch`), the module-constant defaults, and a stub dry run that captured exactly 1 put. **This half
  accepts those three as the write-path trace.**
- **Before-state:** `aws s3 ls amgt/harvest/gold/article_security_mention/ --recursive` reads **6 parts**, the newest
  `date=2026-09-29/part-20260929T192610Z.parquet`. That equals the COO half.
- **The READ path of the claimed user-visible outcome, traced by this seat.**
  - The deployed `opal-amgt-scoped-api` is `zHpr7FhS...` (05:20:04Z, `zz-8`, built at `0bf907bee8`).
  - Its `/timeline/day` takes the day's articles from `_timeline_snapshot_rows("article_security_mention")` (`scoped_amgt.py:4330`).
    That calls `_latest_gold_snapshot_rows_cached`.
  - At `0bf907bee8`, that function LISTS the table on every call, picks the newest by (date partition, key), and reuses its
    decoded rows only when that newest key/ETag/size is unchanged. **So the new part is served on the first call after the
    write, even in a warm container.**
  - The new part's partition is the act's as-of date (2026-09-30), which sorts newest.
  - **The 54 NEW pairs are therefore user-visible on `/timeline/day`, as the COO half states, and the 304 KEPT pairs are
    byte-identical.**

## 2. CONDITIONS

1. **The act-start gate** (`p-1.signing.py` without `--signing`) reads equal to the signing snapshot and the expected rows, or
   STOP.
2. **After the act:** `p-1.AC1.py` / `p-1.AC2.py` pass. That means 358 rows; 304 KEPT byte-identical; 54 NEW (sa 6, wsj 48);
   0 CHANGED or GONE; `mention_count` never null.
3. **One post-act read of the served route**, not only the store: `/timeline/day` for Lenovo on one day of a NEW wsj pair shows
   that article with its count.
4. **`Z-S44` (o-5's 11 bbg silver rows are EMPTY: title `''`, 0 text blocks) is a REPAIR cell before FWD-3 grades.** 11 articles
   uploaded with no content is a possible silent loss on the upload path, the same class as the never-stored fetch. It is not
   accepted as a limit.

## 3. ROLLBACK

The COO half stands: forward only. The prior 6 parts stay. Deleting the new part is Andrew's act.

## 4. NOT COVERED

- `chatter_daily`, `chatter_event` or any other gold table;
- silver;
- a second rebuild.

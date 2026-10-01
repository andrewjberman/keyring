# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 26, `HVST-p-3(a)` (the `chatter_daily` gold rebuild, no egress) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~07:3xZ

**Against:** `deliverables/2.0.0_SA_COO_H/round26/NEVER_WIDEN_HALF_COO_P3.md` @`e7eb9100ea` (msg 27008, READ-acked; read to EOF,
4,236 B).
**Ruling it serves:** `ledger/CTO_RULING_ROUND26_P3_SPLIT_AND_FWD7_DENOMINATOR_20260930.md` @06804f9f99 (the split: (a) now, (b) after).

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT

- **Write path:** the COO half names `build-daily --as-of 2026-09-30` (pinned) -> 1 put, and its stub dry run reproduced the
  digest. Accepted as the write-path trace.
- **Before-state:** `aws s3 ls amgt/harvest/gold/chatter_daily/ --recursive` reads **8 parts**, which equals the COO half.
- **The READ path of the user-visible claim:**
  - The deployed `zHpr7FhS` (built at `0bf907bee8`) serves `/timeline`'s series through `_timeline_snapshot_rows("chatter_daily")`
    -> `publication_gold._latest_gold_snapshot_rows_cached` (`scoped_amgt.py:4292-4299`).
  - That function lists the table on every call and serves the newest part (verified at the `p-1` half).
  - **So Lenovo's days read PARTIAL with their publisher codes on the first call after the write, and the 43 article-count rows
    move.** That is honest: DENIED said "not searched", and PARTIAL says "searched by 2 of 5".
- **No rank moves:** `CHATTER_AXIS_SOURCE=legacy`, and the gold branch HOLDs at 0 of 191 by its current rule. The FWD-7 ruling
  (@ddcc71fd2d) changes that rule only in round 27, under its own cells.

## 2. CONDITIONS

1. **The act-start gate** reads equal to the signing snapshot (8 part ETags and the expected digest), or STOP.
2. **After the act:** `p-3.AC1.py` / `p-3.AC2.py` pass. That means:
   - 52,143 rows with the signed sha256;
   - NEW 191, GONE 0;
   - `data_status` changes on exactly 271 Lenovo rows (DENIED -> PARTIAL);
   - 43 `articles_total` changes;
   - every other row byte-equal apart from the recomputed window fields the COO half names.
3. **One post-act read of the served route:** `/timeline` for 992_HK_Equity shows a day's status as PARTIAL with its publisher codes.
4. **Dependency order (CORPUS round-22 ruling 1):** (a) finishes, with its ACs recorded, before (b)'s collection run starts, because
   (b)'s coverage marks rebuild over (a)'s output.

## 3. ROLLBACK

The COO half stands: forward only, readers take the newest part, and the prior 8 parts stay. A delete is Andrew's act.

## 4. NOT COVERED

- (b), the vendor run, which is its own pair;
- any other gold table;
- the `gold` flip;
- any change to `chatter_axis`.

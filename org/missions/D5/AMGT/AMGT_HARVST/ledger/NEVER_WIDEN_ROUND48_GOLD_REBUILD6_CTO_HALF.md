# AMGT_HARVST round 48 au-3 -- served gold rebuild #6 (the stored `url` joins the gold mention rows) -- never-widen pair, CTO half

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-06 ~05:3xZ. **COO half:** `deliverables/2.0.0_SA_COO_H/round48/NEVER_WIDEN_HALF_COO_GOLD_REBUILD6.md`
@e512987397 (73 lines, read in full; msg 29912). **Why:** round-47 analysis @acc5c6e750 item 3, on `2.0.0_SA_COO~Z`'s ask (msg 29872).

## The two new classes, ruled

- **(c) HASH-ONLY: accepted.** On 5,363 mention rows, `record_hash` is the only changed field, and the built value equals the CURRENT
  stored silver row's hash.
  - Silver was re-written by round 45's ar-1 and round 47's at-4, and every content field is equal.
  - A provenance hash that follows its source is correct, not a widening.
  - Gold is read as the newest whole part, never merged across parts, so no reader double-counts a row on its hash.
- **(d) PAST-DAY COVERAGE-ONLY: accepted.** 558 daily rows change only `data_status` / `publishers_covered` /
  `publishers_covered_codes`. Each grows or holds, and no mention is gained.
  - It is the collection backfill's real coverage of past days, the same kind as round-9 ruling 3's data arrival in ETFS_RIVALS.
  - Bound 1 (the as-of day only) is lifted for this class alone. Bounds 2-4 hold, re-checked on the written part.
- **ft 30 of 930 and wsj 34 of 880 rows carry a url.** Each is the url ALREADY STORED in silver, and **no ft.com or wsj.com host is
  fetched**. Serving a stored link does not attempt the FT route, so Andrew's hold ("Dont attempt FT until I return") stands as is.

## Conditions

1. **The rule as the COO half writes it,** enforced twice: a fresh dry run before the write (STOP on any OTHER, any GONE, any
   unexplained change), and the VERIFY on the written parts.
2. **Exactly 2 new parts,** under the never-overwrite conditional put with read-back. No delete, no other table, no bronze or silver
   write.
3. **ONE act within 24 h of this signing.** A second rebuild is a new dry run and a new pair.
4. **One NEVER-2 entry,** opened at start and closed with the act record (`au-3.act_<stamp>.json`).
5. **After the write,** `2.0.0_SA_COO~Z` is told the build stamp. RESAPP FWD-4's links are graded on its next walk from the served
   `url`.

**CTO HALF: SIGNED** for gold rebuild #6 under conditions 1-5.

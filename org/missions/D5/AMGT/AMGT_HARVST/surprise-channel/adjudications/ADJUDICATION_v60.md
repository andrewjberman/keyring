# AMGT_HARVST ROUND 48 -- L8 COMPILE + L9 -- the upload-timeout and soft-block fixes PASS; gold rebuild #6 PASS, url on every mention row that has a stored link; the collection outcomes stay a qualified wait; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-06 ~06:4xZ
**Input:** `2.0.0_SA_COO~H` `round48/ROUND48_DRAIN_END_PACKET.md` @`a5f52a22b4` (34 lines, read to EOF), msg 29931.

## Grades

| cell | read by this seat | grade |
|---|---|---|
| au-1 upload timeout | plant tests in `test_au1_upload_timeout.py`: pass (9 of 9 with au-2) | **PASS** |
| au-2 soft block | plant tests in `test_au2_soft_block.py`: pass; the issuer's mutant fails | **PASS** |
| au-3 gold rebuild #6 | mention `part-20261006T060121Z`: **33,665 rows**, as the packet says; url non-null on **31,919**: barrons 712/712, bbg 5,102/5,102, sa 26,041/26,041, ft 30/930, wsj 34/880. The 1,746 ft/wsj rows without a url are articles with no stored link; the order was stored links only, with no host fetched. Classes (c) and (d) were accepted by the pair, bounded, before the write | **PASS** against its signed rule |
| collection outcomes | every leg stopped (sa 9, barrons 130, bbg 104, wsj 154, ft 0 of 191); declared set EMPTY | **NOT REALIZED**: a qualified wait on Andrew's hand-solve and the SA account (CTO @`69ce080222`) |

**For RESAPP's FWD-4** ("an item followed out to its original"): from stored links alone, most ft and wsj items cannot be followed out (30 of 930, 34 of 880). Giving those items a link would be a new source, not a repair of this rebuild.

## Rows

`Z-W96-S1`, `Z-W96-S2` and `Z-W97-S1` are INERT, repaired by the issuer at the landing @`093da8e2b8`.

## L10 PRECONDITION

Every cell is terminal, and au-3's NEVER-2 entry is closed. `comp-surprise --armed AMGT_HARVST`: ARMED 0. **MET.**

```json
[
 {
  "id": "AMGT_HARVST-Z-C-S80",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-06T06:41:00Z",
  "one_line": "Round 48 L8/L9: au-1 and au-2 PASS (9 of 9 plant tests on this seat's run); au-3 gold rebuild #6 PASS against its signed rule -- this seat read mention part-20261006T060121Z: 33,665 rows, url on 31,919 (barrons 712/712, bbg 5,102/5,102, sa 26,041/26,041, ft 30/930, wsj 34/880), the 1,746 ft/wsj rows without a url are articles with no stored link (stored links only, nothing fetched); collection outcomes still a qualified wait on Andrew (Z-S89).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "pytest lib/opal_data_harvest/test_au1_upload_timeout.py test_au2_soft_block.py: 9 passed (2026-10-06, run by 3.0.0_SA_CVO~Z)",
    "S3 opal-data-harvest amgt/harvest/gold/article_security_mention/date=2026-10-06/part-20261006T060121Z.parquet: 33,665 rows; url non-null 31,919; by publisher barrons 712, bbg 5,102, sa 26,041, ft 30 of 930, wsj 34 of 880"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A compile record: the round's cells are graded here; the ft/wsj link coverage (30 of 930, 34 of 880) is what the stored-link rule yields, and RESAPP's FWD-4 is graded on the served feed.",
  "spec_asserts": "Gold carries each article's original link where the store holds one, and nothing is fetched to make one.",
  "world_is": "Every barrons, bbg and sa mention row carries its url; most ft and wsj rows have no stored link to carry.",
  "notes": "For RESAPP FWD-4 ('an item followed out to its original'): ft and wsj items mostly cannot be followed out from stored links alone -- a link source for them would be a new cell, not a fix to this one."
 }
]
```

-- 3.0.0_SA_CVO~Z

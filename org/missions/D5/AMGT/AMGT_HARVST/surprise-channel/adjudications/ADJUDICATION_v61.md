# AMGT_HARVST ROUND 49 -- L8 COMPILE + L9 -- every served mention row now carries its original's link (33,665 of 33,665, all on the publisher's own host); av-1 and av-2 PASS; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-06 ~09:0xZ
**Input:** `2.0.0_SA_COO~H` `round49/ROUND49_DRAIN_END_PACKET.md` @`b3354b90b6` (40 lines, read to EOF), msg 29980.

## Grades

| cell | read by this seat | grade |
|---|---|---|
| av-1 stored canonical url | `test_av1_stored_canonical_url.py`: 6 passed. The rule takes the top-level url, else the stored og:url, else wsj sourceUrl, accepted only on the publisher's own host; nothing constructed, nothing fetched | **PASS** |
| av-2 gold rebuild #7 | mention `part-20261006T082836Z`: **33,665 rows, url on 33,665**. A host check of every url against its publisher (ft.com, wsj.com, barrons.com, bloomberg.com, seekingalpha.com) finds **0 foreign or empty**. ft urls are in the canonical `https://www.ft.com/content/<uuid>` form | **PASS** against its signed rule |

**The byte-equality proof** the ruling named could not run: the stored-url articles and the og:url articles are disjoint. The substitute is sound. og:url is the publisher's own canonical form (this seat's host check agrees), and wsj og:url equals sourceUrl on 448 of 448.

**FWD-4 (RESAPP):** the link to the original is now on every gold mention row. Following one out on the served feed is RESAPP's grade.

**Collection outcomes:** still NOT REALIZED, a qualified wait on Andrew (Z-S89).

## L10 PRECONDITION

Both cells are terminal, and av-2's NEVER-2 entry is closed. No rows this round. **MET.**

```json
[
 {
  "id": "AMGT_HARVST-Z-C-S81",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-06T09:05:00Z",
  "one_line": "Round 49 L8/L9: av-1 PASS (6 of 6 plant tests on this seat's run; ft/wsj links come only from stored fields on the publisher's own host); av-2 gold rebuild #7 PASS against its signed rule -- this seat read mention part-20261006T082836Z: 33,665 rows, url on 33,665, every url on its publisher's own host (0 foreign or empty), ft in the canonical https://www.ft.com/content/<uuid> form; the substitute for the byte-equality proof (disjoint sets) is sound; collection outcomes still a qualified wait.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "pytest lib/research/harvest/test_av1_stored_canonical_url.py: 6 passed (2026-10-06, run by 3.0.0_SA_CVO~Z)",
    "S3 opal-data-harvest amgt/harvest/gold/article_security_mention/date=2026-10-06/part-20261006T082836Z.parquet: 33,665 rows, url non-null 33,665; host check against ft.com, wsj.com, barrons.com, bloomberg.com, seekingalpha.com: 0 foreign or empty"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A compile record: the round's two cells are graded here on the served gold and this seat's test run.",
  "spec_asserts": "Every served mention row carries the link to its original, from stored fields only.",
  "world_is": "33,665 of 33,665 rows carry a publisher-host url.",
  "notes": "RESAPP's FWD-4 ('an item followed out to its original') now has its link on every gold row; its grade is RESAPP's, on the served feed."
 }
]
```

-- 3.0.0_SA_CVO~Z

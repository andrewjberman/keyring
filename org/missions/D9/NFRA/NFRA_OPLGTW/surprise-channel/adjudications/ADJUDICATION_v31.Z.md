# NFRA_OPLGTW -- round 37 AC3 of OG-ap-19 graded on its replaced bodies (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v31. Fabric: site-z. Recorded: 2026-10-16 ~11:2xZ.
**Input:** `2.0.0_SA_COO~O` msg 34952 (acked). `deliverables/0.7.0_AE_CloudOps~Z/ANSWER_BODIES.json` @a6bc74441f, the ap-19 entries
read whole: `14440c020e` replaced the cap body (A1), and `a6bc74441f` replaced the quiet-day body (A2). The criterion is read
as amended by A3. The scrub caution of v30 stands, and none of the markers below is touched by it.

**NFRA_OPLGTW.TO-OG-ap-19 AC3: MET.**
- **Freshness in trading days:**
  - `portal_get_pipeline_freshness` gives per-source `trading_days_behind_t1`, `stale` and `frozen`:
    attribution and peer at 11 (frozen), data and model pkl at 1, cma at 0. The summary denominator is
    `trading_days_behind_t1: 11`.
  - `news_search_articles` carries `freshness.trading_days_behind_t1: 0`.
- **An empty window with its as-of (A3):** `news_search_articles` over the one-day window 2020-01-02 returns:
  - `items_matched 0`, `returned 0`, `articles []`, `per_day_counts {2020-01-02: 0}`;
  - `as_of 2026-10-16` and `absent_reason "no article matched the window and filters"`;
  - a separate `freshness` block (newest 2026-10-16, 0 behind).

  An analyst sees an empty window that is stated as empty, with a date, beside proof that the feed itself is current.
- **The 14-day cap stated:** a 45-day ask is refused in the tool's own words: "the window is 45 calendar days;
  news_search_articles caps it at 14" (`harvest_bad_argument`, `guard_denied`).

**Observation, not grounds:** 2020-01-02 is very likely before the news store's first day. The same `absent_reason` would
read for a genuinely quiet day and for a day before coverage, and nothing in the answer tells those apart. A coverage
floor beside the empty answer would close it. That is an enrichment, not a failure of A3's marker.

## Rows

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S78",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T11:25Z",
    "one_line": "Round 37: NFRA_OPLGTW.TO-OG-ap-19 AC3 MET on its replaced bodies -- freshness in trading days per source, an empty news window stated as empty with as_of and absent_reason beside a current freshness block, and the 14-day cap named in the tool's own refusal; enrichment: the empty answer cannot tell a quiet day from a day before coverage.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-OG-ap-19 AC3 (:87) as amended by A3: the first portal and news answers read as an analyst would want (freshness in trading days, an empty window with its as-of on a quiet day, the 14-day news cap stated). Graded on a real call.",
    "world_is": "ANSWER_BODIES.json @a6bc74441f ap-19: pipeline_freshness per-source trading_days_behind_t1 and stale/frozen; news_search_articles 2020-01-02 items_matched 0, as_of 2026-10-16, absent_reason 'no article matched the window and filters', freshness newest 2026-10-16 behind 0; news_search_articles 2026-09-01..10-15 refused 'the window is 45 calendar days; news_search_articles caps it at 14'.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-C-S77"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.7.0_AE_CloudOps~Z/ANSWER_BODIES.json @a6bc74441f, the ap-19 entries read whole",
        "task-orders NFRA_OPLGTW.TO-OG-ap-19 A3 (read at the order bytes in v30)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade: TO-OG-ap-19 AC3 MET. Closes the ap-19 hold of Z-C-S77. Enrichment carried: a coverage floor beside an empty news answer."
  }
]
```

-- 3.0.0_SA_CVO~Z

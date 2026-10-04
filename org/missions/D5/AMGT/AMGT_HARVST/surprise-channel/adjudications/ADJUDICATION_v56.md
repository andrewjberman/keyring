# AMGT_HARVST ROUND 44 -- L8 COMPILE + L9 -- FWD-5 PASS on judgment (REALIZED candidate); FWD-2, FWD-7 and FWD-12(c) FAIL confirmed; aq-4's reading of sa:3793704 carries; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-04 ~20:0xZ, after the site-Z relaunch
**Input:** `2.0.0_SA_COO~H`'s `round44/ROUND44_DRAIN_END_PACKET.md` @`76d0723778` (45 lines, read to EOF), msg 29195. The reads are
@`02217a491f`. There were four READ cells under decomposition section 57 (issued @`834ac9f9c8`) and no task-order files. No repair
was cut, and nothing was written.

## L9 grades

| cell | FWD | grade | basis |
|---|---|---|---|
| `HVST-aq-2` | FWD-5 | **PASS (judgment)** | below |
| `HVST-aq-1` | FWD-2 | **FAIL, confirmed** | Four of the five publishers lose named fields (barrons, bbg, ft, wsj), and 3 of the 50 sampled wsj originals have no silver row. A FAIL on a sample needs no population. |
| `HVST-aq-3` | FWD-7 | **FAIL, confirmed** | This seat read the APPLIED value: `amgt-resapp-chatter-axis` `CHATTER_AXIS_SOURCE` = `legacy`. The served rank is not "computed from the graded daily table". |
| `HVST-aq-4` | FWD-12 | **FAIL on (c), confirmed** | `lib/opal_data_harvest/config.json:26` reads `"sa": 25` at HEAD. The worker path passes it in place of the code default of 200, and storage agrees (maximum `search_page` 25 over 23,364 hits). (a), (b) and (d) PASS as the cell reads them. |

### FWD-5 (judgment): "clicking any day shows the articles behind that day, strongest first"

- **The order is right on names the cell did not read.** This seat invoked the served day route on AAPL, MSFT and TSLA, on the
  three busiest days of each (9 days; the probe is in this seat's session scratch). Every day returned status 200, the listed count
  equalled the series `articles_total`, and there were 0 order violations against (tier, mention count DESC, published ASC).
  Together with the cell's 6 days on BA and NVDA, that is 15 days on 5 names.
- **The page keeps the served order.** On portal `origin/PROD` @`dbd29c63`, `TimelinePanel.tsx` opens `DayDissection` on a day
  click (:264, :318, :668). It renders `day.articles.map` (:499) with no client sort, and each row shows its tier and mention count
  (:424-426).
- **"Strongest" = tier first, then mentions.** That is the right reading. Tier A means the company is the subject; B to D are
  progressively more passing. FWD-7 gives the project's own meaning of strength, "how strongly they were written about, not how many
  times they were named". An order led by mention count would put a passing list-article above a subject article, which is the
  failure FWD-7 names.
- **Not read:** a rendered walk of the page. The route, the PROD component and the served order together carry the grade at this
  class.
- **An observation, not part of FWD-5:** MSFT's three busiest days carry no tier-A article (`CDDD`, `BBCC`, `BCCD`). The busiest days
  for a mega-cap are list and ratings articles. That is FWD-6/FWD-7 territory and is left to the round-44 analysis.

**FWD-5: PASS. A REALIZED candidate for the CTO's board.**

## The contradiction (packet section 2)

**aq-4's reading carries.** FWD-12's class is "the stored article is not the listed item" (DONE WHEN (a)). aq-1's note shows that
`sa:3793704` is about Regeneron and dated 2022. That speaks to relevance and to the store's start date, not to whether the AMD listing
named that item. aq-4 (d) answers the listed-item question directly: the round-32 classifier ran over all 11,210 rows and found 0
mismatches outside the quarantine. The pre-2026 date is `Z-S82`'s question (STORE_START), which is open with `2.0.0_SA_COO~H` for the
CTO's scope call.

## L10 PRECONDITION

- Every cell of the round is reported done; there are no task-order files.
- `python .tools/comp-surprise.py --armed --project AMGT_HARVST`: ARMED 0, defects 0, malformed 0 (293 items, 153 remediation rows).
- 0 BLOCKING rows are undispositioned. `Z-S82` is an INERT OBSERVATION and stays UNDER_INVESTIGATION with its owner.

**MET.**

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S76",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-04T20:05:00Z",
    "one_line": "Round 44 L8/L9: FWD-5 PASS on judgment (15 days on 5 names served in (tier, mentions DESC, published ASC) order with 0 violations; PROD TimelinePanel renders the served order on a day click); FWD-2, FWD-7 (APPLIED CHATTER_AXIS_SOURCE=legacy) and FWD-12(c) (config.json sa cap 25) FAIL confirmed; aq-4's reading of sa:3793704 carries.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda:Invoke opal-amgt-scoped-api /security/{AAPL,MSFT,TSLA}_US_Equity/timeline/day/<3 busiest days each>: 9 of 9 status 200, listed == articles_total, 0 order violations",
        "portal origin/PROD dbd29c63 src/pages/SecurityAnalysis/components/TimelinePanel.tsx:264,318,499,668 (day click -> DayDissection -> day.articles.map, no sort)",
        "aws lambda get-function-configuration amgt-resapp-chatter-axis: CHATTER_AXIS_SOURCE=legacy",
        "lib/opal_data_harvest/config.json:26 \"sa\": 25 at HEAD"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A compile record: the round's four cells are graded here, and the FAIL repairs are offered in the packet for the round-44 analysis.",
    "spec_asserts": "FWD-5: clicking any day shows the articles behind that day, strongest first.",
    "world_is": "The served day route and the PROD page list them tier first, then by mention count.",
    "notes": "MSFT's three busiest days carry no tier-A article; this is left to FWD-6/7 at the analysis."
  }
]
```

-- 3.0.0_SA_CVO~Z

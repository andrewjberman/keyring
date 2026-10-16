# NFRA_OPLGTW -- round 37 AC3 graded on real answer bodies (site Z): four graded, one held for its replaced body

Author: 3.0.0_SA_CVO~Z. Round: v30. Fabric: site-z. Recorded: 2026-10-16 ~11:0xZ.
**Input:** `2.0.0_SA_COO~O` msg 34927 (acked). `deliverables/0.7.0_AE_CloudOps~Z/ANSWER_BODIES.json` @573d610fd0: 16 projected
answer bodies read at 10:36:38Z from the live release `3d5c9c8bf1`, after an on-host scrub and a local UUID post-scrub (30
replaced). Read whole by this seat. Amendments read at the order bytes: ap-19 A3, and ap-23 A8.

**Instrument caution: the record is not the served bytes.** The capture's scrub (`ev1_answer_bodies.py:37, 42-67`):
- hyphenates every run of 8+ digits in groups of 4, so `594918104` reads `5949-1810-4`;
- rewrites any number at or above 10^7 as a comma string (`"156,461,148,221.40"`).

So the hyphenated CUSIPs and ISINs (`5949-1810-4`, `US5949-1810-45`, `7562-5530-3`), the partner csv cells (`1886-6133-0.12`)
and the string-typed `aum` and `market_value` are artifacts of the evidence, not of the gateway. I counted none of them
against a tool. I graded only markers the scrub does not touch: unit fields, date fields, flags, status words, reasons and
per-firm separation.

## The grades

**NFRA_OPLGTW.TO-OG-ap-18 AC3: MET.**
- **Newest-part counts:** `harvest_get_chatter` (AAPL, 10-01..10-15) states `denominator {rows_in_part 68002, rows_for_key 281,
  days_returned 8}` beside `as_of 2026-10-08` and the source part keys. `rows_for_key` 281 is the same for CAT, and it is right:
  one daily row per key from 2026-01-01 to 10-08 is 281.
- **Quiet name:** CAT's answer marks every day `data_status: DENIED` and gives `absent_reason` "security_key has no
  30/90/365-day row in the newest chatter_window part". The analyst is told the zeros come from a denied fetch, not from a
  quiet name. That is the honesty the marker is for.
- **Unheld CUSIP:** `999999AA9` returns `status: not_held`, `not_held: ["cusip"]` and a plain-English reason.
- **Observation, not grounds:** the chatter data's newest partition is 2026-10-08, about 6 trading days behind T-1 at the
  read. The answer states the date (`as_of`) but gives no trading-day lag, unlike the news and portal tools.

**NFRA_OPLGTW.TO-OG-ap-20 AC3: MET.**
- **Units:** `etfs_get_fund_holdings` (IDVZ) states `weight_unit: "pct_points"` with `weight_column: "weight"` (PBR 4.79).
- **Three dates in one row:** the book-totals row carries `date` 10-13, `data_as_of` 10-12 and `prior_date` 10-09, and the
  denominator gives `trading_days_behind_t1: 2`.
- **Partner coverage:** `etfs_get_monthly_report` (2026-09) states coverage in each partner's own words ("21/21 trading days;
  0 carried for missing data", 20/21 with 1 carried, 18/21 with 3 carried) beside each partner's own csv rows.
- **Observation, not grounds:** other holding fields carry no unit (`yield`, `return_*`, a holding-level `aum`). These
  are read beside the unit-bearing weight.

**NFRA_OPLGTW.TO-OG-ap-21 AC3: MET.**
- **The section:** `harvest_get_published_analysis` returns the section asked for (`ledger`, `versions`, `timeline`), each
  absent part with a reason (versions: "no object under ...derived/model_block/AAPL_US_Equity/").
- **The projection:** the timeline answer flags `truncated: true`, `projected_to_bytes: 50815`.
- **Observations, not grounds:**
  - 50,815 bytes is above 50,000, so the cap is read as 50 KiB (51,200).
  - The answer's `as_of` is the time of the read, not the data's own date. The data dates sit in the series rows and
    `latest_by_class` stamps.

**NFRA_OPLGTW.TO-OG-ap-23 AC3 (as amended by A8): PARTIAL.** Three markers stand; two are met and one is half met.
- **A firm's data date stated:** MET. `client_get_holdings` (49financial, a SmartX account `****4521`) states `as_of`
  2026-10-15, `partition_date` 2026-10-15 and `freshness_td: 0`. The platform label is honest:
  `platform_label "Schwab"`, `label_claim "inferred"`, with its source sentence.
- **Rows never merged across firms:** MET. The same account ref asked of `cottonwood` returns `absent_reason
  "firm_not_served"` with no rows, kept apart from 49financial's 12 rows.
- **Figures with units:** HALF MET.
  - The rival answer (`etfs_get_rival_fund_holdings`, BASG) states `weight_unit: "fraction"` and `trading_days_behind_t1: 1`.
  - The client holdings answer gives `weight` (0.067852, `weight_basis "derived"`) and `market_value` with **no unit
    field**: no `weight_unit`, no currency.
  - An analyst must infer that the weight is a fraction. This is the one gap: a `weight_unit` (and a currency) on the
    client envelope.
- **Schwab masters never summed:** left the criterion by A8 and is carried. It returns to this seat's reading on the release
  that carries MX-c-23's Schwab catalog row. It is not dropped.

## Held

**NFRA_OPLGTW.TO-OG-ap-19 AC3: NOT MEASURED until the replaced body lands** (COO msg 34927: "one ap-19 body ... is being
replaced"). Read so far against A3's wording:
- **Freshness in trading days:** MET. `portal_get_pipeline_freshness` gives per-source `trading_days_behind_t1`, `stale` and
  `frozen` (attribution and peer 11, frozen; data and model pkl 1). `news_search_articles` gives `freshness.trading_days_behind_t1: 0`.
- **An empty window with its as-of:** NOT YET SHOWN. The body on record (`news_search_articles`, 2026-10-11, a Sunday)
  matched 716 items, so it is not an empty window. A body whose window holds 0 items, with its `as_of` and `absent_reason`,
  is what the marker needs.
- **The 14-day cap stated:** the body on record is `news_for_security`, which states `window_days_applied: 30` for an ask of
  999. A3 moves the marker to `news_search_articles`, whose replaced body is not yet in the file.

The file is @573d610fd0, with no commit after 10:43Z. Both missing bodies (an empty window, and the 14-day cap on
`news_search_articles`) close this on one read.

## Rows

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S77",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T11:05Z",
    "one_line": "Round 37 AC3 on real answer bodies: NFRA_OPLGTW.TO-OG-ap-18 AC3 MET, NFRA_OPLGTW.TO-OG-ap-20 AC3 MET, NFRA_OPLGTW.TO-OG-ap-21 AC3 MET, NFRA_OPLGTW.TO-OG-ap-23 AC3 PARTIAL (client holdings carry no weight unit or currency; data date and firm separation met; Schwab marker carried by A8); ap-19 AC3 held for its replaced body. The capture's scrub hyphenates 8+ digit runs and comma-formats large numbers, so identifiers in the record are not the served bytes.",
    "class": "OBSERVATION",
    "spec_asserts": "AC3 of OG-ap-18 (:98), OG-ap-20 (:86), OG-ap-21 (:79), OG-ap-23 (:69 as amended by A8), OG-ap-19 (:87 as amended by A3): the first answers read as an analyst would want, graded on a real call.",
    "world_is": "ANSWER_BODIES.json @573d610fd0 (16 bodies, live 3d5c9c8bf1, read 10:36:38Z). ap-18: chatter denominator rows_in_part/rows_for_key/days_returned with as_of; quiet CAT data_status DENIED with absent_reason; CUSIP not_held with reason. ap-20: weight_unit pct_points; book row date/data_as_of/prior_date; partner coverage strings beside each partner's csv. ap-21: section returned, absent parts reasoned, truncated true with projected_to_bytes 50815. ap-23: client as_of/partition_date/freshness_td 0; cottonwood on the same ref firm_not_served with no rows; rival weight_unit fraction; client holdings have no weight_unit or currency. ap-19: freshness in trading days met; the quiet-day body is not an empty window (716 items); the 14-day cap body is pending replacement. ev1_answer_bodies.py:37,42-67 hyphenates 8+ digit runs and comma-formats numbers >= 1e7.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.7.0_AE_CloudOps~Z/ANSWER_BODIES.json @573d610fd0, all 16 bodies read by this seat",
        "deliverables/0.7.0_AE_CloudOps~Z/ev1_answer_bodies.py:37,42-67 (the scrub's hyphenate and number formatting)",
        "task-orders NFRA_OPLGTW.TO-OG-ap-19 A3 and TO-OG-ap-23 A8 (read at the order bytes)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Open: ap-19 AC3 closes on the replaced bodies (an empty news window with as_of and absent_reason; the 14-day cap on news_search_articles). Enrichment: a weight_unit and currency on the client_* envelope (ap-23's half-met marker). Carried: Schwab masters never summed returns on MX-c-23's release (A8)."
  }
]
```

-- 3.0.0_SA_CVO~Z

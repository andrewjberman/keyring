# NFRA_MCPORTAL -- MP-z-6 AC2 with leg (b) on the served catalog (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v17. Fabric: site-z. Recorded: 2026-10-21 ~08:1xZ.

**Input:** `1.0.0_SA_CTO~Z` msg 36265, which points at `NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/evidence/ROUTING_SERVED_bdfee515.md`
@ecb20d56a64 and its `ROUTING_TABLE_served_bdfee515.json`. Both were read, and every non-ROUTED pair was printed by this seat.

**TO-MP-z-6 AC2: NOT MET.**

## The two legs as the CTO's analysis wrote them are now both MET

- **Leg (a):** MET on the served capture (ADJUDICATION_v16.Z.md, Z-C-S67). The 16 shown indexes each name their own
  segment.
- **Leg (b):** MET. On the SERVED catalog `bdfee515` the routing table reads `display` 0, against 127 tools and 199 pairs.

## Why the grade still reads NOT MET

The criterion's own words are "the full breakdown he asked for -- every vendor or channel, the tools and indexes on each".
The same instrument, on the same served catalog, reads `link` 6 and `code` 3. That is 19 of 199 pairs not routed, on 9
tools, which carry index links to rows the tool's code does not read. The page shows each tool's indexes, so on these tools
it shows indexes they do not read:

- `client_resolve_account` carries the three Schwab `fact_acc` rows (`schwab/08242234`, `schwab/08335338`,
  `schwab/08403355`) and `commonwealth_cottonwood_account_links`, and reads none of them. This is the shape of the defect
  Andrew reported on 10-19: index information that does not belong to the tool.
- `client_get_allocation` carries three `smartx` model tables, and `client_get_fees` carries `49f_dim_advisor_fee_role`.
  These two and `client_resolve_account` are the 3 `code` tools owned by `2.0.0_SA_COO~O`.
- **The link-class tools:**
  - `harvest_get_fundamentals` carries three bloomberg bronze rows;
  - `harvest_get_filing_analysis`, `harvest_resolve_security`, `news_market_mood`, `news_trending_topics` and
    `schwab_describe_dataset` carry one row each.

**The breakdown he asked for is therefore not yet the one served.**
- `2.0.0_SA_COO~MI`'s note in the same file says the 6 link misroutes are fixed in candidate e (link 0) and "only its deploy clears them".
- The 3 code defects are NFRA_OPLGTW's.
- The four index-less 49financial and multi segments (v16) still await MI's answer.

**It re-grades when** the served catalog reads `link` 0 (candidate e, or its successor, deployed and re-measured) and MI
has answered the four empty segments. The 3 code tools are graded on the page only for the indexes they show, not for their
code.

## Rows

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-C-S68",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-21T08:10Z",
    "one_line": "L9 re-grade, NFRA_MCPORTAL.TO-MP-z-6 AC2 (judgment): NOT MET -- both of the analysis's legs are now MET (a: the 16 shown indexes name their own segment; b: display 0 on the SERVED catalog bdfee515), but the same served table reads link 6 / code 3: 19 of 199 pairs on 9 tools carry indexes their code does not read (client_resolve_account shows three Schwab fact_acc rows it never reads), so the page does not yet show 'the tools and indexes on each' correctly.",
    "class": "OBSERVATION",
    "spec_asserts": "MP-z-6 AC2: the full breakdown he asked for -- every vendor or channel, the tools and indexes on each; ROUND_ANALYSIS.z-round1.md:29-35 legs (a) and (b).",
    "world_is": "ROUTING_SERVED_bdfee515.md @ecb20d56a64: tools 127, pairs 199, routed 180, link 6, code 3, display 0, untraced 0; candidate e (not served) reads link 0, code 3. ROUTING_TABLE_served_bdfee515.json non-ROUTED pairs printed by this seat: client_resolve_account -> schwab_08242234/08335338/08403355_fact_acc and commonwealth_cottonwood_account_links; client_get_allocation -> three smartx model tables; client_get_fees -> 49f_dim_advisor_fee_role; harvest_get_fundamentals -> three bloomberg bronze rows; harvest_get_filing_analysis, harvest_resolve_security, news_market_mood, news_trending_topics, schwab_describe_dataset -> one each.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/evidence/ROUTING_SERVED_bdfee515.md @ecb20d56a64 (read whole)",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/evidence/ROUTING_TABLE_served_bdfee515.json (counts and every non-ROUTED pair printed by this seat)",
        "ADJUDICATION_v16.Z.md#NFRA_MCPORTAL-Z-C-S67 (leg (a))"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade: TO-MP-z-6 AC2 NOT MET, superseding Z-C-S67. Legs (a) and (b) MET as written; the grade rests on the criterion's 'indexes on each', which the served routing table shows wrong on 9 tools. Re-grades when the served catalog reads link 0 (candidate e or successor deployed and re-measured) and MI has answered the four index-less segments."
  }
]
```

-- 3.0.0_SA_CVO~Z

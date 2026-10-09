# DSGN_AMGTV1 -- round 66 L9 grades (dell1)

<sweep_watermark>2026-10-09T14:33Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T14:33:00Z. Packet: 2.0.0_SA_COO~D1 msg 2559, org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round66/ROUND66_WALK.md, walk tmp/ui-walk/20261009T142010Z. FWD-7 MET; FWD-8 NOT MET (unreadable tickers, USD header over EUR cells, two names walked of three); FWD-27 NOT MET (one figure in two money formats; market cap in two units with no measure label).

```json
[
  {
    "id": "DSGN_AMGTV1-D1-C-S37",
    "project": "DSGN_AMGTV1",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T14:33:00Z",
    "one_line": "FWD-7 MET: walked on two names whose filing lists no officers (no filing has been read for NG/ LN or BP/ LN). Each Exec Management tab shows the officers with where the list came from ('From Bloomberg's officer list'; NG/ LN 9 officers, as of October 7th, 2026; BP/ LN 10), chief executive first, then the chief financial officer.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DSGN_AMGTV1_PRD.md FWD-7/FWD-8/FWD-27 DONE WHEN and ACCEPT; spine L9: graded by a seat that did none of the work.",
    "world_is": "FWD-7 MET: walked on two names whose filing lists no officers (no filing has been read for NG/ LN or BP/ LN). Each Exec Management tab shows the officers with where the list came from ('From Bloomberg's officer list'; NG/ LN 9 officers, as of October 7th, 2026; BP/ LN 10), chief executive first, then the chief financial officer.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO viewed tmp/ui-walk/20261009T142010Z/shots/010-NG-LN-Equity-Exec-Management-expanded.png: 'From Bloomberg's officer list', Zoe A Yujnovich Chief Executive Officer, Andrew Agg Chief Financial Officer, ... '9 officer(s), as of October 7th, 2026'; 'company filings read for this name -- No company filing has been read for this name yet'",
        "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round66/ROUND66_WALK.md FWD-7 table (BP/ LN shot 039)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard."
  },
  {
    "id": "DSGN_AMGTV1-D1-C-S38",
    "project": "DSGN_AMGTV1",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T14:33:00Z",
    "one_line": "FWD-8 NOT MET. On ASML NA's peers table (shot 131): (1) tickers are not all readable -- Tencent reads 'BMMV2K' (an exchange code, not a ticker a PM recognises) and SK hynix's ticker cell holds a sentence ('This listing has only an exchange number; we have no company match for it yet.'); (2) the column headers say 'Mkt Cap (USD mm)' and 'EV (USD mm)' while the subject row in those columns is EUR ('EUR 541,932', 'EUR 625,609') -- the header states a currency the cell contradicts; (3) SK hynix's Price (last) '1,495,000' carries no currency beside USD-scale peers. The mixed-currency case is otherwise handled well (the aggregates exclude the EUR subject, n=12; missing columns explained once). DONE WHEN asks for three names walked; the record grades peers on two (ASML NA, 992 HK).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DSGN_AMGTV1_PRD.md FWD-7/FWD-8/FWD-27 DONE WHEN and ACCEPT; spine L9: graded by a seat that did none of the work.",
    "world_is": "FWD-8 NOT MET. On ASML NA's peers table (shot 131): (1) tickers are not all readable -- Tencent reads 'BMMV2K' (an exchange code, not a ticker a PM recognises) and SK hynix's ticker cell holds a sentence ('This listing has only an exchange number; we have no company match for it yet.'); (2) the column headers say 'Mkt Cap (USD mm)' and 'EV (USD mm)' while the subject row in those columns is EUR ('EUR 541,932', 'EUR 625,609') -- the header states a currency the cell contradicts; (3) SK hynix's Price (last) '1,495,000' carries no currency beside USD-scale peers. The mixed-currency case is otherwise handled well (the aggregates exclude the EUR subject, n=12; missing columns explained once). DONE WHEN asks for three names walked; the record grades peers on two (ASML NA, 992 HK).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO viewed tmp/ui-walk/20261009T142010Z/shots/131-ASML-NA-Equity-Peers-expanded.png: header 'Mkt Cap (USD mm)', 'EV (USD mm)'; subject row 'EUR 1,626 / EUR 541,932 / EUR 625,609'; Tencent 'BMMV2K'; SK hynix ticker sentence and Price 1,495,000",
        "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round66/ROUND66_WALK.md FWD-8 table and 'For the grader' notes"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard."
  },
  {
    "id": "DSGN_AMGTV1-D1-C-S39",
    "project": "DSGN_AMGTV1",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T14:33:00Z",
    "one_line": "FWD-27 NOT MET on 'one money format across the figures the page formats' and 'no two figures for one thing disagree without a label': ASML's price is written 'EUR 1626.20' in its header tile and 'EUR 1,626' in the peers table (two formats, one figure), and its market cap reads 'EUR 631B' (tile, October 9th) against 'EUR 541,932' mm (table, as of September 19th) -- the dates differ, but the two figures sit in different units with no label naming them as different measures. Met on the walk: one time zone (ET) on every page-formatted stamp, one country form, the Filings line per name, officers CEO-then-CFO. The walker's money/date hits on BP and the Thesis windows are served drafted prose, graded as served (C-PRESENTATION-ONLY).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DSGN_AMGTV1_PRD.md FWD-7/FWD-8/FWD-27 DONE WHEN and ACCEPT; spine L9: graded by a seat that did none of the work.",
    "world_is": "FWD-27 NOT MET on 'one money format across the figures the page formats' and 'no two figures for one thing disagree without a label': ASML's price is written 'EUR 1626.20' in its header tile and 'EUR 1,626' in the peers table (two formats, one figure), and its market cap reads 'EUR 631B' (tile, October 9th) against 'EUR 541,932' mm (table, as of September 19th) -- the dates differ, but the two figures sit in different units with no label naming them as different measures. Met on the walk: one time zone (ET) on every page-formatted stamp, one country form, the Filings line per name, officers CEO-then-CFO. The walker's money/date hits on BP and the Thesis windows are served drafted prose, graded as served (C-PRESENTATION-ONLY).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO viewed tmp/ui-walk/20261009T142010Z/shots/131-ASML-NA-Equity-Peers-expanded.png: tile 'EUR 1626.20', 'EUR 631B as of October 9th, 2026'; table 'EUR 1,626', 'EUR 541,932 as of September 19th, 2026'",
        "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round66/ROUND66_WALK.md FWD-27 table"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard."
  }
]
```

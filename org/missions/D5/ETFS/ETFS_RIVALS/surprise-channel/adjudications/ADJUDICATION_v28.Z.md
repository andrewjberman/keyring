# ETFS_RIVALS -- round 24 L8/L9 on the round-24 real run, in a browser (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~21:30Z. Packet: COO~RV msg 31395 (@ac658a6410). Round 24 is merged and NOT deployed.

**cu-1 J1: MET.** Two faults noted: the read-out keeps the last curve position while a marker is pointed at; a tooltip for a
marker at the top of the plot covers the read-out.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S71",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T21:30:00Z",
    "one_line": "Round 24 L9 on the issuer's real run of day 2026-10-07 (local, not served), in a browser: RIV-cu-1 J1 MET. Pointing at the curve, the price (34px, weight 800) and the date (22px, weight 700) are the largest text of the chart; pointing at a buy or a sell marker shows a green or red box headed 'Bought $10,592,358' or 'Sold $1,020,518' at 26px weight 800 with the date, basis points and trade count beneath; the chart is a bordered, rounded figure with five dated ticks. Two faults noted, neither against the criterion.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "RIV-cu-1 J1: hovering the curve, the price and date are the most prominent text of the chart; hovering a buy or sell marker shows what was traded, when and for how much without reading small text; the chart reads as a framed figure with dates on its x-axis. Then Andrew's own look, which is the acceptance.",
    "world_is": "Object: C:/tmp/rv-r24-realrun/layer/ index.html (sha256 f1a4a9044cb86b2a...) and its 13 chart objects on site Z. This seat drove its own headless browser with the chart route answered from those objects (not the issuer's stand-in server), 0 console errors or warnings and 0 page errors, and looked at the screenshots. Six cases, five the issuer did not look at:\n- GQGU Meta, 30 days, a buy marker (1400 px wide): ticks '6 Sep, 14 Sep, 21 Sep, 29 Sep, 6 Oct'; read-out '777.59 USD' 34px / 800 and '2026-09-24' 22px / 700, the next largest text 18.7px; tooltip 'Bought $10,592,358 / on 2026-09-14, 165 bps of the fund, 1 trade.', green, inside the frame.\n- IDVZ Petrobras, 365 days, a SELL marker: ticks 'Oct 25, Jan 26, Apr 26, Jul 26, Oct 26'; tooltip 'Sold $1,020,518 / on 2026-04-08, 68 bps of the fund, 1 trade.', red, inside the frame.\n- CGIC 2454 TT, 365 days, a NON-DOLLAR listing with markers at the TOP of the plot: read-out '4950.00 TWD', axis 'Price in TWD'; the tooltip for a top marker sits over the read-out and hides the price while it shows.\n- GQGU Meta, 365 days, a marker near the top right: tooltip shown; its box ends 1 px past the frame's right edge.\n- BASG Kla (no price history): no chart, the sentence, and the trade list beneath.\n- GQGU Meta, 30 days, a NARROW window (640 px): the frame, read-out and tooltip hold; the axis text scales down with the drawing and is small.\n- Frame: a 1 px border, 10 px radius and its own background around the read-out and the plot; the plot is 934 x 467 px at 1400 px.\nTwo faults, noted for the issuer and for Andrew's look:\n1. While a marker is pointed at, the read-out and the dashed guide keep the LAST curve position, not the marker's day: the Petrobras screenshot shows '20.75 USD 2026-05-11' above a tooltip for 2026-04-08. Two dates are on screen and the larger one is not the trade's.\n2. A tooltip for a marker at the top of the plot covers the read-out (the worker's own caution, seen here on the Taiwan listing). It is common today because non-dollar listings have 3 prices and their markers ride the top edge; a year of closes (FWD-24) removes most of it.\nNot looked at: keyboard focus of a marker; a touch device; the served page (not deployed).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round24/DRAIN_END_PACKET.round24.md @ac658a6410",
        "C:/tmp/rv-r24-realrun/layer/opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-07/ on site Z, read 2026-10-07 ~21:15Z",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_190xZ_RIVALFUNDS_SMOKED_POPUPS_GOOD_CHART_UI_NEXT.md @f76452470f (his three asks)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record. J1 is MET on its three clauses, so the CTO's condition for today's deploy (msg 31398, half @db4ab8faec) is on file. The two faults are for the next display cell if Andrew's look does not already ask for more; his look is the acceptance. The served re-read follows the deploy, with the CTO half's C1 and C2."
  }
]
```

-- 3.0.0_SA_CVO~RV

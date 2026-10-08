# ETFS_RIVALS -- round 25 L8/L9 on the round-25 real run (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~23:45Z. Packet: COO~RV msg 31469 (@7c0730d28d); CTO half @16d5d5acd9. NOT deployed.

**rg-1 J1: NOT MET -- BLOCKING. The object filed under 2026-09-29 holds 2026-09-30's closes; the change would put the next
day's close on 09-29 in every fund's tables and charts. mr-1 J1: MET.**

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S73",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T23:45:00Z",
    "one_line": "Round 25 L9, RIV-rg-1 J1: NOT MET. The object the cell brings into use, security_market date=2026-09-29 market-20260929-53bc393958bd.parquet (434 rows, produced 2026-10-01T11:10:34Z by a reference-data pull), holds the closes of 2026-09-30, not of 2026-09-29: 47 of 57 dollar securities equal the funds' own 09-30 valuations within 0.2 percent (median difference 0.0 percent), against 6 of 58 for their 09-29 valuations (median 1.19 percent). The change would put the next day's close and day return on 09-29 in every fund's rankings and charts.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S69",
      "ETFS_RIVALS-Z-S67"
    ],
    "spec_asserts": "RIV-rg-1 J1: on the real day the tables and charts of every fund read 2026-09-29 from its market closes; each figure that moves against the served page is named and explained by a close that was unused before; nothing moves on a date that had one object or identical objects. CTO half @16d5d5acd9 C1: read MediaTek in CGIC by hand; a close off by a factor, a currency or a listing is NOT MET and nothing is applied.",
    "world_is": "The issuer's counts reproduce on this seat's own read; the object they rest on is misdated.\n- Reproduced: holding_contribution 3,259 of 6,066 rows move (float tolerance 1e-9), 2,418 on the page periods (30d 747, 90d 761, 365d 910; 2,125 security, 293 sector); 0 rows of MTD or QTD, whose windows start after 09-29; buying_trend 0 of 1,406. All 2,328 security rows with a moved contribution are in securities with a close in the 434-row object. Charts against the served objects: 408 points on 2026-09-29 become market closes, each equal to that object's px_close; 696 valuation-implied points on other dates appear for AJG US (twice), JAR LN and ATD CN, which gain a stored currency; no other point on another date changes.\n- C1, MediaTek in CGIC by hand (the fund's own reports, market_value over quantity, 420,000 then 428,000 shares): 09-25 166.04 USD; 09-28 166.04 (unchanged); 09-29 153.81, a day return of -7.36 percent; 09-30 154.57, +0.49 percent. The object says 4,980 TWD and a day return of +1.22 percent. The moved figure is exactly weight times the gap: 2.72 percent of the fund times (1.22 + 7.36) = 0.233 points, the issuer's largest move. The close is not off by a factor or a listing; it is off by a DAY.\n- The day, measured on dollar securities so no exchange rate is involved: the object's px_close against the funds' implied price of each report date: 09-25 5 of 58 within 0.2 percent (median difference 1.50 percent); 09-28 2 of 58 (1.33); 09-29 6 of 58 (1.19); 09-30 47 of 57 (0.00); 10-01 13 of 41 (0.72). The object was produced on 2026-10-01 at 11:10Z, before that day's close, so a last-price pull returned 09-30's close; it was filed under date and as_of 2026-09-29.\n- Size on 09-29: of 533 fund-securities with both a valuation-implied return and the object's day return, 312 differ by more than 1 point, 154 by more than 2 and 6 by more than 5, 24 of the 154 in dollar securities (BASG Marvell: implied +4.51, object +0.36).\n- Consequence if applied: 09-29 would carry 09-30's market move, and 09-30, which stays valuation-implied, would carry it again, while 09-29's own move is dropped. 2,418 figures on the page and 108 top-or-bottom-ten places would move to less correct values.\n- Row Z-S69 re-read: the 413 closes that every reader ignores are real Bloomberg closes, but of the next day. Their being unused is not a loss for 09-29. Used as 09-30's closes they would be a gain (no 09-30 partition is stored).\n- Not measured: whether any other stored date is misdated the same way. The issuer's limit (a market day between valuation-implied days where a valuation lags) is a second, separate question; on 2026-10-05 this seat found 216 of 217 dollar closes within 3 percent of the same day's valuation (ADJUDICATION_v17), which does not test a one-day shift tightly.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round25/DRAIN_END_PACKET.round25.md @7c0730d28d",
        "s3://opal-data-etfs/rivalfunds/etfs/gold/security_market/date=2026-09-29/market-20260929-53bc393958bd.parquet (434 rows; produced_at 2026-10-01T11:10:34Z; date and as_of 2026-09-29)",
        "s3://opal-data-etfs/rivalfunds/etfs/gold/canonical_shape/ date=2026-09-25, 09-28, 09-29, 09-30 (holdings-20261005T054409Z-*.parquet) and date=2026-10-01 (holdings-20261005T054409Z-9357ccb096f1.parquet)",
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round25/before_after_tables_2026-10-07.json @7c0730d28d",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_ETFS_RIVALS_R25_READERS_GRAIN_DEPLOY_20261007.md @16d5d5acd9 (C1)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-Z-C-S74",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T23:45:00Z",
    "one_line": "Round 25 L9, RIV-mr-1 J1: MET on the round-25 real run in a browser. Over 210 marker hovers (5 dialogs, widths 1400 and 640 px) the read-out and the tooltip name the same day in 210 and the tooltip overlaps the read-out in 0.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "RIV-mr-1 J1: pointing at a marker, the read-out and the tooltip name the same day; the tooltip does not hide the read-out for a marker anywhere on the plot.",
    "world_is": "This seat's own headless browser on C:/tmp/rv-r25-realrun/layer/, the chart route answered from the run's chart objects, 0 page errors. Dialogs: GQGU Meta (365d 21 markers, 30d 6), CGIC 2454 TT (40 of 126, the markers at the top of the plot), IDVZ Petrobras (1, a sell), BIDD SK hynix (38), each at 1400 px and 640 px: 210 hovers that showed a tooltip. Same day in the read-out and the tooltip: 210 of 210. Tooltip intersecting the read-out's price or date: 0 of 210. Tooltip above the svg's top: 1 of 210. Tooltip past the frame's edge by more than 1 px: 18 of 210 (not looked at one by one; the issuer saw 0.64 px on one). SCHY Roche has no price history and draws nothing. Not looked at: keyboard focus, a touch device.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round25/DRAIN_END_PACKET.round25.md @7c0730d28d",
        "C:/tmp/rv-r25-realrun/layer/opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-07/ on site Z, read 2026-10-07 ~23:35Z",
        "adjudications/ADJUDICATION_v28.Z.md ETFS_RIVALS-Z-C-S71 @f97c41e692 (the two faults)"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV

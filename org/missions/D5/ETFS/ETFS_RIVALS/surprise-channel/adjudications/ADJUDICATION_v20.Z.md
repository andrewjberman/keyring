# ETFS_RIVALS -- rounds 15 to 19 L9 on the round-19 real run, in a browser (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~12:25Z. Packet: COO~RV msg 30878 (@629a94a0e8). Earlier grades: ADJUDICATION_v16,
v17, v18. Nothing of rounds 15 to 19 is deployed or served. Not the slug (investigation Z-S54, round 14, is undispositioned).

| Criterion | Grade on the round-19 real run |
|---|---|
| RIV-co-1 J1 | MET (as C-S52, C-S53) |
| RIV-pc-1 J1 | MET |
| RIV-nc-1 J1 | MET |
| RIV-tl-1 J1 | MET for list against markers (702 of 702); the buying section above it counts a different window in 141 dialogs |
| RIV-ml-1 J1 | Labels MET (393 of 393); months against trades: 382 of 393 inside the strip's span, 56 strips cannot show October 2025 |
| RIV-md-1 J1 | Works in a browser; NOT GRADED as final (names the live signed-in page); two display faults noted |
| RIV-pd-2 J1 | Controls MET on this page; NOT GRADED as final (names the served page) |

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S60",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T12:25:00Z",
    "one_line": "Rounds 15-19 L9: this seat opened all 702 chart frames of the round-19 real-run page in a headless browser, the chart route stood in by request interception, 0 page errors. Rows Z-S56 and Z-S58 are repaired on this run. The trade list agrees with the chart object's markers in 702 of 702 frames; every month strip is labelled by calendar month ending October. Open: 11 strips disagree with their markers (Z-S59), 56 year strips have no cell for October 2025 trades the list shows, and 141 dialogs put a 30-day or 90-day buying section above a 365-day trade list.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S56",
      "ETFS_RIVALS-Z-S58",
      "ETFS_RIVALS-Z-S59"
    ],
    "spec_asserts": "RIV-tl-1 J1: in a browser, a dialog's trade list agrees with its chart's markers and with the buying section above it. RIV-ml-1 J1: on the real page a strip's bought and sold months are the months of the trades listed beside it. RIV-nc-1 J1: the dialog of a holding with no stored currency shows no chart and the sentence, and a holding with a stored currency is drawn as before. RIV-pc-1 J1: no curve joins two currencies and a reader of a non-US security's dialog can tell the currency. RIV-md-1 J1 (live page, signed-in browser): the curve for 30d / 90d / 365d, hollow green and red markers sized by share of fund, price and date on pointing at any day, the trade's value and basis points on a marker, a gap drawn as a gap with its reason, the price source named. RIV-pd-2 J1 (served page): every ranking, trend and dialog offers exactly 30d, 90d and 365d and opens on 30d; a period a fund's history does not reach reads partial with its reason.",
    "world_is": "Object: C:/tmp/rv-r19-realrun/layer/ on site Z (code root CLOUD 2aba59986e; index.html 1,640,613 B; 13 chart objects, 702 keys). Method: org/tier1_exec/3.0.0_SA_CVO/deliverables/etfs_rivals_r19/r19grade.py (every dialog opened so the page's own script loads and draws; each frame read back) and analyse2.py (each frame against its chart object).\n- Frames: 702 in the DOM, 702 keys in the objects, one to one.\n- tl-1, list against markers: 702 of 702 agree (77 with 0 markers say 'No trades in the last 365 days'; 625 list one line per marker, 70 of them 20 lines plus 'and N earlier'). In 625 of 625 the first line is a marker of the object in side and dollars. Before the script runs, 618 static elements read 'The fund's trades over the last 365 days load with the chart.' and 0 say 'No trades'. Z-S56 is repaired.\n- tl-1, list against the buying section above it: 393 dialogs carry a buying section. 252 are headed 'last 365 days', 87 'last 30 days' and 54 'last 90 days'; the list below is always 365 days. So in 141 dialogs the count in the section ('across N trades') and the list are over different windows, each labelled. Counting markers inside each section's window by this seat's own boundary gives agreement in 352 of 393; the other 41 differ by one or two trades at the window's edge, and this seat did not establish whether the boundary rule or the page is off. The section-window counts and the first-line check were computed ad hoc from the same result file and are not in the committed analyse2.py.\n- ml-1: 393 strips, 393 with a label on every cell, 393 ending in Oct; cells 12 (180), 11 (20), 10 (40), 7 (12), 4 (54), 2 (87). Bought/sold cells against the year-months the markers end in, inside the strip's span: 382 of 393 agree (the issuer's figure, reproduced); the 11 are Z-S59 (examples: GQGU 857477103 and IDVZ TKOMY show October with no October marker; TXUE BTRW LN has February and March markers and no cell lit). 56 of the 252 year strips have one or more markers in October 2025, inside the 365-day list and outside the strip, whose first cell is November 2025. Z-S58 (labels by position) is repaired.\n- nc-1: 97 of 97 frames with no stored currency show no svg and 'No price history is stored for this holding yet.'; the range buttons do nothing there. 604 of 605 frames with a stored currency draw an svg; the one that does not is BIDD 6475395Z_GR_Equity (EUR, 0 prices, 4 markers: the status line reads '0 prices, 4 trade markers' and nothing is drawn).\n- pc-1: 334 of 335 non-dollar frames print their currency in the drawn frame; the 335th is the same BIDD security. The axis label reads 'Price in <currency>' and the hover reads, for example, '2026-10-02: 4950.00 TWD (market close)' and '2026-05-04: 22.01 USD (implied from the holding)'.\n- md-1, exercised on 4 dialogs (IDVZ Petrobras, CGIC 2454 TT, BASG Kla, IDVZ AstraZeneca): each range button redraws and the count line changes (Petrobras 20 / 64 / 190 prices); pointing at the curve gives date, price, currency and source; a marker carries 'Sold on 2026-04-08: $1,020,518, 68 bps of the fund, 1 trade.'; a gap is shaded and listed with its reason; the source sentence is present. Two display faults: the 'Price in <currency>' label is printed over the axis's top figure when that figure is long (TWD), and with markers but almost no prices the markers ride the top edge (CGIC 2454 TT: 2 prices, 126 markers). The drawing uses about two thirds of the frame's width. The marker sizes were not measured.\n- pd-2: all 702 frames carry exactly the buttons 30d, 90d, 365d with 30d current; the page has one period group of three radios opening on 30d. The period rows inside dialogs: 'Last 30 days' 526, 'Last 90 days' 563, 'Last 365 days' 693; a dialog whose holding has no 30-day figure simply omits the row. Whether an omitted row is 'partial with its reason' is for the served grade.\n- Not exercised by any run: the served gateway route; cell pd-3 on real data; the backfill live.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round19/DRAIN_END_PACKET.round19.md @629a94a0e8",
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round19/month_strips_2026-10-06.json @629a94a0e8",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/etfs_rivals_r19/r19grade.py, analyse2.py (this commit)",
        "investigations/INVESTIGATION_v1.Z.md ETFS_RIVALS-Z-S56, ETFS_RIVALS-Z-S58, ETFS_RIVALS-Z-S59"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV

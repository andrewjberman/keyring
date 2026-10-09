# ETFS_RIVALS -- round 28 WORKSTREAMS 2 and 3 (first issuance) L9 (dell1 fabric)

Author: 3.0.0_SA_CVO~RV1, 2026-10-09 ~07:30Z. Packet: 2.0.0_SA_COO~V1 msg 1961,
`deliverables/2.0.0_SA_COO~V1/ws2/L8_PACKET_WS2_WS3.md` @fde80f8b5d. Artifact: the issuer's local real run of page date
2026-10-08 served at http://127.0.0.1:8765/rivalfunds/2026-10-08 (nothing deployed), opened in a browser (Playwright) by
this seat.

**RIV-wc-1 J1 MET. RIV-wc-2 J1 MET. RIV-wd-1 J1 NOT MET (the repeat clause; the other two clauses MET). RIV-wa-1 J1 HELD:
its face names "the first page published with this code", and no page is published yet (WS2 guard 1).** RIV-wb-1 has no
judgment criterion. This is the L9 record only: the round-28 L10 slug waits on tw-1 J1 (11:00Z vehicle run), aw-1 J1
(13:00Z sweep) and row D1-W26-S1 (ARMED).

```json
[
  {
    "id": "ETFS_RIVALS-D1-C-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~RV1",
    "surfaced_at": "2026-10-09T07:30Z",
    "one_line": "Round 28 WS2+WS3 L9: wc-1 J1 MET, wc-2 J1 MET, wd-1 J1 NOT MET on its repeat clause (CGIC calendar marks 10-01, 10-02, 10-05, 10-06 repeat while the windows ending 10-02 and 10-06 each show a trade), wa-1 J1 HELD for the first published page. All five AC1 checks reproduce PASS on this seat's runs at 83028dca8a.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "wa-1 J1: the IDVZ dialog on the first page published with this code reads a continuous 30d curve near 3.3 across 2026-10-07 and names the 15-for-1 split, the factor from a stored row. wc-1 J1: the dialog's trade list is closed by default, its heading names the selected window, and on 30d it lists only the last 30 days' trades. wc-2 J1: the header carries no Period row, the ranking panels still switch periods, and the audit's exclusion line names the excluded line apart from the trade table. wd-1 J1: over CGIC's 2026-09-28..2026-10-06 windows, no unchanged-count row and no sub-20-bps row is shown as a trade, and no trade sits on a day the calendar marks repeat.",
    "world_is": "- Mechanical, this seat, box/dell1 @83028dca8a, 07:2xZ: ws2-a.AC1, ws2-b.AC1, ws2-c.AC1, wc-2.AC1, wd-1.AC1 each 'AC1 RESULT: PASS 0 failures'. Suite not re-run (the packet's 962 passed is the issuer's read).\n- wc-1: Tokio Marine dialog, the one disclosure reads 'Trades in the last 30 days', open=false at load; the heading follows the toggle ('...90 days', '...365 days'). Sweep of 104 dialogs over the 13 funds (each disclosure opened before reading): 90 list on 365d a trade dated before the 30d window's start (2026-09-07), and on 30d none lists a trade wholly before it. Two (Valero, Veeva; fund index 7) list on 30d 'between 2026-09-03 and 2026-09-08': an inference window that ENDS inside the 30 days, matching the curve's '1 trade marker'. Read as in-window; MET.\n- wc-2: header (screenshot) holds title, lede and four stat tiles, no Period row. Ranking panel 30d -> 90d moves the contribution table (Petrobras +0.73% -> +1.25%; second row Taiwan Semiconductor -> China Construction Bank). Audit: three 'Left out: 1 money-market line traded (...)' elements, none inside a <table>; CGIC's reads 'Left out: 1 money-market line traded (CAPITAL GROUP CNTRL CSH-M, $16.6m): cash management, not a holding decision.' in its own div.rf-left-out after the 2026-09-30..10-02 trade table. MET.\n- wd-1: CGIC audit windows: 10-05..10-06 (1 trade, Vale entry $4.62m), 10-02..10-05 (none), 09-30..10-02 (1 trade, TSM trim -$6.58m = 25 bps of $2,593.8m), 09-29..09-30 (1 trade, UMG entry $3.14m), 09-28..09-29 (none). No unchanged-count row shown; the two sub-20-bps notionals are ENTRIES, which the face's item 2 keeps as trades at any size. Calendar row: 09-10..09-30 new, 10-01/10-02/10-05/10-06 repeat, 10-07 gap. Trades sit on 10-02 and 10-06, both marked repeat: the repeat clause is NOT MET as worded. The issuer's row D1-S4 says the labels, not the windows, are stale; this seat did not re-derive that and grades the page as served.\n- wa-1: the local IDVZ dialog shows the split and the 3.3 curve per the packet; not graded, because the face binds the grade to the first PUBLISHED page.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/L8_PACKET_WS2_WS3.md @fde80f8b5d",
        "task-orders/ETFS_RIVALS.TO-RIV-wa-1.split-adjusted-series.md:89, TO-RIV-wc-1...:88, TO-RIV-wc-2...:105, TO-RIV-wd-1...:107 (J1 faces); TO-RIV-wd-1...:37-49 (items 1-3)",
        "http://127.0.0.1:8765/rivalfunds/2026-10-08 and /audit, read by Playwright 2026-10-09 07:19-07:28Z",
        "surprise-channel/investigations/INVESTIGATION_v1.dell1.md ETFS_RIVALS-D1-S4"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV1

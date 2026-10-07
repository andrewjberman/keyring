# ETFS_RIVALS -- round 21 L8/L9 on the round-21 real run, in a browser (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~14:35Z. Packet: COO~RV msg 31023 (@dc23ed5ae9). Nothing of rounds 15 to 21 is deployed.

**pl-1 J1: MET. New, BLOCKING (C-S64): the 7 GQGU securities folded onto their Bloomberg key lost all 86 trade markers;
their dialogs show a buying section with trades above 'No trades in the last 365 days'.**

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S63",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T14:35:00Z",
    "one_line": "Round 21 L9 on the issuer's round-21 real run (local, not served), in a browser: RIV-pl-1 J1 MET. 252 of 252 year strips have a cell for every month their trade list names (180 run 'Oct 25' to 'Oct 26'); the caption 'Trades in the last 365 days' stands before the list in 695 of 695 frames; the currency label overlaps no other chart text in 597 of 597 drawn frames; the drawing fills its frame in 597 of 597.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "RIV-pl-1 J1: a year strip shows a cell for every month the trade list names; the list's caption reads true beside a 30-day or 90-day buying section; the currency label overlaps no axis figure and the chart fills its frame.",
    "world_is": "Object: C:/tmp/rv-r21-realrun/layer/ on site Z (worker branch @1bd3c3efeb; index.html 1,688,519 B; 695 frames, 695 object keys, 0 page errors). Every dialog opened and switched to 365d; each frame read back.\n- Strip: 393 strips. Headed 'last 365 days': 252 (13 cells 180, 11 cells 20, 10 cells 40, 7 cells 12); in 252 of 252 every month named by the list, and every month a marker ends in, has a cell. The 180 full strips start 'Oct 25' and end 'Oct 26'. The 141 strips headed 30 or 90 days show their own window (2 or 4 cells) and are not year strips.\n- Caption: 695 of 695 frames carry a data-chart-trades-head paragraph 'Trades in the last 365 days' immediately before the list. It is true beside a 30-day or 90-day section because it names the list's own window; the list agrees with the object's markers in 695 of 695 frames.\n- Label and width: 597 frames draw; in 597 the 'Price in <currency>' label's box intersects no other text of the chart, and the svg is at least 98 percent of the frame's width.\n- Strip against markers inside its span: 376 of 393 agree, 17 do not (round 19: 382 and 11). The 6 new ones are GQGU securities of row C-S64.\n- md-1 J1 and pd-2 J1 stay owed on the served page.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round21/DRAIN_END_PACKET.round21.md @dc23ed5ae9",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/etfs_rivals_r19/r19grade.py, analyse2.py @0c69a8829e (run on the round-21 layer)",
        "adjudications/ADJUDICATION_v20.Z.md ETFS_RIVALS-Z-C-S60 @0c69a8829e"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-Z-C-S64",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T14:35:00Z",
    "one_line": "On the round-21 real run, the 7 GQGU securities whose CUSIP key was folded into the Bloomberg key (Apple, Meta, Lam Research, Eli Lilly, Micron, Philip Morris, UnitedHealth) have 0 trade markers; the round-19 run held 86 for them under the CUSIP keys. Their dialogs say, for example, '+$43.9m net bought across 12 trades' and directly below 'Trades in the last 365 days: No trades in the last 365 days'. The fold reached the trend and not the chart object's markers.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "RIV-tl-1 J1: a dialog's trade list agrees with its chart's markers and with the buying section above it. RIV-co-1: each marker equals a trade of the fund in that security. Round 20 (RIV-bk-1, row Z-S61): the trend stage takes the parsekey, so one key per security.",
    "world_is": "charts/GQGU.json, round 19 against round 21 (same day 2026-10-06, live inputs): keys 66 to 59; total markers 655 to 569; the difference is exactly the 86 markers of 037833100 (12), 30303M102 (20), 512807306 (9), 532457108 (10), 595112103 (9), 718172109 (19) and 91324P102 (7). Their Bloomberg keys AAPL, META, LRCX, LLY, MU, PM and UNH _US_Equity hold 0 markers in both runs.\n- In the browser on the round-21 page: AAPL tile '+$43.9m net bought across 12 trades', strip lit Jul, Aug, Sep, list 'No trades in the last 365 days'; PM tile '-$31.5m net sold across 19 trades', strip lit in 8 months, list 'No trades'.\n- The list still agrees with the object (695 of 695) because the object itself lost the markers.\n- Cause not read by this seat: the markers come from the trade schedule, which this fold did not re-key.\n- Nothing of this is served; it ships with the round-15+ deploy as built, the first time the vehicle runs the new trend stage.\n- Not measured: whether the audit page's trade log keeps these trades under the CUSIP key.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "C:/tmp/rv-r21-realrun/layer/ charts/GQGU.json and C:/tmp/rv-r19-realrun/layer/ charts/GQGU.json on site Z, read 2026-10-07 ~14:30Z",
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round21/DRAIN_END_PACKET.round21.md @dc23ed5ae9",
        "investigations/INVESTIGATION_v1.Z.md ETFS_RIVALS-Z-S57, ETFS_RIVALS-Z-S61"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV

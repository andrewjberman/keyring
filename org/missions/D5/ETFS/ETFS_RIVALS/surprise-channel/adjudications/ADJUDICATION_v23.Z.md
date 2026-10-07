# ETFS_RIVALS -- round 22 L8/L9 on the final round-22 real run, in a browser (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~16:20Z. Packet: COO~RV msg 31135 (@a8e3357abc); CTO~Z msg 31138. Nothing of rounds 15
to 22 is deployed.

**pm-1 J1: MET. C-S64 (the lost markers): REMEDIATED on the real run -- 0 markers lost in 13 of 13 funds, 46 gained.
Not checked by this seat: the gained markers against the trade schedule (the issuer's read).**

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S65",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T16:20:00Z",
    "one_line": "Round 22 L9 on the issuer's final round-22 real run (local, not served), in a browser: RIV-pm-1 J1 MET on its five limbs, and row C-S64 is repaired. No non-zero marker of the run before the fold is missing in any of the 13 funds (0 lost, 46 gained); GQGU holds 690 against 655. 0 dialogs show a buying section with trades above a list with no trade.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "RIV-pm-1 J1: a reader can tell the strip's first month is partial; a security shown under one key lists every trade the fund made in it; a dialog with no curve says why and still lists its trades; no marker is a zero-dollar trade; a page-day trade is on the list and at the chart's right edge. C-S64's proof (CTO msg 31031; msg 31138).",
    "world_is": "Object: C:/tmp/rv-r22c-realrun/layer/ on site Z, the run from merged CLOUD 23d65887ca (index.html 1,695,878 B, sha256 49d3a36596ed84f0...; 695 frames, 695 object keys, 0 page errors). This seat first read C:/tmp/rv-r22-realrun/, which is the issuer's run from before its strip fix (12-column grid, 180 strips wrapping to a second row); those readings are discarded and every figure here is from the final run.\n- Part month: 393 of 393 strips flag their first cell and no other; its label carries an asterisk ('Oct 25*') and the strip is followed by '* part month: the window starts inside it'. 393 of 393 strips sit on one row (the 13-cell ones included).\n- One key, every trade: marker content (side, start, end, dollars) of the round-19 run, the run before the fold, against this run, zero-dollar markers left out of both: lost 0 in each of 13 funds; gained BASG 10, GQGU 35, IDVZ 1, the other 10 funds 0. GQGU's 7 folded names are no longer under two keys. Names under two keys in one fund: 6, each a different listing (Samsung common and preferred, Tencent and Alibaba Hong Kong line and ADR in BIDD; Roche's two share classes in CGIC, SCHY, TXUE).\n- Whether the 46 gained markers are true trades was not checked by this seat: the ruler is the trade schedule, and that read is the issuer's (CTO msg 31138: per fund, markers against the schedule for the window, the gained ones named). 3 of the 46 are page-day markers.\n- No curve says why and lists trades: 100 of 695 frames draw no curve at 365d. 98 read 'No price history is stored for this holding yet.'; 2 (CNR CN in IDVZ and CGIC, 1 price) read 'Fewer than two prices on file in this range.' under the count line. 99 of the 100 list their trades below; the 100th (INEQ ASSAB SS) has no markers and says 'No trades in the last 365 days'. The list agrees with the object's markers in 695 of 695 frames.\n- Zero-dollar markers: 0 in the 13 objects.\n- Page day: 3 frames hold a marker ending after the object's asof (GQGU 05464C101, GQGU 857477103, IDVZ TKOMY); each is on its list and its circle sits at 0.987 of the chart's width, the rightmost mark.\n- Row Z-S59: the issuer reads 389 of 393 strips agreeing with the markers' months and 4 by-design part-month cases; this seat did not re-measure it on this run.\n- md-1 J1 and pd-2 J1 stay owed on the served page. Nothing of rounds 15 to 22 is deployed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round22/DRAIN_END_PACKET.round22.md @a8e3357abc",
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round22/marker_proof_2026-10-06.json @a8e3357abc (the issuer's 86 of 86)",
        "C:/tmp/rv-r22c-realrun/layer/ and C:/tmp/rv-r19-realrun/layer/ chart objects on site Z, read 2026-10-07 ~16:10Z",
        "adjudications/ADJUDICATION_v22.Z.md ETFS_RIVALS-Z-C-S64 @37c17c640c"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV

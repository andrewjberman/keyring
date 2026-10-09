# ETFS_RIVALS -- round 28 WORKSTREAMS 2 and 3 (first issuance) L9 (dell1 fabric)

Author: 3.0.0_SA_CVO~RV1, 2026-10-09 ~07:30Z. Packet: 2.0.0_SA_COO~V1 msg 1961,
`deliverables/2.0.0_SA_COO~V1/ws2/L8_PACKET_WS2_WS3.md` @fde80f8b5d. Artifact: the issuer's local real run of page date
2026-10-08 served at http://127.0.0.1:8765/rivalfunds/2026-10-08 (nothing deployed), opened in a browser (Playwright) by
this seat.

**RIV-wc-1 J1 MET. RIV-wc-2 J1 MET. RIV-wd-1 J1 NOT MET (the repeat clause; the other two clauses MET). RIV-wa-1 J1 HELD:
its face names "the first page published with this code", and no page is published yet (WS2 guard 1).** RIV-wb-1 has no
judgment criterion. This is the L9 record only: the round-28 L10 slug waits on tw-1 J1 (11:00Z vehicle run), aw-1 J1
(13:00Z sweep) and row D1-W26-S1 (ARMED).

**ADDENDUM 1 (~09:05Z, on packet ADDENDUM 1 @d7868190de): RIV-wd-1 J1's repeat clause NOT MET -> HELD for the first page rendered
with RIV-wf-1; row D1-C-S2 says what that page must show.**

**ADDENDUM 2 (~11:40Z, on the 2026-10-09 11:00Z vehicle run, COO~V1 msg 2341): RIV-tw-1 J1 MET; RIV-tc-1 J1 NOT MEASURED (tc-1
unmerged at the run). Row D1-C-S3.**

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
  },
  {
    "id": "ETFS_RIVALS-D1-C-S2",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~RV1",
    "surfaced_at": "2026-10-09T09:05Z",
    "one_line": "On packet ADDENDUM 1 (@d7868190de, msg 2146): RIV-wd-1 J1's repeat clause moves from NOT MET to HELD for the first page rendered with RIV-wf-1. Even on wf-1's own figures, the calendar labels REQUESTED days and the trade windows are dated by the REPORT'S as-of day, so 10-02 still reads repeat beside a window ending 10-02 that carries a trade.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "wd-1 J1: no trade sits on a day the calendar marks repeat. ADDENDUM 1: on wf-1's calendar (CGIC 10-05/06/07 new, 10-01/02 repeat) the clause can be graded MET.",
    "world_is": "- The local page at http://127.0.0.1:8765/rivalfunds/2026-10-08/audit was re-read at 08:58Z (Playwright). Its files are dated 08:37Z, BEFORE the wf-1 merge 451b193828 (08:50:36Z). The CGIC calendar still reads 10-01, 10-02, 10-05 and 10-06 repeat and 10-07 gap. No rendered artifact of wf-1 exists to grade, and the wf-1 local calendar run is described in the packet but has no committed record.\n- wf-1's code (gold_holdings_coverage.py at 451b193828) still classifies 'per expected day', meaning the requested day: 'repeat / regressed / gap / periodic per expected day'. The trade windows are dated by the report's claimed as-of (row D1-S7). On wf-1's stated figures, expected day 10-02 is 'repeat' (that capture claims 09-30), while the window '2026-09-30 to 2026-10-02 (1 trade)' (TSM trim) ends on the as-of 10-02 report, which was captured on expected day 10-05 ('new'). The trade is real, but the page shows a trade window ending 10-02 beside a 10-02 column marked repeat. As worded, the clause would read NOT MET on the rebuilt page unless the calendar says which day its columns are or is keyed by the as-of date.\n- Grade: HELD for the first page rendered with wf-1. The grade turns on what the page shows a reader: either the two date axes are shown as different, or no repeat-marked day coincides with a window end that carries a trade.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~V1/ws2/L8_PACKET_WS2_WS3.md ADDENDUM 1 @d7868190de",
        "git diff 451b193828^1 451b193828 -- data/etfs/scripts/rivalfunds/gold_holdings_coverage.py (classify(prev_actual); docstring 'per expected day')",
        "C:/tmp/ws2-real-run/layer/opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-08/audit.html mtime 08:37Z; Playwright read 08:58Z",
        "surprise-channel/investigations/INVESTIGATION_v1.dell1.md ETFS_RIVALS-D1-S7"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-D1-C-S3",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~RV1",
    "surfaced_at": "2026-10-09T11:40Z",
    "one_line": "Round 28 L9 on the 2026-10-09 11:00Z vehicle run: RIV-tw-1 J1 MET. The run REACHED the enrichment leg (STEP line 170, EXIT 94 'landed' line 172, 0 vendor-session-failure lines) with tw-1's code in site Z's tree and the switch unset, and printed 0 HISTORY OWED lines. RIV-tc-1 J1 NOT MEASURED: tc-1 was not merged before this run, so its 'first REACHED run after the merge' is still to come.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "tw-1 J1 (AMENDMENT 1): read on the first scheduled vehicle run that REACHED the enrichment leg (STEP line, enrichment exit other than 97, no vendor-session-failure line); the enrichment leg's lines and exit code are unchanged with the switch unset. tc-1 J1 (AMENDMENT 2): the same read, on the first REACHED run AFTER tc-1's merge.",
    "world_is": "- Transcript origin/box/sitez:deliverables/0.0.3_BG_BBGTerminal/VEHICLE_LOG_20261009_1100Z.txt @2a0a40bfe4 (50 lines; it quotes the source log bbg_tplus1_20261009_070014.log, 14,020 bytes, 172 lines, source sha256 8aa0479677c2...). Lines 169-172 of the source: bloomberg leg EXIT 90 'landed, batch whole'; 'RIVALFUNDS ENRICHMENT STEP (RIV-e-1)'; EXIT 94 '-- landed.' The vendor-failure selector finds 0 lines and /HISTORY OWED/ finds 0 over the whole file. The transcript does not show source line 171.\n- REACHED: STEP present, exit 94 (not 97), no failure line. This is the first REACHED run since the tw-1 merge: the 2026-10-08 run was exit 97 with 17 failure lines.\n- tw-1 was in the code: its tip de25db03ea is an ancestor of origin/box/sitez and of origin/CLOUD. At box/sitez's last commit before 11:00Z (b28e2c4932, 10:59:17Z), enrichment_bloomberg.py carries RIVALFUNDS_HISTORY_OWED (tw-1, f30d8018b2) and main()/__main__ (:1190, :1222; row Z-S10's fix). INFERRED, not measured: the vehicle runs site Z's WORKING tree, and this seat read the committed tree.\n- 'Unchanged': the only pre-tw-1 REACHED baseline on record is 2026-10-01 (row Z-S10), exit 94 'landed'. Today's exit is the same 94, now with a real entry point behind it. The module prints a 'HISTORY OWED:' line only on the switched-on path (:917, :937, :1002), and the log has none. So the leg's lines and exit are unchanged with the switch unset. MET.\n- tc-1: its branch tip b0b65368fb is on neither origin/box/sitez nor origin/CLOUD, and at b28e2c4932 HISTORY_OWED_CAP reads 5000 (:901), where tc-1 item 6 sets 20000. tc-1 was unmerged at the run. NOT MEASURED; it is read on the first REACHED run after its merge.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "origin/box/sitez:org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.0.3_BG_BBGTerminal/VEHICLE_LOG_20261009_1100Z.txt @2a0a40bfe4",
        "task-orders/ETFS_RIVALS.TO-RIV-tw-1...md:88 (J1 + AMENDMENT 1); TO-RIV-tc-1...md:89 (J1 + AMENDMENT 2), :47 (item 6, cap 20000)",
        "git merge-base --is-ancestor: de25db03ea in origin/box/sitez and origin/CLOUD; b0b65368fb in neither",
        "data/etfs/scripts/rivalfunds/enrichment_bloomberg.py @b28e2c4932 :901, :917, :937, :1002, :1190, :1222",
        "surprise-channel/investigations/INVESTIGATION_v1.Z.md ETFS_RIVALS-Z-S10 (2026-10-01 exit-94 baseline)",
        "2.0.0_SA_COO~V1 msg 2341"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV1

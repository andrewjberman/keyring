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

**ADDENDUM 3 (~13:30Z, on the 2026-10-09 13:00Z sweep, COO~V1 msg 2460): RIV-aw-1 J1 NOT MET on the plain-English clause
(the counted clauses MET; 4 of 26 items carry '$0.0 million' or a CUSIP). Row D1-C-S4.**

**ADDENDUM 4 (~13:45Z, on COO~V1 msg 2488): RIV-wg-1 J1 MET on the issuer's real 13-fund run (a1-chain/8); the name-abstracted
frame still repeats (6 of 13) -- a round-29 item. Row D1-C-S5.**

**ADDENDUM 5 (~14:20Z, on COO~V1 msg 2526): RIV-wh-1 J1 MET (0 '$0.0 million', 0 bare identifiers over 26 items, real run
a1-chain/8). Row D1-C-S6.**

**ADDENDUM 6 (2026-10-11 ~02:10Z, on COO~V1 msg 3041): RIV-tc-1 J1 NOT MEASURED -- the 2026-10-10 11:00Z vehicle run has
no transcription at origin/box/sitez or origin/CLOUD, so nothing is graded. Row D1-C-S7.**

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
  },
  {
    "id": "ETFS_RIVALS-D1-C-S4",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~RV1",
    "surfaced_at": "2026-10-09T13:30Z",
    "one_line": "Round 28 L9 on the 2026-10-09 13:00Z sweep: RIV-aw-1 J1 NOT MET on its plain-English clause. Every counted clause holds: 0 period codes, both dates stated in 26 of 26, all 146 dollar figures in the text matched to a cited value. But 4 of 26 items read wrong to a portfolio manager: 7 '$0.0 million' trades (WCMG x2 items, ETFT) and a bare CUSIP standing in for Apple (GQGU).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "aw-1 J1: on the first 13:00Z sweep after the deploy, the 26 served account items carry 0 period codes and state their two dates, and every dollar figure in them is cited (the issuer's count); the accounts read as plain English to a portfolio manager. Its prompt (a1-chain/7 SYSTEM) forbids 'a code, a key, a fact id or a short form'.",
    "world_is": "- Artifact: s3://opal-data-etfs/rivalfunds/etfs/gold/research_hypotheses/date=2026-10-09/research_hypotheses-20261009T130227Z-ai.parquet. It is the only object under the prefix, read by this seat 13:2xZ as cloudops-dell1-agent-user: 26 rows, prompt a1-chain/7, grounding PASS 26 of 26.\n- Counted clauses, this seat's own reads: the issuer's counts (COO~V1 msg 2460, round28/sweep_read.py) give 0 of 26 with a period code and 26 of 26 stating two ISO dates. Dollar citation, which the issuer's reader does not count: this seat matched every '$<n>[ million|bn|k]' in `text` against the abs values in that item's cited_rows (value + values), within the shown rounding. 146 figures, 0 unmatched. Positive control: a planted '$9.7 million' on IDVZ/activity_30d is flagged.\n- Plain English, all 26 texts read in full. Most read as a portfolio manager would want, with names, signs, periods in words and the dated range stated once. Defects in 4 items: WCMG/activity_30d 'trimmed Valero Energy Corp by $0.0 million and Wuxi Biologics Cayman Inc by $0.0 million'; WCMG/direction_verdict 'even after a $0.0 million trim'; ETFT/activity_30d 'trimmed Meta Platforms Inc by $0.0 million', 'trimmed Netflix Inc twice by $0.0 million and $0.0 million', 'each at $0.0 million' (7 instances). The million unit rounds these two small funds' trades to zero, so a sold position reads as a trade of nothing. GQGU/activity_30d 'the fund added 037833100 for $8.1 million': Apple's CUSIP where the name belongs, the identifier class the prompt forbids.\n- Observations, not graded here: (a) row D1-S8 (all 13 Direction Verdicts open 'From <date> to <date>'), RIV-wg-1's remedy, confirmed 13 of 13. (b) Five Direction Verdicts that speak of 'the last 365 days' state a range starting later than a year back: IDVZ and PFOE 2026-01-02, WCMG 2026-04-23, ETFT 2025-12-02, PCLG 2025-10-16. The dates are the data's true start, but the words claim a full year.\n- Remedy owners: the unit choice for small funds and the identifier leak are the issuer's to place (a WS3 cell or round 29); this seat cuts nothing.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-etfs/rivalfunds/etfs/gold/research_hypotheses/date=2026-10-09/research_hypotheses-20261009T130227Z-ai.parquet (26 rows; text, cited_rows)",
        "task-orders/ETFS_RIVALS.TO-RIV-aw-1.ai-accounts-name-periods-in-words-and-cite-every-figure.md:100 (J1)",
        "deliverables/2.0.0_SA_COO~V1/round28/sweep_read.py (the issuer's counts); COO~V1 msg 2460",
        "surprise-channel/investigations/INVESTIGATION_v1.dell1.md ETFS_RIVALS-D1-S8"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-D1-C-S5",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~RV1",
    "surfaced_at": "2026-10-09T13:45Z",
    "one_line": "RIV-wg-1 J1 MET on the issuer's real 13-fund run (a1-chain/8, local writes). By the face's instrument, no raw opening leads more than once, and every verdict leads with and argues from its own fund's securities and trades. Observation for round 29: with the name abstracted, the frame '<name> is the clearest ... tell/signal' leads 6 of 13 (over a quarter); the template moved one slot, it did not go.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "wg-1 J1 (task order :50-52): on the issuer's real run over the 13 funds, no opening leads more than a quarter of the verdicts (verdict_openers_check.py), and the verdicts read as fund-specific.",
    "world_is": "- Artifact: deliverables/2.0.0_SA_COO~V1/round28/WG1_J1_REAL_RUN_20261009.md @597396eea6. It holds the 13 Direction Verdicts verbatim from run 20261009T132214Z-ai, prompt a1-chain/8, merged code @3bd0c7c023, local writes only, grounding PASS 26 of 26 with 0 corrections. Not served; this seat read the record, not a page.\n- Opening clause: this seat's census of the 13 texts (first four tokens, dates as one token) gives the most shared opening x1 of 13. That is within the quarter (3.25), matching the issuer. The served a1-chain/7 run read 'from <date> to <date>,' x13 (row D1-S8). MET.\n- Fund-specific clause: every verdict opens on a security from its own fund (Petrobras for IDVZ, Orange for TXUE, SK hynix for BIDD, Vinci for SCHY, Hermes for PFOE, SpaceX's new entry for GQGU, Amazon's trim for BASG, AppLovin for ETFT, Meta for PCLG). The body argues from that fund's own ranks and trades, and no verdict could be swapped onto another fund. MET.\n- Observation (not a fail; the face binds the opening measure to its instrument): abstracting the security name, 'is the clearest ...' leads 6 of 13, 'is the most particular ...' 4 and 'stands out ...' 4. Two frames exceed a quarter, and six verdicts (IDVZ, TXUE, INEQ, SCHY, PFOE, WCMG) literally say 'fund-specific', echoing the prompt. A portfolio manager reading the 13 together meets one sentence pattern. For round 29: vary the frame, or grade it with the name abstracted.\n- Carried, not re-graded here: '$0.0 million' appears again in WCMG ('leaned away by $0.0 million', 'leaned into by $0.0 million over 2 windows', 'a trim of $0.0 million') and in ETFT (3x). That is row D1-S9, the same defect as aw-1's NOT MET (row D1-C-S4). The 'last 365 days' wording beside a later stated start persists for IDVZ, PFOE, WCMG, ETFT and PCLG (D1-C-S4 (b)).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round28/WG1_J1_REAL_RUN_20261009.md @597396eea6",
        "task-orders/ETFS_RIVALS.TO-RIV-wg-1.direction-verdict-fund-specific-lead.md:50-52 (J1)",
        "2.0.0_SA_COO~V1 msg 2488",
        "surprise-channel/investigations/INVESTIGATION_v1.dell1.md ETFS_RIVALS-D1-S8, ETFS_RIVALS-D1-S9"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-D1-C-S6",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~RV1",
    "surfaced_at": "2026-10-09T14:20Z",
    "one_line": "RIV-wh-1 J1 MET on the issuer's real 13-fund run (a1-chain/8, local writes): 0 '$0.0 million' and 0 bare identifiers across the 26 items. Small notionals now read in thousands, and one cross-checks against the page: WCMG's Valero trim '$37 thousand' equals the $37,136 sale in this seat's 07:2xZ dialog read. This repairs the plain-English defect behind aw-1's NOT MET (D1-C-S4) in the code; the served page carries it only after the WS2/WS3 deploy.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "wh-1 J1 (task order :43): on the issuer's real 13-fund run, 0 '$0.0 million' and 0 bare identifiers in any item.",
    "world_is": "- Artifact: deliverables/2.0.0_SA_COO~V1/round28/WH1_J1_REAL_RUN_20261009.md @8da1582b50, 26 items verbatim from run 20261009T140542Z-ai, prompt a1-chain/8, box/dell1 @b48273e3d0 (wh-1 merged @eeba3cad15), local writes only. Not served.\n- This seat's census over the item section only (the record's header table quotes the served run's '$0.0 million' and '037833100', and a whole-file count reads 1 and 1 from that table): '$0.0 million' 0; tokens shaped like a CUSIP, an ISIN or '<ticker>_<cc>_Equity' 0; '$0 thousand' 0; ' thousand' 15 in the item texts. The issuer's 35 may count fields beyond `text`; the record holds text only. GQGU now names 'Apple Inc' where the CUSIP stood. MET.\n- Cross-check of a converted figure: WCMG activity_30d and direction_verdict read 'trimmed Valero Energy Corp by $37 thousand'. The page dialog this seat read at 07:2xZ (D1-C-S1) showed 'Sold between 2026-09-03 and 2026-09-08: $37,136'. Consistent.\n- Still open, not in this J1: aw-1's served NOT MET stands until a 13:00Z sweep runs this code. The name-abstracted Direction Verdict frame (D1-C-S5) and the 'last 365 days' wording beside a later start (D1-C-S4 (b)) are unchanged.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round28/WH1_J1_REAL_RUN_20261009.md @8da1582b50",
        "task-orders/ETFS_RIVALS.TO-RIV-wh-1.small-notional-and-unnamed-facts.md:43 (J1)",
        "2.0.0_SA_COO~V1 msg 2526",
        "this file, ETFS_RIVALS-D1-C-S1 (Valero dialog read) and ETFS_RIVALS-D1-C-S4"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-D1-C-S7",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~RV1",
    "surfaced_at": "2026-10-11T02:10Z",
    "one_line": "RIV-tc-1 J1 NOT MEASURED on the 2026-10-10 11:00Z vehicle run (the run COO~V1 msg 3041 names): neither VEHICLE_LOG_20261010_1100Z transcription exists at origin/box/sitez 2395612d25 or origin/CLOUD 733875cf2c, so there is no log to grade. The issuer's reader on the 2026-10-09 file reads REACHED at both refs, so the empty read is an absent file, not a broken reader. J1 is read on the first transcribed REACHED run after the merge.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "tc-1 J1 (AMENDMENT 2): read on the first scheduled vehicle run after the merge that REACHED the enrichment leg; the leg's lines and exit code are unchanged with the switch unset. COO~V1 msg 3041: that read is on the 2026-10-10 11:00Z run, via round28/tw1_j1_read.py <ref> 20261010, on that day's transcription.",
    "world_is": "- Merge: tc-1 tip b0b65368fb is an ancestor of origin/box/sitez 2395612d25 and origin/CLOUD 733875cf2c (merge-base --is-ancestor, read 02:08Z). enrichment_bloomberg.py :901 at origin/box/sitez reads HISTORY_OWED_CAP = 20000 (tc-1 item 6). This is the committed tree; the vehicle runs site Z's WORKING tree, which this seat cannot read.\n- Subject: `python tw1_j1_read.py origin/box/sitez 20261010` and `... origin/CLOUD 20261010` each print 'J1-READ: NO-FILE'. ls-tree of deliverables/0.0.3_BG_BBGTerminal/ at origin/box/sitez lists only VEHICLE_LOG_20261009_1100Z.txt, and deliverables/0.7.0_AE_CloudOps~ZV/ holds no 20261009 or 20261010 vehicle log.\n- Positive control: the same reader on 20261009 at both refs prints REACHED (50 lines, STEP 1, EXIT 94 'landed', 0 failure lines, 0 HISTORY OWED lines). That is ADDENDUM 2's run and pre-dates the merge.\n- Did the run fire? DESIRED yes: register_daily_task.ps1:62 sets a -Daily trigger, and on a Saturday the vehicle runs for Friday 2026-10-09, a trading day. APPLIED is not read: the task's run record and log live on the terminal machine, which is outside this seat's reach. Whether the run fired and was not transcribed, or did not fire, is not distinguished here.\n- Owed: a transcription of the 2026-10-10 log, or of the next REACHED run after it, by 0.0.3_BG_BBGTerminal (it wrote the 10-09 file on a relayed ask), asked for by the issuer 2.0.0_SA_COO~V1. This seat grades it when the file lands.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round28/tw1_j1_read.py, run at origin/box/sitez 2395612d25 and origin/CLOUD 733875cf2c for 20261010 (NO-FILE) and 20261009 (REACHED)",
        "task-orders/ETFS_RIVALS.TO-RIV-tc-1...md:89 (J1 + AMENDMENT 2), :47 (item 6, cap 20000)",
        "git merge-base --is-ancestor b0b65368fb origin/box/sitez and origin/CLOUD: both true",
        "integrations/bloomberg/pipeline/register_daily_task.ps1:62 (-Daily trigger)",
        "2.0.0_SA_COO~V1 msg 3041; this file, ETFS_RIVALS-D1-C-S3"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV1

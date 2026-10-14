# ETFS_RIVALS -- round 29 L9 (dell1 fabric)

Author: 3.0.0_SA_CVO~RV1, 2026-10-14 ~13:40Z. Packet: 2.0.0_SA_COO~V1 msg 4876,
`deliverables/2.0.0_SA_COO~V1/round29/ROUND29_CLOSE_PACKET.md` @76190e0167. Artifact: the 2026-10-14 13:00Z sweep page,
s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-14/ (manifest generated_at 13:11:53Z, runtime
etfs-rivalfunds-daily-lambda, batch ai-2026-10-14-1c6ff3d3, 13 of 13 funds updated), fetched by this seat and rendered in
Playwright from 127.0.0.1:8767. This is the first sweep on pin de3c6bf211: both lambdas that wrote the partition read
LastModified 2026-10-13 13:59Z (the R29 deploy), and the 10-13 page was written 13:08Z, before it.

**RIV-xa-1 J1 NOT MET. RIV-xc-1 J1 NOT MET.** Both builds match their cells. Each J1 asks for more than its cell's interface
can deliver, so the gap belongs to the cut, not to either worker. Rows D1-C-S19 and D1-C-S20. These are round 29's two
judgment criteria, so every round-29 J1 now has a terminal grade.

- **xa-1:** the sentence is on the page once, visible, in the legend at the top of the trades section (render.py:2471). The
  calendars for BIDD, CGIC and SCHY render 13,384, 19,461 and 20,425 px below it, at the end of each fund's article. With
  any of them centred in a 720 px viewport, the legend is off screen. The cell (task order :33-36) fixed the sentence in
  that one paragraph and put `render._calendar` out of bounds, so "beside the calendar" could not be built from that
  interface.
- **xc-1:** by `frame_of` itself, one frame is shared: SCHY and PCLG, `<name> clearest fund-specific tell is`. PCLG carries
  1 correction. By this seat's measure, the one ADDENDUM 4 used on round 28 (the security name abstracted, the head read up
  to the superlative), IDVZ and TXUE share `<name> is the clearest ... tell`, and both carry 0 corrections. The five-token
  window splits them at token 5 (`fund-specific` against `tell:`). The template moved one slot again. The repetition still
  fell, though: the largest frame family went from 5 of 13 on the 10-13 page to 2 of 13 here.

```json
[
  {
    "id": "ETFS_RIVALS-D1-C-S19",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~RV1",
    "surfaced_at": "2026-10-14T13:40Z",
    "one_line": "ETFS_RIVALS.TO-RIV-xa-1.visible-axis-line J1 NOT MET on the 2026-10-14 13:00Z sweep's audit page, the first on pin de3c6bf211. The sentence is visible once, in the legend at the top of the trades section. The BIDD, CGIC and SCHY calendars render 13,384 to 20,425 px below it, so it does not read beside them. The build matches its cell, which fixed the sentence in that paragraph and put render._calendar out of bounds.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "xa-1 J1 (task order :38-39): on the next published audit page the sentence reads beside the calendar for BIDD, CGIC and SCHY. The cell's interface (:33-36): the sentence goes after 'HOME = home producer.' in the same <p class=\"muted\">, with render._calendar out of bounds.",
    "world_is": "- Page: s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-14/audit.html, 1,206,490 bytes (manifest audit_bytes), written by the 13:00Z sweep (generated_at 13:11:53Z). An earlier 10-14 partition, written 11:06:05Z by rivalfunds-publish-page-lambda off the 07:00 ET holdings marker, also carried the sentence once. The COO named the 13:00Z page, so that is the one graded.\n- Bytes: the full sentence is present once, in '#trades > p.muted' (render.py:2471 at HEAD, which equals the pin for this file). It is in none of the BIDD, CGIC or SCHY <article> elements. Each article holds one calendar table (data-days 20).\n- Render (Playwright, 1280x720, served from 127.0.0.1:8767): the legend is visible at y=512 (display block). The BIDD calendar is at y=13,963, CGIC at y=20,040 and SCHY at y=21,004. That puts them 13,384, 19,461 and 20,425 px below the legend, at the end of each article after all its trade windows. The page has no fund switch: all 13 articles render stacked. With each calendar scrolled to centre, the legend is not in the viewport (3 of 3). The nearest text above each calendar is that fund's 'Left out of the trades shown' line. The BIDD calendar today marks 10-01, 10-02 and 10-08 'repeat', with no legend in view. Screenshot: this seat's scratchpad, xa1_bidd_calendar_20261014.png (not committed).\n- Cause: the cut. The cell fixed the sentence in the section legend and put _calendar out of bounds. The worker built it as cut (AC1 and AC2 pass). A sentence beside each calendar needs a change in or next to render._calendar, or a legend repeated per article.\n- Not done: the page was rendered locally from the served bytes, not at the production URL.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-14/audit.html and manifest.json, fetched 13:14Z and rendered by this seat 13:15Z",
        "data/etfs/scripts/rivalfunds/render.py:2471",
        "task-orders/ETFS_RIVALS.TO-RIV-xa-1.visible-axis-line.md:33-39",
        "aws lambda get-function etfs-rivalfunds-daily-lambda and rivalfunds-publish-page-lambda: LastModified 2026-10-13T13:59Z",
        "deliverables/2.0.0_SA_COO~V1/round29/ROUND29_CLOSE_PACKET.md @76190e0167; 2.0.0_SA_COO~V1 msg 4876; this channel's ADJUDICATION_v1.dell1.md ETFS_RIVALS-D1-C-S15"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-D1-C-S20",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~RV1",
    "surfaced_at": "2026-10-14T13:40Z",
    "one_line": "ETFS_RIVALS.TO-RIV-xc-1.verdict-opening-frame J1 NOT MET on the 2026-10-14 13:00Z sweep page. By this seat's measure, IDVZ and TXUE open in one frame ('<name> is the clearest ... tell'), and neither verdict carries a correction. frame_of's five-token window splits them at token 5. Four frame families are shared in all, and the largest has 2 of 13 openings, down from 5 of 13 on 10-13.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "xc-1 J1 (task order :52-54): on the next sweep page no two openings share a frame by the CVO's own measure, or a correction is on the record for each that did. The CVO's measure is ADDENDUM 4 / row D1-C-S5: the security name abstracted, the opening's head read up to its superlative ('is the clearest ...', 'is the most particular ...', 'stands out ...').",
    "world_is": "- Rows: s3://opal-data-etfs/rivalfunds/etfs/gold/research_hypotheses/date=2026-10-14/research_hypotheses-20261014T130234Z-ai.parquet (the only object), run 20261014T130234Z-ai, prompt a1-chain/8, 26 rows, 13 direction_verdict. 13 of 13 openings are on the served index.html (TSEL's renders NVIDIA Corp as 'Nvidia Corp'). ai_accounts.py at HEAD equals pin de3c6bf211 (git diff empty).\n- frame_of (ai_accounts.py:538, the code's own instrument): 12 distinct frames over 13. One frame is shared: SCHY and PCLG, '<name> clearest fund-specific tell is'. PCLG is later in universe order and carries corrections=1. So one correction was sent and its reply still holds the shared frame, as the cell allows (one correction, the reply stands).\n- This seat's measure: four families are shared. (1) '<name> is the clearest ... tell': IDVZ ('is the clearest fund-specific tell') and TXUE ('is the clearest tell'), corrections 0 and 0. (2) \"<name>'s clearest fund-specific tell is\": SCHY and PCLG, 1 and 1. (3) \"<name>'s most distinctive ... move\": BIDD and CGIC, 1 and 1. (4) '<name> is the most <adj> signal|tell': INEQ ('particular'), GQGU ('fund-specific') and TSEL ('revealing'), all 0. Family (4) is shared only if the adjective is read as a slot; ADDENDUM 4 kept 'particular' as part of its frame. Family (1) carries no correction on either verdict whichever way (4) is read, so J1 is NOT MET.\n- Why frame_of missed (1): its frame is the first five tokens. '<name> is the clearest fund-specific' and '<name> is the clearest tell:' differ at token 5, so one inserted adjective makes a new frame. Round 28's observation (D1-C-S5) named this move: 'the template moved one slot, it did not go'.\n- The correction record: input_manifest carries a correction COUNT only (keys attached_figures, corrections, day, facts, model, run_at, run_path), never its reason. 8 of 13 verdicts carry corrections=1. A frame correction cannot be told from a wording or figure correction from the stored rows.\n- Improvement (measured, not graded): on the 10-13 page (pre-pin run 20261013T130018Z-ai), frame_of shared 4 frames across 9 of 13 verdicts, and this seat's measure put 5 of 13 in '<name> stands out most:'. Here frame_of shares 1 frame across 2 verdicts, and the largest family under this seat's measure is 2 of 13 (3 if (4) counts).\n- Not graded here: aw-1's 10-13 re-read (round29/AW1_REREAD_20261013.md @b43a093fc7). The packet files it as 'not a grade'.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-etfs/rivalfunds/etfs/gold/research_hypotheses/date=2026-10-14/research_hypotheses-20261014T130234Z-ai.parquet, read 13:14Z by this seat's reader (scratchpad xc1_read.py; it imports ai_accounts.frame_of)",
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-14/index.html (1,726,124 bytes, manifest index_bytes)",
        "data/etfs/scripts/rivalfunds/ai_accounts.py:538, :653-654, :674-675",
        "task-orders/ETFS_RIVALS.TO-RIV-xc-1.verdict-opening-frame.md:32-54, :110 (row D1-W37-S1 ruling)",
        "the same reader on date=2026-10-13 (run 20261013T130018Z-ai) as the pre-pin control",
        "this channel's ADJUDICATION_v1.dell1.md ADDENDUM 4 and ETFS_RIVALS-D1-C-S5; 2.0.0_SA_COO~V1 msg 4876"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV1

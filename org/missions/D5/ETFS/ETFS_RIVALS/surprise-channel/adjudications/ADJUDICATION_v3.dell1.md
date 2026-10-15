# ETFS_RIVALS -- round 30 L9 (dell1 fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-15 ~19:45Z. This seat succeeds `3.0.0_SA_CVO~RV1` on this project. Inputs: packet
`deliverables/2.0.0_SA_COO~V1/round30/ROUND30_CLOSE_PACKET.md` @7d58db9f71 (2.0.0_SA_COO~V1 msg 5618) and 2.0.0_SA_COO~RV
msg 6167, the nudge on Andrew's ask. Artifact: the 2026-10-15 13:00Z sweep page,
s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-15/ (manifest generated_at 13:09:27Z, runtime
etfs-rivalfunds-daily-lambda, batch ai-2026-10-15-bd93a9f8, 11 of 13 funds updated), plus its verdict rows. The daily lambda
reads LastModified 2026-10-14T14:53:21Z, so this is the first sweep on pin ea0e5025ac.

**RIV-xa-2 J1 MET. RIV-xc-2 J1 MET as written.** Rows D1-C-S21 and D1-C-S22. Every round-30 J1 now has a terminal grade.

- **xa-2:** the sentence sits directly above all 13 calendars, including BIDD, CGIC and SCHY, and stays in view with each one
  centred. One limb was not exercised: the production URL. mcp.opalinvest.dev/rivalfunds/2026-10-15/audit answers 302 to
  Microsoft sign-in, and this seat holds no session. The bytes graded are the S3 object that route returns unchanged
  (`infra/aws/ec2/opal-gateway/app/rivalfunds_view.py:174-194`). Their sha256 equals the manifest's `audit_sha256`.
- **xc-2:** by `frame_of` v2, the 13 openings fall into 12 families. The one shared family is BIDD and CGIC
  (`<name> stands out:`), and CGIC stores `shared_frame_with` and `frame_still_shared: true`. The criterion is met. The
  outcome it serves is not: a reader sees "<name> is the clearest ... :" open 4 verdicts and "<name> stands out most:"
  open 3. v2 splits both families. The CTO should weigh this before calling the frame work done (row D1-C-S22).

```json
[
  {
    "id": "ETFS_RIVALS-D1-C-S21",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-15T19:45Z",
    "one_line": "ETFS_RIVALS.TO-RIV-xa-2.axis-sentence-beside-every-calendar J1 MET on the 2026-10-15 13:00Z sweep's audit page, the first on pin ea0e5025ac. The day-axis sentence is the paragraph directly before each of the 13 calendars (BIDD, CGIC and SCHY among them), 6 px above it, and with each calendar centred in a 1280x720 viewport it is in view and not covered (13 of 13; 3 of 3 named). The production URL was not exercised: it redirects to Microsoft sign-in.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "xa-2 J1 (task order :38-40): on the served audit page at the production URL, after the deploy and the next 13:00Z sweep, the BIDD, CGIC and SCHY calendars each have the sentence visible in the same viewport as the calendar when the calendar is centred (3 of 3).",
    "world_is": "- Page: s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-15/audit.html, 851,149 bytes, LastModified 13:09:26Z, one version. Its sha256 30ade931...a27a equals manifest audit_sha256.\n- Bytes: the full sentence occurs 14 times. That is the section legend plus 13 `p[data-calendar-axis]`, one per `div.calwrap` (13). No calendar on this page is `unavailable`. After unescaping, each of the 13 paragraphs equals the constant's text exactly, and the legend still carries it.\n- Render (Playwright, 1280x720, the served bytes from 127.0.0.1:8767): each calendar scrolled to centre puts its paragraph at y=278-279 to 323-324 and the calendar at y=329-330 to 390. `elementFromPoint` at the paragraph's centre returns the paragraph, so nothing covers it (13 of 13). BIDD is calendar 3 at page y=14,242. In the screenshot the CGIC article also shows its 'not updated for 2026-10-15' banner (row D1-S17), and the sentence still sits above its calendar. Screenshot: this seat's scratchpad, xa2_bidd_calendar_20261015.png (not committed). The only console error is a favicon 404 from the local server.\n- Production URL: https://mcp.opalinvest.dev/rivalfunds/2026-10-15/audit (and /rivalfunds, /rivalfunds/audit.html) answer 302 to login.microsoftonline.com. The Playwright browser holds no session. The gateway route `_serve_day` (rivalfunds_view.py:174-194) fetches `audit_key(day)` and returns its body as HTML with no wrapper, so the graded bytes are the bytes that URL returns. That holds IF the deployed gateway runs this file; this seat did not read the deployed gateway.\n- Round 29 control: the 10-14 page (D1-C-S19) carried the sentence once, 13,384 to 20,425 px above these calendars.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-15/audit.html and manifest.json, fetched ~19:33Z and rendered by this seat ~19:36Z",
        "curl and Playwright at https://mcp.opalinvest.dev/rivalfunds/2026-10-15/audit: 302 to Microsoft sign-in",
        "infra/aws/ec2/opal-gateway/app/rivalfunds_view.py:174-194",
        "task-orders/ETFS_RIVALS.TO-RIV-xa-2.axis-sentence-beside-every-calendar.md:29-40",
        "aws lambda get-function etfs-rivalfunds-daily-lambda: LastModified 2026-10-14T14:53:21Z",
        "deliverables/2.0.0_SA_COO~V1/round30/ROUND30_CLOSE_PACKET.md @7d58db9f71; 2.0.0_SA_COO~V1 msg 5618; 2.0.0_SA_COO~RV msg 6167"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-D1-C-S22",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-15T19:45Z",
    "one_line": "ETFS_RIVALS.TO-RIV-xc-2.frame-families-and-stored-reason J1 MET as written on the 2026-10-15 sweep: by frame_of v2 the 13 openings fall into 12 families. The one shared family (BIDD, CGIC) has its later verdict carrying shared_frame_with and frame_still_shared. The outcome is not served: to a reader, '<name> is the clearest ... :' opens 4 verdicts (IDVZ, SCHY, BASG, ETFT) and '<name> stands out most:' opens 3 (BIDD, CGIC, TSEL). v2 splits both families, so the largest reader-visible family grew from 2 of 13 (10-14) to 4 of 13.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "xc-2 J1 (task order :47-48): on the next sweep page 13 of 13 openings fall in distinct families by the normalized frame_of, or each shared one carries a stored correction reason. Interface item 5 (:39-42): shared_frame_with names the fund the FIRST reply collided with; frame_still_shared marks a final reply that still shares.",
    "world_is": "- Rows: s3://opal-data-etfs/rivalfunds/etfs/gold/research_hypotheses/date=2026-10-15/research_hypotheses-20261015T130018Z-ai.parquet, the only object, LastModified 13:07:59Z. Run 20261015T130018Z-ai, prompt a1-chain/8, 26 rows, 13 direction_verdict. The 13 verdict texts are all on the served index.html (tag-stripped match, 13 of 13). ai_accounts.py at HEAD equals pin ea0e5025ac (git diff empty). The reader imports ai_accounts.frame_of.\n- frame_of v2: 12 distinct of 13. Shared: '<name> stands out:' for BIDD (first, corrections 0) and CGIC (corrections 1, shared_frame_with IDVZ, frame_still_shared true). So J1 holds as written.\n- CGIC's stored reason names IDVZ, the first collision. Its final reply shares with BIDD, and no stored field names BIDD. A reader of the record learns that the frame is still shared, but not with whom.\n- 7 verdicts store shared_frame_with (CGIC, INEQ, PFOE, WCMG, GQGU, ETFT, PCLG), matching the issuer's L2 read. TXUE carries corrections=1 with no shared_frame_with, so a frame correction can now be told from any other correction.\n- What a reader sees (this seat's measure, ADDENDUM 4 / D1-C-S5: the name abstracted, the head read up to its superlative). (1) '<name> is the clearest ... :': IDVZ 'clearest fund-specific signal', SCHY 'clearest fund-specific tell', BASG 'clearest positive tell', ETFT 'clearest tell in ETFT'; corrections 0, 0, 0, 1. (2) '<name> stands out most:': BIDD, CGIC, TSEL; corrections 0, 1, 0. (3) \"<fund>'s most <adj> <noun> is\": INEQ and PCLG, both corrected. TXUE's 'is the most particular signal here:' sits beside family (1).\n- Why v2 splits them. (1) The clause runs to the colon, and the slot word after 'clearest' stays in the frame: 'signal:' against 'tell:', 'positive tell:' and 'tell in <name>:'. Only fund-specific, most, single and particular are stop-listed. (2) TSEL's name 'Shopify Inc - Class A' breaks the name run at the share-class letter. 'A' is lowercased as a word, which gives '<name> a stands out:' against BIDD's '<name> stands out:'.\n- Control: v2 on the 10-14 rows (run 20261014T130234Z-ai) shares IDVZ and TXUE ('<name> is the clearest tell:') with 0 corrections, which is the case the cell was cut for. The instrument does what was ruled. On 10-14 this seat's measure put the largest family at 2 of 13 (3 if the adjective is a slot). Here it is 4 of 13.\n- Cause: the cut. The CTO's round-29 ruling 2 fixed the J1 to frame_of's families, and the worker built frame_of v2 to the cell (AC1-AC3 pass). The model moved its template into the slot v2 keeps.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-etfs/rivalfunds/etfs/gold/research_hypotheses/date=2026-10-15/research_hypotheses-20261015T130018Z-ai.parquet, read ~19:40Z by this seat's reader (scratchpad xc2_read.py; it imports ai_accounts.frame_of)",
        "the same reader on date=2026-10-14 (run 20261014T130234Z-ai) as the control",
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-15/index.html (1,719,861 bytes, manifest index_bytes)",
        "task-orders/ETFS_RIVALS.TO-RIV-xc-2.frame-families-and-stored-reason.md:29-48",
        "this channel's ADJUDICATION_v1.dell1.md ADDENDUM 4 / ETFS_RIVALS-D1-C-S5 and ADJUDICATION_v2.dell1.md ETFS_RIVALS-D1-C-S20",
        "2.0.0_SA_COO~RV msg 6167 (issuer L2 read: shared_frame_with on 7 verdicts, CGIC frame_still_shared)"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV

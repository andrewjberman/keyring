# ETFS_RIVALS -- the 2026-10-07 morning pass on the served 11:05Z page, and round 17 L9 (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~11:30Z. Morning pass: ROUND_ANALYSIS.round13.md section 3. Round 17 packet: COO~RV
msg 30839 (@b91a3695c0). Not the slug.

- **Morning pass, served 10-07 page (11:05:31Z): item 2 MET. Items 1 and 3 NOT MET on this page. Item 4 NOT READ.**
- **nc-1 J1: MET on the round-17 objects** (browser limb from the issuer's screenshot, not exercised by this seat).
- **New, C-S58: on the round-17 real run 7 GQGU securities carry two keys each.**

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S56",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T11:30:00Z",
    "one_line": "Morning pass on the served 2026-10-07 page (index.html 1,071,040 B, written 11:05:31Z, sha256 ba46d2831a...): fund_sections missing 0 of 1,225 (item 2 MET). Nebius is still two keys, N97284108 in GQGU and NBIS_US_Equity in WCMG (item 1, S43's proof: NOT MET on this page). The four C-S36 names still read as tickers (item 3 NOT MET). The page was published before the day's Bloomberg enrichment, so items 1 and 3 are re-read on the next republish.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "ROUND_ANALYSIS.round13.md section 3: (1) every merged (CUSIP/ISIN key, Bloomberg key) pair with its count, Nebius merged once in the rankings and the trend; (2) fund_sections missing 0 on the 10-07 page; (3) C-S36's four names (8053 JP, 9433 JP, RBLX US, 000270 KS) read as names; (4) the PARSEKYABLE_DES points of the run, and eb-1's bound.",
    "world_is": "Read by this seat from the S3 bytes of s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-07/ in a headless browser (no click).\n- Item 2: 13 funds, 1,225 data-sec buttons, 0 unresolved, 0 whose dialog lacks a section for the button's fund, 0 outside a fund panel. The manifest reads the same (1,225 / 0 missing).\n- Item 1: Nebius appears under 2 keys: GQGU rankings N97284108 (2 buttons), WCMG rankings NBIS_US_Equity (3 buttons). 89 of 1,225 buttons are identifier-keyed, 88 of them in GQGU.\n- Item 3: the 4 dialogs are titled '8053 JP Equity', '9433 JP Equity', 'RBLX US Equity', '000270 KS Equity'.\n- Item 4: the issuer's read; no packet for it has reached this seat.\n- The page: 9 of 13 funds updated; ai_grounding 0 served / 0 earlier (the AI step runs on the 13:00Z sweep).\n- What the next republish will likely show, from the issuer's round-17 real run on live inputs ~11:1xZ (local, day 2026-10-06, round-17 code, not the deployed code): Nebius is one key, NBIS_US_Equity, 10 buttons; RBLX reads 'ROBLOX Corp'; 8053 JP, 9433 JP and 000270 KS still read as tickers. That run also shows C-S58.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-07/index.html (LastModified 2026-10-07T11:05:31Z, 1,071,040 B, sha256 ba46d2831aca5f027a0d4a760457b27c67abf8223ecfb2d02b0c15af0eb2480a)",
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-07/manifest.json (fund_sections 1225/1225/0; funds_updated 9 of 13)",
        "org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round13.md section 3"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record of one page. Item 2 is MET. Items 1 and 3 are not gradable as final on a page published before the day's enrichment; S43 and C-S36 stay OPEN and are re-read on the first republish after it (the 13:00Z sweep's). Item 4 waits on the issuer's read. The ledger etfs-rivalfunds-pk1-al1 does not close on this page."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S57",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T11:30:00Z",
    "one_line": "Round 17 L9 on the issuer's round-17 real run (local, not served): nc-1 J1 MET on the objects. 97 of 97 fund-securities with no stored currency carry 'No price history is stored for this holding yet.' and no priced point; 0 carry 'not quoted in US dollars'. C-S54's false sentence is gone. The run holds 702 fund-securities, not 695: the live inputs moved between the two runs.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-C-S54"
    ],
    "spec_asserts": "RIV-nc-1 J1: in a browser, the dialog of a holding with no stored currency shows no chart and the sentence, and a holding with a stored currency is drawn as before.",
    "world_is": "This seat read the 13 chart objects of C:/tmp/rv-r17-realrun/layer/ against round 16's.\n- 702 fund-securities: USD 270 (market and implied), other currency 335 (334 market only, 1 with no price), no currency 97 (44 US-listed keys, 53 not). 0 implied points outside USD.\n- The 97: 97 of 97 carry the new sentence and 0 priced points. The 1 EUR security with no price keeps the 'not quoted in US dollars' sentence, which is true of it.\n- A holding with a stored currency is drawn as before: 689 of 689 keys present in both runs have identical points.\n- Browser limb: the issuer's screenshot (BASG Kla Corp, key 482480100) shows the sentence and no chart. This seat did not open a browser on this run.\n- The same screenshot shows row Z-S56 directly: the tile says 'net sold across 3 trades' and the line below says 'No trades in the last 365 days'.\n- Inputs moved between the round-16 and round-17 runs: GQGU gained 13 ticker keys and lost 5 CUSIP keys, CGIC lost 1 key, and 10 securities' marker counts changed by one. The packet's 695 is the round-16 count; its parse of 702 frames is the right count for this run.\n- pc-1 J1, pd-2 J1, md-1 J1, co-1 J1 are as graded in ADJUDICATION_v17 C-S53; md-1 J1 is graded after the Z-S56 repair cell, on the served page.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round17/DRAIN_END_PACKET.round17.md @b91a3695c0",
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round17/r17_realrun_modal_no_currency.png @b91a3695c0",
        "adjudications/ADJUDICATION_v17.Z.md ETFS_RIVALS-Z-C-S54 @ff88c0da21"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-Z-C-S58",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T11:30:00Z",
    "one_line": "On the round-17 real run (live inputs ~11:1xZ) 7 GQGU securities carry two keys each, a CUSIP key holding the trade markers and a ticker key holding none: Apple, Meta, Lam Research, Eli Lilly, Micron, Philip Morris, UnitedHealth. Round 16's run, an hour earlier, had 0. This is the wrong-merge case the morning pass names, and the next republish of the served page reads the same inputs.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "RIV-ok-1 / RIV-pk-1: one key per security. ROUND_ANALYSIS.round13.md section 3 item 1: every merged (CUSIP/ISIN key, Bloomberg key) pair with its count; a wrong merge means rollback plus one refresh.",
    "world_is": "charts/GQGU.json of the round-17 run: 66 keys, 35 identifier-form; 7 names appear under two keys: 037833100 (12 markers) and AAPL_US_Equity (0 markers, no currency); 30303M102 (20) and META_US_Equity (0); 512807306 (9) and LRCX_US_Equity (0); 532457108 (10) and LLY_US_Equity (0); 595112103 (9) and MU_US_Equity (0); 718172109 (19) and PM_US_Equity (0); 91324P102 (7) and UNH_US_Equity (0). In the same run 5 CUSIP keys merged cleanly into ticker keys (AMD, Howmet, Interactive Brokers, Oracle, ASML) and Nebius merged to NBIS_US_Equity. The round-16 run's GQGU object: 58 keys, 40 identifier-form, 0 names under two keys. Cause not established; the two runs differ in live inputs (the 11:00Z vehicle run landed between them) and by cell nc-1. Not measured: the served page after its next republish; the other 12 funds were checked on name only through the chart objects' key changes (no new ticker keys outside GQGU).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "C:/tmp/rv-r17-realrun/layer/ charts/GQGU.json on site Z (code root CLOUD 07ff6ebe34), read 2026-10-07 ~11:25Z",
        "C:/tmp/rv-r16-realrun/layer/ charts/GQGU.json on site Z (the control: 0 names under two keys)",
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round17/real_run_2026-10-06.after_nc1.json @b91a3695c0"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV

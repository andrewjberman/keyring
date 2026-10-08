# ETFS_RIVALS -- the 2026-10-08 13:00Z sweep's page: the AI accounts on the rolling periods (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-08 ~13:25Z. Not a round slug.

**R3's count: 0 of 26 accounts name a calendar period (was 20). 25 accounts 'Grounded' on the served build, 1 FAIL of its own.
Found: the accounts print the period codes R30 / R90 / R365 to the reader, 240 times.**

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S82",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-08T13:25:00Z",
    "one_line": "The 2026-10-08 13:00Z sweep's page: 0 of 26 AI accounts name a calendar period (analysis R3 expected 0), and 26 of 26 name a rolling window; 25 accounts read 'Grounded' on the served build and 1 carries a FAIL of its own (TXUE, the last 30 days); every cited contribution figure this seat parsed agrees with the panels. 13 of 13 funds are updated.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "ROUND_ANALYSIS.round22.md R3: after the 2026-10-08 13:00Z sweep the count of AI accounts naming a month-to-date, quarter-to-date or year-to-date figure is read again, 0 of 26 expected; if they still name calendar periods the prompt is the defect. RIV-ab-1 J1 on a second real day.",
    "world_is": "Read by this seat from the S3 bytes in a headless browser.\n- Manifest: status published, 13 of 13 funds updated, no failing freshness check, fund_sections 2,252 buttons / 0 missing, ai_grounding served 25 / earlier 0, the three tables SKIPPED (already built for the day) and the AI run OK.\n- Calendar periods: of 26 accounts, 0 contain MTD, QTD, YTD, 'year to date', 'month to date' or 'quarter to date'; page-wide the visible text holds 0 of those. On the page of 2026-10-07 17:47Z the same count was 20 of 26. 26 of 26 accounts name a thirty-, ninety- or 365-day window.\n- Badges: 25 PASS with data-build served, 0 earlier, 1 FAIL (TXUE: 'figures not in any cited row: $1.2 million; ambiguous figure').\n- Cited contribution figures against the ranking rows of the same fund and security: 127 of 130 equal directly; the other 3 are 'A and B ... at x and y' sentences this seat's pattern attributes to the wrong name, and by hand each agrees with its dialog (INEQ Siemens Energy -0.38% for 30 days; PFOE Broadcom +0.27%, twice). So 130 of 130. The period of a figure was matched only for those three.\n- Not looked at on this page: the chart frames (graded on the 11:06Z page, C-S81) and the audit page.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-08/index.html (generated 2026-10-08T13:08:17Z, 1,688,097 B, sha256 e08fdd70a5f74d7924ce3ff1500738f2af90bde044c1a42c7c12d184aff01f10)",
        "org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round22.md @f8a61834fd (R3)",
        "adjudications/ADJUDICATION_v24.Z.md ETFS_RIVALS-Z-C-S66 @665581ba62 (the 20 of 26)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record. R3's count reads 0 of 26, so the prompt is not the defect R3 feared; RIV-pd-3 is exercised on real data for the first time and its accounts use the rolling windows. C-S83 beside it is the one thing found."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S83",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-08T13:25:00Z",
    "one_line": "The new AI accounts show the tables' internal period codes to the reader: the visible text of the 2026-10-08 13:08Z page carries 'R30' 152 times, 'R365' 65 times and 'R90' 23 times, in sentences such as 'Petroleo Brasileiro SA - Petrobras was the top R30 contributor at +0.73%'. The page's own controls and tables say 30d, 90d, 365d and 'Last 30 days'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FWD-23 (PRD v0.18): the page offers 30d, 90d and 365d everywhere, in the reader's words. RIV-pd-3: the AI accounts are written on the three rolling periods.",
    "world_is": "Counted on the page's visible text (scripts and styles removed): 240 tokens matching R30, R90 or R365 as whole words. Within the first 1,800 characters of each account, 16 of 26 accounts carry one or more; the count per account beyond that length was not taken. The codes sit in the accounts' listed facts ('was the second-best R30 contributor', 'contributed +0.32% in R30 after an entry of $3.5 million'), while the narrative sentences above them say 'the last thirty days'. The page of 2026-10-07 used 'year to date' in words in the same place. Nothing is wrong with the figures; the label is the tables' code and not a reader's word.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-08/index.html (generated 2026-10-08T13:08:17Z, 1,688,097 B, sha256 e08fdd70a5f74d7924ce3ff1500738f2af90bde044c1a42c7c12d184aff01f10)"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV

# ETFS_RIVALS -- the morning pass re-read on the served 2026-10-06 republish of 11:14Z (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~11:45Z. Issuer's read: COO~RV msg 30843, record @b74bdc238b. Cites C-S56 and C-S58
(ADJUDICATION_v18.Z.md @906a907893). Not the slug.

**Item 1: Nebius is one key on the served page (MET for the control); 6 GQGU securities are SERVED under two keys
(row Z-S57 confirmed on the page). Item 2 MET. Item 3 NOT MET: the four names still read as tickers.**

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S59",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T11:45:00Z",
    "one_line": "Morning pass on the served 2026-10-06 page as republished 11:14:34Z (1,298,076 B, sha256 7b1d707a38...): Nebius is one key, NBIS_US_Equity (11 buttons, 0 under N97284108). 6 GQGU securities are served under a CUSIP key and a ticker key at once (Apple, Meta, Lam Research, Micron, Philip Morris, UnitedHealth), which is row Z-S57 and C-S58 on the served page. fund_sections missing 0 of 2,089. The four C-S36 names still read as tickers.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S57"
    ],
    "spec_asserts": "ROUND_ANALYSIS.round13.md section 3 items 1 to 3; RIV-ok-1 / RIV-pk-1: one key per security on the page.",
    "world_is": "Read by this seat from the S3 bytes in a headless browser (no click).\n- Item 2: 13 funds, 2,089 data-sec buttons, 0 unresolved, 0 without the fund's section.\n- Item 1, the control: every Nebius button (11) carries NBIS_US_Equity; all 11 sit in WCMG's panel, so the page shows no Nebius button in GQGU's panel to compare. S43's page proof (WCMG's and GQGU's mentions open one modal carrying both funds) is therefore not exercised on this page; the issuer's table read (holding_contribution merged 13, split 0) is the evidence for the merge.\n- Item 1, the split: GQGU buttons by key: Apple 037833100 x16 and AAPL_US_Equity x4; Meta 30303M102 x5 and META_US_Equity x35; Lam Research 512807306 x2 and LRCX_US_Equity x12; Micron 595112103 x2 and MU_US_Equity x6; Philip Morris 718172109 x1 and PM_US_Equity x5; UnitedHealth 91324P102 x1 and UNH_US_Equity x2. Eli Lilly, the 7th name of C-S58, is one key on this page (LLY_US_Equity x11). 41 identifier-keyed buttons remain in GQGU and 1 in BASG. The issuer measured the same thing on the table (buying_trend merged 2, split 7; row Z-S57, cause unread). No wrong merge (two securities under one key) was seen; this is a split, so the rollback clause does not apply.\n- Item 3: the 4 dialogs are titled '8053 JP Equity', '9433 JP Equity', 'RBLX US Equity', '000270 KS Equity' (14 buttons).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-06/index.html (LastModified 2026-10-07T11:14:34Z, 1,298,076 B, sha256 7b1d707a38c5936c0d840a8709c091e87998ddf27cb9de9e9bf22c4bfe21fd6b)",
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round14/morning_pass_2026-10-06.after_vehicle_20261007.json @b74bdc238b",
        "adjudications/ADJUDICATION_v18.Z.md ETFS_RIVALS-Z-C-S56, ETFS_RIVALS-Z-C-S58 @906a907893"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV

# ETFS_RIVALS -- round 14 L8/L9 on the served 2026-10-07 page of the 13:00Z sweep; the morning pass closed (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~13:15Z. Round 14: RIV-ab-1, RIV-as-1 (drain 22844f744f, deploy cc02eeac7d). With
ADJUDICATION_v16 to v20 and REMEDIATION_v12 this is the L10 slug for rounds 14 to 19.

**ab-1 J1: MET**, with one account (SCHY, the last 30 days) carrying a FAIL badge of its own. **Z-S54 REMEDIATED on the
served page. S43 REMEDIATED on the served page. C-S36 (the four names) NOT MET. Z-S57 (two keys) still served.**

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S61",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T13:15:00Z",
    "one_line": "Round 14 L9 on the served 2026-10-07 page written by the 13:00Z sweep (index.html 1,286,540 B, 13:07:30Z, sha256 97cf3f030f...): 25 of 26 AI accounts carry 'Grounded' with data-build served and 1 carries a FAIL badge; 157 of 157 cited contribution figures this seat could parse equal a ranking row of the same fund and security (Petrobras in IDVZ: +0.97% and +2.53% on both). The earlier-build badge is exercised on the served 10-06 republish: 24 of 24 PASS accounts read 'Grounded on an earlier build'. ab-1 J1 MET; row Z-S54 is remediated.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S54"
    ],
    "spec_asserts": "RIV-ab-1 J1 (on a real day's run): 26 of 26 accounts cite the served revision and a sample of cited figures equals the panel's (Petrobras in IDVZ among them); a late rebuild turns that fund's badge to 'Grounded on an earlier build'. ROUND_ANALYSIS.round13.md section 3 items 1 to 3.",
    "world_is": "Read by this seat from the S3 bytes in a headless browser (no click).\n- Accounts: 26 (2 per fund, 13 funds). 25 PASS with data-build 'served' and the text 'Grounded'; 0 'earlier'; 1 FAIL (SCHY, the last 30 days: 'figures not in any cited row: $3.9 million; ambiguous figure'). The manifest reads ai_grounding served 25, earlier 0. The criterion says 26 of 26; the 26th is not on an earlier build, it failed its own grounding check and says so on its badge.\n- Cited figures: for every account, each '<security> at/added/by <signed percent>' whose security is a button in the account was compared with the ranking rows of the same fund and security on the page: 157 of 157 equal one of that security's ranking figures (SCHY's FAIL account: 9 of 9). The period of each figure was not matched, only the value; 5 accounts yielded no parsable figure. On the served 2026-10-06 page the issuer had measured 149 of 197 cited figures moved (row Z-S54).\n- Petrobras in IDVZ: both accounts say +0.97% over thirty days and the direction verdict says +2.53% year to date; the rankings show +0.97% and +2.53%.\n- The earlier-build badge: not produced by this run (no table was rebuilt after the accounts; a1_produced reads SKIPPED for the three tables). It is exercised on the served 2026-10-06 page republished 11:14:34Z, whose accounts predate its tables: 24 PASS badges read 'Grounded on an earlier build' with data-build 'earlier', 0 read plain 'Grounded', 2 FAIL.\n- The sweep's refresh: the issuer's read (SWEEP_READ_2026-10-07.md @93f23ea2f4, COO~RV msg 30932, arrived after this grade was made) says the three tables were refreshed 13:00:55Z to 13:02:25Z before the AI run. This seat did not read the sweep's record itself; the grade rests on the page.\n- as-1 is mechanical (issuer re-run PASS); the audit page is 1,243,556 B on this run, under the gateway's 2,097,152 B cap, so the size rule did not fire.\n- Morning pass item 1 (S43): Nebius is one key, NBIS_US_Equity, in GQGU's rankings (2 buttons) and in WCMG's panel (9); every one of the 2,053 buttons on the page opens a dialog carrying a section for the button's own fund (0 missing), so the one Nebius dialog carries both funds. S43 is remediated on the served page.\n- Morning pass item 3 (C-S36): '8053 JP Equity', '9433 JP Equity', 'RBLX US Equity', '000270 KS Equity' still title their dialogs (9 buttons). NOT MET.\n- Row Z-S57 on this page: Apple, Meta, Lam Research, Micron, Philip Morris and UnitedHealth are each under a CUSIP key and a ticker key in GQGU; 101 identifier-keyed buttons remain.\n- The accounts' prose still says 'year to date' and 'thirty days': cell RIV-pd-3 is merged and not deployed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-07/index.html (LastModified 2026-10-07T13:07:30Z, 1,286,540 B, sha256 97cf3f030fd06fe88ceb2f462c04c69077f24b973e924ff37a3d87aefa57d216)",
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-07/manifest.json (generated_at 2026-10-07T13:07:29Z; ai_grounding served 25 / earlier 0; fund_sections 2053 / 0 missing)",
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-06/index.html (LastModified 2026-10-07T11:14:34Z, sha256 7b1d707a38c5936c0d840a8709c091e87998ddf27cb9de9e9bf22c4bfe21fd6b): 24 earlier, 0 served, 2 FAIL",
        "investigations/INVESTIGATION_v1.Z.md ETFS_RIVALS-Z-S54"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-Z-C-S62",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T13:25:00Z",
    "one_line": "Round 20 (RIV-bk-1, no judgment criterion) repairs rows Z-S60 and Z-S61 in the build; neither is exercised on a served or vendor plane yet. Z-S60: the issuer's record shows the rankings table equal on 13 of 13 funds with 25 planted backfill-marked partitions and different on 13 of 13 with the same rows unmarked. Z-S61: the trend stage's G4 read now names security_parsekey at HEAD. The backfill has not run and the new build is not deployed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S60",
      "ETFS_RIVALS-Z-S61"
    ],
    "spec_asserts": "Z-S60: the Bloomberg range backfill serves the modal's price curve only, gives a formerly-held key its currency, and fits a day's budget (Andrew-direct @96d0ab2f4b; CTO rulings msg 30817 term 1 and msg 30897). Z-S61: cell RIV-al-1, the three readers take pk-1's parsekey.",
    "world_is": "This seat read the issuer's record and the code; it re-ran nothing of round 20.\n- Z-S60, the rankings limb: round20/delta0_2026-10-06.json reads whole-table hash A = B (c31d3824c89b) and C different (8b488be5fe8f); 13 of 13 funds A equals B, 0 of 13 A equals C; 6,067 rows in each arm; price_source counts identical in A and B. The proof is the stage's table; the publisher was not run on the planted layers (the packet says so).\n- Z-S60, the currency limb: one CRNCY reference request for the securities with no stored currency is built and unmeasured at real size (282 formerly-held keys; row Z-W10-S1).\n- Z-S60, the budget limb: 863 securities, 217,476 points against a 120,000-point daily allowance, so two days or more; a held date is neither counted nor asked.\n- Z-S61: data/etfs/scripts/rivalfunds/gold_buying_trend.py line 313 at HEAD reads ('security_id', 'date', 'security_name', 'security_parsekey'). On the served pages the split is still there (C-S59, C-S61: 6 GQGU names under two keys), because the deployed build is round 14's.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round20/DRAIN_END_PACKET.round20.md @0192e63608",
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round20/delta0_2026-10-06.json @0192e63608",
        "data/etfs/scripts/rivalfunds/gold_buying_trend.py:313 (read at HEAD 2026-10-07 ~13:22Z)",
        "investigations/INVESTIGATION_v1.Z.md ETFS_RIVALS-Z-S60, ETFS_RIVALS-Z-S61"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV

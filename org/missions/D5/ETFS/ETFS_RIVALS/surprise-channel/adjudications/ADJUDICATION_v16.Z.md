# ETFS_RIVALS -- round 15 judgment criteria, the pre-deploy grade on the issuer's real run (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~10:25Z. Packet: COO~RV msg 30785, DRAIN_END_PACKET.round15.md @e9e43448dc.

**co-1 J1: MET on the real-run objects (not served). pd-2 J1 and md-1 J1: NOT MEASURED** -- each names the served page,
and round 15 is not deployed. Row ETFS_RIVALS-Z-S55 stands BLOCKING and is wider than its 3x census. No slug is owed yet.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S52",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T10:25:00Z",
    "one_line": "Round 15 L9, pre-deploy, on the issuer's real run of day 2026-10-06: co-1 J1 is MET on the local chart objects (116 of 116 sampled points equal their source; 123 of 123 markers inside the audit page's windows equal a logged trade). pd-2 J1 and md-1 J1 are NOT MEASURED, because each names the served page and nothing of round 15 is served. Row Z-S55 is confirmed and is wider than its 3x census: 5 of 5 IDVZ securities with a non-dollar close differ from the same day's implied dollar price, 3 of them by less than 3x.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "RIV-co-1 J1: for one fund, a sample of points equals the market close or the holding-implied price of that day, and each marker equals a trade of the audit page's trade log in side, window and dollars. RIV-pd-2 J1: graded on the served page. RIV-md-1 J1: graded on the live page in a signed-in browser.",
    "world_is": "Graded object: the local layer C:/tmp/rv-r15-realrun/layer/ on site Z (13 chart objects, index.html 1,575,038 B, audit.html 1,385,526 B), written by round15/real_run.py @a26fc880e9. It is a real day's objects from live inputs; it is not the served page.\n- co-1 J1, points (fund IDVZ, 47 securities, days 2026-10-01, 10-02, 10-05): this seat downloaded the newest gold security_market object of 10-02 and 10-05 and the newest gold canonical_shape object of 10-01, 10-02 and 10-05 from S3 and recomputed with its own code (close = px_close by security_id; implied = median over funds of summed market_value over summed quantity). 48 of 48 market points and 68 of 68 implied points are equal; 24 gap points have no source on either table. 1 market point (TSM, 10-01) was not compared: this seat did not download that day's market object.\n- co-1 J1, markers: IDVZ has no window in the audit page's trade log, so the marker limb was graded on the 7 funds that have one (CGIC, INEQ, SCHY, GQGU, BASG, TXUE, BIDD; 22 windows). 123 of 123 markers inside those windows equal a logged trade group in side, window, dollars and trade count; 0 markers without a logged trade. 95 logged trades carry no marker: all 95 are in securities that are in no chart object and have no button on the page, so no dialog exists to draw them.\n- NOT MEASURED for co-1: the markers outside the audit page's windows (the log holds recent windows only; IDVZ alone has 135 markers over 365 days, 0 of them gradable against it). The grade does not extend to them.\n- Row Z-S55, an independent read: on IDVZ, 5 of 5 securities with a non-dollar close differ from the same day's implied price (AZN LN GBp 12032 against 156.7; ICT PM PHP 890 against 14.4; TTE FP EUR 74.85 against 84.18; UBSG SW CHF 40.55 against 50.46; CNR CN CAD 170.45 against 119.32). Only 2 of the 5 exceed 3x, so the row's 152 of 598 is a floor; the population is every listing not quoted in dollars. 39 of 39 dollar closes compared on 10-05 show no mismatch above 3 percent where an implied price exists.\n- Coverage of the market source today: 49 of 8,225 priced IDVZ points are market closes, on 3 dates; the rest are implied. The backfill (bf-1) is built and not run.\n- pd-2, a pre-deploy read only: the real-run page carries one period group of exactly three radios (R30 checked, R90, R365) and no other period label in its controls; 10 mentions of MTD, QTD or YTD remain, all in AI prose from the earlier sweep (cell pd-3 is not exercised on real data). A short history reads 'Data available since <date>, through <date>, N trading days' (12 places); whether that is the criterion's 'partial with its reason' is graded on the served page.\n- md-1, a pre-deploy read only: the issuer's two screenshots show the range buttons, the count line, a gap line with its reason and the source sentence. The 365d screenshot's y axis runs from -209.14 to 5195.67 (row Z-S55) and the drawing uses about two thirds of the frame. The hover and the marker text were not exercised by this seat.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/DRAIN_END_PACKET.round15.md @e9e43448dc",
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/real_run_2026-10-06.json @a26fc880e9",
        "s3://opal-data-etfs/rivalfunds/etfs/gold/security_market/date=2026-10-02/market-20261005T124613Z-ea632b9bca87.parquet; date=2026-10-05/market-20261006T123301Z-b6602b19fad6.parquet",
        "s3://opal-data-etfs/rivalfunds/etfs/gold/canonical_shape/date=2026-10-01/holdings-20261005T054409Z-9357ccb096f1.parquet; date=2026-10-02/holdings-20261006T123244Z-0733bdbcc7aa.parquet; date=2026-10-05/holdings-20261006T123244Z-928e3e0810ec.parquet",
        "investigations/INVESTIGATION_v1.Z.md ETFS_RIVALS-Z-S55"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record. co-1 J1 is MET on a real day's objects as the criterion names them; the object is local, so the grade is re-read on the served objects after the deploy. pd-2 J1 and md-1 J1 stay owed until round 15 is served. Row Z-S55 stays OPEN and BLOCKING at its owners (shape of the repair at 1.0.0_SA_CTO~Z); this row adds the measurement that the mismatch reaches every non-dollar listing, including the ones under 3x. The round-15 slug waits on S55's disposition and on the two served grades."
  }
]
```

-- 3.0.0_SA_CVO~RV

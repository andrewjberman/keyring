# ETFS_RIVALS -- row Z-S57 re-read on the served tables and page of 2026-10-07 (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~20:00Z. Asked by 1.0.0_SA_CTO~Z msg 31342.

**Z-S57: CLOSED. GQGU has 0 security names under two keys in buying_trend, in holding_contribution and on the page.**

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S70",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T20:00:00Z",
    "one_line": "Row Z-S57 re-read on the served plane, asked by the CTO (msg 31342): CLOSED. In the served gold tables of date=2026-10-07 and on the served page of 19:19Z, GQGU has 0 security names under two keys; Meta sits under META_US_Equity alone in both tables. What remains across all funds is 14 fund-name pairs in holding_contribution and 2 in buying_trend, each a different listing, share class or temporary line of one issuer.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Row Z-S57 / Z-S61 (REMEDIATION_v12): on a served page, for GQGU, 0 security names under two keys; buying_trend reads SPLIT 0. CTO ruling msg 31342: pairs that are different listings or share classes stay under their own keys.",
    "world_is": "This seat downloaded the newest served objects of date=2026-10-07 and grouped the security-axis rows by fund and normalised name.\n- buying_trend (buying_trend-20261007T174616Z-2c3ec5a7408d.parquet, 995 security rows): GQGU 40 keys, 0 names under two keys; Meta: META_US_Equity only. All funds: 2 fund-name pairs (BIDD Alibaba 9988 HK and BABA US; BIDD Samsung 005930 KS and 005935 KS).\n- holding_contribution (holding_contribution-20261007T174527Z-95b437825a81.parquet, 5,347 security rows, 16 with no name left out): GQGU 111 keys, 0 names under two keys; Meta: META_US_Equity only. All funds: 14 fund-name pairs: Roche ROG and ROP (TXUE, CGIC, SCHY); Iberdrola IBE, IBE/D and 2663721D (TXUE, CGIC); Tencent 700 HK and TCEHY, Alibaba, Samsung common and preferred, EssilorLuxottica EL and 2653282D (BIDD); Amcor AMCR US and AMC AU (CGIC); Klabin KLBN11 and KLBN4, Sberbank common and preferred, Tisco and TTB local and foreign lines (SCHY).\n- Page (C-S69): GQGU 0 names under two keys; 89 identifier-keyed buttons remain, one key each.\n- Three of the pairs carry a Bloomberg temporary line (2663721D SM, IBE/D SM, 2653282D FP), a rights or interim line rather than a second listing. By the CTO's ruling they stay under their own keys and no cell is cut; this seat notes them and asks nothing.\n- Both tables were written 17:45Z to 17:46Z, by the rounds 15-22 build; the round-23 republish wrote no table.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-etfs/rivalfunds/etfs/gold/buying_trend/date=2026-10-07/buying_trend-20261007T174616Z-2c3ec5a7408d.parquet (LastModified 2026-10-07T17:46:17Z)",
        "s3://opal-data-etfs/rivalfunds/etfs/gold/holding_contribution/date=2026-10-07/holding_contribution-20261007T174527Z-95b437825a81.parquet (LastModified 2026-10-07T17:45:29Z)",
        "adjudications/ADJUDICATION_v26.Z.md ETFS_RIVALS-Z-C-S69 @cbd337cd24",
        "1.0.0_SA_CTO~Z msg 31342 (the ruling: no cell; R6 withdrawn)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record. Z-S57's proof is met on the served tables and the served page; Z-S57, Z-S61, C-S58 and C-S59 move OPEN to REMEDIATED in place in REMEDIATION_v12. Nothing remains of the row; the other pairs are different securities by the CTO's ruling."
  }
]
```

-- 3.0.0_SA_CVO~RV

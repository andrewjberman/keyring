# ETFS_RIVALS -- round 23 L8/L9 on the round-23 real run (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~19:10Z. Packet: COO~RV msg 31265 (@ce0b3a783b). Round 23 is merged and NOT deployed.

**ks-1 J1: MET on the real run. The served page keeps the fault (4 of 2,247 buttons) until round 23 is deployed.**

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S67",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T19:10:00Z",
    "one_line": "Round 23 L9 on the issuer's real run of day 2026-10-07 (local, not served): RIV-ks-1 J1 MET. 0 of 2,247 buttons open a dialog without their fund's section (served: 4) and 0 of 408 dialogs hold only a name (served: 2 of 410). Against the served page exactly 4 buttons differ: GQGU's two META and two ASML mentions now open META_US_Equity and ASML_US_Equity, each carrying GQGU's section. The served page still has the fault until round 23 is deployed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S65",
      "ETFS_RIVALS-Z-S66"
    ],
    "spec_asserts": "RIV-ks-1 J1: in GQGU's panel the META and ASML mentions open the dialog that carries GQGU's section, or read as plain text; no mention on the page opens a dialog holding only a name.",
    "world_is": "This seat read both pages in a headless browser: C:/tmp/rv-r23-realrun/layer/ index.html (1,690,296 B, sha256 e58a6895b2f4bd67...) and the served 2026-10-07 page of 17:47Z (sha256 5818c309f7...).\n- Round-23 run: 2,247 buttons, 0 unresolved, 0 without the fund's section; 408 dialogs, 0 with no section. GQGU's META and ASML buttons: 6, every one opening a dialog with GQGU's section (4 in account text, 2 in the panels).\n- Served page: 2,247 buttons, 4 without the fund's section, all in GQGU's account text (30303M102 twice, N07059210 twice); 410 dialogs, 2 with no section (those two keys).\n- The difference between the two pages, as a multiset of (fund, key, text, component) over every button: 4 gone, 4 added, the four named above; nothing else changed.\n- Row Z-S57 re-read: on the served page the one GQGU name under two keys, Meta, is this link fault and not a split in the tables; the served GQGU chart object has 58 keys and 0 names under two keys, and on the round-23 page GQGU has 0 names under two keys. 89 identifier-keyed buttons remain on the round-23 page (27 identifier-form keys in GQGU's chart object): securities with no parsekey yet, one key each.\n- Not read by this seat: the buying_trend table's own census (the issuer's SPLIT count).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round23/DRAIN_END_PACKET.round23.md @ce0b3a783b",
        "C:/tmp/rv-r23-realrun/layer/opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-07/index.html on site Z, read 2026-10-07 ~19:00Z",
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-07/index.html (LastModified 2026-10-07T17:47:34Z, sha256 5818c309f77646a740abf379f09d7e5874d747ee87afc41c9caa3d1e723b88a6)",
        "adjudications/ADJUDICATION_v24.Z.md ETFS_RIVALS-Z-C-S66 @665581ba62"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-Z-C-S68",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T19:10:00Z",
    "one_line": "Row Z-S63 (the rounds 15-22 deploy at 1,024 MB) is answered by the deploy itself: 5 of 5 rivalfunds Lambda functions read MemorySize 3008 at 19:05Z, last modified 17:35Z. The first full daily run on the new code has not happened; its Max Memory Used and Duration are legs of the deploy ledger for 2026-10-08.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S63"
    ],
    "spec_asserts": "Row Z-S63: the deploy of rounds 15 to 22 does not go out at 1,024 MB; the 11:00Z daily run and the 13:00Z sweep must publish the page after the deploy as they do today.",
    "world_is": "This seat's own read of the functions (list-functions, 19:05Z): rivalfunds-publish-page-lambda, rivalfunds-build-canonical-shape-lambda, rivalfunds-build-silver-lambda, etfs-rivalfunds-daily-lambda and etfs-rivalfunds-fetch-holdings-lambda each read MemorySize 3008; LastModified 17:35:14Z to 17:36:17Z; Timeout 900 s (fetch-holdings 300 s). The round-22 analysis reports one republish at 164.5 s and Max Memory Used 1,009 MB; this seat did not read that log line. Not yet measured by anyone: a full daily run (11:00Z) and a sweep (13:00Z) on the new code; the analysis makes a duration above 720 s BLOCKING before the backfill.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws lambda list-functions, names containing 'rivalfunds', read 2026-10-07 ~19:05Z: 5 of 5 MemorySize 3008",
        "org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round22.md @f8a61834fd sections 1 and 2",
        "investigations/INVESTIGATION_v1.Z.md ETFS_RIVALS-Z-S63"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV

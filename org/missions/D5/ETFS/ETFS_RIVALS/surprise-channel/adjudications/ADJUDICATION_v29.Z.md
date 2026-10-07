# ETFS_RIVALS -- RIV-cu-1 J1 and the deploy's two conditions on the served 2026-10-07 page of 21:26Z (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~21:45Z. Deploy: COO~RV msg 31425. Round 24 is slugged (ADJUDICATION_v28 @f97c41e692).

**cu-1 J1: MET on the served page. C1 and C2 of the CTO half: hold.**

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S72",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T21:45:00Z",
    "one_line": "RIV-cu-1 J1 on the served page: MET. The 2026-10-07 page republished 21:26:48Z (index.html 1,693,555 B, sha256 78cf9e0873...) behaves as the graded run did on the same six cases. The CTO half's two conditions read true on this seat's own reads: C1, 32 keys written, all under the page day and its state record; C2, one script block whose one network call is fetch to /rivalfunds/<day>/chart/<fund>.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "RIV-cu-1 J1 on the served page. CTO half @db4ab8faec: C1, the republish wrote the same keys as round 23 and no object under any other key of the product's prefix; C2, one script block, and the one fetch's target is named.",
    "world_is": "Read by this seat from S3 and in its own headless browser, the chart route answered from the served chart objects; 0 console errors, 0 page errors. The signed-in gateway hop was not taken.\n- J1, six cases (ADJUDICATION_v28 C-S71): the same read-outs, tick labels and tooltips as on the graded run: '777.59 USD' 34px / 800 with '2026-09-24' 22px / 700; 'Bought $10,592,358 / on 2026-09-14, 165 bps of the fund, 1 trade.' (buy); 'Sold $1,020,518 / on 2026-04-08, 68 bps of the fund, 1 trade.' (sell); 'Price in TWD' on the Taiwan listing; the no-history frame draws nothing and says why; the 640 px window holds. The two faults of C-S71 are served as graded.\n- Sections: 2,247 buttons, 0 unresolved, 0 without the fund's section; 408 dialogs, 0 with none.\n- C1: every object under rivalfunds/etfs/ with LastModified at or after 21:20Z: 32, written 21:26:48Z to 21:26:53Z. By class: index.html 1, audit.html 1, manifest.json 1, charts 13, one revisions/<timestamp>/ copy of index 1, manifest 1 and charts 13, and 1 state/publish_page record. 0 keys outside date=2026-10-07; 0 gold or table objects. The comparison with round 23's key classes is the issuer's (its ledger record); this seat counted this run only.\n- C2: 1 script block, 9,367 bytes, 0 script src attributes. In it: 1 fetch call, to \"/rivalfunds/\"+D+\"/chart/\"+encodeURIComponent(fund); 0 XMLHttpRequest, 0 WebSocket, 0 sendBeacon, 0 dynamic import. The one http string is the SVG namespace.\n- The issuer gives the script as 9,348 bytes; this seat counts 9,367 UTF-8 bytes between the tags. The difference was not traced.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-07/index.html (LastModified 2026-10-07T21:26:48Z or later, 1,693,555 B, sha256 78cf9e0873a7678c8844b28528dc77d86cd03bfd277cc6e28a9462676a3dd1ad)",
        "aws s3api list-objects-v2, prefix rivalfunds/etfs/, LastModified >= 2026-10-07T21:20Z, read ~21:40Z: 32 keys",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_ETFS_RIVALS_R24_CHART_UI_DEPLOY_20261007.md @db4ab8faec",
        "adjudications/ADJUDICATION_v28.Z.md ETFS_RIVALS-Z-C-S71 @f97c41e692"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record. J1 is MET on the served page and C1 and C2 hold on this seat's reads. The acceptance is Andrew's own look. The two faults are round 25's first cell by the CTO's analysis (msg 31414)."
  }
]
```

-- 3.0.0_SA_CVO~RV

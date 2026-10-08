# ETFS_RIVALS -- the round-27 package's first run on the served plane, 2026-10-08 15:09Z (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-08 ~15:55Z. Not a slug.

**Nothing moved: 2 keys written (input_census, one state record); the served page is unchanged.**

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S84",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-08T15:55:00Z",
    "one_line": "The round-27 package's first run on the served plane (the publish-page invoke of 2026-10-08 at 15:09Z, CTO ruling msg 31819) moved nothing: 2 keys written, an input_census object and one state record; no table, chart or page object. The served page of 2026-10-08 is still the 13:08:16Z object. RIV-rk-1 holds served.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "RIV-rk-1 J1 on the served plane: no table row and no chart point differs from the served page. CTO ruling msg 31819: the keys the invoke may write are read after it.",
    "world_is": "This seat's own reads of S3 and of the function, 2026-10-08 15:51Z.\n- rivalfunds-publish-page-lambda reads LastModified 14:56:44Z (the round-27 apply).\n- Written under rivalfunds/etfs/ at or after 14:00Z: 2 keys: gold/input_census/date=2026-10-08/input_census-20261008T150929Z-3bc36465cd6c.parquet (15:09:30Z) and state/publish_page/date=2026-10-08/rv-publish-1008r27.json (15:09:38Z).\n- index.html of date=2026-10-08: LastModified 13:08:16Z, 1,688,097 B, the object graded in C-S82. No holding_contribution, buying_trend, chart or revision object written.\n- As on 2026-10-08 01:41Z (C-S79), that the tables were rebuilt to an already stored content hash is the issuer's read of the run; this seat saw only that no new table object exists. No issuer record of this invoke had reached this seat at the read.\n- RIV-ho-1 runs nothing on the served plane until RIV-tw-1 is merged and the vehicle runs; RIV-tw-1 J1 stays owed (C-S80).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws s3api list-objects-v2, prefix rivalfunds/etfs/, LastModified >= 2026-10-08T14:00Z, read 15:51Z: 2 keys",
        "aws s3api head-object rivalfunds/etfs/platinum/page/date=2026-10-08/index.html: LastModified 2026-10-08T13:08:16Z, 1,688,097 B",
        "aws lambda get-function-configuration rivalfunds-publish-page-lambda: LastModified 2026-10-08T14:56:44Z",
        "adjudications/ADJUDICATION_v35.Z.md ETFS_RIVALS-Z-C-S80 @f78a9b6cb1"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record. The deployed round-27 package ran once and changed no served object. C-S80 stays OPEN for RIV-tw-1 J1."
  }
]
```

-- 3.0.0_SA_CVO~RV

# ETFS_RIVALS -- round 26 remediations (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-08 ~01:20Z. Graduated at the round-26 L9 (`adjudications/ADJUDICATION_v33.Z.md`).

REMEDIATED on the real run: C-S78 (rg-2). Still OPEN: C-S73 / Z-S69 / Z-S71 (the mis-dated object; round 27's term).

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S78",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The round-26 grade record: the narrowed reader (RIV-rg-2) reads untimed dates as the live code does and never opens the mis-dated 2026-09-29 object.",
    "evidence": [
      "adjudications/ADJUDICATION_v33.Z.md ETFS_RIVALS-Z-C-S78"
    ],
    "remedy": "Cell RIV-rg-2 (merge 8d13655287). Proof on the real run: 0 moved rows in both tables, 13 of 13 chart objects unchanged, 0 market points on 2026-09-29. Its deploy is not held by C-S73: this reader does not read that object. Proof owed after the deploy: the served after-tables read 0 moved rows. C-S73 and Z-S71 stay OPEN for round 27's term (a close carries its trading date).",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v18",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v18"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO~RV

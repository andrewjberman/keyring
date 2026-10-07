# ETFS_RIVALS -- the corrected remediation row for Z-S67 (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~23:55Z. Graduated by `adjudications/ADJUDICATION_v31.Z.md`.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S75",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Z-S67 as it is: bbg_budget's check_points and check_backfill price one day 150 times apart, and the ledger's rows field mixes points requested with records returned. Supersedes the mechanism sentence of REMEDIATION_v16's Z-S67 row, which is wrong.",
    "evidence": [
      "adjudications/ADJUDICATION_v31.Z.md ETFS_RIVALS-Z-C-S75",
      "investigation rows ETFS_RIVALS-Z-S67, ETFS_RIVALS-Z-S68"
    ],
    "remedy": "As the CTO ruled (msg 31309; the round-22 analysis's R7): the backfill's bbg_budget line states one unit, and the first market-range day's log gives the measured ratio of records returned to points requested. Proof: after that day, spent() for it is printed in one named unit beside the request count. No edit under integrations/bloomberg.",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v17"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-S68",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The disarm owner's statement for Z-S67: the backfill's guard is check_points and its unit, one requested price point, is an upper bound on records returned. Read from the request's shape, not measured.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S68",
      "adjudications/ADJUDICATION_v31.Z.md ETFS_RIVALS-Z-C-S75"
    ],
    "remedy": "As C-S75 above: the first market-range day's log gives the measured ratio, and the statement is confirmed or corrected on it.",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v17"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-S71",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The 2026-09-29 live pull of security_market holds 2026-09-30's closes; rows Z-S69 and Z-S70 read the fault backwards. One object of five is misdated; as_of does not show it.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S71",
      "adjudications/ADJUDICATION_v31.Z.md ETFS_RIVALS-Z-C-S76",
      "adjudications/ADJUDICATION_v30.Z.md ETFS_RIVALS-Z-C-S73"
    ],
    "remedy": "As C-S73 (REMEDIATION_v16) and the CTO's ruling msg 31481: the re-cut reader names the misdated object in its test and moves no served figure; every close a future writer adds carries the trading date it belongs to. Proof: C-S73's.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v17"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-C-S76",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The 2026-09-29 live pull of security_market holds 2026-09-30's closes; rows Z-S69 and Z-S70 read the fault backwards. One object of five is misdated; as_of does not show it.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S71",
      "adjudications/ADJUDICATION_v31.Z.md ETFS_RIVALS-Z-C-S76",
      "adjudications/ADJUDICATION_v30.Z.md ETFS_RIVALS-Z-C-S73"
    ],
    "remedy": "As C-S73 (REMEDIATION_v16) and the CTO's ruling msg 31481: the re-cut reader names the misdated object in its test and moves no served figure; every close a future writer adds carries the trading date it belongs to. Proof: C-S73's.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v17"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~RV

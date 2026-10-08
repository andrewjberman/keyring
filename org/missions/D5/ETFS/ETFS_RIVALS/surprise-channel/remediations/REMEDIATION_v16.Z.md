# ETFS_RIVALS -- round 25 remediations (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~23:45Z. Graduated at the round-25 L9 (`adjudications/ADJUDICATION_v30.Z.md`).

OPEN and BLOCKING for the rg-1 deploy: C-S73 (the misdated object), with Z-S69. REMEDIATED on the real run: C-S74 (mr-1).

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S73",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The security_market object filed under 2026-09-29 by a pull made on 2026-10-01 holds 2026-09-30's closes and day returns. RIV-rg-1's union makes every reader use it as 09-29.",
    "evidence": [
      "adjudications/ADJUDICATION_v30.Z.md ETFS_RIVALS-Z-C-S73"
    ],
    "remedy": "The rg-1 reader does not deploy while this object reads as 2026-09-29. Rule on the object (leave it unused; or re-file it under the date its closes are, by a recorded act), and on the producer: a reference-data pull records the date its PX_LAST belongs to, not the date asked. Proof: on every stored security_market date, the dollar closes equal the funds' own valuation of the SAME report date for the large majority and no neighbouring date fits better, printed per date with its denominator; then the before and after of the tables.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v16"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-S69",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Every reader of security_market takes one object per date, so the 434-row object of date=2026-09-29 is ignored. The row called this dropped production closes.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S69",
      "adjudications/ADJUDICATION_v30.Z.md ETFS_RIVALS-Z-C-S73"
    ],
    "remedy": "The reader's grain (one object per date) is still a fault for FWD-24's top-ups and RIV-rg-1 repairs it in the build. The row's harm is not as stated: the ignored closes are 09-30's, so nothing of 09-29 is lost on the served page today. The row closes with C-S73: the reader deploys once the misdated object is ruled on.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v16"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-C-S74",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The round-25 grade record for RIV-mr-1: the two faults of C-S71 are repaired on the real run.",
    "evidence": [
      "adjudications/ADJUDICATION_v30.Z.md ETFS_RIVALS-Z-C-S74"
    ],
    "remedy": "Cell RIV-mr-1 (merge 4c34f7f298). Proof on the real run: 210 of 210 marker hovers name one day in the read-out and the tooltip; 0 tooltips over the read-out. Re-read on the served page after its deploy.",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v16",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v16"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-S67",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Adjudicated with Z-S69 by ADJUDICATION_v30 C-S73 (a correction or companion row of the readers' grain finding).",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S67",
      "adjudications/ADJUDICATION_v30.Z.md ETFS_RIVALS-Z-C-S73"
    ],
    "remedy": "As Z-S69 above.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v16"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~RV

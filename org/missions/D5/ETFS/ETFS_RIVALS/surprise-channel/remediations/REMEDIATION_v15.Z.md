# ETFS_RIVALS -- round 23 remediations (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~19:10Z. Graduated at the round-23 L9 (`adjudications/ADJUDICATION_v25.Z.md`).

OPEN until round 23 is served: Z-S65, Z-S66, C-S67 (and Z-S57 in REMEDIATION_v12, which closes on the same served read).

```json
[
  {
    "id": "ETFS_RIVALS-Z-S65",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "On the page rounds 15 to 22 serve, 4 mentions in GQGU's account text (META and ASML, cited by a raw CUSIP key the fund traded under) open a dialog holding a name and nothing else.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S65",
      "adjudications/ADJUDICATION_v25.Z.md ETFS_RIVALS-Z-C-S67"
    ],
    "remedy": "Cell RIV-ks-1 (merge d7bbe4f5a3): inside a fund's panel a mention links only to a key that has a section for that fund. Built and graded on the real run (0 of 2,247 missing). Proof still owed on the served plane: after the deploy of round 23, the served page reads 0 buttons without their fund's section and 0 dialogs with no section, and GQGU shows 0 names under two keys.",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v15",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v15"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-S66",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The correction to Z-S65: its first cause was a guess. The cause as read in round 23: a trade-only key counted as a held key, so the citation chose a key with no section.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S66",
      "adjudications/ADJUDICATION_v25.Z.md ETFS_RIVALS-Z-C-S67"
    ],
    "remedy": "As Z-S65 above.",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v15",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v15"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-C-S67",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The round-23 grade record that adjudicates Z-S65 and Z-S66 and re-reads Z-S57.",
    "evidence": [
      "adjudications/ADJUDICATION_v25.Z.md ETFS_RIVALS-Z-C-S67"
    ],
    "remedy": "As Z-S65 above. Z-S57 (REMEDIATION_v12) closes on the same served read: GQGU 0 names under two keys.",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v15",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v15"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-S63",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The deployed rivalfunds Lambdas ran at 1,024 MB with a peak of 864 MB on round-14 code, and the new code's stages peaked higher on site Z; a deploy at 1,024 MB risked an out-of-memory kill of the daily run.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S63",
      "adjudications/ADJUDICATION_v25.Z.md ETFS_RIVALS-Z-C-S68"
    ],
    "remedy": "memory_size raised to 3008 MB in the rounds 15-22 apply. Proof: 5 of 5 functions read MemorySize 3008 (this seat's read, 19:05Z). The first full run's Max Memory Used and Duration are read on 2026-10-08 as legs of ledger etfs-rivalfunds-r22.",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v15",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v15"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-C-S68",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The record that adjudicates Z-S63.",
    "evidence": [
      "adjudications/ADJUDICATION_v25.Z.md ETFS_RIVALS-Z-C-S68"
    ],
    "remedy": "As Z-S63 above.",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v15",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v15"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO~RV

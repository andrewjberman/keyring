# ETFS_RIVALS -- the remediation row for C-S83, the period codes in the AI accounts (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-08 ~13:25Z. Graduated by `adjudications/ADJUDICATION_v37.Z.md`.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S83",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The AI accounts' listed facts name periods by the tables' codes (R30, R90, R365) and the page prints them: 240 tokens on the 2026-10-08 13:08Z page.",
    "evidence": [
      "adjudications/ADJUDICATION_v37.Z.md ETFS_RIVALS-Z-C-S83"
    ],
    "remedy": "The accounts' facts name a period as the page does (30 days, 90 days, 365 days), by the prompt or at render. Proof: on a sweep's served page the visible text holds 0 whole-word R30, R90 or R365, and the calendar-period count stays 0 of 26.",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v20",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v20"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~RV

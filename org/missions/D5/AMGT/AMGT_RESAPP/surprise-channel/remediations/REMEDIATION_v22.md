# AMGT_RESAPP -- surprise channel, REMEDIATION v22 -- round 76: Z-W266-S1, Z-W266-S2, Z-W266-S3

Author: 3.0.0_SA_CVO~Z. Round: v91. Fabric: site-z. Recorded: 2026-10-06T22:2xZ. **Reader:** `1.0.0_SA_CTO~Z`.

```json
[
  {
    "id": "AMGT_RESAPP-Z-W266-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The /freshness flag keys on the oldest input and counts a source never collected for a name as stale, while Last refreshed shows the newest input; so 95 of 95 rows are flagged under one date and no row reads not-stale.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W266-S1",
      "deliverables/0.9.0_WK_AMGT_RESAPP~266/captures/001-fwd7-freshness-first.png: 95 of 95 stale; Last refreshed 2026-10-06 on every row; 92 'Seeking Alpha has never been read'",
      "WALK_ROUND76.md: first paint 4,116 ms; the /freshness read 2,665 ms for 1,073,156 bytes encoded"
    ],
    "remedy": "Rule whether a never-collected source flags a name; make Last refreshed and the flag read the same input; then one visit shows a not-stale row beside a stale one. Find the cause of the 2,665 ms read.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v91",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v91"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W266-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The segment breakdown is built from filing analysis, which is stored for 12 names; the other covered names serve a reason, and the builder accepts share-capital items (ASML) and all-'Other' rows (PBR) as segments.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W266-S2",
      "read_thesis_bundle over 242 keys by 3.0.0_SA_CVO~Z 2026-10-06 ~22:0xZ: segment rows on 12, reason on 230; ASML_NA labels Authorized share capital / Treasury shares / Major holders / Board holdings / Other; PBR_US 8 rows 'Other'",
      "WALK_ROUND76.md: AMD 'No filing analysis is stored for this name yet, so no segment breakdown is shown'; BA 11 rows under 3 repeated labels"
    ],
    "remedy": "The authorized Bloomberg segment pull for 83 names (Andrew's word @b5f90bbf8d, ruling 1); a segment row is a business segment, not a share-capital item; one heading per segment.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v91",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v91"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W266-S3",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The driver chart is served for 2 names; the passage is rendered as flat table-extraction text once per chart point; the y-axis does not fit nine-digit ticks; ASML's chosen driver is a share count.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W266-S3",
      "captures/017-fwd18-ASML-passage-open.png: the passage block under each of three links, each 'From the filing: TABLE / period 2023'; y-axis ticks '00000000'",
      "read_thesis_bundle over 242 keys: thesis_driver_chart SERVED 2 (BA_US_Equity, ASML_NA_Equity), ABSENT 240"
    ],
    "remedy": "One passage per press; column labels kept with their numbers; an axis that fits its ticks; a driver chosen for what the company lives or dies on; charts for more than 2 names.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v91",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v91"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z

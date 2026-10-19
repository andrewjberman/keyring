# MDPF_SECCLASS -- round 27 remediations (dell1)

<sweep_watermark>2026-10-17T07:34:38Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-17T07:34:38Z. Graduated at ADJUDICATION_v28 (C-S31): 3 rows, owner 2.0.0_SA_COO~M1.

```json
[
  {
    "id": "MDPF_SECCLASS-D1-S48",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The 04:00Z 2026-10-17 fire restated 14 served dates (2026-10-01 to 10-14) of mix_daily_summary.json. The total rose about $381k to $419k per date, and no pair of this project covers the change.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S48",
      "adjudication rows MDPF_SECCLASS-D1-C-S30 (ADJUDICATION_v27), MDPF_SECCLASS-D1-C-S31 (ADJUDICATION_v28)"
    ],
    "remedy": "Name the cause (the producer's designed open-window restatement, an input-book change, or another project's act) and the signed pair that covers it, if any. Close when: the cause is read and recorded, and this seat re-reads one restated date against its stated cause.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v27",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v27"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": "2026-10-18T01:54:47Z"
    }
  },
  {
    "id": "MDPF_SECCLASS-D1-S45",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Leg G of the seed: SEED22-LEGG ok=False on 15 of 15 window dates. unclassified plus other did not fall by the seeded dollars.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S45",
      "adjudication rows MDPF_SECCLASS-D1-C-S30 (ADJUDICATION_v27), MDPF_SECCLASS-D1-C-S31 (ADJUDICATION_v28)"
    ],
    "remedy": "Re-grade leg G on a fire whose input book is unchanged against the pre version, or name why the seed cannot show. Close when: SEED22-LEGG ok=True, or a ruling names the cause.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v27",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v27"
    },
    "closed": true
  },
  {
    "id": "MDPF_SECCLASS-D1-S42",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "22 old-list-only tickers kept E_18 blind until the seed; the 9 held out remain, and E_18 still reads the old list until TO-SC-e108b ships.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S42",
      "adjudication rows MDPF_SECCLASS-D1-C-S30 (ADJUDICATION_v27), MDPF_SECCLASS-D1-C-S31 (ADJUDICATION_v28)"
    ],
    "remedy": "Ship E_18 off the old list (TO-SC-e108b, under its signed pair). Close when: E_18's own output reads 0 old-list-only tickers after the ship.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v27",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v27"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": "2026-10-19T05:07:28Z"
    }
  }
]
```

-- 3.0.0_SA_CVO

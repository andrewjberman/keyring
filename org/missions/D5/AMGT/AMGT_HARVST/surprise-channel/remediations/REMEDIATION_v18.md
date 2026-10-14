# AMGT_HARVST -- round 85 remediations (dell1)

<sweep_watermark>2026-10-14T14:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T14:00:00Z. Graduated at ADJUDICATION_v80 D1-C-S51: 2 rows.

```json
[
  {
    "id": "AMGT_HARVST-Z-S121",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The one refresh per publisher per cycle reports done and the next job is refused 'expired' again; the cause is unread.",
    "evidence": [
      "investigation row AMGT_HARVST-Z-S121",
      "adjudication row AMGT_HARVST-D1-C-S51 (ADJUDICATION_v80)"
    ],
    "remedy": "The CTO's round-85 analysis: park as ordered, or a round 86 that reads the session, credential and producer behind the refusal.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v85",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v85"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_HARVST-Z-S120",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The runner's graceful-stop file sits in a directory nothing creates, so the documented stop step fails.",
    "evidence": [
      "investigation row AMGT_HARVST-Z-S120",
      "adjudication row AMGT_HARVST-D1-C-S51 (ADJUDICATION_v80)"
    ],
    "remedy": "The installer creates the STOP file's parent at registration, or the stop step creates the directory; carried in the park record.",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v85",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v85"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~W1",
      "at": null
    },
    "closed": false
  }
]
```

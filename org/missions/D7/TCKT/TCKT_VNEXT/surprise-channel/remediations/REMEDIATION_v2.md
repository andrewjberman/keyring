# TCKT_VNEXT -- remediations: v2 (round 20 close)

<sweep_watermark>2026-10-20T06:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-20.

This file holds three rows:
- **D2-S46 and D2-S53 graduate** (ADJUDICATION_v17 row D2-C-S13). Both are OPEN and ARMED, owner `1.0.0_SA_CTO~DELL2`.
- **D2-W6-S2 is disarmed by a new row, D2-C-S14.** It graduated in REMEDIATION_v1 with `disarm.state` ARMED, and the channel is
  append-only, so a new row disarms it through `disarms`. The evidence is in ADJUDICATION_v16:
  - the live `opal-data-refresh-api` source equals the tree;
  - its admission fails closed;
  - `test_admission_gate.py` passes 5, run by this seat.

```json
[
  {
    "id": "TCKT_VNEXT-D2-S46",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A direct lambda:InvokeFunction on a function behind the portal authorizer goes around it, and the ticket handler believes the event's own caller context, so any holder of the invoke grant can act as any caller.",
    "evidence": [
      "investigation row TCKT_VNEXT-D2-S46",
      "ADJUDICATION_v17 row TCKT_VNEXT-D2-C-S13"
    ],
    "remedy": "The owner reads who holds lambda:InvokeFunction on opal-ticket-api (in progress) and narrows the grant, or makes the handler refuse a context the authorizer did not sign.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~DELL2",
      "at": null
    }
  },
  {
    "id": "TCKT_VNEXT-D2-S53",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "An ACTIVE users row on an outside company's domain carries the internal firm id with no firm list; it reads every firm in every service that classes by firm id, the data-refresh admission gate included (is_opal_internal trusts firmId).",
    "evidence": [
      "investigation row TCKT_VNEXT-D2-S53",
      "ADJUDICATION_v16 row TCKT_VNEXT-D2-C-S11 (data-refresh gate trusts firmId)"
    ],
    "remedy": "Andrew rules whether the row is meant to be internal; if not, its firm id is corrected or the row disabled, under a pair.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~DELL2",
      "at": null
    }
  },
  {
    "id": "TCKT_VNEXT-D2-C-S14",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "D2-W6-S2's hazard (the data-refresh routes admitted a caller with no userType) is closed by NFRA_OPLGTW TO-OG-da-1: validate_user_type admits only Dev or an Opal-internal tier or firm and refuses an empty userType and a call with no authorizer context.",
    "evidence": [
      "ADJUDICATION_v16 row TCKT_VNEXT-D2-C-S11",
      "live opal-data-refresh-api CodeSha256 qHMjXkK1/1NhmBmkK/6Q+q+WdXMRoTOprNfTixBIxaM=; the downloaded lambda_function.py equals infra/aws/lambda/data_refresh/lambda_function.py",
      "infra/aws/lambda/data_refresh/test_admission_gate.py: 5 passed (3.0.0_SA_CVO~DELL2, 2026-10-20)"
    ],
    "remedy": "Done by another repair (NFRA_OPLGTW TO-OG-da-1). The firmId trust is D2-S53's and stays there.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v3"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL2",
      "at": "2026-10-20T06:05Z"
    },
    "disarms": [
      "TCKT_VNEXT-D2-W6-S2"
    ]
  }
]
```

-- `3.0.0_SA_CVO~DELL2`

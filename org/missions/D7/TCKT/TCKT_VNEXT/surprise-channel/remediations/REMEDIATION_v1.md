# TCKT_VNEXT -- remediations: workstreams F10 and SA

<sweep_watermark>2026-10-09T05:21Z</sweep_watermark>

Graduated at the F10/SA L8 (ADJUDICATION_v1.md): 4 rows, OPEN. D2-W6-S2 stays ARMED: its fix belongs to the data_refresh Lambda's owner.

```json
[
  {
    "id": "TCKT_VNEXT-D2-S6",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FWD-6 says the draft appears on the SAME ticket and the ticket shows who sent the final commentary and when; workstream F10 (CTO scope msg 1789: svc-commentary CREATE-only) puts the draft on a NEW analysis_request ticket and builds no sent-by/sent-at field.",
    "evidence": [
      "investigation row TCKT_VNEXT-D2-S6",
      "org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md:57 (FWD-6 text)"
    ],
    "remedy": "Rule FWD-6's 'same ticket': an append-to-existing-ticket route needs the report to know its ticket (contract O2); until then the draft lands on a new analysis_request, which FWD-6 does not accept.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "TCKT_VNEXT-D2-S9",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The svc-commentary read grant reaches dell1 as well as dell2: the laptop put the one ARN in the SHARED Dell platform-key policy, while the signed pair (COO AMENDMENT 1 @b70dd6fbad, CTO 1.2) names dell2's allow-list only.",
    "evidence": [
      "investigation row TCKT_VNEXT-D2-S9",
      "0.0.0_AB_MSTR~DELL2 msg 2170 relaying laptop 2.0.0_SA_COO~C msg 107630: cloudops-dell2-agent-user AND cloudops-dell1-agent-user each allowed GetSecretValue on opal/ticketing/svc-commentary-pXsmuU (policy default v3)"
    ],
    "remedy": "Accept the svc-commentary read grant's parity with svc-analyst-intake on both Dells, or narrow it to dell2 as the signed pair names.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "TCKT_VNEXT-D2-W6-S2",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The data-refresh routes (including trigger and rollback) admit a caller whose userType is absent, so a one-firm test filer token reaches platform-wide data operations that have no firm axis",
    "evidence": [
      "investigation row TCKT_VNEXT-D2-W6-S2",
      "infra/aws/lambda/data_refresh/lambda_function.py:160-167: 'Allow Dev users or users without userType restriction' returns True when user_type is empty"
    ],
    "remedy": "The data-refresh Lambda refuses a caller with no userType on trigger and rollback (measured real: 45 PROFILE rows lack userType). Routed by 1.0.0_SA_CTO~DELL2 through 0.0.0_AB_MSTR~DELL2 to the data_refresh owner; TCKT_VNEXT builds nothing on it, and the seat run SA-r-1 must not use a token that reaches those routes until it lands.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "the data_refresh Lambda's owning project (via 0.0.0_AB_MSTR~DELL2)",
      "at": null
    }
  },
  {
    "id": "TCKT_VNEXT-D2-W6-S3",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The portal route denominator cannot be completed from source: a console-only default route and live-only routes exist, and the IRPT route contract's own denominator is stale",
    "evidence": [
      "investigation row TCKT_VNEXT-D2-W6-S3",
      "infra/aws/terraform/shared-infra/apigateway-portal/routes.tf:1-2 and main.tf:53-57: $default route and stage console-only"
    ],
    "remedy": "State the route census's live-only remainder by ruling (the console-only $default, the 2 trade-identifier-cache routes with no repo source), and correct IRPT routes.json's _denominator (19 stated, 21 held).",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v2"
    },
    "closed": false
  }
]
```

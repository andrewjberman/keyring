# TCKT_VNEXT -- remediations: v3 (D2-S46 closed, accepted by the CTO's ruling on the IAM census)

<sweep_watermark>2026-10-20T06:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-20.

D2-S46 graduated in REMEDIATION_v2, OPEN and ARMED. The CTO ruled it closed (msg 11229) on `2.0.0_SA_COO~V2`'s IAM census
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R20_S46/` (packet part 6, msg 11232).

## What this seat read in `S46_CENSUS_RESULT.json` and the census note

- **The denominator:** 7 users, 335 roles, 3 groups, 79 managed policies; 20 functions behind the portal authorizer.
- **Who can invoke `opal-ticket-api` directly:** exactly 4 users. `Andrew_Berman`, `Andrew_Berman_Console`, `cloudops-dell1-agent-user` and
  `cloudops-dell2-agent-user` all hold it through `AdministratorAccess`, with no boundary and no Deny.
- **The 4 roles:** they hold 1 to 4 other functions each (scheduler, gateway reader, export render, trade submission), and none holds
  `opal-ticket-api`. The 3 gateway S3 roles deny Lambda.
- **Resource policies:** `apigateway.amazonaws.com` on all 20 functions, plus `events` on one.

So the bypass gives its holders nothing they do not already have as full administrators. No narrower grant exists to remove.

**Limits (the census's own):** SCPs, session policies, cross-account assumption chains and identities outside the account were not read. A
future narrower grant of `lambda:InvokeFunction` on any authorizer-fronted function re-opens this hazard. That would be a new row, not
this one.

This row also disarms `TCKT_VNEXT-D2-C-S13`, this seat's own graduation row, written ARMED in ADJUDICATION_v17. D2-S53 keeps its own
ARMED rows and is NOT disarmed here: it is Andrew's.

```json
[
  {
    "id": "TCKT_VNEXT-D2-C-S15",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "D2-S46 (a direct invoke bypasses the portal authorizer and the handler trusts the event's caller context) is held only by full administrators: the census finds 4 users with AdministratorAccess and no role holding lambda:InvokeFunction on opal-ticket-api, so the bypass grants nothing beyond what they already hold.",
    "evidence": [
      "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R20_S46/S46_CENSUS_RESULT.json (users 7, roles 335, groups 3, managed policies 79; 20 functions)",
      "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R20_S46/S46_INVOKE_GRANT_CENSUS_20261020.md",
      "1.0.0_SA_CTO~DELL2 msg 11229 (the ruling); 2.0.0_SA_COO~V2 msg 11232"
    ],
    "remedy": "None owed while invoke stays admin-only; any future narrower lambda:InvokeFunction grant on an authorizer-fronted function is a new row.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v4",
    "remediation": {
      "state": "CLOSED_UNREMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v4",
      "closure": {
        "reason": "ACCEPTED_BY_RULING",
        "pointer": "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R20_ARMED_ROWS_OWNED_BY_COO.md"
      }
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL2",
      "at": "2026-10-20T06:15Z"
    },
    "disarms": [
      "TCKT_VNEXT-D2-S46",
      "TCKT_VNEXT-D2-C-S13"
    ]
  }
]
```

-- `3.0.0_SA_CVO~DELL2`

# MDPF_SECHIST -- correction: Z-S2 fabric value (dell1)

<sweep_watermark>2026-10-13T19:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T19:10:00Z.

```json
[
  {
    "id": "MDPF_SECHIST-D1-C-S9",
    "project": "MDPF_SECHIST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T19:10:00Z",
    "one_line": "Correction to REMEDIATION_v4 row MDPF_SECHIST-Z-S2: its fabric field reads 'sitez', which is not in the remediation_row schema enum (laptop, site-z, dell1, dell2); the correct value is 'site-z' (the id carries the Z- infix). The value landed in commit cfa051f0cd under an audited surprise-row-override whose stated reason (CTO msg 5020: TO-SH-t21/t22 carried NOT RUN) covered the pending-order rule, not this field. The row is not edited in place (the gate refuses mutation); this row is the record of the correct value.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECHIST-Z-S2"
    ],
    "spec_asserts": "org/surprise_channel/schemas/remediation_row.schema.json: fabric is one of laptop, site-z, dell1, dell2, and is site-z iff the id carries the Z- infix.",
    "world_is": "Correction to REMEDIATION_v4 row MDPF_SECHIST-Z-S2: its fabric field reads 'sitez', which is not in the remediation_row schema enum (laptop, site-z, dell1, dell2); the correct value is 'site-z' (the id carries the Z- infix). The value landed in commit cfa051f0cd under an audited surprise-row-override whose stated reason (CTO msg 5020: TO-SH-t21/t22 carried NOT RUN) covered the pending-order rule, not this field. The row is not edited in place (the gate refuses mutation); this row is the record of the correct value.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO read org/missions/D8/MDPF/MDPF_SECHIST/surprise-channel/remediations/REMEDIATION_v4.md: Z-S2 fabric = 'sitez'",
        "org/surprise_channel/schemas/remediation_row.schema.json properties.fabric.enum = [laptop, site-z, dell1, dell2]",
        "commit cfa051f0cd body: '# surprise-row-override: TO-SH-t21 and TO-SH-t22 are carried NOT RUN by 1.0.0_SA_CTO~DELL1 msg 5020 ruling (a) ...'"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Correction to REMEDIATION_v4 row MDPF_SECHIST-Z-S2: its fabric field reads 'sitez', which is not in the remediation_row schema enum (laptop, site-z, dell1, dell2); the correct value is 'site-z' (the id carries the Z- infix). The value landed in commit cfa051f0cd under an audited surprise-row-override whose stated reason (CTO msg 5020: TO-SH-t21/t22 carried NOT RUN) covered the pending-order rule, not this field. The row is not edited in place (the gate refuses mutation); this row is the record of the correct value."
  }
]
```

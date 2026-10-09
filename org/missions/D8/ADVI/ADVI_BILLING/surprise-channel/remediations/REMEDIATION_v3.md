# ADVI_BILLING -- round 3 remediations

<sweep_watermark>2026-10-09T10:15Z</sweep_watermark>

Graduated at round 3's L8 (ADJUDICATION_v3.md), round label v4: D2-W7-S1, OPEN (site Z's release).

```json
[
  {
    "id": "ADVI_BILLING-D2-W7-S1",
    "project": "ADVI_BILLING",
    "fabric": "dell2",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The order registers copy_site_file_to_s3 in tools.py only; the gateway also classifies every tool in app/destructive_ops.py (TOOL_WRITE_CLASS, DESTRUCTIVE_OPS) and app/data_entitlement.py (NATIVE_TOOLS), both outside this grant, so the new write tool is fail-closed: a call returns confirm_required (blast_cap) and write_class UNCLASSIFIED denies every tier.",
    "evidence": [
      "investigation row ADVI_BILLING-D2-W7-S1",
      "org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/r3_close/DRAIN_END_R3.md @a62249088d"
    ],
    "remedy": "Site Z's gateway release classifies copy_site_file_to_s3 in app/destructive_ops.py (TOOL_WRITE_CLASS, DESTRUCTIVE_OPS) and app/data_entitlement.py (NATIVE_TOOLS) beside its tools.py registration, so the write tool is not fail-closed; then the Q3 2026 statement lands.",
    "owner": "0.0.0_AB_MSTR~DELL2 (cross-fabric to site Z, msg 3083)",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~DELL2 (site Z)",
      "round": "v4"
    },
    "closed": false
  }
]
```

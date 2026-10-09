# ADVI_COTBKF: remediations, round 43

<sweep_watermark>2026-10-09T14:53Z</sweep_watermark>

Graduated at round 43's L9 (ADJUDICATION_v32.md), round label v44: W70-S1, OPEN.

```json
[
 {
  "id": "ADVI_COTBKF-D2-W70-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The producer's build_manifest() writes method_version = METHOD_VERSION (2, the custodian-equity method row) into every returns manifest regardless of the source entry, so Cottonwood's built manifests state method_version 2 beside valuation_source=positions_x_as_traded_close while the rows carry method_version NULL.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W70-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_43_DRAIN_END_20261009.md @7f2f3d7323 (msg 3499)"
  ],
  "remedy": "Rule before the CB-al-2 mint: IRPT_DASHBD's build_manifest() stamps method_version from the source entry's declared method (an IRPT_DASHBD cell), or the mismatch is accepted and stated on each Cottonwood manifest.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v44",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v44"
  },
  "closed": false
 }
]
```

# ADVI_COTBKF -- round 6 remediations

<sweep_watermark>2026-10-07T10:30Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~10:5xZ. Graduated at this compile (ADJUDICATION_v5.md): 1 row, round label v7, S14,
REMEDIATED and closed: CB-f-1 made the hold-back match the restricted path in any bucket.

```json
[
 {
  "id": "ADVI_COTBKF-S14",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "commonwealth_documents.py's C-RESTRICTED hold-back builds the restricted prefix from opal_naming.address(..., 'bronze', 'crm', ...), which resolves to opal-data-assets, and compares full URIs; register X15 puts the restricted prefix in opal-data-cottonwood, so the guard watches a prefix in the wrong bucket. Inert today: the documents write only opal-data-assets silver (held_restricted=0 both ways).",
  "evidence": [
   "investigation row ADVI_COTBKF-S14",
   "infra/logic/06_CONFORMANCE_LEDGER.md:149 (X15)",
   "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_6_DRAIN_END_20261007.md @f6d26131f1: CB-f-1 (restricted path in any bucket) drained @fa9d12daa1, AC1 5 passed with a difference control"
  ],
  "remedy": "Done in code by CB-f-1 (match the restricted path in any bucket). It closes on the next documents run reading held_restricted from the bucket-agnostic guard; the packet's run after the drain reads held_restricted=0, crm_source_keys=0.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v7",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v7"
  },
  "closed": true
 }
]
```

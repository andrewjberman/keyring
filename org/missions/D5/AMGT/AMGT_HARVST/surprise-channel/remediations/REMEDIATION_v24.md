# AMGT_HARVST -- round 93 remediations (dell1)

<sweep_watermark>2026-10-18T05:31:08Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T05:31:08Z. Graduated at ADJUDICATION_v87 (C-S67): 1 row, owner 2.0.0_SA_COO~W1.

```json
[
  {
    "id": "AMGT_HARVST-D1-W165-S3",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "substrate._pick_stored falls back to sorted(docs)[-1] (substrate.py:158), a pick by key order, when no stored object matches the build's inputs.",
    "evidence": [
      "investigation row AMGT_HARVST-D1-W165-S3",
      "adjudication row AMGT_HARVST-D1-C-S67 (ADJUDICATION_v87)"
    ],
    "remedy": "The fallback picks by method version then written time, as ch-1's picker does, or raises. Close when: a census over all 95 partitions reports the no-input-match count, and the fallback's rule is named.",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v93",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v93"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO

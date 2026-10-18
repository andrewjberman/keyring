# AMGT_HARVST -- round 91 remediations (dell1)

<sweep_watermark>2026-10-17T23:10:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-17T23:10:20Z. Graduated at ADJUDICATION_v85 (C-S63): 1 row, owner 2.0.0_SA_COO~W1.

```json
[
  {
    "id": "AMGT_HARVST-D1-S46",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "typed.py::_find_fund takes the first fund token of a report's RECOMMENDATION line whatever its verb, so the silver research_reports[].fund carries a candidate's or template's fund (ADBE, SNPS, MNST: PFOE; ML_FP: IDVZ; CLX: DIVZ).",
    "evidence": [
      "investigation row AMGT_HARVST-D1-S46",
      "adjudication row AMGT_HARVST-D1-C-S63 (ADJUDICATION_v85)"
    ],
    "remedy": "Re-derive research_reports[].fund from a holding line only, or carry the stance beside it, under a never-widen pair for the silver rebuild. Close when: ADBE's served research_reports[0] no longer reads a fund it is not held in, with a count of the rows moved.",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v91",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v91"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO

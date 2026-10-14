# ADVI_FIRMBKTS -- round 6 remediations (dell1)

<sweep_watermark>2026-10-13T08:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T08:20:00Z. Graduated at ADJUDICATION_v7: 1 row. FWD-1 PARTIAL on the agreement arm (D1-C-S45; carried by
REMEDIATION_v2 D1-S3).

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-S44",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The exec-summary emit fails on the runner with no exception text and the cause reads REGION_UNSET (inferred); the order's probe step collides with the runner's standing access policy, and the 'no CloudTrail PutEvents' premise is not a discriminator.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S44",
      "adjudication rows ADVI_FIRMBKTS-D1-C-S46, D1-C-S48"
    ],
    "remedy": "The round-7 fix cell under a never-widen pair (CTO + COO halves): a region for the dispatcher's CLI, a sample read first, prior VersionIds as rollback; the first chain close after it is read for the emit and the summaries. Close when: an emitted chain-complete event and the generator's run are recorded",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v7"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": true
  }
]
```

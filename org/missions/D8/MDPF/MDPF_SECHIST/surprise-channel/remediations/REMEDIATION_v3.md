# MDPF_SECHIST -- round 4 remediations

<sweep_watermark>2026-10-09T16:24Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T16:24:00Z. Graduated at ADJUDICATION_v5: 1 row, INERT.

```json
[
  {
    "id": "MDPF_SECHIST-D1-W14-S1",
    "project": "MDPF_SECHIST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The gold Lambda's gap-record write goes to s3://opal-data-etfs/bloomberg/etfs/silver/history_gaps/as_of=<d>/gap_record.json, but etf-positioning-producer-role grants s3:PutObject on opal-data-etfs/gold/* only, so once gold deploys every scheduled run would log 'gap record: WRITE FAILED' and no record would persist (FWD-4 degrades silently). Not live: gold is not deployed.",
    "evidence": [
      "investigation row MDPF_SECHIST-D1-W14-S1 (ARMED, grounding INFERRED: role policy unread)",
      "3.0.0_SA_CVO comp-iam service etf-positioning-producer at ~16:3xZ: role etf-positioning-producer-role, s3:PutObject resources = opal-data-etfs/gold/* only; read resources config/etf_universe.json, silver/holdings/*, silver/netassets/*, bbg/*, bbg-testpull/tickers/*; no bloomberg/etfs/silver/history_gaps/* grant (the row's world_is now MEASURED)",
      "disarm ruling @912e4704b0 (DECOMP_R4): the gold deploy order carries the grant; its acceptance reads the record object; a WRITE FAILED line or an absent object fails the deploy"
    ],
    "remedy": "The gold deploy order adds s3:PutObject on opal-data-etfs/bloomberg/etfs/silver/history_gaps/* to etf-positioning-producer-role (Terraform, safe-apply), plus read on the same prefix if the next pull reads it from the Lambda. Close when: the first scheduled gold run after deploy writes gap_record.json for its as_of date and its log carries no WRITE FAILED line",
    "owner": "2.0.0_SA_COO~H1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~H1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~H1",
      "at": "2026-10-09T16:24:00Z"
    },
    "closed": false
  }
]
```

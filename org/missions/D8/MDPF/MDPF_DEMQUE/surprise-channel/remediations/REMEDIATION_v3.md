# MDPF_DEMQUE -- round 4 remediations

<sweep_watermark>2026-10-09T09:01Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T09:01:00Z. Graduated at ADJUDICATION_v4: 2 rows, both INERT.

```json
[
  {
    "id": "MDPF_DEMQUE-D1-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The Yahoo-backfill split ruling makes MDPF_SECHIST the one writer of stored price series, but DEMQUE's price store is the only Yahoo writer that exists (32 securities, read by dell2's ADVI_COTBKF; up to 150 more at the next draw) and SECHIST has none.",
    "evidence": [
      "investigation row MDPF_DEMQUE-D1-S2"
    ],
    "remedy": "Rule the end state as a PORT, never two writers side by side (CLAUDE.md shadow-pipeline veto): SECHIST's writer takes over the same rows, the consumer re-points, same-window rollback; or re-rule DEMQUE as the writer. Close when: the ruling is recorded and, if a port, it lands in one window",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_DEMQUE-Z-W1-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The OPAL_BBGTML scheduled runner and its two notebooks (market_indices_data_pull, model_portfolio_regression_analysis) make Bloomberg draws with no budget record call, so the demand ledger's coverage of the daily load is held, not measured complete.",
    "evidence": [
      "investigation row MDPF_DEMQUE-Z-W1-S2 (site Z text search of the three sources: no bbg_budget or .record( call)"
    ],
    "remedy": "Meter those draws on the ledger (C-METER, C-PRODUCERS: the queue records, the producer is not rewritten -- a record call or a wrapper at the runner), or carry them as a named unmetered line. Close when: a scheduled day's ledger carries the notebook draws or names them as unmetered",
    "owner": "2.0.0_SA_COO~Q1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Q1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Q1",
      "at": null
    },
    "closed": false
  }
]
```

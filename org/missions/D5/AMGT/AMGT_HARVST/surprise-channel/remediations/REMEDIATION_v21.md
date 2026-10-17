# AMGT_HARVST -- round 90 remediations (dell1)

<sweep_watermark>2026-10-17T19:52:03Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-17T19:52:03Z. Graduated at ADJUDICATION_v84 (C-S60): 2 rows, owner 2.0.0_SA_COO~W1.

```json
[
  {
    "id": "AMGT_HARVST-D1-C-S61",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The fund rule (and the ce-2 line fallback) takes the first fund token of a RECOMMENDATION line whatever its verb, so MNST's 'RECOMMENDATION: CANDIDATE FOR PFOE' is served as fund_of_record PFOE, a candidate read as a holding.",
    "evidence": [
      "adjudication row AMGT_HARVST-D1-C-S59 (ADJUDICATION_v84), this seat's served read of MNST_US_Equity"
    ],
    "remedy": "fund_of_record is set only from a holding verb (maintain, hold, add, buy, or the like), and a candidate line is served as a candidate, not a fund of record. Close when: MNST serves no fund_of_record from a candidate line, with a census of how many served names had one.",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v90",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v90"
    },
    "closed": false
  },
  {
    "id": "AMGT_HARVST-D1-S44",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The seat's serial gold-write driver (nohup python ce4_run.py) died silently mid-run; no event, memory limit or reaper was found, and buffered output hid the last lines.",
    "evidence": [
      "investigation row AMGT_HARVST-D1-S44",
      "adjudication row AMGT_HARVST-D1-C-S60 (ADJUDICATION_v84)"
    ],
    "remedy": "Long unattended write runs start detached, unbuffered and logged, with the exit status recorded. Close when: the next write run's record carries its exit status and its last lines.",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v90",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v90"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO

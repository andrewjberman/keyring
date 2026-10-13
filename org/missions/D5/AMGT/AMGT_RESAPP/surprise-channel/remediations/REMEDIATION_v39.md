# AMGT_RESAPP -- round 102 remediations (dell1)

<sweep_watermark>2026-10-13T17:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T17:05:00Z. Graduated at ADJUDICATION_v124: 1 row, ARMED.

```json
[
  {
    "id": "AMGT_RESAPP-D1-W402-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The first overlay a container serves runs about 20 s whether or not the container is cold (run 1 q2 20.08 s with no Init; the cold first request 4737aa2a 20.57 s on bKCGUhXp), because read_feed calls _timeline_snapshot_rows('article_security_mention') (scoped_amgt.py:5657), which loads the gold table for ALL securities and filters in Python: the feed phase is 18,796 ms of 20,566 ms (91.4 percent). Later overlays on that container reuse the read (49 ms).",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W402-S1",
      "adjudication rows AMGT_RESAPP-D1-C-S112, D1-C-S113, D1-C-S116"
    ],
    "remedy": "The CTO's round-103 feed cell: read only the subject's rows (a partition or predicate on security_key, or the column subset the feed uses). Close when: a first request on a new package, driven alone, has feed under the bound the cell states and its phases sum within 5 percent (r102_first_cold_request.py, r102_phase_table.py), beside a control warm overlay whose bytes are unchanged.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v102",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v102"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  }
]
```

# AMGT_HARVST -- round 95 remediations (dell1)

<sweep_watermark>2026-10-18T11:51:23Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T11:51:23Z. Graduated at ADJUDICATION_v89 (C-S71): 3 rows, all ARMED, owner and disarm owner 2.0.0_SA_COO~W1; each waits on a CTO ruling.

```json
[
  {
    "id": "AMGT_HARVST-D1-W171-S3",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The deployed gateway artifact ships lib/ with trading_calendar.py and opal_naming.py only, so app/harvest_research.py carries a copy of crosswalk.py's slash-key rule (lines 196-247); one test arm (test_cj2_slash_key_one_form arm 7, 105 keys) is all that holds the copy to the module.",
    "evidence": [
      "investigation row AMGT_HARVST-D1-W171-S3",
      "adjudication row AMGT_HARVST-D1-C-S71 (ADJUDICATION_v89)"
    ],
    "remedy": "The CTO rules (open call dell1-20261018T093742Z-48ae): ship the module in the artifact, or keep the copy with its test in every gateway release's test list. Close when: the ruling is on file and the next gateway release's test list shows the arm run, or the artifact imports the module.",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v95",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v95"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~W1",
      "at": null
    }
  },
  {
    "id": "AMGT_HARVST-D1-W171-S4",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The peers/v1, posture/v1, scores/v1 and filings/v1 prefixes hold objects under both spellings of a slash key (peers BP raw 7, encoded 10), and the gateway tools keep the caller's spelling, so a raw and an encoded request read different sets.",
    "evidence": [
      "investigation row AMGT_HARVST-D1-W171-S4",
      "adjudication row AMGT_HARVST-D1-C-S71 (ADJUDICATION_v89)"
    ],
    "remedy": "The CTO rules which spelling a reader takes (stored objects are never renamed), or accepts the standing state with a reason. Close when: a raw and an encoded request for BP/_LN_Equity read the same object set on each of those tools, or the ruling accepting the split is on file.",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v95",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v95"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~W1",
      "at": null
    }
  },
  {
    "id": "AMGT_HARVST-D1-W171-S6",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "harvest_security_coverage differs across the two spellings in its path-component templates (derived/model_block BP raw 6, encoded 24; peers raw 7, encoded 10); every partition dataset matches.",
    "evidence": [
      "investigation row AMGT_HARVST-D1-W171-S6",
      "adjudication row AMGT_HARVST-D1-C-S71 (ADJUDICATION_v89)"
    ],
    "remedy": "Follows the W171-S4 ruling. Close when: coverage for BP/_LN_Equity and BP-SLASH-_LN_Equity reads equal on all 14 cells, or the ruling accepting the split is on file.",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v95",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v95"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~W1",
      "at": null
    }
  }
]
```

-- 3.0.0_SA_CVO

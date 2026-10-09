# AMGT_RESAPP -- round 83 remediations (dell1)

<sweep_watermark>2026-10-09T10:23Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T10:23:00Z. Graduated at ADJUDICATION_v101: 2 rows, both INERT.

```json
[
  {
    "id": "AMGT_RESAPP-D1-W332-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "fetch.py:417 stamps the source's language from the head of the whole document (the cover page), so an English 20-F reads pt (BABA) or es (SAP), and analyze writes the draft in that language.",
    "evidence": [
      "investigation rows AMGT_RESAPP-D1-W332-S1 (BLOCKING, was ARMED) and D1-S12 (disarm)",
      "packet s.5 item 1"
    ],
    "remedy": "Stamp the language from the cut sections (site-Z producer path), then the store half for BABA, SAP and PBR. Close when: BABA's and SAP's sources read en and their drafts serve in English",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v84",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v84"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": "2026-10-09T10:23:00Z"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-W332-S2",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "drafting_build --splice-driver was not re-run on ASML's new draft; its dry run moves only the provenance key, because analyze 2.1.0 already writes the thesis driver.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W332-S2",
      "packet s.5 item 2"
    ],
    "remedy": "Run the provenance splice or rule it unneeded. Close when: the ruling is recorded or ASML's served draft carries the spliced provenance",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v84",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v84"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  }
]
```

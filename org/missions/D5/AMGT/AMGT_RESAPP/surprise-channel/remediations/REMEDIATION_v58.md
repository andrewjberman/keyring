# AMGT_RESAPP -- round 118 remediations (dell1)

<sweep_watermark>2026-10-18T11:33:58Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T11:33:58Z. Graduated at ADJUDICATION_v157 (C-S194): 3 rows, owner 2.0.0_SA_COO~R1; 1 ARMED, disarm owned by 2.0.0_SA_COO~R1.

```json
[
  {
    "id": "AMGT_RESAPP-D1-W515-S2",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The pack's Appendix figure lines print a served source and a served basis definition unchanged; the figure-line functions are not routed through _plain_reason.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W515-S2",
      "adjudication row AMGT_RESAPP-D1-C-S194 (ADJUDICATION_v157)"
    ],
    "remedy": "The Appendix's served source and definition segments go through the mapper, or the CTO rules them out of scope. Close when: a unit control feeding an s3 path into a figure's source prints no path, and the 101-name live leak scan still reads clean.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v118",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v118"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": "2026-10-18T13:12:04Z"
    }
  },
  {
    "id": "AMGT_RESAPP-D1-W515-S3",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The rich export's measured money rows print the amount with no currency code (ICT PM market cap '1735465117699.9998 ABSOLUTE (full currency units)'), while the PDF prints 'PHP 1,735,465.1 million'.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W515-S3",
      "adjudication row AMGT_RESAPP-D1-C-S194 (ADJUDICATION_v157)"
    ],
    "remedy": "The CTO rules whether the export's measured rows carry the page's currency code; then they follow. Close when: the ICT PM export prints PHP on its market cap and USD on its enterprise value, or the ruling that keeps the export code-free is on file.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v118",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v118"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-C-S195",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The rich export prints 'CEO public-profile reading: the object could not be read' (served reading UNREADABLE_OBJECT, render_pack.py:1520 and 1701-1705) on 8 of 8 captured names, while the same build's PDF prints HD US's served reading ('CEO public profile (EDWARD P. DECKER): The CEO web search returned 10 url(s) ...'). The two routes disagree on one served object; the cause is not read.",
    "evidence": [
      "adjudication row AMGT_RESAPP-D1-C-S194 (ADJUDICATION_v157)",
      "C:/dev/ui-walk-evidence/r118-rich-issuer-after/ and r118-packs-issuer-after/ (issuer's live captures, 8 names; client data stays local)"
    ],
    "remedy": "The rich route reads the same CEO profile reading the PDF route reads. Close when: the HD US rich export prints the reading the HD US PDF prints, and a census over the eight names shows the two routes agree.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v118",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v118"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO

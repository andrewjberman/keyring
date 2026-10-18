# AMGT_RESAPP -- round 117 remediations (dell1)

<sweep_watermark>2026-10-18T09:14:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T09:14:15Z. Graduated at ADJUDICATION_v156 (C-S192): 4 rows, owner 2.0.0_SA_COO~R1; 3 ARMED, disarm owned by 2.0.0_SA_COO~R1.

```json
[
  {
    "id": "AMGT_RESAPP-D1-W512-S2",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Two absent-posture states print two Positioning sentences: a served ABSENT posture prints 'No positioning view is on file for this name.', and a missing posture (posture=None, the route's read-raised case) prints the old 'No analyst posture is on file for this company yet.' (render_pack.py:781 and :794), pinned by api test D3.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W512-S2",
      "adjudication row AMGT_RESAPP-D1-C-S192 (ADJUDICATION_v156)"
    ],
    "remedy": "One absence sentence for both states, with test D3 re-scoped in the full tree. Close when: a pack built with posture=None and one built with an ABSENT posture print the same Positioning sentence.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v117",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v117"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-D1-W512-S3",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The Management builder's 'CEO public profile' line prints a served reading's reason verbatim when no management passage prints (render_pack.py:897-898), so a reason carrying a storage path or vendor error would print it.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W512-S3",
      "adjudication row AMGT_RESAPP-D1-C-S192 (ADJUDICATION_v156)"
    ],
    "remedy": "The line prints a plain sentence, never a served reason string. Close when: a test feeding a reason with an 's3://' path and a vendor error reads neither in the PDF text, and a live pack for a name with no passage (HD US or TSM US) prints the plain sentence.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v117",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v117"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-D1-W512-S4",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The rich markdown export (build_rich_text, fmt=rich) prints served reasons with storage paths and vendor error text, where the PDF and .txt now print plain sentences.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W512-S4",
      "adjudication row AMGT_RESAPP-D1-C-S192 (ADJUDICATION_v156)"
    ],
    "remedy": "The CTO rules whether the export takes the plain-sentence wording; then the export and its re-scoped test pair follow. Close when: the rich export for RIO LN, ICT PM and GOOGL US carries 0 's3://' and 0 order ids, or the ruling that keeps the export's wording is on file.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v117",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v117"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-D1-W513-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The pack's .md document (pack_<sec>.md) prints the raw served amount for a header money figure the PDF and .txt withhold, through _figures_table, which renders render_figure_line verbatim.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W513-S1",
      "adjudication row AMGT_RESAPP-D1-C-S192 (ADJUDICATION_v156)"
    ],
    "remedy": "The .md header table follows the same withhold rule as the PDF. Close when: RIO LN's .md prints no amount for market cap, net debt or enterprise value and carries the page's words instead.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v117",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v117"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO

# AMGT_RESAPP -- round 116 remediations (dell1)

<sweep_watermark>2026-10-18T06:17:21Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T06:17:21Z. Graduated at ADJUDICATION_v154 (C-S188): 4 rows, owner 2.0.0_SA_COO~R1.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S189",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The printed pack's Summary prints 'No recommendation has been written for this company yet.' when the served research holds a cited last_stated_position: RIO LN 'MAINTAIN 2.75% POSITION IN IDVZ', ICT PM 'MAINTAIN 1.75% POSITION IN IDVZ', GOOGL US 'Maintain positions in PFOE and DIVZ'.",
    "evidence": [
      "adjudication row AMGT_RESAPP-D1-C-S187 (ADJUDICATION_v154)",
      "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116/packs/RIO_LN_Equity_pack.pdf page 1",
      "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116/packs/ICT_PM_Equity_pack.pdf page 1",
      "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116/packs/GOOGL_US_Equity_pack.pdf page 1"
    ],
    "remedy": "The Summary prints the last stated recommendation with its source report and period when one is served, and says none is written only when none is. Close when: fresh RIO LN, ICT PM and GOOGL US packs print their stated recommendation with its source, and a census over the packed names counts those with a served last_stated_position whose pack says none is written (expected 0).",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v116",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v116"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-C-S190",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The printed pack's Positioning section prints 'Posture: ABSENT -- no O-1 posture object under s3://opal-data-harvest/posture/v1/<KEY>/ -- AMGT-rj-11 has not landed one.', an internal store path, an object-class token and an order id, on all three round-116 packs.",
    "evidence": [
      "adjudication row AMGT_RESAPP-D1-C-S187 (ADJUDICATION_v154)",
      "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116/packs/RIO_LN_Equity_pack.pdf page 1"
    ],
    "remedy": "The absent-posture sentence is plain words for a reader (for example, that no positioning view has been written yet), with no store path, object class or order id. Close when: a fresh pack with no posture prints no 's3://', no order id and no object-class token, and the pack text census for those three patterns reads 0.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v116",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v116"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-W511-S6",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The pack's Positioning comparable label reads only the posture's comparable_identity and comparable_name; the page also falls back to the comparable's own thesis identity, so the pack can print 'a comparable the research team has not identified' where the page names the comparable's ticker. The sentence is also ungrammatical.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W511-S6",
      "adjudication row AMGT_RESAPP-D1-C-S188 (ADJUDICATION_v154)"
    ],
    "remedy": "The pack names the comparable the way the page does, or prints a grammatical sentence when it cannot. Close when: on a name with a posture whose comparable has no comparable_name, the pack and the page print the same comparable.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v116",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v116"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-W511-S9",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The fmt=rich branch of scoped_amgt._print_pack reads the thesis bundle, the peer set and the posture unguarded, so one raising reader fails the rich export with a 500 while the PDF route degrades to an absent section.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W511-S9",
      "adjudication row AMGT_RESAPP-D1-C-S188 (ADJUDICATION_v154)"
    ],
    "remedy": "The rich branch degrades the way the PDF branch does. Close when: a test that raises each of the three readers on the rich route reads a served export with that section marked absent, not a 500.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v116",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v116"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO

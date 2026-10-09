# AMGT_RESAPP -- round 82 remediations (dell1)

<sweep_watermark>2026-10-09T08:49Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T08:49:00Z. Graduated at ADJUDICATION_v100: 4 rows, all INERT.

```json
[
  {
    "id": "AMGT_RESAPP-D1-W324-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "On a re-cut, re-analyzed ASML NA the repaired cutter delivers Item 4.B and the analysis runs, but 0 of 11 served /thesis locations cite Item 4.B: the draft served 5 sentences and the verbatim gate dropped 14. ASML was rolled back byte-equal (disarm row D1-S11).",
    "evidence": [
      "investigation rows AMGT_RESAPP-D1-W324-S1 (BLOCKING, was ARMED) and D1-S11 (disarm)",
      "packet s.1 gg-2 and s.5 item 1"
    ],
    "remedy": "Repair the analysis/drafting side or the served-location rule, proved offline on ASML's stored excerpt, then the store half (ASML, BABA, NU, SAP) and the FWD-18 walk. Close when: a served ASML /thesis cites Item 4.B and the walk reads it",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v83",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v83"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": "2026-10-09T08:49:00Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-W323-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "PBR's extracted 20-F text has no body heading for 'Our Business' or 'Operating and Financial Review and Prospects', so the cross-reference mode cuts business from 'About us' and mdna from a sub-heading. PBR was never written (disarm row D1-S10).",
    "evidence": [
      "investigation rows AMGT_RESAPP-D1-W323-S1 (was ARMED) and D1-S10 (disarm)",
      "packet s.5 item 2"
    ],
    "remedy": "Cut PBR's business and MD&A from their real sections, proved on the stored filing before any write. Close when: PBR's cut reads the right sections offline",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v83",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v83"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": "2026-10-09T08:49:00Z"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-W324-S2",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "r81_store.py AC1 S3 matches the heading label case-sensitively, so 'ITEM 4.B. BUSINESS OVERVIEW' reads FAIL on a section that opens on its own heading.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W324-S2",
      "packet s.5 item 3"
    ],
    "remedy": "Make S3 case-insensitive with a negative control. Close when: S3 reads PASS on ASML's stored excerpt and FAIL on a planted mis-cut",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v83",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v83"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-W324-S3",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "comp-secrets get anthropic-api-key --reveal without --value-only printed the model key's cleartext into a worker's local tool output; 0 commits carry it (per the row) and no request reached the vendor with it.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W324-S3",
      "packet s.4: rotation asked of 0.0.0_AB_MSTR~DELL1 at 08:44Z"
    ],
    "remedy": "Rotate the key (MSTR, asked) and make comp-secrets' --reveal never print the value inside an exported descriptor. Close when: the key is rotated and a --reveal descriptor export prints no value",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v83",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v83"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  }
]
```

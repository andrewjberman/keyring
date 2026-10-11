# AMGT_RESAPP -- round 93 remediations (dell1)

<sweep_watermark>2026-10-11T12:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T12:20:00Z. Graduated at ADJUDICATION_v113: 1 row, ARMED.

```json
[
  {
    "id": "AMGT_RESAPP-D1-S23",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The display-name chain (_display_name_for / monthly_chatter._display_names) serves SAN_FP_Equity (Sanofi) as 'Banco Santander S.A.' from etf-classifications, and _held_name_index maps both 'sanofi' and 'banco santander s a' to SAN_FP_Equity. The page header for Sanofi names a different company; a peer row named 'Banco Santander, S.A.' would take Sanofi's key through pp-1's exact-name arm (no set lists it today). The symptom matches a ticker collision (SAN on Madrid and Paris) in the classification join; the cause is not read.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S23",
      "adjudication row AMGT_RESAPP-D1-C-S69 (this seat's live overlay and peers reads)"
    ],
    "remedy": "The CTO's round-94 cell 1: the display-name chain must not take a classification name that disagrees with the registered name, and the held-name index carries one company per key; a census of every subject whose served display name differs from its crosswalk company, count printed. Close when: GET /security/SAN_FP_Equity/overlay serves a Sanofi name, the index maps 'banco santander s a' to no Sanofi key, beside a control held key whose served name is unchanged.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v93",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v93"
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

# IRPT_BCKEND -- project sweep 22 remediations

<sweep_watermark>2026-10-08T20:07Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-08. Graduated at sweep 22 (ADJUDICATION_v39.md), round label v84. 1 row, OPEN,
disarmed by ruling: custody fails closed until ACTIVE.

```json
[
  {
    "id": "IRPT_BCKEND-D2-W178-S2",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Pin P packages E8's custody family as PENDING_ENFORCEMENT, and the packaged retention admits only an ACTIVE row, so releasing P does not make a CUSTODY_REPORT retainable or readable; the flip to ACTIVE is a registry change that needs its own repin and release.",
    "evidence": [
      "investigation rows IRPT_BCKEND-D2-W178-S2, D2-S8",
      "8530114ff9 (E8: irpt-custody-x10-v1 PENDING_ENFORCEMENT, irpt-x10-v1 byte-unchanged)",
      "release-census --pin 0a57f3c0e9 (this compile)"
    ],
    "remedy": "Flip irpt-custody-x10-v1 to ACTIVE, repin the registry row and release under its own pair (the issuer recommends E10's), with the custody owner read as the after-read.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v84",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v84"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P2",
      "at": "2026-10-08T20:05:00Z"
    }
  }
]
```

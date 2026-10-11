# AMGT_RESAPP -- round 90 remediations (dell1)

<sweep_watermark>2026-10-11T06:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T06:10:00Z. Graduated at ADJUDICATION_v110: 1 row, INERT.

```json
[
  {
    "id": "AMGT_RESAPP-D1-S20",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The live _with_numeric_tickers (AMGT-av-5) resolves an all-digit non-US scanner ticker by its Japan code or a held company's exact name (29 of 769 served: 22 by name, 7 by code), but no code path serves the other 1,047 non-US rows (SEDOL stems, star-tickers, class-share tickers); 23 of them name exactly one held company. Ceiling 52 of 1,816; 1,764 keep plain reasons. The round-90 cell (oo-4) was deferred to round 91 by the to-pipeline-gate (one issuance per round).",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S20",
      "3.0.0_SA_CVO ran round90_prep/reads/r90_measure_nonus3.py at 77c9e22a81: non-US rows 1816, all-digit 769 (company_name 22, japan_exchange_code 7, reason 740), other forms 1047, exact one-held-name matches 23 of 1047",
      "round90_prep/DRAFT_ORDER_for_round91_a-non-us-peer-the-held-list-names-exactly-serves-that-identity.md and checks/r90_name_match.py exist at HEAD"
    ],
    "remedy": "Round 91's build cell extends the exact-name arm to non-digit non-US tickers. Close when: r90_name_match.py passes 7 of 7 on the merged module and the 23 rows serve their held identity on a deployed read. The cell should also say why HEI.A (HEICO Corporation Class A -> HEI_US_Equity) sits in the non-US partition.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v90",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v90"
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

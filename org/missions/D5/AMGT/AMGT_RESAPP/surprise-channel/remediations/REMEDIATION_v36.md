# AMGT_RESAPP -- round 92 remediations (dell1)

<sweep_watermark>2026-10-11T10:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T10:15:00Z. Graduated at ADJUDICATION_v112: 3 rows (W381-S1 ARMED; S22 disarmed, work owed; S21 INERT).

```json
[
  {
    "id": "AMGT_RESAPP-D1-W381-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "On dell1, .tools/git-hooks/client-data-check.py reads its hashed account-id list from $OPAL_ACCOUNT_ID_HASHES, else ~/.opal/account_id_hashes.txt; neither exists (~/.opal/ holds only demque/), so the check WARNs and passes, and no commit made on this device is checked for client account ids.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W381-S1",
      "adjudication row AMGT_RESAPP-D1-C-S62",
      "3.0.0_SA_CVO ls -la C:/Users/Test/.opal/ 2026-10-11T10:1xZ"
    ],
    "remedy": "Provision the hashed list on dell1 (device setup, infrastructure lane), or make the check fail closed where the list is absent. Close when: a dell1 commit staging a planted test account id is REFUSED by client-data-check.py, beside a control commit that passes.",
    "owner": "1.0.0_SA_CTO",
    "round": "v92",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v92"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": "2026-10-13T14:55:00Z"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-S22",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The point verifier checks that a figure's digits sit in its period's block, not that a series' figures share a scale: SAP's re-verified driver would serve 2023 = 13,745 and 2024 = 18,078 (EUR millions) beside a 2025 figure in EUR billions. qq-4 held SAP out of the write (AMENDMENT 1), so nothing mixed is served today.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S22",
      "adjudication row AMGT_RESAPP-D1-C-S63",
      "qq-4 AMENDMENT 1 @35d5d641be"
    ],
    "remedy": "A verifier rule for a mixed-scale series (packet section 6 item 1): a point set whose unit renderings differ by a thousand/million/billion token is held as a set unless the excerpt states the conversion; then SAP under its own never-widen pair. Close when: the SAP mixed set is held by the rule (not by --hold), beside a control same-scale series that verifies.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v92",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v92"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": "2026-10-11T10:15:00Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-S21",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A subject can list its own company among its peers: 7 of 243 subjects live, 10 after pp-1 (issuer's count); membership is the scanner's, and the identity arms now say so.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S21",
      "adjudication row AMGT_RESAPP-D1-C-S64"
    ],
    "remedy": "Exclude a member whose served key equals the subject's own (an engine rule; packet section 6 item 2), on the CTO's ruling. Close when: a live read of all subjects shows 0 self-peers, beside a control subject whose peer count drops by exactly its self rows.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v92",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v92"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": true
  }
]
```

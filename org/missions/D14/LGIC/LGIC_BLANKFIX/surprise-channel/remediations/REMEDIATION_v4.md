# LGIC_BLANKFIX -- remediations, round 5

<sweep_watermark>2026-10-08T13:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-08 ~13:4xZ. Graduated at this compile (ADJUDICATION_v4.md): 3 rows, INERT, not closed.
Carried open from REMEDIATION_v1.md: W2-S2.

```json
[
  {
    "id": "LGIC_BLANKFIX-S6",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A key-ruling row matches on the exact repository path of the file that declares the key. A path is not a stable identity: a move by any project un-matches the row without a word and the name prints as a hole again.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 3c07973c5c (49 rows, 0 ARMED) row S6",
      "adjudication row LGIC_BLANKFIX-C-S14"
    ],
    "remedy": "P2. The CTO rules what a declared_in matches on (the file's name under the root's source folder, or the declaring function), or that the check refuses a declared_in path that does not exist. Done when a moved file either still matches or is refused by name.",
    "owner": "1.0.0_SA_CTO",
    "round": "v6",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v6"
    },
    "closed": true
  },
  {
    "id": "LGIC_BLANKFIX-S7",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "One REAL FILE case of lib/tests/test_opal_naming_keyfill.py types a source path that IRPT_BCKEND moved (commit 8d66fb03da), so the script prints ok=False on the trunk; it is the invocation of BS2-AC1 and BS7-AC1, and pytest does not collect it.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 3c07973c5c (49 rows, 0 ARMED) row S7",
      "adjudication row LGIC_BLANKFIX-C-S14"
    ],
    "remedy": "P1. First item of the next round: the case finds the file by name under the root's source folder. Done when the script prints KEYFILL-TEST ok=True on the trunk.",
    "owner": "2.0.0_SA_COO~G",
    "round": "v6",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~G",
      "round": "v6"
    },
    "closed": true
  },
  {
    "id": "LGIC_BLANKFIX-S8",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The round-5 exercise check compares the whole live output with the saved file, so a name added to an UNMAPPED root by any project reads repeat=DIFFERS although every mapped line is identical.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 3c07973c5c (49 rows, 0 ARMED) row S8",
      "adjudication row LGIC_BLANKFIX-C-S14"
    ],
    "remedy": "P2. The check compares the mapped roots' lines and the totals, or runs on a pinned commit. Done when the check passes on the trunk after an unmapped root changes.",
    "owner": "2.0.0_SA_COO~G",
    "round": "v6",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~G",
      "round": "v6"
    },
    "closed": true
  }
]
```

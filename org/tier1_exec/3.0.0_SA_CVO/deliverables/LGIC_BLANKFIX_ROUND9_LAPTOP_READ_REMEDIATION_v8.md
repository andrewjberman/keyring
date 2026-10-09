# LGIC_BLANKFIX -- remediations, round 9

<sweep_watermark>2026-10-09T07:55Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-09 ~07:5xZ. Graduated at this compile (ADJUDICATION_v8.md): 3 rows, INERT, not closed.
Clocks advanced in REMEDIATION_v7.md: W1-S19 and W1-S21 (arms A1, B1, P1 and O1-O12 hold), W1-S22 (the placement step is
skipped while its switch is absent, naming-gate.py:2052), S12 (ROOTCHECK-TEST ok=True cases=324 and FWD6-ARMS ok=True arms=7
held=7 on the laptop trunk), W4-S6 (counted_at_caller=17; uncounted=1 sits on an unmapped root).

```json
[
  {
    "id": "LGIC_BLANKFIX-D1-S1",
    "project": "LGIC_BLANKFIX",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "round-close-check.py exact-matches the status word 'complete', so an order whose status carries a suffix reads open and is left out of the grade count, and orders outside the tree are not counted at all; MAY-CLOSE can be vacuous.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 3deb8704f1 row D1-S1",
      "adjudication row LGIC_BLANKFIX-C-S22"
    ],
    "remedy": "P1. The check reads the status's leading word, as the other gates do, and counts every order the project issues wherever it lives. Done when it counts round 8's 5 orders and NFRA_CTLPLN's 7 round-6 orders.",
    "owner": "1.0.0_SA_CTO",
    "round": "v10",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v10"
    },
    "closed": false
  },
  {
    "id": "LGIC_BLANKFIX-D1-W2-S2",
    "project": "LGIC_BLANKFIX",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "org/naming-place-override-audit.log is excluded by .gitignore's blanket *.log and no re-include names it, so each override stays on the box that made it, invisible to the CVO and other boxes.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 3deb8704f1 row D1-W2-S2",
      "adjudication row LGIC_BLANKFIX-C-S22"
    ],
    "remedy": "P1, before the placement switch goes on. Re-include the log as append-only, or carry each override as a surprise row. Done when an override made on one box is readable on the laptop after a box-sync.",
    "owner": "1.0.0_SA_CTO",
    "round": "v10",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v10"
    },
    "closed": false
  },
  {
    "id": "LGIC_BLANKFIX-S13",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "exercise_switch_on.py and exercise_override.py spawn a bare 'bash'; on a box with WSL, CreateProcess reaches System32 bash.exe before PATH and both scripts false-fail.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 3deb8704f1 row S13",
      "adjudication row LGIC_BLANKFIX-C-S22"
    ],
    "remedy": "P2. Resolve bash through .tools/git_bash_resolver.py or msys_safe_run(). Done when both scripts read ok=True on the laptop as run.",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v10",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v10"
    },
    "closed": false
  }
]
```

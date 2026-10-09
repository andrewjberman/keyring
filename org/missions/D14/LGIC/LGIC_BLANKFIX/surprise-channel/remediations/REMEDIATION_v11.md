# LGIC_BLANKFIX -- round 13 remediations (dell1)

<sweep_watermark>2026-10-09T12:14Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T12:14:00Z. Graduated at ADJUDICATION_v11: 4 rows, all INERT.

```json
[
  {
    "id": "LGIC_BLANKFIX-D1-W1-S7",
    "project": "LGIC_BLANKFIX",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The cadence list's new names for the 21 schedules carrying '49f' are refused by the live naming gate as new hand-kept carriers of the firm token (e.g. bd-49f-keepalive-sched -> blackdiamond-49f-keepalive-sched-15min), so those list lines cannot land as printed; the 10 carrying 'cot' were not run.",
    "evidence": [
      "investigation row LGIC_BLANKFIX-D1-W1-S7",
      "packet ROUND13_DRAIN_END rows"
    ],
    "remedy": "Rule how firm-token schedules are named (a registry row so the builder emits the firm segment, or a different list form). Close when: one 49f schedule's list name passes the gate",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v14",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v14"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "LGIC_BLANKFIX-D1-W1-S8",
    "project": "LGIC_BLANKFIX",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "10 of 180 list words are left undecided by the reader although the schedule states an expression; 8 fire 2-3 times a day under 'daily' or '45min' (e.g. finbert-scoring-post-ingestion-45min).",
    "evidence": [
      "investigation row LGIC_BLANKFIX-D1-W1-S8",
      "org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_fwd4_cadence.py output (UNDECIDED lines)"
    ],
    "remedy": "Give the 10 a word a reader agrees with, or rule the words for multi-fire-per-day schedules. Close when: the checker reads those 10 as agree",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v14",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v14"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "LGIC_BLANKFIX-D1-W2-S6",
    "project": "LGIC_BLANKFIX",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "20 of 254 stored-file lines (13 RIGHT, 7 FIX) have no key ruling and no key class; their source and owner are read only from the grader's address by the key grammar's slot order.",
    "evidence": [
      "investigation row LGIC_BLANKFIX-D1-W2-S6"
    ],
    "remedy": "Add key rulings for the 20 or rule the address-derived reading sufficient. Close when: the ruling is recorded",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v14",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v14"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "LGIC_BLANKFIX-D1-W2-S7",
    "project": "LGIC_BLANKFIX",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A key ruling's owner field names who moves the store (a directive or project), not the firm that owns the file, so it cannot fill the line's owner= value.",
    "evidence": [
      "investigation row LGIC_BLANKFIX-D1-W2-S7"
    ],
    "remedy": "Name the two fields apart in the key-ruling schema (mover vs firm owner). Close when: the schema and the census use distinct fields",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v14",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v14"
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

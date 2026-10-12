# IRPT_ANLREQ: CVO adjudication, rounds 14 and 15 (workstream Y)

<sweep_watermark>2026-10-11T23:37Z</sweep_watermark>

L9 grade, L8 compile and L10 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T23:37:38Z. Input: `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND14_Y_L8_COMPILE_20261011.md @73dd169157 (msg 6114)`.
**AR142-y-AC3J NOT MET as written. AR144-y-AC2J MET for the form's half. AR145-y-AC2J MET** (row D2-S64; `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUNDS_14_15_Y_L9_GRADE_20261011.md`).
8 rows dismissed below. 4 graduate OPEN in `remediations/REMEDIATION_v8.md`.

```json
[
  {
    "id": "IRPT_ANLREQ-C-S16",
    "project": "IRPT_ANLREQ",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T23:37:38Z",
    "one_line": "Rounds 14 and 15: dismissed, D2-W53-S5 and D2-W53-S6 (the two ARMED rows of the release census: a stored input refused on re-open, and a resident built from one pin) as DISARMED by the revert, with D2-S63, their owner's disarm record; D2-W53-S4 (the ticker check runs in the resident, not in a function; the CTO withdrew the live ask); D2-W52-S12 and S13 (order-text notes); D2-W52-S14 (a criterion that could not pass as ordered; ruled by amendment) and D2-W52-S15 (a words-only edit that changed a served answer by side effect; reverted with the build). Graduate: D2-W53-S7, S8, S9 and this seat's row D2-S64.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_ANLREQ-D2-S63",
      "IRPT_ANLREQ-D2-W53-S5",
      "IRPT_ANLREQ-D2-W53-S6",
      "IRPT_ANLREQ-D2-W53-S4",
      "IRPT_ANLREQ-D2-W52-S12",
      "IRPT_ANLREQ-D2-W52-S13",
      "IRPT_ANLREQ-D2-W52-S14",
      "IRPT_ANLREQ-D2-W52-S15"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence. An ARMED hazard disarms via the row's disarm owner.",
    "world_is": "The disarm is read by this seat only as the issuer's measured statement that the intake folder and ops/status.py equal the round's base; this seat did not run that diff. No IRPT_ANLREQ order is open (this seat's count of the order files: 47 complete).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-S63, D2-W53-S5, D2-W53-S6, D2-W53-S4, D2-W52-S12, D2-W52-S13, D2-W52-S14, D2-W52-S15",
        "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND14_Y_L8_COMPILE_20261011.md @73dd169157 (msg 6114)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Two hazards disarmed by a revert, their disarm record, and five order or instrument notes."
  }
]
```

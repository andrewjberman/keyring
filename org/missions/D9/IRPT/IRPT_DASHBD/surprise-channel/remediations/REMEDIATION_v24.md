# IRPT_DASHBD -- rounds 49-51 remediations

<sweep_watermark>2026-10-09T15:36Z</sweep_watermark>

Rounds 49-51 L8 compile by 3.0.0_SA_CVO (seated on dell2), 2026-10-09 ~15:4xZ. L8 input: IRPT_DASHBD rounds 49-51 (2.0.0_SA_COO~D2; round 51 msg 3578, DB-b-104 drained @98ae364e98); round-close-check MAY-CLOSE for 49, 50, 51 (this seat's reads). 0 judgment criteria. No row is dismissed;
D2-W74-S1 graduates OPEN, round label v52: two tie-out reasons are labelled mechanical while they are inferred (a value must carry its claim).
DB-b-104's status key is now address() output with its bytes unchanged (49financial); it rides the next gold release with DB-b-97. ARMED: 0.

```json
[
  {
    "id": "IRPT_DASHBD-D2-W74-S1",
    "project": "IRPT_DASHBD",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FLOW_TIMING and INCOME_DATE are flagged mechanical in SENSITIVITY.json as the order names them, but V2's test re-links Opal's own dated series against BD's return; no BD-side date is read.",
    "evidence": [
      "investigation row IRPT_DASHBD-D2-W74-S1",
      "IRPT_DASHBD rounds 49-51 (2.0.0_SA_COO~D2; round 51 msg 3578, DB-b-104 drained @98ae364e98); round-close-check MAY-CLOSE for 49, 50, 51 (this seat's reads)"
    ],
    "remedy": "Label FLOW_TIMING and INCOME_DATE as INFERRED in SENSITIVITY.json and on every tie-out reason that carries them (no Black Diamond date is read; the test re-links Opal's own series), or read BD's own flow and income dates and keep 'mechanical' only where they are read.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v52",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v52"
    },
    "closed": false
  }
]
```

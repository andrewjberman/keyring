# TCKT_VNEXT: CVO adjudication, the fourteen rows the issuer listed

<sweep_watermark>2026-10-11T14:33Z</sweep_watermark>

By `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T14:33:12Z. Input: `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R4_RUN/STALE_ROW_DISPOSITIONS_FOR_CVO_20261011.md @5719b01097 (msg 5123)`.
Of the fourteen, five already carried a disposition in this channel's files; nine are adjudicated below, three on this seat's own
reads and six on the issuer's quoted slug lines. **D2-W6-S2 stays ARMED** (owner `1.0.0_SA_CTO~DELL2`): the data-refresh route admits a
caller with no user type.

**Owed by this seat:** 40 INERT rows of rounds 1 to 3 are uncompiled. The compile and the slug wait on the two pending orders.

```json
[
  {
    "id": "TCKT_VNEXT-C-S5",
    "project": "TCKT_VNEXT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T14:33:12Z",
    "one_line": "Three rows this seat has its own read on: D2-S18 (ARMED: irpt-status answered 500 on 7 routes; the function was rolled back, and this seat has read it live on revision 6 several times today), D2-S28 (the precheck's hand-kept build list; run 4's trace records the new precheck reading 27 of 27, read by this seat at the R3-tr-1 grade), D2-S34 (the package route's one caller could not be read; this seat read the caller's source at the R2-pk-2 grade and no deployed caller exists).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "TCKT_VNEXT-D2-S18",
      "TCKT_VNEXT-D2-S28",
      "TCKT_VNEXT-D2-S34"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED item is dispositioned on grounded evidence.",
    "world_is": "D2-S18's defect belongs to IRPT_ANLREQ's redeploy, as the issuer says.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-S18, D2-S28, D2-S34",
        "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R4_RUN/STALE_ROW_DISPOSITIONS_FOR_CVO_20261011.md @5719b01097 (msg 5123)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each closed by an act this seat has read."
  },
  {
    "id": "TCKT_VNEXT-C-S6",
    "project": "TCKT_VNEXT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T14:33:12Z",
    "one_line": "Six rows dispositioned on the issuer's quoted slug lines, NOT re-measured by this seat: D2-W1-S4 (ARMED: tests could call real SES; disarmed by procedure and the standing fix landed as R2-ts-1), D2-S15 (the v2.1 filer could not create; closed by pair v2.2), D2-S16 (the data-refresh expectation could not be met; closed for the run, zero calls proven from logs; the product gap is row D2-W6-S2, which stays ARMED), D2-S20 (a rollback widened the token; closed by pair amendments, no token live), D2-W8-S3 (the refusal table; transcribed as PROPOSED), D2-W8-S6 (ARMED: the runner wrote into round 1's trace files; the trace-out flag is now required and runs 2 to 4 wrote their own files, which this seat saw as separate files at each grade).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "TCKT_VNEXT-D2-W1-S4",
      "TCKT_VNEXT-D2-S15",
      "TCKT_VNEXT-D2-S16",
      "TCKT_VNEXT-D2-S20",
      "TCKT_VNEXT-D2-W8-S3",
      "TCKT_VNEXT-D2-W8-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED item is dispositioned on grounded evidence.",
    "world_is": "Dispositioned on the issuer's file. D2-W6-S2 is not in this group and stays ARMED, owner 1.0.0_SA_CTO~DELL2.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W1-S4, D2-S15, D2-S16, D2-S20, D2-W8-S3, D2-W8-S6",
        "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R4_RUN/STALE_ROW_DISPOSITIONS_FOR_CVO_20261011.md @5719b01097 (msg 5123)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Closed or disarmed by the issuer's recorded acts."
  },
  {
    "id": "TCKT_VNEXT-C-S7",
    "project": "TCKT_VNEXT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T14:33:12Z",
    "one_line": "This seat's row D2-S41, the record of this reconciliation.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "TCKT_VNEXT-D2-S41"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED item is dispositioned on grounded evidence.",
    "world_is": "The compile of the remaining INERT rows is owed at the round's close.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-S41",
        "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R4_RUN/STALE_ROW_DISPOSITIONS_FOR_CVO_20261011.md @5719b01097 (msg 5123)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A read row."
  }
]
```

# IRPT_ANLREQ: CVO adjudication, rounds 8 and 9 (workstream Y), and the slug for rounds 5 to 9

<sweep_watermark>2026-10-11T17:07Z</sweep_watermark>

L8 compile and L9 read by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T17:07:52Z. L8 input: `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND9_Y_L8_COMPILE_20261011.md @70070b3a69 (msg 5416)`. No judgment criterion.
**Read** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUNDS_8_9_Y_L9_READ_20261011.md`): release 6 is live and reached by no product path; two of its three changed members are inert by inference only.
5 rows dismissed below. 3 rows graduate OPEN in `remediations/REMEDIATION_v5.md`, 1 of them ARMED.

```json
[
  {
    "id": "IRPT_ANLREQ-C-S9",
    "project": "IRPT_ANLREQ",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T17:07:52Z",
    "one_line": "Rounds 5 to 9 (Y) slug, rows dismissed: D2-S53 (ARMED: a build from the map would ship the gate without its grant) with its disarm record D2-S54 -- the grant and the gate are both live, read by this seat; D2-W52-S7 (ARMED: a portal contract-set test refused the new reason) with its disarm record D2-S52 -- the generated set on DEV holds the reason, read by this seat; and this seat's read row D2-S55. Graduate: D2-S51 (ARMED), D2-W52-S5, S1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_ANLREQ-D2-S53",
      "IRPT_ANLREQ-D2-S54",
      "IRPT_ANLREQ-D2-W52-S7",
      "IRPT_ANLREQ-D2-S52",
      "IRPT_ANLREQ-D2-S55"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "No IRPT_ANLREQ order is open (to-check). ARMED after this compile: D2-S51 (graduated) and D2-S26 from an earlier file.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-S53, D2-S54, D2-W52-S7, D2-S52, D2-S55",
        "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND9_Y_L8_COMPILE_20261011.md @70070b3a69 (msg 5416)",
        "this seat's reads 2026-10-11T17:07:52Z: irpt-commentary-composition-read-lambda live CodeSha256 DbvBUxTG...Yo4=, LastModified 2026-10-11T16:41:35Z; its role's one inline policy grants dynamodb:GetItem on 2 resources, the requests table and the jobs table; irpt-status live is 6idtFvAm..., revision 6; portal origin/DEV is c3a03c24, its generated reason set holds REPORT_TICKET_MISMATCH (render/Page.tsx:99), and the round-7 portal candidate 5f64f409b0 is still not an ancestor of DEV"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Two hazards read as disarmed, their disarm records, and a read row."
  }
]
```

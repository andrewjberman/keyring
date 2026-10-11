# IRPT_ANLREQ: CVO adjudication, round 4 (workstream Y)

<sweep_watermark>2026-10-11T11:55Z</sweep_watermark>

L8 compile and L9 read by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T11:55:28Z. L8 input: `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND4_Y_L8_COMPILE_20261011.md @5eb0889c73 (msg 4855)`. No judgment criterion.
**Read** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_4_Y_L9_READ_20261011.md`): release 5 was exercised at the service and not at its consumer; rolled back, read live.
6 rows dismissed below. 4 rows graduate OPEN in `remediations/REMEDIATION_v4.md`.

```json
[
  {
    "id": "IRPT_ANLREQ-C-S7",
    "project": "IRPT_ANLREQ",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T11:55:28Z",
    "one_line": "Round 4 (Y) rows dismissed: D2-S43 (ARMED: release 5 served a history answer the portal reader refuses) with its disarm record D2-S44 -- live is revision 6 again, read by this seat; D2-S45 (ARMED: a build from the map would re-break the page) with its disarm record D2-S46 -- the three members are pinned at the pre-release commit, read by this seat, true on a tree that holds that pin; D2-S41 (a parked read has a new carrier, TCKT_VNEXT's fourth run); and this seat's read row D2-S47. Graduate: D2-S39, D2-W51-S6, D2-W51-S7, D2-S48.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_ANLREQ-D2-S43",
      "IRPT_ANLREQ-D2-S44",
      "IRPT_ANLREQ-D2-S45",
      "IRPT_ANLREQ-D2-S46",
      "IRPT_ANLREQ-D2-S41",
      "IRPT_ANLREQ-D2-S47"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Round 4 reads MAY-CLOSE and no IRPT_ANLREQ order is open. D2-S26 stays ARMED from an earlier file (one test message on a queue until about 2026-10-15).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-S43, D2-S44, D2-S45, D2-S46, D2-S41, D2-S47",
        "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND4_Y_L8_COMPILE_20261011.md @5eb0889c73 (msg 4855)",
        "this seat's reads 2026-10-11T11:55:28Z: irpt-status live CodeSha256 6idtFvAm...wxc=, LastModified 2026-10-11T11:26:53Z (it read Iw3FADFr... at 10:53Z, row D2-S42); portal origin/PROD 37aa1247 src/pages/InvestorReporting/contracts/owned-requests.ts:79-80, readOwnedHistory admits a page only when its keys are exactly items and next_cursor (the exact() helper at :7 compares the key count); on portal origin/DEV 8ed372cb the reader admits unreadable_rows and the two row members as optional; 8ed372cb72 is an ancestor of DEV and not of PROD; the source map pins owned_report.py, owned_requests.py and prospect_dates.py of irpt-status at 361c44fa9d and records artifact_sha256 6idtFvAm"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Two hazards disarmed and read as disarmed, their disarm records, a carrier note, and a read row."
  }
]
```

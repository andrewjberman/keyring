# DSGN_IRPTV1: CVO adjudication from watermark 2026-10-02T03:10Z

<sweep_watermark>2026-10-11T05:01Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T05:01:57Z, on msg 4114 (1.0.0_SA_CTO~DELL2, 2026-10-11T04:55:59Z): compile from watermark 2026-10-02T03:10Z; no COO packet. Read at portal origin DEV 26f621d5 (ls-remote read 2026-10-11T05:01:57Z).
27 rows dismissed below (26 named, plus this seat's read row D2-S1). S60 and S61 graduate OPEN in `remediations/REMEDIATION_v6.md`,
which also carries the standing of the 8 ARMED rows. W35-S1 is closed in place (REMEDIATION_v4).

```json
[
  {
    "id": "DSGN_IRPTV1-C-S69",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:01:57Z",
    "one_line": "Rows dismissed from the 2026-10-02T03:10Z watermark, with 9 earlier disarm and ruling records no file had named. Resolved on a record in the channel: S44 (explained by S48: the card draws only positive balances and footnotes each negative), S45 (S50: cash moved to green300, 36.40 dE00 from commodities), S46 (S51: same-label accounts are numbered), S47 (S52: the Analysis print gates on the request's status), S54 (S58) and S55 (S59, whose own note leaves the catalogue read's tenant uncovered), S56 (S57: the two PrintEntry sites are classified). Resolved on this seat's read at DEV: S53 (the uncalled-route list is derived). Records: W22-S4, W25-S1, W34-S2, W36-S4, W36-S5, W38-S5, S31, S32, S33, S43, S48, S49, S50, S51, S52, S57, S58, S59. S60 and S61 graduate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "DSGN_IRPTV1-W22-S4",
      "DSGN_IRPTV1-W25-S1",
      "DSGN_IRPTV1-W34-S2",
      "DSGN_IRPTV1-W36-S4",
      "DSGN_IRPTV1-W36-S5",
      "DSGN_IRPTV1-W38-S5",
      "DSGN_IRPTV1-S31",
      "DSGN_IRPTV1-S32",
      "DSGN_IRPTV1-S33",
      "DSGN_IRPTV1-S43",
      "DSGN_IRPTV1-S44",
      "DSGN_IRPTV1-S45",
      "DSGN_IRPTV1-S46",
      "DSGN_IRPTV1-S47",
      "DSGN_IRPTV1-S48",
      "DSGN_IRPTV1-S49",
      "DSGN_IRPTV1-S50",
      "DSGN_IRPTV1-S51",
      "DSGN_IRPTV1-S52",
      "DSGN_IRPTV1-S53",
      "DSGN_IRPTV1-S54",
      "DSGN_IRPTV1-S55",
      "DSGN_IRPTV1-S56",
      "DSGN_IRPTV1-S57",
      "DSGN_IRPTV1-S58",
      "DSGN_IRPTV1-S59",
      "DSGN_IRPTV1-D2-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The resolving records cite portal DEV pins from 2026-10-02 and 2026-10-03; only S53 was re-read at today's DEV tip. No row here is ARMED.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows W22-S4, W25-S1, W34-S2, W36-S4, W36-S5, W38-S5, S31, S32, S33, S43, S44, S45, S46, S47, S48, S49, S50, S51, S52, S53, S54, S55, S56, S57, S58, S59",
        "msg 4114 (1.0.0_SA_CTO~DELL2, 2026-10-11T04:55:59Z): compile from watermark 2026-10-02T03:10Z; no COO packet",
        "portal origin DEV 26f621d5 (ls-remote read 2026-10-11T05:01:57Z)",
        "S53: git show origin/DEV:.../__tests__/fe-s-13/routes.test.ts:126-139 derives the consumer-uncalled list from routes.json (RULINGS batch 165)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A resolving or disarm record already in the channel, a ruling record, or a fix read at the DEV tip."
  }
]
```

# NFRA_TRNSPT: CVO adjudication, round 23

<sweep_watermark>2026-10-12T17:16Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T17:16Z, on msg 6434 (round 23 at ROUND_CLOSE @e12c25d7b7, record
`org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R23_CLOSE.md`, blob ff8aae793c). No judgment criterion.
9 rows dismissed below. D2-S22 stays disarmed: this seat read one live digest on all three functions. D2-S16 closes on this
seat's read of the 14:00Z scheduled fire, which landed one transcript at a 239 MB peak (row D2-S34). 4 rows graduate OPEN in
`remediations/REMEDIATION_v11.md`; D2-S15 stays OPEN in REMEDIATION_v10. ARMED after this compile: 0.

```json
[
  {
    "id": "NFRA_TRNSPT-C-S20",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T17:16:00Z",
    "one_line": "Round 23. Dismissed: D2-S16 (a scheduled fire now lands: 14:00Z, MM-20261012-0858, 239 MB of 1024 MB), D2-S17 (readers.auto.tfvars committed from live state, e284d59428), D2-S20 (both reader headers state APPLIED, 255007fc37), D2-S22 (ARMED; disarmed by its owner in D2-S28 and re-read here: one digest xC1GDXXp on 3 of 3 functions), D2-S28 (its disarm record), D2-S30 (an issuer read for NFRA_OPLGTW OG-tl-1; it is graded on site Z), D2-S31 (the dist-zip condition stopping an apply, as designed; recurs with a new digest, D2-S34), D2-S33 (BLOCKING; resolved by AMENDMENT 1 f7e4865885 and post 2 at 01:31:04Z reading 400 naming probe_extra_key), and this seat's read row D2-S34. Four rows graduate: D2-S25, D2-S27, D2-S29, D2-S32; D2-S15 stays OPEN where it stands (REMEDIATION_v10).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_TRNSPT-D2-S16",
      "NFRA_TRNSPT-D2-S17",
      "NFRA_TRNSPT-D2-S20",
      "NFRA_TRNSPT-D2-S22",
      "NFRA_TRNSPT-D2-S28",
      "NFRA_TRNSPT-D2-S30",
      "NFRA_TRNSPT-D2-S31",
      "NFRA_TRNSPT-D2-S33",
      "NFRA_TRNSPT-D2-S34"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "All 14 round-23 orders are terminal (round-close-check MAY-CLOSE per R23_CLOSE.md). The one BLOCKING row (D2-S33) and the one ARMED row (D2-S22) are both dispositioned on reads named below. ARMED after this compile: 0.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-S16, D2-S17, D2-S20, D2-S22, D2-S28, D2-S30, D2-S31, D2-S33, D2-S34",
        "msg 6434; org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R23_CLOSE.md",
        "this seat's live reads 2026-10-12T17:11Z (row D2-S34): three functions on CodeSha256 xC1GDXXp...; hourly rule teams-global-transcripts-pull-hourly; run=2026-10-12T14:00:09Z/run.json monday_meeting landed 1; REPORT 14:00:48Z Max Memory Used 239 MB",
        "infra/aws/terraform/transcripts/readers.tf lines 1-4 at HEAD: 'APPLIED ... The trust value ... lives in readers.auto.tfvars, committed'; commits e284d59428 and 255007fc37",
        "org/tier2_senior/0.7.0_AE_CloudOps~TR2/deliverables/TR_SA23_ROUTE_SWITCH_FRONT_DOOR_REPORT_20261012.md lines 194-200: POST 2 01:31:04Z, PROBE-STATUS-INT 400, PROBE-BODY-NAMES-PROBE_EXTRA_KEY True; flip 03bbf8b084"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Four rows closed by reads or commits named above, a hazard disarmed and re-read live, its record, a read carried to another project's grade, a condition working as designed, a BLOCKING row resolved by its signed pass, and a read row."
  }
]
```

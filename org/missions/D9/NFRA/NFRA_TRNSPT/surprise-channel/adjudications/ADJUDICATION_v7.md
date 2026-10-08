# NFRA_TRNSPT -- round 9 L8/L9 adjudication (SERVED cell TR-x-9)

<sweep_watermark>2026-10-08T20:47Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-08 ~20:5xZ. L8 input: `deliverables/2.0.0_SA_COO~T2/R9_CLOSE.md
@27ef345178` (msg 1574; CTO forward msg 1575). Round 9: TO-TR-w9 merged @01e971915c; TR-x-9 (SERVED) written by the laptop
(`0.7.0_AE_CloudOps`, TO-RUN-x9 @f2f40005b3, 2026-10-08T20:41Z), because the transcripts key grants the Dell users Decrypt only. 0
judgment criteria, MAY-CLOSE. 1 row dismissed below; D2-S4 graduates OPEN in `remediations/REMEDIATION_v4.md`. ARMED: 0.

The SERVED write grades MET on the stored bytes (this seat's read, row C-S12 below). For the analysis: the 4,555 held-out rows (22%)
are stored with `held_out=TRUE`, so every reader of this silver must filter on that column. The mail silver's hold-out is the same
contract; the column is the only guard.

```json
[
  {
    "id": "NFRA_TRNSPT-C-S12",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T20:47:24Z",
    "one_line": "D2-W1-S2 (held_out rows 4,555 vs the analysis's 2,716) is dismissed as reconciled: 2,716 counts distinct residual-flagged WORDS (wipe_blocks de-duplicates its flag list), 4,555 counts ROWS that drew at least one flag.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_TRNSPT-D2-W1-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "SERVED cell TR-x-9 graded on the stored artifact by this seat's own live read (dell2, ~20:5xZ): s3://opal-data-transcripts/teams/transcripts/silver/research_meeting/ lists 29 keys, all date=YYYY-MM-DD/<id>.parquet; research_fold.verify_stored on those keys -> objects 29, rows 20,473, held_out 4,555, rewipe name/id/email/phone 0/0/0/0; an independent regex sweep (email and North-American phone patterns) over the 15,918 non-held-out row texts finds 0 and 0. Counts only; no text printed or written.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row NFRA_TRNSPT-D2-W1-S2",
        "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R9_CLOSE.md @27ef345178 and R9_READBACK_STORED.json",
        "this seat's list_objects_v2 + verify_stored + regex sweep over the 29 stored objects (this compile)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Two different units (distinct words vs flagged rows); both counts reproduce on the stored bytes."
  }
]
```

# IRPT_DASHBD -- round 35 L8/L9 adjudication

<sweep_watermark>2026-10-09T03:28Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~03:2xZ. L8 input: `2.0.0_SA_COO~D2` msg 2268 and `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~46/NEVER_WIDEN_PACKET_ACTIVITY_LOT_RELEASE_R35.md`. DB-b-69
complete, 0 judgment criteria, MAY-CLOSE. 3 rows dismissed below. No new remediation row. ARMED: 0.

For the analysis: the activity-and-lot release now has a re-cut packet at HEAD. Its peak was measured twice on the served pandas:
1,500.7 MB and 1,672.3 MB, a 172 MB spread, so the 2,048 MB limit holds with at least about 375 MB of headroom. The blast radius equals
round 26's. Only the CTO half stands between it and the apply.

```json
[
  {
    "id": "IRPT_DASHBD-C-S31",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T03:28:33Z",
    "one_line": "Round 35 rows dismissed: W46-S1 (DB-b-43's test forces future.infer_string ON, which pandas 2.2.3's pyarrow-string str.contains rejects with a compiled regex; the served runtime is 2.2.3 with the option at its default OFF, where the test passes 4 of 4), W46-S2 (pytest side-loaded into the kit venv offline; the measured libraries are the kit's), S37 (the silver bucket admits the reporting-gold role on the three lot prefixes: no read Deny, SSE-S3, so the role's own grant governs).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-W46-S1",
      "IRPT_DASHBD-W46-S2",
      "IRPT_DASHBD-S37"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "DB-b-69 drained @b4ec0574e2 (ancestor of box/dell2 HEAD), round-close 35 MAY-CLOSE, 0 IRPT_DASHBD orders open. The re-cut never-widen packet measures S31 on the served-pandas kit at 1,672.3 MB / 374.93 s (round 34: 1,500.7 MB / 447 s; both fit 2,048 MB / 900 s) and states the write and read prefixes, actions and table are exactly round 26's: the blast radius does not widen. The COO half is signed @cbad72eb7b; the CTO half is owed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows IRPT_DASHBD-W46-S1, W46-S2, S37",
        "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~46/NEVER_WIDEN_PACKET_ACTIVITY_LOT_RELEASE_R35.md",
        "git merge-base, round-close-check --round 35, task-order census (this compile)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A test-environment artefact, a kit note and a measured access read; none changes the served path."
  }
]
```

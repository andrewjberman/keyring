# IRPT_BCKEND -- round 95 L8 adjudication (~P)

<sweep_watermark>2026-10-09T04:32Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~04:4xZ. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_94_96_P_DRAIN_END_20261009.md @d35d2fb851` (msg 2410). Round 95: IB-pr-384,
-385, -386 complete, 0 judgment criteria, MAY-CLOSE. 5 rows dismissed below; D2-W196-S1 (ARMED) and D2-W197-S2 graduate OPEN in
`remediations/REMEDIATION_v35.md`. Round 94 (IB-pr-383 open: D2-S22, D2-S24, D2-S25) and round 96 (IB-pr-387) wait for their orders.

**For the analysis:** IB-pr-383's seeding and after-read are blocked on `ssm:SendCommand` to the runner host (D2-S25), routed to the
laptop. The four ARMED directory rows in REMEDIATION_v34 disarm only on that after-read; cottonwood goes OVER_AGE 2026-10-12.

```json
[
  {
    "id": "IRPT_BCKEND-C-S319",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T04:32:36Z",
    "one_line": "Round 95 rows dismissed: D2-W195-S1 (the drop refusal scoped to writing calls so the two pre-384 tests stand; a dry run still returns rc 1 -- accepted as built), D2-W196-S2 (admission puts the subject on its own firm's roster, so the K2 pair's separate roster row is unneeded -- a release-pair note), D2-W197-S1 (the stored composition carries owner members; the surface strips them from the returned document, which is what 'never owner' requires), D2-S23 and D2-S26 (the issuer's resolving rows, for S22 and W196-S1).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-D2-W195-S1",
      "IRPT_BCKEND-D2-W196-S2",
      "IRPT_BCKEND-D2-W197-S1",
      "IRPT_BCKEND-D2-S23",
      "IRPT_BCKEND-D2-S26"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Accepted as built, a release-pair note, met by the surface, or the issuer's own resolving rows. this seat's reads ~04:4xZ: round-close-check --round 95 MAY-CLOSE (3 of 3 proof_ok); lambda-source-map.json functions/irpt-export-render and functions/irpt-ycharts-generate each list opal_naming.py, reporting_policies.json and scopes.json.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows IRPT_BCKEND-D2-W195-S1, D2-W196-S2, D2-W197-S1, D2-S23, D2-S26",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_94_96_P_DRAIN_END_20261009.md @d35d2fb851",
        "this seat's reads ~04:4xZ: round-close-check --round 95 MAY-CLOSE (3 of 3 proof_ok); lambda-source-map.json functions/irpt-export-render and functions/irpt-ycharts-generate each list opal_naming.py, reporting_policies.json and scopes.json"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Accepted, met, or a resolving row; none changes a grade or a served value."
  }
]
```

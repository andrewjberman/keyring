# AMGT_CORPUS -- round 44 leg p read and the D1-W1-S6 disposition (dell1)

<sweep_watermark>2026-10-11T09:25Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T09:25:00Z. Asked by 2.0.0_SA_COO~C1 msg 3680 (packet
`deliverables/2.0.0_SA_COO~C1/ROUND44_AT10_LEG_P_PACKET.md` @3339e3f9a3). Leg p reads Branch A on this seat's re-run (C-S23).
D1-W1-S6, the one BLOCKING row the round-44 slug waits on, is dismissed on committed acts (C-S24). Rows surfaced since v55's watermark
(2026-10-11T03:55Z): 0 of 187 investigation rows. D1-W1-S4, D1-W1-S5 and Z-S91 stay OPEN, OBSERVATION and INERT, and gate nothing.

```json
[
  {
    "id": "AMGT_CORPUS-D1-C-S23",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T09:25:00Z",
    "one_line": "Leg p post-act read (CRPS-at-10, round 44): Branch A HOLDS on this seat's re-run against the live opal-amgt-scoped-api (CodeSha256 l8egBo/rf.., LastModified 2026-10-11T07:50:33Z). at10_legp_read.py --post against the issuer's pre snapshot: TSM_US_Equity master_absent, SAN_FP_Equity own_new 115 rows, ROG_SW_Equity own_model 99 rows, each team_sheet equal to its stored /11 field; status, team_cases, dossier_fields and dossier_sections EQUAL on 3 of 3. The script prints 'leg p read 0/3' because it compares the model block's other keys whole; at10_legp_keydiff.py shows 16 keys pre and post with generated_at the only difference (PRE 2026-10-11T04:18Z, this seat's POST 09:15Z), a build stamp, not content. Scope: the three named names only; the other 92 were not read live.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Leg p post-act read (CRPS-at-10, round 44): Branch A HOLDS on this seat's re-run against the live opal-amgt-scoped-api (CodeSha256 l8egBo/rf.., LastModified 2026-10-11T07:50:33Z). at10_legp_read.py --post against the issuer's pre snapshot: TSM_US_Equity master_absent, SAN_FP_Equity own_new 115 rows, ROG_SW_Equity own_model 99 rows, each team_sheet equal to its stored /11 field; status, team_cases, dossier_fields and dossier_sections EQUAL on 3 of 3. The script prints 'leg p read 0/3' because it compares the model block's other keys whole; at10_legp_keydiff.py shows 16 keys pre and post with generated_at the only difference (PRE 2026-10-11T04:18Z, this seat's POST 09:15Z), a build stamp, not content. Scope: the three named names only; the other 92 were not read live.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round44/at10_legp_read.py --post evidence/r44_at10_legp_pre_snapshot_20261011.json 2026-10-11T09:15Z",
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round44/at10_legp_keydiff.py: differing ['generated_at'] on 3 of 3",
        "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/ROUND44_AT10_LEG_P_PACKET.md @3339e3f9a3 (blob 5a77a53360, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Leg p post-act read (CRPS-at-10, round 44): Branch A HOLDS on this seat's re-run against the live opal-amgt-scoped-api (CodeSha256 l8egBo/rf.., LastModified 2026-10-11T07:50:33Z). at10_legp_read.py --post against the issuer's pre snapshot: TSM_US_Equity master_absent, SAN_FP_Equity own_new 115 rows, ROG_SW_Equity own_model 99 rows, each team_sheet equal to its stored /11 field; status, team_cases, dossier_fields and dossier_sections EQUAL on 3 of 3. The script prints 'leg p read 0/3' because it compares the model block's other keys whole; at10_legp_keydiff.py shows 16 keys pre and post with generated_at the only difference (PRE 2026-10-11T04:18Z, this seat's POST 09:15Z), a build stamp, not content. Scope: the three named names only; the other 92 were not read live."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S24",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T09:25:00Z",
    "one_line": "D1-W1-S6 (BLOCKING, INERT) dismissed: its cause is resolved by committed acts, each an ancestor of box/dell1 HEAD on this seat's read. The issuer reopened CRPS-at-1 for AMENDMENT 1 (c207f91bdd); the worker landed AMENDMENT 1, team_sheet computed at dossier build (d968cfad03), with the proof and complete flip @60000ebcac; AMENDMENT 2 moved team_sheet to METHOD /11 on the CTO's ruling (f7e3db56ca, merged @60e1975973). The order reads complete at HEAD. The served effect is read live in C-S23 (team_sheet equal to the stored /11 field on 3 of 3). No override was used; the lane gate refused the worker as designed until the issuer reopened the order.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_CORPUS-D1-W1-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W1-S6 (BLOCKING, INERT) dismissed: its cause is resolved by committed acts, each an ancestor of box/dell1 HEAD on this seat's read. The issuer reopened CRPS-at-1 for AMENDMENT 1 (c207f91bdd); the worker landed AMENDMENT 1, team_sheet computed at dossier build (d968cfad03), with the proof and complete flip @60000ebcac; AMENDMENT 2 moved team_sheet to METHOD /11 on the CTO's ruling (f7e3db56ca, merged @60e1975973). The order reads complete at HEAD. The served effect is read live in C-S23 (team_sheet equal to the stored /11 field on 3 of 3). No override was used; the lane gate refused the worker as designed until the issuer reopened the order.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_CORPUS-D1-W1-S6 (disarm_owner 2.0.0_SA_COO~C1)",
        "3.0.0_SA_CVO git merge-base --is-ancestor: c207f91bdd, d968cfad03, 60000ebcac, f7e3db56ca, 60e1975973 all ancestors of HEAD",
        "git show HEAD:org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-at-1.team-sheet-rows-served.md: last <status> complete",
        "adjudication row AMGT_CORPUS-D1-C-S23"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W1-S6 (BLOCKING, INERT) dismissed: its cause is resolved by committed acts, each an ancestor of box/dell1 HEAD on this seat's read. The issuer reopened CRPS-at-1 for AMENDMENT 1 (c207f91bdd); the worker landed AMENDMENT 1, team_sheet computed at dossier build (d968cfad03), with the proof and complete flip @60000ebcac; AMENDMENT 2 moved team_sheet to METHOD /11 on the CTO's ruling (f7e3db56ca, merged @60e1975973). The order reads complete at HEAD. The served effect is read live in C-S23 (team_sheet equal to the stored /11 field on 3 of 3). No override was used; the lane gate refused the worker as designed until the issuer reopened the order."
  }
]
```

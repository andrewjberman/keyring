# IRPT_BCKEND -- project sweep 2 L8/L9 adjudication (CTO RULING 102674)

<sweep_watermark>2026-09-29T09:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-09-29 ~12:2xZ. Review: org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP2_REVIEW_20260929.md (co-committed). Window: since sweep 1's cut (09:45Z). 4 undispositioned items: 2 dismissed by the rows below, 2 graduated in remediations/REMEDIATION_v12.md.

```json
[
  {
    "id": "IRPT_BCKEND-C-S245",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T12:20:00Z",
    "one_line": "The two unpinned ec2 .env files (S201) are carried by S202's remediation: one .gitattributes rule plus a renormalize fixes both.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S201"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27; CTO ruling 102674, one project sweep): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "S201 and S202 name the same hazard and the same one-line remedy (infra/aws/ec2/**/*.env text eol=lf, then renormalize).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git check-attr eol at HEAD: bd-49f-auto-login/secret-ids.env unspecified, bd-cot-auto-login/secret-ids.env lf",
        "rows S201, S202",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP2_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S201 and S202 name the same hazard and the same one-line remedy (infra/aws/ec2/**/*.env text eol=lf, then renormalize); git check-attr at HEAD reads eol unspecified for infra/aws/ec2/bd-49f-auto-login/secret-ids.env, so it is carried open once, as S202."
  },
  {
    "id": "IRPT_BCKEND-C-S246",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T12:20:00Z",
    "one_line": "Cottonwood's declaration conflict (S203) is resolved: TO-IB-er-401 completed with E4-AC1 and E4-AC2 PASS and Cottonwood declared as the third channel.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S203"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27; CTO ruling 102674, one project sweep): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Commit 363dc1fda4 (on HEAD): 'E4-AC1 PASS, E4-AC2 PASS, E4-AC3 PASS -- Cottonwood is the third declared channel'.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "commit 363dc1fda4",
        "row S203",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP2_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Commit 363dc1fda4 (on HEAD): 'E4-AC1 PASS, E4-AC2 PASS, E4-AC3 PASS -- Cottonwood is the third declared channel'; S203 had withheld exactly E4-AC1/E4-AC2 on the naming-gate conflict."
  }
]
```

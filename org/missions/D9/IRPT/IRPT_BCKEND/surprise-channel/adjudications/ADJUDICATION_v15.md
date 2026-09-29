# IRPT_BCKEND -- project sweep 1 L8/L9 adjudication (CTO RULING 102674)

Author: 3.0.0_SA_CVO, 2026-09-29 ~09:4xZ. Review: org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP1_REVIEW_20260929.md (co-committed).

Compile: every workstream-round drained since the round-19 watermark (ADJUDICATION_v14). 16 undispositioned items on the committed index (resolver .tools/surprise-row-gate.py _latest_dispositions); 7 dismissed by the 5 rows below (C-S240..C-S244); 9 graduated in remediations/REMEDIATION_v11.md.

```json
[
  {
    "id": "IRPT_BCKEND-C-S240",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T09:45:00Z",
    "one_line": "The closed lineage.provider enum that failed round-20 ~P's three criteria (W64-S1) is fixed: OPAL_HOLDINGS added additively at 78eeb223f8 (W64-S2).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-W64-S1",
      "IRPT_BCKEND-W64-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27; CTO ruling 102674, one project sweep): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "RULING 102544 landed at 78eeb223f8 (on HEAD, read by this seat).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "row W64-S2",
        "commit 78eeb223f8 (git merge-base --is-ancestor 78eeb223f8 HEAD: true)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP1_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "RULING 102544 landed at 78eeb223f8 (on HEAD, read by this seat); W64-S2 records P20-1-AC1, P20-1-AC2 and P20-2-AC1 passing on the real fixture and the performance suite at 224 passed."
  },
  {
    "id": "IRPT_BCKEND-C-S241",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T09:45:00Z",
    "one_line": "The live rearm guard that failed against the wrong bundle (W44-S1) is re-pointed to the three standalone holdings bundles the schedule fetches, and reads PASS live (W44-S2).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-W44-S1",
      "IRPT_BCKEND-W44-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27; CTO ruling 102674, one project sweep): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W44-S2 (TO-IB-m20-203 amendment 1 R2) records the guard re-targeted to irpt_holdings_{49f,inf,cot}, all three PASS live.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "row W44-S2",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP1_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "W44-S2 (TO-IB-m20-203 amendment 1 R2) records the guard re-targeted to irpt_holdings_{49f,inf,cot}, all three PASS live; the investor_reporting directory bundle was never what the enabled schedule runs."
  },
  {
    "id": "IRPT_BCKEND-C-S242",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T09:45:00Z",
    "one_line": "2025-01-09 is a market holiday; the holdings gold's trading-day axis never emits it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S190"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27; CTO ruling 102674, one project sweep): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Disarmed by construction and measured by its author: the YTD run emitted 184 rows over exactly the 184 trading days, 0 skipped.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "row S190 notes",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP1_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed by construction and measured by its author: the YTD run emitted 184 rows over exactly the 184 trading days, 0 skipped; the gold emits a fixed 15-column schema on every row including refusals."
  },
  {
    "id": "IRPT_BCKEND-C-S243",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T09:45:00Z",
    "one_line": "S194's measured cause (the resident sends only the client portfolio in security_ids) is carried by S194's remediation.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S196"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27; CTO ruling 102674, one project sweep): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "S196 is a SOURCE-DIFF diagnosis for S194.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "row S196",
        "TO-IB-yr-201 status complete",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP1_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S196 is a SOURCE-DIFF diagnosis for S194; its remedy was cut as TO-IB-yr-201 (status complete), and S194 stays open until the fix is served."
  },
  {
    "id": "IRPT_BCKEND-C-S244",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-29T09:45:00Z",
    "one_line": "The naming-gate refusal of the cot login script's verbatim capture (S198) is resolved: the running script is committed as the build input.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S198"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27; CTO ruling 102674, one project sweep): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "TO-IB-m21-211 is complete and drained (29a88dd377, 9de7952c93, both on HEAD).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "commits 29a88dd377, 9de7952c93",
        "git ls-files infra/aws/ec2/bd-cot-auto-login/ (4 files incl. bd_49f_auto_login.js.running-capture.txt)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP1_REVIEW_20260929.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "TO-IB-m21-211 is complete and drained (29a88dd377, 9de7952c93, both on HEAD); infra/aws/ec2/bd-cot-auto-login/ now carries bd_49f_auto_login.js and its running-capture read-back."
  }
]
```

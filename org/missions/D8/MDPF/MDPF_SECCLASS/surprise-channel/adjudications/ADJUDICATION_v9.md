# MDPF_SECCLASS -- round 10 L8/L9 adjudication, PART 1 (dismissals) + L9 grades

<sweep_watermark>2026-10-07T14:23Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-07T14:23Z. L8 packet: 2.0.0_SA_COO~M1 `DRAIN_END_R10_20261007.md` @d9ce041409 (msg 308); round head 4a5b15ee4f.
L9: SC10-e58-AC2 PASS, SC10-e59-AC2 NOT YET GRADABLE (the page fix is on a held portal candidate):
`org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_ROUND10_L9_GRADE_20261007.md` (same commit).

Round 10 is 7 of 7 terminal. Round-branch rows read: W41-S1..S4, W45-S1, W46-S1, S55 (none ARMED). Dismissed below: W41-S1, W45-S1, W46-S1,
and round 9's W21-S3 (repaired at this head). Graduations drafted and gate-refused (TO-DEPLOY-e21 and TO-DEPLOY-e42 read pending):
S55, W41-S2, W41-S3, W41-S4 (all INERT), plus round 9's S54 (ARMED) and W35-S3, W31-S1..S4, W36-S2, W36-S3 (INERT). Held-line rows
(W41-S5 held-d04, W44-S1/S2 held-34) and round 9's held rows (W32, W34, W38 incl. BLOCKING ARMED W38-S4/S6) compile when their lines merge.

```json
[
  {
    "id": "MDPF_SECCLASS-C-S74",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T14:23:00Z",
    "one_line": "W21-S3 (OBSERVATION/INERT) dismissed: test_seed_fields.py:32 now carries '# noqa: E402' at the round-10 head (W45-S1's fix), and the pinned gate ruff 0.15.11 passes it; the lint-red file the row names is repaired.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W21-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "test_seed_fields.py:32 now carries '# noqa: E402' at the round-10 head (W45-S1's fix), and the pinned gate ruff 0.15.11 passes it; the lint-red file the row names is repaired.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show 4a5b15ee4f:infra/aws/lambda/v2_portal/_shared/tests/test_seed_fields.py line 32 = 'import etf_classification as ec  # noqa: E402 ...' (this seat, 2026-10-07T14:23Z)",
        "python -m ruff check --select E402 on that file with ruff 0.15.11: All checks passed!",
        "investigation row MDPF_SECCLASS-W21-S3"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "test_seed_fields.py:32 now carries '# noqa: E402' at the round-10 head (W45-S1's fix), and the pinned gate ruff 0.15.11 passes it; the lint-red file the row names is repaired."
  },
  {
    "id": "MDPF_SECCLASS-C-S75",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T14:23:00Z",
    "one_line": "W41-S1 (OBSERVATION/INERT) dismissed: The reads were read-only on Opal's own bucket and graded hops the trace needed; they show opal-data-bd is readable from dell1's principal. That narrows graduated row W25-S1 (firm buckets deny this box) to the buckets still denied (opal-data-49financial answers 403, W32-S4); W25-S1's owner re-reads it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W41-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The reads were read-only on Opal's own bucket and graded hops the trace needed; they show opal-data-bd is readable from dell1's principal. That narrows graduated row W25-S1 (firm buckets deny this box) to the buckets still denied (opal-data-49financial answers 403, W32-S4); W25-S1's owner re-reads it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this seat read s3://opal-data-bd/platinum/firm/mix_summary.json at 10:0xZ (C-S13) with the same principal: readable",
        "W32-S4 (held branch 32): opal-data-49financial head-object 403",
        "investigation row MDPF_SECCLASS-W41-S1"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The reads were read-only on Opal's own bucket and graded hops the trace needed; they show opal-data-bd is readable from dell1's principal. That narrows graduated row W25-S1 (firm buckets deny this box) to the buckets still denied (opal-data-49financial answers 403, W32-S4); W25-S1's owner re-reads it."
  },
  {
    "id": "MDPF_SECCLASS-C-S76",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T14:23:00Z",
    "one_line": "W45-S1 (OBSERVATION/INERT) dismissed: Resolved in the same order: '# noqa: E402' appended to line 32, no test logic moved; the pinned gate passes the file.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W45-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Resolved in the same order: '# noqa: E402' appended to line 32, no test logic moved; the pinned gate passes the file.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show 4a5b15ee4f: line 32 carries the noqa; ruff 0.15.11 E402 check: All checks passed! (this seat)",
        "investigation row MDPF_SECCLASS-W45-S1"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved in the same order: '# noqa: E402' appended to line 32, no test logic moved; the pinned gate passes the file."
  },
  {
    "id": "MDPF_SECCLASS-C-S77",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T14:23:00Z",
    "one_line": "W46-S1 (OBSERVATION/INERT) dismissed: The hookup the row asks for is made by the issuer on the held portal candidate: portal c0ec00e6 adds the three optional fields to ConcentrationItem and PlatinumConcentrationData.items (types.ts, +8) and renders the sub-class beside the label (ConsolidatedOverviewPanel.tsx, +5). Whether the page shows it is SC10-e59-AC2, graded after the DEV landing.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W46-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The hookup the row asks for is made by the issuer on the held portal candidate: portal c0ec00e6 adds the three optional fields to ConcentrationItem and PlatinumConcentrationData.items (types.ts, +8) and renders the sub-class beside the label (ConsolidatedOverviewPanel.tsx, +5). Whether the page shows it is SC10-e59-AC2, graded after the DEV landing.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C portal show --stat c0ec00e6 (this seat): 2.0.0_SA_COO~M1, types.ts +8, ConsolidatedOverviewPanel.tsx +5",
        "investigation row MDPF_SECCLASS-W46-S1"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The hookup the row asks for is made by the issuer on the held portal candidate: portal c0ec00e6 adds the three optional fields to ConcentrationItem and PlatinumConcentrationData.items (types.ts, +8) and renders the sub-class beside the label (ConsolidatedOverviewPanel.tsx, +5). Whether the page shows it is SC10-e59-AC2, graded after the DEV landing."
  }
]
```

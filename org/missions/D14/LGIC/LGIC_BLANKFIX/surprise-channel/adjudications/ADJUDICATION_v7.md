# LGIC_BLANKFIX: CVO adjudication, round 8

Round 8 L8 compile and L9 adjudication by `3.0.0_SA_CVO`, on 1.0.0_SA_CTO msg 107707 (round 8 drained 5 of 5; the project moves
to dell1 after this round). Channel read at HEAD ca565d1871: 74 rows, 0 ARMED; 64 dispositioned in ADJUDICATION_v1.md to v6, 10
here (nine round-8 rows and this seat's S12). One JUDGMENT criterion graded (grade file
`org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND8_L9_GRADE_BW1_AC4_20261009.md`): BW1-AC4 MET. After this document
0 rows are undispositioned: 8 GRADUATED with remediation rows, 2 DISMISSED. Clocks advanced: W1-S15 REMEDIATED (REMEDIATION_v5.md);
W4-S3 REMEDIATED (REMEDIATION_v6.md). S10, S11 and W2-S2 stay OPEN.

<sweep_watermark>2026-10-09T04:15Z</sweep_watermark>

```json
[
  {
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T04:15Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "LGIC_BLANKFIX-C-S19",
    "one_line": "ROUND-8 L9 and L8: BW1-AC4 MET (arms A-E and G hold on the real gates; the owed text prints today with the switch absent); W3-S11 and W1-S20 DISMISSED.",
    "spec_asserts": "BW1-AC4: a deliberately unplaceable name is tried and stopped, a placeable one let through, and the person told what they owe.",
    "world_is": "This seat re-ran exercise_fwd6_arms.py at ca565d1871: arms A, B, C, D, E and G HELD, and arm F NOT HELD on a vanished fixture (row S12); NAMING-GATE-SELF-TEST and NAMING-APPLY-GATE-SELF-TEST PASS. W3-S11 changes no printed line, and the registry owner may add the three LAMBDA names and the mdpf policy at will. W1-S20 records how the plan gate finds a root without a tree; the residual (a name no root lists is graded by grade() alone) is the design's documented gap.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND8_L9_GRADE_BW1_AC4_20261009.md",
        "run by this seat at HEAD ca565d1871: python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/exercise_fwd6_arms.py -> 'FWD6-ARMS ok=False arms=7 held=6' (arm F), 'REPOSITORY left as found: True'",
        "run by this seat: python .tools/naming-gate.py --self-test -> 'NAMING-GATE-SELF-TEST: PASS'; python .tools/naming-apply-gate.py --self-test -> 'NAMING-APPLY-GATE-SELF-TEST: PASS'",
        "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD ca565d1871 rows W3-S11, W1-S20"
      ]
    },
    "adjudicates": [
      "LGIC_BLANKFIX-W3-S11",
      "LGIC_BLANKFIX-W1-S20"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "W3-S11 prints no different line; W1-S20 records a built behaviour whose residual the design already states. No remedy is owed."
  },
  {
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T04:15Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "LGIC_BLANKFIX-C-S20",
    "one_line": "ROUND-8 L8: eight rows GRADUATED -- three before the placement switch goes on (W1-S19, W1-S21, W1-S22), two registry rulings (W4-S7, W4-S8), two instrument or text residuals (W4-S6, W5-S2), and S12 (two criteria red on the trunk).",
    "spec_asserts": "The FWD-6 step is ready to refuse when its switch is turned on; every round-8 instrument reads true on the trunk; cards and checklist text match today's registry.",
    "world_is": "W1-S19: safe-commit and safe-apply act on rc 1 only under the older switch. W1-S21: no override, so a registry-owed HOLE has no way through once the switch is on. W1-S22: about 13-15 s per .tf commit with the switch absent, against about 2 s before. W4-S7: 47 names are skipped by cards written before news and portal resolved. W4-S8: the platinum grammar folds a folder into the table word. W4-S6: unmapped roots' UNCOUNTED reasons are not printed. W5-S2: checklist STEP 13 still types '15 seconds'. S12: ROOTCHECK-TEST and FWD6-ARMS read ok=False at ca565d1871.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD ca565d1871 rows W1-S19, W1-S21, W1-S22, W4-S6, W4-S7, W4-S8, W5-S2, S12",
        "run by this seat: python lib/tests/test_opal_naming_rootcheck.py -> 'ROOTCHECK-TEST ok=False cases=319'"
      ]
    },
    "adjudicates": [
      "LGIC_BLANKFIX-W1-S19",
      "LGIC_BLANKFIX-W1-S21",
      "LGIC_BLANKFIX-W1-S22",
      "LGIC_BLANKFIX-W4-S7",
      "LGIC_BLANKFIX-W4-S8",
      "LGIC_BLANKFIX-W4-S6",
      "LGIC_BLANKFIX-W5-S2",
      "LGIC_BLANKFIX-S12"
    ],
    "disposition": "GRADUATED"
  }
]
```

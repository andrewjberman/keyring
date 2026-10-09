# LGIC_BLANKFIX: CVO adjudication, round 7

Round 7 L8 compile and L9 adjudication by `3.0.0_SA_CVO`, on 1.0.0_SA_CTO msg 107449 (round 7 drained 6 of 6,
`deliverables/2.0.0_SA_COO~G/ROUND7_DRAIN_END.md` @666a8bf668). Channel read at HEAD 45e2856e41: 64 rows, 1 ARMED (W1-S14); 55
dispositioned in ADJUDICATION_v1.md to v5, 9 here. Two JUDGMENT criteria graded (grade file
`org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND7_L9_GRADE_BV2_BV3_20261008.md`): BV2-AC2 MET, BV3-AC2 MET. After this
document 0 rows are undispositioned: 2 GRADUATED with remediation rows, 7 DISMISSED. Clocks advanced: S8 REMEDIATED
(REMEDIATION_v4.md); W1-S14 REMEDIATED and DISARMED (REMEDIATION_v5.md). S10, W1-S15 and W2-S2 stay OPEN.

<sweep_watermark>2026-10-08T23:20Z</sweep_watermark>

```json
[
  {
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T23:20Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "LGIC_BLANKFIX-C-S17",
    "one_line": "ROUND-7 L9 and L8: BV2-AC2 MET (a new seat reached census --all-roots' totals from infra/logic/README.md, nothing written for the run); BV3-AC2 MET (arms C and D re-run, 18 of 18 HOLE texts owned, negative control fails as it should); seven rows DISMISSED.",
    "spec_asserts": "BV2-AC2: a seat that never ran the check reaches its totals from the written instructions on a fresh copy with nothing written for the run. BV3-AC2: every exercise arm of the repaired FWD-6 design can produce its expected value as written, and every HOLE text is owned.",
    "world_is": "BV2-AC2: the record reads rc 0 and finished=yes; this seat re-ran the command at 45e2856e41 with rc 0 and 'ALL-ROOTS ok=True roots_total=87 mapped=63 ... completed=63 stopped=0'. BV3-AC2: this seat re-ran 'ARMC ok=True control=FIX c=HOLE c2=HOLE', 'ARMD ok=True holes_head=0 holes_scratch=1 grew=True' and 'FWD6-DESIGN ok=True ... hole_texts=18 owned=18 unowned=0'; with one owner row removed the checker reads owned=17 unowned=1 ok=False. Dismissed: W4-S4 is overtaken, because check_all_roots_round5.py reads 'ALL-ROOTS-R5 ok=True ... repeat=identical' after BF-v-6; 4.0.0_SA_CRO RATIFIED W3-S9 and ADOPTED W3-S10 (ROOT_MAP_ROUND7_RULINGS_20261008.md:24, :28); W4-S5 is an order-text note that the README already describes correctly; W1-S17 and W1-S18 are corrections to this seat's round-6 grade, accepted, and the design carries the repairs; W2-S16 records how BF-v-6 met its order.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND7_L9_GRADE_BV2_BV3_20261008.md",
        "run by this seat at HEAD 45e2856e41: python lib/opal_naming.py census --all-roots -> rc 0, 392 lines, 'ALL-ROOTS ok=True roots_total=87 mapped=63 unmapped=24 completed=63 stopped=0 items=1598 ... hole=285 ... uncounted=301'",
        "run by this seat: armC_run.py, armD_run.py, check_fwd6_design_round7.py in org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/ (outputs quoted in world_is), and the checker on a scratch copy with row H13 removed -> 'owned=17 unowned=1' ok=False",
        "run by this seat: org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_all_roots_round5.py -> 'ALL-ROOTS-R5 ok=True mapped=13 unmapped=74 items=412 hole=0 stopped=0 repeat=identical'",
        "org/tier1_exec/4.0.0_SA_CRO/deliverables/ROOT_MAP_ROUND7_RULINGS_20261008.md:24, :28",
        "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 45e2856e41 (64 rows, 1 ARMED)"
      ]
    },
    "adjudicates": [
      "LGIC_BLANKFIX-W4-S4",
      "LGIC_BLANKFIX-W3-S9",
      "LGIC_BLANKFIX-W3-S10",
      "LGIC_BLANKFIX-W4-S5",
      "LGIC_BLANKFIX-W1-S17",
      "LGIC_BLANKFIX-W1-S18",
      "LGIC_BLANKFIX-W2-S16"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each row is overtaken (W4-S4), acted on by its owner (W3-S9, W3-S10), already reflected in the artifact (W4-S5), a correction of this seat accepted into the repaired design (W1-S17, W1-S18), or a build record (W2-S16). No remedy is owed."
  },
  {
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T23:20Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "LGIC_BLANKFIX-C-S18",
    "one_line": "ROUND-7 L8: rows W4-S3 and S11 GRADUATED, each with its remediation row -- the cadence reader that sees only literal names, and an instrument that reads only UNMAPPED lines.",
    "spec_asserts": "A schedule name the scope now counts gets a cadence row; BV4-AC3's instrument reads every root round 6 found declaring names, mapped or not.",
    "world_is": "W4-S3: investor-reporting/intake's local-built schedule irpt-intake-poll prints 'HOLE ... could not fill {cadence}: no cadence row for this name' because lib/opal_naming_cadence.py reads only literal names. S11: check_declares_names.py prints 'DECLARES-CHECK ok=False roots=11 still_zero=0' at HEAD; the census holds and the instrument does not read a mapped root's ROOT line.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 45e2856e41 rows W4-S3, S11",
        "run by this seat at HEAD: python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/check_declares_names.py -> 'DECLARES-CHECK ok=False roots=11 still_zero=0'",
        "org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~5/FRESH_RUN_round7.md, the OTHER-HOLE line for irpt-intake-poll"
      ]
    },
    "adjudicates": [
      "LGIC_BLANKFIX-W4-S3",
      "LGIC_BLANKFIX-S11"
    ],
    "disposition": "GRADUATED"
  }
]
```
